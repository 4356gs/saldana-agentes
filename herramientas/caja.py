#!/usr/bin/env python3
"""Caja, tramos, horas y alertas de la organización.

Uso:
  python3 herramientas/caja.py              resumen legible
  python3 herramientas/caja.py --json       resumen en JSON
  python3 herramientas/caja.py --verificar  valida libro y horas, y que solo hayan crecido

Fuentes: estado/parametros.json, estado/libro.csv, estado/horas.csv.
Solo usa la biblioteca estándar de Python.
"""
import argparse
import csv
import json
import subprocess
import sys
from datetime import date, datetime
from decimal import Decimal, InvalidOperation
from pathlib import Path

try:
    from zoneinfo import ZoneInfo
except ImportError:  # Python < 3.9
    ZoneInfo = None

RAIZ = Path(__file__).resolve().parent.parent
PARAMS = RAIZ / "estado" / "parametros.json"
LIBRO = RAIZ / "estado" / "libro.csv"
HORAS = RAIZ / "estado" / "horas.csv"

COLS_LIBRO = ["fecha", "id", "tipo", "concepto", "importe", "partida",
              "experimento", "ref", "comprobante", "registrado_por"]
COLS_HORAS = ["fecha", "ref", "horas", "ejecutor", "nota"]
TIPOS = {"ingreso", "gasto", "compromiso", "liberacion", "anulacion"}
CERO = Decimal("0")


def cargar_parametros():
    with PARAMS.open(encoding="utf-8") as f:
        return json.load(f)


def es_pendiente(valor):
    if valor is None:
        return True
    if isinstance(valor, str) and "PENDIENTE" in valor.upper():
        return True
    return False


def hoy(params):
    zona = params.get("zona_horaria")
    if ZoneInfo and zona:
        try:
            return datetime.now(ZoneInfo(zona)).date()
        except Exception:
            pass
    return date.today()


def dec(valor):
    if valor is None or es_pendiente(valor):
        return None
    return Decimal(str(valor))


def leer_csv(ruta):
    with ruta.open(encoding="utf-8", newline="") as f:
        lector = csv.DictReader(f)
        return lector.fieldnames or [], list(lector)


def fmt(d, moneda=""):
    if d is None:
        return "—"
    s = f"{d:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return f"{s} {moneda}".strip()


def misma_semana(fecha_txt, ref):
    try:
        f = date.fromisoformat(fecha_txt)
    except ValueError:
        return False
    return f.isocalendar()[:2] == ref.isocalendar()[:2]


def resumen(params):
    _, libro = leer_csv(LIBRO)
    _, horas = leer_csv(HORAS)
    moneda = params.get("moneda", "")
    dia = hoy(params)

    por_id = {f.get("id", "").strip(): f for f in libro}
    ids_compromiso = {i for i, f in por_id.items()
                      if f.get("tipo", "").strip() == "compromiso"}
    tot = {t: CERO for t in TIPOS}
    semana_salidas = CERO
    por_exp = {}
    for fila in libro:
        tipo = fila.get("tipo", "").strip()
        try:
            imp = Decimal(fila.get("importe", "0"))
        except InvalidOperation:
            continue
        if tipo not in TIPOS:
            continue
        if tipo == "anulacion":
            # Resta el importe del movimiento erróneo al que apunta ref.
            original = por_id.get(fila.get("ref", "").strip())
            if not original or original.get("tipo", "").strip() not in ("ingreso", "gasto"):
                continue
            tipo_orig = original["tipo"].strip()
            tot[tipo_orig] -= imp
            if (tipo_orig == "gasto"
                    and misma_semana(original.get("fecha", ""), dia)
                    and original.get("ref", "").strip() not in ids_compromiso):
                semana_salidas -= imp
            exp = original.get("experimento", "").strip() or "(sin experimento)"
            e = por_exp.setdefault(exp, {"ingresos": CERO, "gastos": CERO})
            e["ingresos" if tipo_orig == "ingreso" else "gastos"] -= imp
            continue
        tot[tipo] += imp
        # Dinero nuevo de la semana: compromisos creados + gastos que no ejecutan
        # un compromiso previo (esos ya contaron cuando se comprometieron).
        if misma_semana(fila.get("fecha", ""), dia):
            if tipo == "compromiso":
                semana_salidas += imp
            elif tipo == "gasto" and fila.get("ref", "").strip() not in ids_compromiso:
                semana_salidas += imp
        exp = fila.get("experimento", "").strip() or "(sin experimento)"
        e = por_exp.setdefault(exp, {"ingresos": CERO, "gastos": CERO})
        if tipo == "ingreso":
            e["ingresos"] += imp
        elif tipo == "gasto":
            e["gastos"] += imp

    capital = dec(params.get("capital_inicial")) or CERO
    reserva = dec(params.get("reserva_intocable")) or CERO
    tramo1 = dec(params.get("tramo_1_max_comprometido"))
    umbral_sem = dec(params.get("umbral_gasto_semanal"))

    compromisos = tot["compromiso"] - tot["liberacion"]
    caja = capital + tot["ingreso"] - tot["gasto"]
    disponible = caja - reserva - compromisos
    expuesto = tot["gasto"] + compromisos
    ingreso_neto = tot["ingreso"] - tot["gasto"]
    en_tramo_1 = tot["ingreso"] == CERO
    margen_tramo = (tramo1 - expuesto) if (en_tramo_1 and tramo1 is not None) else None

    h_ceo_total = CERO
    h_ceo_semana = CERO
    h_delegadas = CERO
    for fila in horas:
        try:
            h = Decimal(fila.get("horas", "0"))
        except InvalidOperation:
            continue
        if fila.get("ejecutor", "").strip().upper() == "CEO":
            h_ceo_total += h
            if misma_semana(fila.get("fecha", ""), dia):
                h_ceo_semana += h
        else:
            h_delegadas += h

    h_max = dec(params.get("horas_ceo_max_semana"))
    coste_hora = dec(params.get("coste_hora_ceo"))
    coste_sombra = (h_ceo_total * coste_hora) if coste_hora is not None else None
    neto_ajustado = (ingreso_neto - coste_sombra) if coste_sombra is not None else None

    experimentos = {}
    for nombre, v in sorted(por_exp.items()):
        neto = v["ingresos"] - v["gastos"]
        roi = (neto / v["gastos"]) if v["gastos"] > 0 else None
        experimentos[nombre] = {"ingresos": v["ingresos"], "gastos": v["gastos"],
                                "neto": neto, "roi": roi}

    alertas = []
    if caja < reserva:
        alertas.append("La caja está por debajo de la reserva intocable.")
    if disponible < 0:
        alertas.append("Lo comprometido supera lo disponible fuera de la reserva.")
    if margen_tramo is not None and margen_tramo < 0:
        alertas.append("Primer tramo superado sin ingresos cobrados.")
    if umbral_sem is not None and semana_salidas > umbral_sem:
        alertas.append("El dinero nuevo de esta semana supera umbral_gasto_semanal: "
                       "cada movimiento debe tener su APR aprobado.")
    if h_max is not None and h_ceo_semana > h_max:
        alertas.append("Horas del CEO esta semana por encima del máximo.")
    pendientes = [k for k, v in params.items() if es_pendiente(v)]
    if pendientes:
        alertas.append("Parámetros pendientes: " + ", ".join(pendientes))

    return {
        "fecha": dia.isoformat(),
        "moneda": moneda,
        "capital_inicial": capital,
        "ingresos_cobrados": tot["ingreso"],
        "gastos_ejecutados": tot["gasto"],
        "compromisos_abiertos": compromisos,
        "caja": caja,
        "reserva_intocable": reserva,
        "disponible_para_comprometer": disponible,
        "en_primer_tramo": en_tramo_1,
        "margen_primer_tramo": margen_tramo,
        "dinero_nuevo_semana": semana_salidas,
        "ingreso_neto": ingreso_neto,
        "horas_ceo_semana": h_ceo_semana,
        "horas_ceo_max_semana": h_max,
        "horas_ceo_total": h_ceo_total,
        "horas_delegadas_total": h_delegadas,
        "coste_sombra_ceo_total": coste_sombra,
        "ingreso_neto_ajustado_por_coste_sombra": neto_ajustado,
        "experimentos": experimentos,
        "alertas": alertas,
    }


def imprimir(r):
    m = r["moneda"]
    print(f"CAJA — {r['fecha']}")
    print(f"  Caja: {fmt(r['caja'], m)}  (capital {fmt(r['capital_inicial'], m)} "
          f"+ cobrado {fmt(r['ingresos_cobrados'], m)} − gastado {fmt(r['gastos_ejecutados'], m)})")
    print(f"  Comprometido sin ejecutar: {fmt(r['compromisos_abiertos'], m)}")
    print(f"  Reserva intocable: {fmt(r['reserva_intocable'], m)}")
    print(f"  Disponible para comprometer: {fmt(r['disponible_para_comprometer'], m)}")
    if r["en_primer_tramo"]:
        print(f"  Primer tramo (sin ingresos todavía): margen {fmt(r['margen_primer_tramo'], m)}")
    print(f"  Dinero nuevo comprometido o gastado esta semana: {fmt(r['dinero_nuevo_semana'], m)}")
    print(f"  Ingreso neto: {fmt(r['ingreso_neto'], m)}")
    hmax = r["horas_ceo_max_semana"]
    print(f"  Horas CEO esta semana: {r['horas_ceo_semana']} / {hmax if hmax is not None else '—'}")
    print(f"  Horas CEO acumuladas: {r['horas_ceo_total']}  ·  delegadas: {r['horas_delegadas_total']}")
    print(f"  Coste sombra CEO acumulado: {fmt(r['coste_sombra_ceo_total'], m)}")
    print(f"  Ingreso neto ajustado por coste sombra: {fmt(r['ingreso_neto_ajustado_por_coste_sombra'], m)}")
    if r["experimentos"]:
        print("EXPERIMENTOS")
        for nombre, v in r["experimentos"].items():
            roi = f"{v['roi'] * 100:.0f}%" if v["roi"] is not None else "—"
            print(f"  {nombre}: cobrado {fmt(v['ingresos'], m)} · gastado {fmt(v['gastos'], m)} "
                  f"· neto {fmt(v['neto'], m)} · ROI {roi}")
    print("ALERTAS")
    if r["alertas"]:
        for a in r["alertas"]:
            print(f"  ! {a}")
    else:
        print("  Ninguna")


def a_json(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError(type(obj))


def validar_fecha(txt):
    try:
        date.fromisoformat(txt)
        return True
    except (ValueError, TypeError):
        return False


def verificar():
    errores = []

    cols, libro = leer_csv(LIBRO)
    if cols != COLS_LIBRO:
        errores.append(f"libro.csv: cabecera distinta de {','.join(COLS_LIBRO)}")
    ids = set()
    compromisos = {}
    liberado = {}
    anulables = {}
    anulado = {}
    for n, fila in enumerate(libro, start=2):
        pref = f"libro.csv línea {n}"
        if not validar_fecha(fila.get("fecha")):
            errores.append(f"{pref}: fecha no es AAAA-MM-DD")
        fid = (fila.get("id") or "").strip()
        if not fid:
            errores.append(f"{pref}: id vacío")
        elif fid in ids:
            errores.append(f"{pref}: id repetido {fid}")
        ids.add(fid)
        tipo = (fila.get("tipo") or "").strip()
        if tipo not in TIPOS:
            errores.append(f"{pref}: tipo '{tipo}' no válido")
        try:
            imp = Decimal(fila.get("importe") or "")
            if imp <= 0:
                errores.append(f"{pref}: importe debe ser positivo")
            if imp.as_tuple().exponent < -2:
                errores.append(f"{pref}: importe con más de 2 decimales")
        except InvalidOperation:
            errores.append(f"{pref}: importe no numérico (usa punto decimal, sin separador de miles)")
            imp = None
        if not (fila.get("concepto") or "").strip():
            errores.append(f"{pref}: concepto vacío")
        if tipo == "compromiso" and imp is not None:
            compromisos[fid] = imp
        if tipo == "liberacion" and imp is not None:
            ref = (fila.get("ref") or "").strip()
            if ref not in compromisos:
                errores.append(f"{pref}: liberación sin compromiso previo en ref ({ref or 'vacío'})")
            else:
                liberado[ref] = liberado.get(ref, CERO) + imp
                if liberado[ref] > compromisos[ref]:
                    errores.append(f"{pref}: se libera más de lo comprometido en {ref}")
        if tipo in ("ingreso", "gasto") and imp is not None:
            anulables[fid] = imp
        if tipo == "anulacion" and imp is not None:
            ref = (fila.get("ref") or "").strip()
            if ref not in anulables:
                errores.append(f"{pref}: anulación sin ingreso o gasto previo en ref ({ref or 'vacío'}); "
                               "los compromisos se cancelan con liberacion")
            else:
                anulado[ref] = anulado.get(ref, CERO) + imp
                if anulado[ref] > anulables[ref]:
                    errores.append(f"{pref}: se anula más de lo registrado en {ref}")

    cols_h, horas = leer_csv(HORAS)
    if cols_h != COLS_HORAS:
        errores.append(f"horas.csv: cabecera distinta de {','.join(COLS_HORAS)}")
    for n, fila in enumerate(horas, start=2):
        pref = f"horas.csv línea {n}"
        if not validar_fecha(fila.get("fecha")):
            errores.append(f"{pref}: fecha no es AAAA-MM-DD")
        try:
            if Decimal(fila.get("horas") or "") <= 0:
                errores.append(f"{pref}: horas debe ser positivo")
        except InvalidOperation:
            errores.append(f"{pref}: horas no numérico")
        if not (fila.get("ejecutor") or "").strip():
            errores.append(f"{pref}: ejecutor vacío (usa CEO o delegado: nombre)")

    avisos = []
    try:
        subprocess.run(["git", "rev-parse", "--verify", "HEAD"], cwd=RAIZ,
                       check=True, capture_output=True)
        diff = subprocess.run(
            ["git", "diff", "--unified=0", "HEAD", "--",
             "estado/libro.csv", "estado/horas.csv"],
            cwd=RAIZ, check=True, capture_output=True, text=True).stdout
        for linea in diff.splitlines():
            if linea.startswith("-") and not linea.startswith("---"):
                errores.append("Se ha editado o borrado una fila ya registrada: "
                               + linea[1:].strip()
                               + " → restaura la fila y corrige con una fila nueva")
    except (subprocess.CalledProcessError, FileNotFoundError):
        avisos.append("Sin historial git: no se comprobó que libro y horas solo crezcan.")

    for a in avisos:
        print(f"AVISO: {a}")
    if errores:
        print("VERIFICACIÓN FALLIDA")
        for e in errores:
            print(f"  ✗ {e}")
        return 1
    print(f"VERIFICACIÓN OK — {len(libro)} movimientos, {len(horas)} registros de horas")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--json", action="store_true", help="salida en JSON")
    ap.add_argument("--verificar", action="store_true", help="validar libro y horas")
    args = ap.parse_args()
    if args.verificar:
        sys.exit(verificar())
    r = resumen(cargar_parametros())
    if args.json:
        print(json.dumps(r, default=a_json, ensure_ascii=False, indent=2))
    else:
        imprimir(r)


if __name__ == "__main__":
    main()
