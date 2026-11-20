# Acta de Activación · Línea EE. UU. · Primera Respuesta para inmobiliarias

Fecha: 2026-11-19 · Solicitud de aprobación: APR-005 · Revisada por riesgo: no.

La redactó Claude en el chat del CEO, a petición suya, a partir del plan que el CEO aceptó ese día. La primera sesión del equipo la revisa con `riesgo` y anota las objeciones en el reporte, sin bloquear el trabajo sin coste.

Contexto, fuentes y supuestos: `contexto/linea-eeuu-inmobiliarias.md`. Cálculos: `herramientas/embudo_eeuu.py`.

**Actualización del 2026-11-20, con las respuestas del CEO a las preguntas 9 a 11:**
- **Pregunta 9:** el flujo de WhatsApp de Primera Respuesta no existe. Estaba diseñado, no construido.
  - El CEO decidió construir una demo mínima antes de vender. Es una excepción a "activos primero" (CLAUDE.md §3), con un tope de 8 h (OEF-004).
  - Los envíos pasan del 30 nov al 7 dic.
- **Pregunta 10:** se cobra por PayPal. Las cifras de §8 ya descuentan su comisión.
- **Pregunta 11:** sin preferencia sobre la dirección de la firma. Se aplica por defecto un buzón virtual en EE. UU. (OEF-005).

## 1. Ángulo de activación elegido
- **Qué se vende.** Primera Respuesta, el producto diseñado para clínicas (WhatsApp Business API → n8n → Claude → Google Calendar), con otra base de conocimiento. Estaba sin construir: la demo mínima se construye antes de vender (OEF-004).
- **A quién.** Agentes y equipos inmobiliarios de Florida y Texas que ya atienden en español.
- **Por qué compraría.**
  - Cada consulta tardía es una operación que se enfría [SUPUESTO].
  - Sus clientes usan WhatsApp mucho más que la media: un 56 % de los adultos hispanos, frente al 32 % del total [VERIFICADO: Pew 2025, vía Sinch].
  - La alternativa es cara: un ISA humano cuesta entre 3.000 y 5.000 USD/mes [ESTIMADO: fuente secundaria], y Structurely parte de 499 USD/mes más 1.500 a 2.000 USD de alta [VERIFICADO: fitgap, aiproductivity].
- **En qué se diferencia.** En español primero, por WhatsApp y llave en mano.
- **Qué cambia frente a lo que no funcionó en España:**
  - mercado en USD;
  - un producto concreto en vez de un diagnóstico;
  - el mismo horario laboral que el cliente;
  - el primer correo pide permiso para enviar un vídeo en lugar de ofrecer una auditoría.

  El canal (correo en frío individual) se mantiene y se mide aparte con su propio corte (§12).

## 2. Activos que se usan y qué NO se construye
| Pieza | Activo | Comprobación |
|---|---|---|
| Producto y demo | Primera Respuesta / Atlas (`contexto/oferta-y-activos.md` §4): diseñado, sin construir [VERIFICADO: CEO, 19 nov] | **Excepción del CEO (20 nov):** demo mínima antes de vender, con tope de 8 h de construcción y 1 h de vídeo, y punto de parada (OEF-004). Lo único nuevo es la base de conocimiento, que ya está escrita. `oferta-entrega` deja anotada la excepción, no la firma como comprobación superada. |
| Infraestructura | La instancia de n8n que ya exista (VPS de Hostinger) o la prueba de n8n Cloud; número de prueba de WhatsApp Cloud API [SUPUESTO: confirmar] | Nada de pago salvo el uso de la API (tramo 1). |
| Dirección postal (CAN-SPAM) | — | Buzón virtual en EE. UU., hasta 80 USD por 3 meses (OEF-005). |
| Envío | `cuenta_envio`, borradores vía Microsoft 365 | Nada nuevo. |
| Embudo y caja | `pipeline.py` (con el canal `email_eeuu` y el corte de la línea), `caja.py` | Se añadió `embudo_eeuu.py` para los cálculos de esta Acta, que el equipo exige hacer con código. |
| Mensajes y llamada | `salidas/material/eeuu-inmobiliarias-plantillas.md` | Plantillas base; los borradores son por cuenta. |

**No se construye** sin una cuenta concreta que lo pida para firmar:
- una landing o una web en inglés;
- integraciones con CRMs inmobiliarios;
- SMS o voz;
- un panel de métricas;
- más funciones en la demo.

## 3. Misión del equipo
Que agentes y equipos inmobiliarios de EE. UU. con clientela hispanohablante respondan cada consulta en segundos y la conviertan en cita, y que lo paguen: al menos un cliente pagando antes del 2027-04-19.

## 4. Visión a 12 meses
Noviembre de 2027: 10 clientes activos y 3.000 USD/mes de recurrencia, unos 43.000 USD cobrados en el año. Es el escenario optimista de `embudo_eeuu.py`. El escenario base da 3,6 clientes y unos 15.500 USD cobrados [ESTIMADO, ver §7].

## 5. Estrategia
**Dónde jugamos.** Florida (Miami-Dade, Broward, Palm Beach, Orange) y Texas (Harris, Dallas, Tarrant, Bexar). Equipos de 3 a 15 agentes y agentes con volumen que ya atienden en español.

**Cómo ganamos.**
- Respuesta en segundos, en español y por WhatsApp.
- Llave en mano.
- Mensualidad por debajo del referente.
- Una demo de 60 segundos.

**Qué NO vamos a hacer:**
- SMS, WhatsApp ni llamadas en frío;
- comprar bases de datos;
- anuncios antes del tramo 2;
- otros verticales;
- integraciones antes del primer cobro;
- tocar la demo después de su tope de 8 h, hasta tener 10 conversaciones serias.

**Plan semanal:**
| Semana | Fechas | Hito | Métrica |
|---|---|---|---|
| S47 | 20–22 nov | El equipo cualifica las primeras 30 cuentas (Florida) | 30 fichas con señal en español y fricción [VERIFICADO + fuente] |
| S48 | 23–27 nov | OEF-004: construcción de la demo, hasta 6 h. No se envía nada: Thanksgiving es el jueves 26 | Avance de la demo |
| S49 | 30 nov–4 dic | OEF-004: demo terminada y vídeo. OEF-005: buzón. Lote 1 listo, con su APR | Enlace al vídeo y dirección activa |
| S50 | 7–11 dic | EXP-US-01: 30 primeros contactos en Florida, como máximo 10 al día | 30 contactos confirmados |
| S51 | 14–18 dic | Seguimientos +5 de EXP-US-01. EXP-US-02: 30 cuentas de Texas | Respuestas y conversaciones |
| S52–S53 | 21 dic–1 ene | Baja respuesta [SUPUESTO]. Los seguimientos +12 se mueven al 4 de enero; solo llamadas agendadas y cualificación | — |
| S1–S6 | 4 ene–12 feb | 30 primeros contactos por semana, con el ángulo que ganó; propuestas a quien encaje | Conversaciones, propuestas y pagos |
| S7 | 15–18 feb | **Control del día 90 (18 feb)** | Al menos 3 conversaciones serias o 1 cliente pagando |
| S8–S16 | 22 feb–19 abr | Mismo ritmo | **Límite (19 abr): al menos 1 cliente pagando** |

## 6. Cultura
1. **Vender antes de construir.** Sacrifica pulir la demo y el producto.
2. **Una observación verificada por cuenta.** Sacrifica volumen.
3. **El tiempo del CEO vale más que el del equipo: todo le llega listo para ejecutar.** Sacrifica que el equipo dedique más trabajo de preparación a cada minuto del CEO.
4. **Cumplimiento antes que velocidad** (CAN-SPAM, vivienda justa, datos). Sacrifica canales rápidos como el SMS o el WhatsApp en frío.
5. **Se corta en la fecha pactada.** Sacrifica la esperanza de que "funcione con un poco más".

## 7. Embudo esperado
Volumen: 30 primeros contactos por semana, por el tope de 10 al día y la cuenta única. Conversiones por paso [SUPUESTO]:

| Escenario | Respuesta / contacto | Conversación / respuesta | Propuesta / conversación | Pago / propuesta |
|---|---|---|---|---|
| Pesimista | 3 % | 30 % | 40 % | 25 % |
| Base | 5 % | 40 % | 50 % | 30 % |
| Optimista | 8 % | 50 % | 60 % | 35 % |

Referencia propia: en España respondieron 5 de 64 cuentas (7,8 %) y ninguna llegó a conversación seria [VERIFICADO: `pipeline.py`].

**Salida de `embudo_eeuu.py`** (valores esperados). Recalculada el 20 nov con los envíos desde el 7 dic: construir la demo antes cuesta una semana de venta.

| Momento | Contactos | Pesimista | Base | Optimista |
|---|---|---|---|---|
| Control del 18 feb (7 semanas útiles): conversaciones | 210 | 1,9 | 4,2 | 8,4 |
| Día 90 (5 semanas útiles con ciclo de 4 semanas): clientes | 150 | 0,13 | 0,45 | 1,26 |
| Límite del 19 abr (13 semanas útiles): clientes | 390 | 0,35 | 1,17 | 3,28 |

**Probabilidad de tener al menos un cliente** [ESTIMADO: Poisson sobre el valor esperado]:
- al día 90: 12 % / 36 % / 72 %;
- al día 150: 30 % / 69 % / 96 %.

**Por eso:**
- el control del día 90 mide conversaciones, que es lo que separa el escenario pesimista del base;
- el cliente pagando se exige al día 150.

## 8. Economía unitaria
Salida de `embudo_eeuu.py`, con 2.500 USD de implantación, 300 USD/mes y 6 meses medios de mantenimiento en el año. Costes:
- coste directo de 70 USD/mes por cliente [SUPUESTO];
- 10 h de implantación [SUPUESTO];
- 1 h/mes de mantenimiento [SUPUESTO];
- 4 h/semana de venta [SUPUESTO];
- la hora del CEO a 40 USD;
- comisión de PayPal del 5,4 % sobre lo cobrado [ESTIMADO: comparalatam.com, fuente secundaria; verificar en paypal.com/do]. No incluye la conversión a pesos (3–4 % [ESTIMADO]) ni los 100 DOP por retiro a un banco dominicano [VERIFICADO: Diario Libre, 2022].

**Por cliente, primer año:**
- ingreso neto de comisión 4.068 − directos 420 − horas del CEO 640 = **margen de contribución de 3.008 USD**;
- mantenimiento: 174 USD/mes de margen.

**Coste sombra de adquisición:**
| Escenario | Cada cuántos contactos sale un cliente | Coste de adquisición | Margen tras adquisición |
|---|---|---|---|
| Base | 333 | 1.778 USD | 1.230 USD |
| Pesimista | 1.111 | — | −2.918 USD |
| Optimista | — | — | 2.373 USD |

**Con una implantación de 1.500 USD:** margen de contribución de 2.062 USD; en el base, 284 USD tras adquisición.

**A 12 meses:**
| Escenario | Clientes | Cobrado (neto de comisión) | Neto tras el coste sombra |
|---|---|---|---|
| Base | 3,6 | 14.644 USD | 4.428 USD |
| Pesimista | 1,1 | — | −3.152 USD |
| Optimista | 10,1 | — | 23.919 USD |

`finanzas-control` sustituye los supuestos por costes reales cuando existan.

## 9. Quién vende y cierra
**El equipo:**
- cualifica 30 cuentas por semana;
- redacta los borradores y los deja en Outlook;
- prepara cada llamada y la propuesta de una página;
- registra el embudo.

**El CEO** envía, llama, cierra y cobra.

**Horas del CEO por semana** (máximo 6):
- S48: hasta 6 h de OEF-004.
- S49: el resto de OEF-004, como máximo 3 h, más 1 h de OEF-005 y 30 min para revisar el lote 1.
- Desde S50: hasta 4 h:
  - envíos y seguimientos: unos 20 minutos al día;
  - llamadas: hasta 2 h;
  - bandeja y lote: 30 min.

## 10. Organigrama y subequipos previstos
Sin cambios: los seis líderes y ningún subequipo. Si la cualificación no llega a 30 cuentas por semana, `inteligencia-comercial` puede pedir un subequipo temporal con las reglas de CLAUDE.md §6.

## 11. Presupuesto por tramos
| Tramo | Importe | Condición de liberación | Uso previsto |
|---|---|---|---|
| 1 | Hasta 1.000 USD (`tramo_1_max_comprometido`) | Aprobación de esta Acta | Demo (OEF-004): hasta 100 USD [ESTIMADO]. Buzón postal virtual en EE. UU. para la firma (OEF-005): hasta 80 USD por 3 meses [ESTIMADO: 9,99 USD/mes más 37 USD de notarización]. Revisión profesional del contrato de servicio y de la cláusula de datos: hasta 400 USD [SUPUESTO], solo cuando haya una propuesta aceptada (APR). Total previsto: hasta 580 USD. |
| 2 | Hasta 1.000 USD más | Primer cobro | Prueba de anuncios en español: hasta 600 USD, 14 días, y solo si el correo ya produjo al menos 1 conversación seria (APR). Técnico de n8n para entregar y liberar horas del CEO: hasta 400 USD (APR). |
| 3 | 400 USD | Tercer cliente o 900 USD/mes de recurrencia | Lo que el Comité proponga, con APR. |
| Reserva | 600 USD | Solo con aprobación expresa del CEO | — |

Diferencias con el plan del chat del 19 nov, ya incorporadas:
- No hay base de datos de pago: CLAUDE.md §4 prohíbe comprar bases de datos personales.
- Los anuncios pasan al tramo 2: primero hay que demostrar que el mensaje convierte.

## 12. Primeros experimentos
**EXP-US-01 · Florida, correo en el idioma de la web.** Primer correo sin enlace y vídeo en el segundo.
- **Hipótesis:** un correo con una observación concreta y una oferta en español obtiene interés de agentes que ya atienden en español.
- **Cuentas:** las 30 primeras cualificadas en Florida.
- **Presupuesto:** 0 USD y unas 2 h del CEO.
- **Duración:** 14 días desde el primer envío (7–21 dic). El seguimiento +12 cae en fiestas y se mueve al 4 de enero, así que el veredicto se lee con esa salvedad.
- **Éxito:** al menos 2 respuestas de interés (sin contar bajas ni respuestas automáticas) o al menos 1 conversación seria.
- **Abandono:** 0 respuestas de interés. El siguiente lote cambia de ángulo, no solo de redacción.

**EXP-US-02 · Texas, mismo mensaje.** 30 cuentas, del 14 al 28 de diciembre, con las mismas métricas y la misma salvedad por las fiestas. Sirve para comparar los dos estados.

**EXP-US-03 · Ángulo alternativo**, solo si EXP-US-01 y EXP-US-02 suman menos de 2 respuestas de interés. Lo decide el Comité. Opciones:
- en inglés, centrado en los leads de portales que llegan de noche;
- mensajes directos en Instagram enviados por el CEO a 20 cuentas (1,5 h).

**Corte de la línea** (en `pipeline.py`, sobre el canal `email_eeuu`):
- Si 60 cuentas llevan más de 14 días desde el primer contacto y hay menos de 3 respuestas, ninguna conversación seria y ningún pago, no se sube volumen: se cambia de ángulo o de mensaje.
- El corte general de 30 cuentas y 5 conversaciones se mantiene para los canales de España. En EE. UU. saltaría a los tres días de envío, antes de que lleguen las respuestas.

## 13. Ángulos descartados
- **SMS o WhatsApp en frío:** el SMS exige registro A2P 10DLC; el WhatsApp en frío necesita consentimiento previo; y quemaría la reputación.
- **Comprar bases de datos:** prohibido (CLAUDE.md §4).
- **Anuncios desde el día 1:** primero hay que validar el mensaje; pasan al tramo 2.
- **Med spas y clínicas en EE. UU.:** manejan datos de salud, con más exigencias legales.
- **Agencias de seguros:** cada cliente vale menos y miran más el precio [SUPUESTO].
- **Contratistas:** sus clientes llaman por teléfono, así que pedirían voz.
- **Construir integraciones con CRMs:** sería construir sin demanda.

## 14. Disensos del Comité
El Acta no ha pasado por el Comité. La primera sesión registra aquí el dictamen de `riesgo` y la nota de `oferta-entrega`.

Disenso ya registrado, del 20 nov. Claude, en el chat, recomendó vender primero y construir la demo cuando una cuenta pidiera verla, como manda "activos primero". El CEO eligió construir la demo antes. Coste estimado de su opción:
- una semana menos de venta antes del control;
- un día 90 con un 36 % de probabilidad de cliente en el escenario base, frente al 42 % anterior.

Beneficio esperado: más credibilidad en el correo y menos riesgo de entrega.

## 15. Pre-mortem
"Llegó el 19 de abril de 2027 sin clientes pagando. ¿Por qué?"

1. **Los lotes no salieron.** La bandeja estuvo sin respuesta del CEO del 2 al 19 de noviembre.
   - Mitigación:
     - lotes de 20 minutos al día ya listos en Outlook;
     - aprobación con una sola línea por lote;
     - el CEO puede responder desde el chat y su respuesta llega por PR;
     - disparador 4.
2. **Los agentes no leen correos de proveedores.**
   - Mitigación:
     - una observación concreta y en español;
     - sin enlace en el primer toque;
     - vídeo corto;
     - cambio de ángulo al llegar a 60 cuentas maduras;
     - EXP-US-03.
3. **Desconfianza hacia un proveedor remoto sin casos en EE. UU.**
   - Mitigación:
     - videollamada y demo en vivo;
     - mensualidad por debajo del referente;
     - garantía de devolución de la implantación cuando el contrato esté validado;
     - regla de bajar la implantación a 1.500 USD tras tres rechazos por precio.

4. **La demo se comió las semanas de venta**, el patrón documentado de construir y refinar.
   - Mitigación:
     - tope de 8 h y punto de parada en OEF-004;
     - alcance cerrado;
     - la demo no se toca hasta tener 10 conversaciones serias;
     - si se llega al tope sin terminar, el Comité propone delegar o vender sin demo.

Riesgos secundarios:
- La demo no funciona: punto de parada en OEF-004.
- La primera implantación tarda más de lo prometido: antes de la primera propuesta, `oferta-entrega` fija el plazo contando la verificación del número del cliente en Meta [SUPUESTO].
- El cobro en USD no está resuelto: `jurisdiccion` bloquea la primera propuesta con precio y se pregunta ya.

## 16. Política de beneficios
- Se reinvierte el 100 % hasta reponer lo gastado y llegar a 900 USD/mes de recurrencia.
- Después: 50 % de reinversión, 20 % a la reserva y 30 % al CEO [SUPUESTO; lo fija el CEO].

## 17. Disparadores de cierre de la línea
Cada uno lleva a una propuesta de cierre o de pausa de la línea, con APR. Mientras el CEO decide, se congela el gasto nuevo.
1. **18 feb 2027:** menos de 3 conversaciones serias y ningún cliente pagando (`pipeline.py` lo avisa).
2. **19 abr 2027:** ningún cliente pagando (`pipeline.py` lo avisa).
3. **990 USD gastados sin ingresos.**
4. **7 días sin respuesta del CEO** teniendo un lote o una OEF pendientes. El equipo pasa a reportes de tres líneas, lo dice en el primero y no genera lotes nuevos.
5. **Una queja formal por spam** o una señal de mala reputación en el dominio de `cuenta_envio`: se paran los envíos y se revisa.
