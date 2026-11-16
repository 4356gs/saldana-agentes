# Propuesta de Disolución, Pausa o Reactivación

Fecha: 2026-11-16 · Solicitud de decisión: **APR-004**
Motivo: conclusión del Comité. Hoy vence el disparador 1 del Acta (§17: "0 conversaciones serias el 2026-11-16") y el dato es 0 conversaciones serias (`pipeline.py`, 2026-11-16). El disparador no está formalmente en vigor porque el Acta (APR-001) no está aprobada. El disparador 4 ("menos de 4 cuentas cálidas el 2026-11-06") se habría cumplido el 6 nov: no se nombró ninguna.

La causa no es que el plan haya fallado: el plan no ha empezado. APR-001, APR-002 y APR-003 llevan 14 días sin respuesta, y la OEF-001 y la OEF-003 vencieron el 6 nov. Desde entonces el equipo solo ha podido emitir reportes de 3 líneas.

Desde esta fecha está congelado todo gasto nuevo hasta que el CEO decida. En la práctica no cambia nada: no hay gasto previsto.

## 1. Capital restante
Salida de `caja.py` (2026-11-16):
- Caja: 3.000,00 USD. Gastado: 0. Cobrado: 0. Comprometido: 0.
- Reserva intocable: 600 USD. Disponible para comprometer: 2.400 USD.
- Horas del CEO registradas: 0. Coste sombra acumulado: 0 USD.

## 2. Compromisos abiertos
- Con terceros: ninguno. No hay contratos, LOIs, comisiones ni pagos pendientes.
- Con cuentas, sin dinero de por medio:
  - Albamar: Xurxo pidió seguir por WhatsApp el 6 oct y lleva 41 días sin respuesta nuestra (EV-0099). `pipeline.py` marca 76 días porque cuenta desde nuestro último seguimiento, del 1 sep.
  - Barrancolí dice haber pagado en febrero y adjunta comprobante (correo del 5 nov). Sigue sin conciliar ni contestar.
    - Si pagó, puede haber un cobro sin registrar ni facturar. Eso es un tema fiscal, no solo de relación: se valida con quien lleva la facturación, y `jurisdiccion` sigue PENDIENTE.
    - No entra en `estado/libro.csv` hasta que el CEO lo confirme con el importe recibido.
- Internos: las OEF-001, OEF-002 y OEF-003 siguen abiertas. Si se disuelve, se cancelan.

## 3. Activos generados y reutilizables
- El Acta "Cálido primero" (`actas/acta-activacion.md`), revisada por `riesgo` y lista para aprobar.
- El borrador de WhatsApp para Albamar y su guion de llamada (`salidas/borradores/`).
- La conciliación de los envíos de octubre (`salidas/material/conciliacion-correo-2026-11-02.md`).
- Un pipeline de 73 cuentas, y las herramientas de caja, embudo e higiene (`herramientas/`), con reglas que vienen de errores reales.
- El inventario de activos verificado en Drive (`contexto/oferta-y-activos.md` §4) y las 9 lecciones comerciales (`contexto/saldana-digital.md` §5).

## 4. Aprendizajes
- Refutada: "falta volumen o un mensaje mejor". Unas 108 cuentas frías dieron 0 conversaciones serias [ESTIMADO: 63 cargadas más unas 45 pendientes de APR-002]. El canal `email_frio` alcanzó el criterio de corte (63 cuentas en el pipeline y 0 conversaciones).
- Sin probar: "lo cálido convierte". Albamar y la red del CEO no se han activado, así que no hay dato a favor ni en contra.
- Cuello de botella: lo que avanza hacia una LOI está bloqueado por decisiones del CEO desde el 6 nov [SUPUESTO sobre la causa: falta de tiempo del CEO, o que el canal de la bandeja no le llega].

## 5. Opciones y recomendación

Quedan 15 días hasta el 2026-12-01.

Con el embudo del Acta y 4 cuentas de red, el plan completo de 29 días daba 1,07 LOIs esperadas [ESTIMADO: `python3 herramientas/embudo_acta.py 4`, conversiones del Acta §7 marcadas como SUPUESTO]. Con la mitad del plazo y ninguna cuenta de red nombrada, la expectativa queda **por debajo de 1 LOI legítima antes del 1 dic**, aunque se reactive hoy. Esto no se ha recalculado por plazo, porque no hay base para ajustar cada paso.

Las LOIs solo se piden después de una conversación seria y de un diagnóstico. Acortar ese ciclo para llegar a la fecha empujaría a cartas de complacencia, que ponen en riesgo el expediente.

| Opción | Qué hace el CEO | Coste para el CEO | Qué consigue |
|---|---|---|---|
| **A. Reactivar** | Antes del 18 nov:<br>• aprueba APR-001, APR-002 y APR-003;<br>• nombra al menos 4 personas de su red (pregunta 1);<br>• envía el WhatsApp a Albamar y hace la llamada (OEF-002);<br>• hace la OEF-001. | Unas 2,75 h esta semana (110 USD de coste sombra), más leer tres APR. Después, hasta 6 h/semana. | Una opción real a 1 LOI antes del 1 dic, y a más si la fecha tiene margen. |
| **B. Pausar** | Responde "PAUSA" con una fecha de reanudación, o cambia la tarea programada a semanal. Aun así, hace la OEF-001 (30 min). | 0,5 h | Se acaban los reportes vacíos y se conservan el repositorio, el Acta y las cuentas. Al reanudar hará falta un Acta con fecha nueva. |
| **C. Disolver** | Responde "DISUELVE". | 0 h | Se cancelan las OEF y se archiva el repositorio. La vía de LOIs queda sin equipo. |

**Recomendación de la Directora, alineada con `riesgo`:**
- **B por defecto.** Pasa a **A** solo si, antes del 18 nov, el CEO aprueba APR-001 y nombra al menos 4 personas de su red.
- En cualquier opción, la OEF-001 se hace: sin ella no se sabe si el 1 dic es la fecha real, y ninguna LOI sería válida.
- Se descarta **C**: el equipo no consume capital, y el expediente seguirá necesitando LOIs si la fecha tiene margen.

Lo que no se propone: volver al correo en frío ni subir el volumen. El canal está cortado (CLAUDE.md §8).

## 6. Revisión de riesgo
Revisado el 2026-11-16. Veredicto: **pasa con cambios**, ya incorporados:
- 41 días de Albamar, no 76;
- coste de A en 2,75 h, no 75 min;
- estimación calculada con código;
- supuestos etiquetados;
- Barrancolí como tema fiscal.

Tesis contraria: A pide al CEO lo mismo que lleva 14 días sin hacer y por el mismo canal. En 15 días, sin modelo de LOI validado, A solo llega a una LOI si se acorta el ciclo, y eso empuja a la complacencia.

Recomendación textual de `riesgo`: "Recomiendo B por defecto. Solo pasaría a A si antes del 18 nov el CEO aprueba APR-001 y nombra al menos 4 personas de su red. En cualquier opción, la OEF-001 (30 min) debe hacerse: sin ella no sabemos si el 1 dic es real, y ninguna LOI sería válida."

Riesgo recomendaría A sin condiciones si quien lleva el expediente confirma que la fecha tiene margen.
