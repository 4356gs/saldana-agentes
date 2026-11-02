---
cuenta_id: bodegas-albamar
tipo: seguimiento a respuesta (no es primer contacto)
canal: WhatsApp, a petición expresa del contacto
destinatario: Xurxo, Bodegas Albamar (Cambados), +34 660 292 750 (número que él mismo facilitó por correo el 6 oct) [VERIFICADO: Outlook, correo 2026-10-06]
cargo: sin verificar; confirmarlo en la llamada
estado: BORRADOR. No se envía sin APR-003
comprobacion: `python3 herramientas/pipeline.py --puede-contactar bodegas-albamar`, ejecutado el 2026-11-02 a las 11:59 CET. Salida literal: `SÍ: sin bloqueos`
autor: desarrollo-negocio · revisión: riesgo (correcciones del 2026-11-02 incorporadas)
---

## Antes de enviar (decisión del CEO en APR-003)

**Desde qué número.** CLAUDE.md §4 solo autoriza `cuenta_envio` con prospectos. Aquí el canal lo pidió el propio contacto, pero el número desde el que se escribe lo decide el CEO de forma explícita en APR-003. Si se usa el 18496539171 (el número de Saldaña Digital para páginas de cliente), hay que tener en cuenta que es un número dominicano (+1 849) y que Xurxo lo verá así, con prefijo extranjero, al recibir el mensaje.

Franjas: se proponen en hora de España (Europe/Madrid). Equivalen a 11:30 y 12:30 en Santo Domingo [SUPUESTO: compatibles con la agenda laboral del CEO; si no lo son, cambiar la hora antes de enviar]. Si el mensaje sale después del martes 3 nov, usar en su lugar lunes 9 nov a las 16:30 y martes 10 nov a las 17:30.

## Mensaje (texto exacto)

Hola, Xurxo. Te escribo de Saldaña Digital: en octubre me pediste que siguiéramos por WhatsApp y se me quedó pendiente contestarte, disculpa la demora.

En agosto te escribí por lo del dominio de Albamar y me gustaría contarte lo que vi.

¿Ya tenéis la campaña cerrada? Si es así, ¿te encaja una llamada de 20 minutos esta semana? Te propongo el miércoles 4 a las 16:30 o el jueves 5 a las 17:30, hora de España. Si te va mejor otro momento, dime y me adapto.

## Por qué este mensaje a esta cuenta

- Es la única cuenta cálida abierta que confirma el CEO (bandeja 2026-11-01). Respondió dos veces y fue él quien pidió el canal. Lleva 27 días sin respuesta nuestra.
- Lección 1 (sección 5): lo único que generó respuesta en bodegas fue la observación concreta de su dominio. Por eso se retoma ese mismo hilo, sin afirmar cómo está hoy el dominio (no está verificado a fecha de envío), y no se cambia de tema, a diferencia de los dos borradores del 27 oct (costes y pedidos, por correo), que no deben enviarse.
- Corto, sin precio, sin enlaces y sin hablar de la LOI. El mensaje solo busca una cosa: la llamada.

## Siguiente paso

- **Si responde y acepta una franja:** el CEO la confirma por WhatsApp y hace la llamada con `2026-11-02-guion-llamada-albamar.md` (`ejecucion-fisica` la incorpora a la OEF). Después reporta en la bandeja `respuesta` y, si se celebra, `conversacion`.
- **Si propone otra fecha:** se acepta la primera que caiga antes del 20 nov.
- **Si no responde:** un único recordatorio por WhatsApp a la fecha de envío + 5 días (`dias_minimos_entre_contactos`), sin cambiar de tema. La fecha exacta se calcula cuando el CEO confirme en la bandeja el día de envío. Si tampoco hay respuesta, Albamar sale del plan de LOIs de noviembre y queda como `nota` para enero. No se vuelve al correo.
- **Si pide no recibir más mensajes:** `no_contactar` el mismo día.
