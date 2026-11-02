#!/usr/bin/env python3
"""Economia unitaria y presupuesto del plan. Solo lectura de estado/parametros.json."""
import json, math, sys, os
P = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "estado", "parametros.json")))
FX = float(sys.argv[1]) if len(sys.argv) > 1 else 1.08   # [SUPUESTO] USD por EUR
H = P["coste_hora_ceo"]; H_ENT, H_VTA = 8, 3; SEMANAS = 4
BLOQ = {"WhatsApp/llamadas Albamar": 1, "OEF validacion LOI": 0.5, "Llamadas a socios": 2,
        "Revision de borradores": 1, "Reuniones": 1.5}
print(f"FX [SUPUESTO] 1 EUR = {FX} USD (cobro real = importe recibido en USD)")
print(f"Coste sombra por ACD: {H_ENT+H_VTA} h x {H} = {(H_ENT+H_VTA)*H:.0f} USD; coste directo ~0 [SUPUESTO]")
hs = sum(BLOQ.values()); plan = hs*SEMANAS*H
print(f"Plan: {hs} h/sem (tope {P['horas_ceo_max_semana']}) x {SEMANAS} sem = {hs*SEMANAS} h = {plan:.0f} USD sombra")
for pe in (900, 1290, 1490):
    bruto = pe*FX
    for com in (0, .2, .4):
        neto = bruto*(1-com); mc = neto-(H_ENT+H_VTA)*H
        inc = neto-H_ENT*H  # contribucion incremental (venta ya en el plan)
        be = math.ceil(plan/inc) if inc > 0 else None
        print(f"ACD {pe:>4} EUR={bruto:7.0f} USD com {int(com*100):>2}%: neto {neto:7.0f}  MC tras 11h {mc:7.0f}  "
              f"MC tras 8h {inc:7.0f}  PE plan: {be if be else 'no cubre'} ACD")
print("Tramo 1: max comprometido sin ingresos", P["tramo_1_max_comprometido"], "USD; plan usa 0 USD directo")
cap = P["capital_inicial"]; res = P["reserva_intocable"]
print(f"Caja disponible sobre reserva: {cap-res} USD; umbrales gasto {P['umbral_gasto_unitario']}/{P['umbral_gasto_semanal']} USD")
for pct in (10, 20, 33):
    print(f"  {pct}% capital = {cap*pct/100:.0f} USD")
