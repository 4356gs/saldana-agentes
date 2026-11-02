---
cuenta_id: bodegas-albamar
tipo: guion en dos conversaciones (para la OEF de `ejecucion-fisica`)
interlocutor: Xurxo, Bodegas Albamar (Cambados). Cargo sin verificar: confirmarlo en el minuto 2 de la llamada 1
comprobacion: `python3 herramientas/pipeline.py --puede-contactar bodegas-albamar`, ejecutado el 2026-11-02 a las 11:59 CET → `SÍ: sin bloqueos`
estado: BORRADOR. Correcciones de riesgo del 2026-11-02 incorporadas
---

## Secuencia

1. **Llamada 1 (20 min):** descubrimiento y oferta del mini-diagnóstico gratuito. **No se habla de carta de intención.**
2. **Entrega del mini-diagnóstico por escrito** en la fecha acordada en la llamada 1.
3. **Conversación 2 (20 min):** repasar el diagnóstico con él delante. Solo aquí, y solo si se cumplen las condiciones de intención real, se plantea la carta.

Esto aplica la regla anticomplacencia del Acta de Activación (§1): no se pide una LOI a nadie sin una conversación seria y un diagnóstico entregado antes.

## Llamada 1

**Objetivo:** que sea una conversación seria (CLAUDE.md §8: con el decisor y sobre un problema concreto suyo) y salir con la fecha de entrega del diagnóstico.

**Qué tener delante (5 minutos antes):** el hilo de correo de agosto a octubre y lo que `inteligencia-comercial` haya verificado sobre el dominio. Si el diagnóstico aún no está, no se improvisa: se promete para dentro de 5 días hábiles.

**Min 0–2. Apertura**
- "Gracias por sacar el rato, Xurxo, y perdona que tardara en escribirte por WhatsApp. Tengo 20 minutos apuntados. ¿Te sigue yendo bien?"
- "Para no hacerte perder el tiempo: te cuento en un minuto qué hago, te hago unas preguntas sobre cómo os entra la venta y, si tiene sentido, te digo qué te puedo mandar."

**Min 2–4. Quién decide y en qué punto están**
- "¿Qué papel tienes tú en la bodega? ¿Las decisiones sobre la web y la venta las tomas tú?" (Si no es el decisor, el objetivo pasa a ser que nos presente a quien lo es.)
- "¿Cómo ha ido la campaña? ¿Ya está todo cerrado?"

**Min 4–12. Descubrimiento (que hable él al menos el 70% del tiempo)**
- "Cuando alguien quiere comprar o visitar Albamar, ¿por dónde os llega hoy? ¿Teléfono, correo, Instagram, la tienda, distribuidores?"
- "En agosto vi que el dominio no cargaba. ¿Cómo está ahora? ¿Notasteis algo, os escribió alguien diciendo que no os encontraba?"
- "¿Qué parte de lo que vendéis va en venta directa y qué parte a distribución? Me basta con una idea aproximada." (Se apunta como estimación del propio cliente y no se discute.)
- "¿Qué es lo que más tiempo os quita fuera de la viña y la bodega: pedidos, visitas, facturas, contestar mensajes?"
- "Si para la próxima campaña pudieras arreglar una sola cosa de cómo os llegan los clientes, ¿cuál sería?"

Se apunta literalmente el problema que él nombre.

**Min 12–17. Devolver valor**
- "Lo que hago es medir dónde se pierden ventas entre que alguien os busca y que acaba comprando, con datos públicos primero. Te propongo esto: te preparo gratis un diagnóstico de una página sobre Albamar (ficha de Google, web, directorios, cómo estáis frente a bodegas parecidas de la zona, sin nombrarlas) y te lo mando en 5 días hábiles. Sin compromiso."
- Si dice que sí, se fija en la llamada la fecha de envío y la de la conversación 2 para repasarlo.

**Min 17–20. Cierre**
- Si pregunta qué viene después: "El paso siguiente sería una auditoría completa: nueve indicadores, las fugas cuantificadas con supuestos que ves tú, una hoja de ruta ordenada por retorno. Son 1.290 € para bodegas, con la sesión de una hora incluida. Para bodegas suele encajar en enero o febrero, con la campaña cerrada." No se insiste si no pregunta.
- Repetir en voz alta las dos fechas acordadas: la de envío del diagnóstico y la de la conversación 2.

## Conversación 2 (tras entregar el diagnóstico)

**Min 0–12.** Repasar el diagnóstico: qué le sorprende, qué confirma, qué no le encaja. Volver al problema que nombró en la llamada 1.

**Min 12–16.** Si hay interés: "Lo que has visto es la parte externa. La auditoría completa mide también lo de dentro y te deja la hoja de ruta. Son 1.290 € para bodegas, con la sesión de una hora incluida. ¿Te encajaría hacerla en enero o febrero?"

**Señales de intención real** (se cuentan a lo largo de las dos conversaciones; hacen falta al menos 3 de 4, y una tiene que ser la 1):
1. Es quien decide, o lo decide con alguien concreto que ha estado en la conversación.
2. Ha nombrado un problema propio, con sus palabras.
3. Dice que enero o febrero le encaja, o propone otra fecha.
4. Pregunta por el contenido, el alcance o cómo se trabajaría.

**Min 16–20. Cierre. Dos ramas**

*Rama A: 3 o más señales, incluida la 1.*
- "Te comento algo con transparencia, y dime con total libertad si no te encaja. Estoy recogiendo cartas de intención de empresas españolas que quieren trabajar con Saldaña Digital, y esas cartas se presentarán en un trámite ante la administración española. Sería una carta no vinculante en la que dices, si es tu intención, que quieres hacer la auditoría en enero o febrero. No te compromete a pagar ni a una fecha cerrada. La redacción final la valida quien lleva ese trámite y tú la revisas antes de firmar, para que diga solo lo que tú piensas. ¿Te parecería bien que te la pase?"
- Si dice que sí: "Te la mando para que la leas con calma y cambies lo que no refleje tu intención." (El texto no sale hasta que lo valide quien lleva el expediente.)
- Si duda o dice que no: "Sin problema, de verdad." No se insiste, ni en esa conversación ni después.

*Rama B: menos de 3 señales, o falta la 1.*
- No se menciona ninguna carta. "Si te sirve, hablamos en enero cuando cerréis el año." Si no es el decisor, se pide que nos presente a quien lo es.

## Qué NO se promete ni se dice

- Ningún precio distinto de "1.290 € para bodegas, con la sesión de una hora incluida". Nada de "desde 900 €", descuentos, "gratis si firmas", ni precios de implantación o de acompañamiento.
- Ninguna mención a la carta de intención en la llamada 1.
- Ningún tono de favor personal ("me sirve mucho", "me ayudarías"). La carta no se presenta como un favor ni se oculta para qué es.
- Ninguna cifra de retorno ni de ventas recuperadas antes del diagnóstico.
- Ni visitas presenciales ni fechas de entrega que `oferta-entrega` no haya confirmado.
- Nada de redactar la carta por él con condiciones que no ha dicho.
- No se nombra al empleador del CEO. No se dice "PYME". No se da asesoramiento legal, fiscal ni migratorio.
- No se habla de logística, reparto ni almacén como servicio (`conflictos_excluidos`).

## Después de cada conversación (lo reporta el CEO en la bandeja)

`fecha | bodegas-albamar | conversacion | quién estaba, problema nombrado, señales de intención (1–4), qué se acordó y fechas`

Con eso, `desarrollo-negocio` registra el evento. Tras la llamada 1, `inteligencia-comercial` cierra el diagnóstico. Solo si la conversación 2 fue rama A, se prepara el borrador de carta marcado "pendiente de validar por el expediente".
