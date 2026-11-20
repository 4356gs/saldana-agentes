# Acta de Activación · Línea EE. UU. · Primera Respuesta para inmobiliarias

Fecha: 2026-11-19 · Solicitud de aprobación: APR-005 · Revisada por riesgo: no.

La redactó Claude en el chat del CEO, a petición suya, a partir del plan que el CEO aceptó ese día. La primera sesión del equipo la revisa con `riesgo` y anota las objeciones en el reporte, sin bloquear el trabajo sin coste.

Contexto, fuentes y supuestos: `contexto/linea-eeuu-inmobiliarias.md`. Cálculos: `herramientas/embudo_eeuu.py`.

## 1. Ángulo de activación elegido
- **Qué se vende.** Primera Respuesta, el producto ya definido para clínicas (WhatsApp Business API → n8n → Claude → Google Calendar), con otra base de conocimiento.
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
| Producto y demo | Primera Respuesta / Atlas (`contexto/oferta-y-activos.md` §4) | Solo se adapta la base de conocimiento (OEF-004, como máximo una semana). `oferta-entrega` firma la comprobación de "activos primero" en la primera sesión. |
| Infraestructura | VPS de Hostinger con n8n, el mismo de Pazo do Val [SUPUESTO: confirmar] | Nada nuevo. |
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
- tocar la demo después de su semana.

**Plan semanal:**
| Semana | Fechas | Hito | Métrica |
|---|---|---|---|
| S47 | 20–22 nov | El equipo cualifica las primeras 30 cuentas (Florida) y prepara el lote 1 | 30 fichas con señal en español y fricción [VERIFICADO + fuente] |
| S48 | 23–27 nov | OEF-004: demo y vídeo. No se envía nada: Thanksgiving es el jueves 26 | Enlace al vídeo en la bandeja |
| S49 | 30 nov–4 dic | EXP-US-01: 30 primeros contactos en Florida, como máximo 10 al día | 30 contactos confirmados |
| S50 | 7–11 dic | Seguimientos +5. EXP-US-02: 30 cuentas de Texas | Respuestas y conversaciones |
| S51 | 14–18 dic | Cierre de EXP-US-01 y seguimientos +12 | Veredicto de EXP-US-01 |
| S52–S53 | 21 dic–1 ene | Baja respuesta [SUPUESTO]: solo llamadas agendadas y cualificación | — |
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

**Salida de `embudo_eeuu.py`** (valores esperados):

| Momento | Contactos | Pesimista | Base | Optimista |
|---|---|---|---|---|
| Control del 18 feb (8 semanas útiles): conversaciones | 240 | 2,2 | 4,8 | 9,6 |
| Día 90 (6 semanas útiles con ciclo de 4 semanas): clientes | 180 | 0,16 | 0,54 | 1,51 |
| Límite del 19 abr (14 semanas útiles): clientes | 420 | 0,38 | 1,26 | 3,53 |

**Probabilidad de tener al menos un cliente** [ESTIMADO: Poisson sobre el valor esperado]:
- al día 90: 15 % / 42 % / 78 %;
- al día 150: 32 % / 72 % / 97 %.

**Por eso:**
- el control del día 90 mide conversaciones, que es lo que separa el escenario pesimista del base;
- el cliente pagando se exige al día 150.

## 8. Economía unitaria
Salida de `embudo_eeuu.py`, con 2.500 USD de implantación, 300 USD/mes y 6 meses medios de mantenimiento en el año. Costes [SUPUESTO]:
- coste directo de 70 USD/mes por cliente;
- 10 h de implantación;
- 1 h/mes de mantenimiento;
- 4 h/semana de venta;
- la hora del CEO a 40 USD.

**Por cliente, primer año:**
- ingreso 4.300 − directos 420 − horas del CEO 640 = **margen de contribución de 3.240 USD**;
- mantenimiento: 190 USD/mes de margen.

**Coste sombra de adquisición:**
| Escenario | Cada cuántos contactos sale un cliente | Coste de adquisición | Margen tras adquisición |
|---|---|---|---|
| Base | 333 | 1.778 USD | 1.462 USD |
| Pesimista | 1.111 | — | −2.686 USD |
| Optimista | — | — | 2.605 USD |

**Con una implantación de 1.500 USD:** margen de contribución de 2.240 USD; en el base, 462 USD tras adquisición.

**A 12 meses:**
| Escenario | Clientes | Cobrado | Neto tras el coste sombra |
|---|---|---|---|
| Base | 3,6 | 15.480 USD | 5.264 USD |
| Pesimista | 1,1 | — | −2.901 USD |
| Optimista | 10,1 | — | 26.259 USD |

`finanzas-control` sustituye los supuestos por costes reales cuando existan.

## 9. Quién vende y cierra
**El equipo:**
- cualifica 30 cuentas por semana;
- redacta los borradores y los deja en Outlook;
- prepara cada llamada y la propuesta de una página;
- registra el embudo.

**El CEO** envía, llama, cierra y cobra.

**Horas del CEO por semana** (máximo 6):
- S48: 4 h de OEF-004.
- Desde S49: hasta 4 h:
  - envíos y seguimientos: unos 20 minutos al día;
  - llamadas: hasta 2 h;
  - bandeja y lote: 30 min.

## 10. Organigrama y subequipos previstos
Sin cambios: los seis líderes y ningún subequipo. Si la cualificación no llega a 30 cuentas por semana, `inteligencia-comercial` puede pedir un subequipo temporal con las reglas de CLAUDE.md §6.

## 11. Presupuesto por tramos
| Tramo | Importe | Condición de liberación | Uso previsto |
|---|---|---|---|
| 1 | Hasta 1.000 USD (`tramo_1_max_comprometido`) | Aprobación de esta Acta | Demo: hasta 100 USD [ESTIMADO]. Revisión profesional del contrato de servicio y de la cláusula de datos: hasta 400 USD [SUPUESTO], solo cuando haya una propuesta aceptada (APR). Buzón postal comercial en EE. UU. para la firma: hasta 60 USD (opcional, si el CEO no usa su dirección de Santo Domingo). |
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
- **Duración:** 14 días desde el primer envío (30 nov – 14 dic).
- **Éxito:** al menos 2 respuestas de interés (sin contar bajas ni respuestas automáticas) o al menos 1 conversación seria.
- **Abandono:** 0 respuestas de interés. El siguiente lote cambia de ángulo, no solo de redacción.

**EXP-US-02 · Texas, mismo mensaje.** 30 cuentas, del 7 al 21 de diciembre, con las mismas métricas. Sirve para comparar los dos estados.

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
Pendientes. El Acta no ha pasado por el Comité. La primera sesión registra aquí el dictamen de `riesgo` y la comprobación de `oferta-entrega`.

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

Riesgos secundarios:
- La demo no funciona: punto de parada en OEF-004.
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
