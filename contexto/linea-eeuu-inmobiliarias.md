# Línea EE. UU. · Primera Respuesta para inmobiliarias

Decisión del CEO del 2026-11-19 (APR-004 y APR-005, en `bandeja/CEO.md`). Plan aprobado: `actas/acta-activacion-eeuu.md`.

La Directora mantiene este archivo. `oferta-entrega` mantiene la oferta y los precios. Si algo de aquí choca con la bandeja, gana la bandeja y se actualiza este archivo.

## 1. Por qué esta línea

- **Tesis del CEO.** Con 3.000 USD, el capital no es lo escaso. Lo escaso son sus horas y su capacidad de vender. El dinero se usa para vender en dólares algo que ya sabe hacer, no para construir.
- **Lo que no funcionó en España.**
  - Unas 108 cuentas en frío dieron 0 conversaciones serias [ESTIMADO: `actas/propuesta-disolucion.md` §4].
  - El canal `email_frio` alcanzó el criterio de corte [VERIFICADO: `pipeline.py`, 2026-11-19].
- **Lo que cambia.**
  - **Mercado:** se cobra en USD [SUPUESTO: los precios aceptables son más altos que en Galicia; se valida con las primeras propuestas].
  - **Oferta:** un producto concreto ya definido, Primera Respuesta, en vez de una auditoría.
  - **Clientela:**
    - Los adultos hispanos son el grupo que más usa WhatsApp en EE. UU.: un 56 %, frente al 22 % de los adultos blancos y al 32 % del total [VERIFICADO: Pew Research Center 2025, citado por Sinch; confirmar en pewresearch.org].
    - En 2024 la cifra era del 54 % [VERIFICADO: Pew, citado por Latin Times].
  - **Horario:**
    - Santo Domingo está en UTC−4 todo el año.
    - Florida (hora del Este) está en UTC−5 en invierno y UTC−4 en verano. Texas (hora del Centro) está una hora por detrás de Florida.
    - En la práctica, el horario laboral coincide o difiere en una o dos horas [VERIFICADO: zonas horarias IANA].

## 2. Oferta

**Qué hace el asistente.**
- Contesta en segundos cada consulta que llega por WhatsApp o por la web, en el idioma del cliente (español o inglés).
- Hace las preguntas que haría el equipo:
  - compra o alquiler;
  - zona que busca el propio cliente;
  - presupuesto;
  - plazo;
  - financiación: preaprobado, al contado o todavía no.
- Agenda la llamada o la visita en el Google Calendar del agente.
- Avisa al agente con un resumen.
- Pasa a una persona cuando el cliente lo pide o cuando la pregunta no está en su base.
- Se presenta como asistente virtual del equipo.

**Qué no hace.**
- No da consejo legal, fiscal, migratorio ni financiero.
- No negocia ni promete disponibilidad o precios que no estén en su base.
- No inicia conversaciones sin consentimiento.
- No usa SMS en la versión inicial (ver §5).
- No pregunta, filtra, recomienda ni describe zonas por clases protegidas (ver §5).

**Arquitectura.** La del producto de clínicas: WhatsApp Business API → n8n → Claude → Google Calendar. Solo Google Calendar, por la regla 80/20 del CEO.

**Precio de lista:** 2.500 USD de implantación + 300 USD/mes [SUPUESTO; aprobado como hipótesis en APR-005].

Referentes:
- **Structurely** (asistente de IA para leads inmobiliarios): desde 499 USD/mes por 250 leads, con 1.500 USD de alta y un mínimo de 3 meses [VERIFICADO: us.fitgap.com]. Otra fuente da 499 USD/mes con 2.000 USD de alta [VERIFICADO: aiproductivity.ai, junio de 2026]. Hay que confirmarlo en structurely.com antes de usarlo en una propuesta.
- **Un ISA humano** (la persona que atiende y cualifica los leads de un equipo): entre 3.000 y 5.000 USD/mes [ESTIMADO: un blog que cita a Real Trends 2025; no es fuente primaria].

**Reglas de precio.**
- El primer correo no menciona precio. El precio se da en la llamada.
- Si las tres primeras propuestas se rechazan por precio, `oferta-entrega` propone bajar la implantación a 1.500 USD (requiere APR).
- Garantía propuesta: si en los primeros 30 días el asistente no responde y agenda como se acordó, se devuelve la implantación. No se ofrece hasta validar el contrato (§5).

## 3. Cliente ideal

- **Quién:**
  - equipos de 3 a 15 agentes;
  - agentes individuales con volumen;
  - broker-propietarios.
- **Dónde:** Florida (Miami-Dade, Broward, Palm Beach, Orange) y Texas (Harris, Dallas, Tarrant, Bexar) [SUPUESTO: concentración de clientela hispanohablante; EXP-US-01 y EXP-US-02 comparan los dos estados].
- **Señal obligatoria:** la cuenta ya atiende en español, sea en su web, sus anuncios, sus redes o su perfil profesional [VERIFICADO + fuente, en cada ficha].
- **Fricción observada:** al menos una, verificada en datos públicos:
  - el único contacto es un formulario sin respuesta inmediata;
  - publica un WhatsApp sin indicar respuesta fuera de horario (solo lo visible públicamente: nunca se escribe a la cuenta para probarlo);
  - anuncios en español que llevan a una web solo en inglés;
  - reseñas que mencionan lentitud o falta de respuesta (análisis agregado, sin identificar a quien las escribe).
- **Decisor:** team lead, broker-propietario o el propio agente.
- **Exclusiones:**
  - redes con herramientas corporativas obligatorias;
  - cuentas sin un correo profesional publicado por ellas mismas;
  - gestoras de alquiler, que necesitan otro producto.
- **Fuentes permitidas:** la web de la cuenta, sus perfiles profesionales públicos y los directorios públicos. Prohibido comprar bases de datos o adivinar direcciones (CLAUDE.md §4).

## 4. Canal y mensaje

- **Canal:** correo individual desde `cuenta_envio`. Queda en borrador y lo envía el CEO. En el pipeline se registra con el canal `email_eeuu`.
- **Volumen:**
  - hasta 30 primeros contactos por semana, con un máximo de 10 al día;
  - dos seguimientos por cuenta, a los 5 y a los 12 días;
  - la cuenta de envío es el dominio de la marca: más volumen arriesga su reputación.
- **Idioma:** el de la web de la cuenta; español por defecto.
- **Estructura:**
  - el primer correo no lleva enlace y ofrece un vídeo de 60 segundos;
  - el vídeo va en el segundo correo.
- **Plantillas base:** `salidas/material/eeuu-inmobiliarias-plantillas.md`.
- **Nunca:** SMS, WhatsApp ni llamadas en frío a prospectos.

## 5. Cumplimiento

**Correo comercial: ley CAN-SPAM** [VERIFICADO: FTC, "CAN-SPAM Act: A Compliance Guide for Business"].
- La ley no exime el correo entre empresas.
- El remitente y el asunto deben ser veraces.
- Debe quedar claro que es una comunicación comercial.
- Cada correo lleva una dirección postal física válida del remitente. Vale una dirección, un apartado de USPS o un buzón comercial registrado.
- Cada correo explica cómo darse de baja, y la baja se respeta. La ley da 10 días hábiles; el equipo la aplica el mismo día.
- La multa llega a 53.088 USD por correo infractor.

**Vivienda justa: Fair Housing Act** [VERIFICADO: NAR, "Fair Housing", cap. 6; guías de examen inmobiliario de 2026].
- Protege 7 clases: raza, color, religión, origen nacional, sexo, situación familiar y discapacidad. Algunos estados y ciudades añaden otras.
- Prohíbe el "steering": orientar a alguien hacia unas zonas o apartarlo de otras por una clase protegida.

Reglas del asistente:
- Nunca pregunta por esas clases ni por el estatus migratorio.
- Nunca describe una zona por quién vive en ella.
- Ante preguntas como "¿es buena zona para familias?" o "¿es zona de latinos?", responde de forma neutral, remite a fuentes públicas objetivas y ofrece hablar con el agente.
- `riesgo` revisa cada guion del asistente con estas reglas.

**SMS.** En EE. UU., cualquier SMS enviado desde una aplicación por un número de 10 dígitos exige registro A2P 10DLC [VERIFICADO: documentación de Twilio]. El registro pide identificador fiscal y lleva tiempo, así que el SMS queda fuera de la versión inicial.

**WhatsApp.** El asistente responde a quien escribe. Los mensajes que inicia el negocio usan plantillas aprobadas y consentimiento [SUPUESTO: verificar en la política de WhatsApp Business antes de la primera implantación].

**Datos de los clientes de cada agencia.** El contrato de servicio incluye una cláusula de tratamiento de datos, y los datos no se usan para nada más [SUPUESTO: lo valida el profesional que revise el contrato].

**Datos de prospectos.** Solo datos profesionales publicados por la propia cuenta.

**Cobro y facturación.** PENDIENTE (`jurisdiccion`). Bloquea la primera propuesta con precio, no la prospección.

## 6. Demo

- **Activo:** el producto de clínicas, Primera Respuesta / Atlas (360dialog + n8n + Claude + Google Calendar). En `contexto/oferta-y-activos.md` §4 consta como "Definido" [VERIFICADO], pero su estado real es PENDIENTE (pregunta 9 de la bandeja).
- **Qué cambia:**
  - la base de conocimiento, que es de un equipo ficticio rotulado como demostración (`salidas/material/eeuu-demo-base-conocimiento.md`);
  - el guion bilingüe;
  - las reglas de vivienda justa.
- **Entregable:** un vídeo de 60 a 90 segundos (OEF-004). Escena: llega una consulta en español a las 22:40, el asistente responde en segundos, hace cuatro preguntas, deja la cita en el calendario y avisa al agente.
- **Regla:**
  - como máximo una semana de trabajo;
  - después no se toca hasta tener 10 conversaciones serias;
  - nunca se usa una marca o un agente reales.

## 7. Calendario y controles

- **Fechas** (calendario y zonas horarias en `actas/acta-activacion-eeuu.md` §5):
  - Thanksgiving es el 26 de noviembre de 2026 [VERIFICADO: calendario], así que esa semana no se envía.
  - La segunda quincena de diciembre tiene baja respuesta [SUPUESTO].
- **Control del día 90 (2027-02-18):**
  - si hay al menos 3 conversaciones serias o un cliente pagando, se sigue;
  - si no, propuesta de cierre de la línea.
- **Límite del día 150 (2027-04-19):** al menos un cliente pagando, o propuesta de cierre.
- **Por qué 150 días y no 90:** el volumen está limitado por las reglas del equipo (10 primeros contactos al día y una sola cuenta de envío). Con ese volumen, el escenario base da [ESTIMADO: `herramientas/embudo_eeuu.py`, con Poisson sobre el valor esperado]:
  - **al día 90:** 0,54 clientes esperados, un 42 % de probabilidad de tener al menos uno;
  - **al día 150:** 1,26 clientes esperados, un 72 %.

  Cortar a los 90 días mataría la línea en más de la mitad de los escenarios base.

## 8. Supuestos críticos y cómo se validan

| Supuesto | Validación | Cuándo |
|---|---|---|
| Un correo en español con una observación concreta obtiene al menos un 5 % de respuestas | EXP-US-01 y EXP-US-02; corte de la línea con 60 cuentas maduras | Diciembre de 2026 |
| Se paga 2.500 USD de implantación + 300 USD/mes | Las tres primeras propuestas | Enero de 2027 |
| El flujo de clínicas sirve con otra base de conocimiento en una semana o menos | OEF-004 | S48 |
| El coste directo es de 70 USD/mes por cliente o menos | `finanzas-control`, con las facturas reales de la demo | Diciembre de 2026 |
| Florida responde distinto que Texas | EXP-US-01 frente a EXP-US-02 | Diciembre de 2026 |
| El CEO puede cobrar en USD desde República Dominicana sin fricción | `jurisdiccion`, con su contador | Antes de la primera propuesta con precio |

## 9. Fuentes

- FTC, CAN-SPAM Act: A Compliance Guide for Business: https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business
- NAR, Fair Housing (capítulo 6): https://www.nar.realtor/sites/default/files/documents/Fair-Housing-RE-Brokerage-Essentials-Chapter-06-2016.pdf
- Clases protegidas y "steering" (guía de examen, 2026): https://open-exam-prep.com/study-guides/ne-real-estate/national-practice/nat-5-federal-fair-housing-protected-classes
- Twilio, A2P 10DLC: https://www.twilio.com/docs/messaging/compliance/a2p-10dlc
- Pew Research Center, Americans' Social Media Use 2025: https://www.pewresearch.org/internet/2025/11/20/americans-social-media-use-2025/
- Sinch, uso de WhatsApp en EE. UU. con datos de Pew: https://sinch.com/es/blog/whatsapp-en-ee-uu-potencial/
- Latin Times, uso de WhatsApp entre adultos hispanos (Pew, 2024): https://www.latintimes.com/latinos-dominate-social-media-leading-usage-tiktok-instagram-whatsapp-across-us-551034
- Structurely, precios: https://us.fitgap.com/products/structurely y https://aiproductivity.ai/tools/structurely/
- Coste de un ISA humano (fuente secundaria): https://realty-copilot.pages.dev/blog/real-estate-chatbot-for-agents/
