# Plantillas base · Línea EE. UU. (inmobiliarias)

Revisadas por riesgo el 2026-11-20 (objeciones 1, 2, 4 y 14 aplicadas). Son plantillas, no borradores. `desarrollo-negocio` escribe cada borrador para una cuenta concreta, con su observación verificada, y `riesgo` lo revisa. Las llaves `{así}` marcan lo que se sustituye: ningún borrador sale con llaves ni corchetes (CLAUDE.md §8).

Reglas que aplican a todos los correos:
- **Formato:** texto plano, sin adjuntos ni imágenes y como máximo un enlace (CLAUDE.md §4).
- **Primer correo sin enlace.** El vídeo va en el segundo.
- **Precio:** ninguno en el correo. Se da en la llamada.
- **Seguimientos:** a los 5 y a los 12 días. El borrador se crea como respuesta al correo enviado, en el mismo hilo; solo así lleva "Re:". Si no se puede, el asunto va sin "Re:" (CAN-SPAM: asunto veraz).
- **Identificación comercial:** la firma incluye la línea "Este es un correo comercial de Saldaña Digital" (riesgo, 20 nov).
- **Teléfono:** si es un número de República Dominicana se indica así: "{teléfono} (WhatsApp · República Dominicana)", o se omite.
- **Registro:** el mismo en todo el correo (tú o usted), según el tono de la web de la cuenta.
- **Firma:** completa, con la dirección postal física válida (CAN-SPAM) y la línea de baja.
- **Vivienda justa:** ninguna frase sobre quién vive en una zona.
- **Sin promesas de resultados.** Saldaña Digital no tiene todavía clientes inmobiliarios en EE. UU.: no se escribe "trabajo con equipos" ni se citan casos.
- **"Monté un asistente".** El correo 1 lo dice, así que solo se envía con la OEF-004 hecha, es decir, con la demo funcionando. Si el Comité activa el plan B sin vídeo, `desarrollo-negocio` reescribe esa frase para no afirmar que el asistente ya existe. Si la OEF-004 la termina un técnico delegado, la frase pasa a "Tengo montado un asistente" / "I have an assistant set up".

## Firma

```
Gelo Saldaña
Saldaña Digital · Automatización comercial
{teléfono profesional}
{dirección postal física válida}

Este es un correo comercial de Saldaña Digital.
Si prefieres no recibir más correos míos, contéstame "baja" y no vuelvo a escribirte.
```

```
Gelo Saldaña
Saldaña Digital · Sales automation
{business phone}
{valid physical postal address}

This is a commercial message from Saldaña Digital.
If you'd rather not hear from me again, reply "unsubscribe" and I won't write again.
```

## Correo 1 · día 0 · sin enlace

**ES**

Asunto: Consultas en español fuera de horario · {nombre del equipo}

```
Hola {nombre},

{observación verificada, una sola frase; por ejemplo: "Vi que en su web invitan a escribir por WhatsApp para atención en español, y que el formulario de contacto no promete respuesta inmediata."}

Monté un asistente para equipos inmobiliarios que contesta por WhatsApp en segundos, en español o en inglés (también puede conectarse al chat de la web). Hace las preguntas que haría tu equipo (zona, presupuesto, plazo y si ya tiene preaprobación) y deja la llamada o la visita agendada en tu Google Calendar. Tu equipo entra cuando el cliente ya está calificado.

¿Te mando un vídeo de 60 segundos donde se ve funcionando?

{firma ES}
```

**EN**

Subject: After-hours Spanish inquiries · {team name}

```
Hi {name},

{verified observation, one sentence}

I built an assistant for real estate teams that answers WhatsApp inquiries within seconds, in Spanish or English (it can also be connected to a website chat). It asks the questions your team would ask (area, budget, timeline, and whether they're pre-approved) and books the call or showing on your Google Calendar. Your team steps in once the lead is qualified.

Want me to send a 60-second video of it working?

{firma EN}
```

## Correo 2 · día +5 · con el enlace

Se envía si no hubo respuesta. Si la cuenta respondió que sí, se le manda el vídeo en la respuesta y no se envía este correo.

**ES**

Asunto: Re: Consultas en español fuera de horario · {nombre del equipo}

```
Hola {nombre},

Te dejo el vídeo por si te sirve: {enlace al vídeo}

Alguien escribe a las 10:40 de la noche preguntando por una casa. El asistente le contesta en segundos, le hace cuatro preguntas y la visita queda en el calendario del agente.

¿Cuánto tarda hoy tu equipo en contestar una consulta que entra a esa hora?

{firma ES}
```

**EN**

Subject: Re: After-hours Spanish inquiries · {team name}

```
Hi {name},

Here's the video in case it's useful: {video link}

Someone messages at 10:40 p.m. about a home. The assistant replies within seconds, asks four questions, and the showing lands on the agent's calendar.

How long does your team take today to answer an inquiry that comes in at that hour?

{firma EN}
```

## Correo 3 · día +12 · cierre

**ES**

Asunto: Re: Consultas en español fuera de horario · {nombre del equipo}

```
Hola {nombre},

La cuenta que vale la pena hacer: cuántas consultas en español se enfrían al mes por contestar tarde, y cuánto vale cada una. Si quieres, la hacemos con tus números en 15 minutos: {dos franjas concretas, en la hora local de la cuenta (del Este o del Centro)}.

Si no es el momento, no vuelvo a escribirte sobre esto.

{firma ES}
```

**EN**

Subject: Re: After-hours Spanish inquiries · {team name}

```
Hi {name},

The math worth doing: how many Spanish-speaking inquiries go cold each month because the reply came late, and what each one is worth. Happy to run it with your numbers in 15 minutes: {two specific slots, in the account's local time (Eastern or Central)}.

If now isn't the time, I won't write again about this.

{firma EN}
```

## Qué hacer según la respuesta

| Respuesta | Siguiente paso |
|---|---|
| Sí, manda el vídeo | Contestar con el enlace y dos franjas para una llamada de 15 minutos. Se registra `respuesta` cuando el CEO lo confirme en la bandeja. |
| Ya tengo una herramienta | Preguntar cuál y si responde en español por WhatsApp y agenda sola. Si la respuesta es sí a todo, la cuenta se cierra con cortesía. |
| ¿Cuánto cuesta? | "Depende del volumen de consultas. En una llamada de 15 minutos te doy una cifra cerrada", más dos franjas. |
| Baja / unsubscribe | Marcar `no_contactar` el mismo día. No se contesta. |
| Fuera de la oficina | Reintentar después de la fecha de vuelta, siempre que hayan pasado al menos 5 días desde el último toque. |
| Rebote | Marcar `no_contactar`. No se reintenta con otra dirección adivinada. |

## Guion de la llamada de 15 minutos

Lo usa el CEO. `ejecucion-fisica` lo incorpora a cada OEF de llamada con los datos de la cuenta.

1. **Encuadre (1 min).** "Gracias por el rato. La idea es entender cómo les llegan hoy las consultas y ver si el asistente encaja. Si no encaja, te lo digo."
2. **Preguntas (7 min).**
   - ¿Cuántas consultas reciben por semana, y por dónde: WhatsApp, web, portales, redes?
   - ¿Qué parte llega en español?
   - ¿Quién contesta hoy y en cuánto tiempo? ¿Y de noche o un sábado?
   - ¿Qué pasa con una consulta que entra un sábado a las 10 de la noche?
   - ¿Cuántas visitas o llamadas agendan por semana?
   - ¿Qué vale para ustedes una operación cerrada?
   - ¿Usan Google Calendar? ¿Y qué CRM?
3. **Demo (4 min).** El vídeo o la demo en vivo. Al enseñarla, se dice que el asistente no pregunta ni comenta nada sobre quién vive en una zona (vivienda justa).
4. **Cierre (3 min).**
   - Si encaja, se da el precio de lista y se propone el siguiente paso: una propuesta de una página en 48 horas, con un plazo de implantación cerrado. Ese plazo lo fija antes `oferta-entrega`, contando la verificación del número del cliente en Meta. En la llamada no se promete un plazo.
   - El cobro es por PayPal.
   - No se promete un número de citas ni de operaciones.
   - No se habla de garantía hasta que el contrato esté validado.

**Encaja si** se cumplen las tres condiciones:
- recibe al menos unas 20 consultas por semana [SUPUESTO];
- una parte relevante llega en español o por WhatsApp;
- quien está en la llamada decide.

**Qué no se dice:**
- nada sobre zonas, vecindarios o perfiles de compradores;
- nada sobre el empleador del CEO: se habla de "más de 20 años implantando tecnología en multinacionales de logística y telecomunicaciones";
- ningún caso o cliente que no exista.
