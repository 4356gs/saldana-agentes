#!/usr/bin/env python3
"""Embudo esperado del Acta de Activación (supuestos etiquetados [SUPUESTO]).
Uso: python3 herramientas/embudo_acta.py [cuentas_red]"""
import sys
red = int(sys.argv[1]) if len(sys.argv) > 1 else 6
vias = {  # cuentas, p_respuesta, p_conversacion, p_loi  [SUPUESTO]
    "Albamar": (1, 0.6, 0.4, 0.7),
    "Red cálida": (red, 0.7, 0.5, 0.5),
    "Socio derivación": (2, 0.5, 0.4, 0.5),
}
tc = tl = 0
for k, (n, r, c, l) in vias.items():
    conv = n * r * c; loi = conv * l; tc += conv; tl += loi
    print(f"{k:18} cuentas={n:2} resp={n*r:4.1f} conv={conv:4.2f} loi={loi:4.2f}")
print(f"TOTAL conversaciones={tc:.2f} LOIs={tl:.2f}")
base = tl - red * 0.7 * 0.5 * 0.5
need = (3 - base) / (0.7 * 0.5 * 0.5)
print(f"Cuentas de red necesarias para 3 LOIs esperadas: {need:.1f}")
