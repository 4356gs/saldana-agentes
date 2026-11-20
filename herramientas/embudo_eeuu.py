#!/usr/bin/env python3
"""Embudo esperado y economía unitaria de la línea EE. UU. (Acta EE. UU., secciones 7 y 8).

Todas las conversiones y costes son [SUPUESTO] hasta que haya datos propios en
estado/pipeline.csv. Cuando los haya, se sustituyen pasando los argumentos.

Uso:
  python3 herramientas/embudo_eeuu.py
  python3 herramientas/embudo_eeuu.py --por-semana 30 --semanas-utiles 13 --semanas-anio 40

Momentos del Acta EE. UU. §7 (envíos desde el 7 dic, ciclo de venta de --ciclo-semanas):
  control 18 feb: 7 semanas de envío (mide conversaciones) -> --semanas-utiles 7
  día 90:         5 semanas útiles (7 de envío menos el ciclo) -> --semanas-utiles 5
  límite 19 abr:  13 semanas útiles (valor por defecto)
La probabilidad de tener al menos un cliente es 1 - exp(-clientes esperados) (Poisson) [ESTIMADO].
  python3 herramientas/embudo_eeuu.py --implantacion 1500 --mensual 300

Solo usa la biblioteca estándar. Lee estado/parametros.json (coste_hora_ceo, horas).
"""
import argparse
import json
import math
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
P = json.loads((RAIZ / "estado" / "parametros.json").read_text(encoding="utf-8"))

# Conversión por paso, sobre primeros contactos [SUPUESTO]:
# respuesta / contacto, conversación seria / respuesta, propuesta / conversación, pago / propuesta.
# Referencia propia: en España respondieron 5 de 64 cuentas contactadas (7,8 %) y ninguna
# respuesta llegó a conversación seria (pipeline.py, 2026-11-19) [VERIFICADO: pipeline.py].
ESCENARIOS = {
    "pesimista": (0.03, 0.30, 0.40, 0.25),
    "base":      (0.05, 0.40, 0.50, 0.30),
    "optimista": (0.08, 0.50, 0.60, 0.35),
}

# Costes y horas por cliente [SUPUESTO]; finanzas-control los sustituye por reales.
COSTE_DIRECTO_MES = 70      # USD/mes por cliente: número de WhatsApp, API de Claude y hosting
HORAS_IMPLANTACION = 10     # horas del CEO por implantación
HORAS_MANTENIMIENTO_MES = 1 # horas del CEO por cliente y mes
HORAS_VENTA_SEMANA = 4      # horas del CEO por semana en envíos y llamadas
MESES_MEDIOS_ACTIVO = 6     # meses de mantenimiento cobrados en el año, de media por cliente
# Comisión de cobro por PayPal (medio elegido por el CEO el 2026-11-19): pagos comerciales
# internacionales ~5,4 % + tarifa fija [ESTIMADO: comparalatam.com, fuente secundaria;
# verificar en paypal.com/do]. No incluye la conversión a pesos (3–4 %) si se retira en DOP.
COMISION_COBRO = 0.054


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--por-semana", type=int, default=30,
                    help="primeros contactos por semana (tope legal del equipo: 10 al día)")
    ap.add_argument("--semanas-utiles", type=int, default=13,
                    help="semanas de envío cuyo ciclo puede cerrar antes de la fecha límite")
    ap.add_argument("--ciclo-semanas", type=int, default=4,
                    help="semanas desde el primer contacto hasta el cobro (solo informativo)")
    ap.add_argument("--semanas-anio", type=int, default=40,
                    help="semanas de envío en 12 meses (descontando festivos)")
    ap.add_argument("--implantacion", type=float, default=2500, help="USD por implantación")
    ap.add_argument("--mensual", type=float, default=300, help="USD por mes de mantenimiento")
    ap.add_argument("--comision-cobro", type=float, default=COMISION_COBRO,
                    help="fracción que se queda el medio de cobro (PayPal ~0.054)")
    a = ap.parse_args()

    h = P["coste_hora_ceo"]
    linea = P.get("linea_activa") or {}
    print(f"Línea {linea.get('id', '?')} · objetivo {linea.get('objetivo_clientes_pagando')} "
          f"cliente(s) pagando antes de {linea.get('fecha_limite')}")
    print(f"Volumen: {a.por_semana} primeros contactos/semana · {a.semanas_utiles} semanas útiles "
          f"hasta la fecha límite · {a.semanas_anio} semanas en 12 meses  [SUPUESTO]")
    print(f"Precio: {a.implantacion:,.0f} USD implantación + {a.mensual:,.0f} USD/mes  [SUPUESTO] · "
          f"comisión de cobro {a.comision_cobro:.1%}  [ESTIMADO]\n")

    print("EMBUDO HASTA LA FECHA LÍMITE (valores esperados)")
    print(f"  {'escenario':10} {'contactos':>9} {'respuestas':>10} {'conversac.':>10} "
          f"{'propuestas':>10} {'clientes':>8} {'P(>=1)':>7}")
    for nombre, (r, c, p, g) in ESCENARIOS.items():
        n = a.por_semana * a.semanas_utiles
        resp = n * r
        conv = resp * c
        prop = conv * p
        cli = prop * g
        print(f"  {nombre:10} {n:9d} {resp:10.1f} {conv:10.1f} {prop:10.1f} {cli:8.2f} {1 - math.exp(-cli):7.0%}")

    print("\nPROYECCIÓN A 12 MESES (valores esperados, ingresos cobrados netos de comisión de cobro)")
    horas_venta = HORAS_VENTA_SEMANA * a.semanas_anio
    for nombre, (r, c, p, g) in ESCENARIOS.items():
        n = a.por_semana * a.semanas_anio
        cli = n * r * c * p * g
        ingresos = cli * (a.implantacion + a.mensual * MESES_MEDIOS_ACTIVO) * (1 - a.comision_cobro)
        directos = cli * COSTE_DIRECTO_MES * MESES_MEDIOS_ACTIVO
        horas = horas_venta + cli * (HORAS_IMPLANTACION + HORAS_MANTENIMIENTO_MES * MESES_MEDIOS_ACTIVO)
        neto = ingresos - directos
        print(f"  {nombre:10} clientes {cli:5.1f} · ingresos {ingresos:9,.0f} USD · costes directos "
              f"{directos:7,.0f} · neto {neto:9,.0f} · horas CEO {horas:5.0f} "
              f"(sombra {horas * h:7,.0f}) · neto tras sombra {neto - horas * h:9,.0f}")

    print("\nECONOMÍA UNITARIA POR CLIENTE (primer año, sin coste de adquisición)")
    ingreso = (a.implantacion + a.mensual * MESES_MEDIOS_ACTIVO) * (1 - a.comision_cobro)
    directo = COSTE_DIRECTO_MES * MESES_MEDIOS_ACTIVO
    sombra = (HORAS_IMPLANTACION + HORAS_MANTENIMIENTO_MES * MESES_MEDIOS_ACTIVO) * h
    mc = ingreso - directo - sombra
    print(f"  Ingreso neto de comisión {ingreso:,.0f} − directos {directo:,.0f} − horas CEO {sombra:,.0f} "
          f"= margen de contribución {mc:,.0f} USD")
    margen_mes = a.mensual * (1 - a.comision_cobro) - COSTE_DIRECTO_MES - HORAS_MANTENIMIENTO_MES * h
    print(f"  Margen mensual de mantenimiento: {margen_mes:,.0f} USD/mes")
    for nombre, (r, c, p, g) in ESCENARIOS.items():
        tasa = r * c * p * g
        contactos = 1 / tasa
        semanas = contactos / a.por_semana
        cac = semanas * HORAS_VENTA_SEMANA * h
        print(f"  {nombre:10} 1 cliente cada {contactos:5.0f} contactos ≈ {semanas:4.1f} semanas · "
              f"coste sombra de adquisición {cac:7,.0f} USD · margen tras adquisición {mc - cac:8,.0f} USD")


if __name__ == "__main__":
    main()
