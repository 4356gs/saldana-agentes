#!/usr/bin/env python3
"""Embudo comercial de Saldaña Digital: métricas, estado por cuenta, higiene y criterio de corte.

Uso:
  python3 herramientas/pipeline.py                        resumen del embudo y alertas
  python3 herramientas/pipeline.py --json                 resumen en JSON
  python3 herramientas/pipeline.py --cuenta ID            historial y estado de una cuenta
  python3 herramientas/pipeline.py --puede-contactar ID   SÍ / NO con motivo (sale con 1 si NO)
  python3 herramientas/pipeline.py --verificar            valida el archivo y que solo haya crecido

Fuente: estado/pipeline.csv (una fila por evento; solo se añaden filas) y estado/parametros.json.

Columnas:
  fecha           AAAA-MM-DD del evento
  id              EV-0001 consecutivo
  cuenta_id       slug en minúsculas con guiones (bodegas-albamar)
  cuenta          nombre legible
  vertical        uno de parametros.verticales, u "otro"
  municipio       texto libre (puede ir vacío)
  canal           email_frio | derivacion | institucional | presencial | red | web | desconocido
  evento          ver EVENTOS
  detalle         texto libre, sin datos de salud
  experimento     EXP-## si aplica
  ref             confirmación del CEO (bandeja AAAA-MM-DD / APR-###) o id corregido (correccion)
  registrado_por  quien escribe la fila (desarrollo-negocio, o carga-inicial)

Un error se corrige con una fila "correccion" cuyo ref es el id erróneo; la fila errónea deja de contar.
Solo usa la biblioteca estándar de Python.
"""
import argparse
import csv
import json
import re
import subprocess
import sys
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path

try:
    from zoneinfo import ZoneInfo
except ImportError:  # Python < 3.9
    ZoneInfo = None

RAIZ = Path(__file__).resolve().parent.parent
PARAMS = RAIZ / "estado" / "parametros.json"
PIPELINE = RAIZ / "estado" / "pipeline.csv"

COLUMNAS = ["fecha", "id", "cuenta_id", "cuenta", "vertical", "municipio", "canal",
            "evento", "detalle", "experimento", "ref", "registrado_por"]
EVENTOS = ["identificada", "cualificada", "contacto", "seguimiento", "respuesta",
           "conversacion", "diagnostico_enviado", "propuesta", "loi_enviada",
           "loi_firmada", "pago", "descartada", "no_contactar", "reactivada",
           "nota", "correccion"]
TOQUES = {"contacto", "seguimiento"}
BLOQUEOS = {"descartada", "no_contactar"}
CONFIRMADOS_POR_CEO = {"contacto", "seguimiento", "respuesta", "conversacion",
                       "loi_firmada", "pago"}
CANALES = {"email_frio", "derivacion", "institucional", "presencial", "red", "web",
           "desconocido"}
CARGA_INICIAL = "carga-inicial"
EMBUDO = [("cualificada", "cualificadas"), ("contactada", "contactadas"),
          ("respuesta", "respondieron"), ("conversacion", "conversaciones"),
          ("diagnostico_enviado", "diagnósticos"), ("propuesta", "propuestas"),
          ("loi_enviada", "LOI enviadas"), ("loi_firmada", "LOI firmadas"),
          ("pago", "pagos")]
RE_ID_CUENTA = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
RE_ID_EVENTO = re.compile(r"^EV-\d{4,}$")
RE_RELLENO = re.compile(r"\[[^\]]*\]|XXX")


def cargar_parametros():
    with PARAMS.open(encoding="utf-8") as f:
        return json.load(f)


def es_pendiente(valor):
    return valor is None or (isinstance(valor, str) and "PENDIENTE" in valor.upper())


def hoy(params):
    zona = params.get("zona_horaria")
    if ZoneInfo and zona:
        try:
            return datetime.now(ZoneInfo(zona)).date()
        except Exception:
            pass
    return date.today()


def a_fecha(txt):
    return datetime.strptime(txt.strip(), "%Y-%m-%d").date()


def leer():
    with PIPELINE.open(encoding="utf-8", newline="") as f:
        lector = csv.DictReader(f)
        return lector.fieldnames or [], list(lector)


def vigentes(filas):
    """Filas que cuentan: sin las corregidas ni las propias correcciones."""
    corregidas = {(f.get("ref") or "").strip() for f in filas
                  if (f.get("evento") or "").strip() == "correccion"}
    return [f for f in filas
            if (f.get("evento") or "").strip() != "correccion"
            and (f.get("id") or "").strip() not in corregidas]


def por_cuenta(filas):
    cuentas = defaultdict(list)
    for f in filas:
        cuentas[f["cuenta_id"].strip()].append(f)
    for lista in cuentas.values():
        lista.sort(key=lambda f: (f["fecha"], f["id"]))
    return cuentas


def estado_cuenta(eventos, params, dia):
    tipos = [e["evento"].strip() for e in eventos]
    bloqueo = None
    for e in eventos:
        t = e["evento"].strip()
        if t in BLOQUEOS:
            bloqueo = (t, e)
        elif t == "reactivada":
            bloqueo = None
    toques = [a_fecha(e["fecha"]) for e in eventos if e["evento"].strip() in TOQUES]
    ultimo = a_fecha(eventos[-1]["fecha"])
    ultimo_relevante = max((a_fecha(e["fecha"]) for e in eventos
                            if e["evento"].strip() != "nota"), default=ultimo)
    caliente = (any(t in tipos for t in ("respuesta", "conversacion", "loi_enviada"))
                and "loi_firmada" not in tipos and bloqueo is None)
    return {
        "cuenta": eventos[-1]["cuenta"].strip(),
        "vertical": eventos[-1]["vertical"].strip(),
        "canal": next((e["canal"].strip() for e in eventos if e["evento"].strip() in TOQUES),
                      eventos[0]["canal"].strip()),
        "hitos": set(tipos) | ({"contactada"} if toques else set()),
        "bloqueo": bloqueo,
        "ultimo_toque": max(toques) if toques else None,
        "ultimo_evento": ultimo,
        "dias_sin_movimiento": (dia - ultimo_relevante).days,
        "caliente": caliente,
    }


def puede_contactar(cuenta_id, cuentas, params, dia):
    if cuenta_id not in cuentas:
        return True, "cuenta sin historial en el pipeline"
    st = estado_cuenta(cuentas[cuenta_id], params, dia)
    if st["bloqueo"]:
        tipo, fila = st["bloqueo"]
        return False, f"marcada {tipo} el {fila['fecha']} ({fila['id']}): {fila['detalle'].strip()}"
    minimo = int(params.get("dias_minimos_entre_contactos") or 0)
    if st["ultimo_toque"] is not None:
        dias = (dia - st["ultimo_toque"]).days
        if dias < minimo:
            return False, (f"último toque el {st['ultimo_toque']} (hace {dias} días; "
                           f"mínimo {minimo})")
    if "loi_firmada" in st["hitos"]:
        return True, "ya firmó LOI: solo mensajes de entrega o seguimiento de cliente"
    return True, "sin bloqueos"


def resumen(params):
    _, filas = leer()
    filas = vigentes(filas)
    dia = hoy(params)
    cuentas = por_cuenta(filas)
    estados = {cid: estado_cuenta(ev, params, dia) for cid, ev in cuentas.items()}

    def conteo(grupo):
        return {clave: sum(1 for st in grupo if clave in st["hitos"]) for clave, _ in EMBUDO}

    por_vertical = defaultdict(list)
    por_canal = defaultdict(list)
    for st in estados.values():
        por_vertical[st["vertical"]].append(st)
        if "contactada" in st["hitos"]:
            por_canal[st["canal"]].append(st)

    objetivo = params.get("objetivo_lois")
    limite = params.get("fecha_limite_lois")
    dias_restantes = None
    if not es_pendiente(limite):
        try:
            dias_restantes = (a_fecha(limite) - dia).days
        except ValueError:
            dias_restantes = None

    alertas = []
    if es_pendiente(limite):
        alertas.append("fecha_limite_lois pendiente: sin ella no se puede planificar hacia atrás.")
    elif dias_restantes is not None and dias_restantes < 0:
        alertas.append("fecha_limite_lois ya pasó.")

    corte_c = int(params.get("corte_cuentas") or 0)
    corte_conv = int(params.get("corte_conversaciones") or 0)
    corte_pag = int(params.get("corte_diagnosticos_pagados") or 0)
    canales = {}
    for canal, grupo in sorted(por_canal.items()):
        c = conteo(grupo)
        alcanzado = (corte_c and c["contactada"] >= corte_c
                     and c["conversacion"] < corte_conv and c["pago"] < corte_pag)
        canales[canal] = {"contactadas": c["contactada"], "conversaciones": c["conversacion"],
                          "pagos": c["pago"], "loi_firmadas": c["loi_firmada"],
                          "corte_alcanzado": bool(alcanzado)}
        if alcanzado:
            alertas.append(f"Criterio de corte alcanzado en el canal {canal}: {c['contactada']} "
                           f"cuentas contactadas, {c['conversacion']} conversaciones, "
                           f"{c['pago']} pagos. No subir volumen; revisar problema, nicho, "
                           "oferta y mensaje.")

    fria = int(params.get("dias_cuenta_fria") or 0)
    calientes = []
    for cid, st in sorted(estados.items(), key=lambda kv: kv[1]["dias_sin_movimiento"]):
        if st["caliente"]:
            calientes.append({"cuenta_id": cid, "cuenta": st["cuenta"],
                              "vertical": st["vertical"],
                              "dias_sin_movimiento": st["dias_sin_movimiento"],
                              "enfriandose": bool(fria and st["dias_sin_movimiento"] > fria)})
    enfriando = [c["cuenta"] for c in calientes if c["enfriandose"]]
    if enfriando:
        alertas.append(f"Cuentas con respuesta sin movimiento desde hace más de {fria} días: "
                       + ", ".join(enfriando))

    alertas.extend(infracciones(filas, cuentas, params))

    total = conteo(estados.values())
    return {
        "fecha": dia.isoformat(),
        "cuentas": len(estados),
        "loi_firmadas": total["loi_firmada"],
        "objetivo_lois": objetivo,
        "objetivo_ideal": params.get("objetivo_lois_ideal", objetivo),
        "fecha_limite_lois": limite,
        "dias_restantes": dias_restantes,
        "pagos": total["pago"],
        "total": total,
        "por_vertical": {v: conteo(g) for v, g in sorted(por_vertical.items())},
        "por_canal": canales,
        "calientes": calientes,
        "alertas": alertas,
    }


def infracciones(filas, cuentas, params):
    """Higiene: solo filas nuevas (no la carga inicial, que conserva errores históricos)."""
    avisos = []
    minimo = int(params.get("dias_minimos_entre_contactos") or 0)
    for cid, eventos in cuentas.items():
        bloqueo = None
        ultimo_toque = None
        for e in eventos:
            t = e["evento"].strip()
            nueva = (e.get("registrado_por") or "").strip() != CARGA_INICIAL
            if t in TOQUES:
                f = a_fecha(e["fecha"])
                if nueva and bloqueo:
                    avisos.append(f"{e['id']}: toque a {cid}, marcada {bloqueo}.")
                if nueva and ultimo_toque is not None and (f - ultimo_toque).days < minimo:
                    avisos.append(f"{e['id']}: toque a {cid} a {(f - ultimo_toque).days} días "
                                  f"del anterior (mínimo {minimo}).")
                ultimo_toque = f
            if t in BLOQUEOS:
                bloqueo = t
            elif t == "reactivada":
                bloqueo = None
    return avisos


def imprimir(r):
    print(f"EMBUDO — {r['fecha']}")
    limite = r["fecha_limite_lois"]
    resto = (f"{r['dias_restantes']} días hasta {limite}" if r["dias_restantes"] is not None
             else "fecha límite PENDIENTE")
    print(f"  LOIs firmadas: {r['loi_firmadas']} / {r['objetivo_lois']} (ideal {r['objetivo_ideal']})  ·  {resto}")
    print(f"  Pagos (diagnóstico o ACD): {r['pagos']}  ·  Cuentas en el pipeline: {r['cuentas']}")
    cab = ["vertical"] + [nombre for _, nombre in EMBUDO]
    anchos = [16] + [max(5, len(c)) for c in cab[1:]]
    print("\nPOR VERTICAL")
    print("  " + "  ".join(c.rjust(a) if i else c.ljust(a) for i, (c, a) in enumerate(zip(cab, anchos))))
    for v, c in list(r["por_vertical"].items()) + [("TOTAL", r["total"])]:
        celdas = [v] + [str(c[k]) for k, _ in EMBUDO]
        print("  " + "  ".join(x.rjust(a) if i else x.ljust(a)
                               for i, (x, a) in enumerate(zip(celdas, anchos))))
    print("\nPOR CANAL (cuentas contactadas)")
    for canal, c in r["por_canal"].items():
        marca = "  ← CORTE ALCANZADO" if c["corte_alcanzado"] else ""
        print(f"  {canal}: {c['contactadas']} contactadas · {c['conversaciones']} conversaciones · "
              f"{c['pagos']} pagos · {c['loi_firmadas']} LOI firmadas{marca}")
    print("\nCUENTAS CON RESPUESTA ABIERTA")
    if not r["calientes"]:
        print("  Ninguna.")
    for c in r["calientes"]:
        marca = "  ← enfriándose" if c["enfriandose"] else ""
        print(f"  {c['cuenta']} ({c['cuenta_id']}, {c['vertical']}): "
              f"{c['dias_sin_movimiento']} días sin movimiento{marca}")
    if r["alertas"]:
        print("\nALERTAS")
        for a in r["alertas"]:
            print(f"  ! {a}")


def mostrar_cuenta(cuenta_id, params):
    _, filas = leer()
    cuentas = por_cuenta(vigentes(filas))
    dia = hoy(params)
    if cuenta_id not in cuentas:
        print(f"{cuenta_id}: sin historial en el pipeline.")
        return
    for e in cuentas[cuenta_id]:
        print(f"  {e['fecha']}  {e['id']}  {e['evento']:<20} {e['canal']:<12} {e['detalle']}")
    ok, motivo = puede_contactar(cuenta_id, cuentas, params, dia)
    print(f"¿Puede contactarse hoy? {'SÍ' if ok else 'NO'}: {motivo}")


def verificar(params):
    errores = []
    cab, filas = leer()
    if cab != COLUMNAS:
        errores.append(f"Cabecera distinta de la esperada: {','.join(COLUMNAS)}")
    verticales = set(params.get("verticales") or []) | {"otro"}
    corregidas = {(f.get("ref") or "").strip() for f in filas
                  if (f.get("evento") or "").strip() == "correccion"}
    ids = set()
    numeros = []
    for n, f in enumerate(filas, start=2):
        pref = f"Fila {n} ({f.get('id', '?')})"
        try:
            a_fecha(f.get("fecha") or "")
        except ValueError:
            errores.append(f"{pref}: fecha no válida (AAAA-MM-DD)")
        fid = (f.get("id") or "").strip()
        if not RE_ID_EVENTO.match(fid):
            errores.append(f"{pref}: id no válido (EV-0001)")
        elif fid in ids:
            errores.append(f"{pref}: id duplicado")
        else:
            ids.add(fid)
            numeros.append(int(fid[3:]))
        if fid in corregidas:
            continue  # ya corregida: deja de contar y no bloquea la verificación
        if not RE_ID_CUENTA.match((f.get("cuenta_id") or "").strip()):
            errores.append(f"{pref}: cuenta_id no válido (minúsculas, números y guiones)")
        if not (f.get("cuenta") or "").strip():
            errores.append(f"{pref}: cuenta vacía")
        if (f.get("vertical") or "").strip() not in verticales:
            errores.append(f"{pref}: vertical fuera de parametros.verticales")
        if (f.get("canal") or "").strip() not in CANALES:
            errores.append(f"{pref}: canal no válido ({', '.join(sorted(CANALES))})")
        evento = (f.get("evento") or "").strip()
        if evento not in EVENTOS:
            errores.append(f"{pref}: evento no válido ({', '.join(EVENTOS)})")
        nueva = (f.get("registrado_por") or "").strip() != CARGA_INICIAL
        if not (f.get("registrado_por") or "").strip():
            errores.append(f"{pref}: registrado_por vacío")
        if evento == "correccion" and not (f.get("ref") or "").strip():
            errores.append(f"{pref}: una correccion necesita ref = id de la fila corregida")
        if nueva and evento in CONFIRMADOS_POR_CEO and not (f.get("ref") or "").strip():
            errores.append(f"{pref}: {evento} sin ref a la confirmación del CEO en la bandeja")
        if RE_RELLENO.search(f.get("detalle") or ""):
            errores.append(f"{pref}: el detalle contiene un campo sin rellenar")
    if numeros and sorted(numeros) != list(range(min(numeros), max(numeros) + 1)):
        errores.append("Los ids EV no son consecutivos")
    for f in filas:
        if (f.get("evento") or "").strip() == "correccion" and (f.get("ref") or "").strip() not in ids:
            errores.append(f"{f.get('id')}: corrige un id que no existe")

    avisos = []
    try:
        subprocess.run(["git", "rev-parse", "--verify", "HEAD"], cwd=RAIZ,
                       check=True, capture_output=True)
        diff = subprocess.run(["git", "diff", "--unified=0", "HEAD", "--", "estado/pipeline.csv"],
                              cwd=RAIZ, check=True, capture_output=True, text=True).stdout
        for linea in diff.splitlines():
            if linea.startswith("-") and not linea.startswith("---"):
                errores.append("Se ha editado o borrado una fila ya registrada: " + linea[1:].strip()
                               + " → restáurala y corrige con una fila correccion")
    except (subprocess.CalledProcessError, FileNotFoundError):
        avisos.append("Sin historial git: no se comprobó que el pipeline solo crezca.")

    for a in avisos:
        print(f"AVISO: {a}")
    if errores:
        print("VERIFICACIÓN FALLIDA")
        for e in errores:
            print(f"  ✗ {e}")
        return 1
    print(f"VERIFICACIÓN OK — {len(filas)} eventos")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--json", action="store_true", help="salida en JSON")
    ap.add_argument("--cuenta", metavar="ID", help="historial y estado de una cuenta")
    ap.add_argument("--puede-contactar", metavar="ID", help="¿se puede contactar hoy?")
    ap.add_argument("--verificar", action="store_true", help="validar el pipeline")
    args = ap.parse_args()
    params = cargar_parametros()
    if args.verificar:
        sys.exit(verificar(params))
    if args.cuenta:
        mostrar_cuenta(args.cuenta, params)
        return
    if args.puede_contactar:
        _, filas = leer()
        ok, motivo = puede_contactar(args.puede_contactar, por_cuenta(vigentes(filas)),
                                     params, hoy(params))
        print(f"{'SÍ' if ok else 'NO'}: {motivo}")
        sys.exit(0 if ok else 1)
    r = resumen(params)
    if args.json:
        r["total"] = dict(r["total"])
        print(json.dumps(r, ensure_ascii=False, indent=2, default=str))
    else:
        imprimir(r)


if __name__ == "__main__":
    main()
