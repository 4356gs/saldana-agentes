# LOTE 1b · Línea EE. UU. · EXP-US-01 (Florida)

Preparado: 2026-11-21 · desarrollo-negocio · canal `email_eeuu` · vertical `inmobiliaria`. Revisado por `riesgo` (pasa con cambios, aplicados).
**Aprobación: APR-007, APROBADO por el CEO el 2026-11-25 sin cambios (DEC-011)**, un solo APR para el lote 1b entero: correos 1, 2 y 3 de las 4 cuentas. No entra en APR-006 y no depende de que APR-006 se apruebe tal cual, pero sí de sus mismas condiciones (§2).

## 1. Qué entra y qué no

`inteligencia-comercial` presentó 9 cuentas nuevas de Florida el 21 nov. Cuatro cumplen la definición de cuenta cualificada (CLAUDE.md §8) y entran en el lote (EV-0121 a EV-0124). Cinco quedan como `identificada` (EV-0125 a EV-0129):

| Cuenta | Por qué no entra | Cómo se recupera |
|---|---|---|
| acevedo-team-exp | Bajo eXp Realty; el contexto excluye redes con herramientas corporativas obligatorias y no está verificado si eXp las impone. Decisión de la Directora | Verificar la política de eXp para equipos |
| bella-mar-real-estate | La web no se pudo abrir: faltan fricción, correo y español en la web | El CEO o un delegado la abre en pantalla |
| rds-realty | Web inaccesible al lector: sin fricción ni correo | Igual: 2 minutos en pantalla |
| mav-united-realty-andres-sanchez | Correo ofuscado e ilegible; no se adivina | El CEO lee el correo en pantalla |
| perez-team-united-realty | Correo protegido e ilegible; español solo por Zillow | Igual |

**Recuento de EXP-US-01:** 9 cuentas del lote 1 + 4 del lote 1b = 13 de las 30 previstas en el Acta (§12). Con 13 cuentas, el criterio de éxito (2 respuestas de interés o 1 conversación seria) sigue leyéndose sobre una muestra pequeña, y así se dirá en el veredicto.

**Calidad del lote, sin adornos:** tres de las cuatro (valdivia, met y, en parte, viva) tienen la señal de español solo por el perfil profesional, no por la web. Es la señal admitida por el contexto (§3), pero más débil que la del lote 1. Si el lote 1b responde peor que el lote 1, esa es la primera hipótesis.

## 2. Condiciones previas: sin todas ellas no se carga ningún borrador

Idénticas a las de APR-006:

1. **OEF-004 hecha** (demo funcionando). El correo 1 dice "Monté un asistente" / "I built an assistant".
   - Si OEF-004 no está hecha el 8 de diciembre, no se envía. `desarrollo-negocio` reescribe esa frase para el plan B sin vídeo y `riesgo` la revisa.
   - Si la demo la terminó un técnico delegado, la frase pasa a "Tengo montado un asistente" / "I have an assistant set up".
2. **OEF-005 hecha**, con la dirección postal física literal (buzón virtual en EE. UU.) devuelta en la bandeja.
3. **Firma completa.** Cada borrador lleva en su propia línea una marca de firma: `FIRMA-ES-USTED` o `FIRMA-EN`.
   - Al cargar los borradores en Outlook, esa línea se sustituye por la firma correspondiente del §3, ya con el teléfono y la dirección.
   - Para completarla faltan dos datos: la dirección (OEF-005) y el teléfono del CEO (pregunta abierta en la bandeja).
   - **Ningún borrador se carga ni se envía con una marca `FIRMA-…` o `ENLACE-VIDEO` en el cuerpo.**
4. **Pregunta 12 del CEO sobre el dominio, respondida.**
5. **Enlace al vídeo** (OEF-004). Sustituye `ENLACE-VIDEO` en los correos 2: un solo enlace, sin acortador ni seguimiento.
6. **El mismo día del envío**, `python3 herramientas/pipeline.py --puede-contactar <cuenta_id>` para cada cuenta. Si responde NO, ese borrador no se carga.
7. **Corredurías sin verificar** (mismo criterio que invierte-en-miami-group en APR-006). Tres cuentas operan dentro de una correduría cuya política de herramientas no está verificada:
   - alexander-pena-apc-team, bajo Prime Agent Group, LLC;
   - valdivia-home-team, con United Realty Group;
   - met-real-estate-gomez-team, bajo Met Real Estate Corp.

   Ninguna es una franquicia de marca ni una red nacional como LPT o eXp [SUPUESTO: no verificado en ninguna de las tres]. United Realty Group es una correduría grande (empatada en el n.º 1 de Broward con 788 agentes en 2015 [VERIFICADO: The Real Deal, 2015-11-19]), así que en valdivia-home-team el riesgo de herramientas obligatorias es mayor que en invierte-en-miami-group. Las tres tienen web, equipo y correo propios. El CEO puede excluir cualquiera antes del envío.

Condición propia del lote 1b:

8. **El lote 1 va primero.** Si APR-006 se retrasa o cambia de fecha, el lote 1b se mueve con él: siempre al día siguiente del último envío del lote 1, sin superar 10 primeros contactos en un día.

## 3. Firmas

Las mismas del lote 1 (LOTE.md del lote 1, §3), aprobadas por `riesgo`. Solo faltan el teléfono y la dirección.

**FIRMA-ES-USTED** (alexander-pena-apc-team)
```
Gelo Saldaña
Saldaña Digital · Automatización comercial
TELÉFONO-PROFESIONAL
DIRECCIÓN-POSTAL-OEF-005

Este es un correo comercial de Saldaña Digital.
Si prefiere no recibir más correos míos, contésteme "baja" y no vuelvo a escribirle.
```

**FIRMA-EN** (viva-orlando-realty, valdivia-home-team, met-real-estate-gomez-team)
```
Gelo Saldaña
Saldaña Digital · Sales automation
TELÉFONO-PROFESIONAL
DIRECCIÓN-POSTAL-OEF-005

This is a commercial message from Saldaña Digital.
If you'd rather not hear from me again, reply "unsubscribe" and I won't write again.
```

`TELÉFONO-PROFESIONAL` y `DIRECCIÓN-POSTAL-OEF-005` son marcas de este archivo, no de los borradores, y se sustituyen al montar la firma. Si el teléfono es dominicano, va con el formato "número (WhatsApp · República Dominicana)"; si no se tiene, la línea se omite.

**Idioma y registro.**
- alexander-pena-apc-team: español, porque su web está en español. Registro usted [SUPUESTO], como en el lote 1.
- valdivia-home-team y met-real-estate-gomez-team: inglés, porque sus webs están solo en inglés (mismo criterio que liv-realty-linda-guzman).
- viva-orlando-realty: inglés. La ficha recomendaba español, pero la página en español es de la rama de alquileres y el español de la broker no está verificado; la web principal y la página de equipo están en inglés (mismo criterio que leonard-real-estate-group). Si el CEO prefiere español, lo reescribe `desarrollo-negocio`, no se traduce a mano.

## 4. Orden de envío (hora del Este)

**Propuesta: martes 8 de diciembre de 2026, a continuación del lote 1.** Ese día el lote 1 envía 3 correos (9:00, 9:30 y 10:00); con estos 4 son **7 primeros contactos**, por debajo del máximo de 10. El CEO lo hace en la misma sesión, con las firmas ya montadas, y los seguimientos coinciden con los del lote 1 del 15 de diciembre. Se mantiene un correo cada 30 minutos, nunca todos juntos. En diciembre, la hora del Este va una hora por detrás de Santo Domingo.

| # | Hora del Este (Santo Domingo) | Cuenta | Idioma | Para |
|---|---|---|---|---|
| 10 | 10:30 (11:30) | alexander-pena-apc-team | ES (usted) | info@alexanderpenarealtor.com |
| 11 | 11:00 (12:00) | viva-orlando-realty | EN | milena@vivaorlando.com |
| 12 | 11:30 (12:30) | valdivia-home-team | EN | roylan@valdiviahometeam.com |
| 13 | 12:00 (13:00) | met-real-estate-gomez-team | EN | Daniel@metsells.com |

La numeración sigue la del lote 1 (cuentas 1 a 9).

**Alternativa: miércoles 9 de diciembre**, a las mismas cuatro horas pero desde las 9:00 (9:00, 9:30, 10:00, 10:30 del Este). Así cada día queda con menos envíos (6, 3 y 4), a cambio de una sesión más del CEO (unos 5 minutos más) y de unos seguimientos el miércoles 16. La Directora elige; por defecto, el 8.

**Direcciones que el CEO confirma en pantalla antes de enviar:**
- met-real-estate-gomez-team: Daniel@metsells.com, en https://www.danielgomezrealestate.com/. Es del dominio de la correduría, no del equipo.

Las otras tres se leyeron en texto plano en la web de la cuenta. Si una dirección no aparece en la web, ese borrador no se envía y se avisa en la bandeja.

## 5. Seguimientos (en el mismo hilo, solo a quien no respondió)

- **Correo 2 (+5, con el vídeo):** martes 15 de diciembre, a las mismas horas que el correo 1, a continuación de las cuentas 7 a 9 del lote 1. Con la alternativa del 9 dic, el miércoles 16.
- **Correo 3 (cierre):** lunes 4 de enero de 2027, igual que el lote 1, por las fiestas (Acta §5).
  - Ese día salen hasta 13 cierres (9 del lote 1 y 4 de este). Se espacian de 9:00 a 12:00 del Este, uno cada 15 minutos. El tope de 10 al día es para primeros contactos, no para seguimientos, pero se espacian igual.
  - Mismas dos franjas que el lote 1: miércoles 6 de enero a las 10:00 y jueves 7 de enero a las 15:00, hora del Este (11:00 y 16:00 en Santo Domingo). El CEO las confirma con su agenda antes de cargarlos; si cambian, se cambian en los 13.
  - Si dos cuentas eligen la misma franja, la segunda recibe otra franja al contestarle.
- Una cuenta que respondió, aunque sea con una pregunta, no recibe el seguimiento. Se le contesta según el §6.

## 6. Qué hacer según la respuesta

| Respuesta | Siguiente paso |
|---|---|
| Sí, manda el vídeo | Contestar con el enlace y dos franjas para una llamada de 15 minutos. No se envía el correo 2. `ejecucion-fisica` prepara la OEF de la llamada con el guion de la plantilla. |
| ¿Cuánto cuesta? | El precio no se da por correo: "Depende del volumen de consultas. En una llamada de 15 minutos lo vemos con sus números y le envío la cifra por escrito" (cambio de riesgo del 21 nov: la cifra no se da en la llamada mientras `jurisdiccion` esté pendiente), más dos franjas. |
| Ya tengo una herramienta | Preguntar cuál y si responde en español por WhatsApp y agenda sola. Si es que sí a todo, cerrar con cortesía. |
| La correduría me impone sus herramientas | Cerrar con cortesía y anotarlo en la bandeja: es la lección que decide si se recuperan acevedo-team-exp y the-cuervo-team. |
| Baja / unsubscribe | `no_contactar` el mismo día. No se contesta. |
| Fuera de la oficina | Reintentar tras la fecha de vuelta, con al menos 5 días desde el último toque. |
| Rebote | `no_contactar`. No se prueba otra dirección. |

Cada envío, respuesta o baja se registra en `estado/pipeline.csv` solo cuando el CEO lo confirma en la bandeja, con el formato `cuenta_id | correo N | enviado AAAA-MM-DD` o `cuenta_id | respuesta | resumen`. Sin esa confirmación, nada cuenta como contacto.

## 7. Minutos estimados del CEO

Calculados con Python sobre los mismos supuestos del lote 1 [SUPUESTO]:
- 3 min por cada correo 1: confirmar la dirección, leer, poner la firma y enviar;
- 0 min de preparación de firmas: ya las montó el 7 de diciembre para el lote 1;
- la confirmación en pantalla de la dirección de met cabe en sus 3 minutos;
- 1,5 min por seguimiento.

| Bloque | Minutos |
|---|---|
| 8 dic (4 correos 1, tras los 3 del lote 1) | 12 |
| Correos 2 (15 dic, hasta 4) | 6 |
| Correos 3 (4 ene, hasta 4) | 6 |
| **Total del lote 1b** | **24 (0,4 h)** |

Con la alternativa del 9 de diciembre: 29 min (5 más por abrir otra sesión). Sumado al lote 1 (66 min), los dos lotes piden 90 min del CEO repartidos en cinco días. El 8 de diciembre la sesión pasa de 9 a 21 minutos. No incluye las llamadas.

## 8. Reglas que cumple este lote

- Cada correo 1 parte de una observación verificada en la ficha de esa cuenta. Ninguna frase habla de zonas, de ciudades ni de quién vive en ellas; valdivia y met no mencionan su ciudad.
- viva-orlando-realty no habla de compradores ni de vendedores: el asistente pregunta "buying or renting", que es un dato que da el propio cliente (decisión de la Directora del 21 nov).
- Ningún correo da precio. El correo 1 no lleva enlace; el correo 2 lleva uno solo (el vídeo).
- Texto plano, sin adjuntos ni imágenes, con asunto veraz. La firma identifica el correo como comercial y lleva la dirección postal y la línea de baja.
- Un solo mensaje por cuenta y día. Ninguna cuenta del lote tiene historial de contacto previo, y ninguna coincide con las del lote 1.
- 7 primeros contactos el 8 de diciembre (3 + 4), por debajo de `max_primeros_contactos_dia` (10).
- Ningún nombre inventado: los saludos usan nombres publicados por la propia cuenta o su perfil profesional.
- Los cuerpos no llevan "[Nombre]", "XXX" ni corchetes. Las únicas marcas son las de firma y `ENLACE-VIDEO`, y se sustituyen antes de cargar.
- Ningún correo menciona la ACD, "PYME", "SME" ni el empleador del CEO.
