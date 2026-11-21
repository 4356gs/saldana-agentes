# Borrador · viva-orlando-realty · lote 1b EE. UU. (EXP-US-01)

Preparado: 2026-11-21 · desarrollo-negocio · canal `email_eeuu` · vertical `inmobiliaria` · Aprobación: APR-007 (lote 1b entero; número propuesto, lo asigna la Directora).
Envío previsto del correo 1: martes 8 de diciembre de 2026, 11:00 hora del Este. Ficha: `cuentas/viva-orlando-realty.md`.

## Comprobación previa

`python3 herramientas/pipeline.py --puede-contactar viva-orlando-realty` (2026-11-21):

```
SÍ: sin bloqueos
```

Repetirla el día del envío: si responde NO, este borrador no se carga.

## Destinatario

- **Para:** milena@vivaorlando.com
- **Quién:** Milena Valle, Broker (cargo rotulado en la página de equipo) de Viva Orlando Realty, Inc.
- **Fuente del correo y de la observación:** https://www.vivaorlando.com/our-team y https://www.vivaorlando.com/en-espanol
- **Idioma y registro:** Inglés. La web principal y la página de equipo, donde están la broker, los WhatsApp y el formulario, están en inglés [VERIFICADO: https://www.vivaorlando.com/our-team, según la ficha]. La página "En Espanol" existe, pero describe la rama de alquileres, y el español de la broker no está verificado. La ficha recomienda español; se elige inglés por la regla del lote (idioma de la web principal, como en leonard-real-estate-group) y porque escribir en español sobre la venta se apoyaría en algo no verificado. Si el CEO prefiere español, lo reescribe `desarrollo-negocio` con registro usted y `FIRMA-ES-USTED`, no a mano.
- **Alcance (decisión de la Directora, 21 nov):** cualifica por el perfil bilingüe de sus agentes; la rama de alquileres no la excluye. El correo no habla de compradores ni de vendedores: la ficha no respalda en qué proporción atiende cada uno. Por eso las preguntas del asistente se escriben como "buying or renting", que es un criterio que da el propio cliente (vivienda justa).

## Correo 1 · día 0 · sin enlace

**Asunto:** After-hours Spanish inquiries · Viva Orlando Realty

```
Hi Milena,

I noticed your contact form promises to get back "as soon as possible," and six agents on your team page list their own WhatsApp, with nothing saying who answers after hours.

I built an assistant for real estate teams that answers WhatsApp inquiries within seconds, in Spanish or English (it can also be connected to a website chat). It asks the questions your team would ask (buying or renting, area, budget, and timeline) and books the call or showing on your Google Calendar. Your team steps in once the lead is qualified.

Want me to send a 60-second video of it working?

FIRMA-EN
```

## Por qué este mensaje a esta cuenta

Nueve agentes, broker nombrada y correo propio. La fricción es doble y está a la vista: un formulario sin plazo y seis WhatsApp personales, cada uno dependiente de que su agente esté disponible. El asistente centraliza esa entrada sin quitarle el lead a ningún agente. La frase de cualificación cambia respecto a la plantilla ("buying or renting" en vez de "pre-approved") para no presuponer que la consulta es de compra.

## Correo 2 · día +5 (ver fechas en LOTE.md) · solo si no respondió

Se crea como respuesta al correo 1, en el mismo hilo. Si no se puede, el asunto va sin "Re:".

**Asunto:** Re: After-hours Spanish inquiries · Viva Orlando Realty

```
Hi Milena,

Here's the video in case it's useful: ENLACE-VIDEO

Someone messages at 10:40 p.m. about a home. The assistant replies within seconds, asks four questions, and the showing lands on the agent's calendar.

When a lead writes to one of your agents' WhatsApp at that hour, who picks it up today?

FIRMA-EN
```

## Correo 3 · 4 de enero · cierre · solo si no respondió

Mismo hilo. Las dos franjas se confirman con la agenda del CEO antes de cargarlo (en Santo Domingo son las 11:00 y las 16:00).

**Asunto:** Re: After-hours Spanish inquiries · Viva Orlando Realty

```
Hi Milena,

The math worth doing: how many Spanish-speaking inquiries go cold each month because the reply came late, and what each one is worth. Happy to run it with your numbers in 15 minutes: Wednesday, January 6 at 10:00 a.m. or Thursday, January 7 at 3:00 p.m. (Eastern).

If now isn't the time, I won't write again about this.

FIRMA-EN
```

## Siguiente paso según responda o no

- **Sí, manda el vídeo:** contestar con el enlace y dos franjas para una llamada de 15 minutos; no se envía el correo 2. Registrar `respuesta` cuando el CEO lo confirme en la bandeja.
- **Pregunta el precio:** no se da por correo. Contestar que depende del volumen de consultas y que en 15 minutos se da una cifra cerrada, con dos franjas.
- **Ya tengo una herramienta:** preguntar cuál y si responde en español por WhatsApp y agenda sola; si es que sí a todo, cerrar con cortesía.
- **Baja / unsubscribe:** `no_contactar` el mismo día; no se contesta.
- **Fuera de la oficina:** reintentar tras la fecha de vuelta, con al menos 5 días desde el último toque.
- **Rebote:** `no_contactar`; no se prueba otra dirección (tampoco info@).
- **Sin respuesta:** correo 2, después correo 3, y la cuenta queda en reposo.
- **Específico de esta cuenta:** Si responde en español, seguir en español (usted). Si su interés es la gestión de alquileres para propietarios (Viva Orlando Rentals), eso es otro producto y queda fuera (gestoras de alquiler excluidas, contexto §3): cerrar con cortesía y anotarlo en la bandeja. En la llamada, el asistente solo cualifica por lo que pide el cliente (compra o alquiler, zona, presupuesto, plazo y financiación).
