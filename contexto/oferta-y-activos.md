# Oferta y activos

Lo mantiene `oferta-entrega`. Los cambios de precio u oferta publicada requieren un APR del CEO. Carga inicial: 1 de noviembre de 2026.

## 1. Oferta publicada (saldanadigital.com)

1. **Diagnóstico gratuito.** Una página con datos públicos:
   - ficha de Google y reseñas frente a la media del sector;
   - web en móvil (velocidad, reservas, tienda);
   - coherencia de los datos en directorios;
   - tres competidores cercanos, anonimizados;
   - las tres fugas más visibles, por orden de impacto.

   No requiere llamada ni acceso a sistemas.
2. **Auditoría Comercial Digital (ACD), desde 900 €.** Nueve indicadores, fugas cuantificadas con supuestos declarados, hoja de ruta ordenada por retorno y una sesión de 60 minutos.
3. **Implantación.** Presupuesto cerrado tras la auditoría y solo de lo que esta justifica: reservas, WhatsApp, CRM, Odoo o cuadros de mando.
4. **Acompañamiento.** Medición mensual y ajustes. Se presupuesta tras la auditoría.

## 2. Precios de referencia (sin arquitectura única todavía)

| Pieza | Precio | Origen |
|---|---|---|
| ACD | 900–1.490 € | Referencia del CEO |
| ACD bodegas, con benchmark de zona | 1.290 € fijo | Decisión previa del CEO |
| Proyecto de implantación | desde 4.500 € | Referencia del CEO |
| Acompañamiento | 1.800 €/mes | Referencia del CEO |
| Hipótesis del 6 oct | ACD 750–1.100 €; proyecto ancla 3.500–5.500 €; acompañamiento 600–900 €/mes (1.500–2.500 € como destino) | Decisión de activación del 6 oct |
| Clínicas, ángulo de control de peso | 1.500 € de implantación + 290 €/mes | Decisión del 30 oct |
| Canal gestorías | reparto del 40% | Dossier de gestorías |

Hasta que el CEO fije una arquitectura única, ningún borrador menciona un precio que no esté en la web ("desde 900 €" para la ACD).

## 3. Reglas de oferta vigentes

- El primer contacto ofrece el diagnóstico gratuito. La ACD es el segundo paso y no se menciona en el primer toque.
- A las gestorías no se les habla de precio ni de comisión en el primer correo.
- Los competidores del diagnóstico siempre van anonimizados.
- Odoo es arquitectura de entrega, no producto. Se vende la corrección estructural que revele el diagnóstico.
- Clínicas: solo Google Calendar, para mantener la replicabilidad 80/20. Si la agenda vive en otro sistema, el diagnóstico dice si compensa cambiarla.
- El asistente de clínicas no diagnostica ni da consejo médico, y opera con un encargo de tratamiento firmado.

## 4. Inventario de activos

Las ubicaciones marcadas como PENDIENTE se preguntan en la Fase 0. La carpeta raíz del archivo documental en Google Drive es "SALDAÑA DIGITAL", con ID `1h8L0cIS1XkJRCsN0DOuw1gqebRSvtAh1`.

| Activo | Estado | Ubicación | Notas |
|---|---|---|---|
| Kit DFO (C02 → C04 → C05 → C06) | Listo, sin desplegar | PENDIENTE | La C06 genera las LOIs. Es el punto de partida obligado para cualquier LOI. |
| Expediente Cero | Listo, sin desplegar | Repo `4356gs/expediente-cero` (público) | Contenido y uso a confirmar con el CEO. |
| Pipeline ACD | Completo, sin activación sistemática | PENDIENTE | Nueve indicadores, análisis con Claude e informe en Word. |
| Diagnóstico externo con datos públicos | En uso | PENDIENTE | Google Places, web y PageSpeed, con cohorte sectorial y competidores anonimizados. Ejemplos: el diagnóstico de Contagal (PDF "Diagnostico_Presencia_Comercial_Vigo_Contagal") y Más Humanos ETT. |
| Marco de detección de fricciones en bodegas | Listo | PENDIENTE | Jerarquía determinista y Excel de validación manual. |
| Base de 165 bodegas de Rías Baixas | En uso | PENDIENTE | Puntuada y enriquecida. |
| Informe ARDÁN Galicia 2026 (Igape) | En uso | PENDIENTE | Indicadores Gacela y de alto potencial. Se usó para segmentar O Salnés. |
| Dossier de gestorías | Desplegado desde el 31 ago | Outlook y Drive | Tres variantes de correo. |
| One-pager y Kit_Outreach_Gestorias_v3 | Desalineados | Drive | Llevan 590 € y 236 € de comisión, la palabra "PYME" y la paleta antigua. No se adjuntan sin reescribir. |
| Seguimiento reforzado de gestorías (caso Sofigal + Verifactu) | Listo, sin enviar | Outlook | El argumento de Verifactu quedó desfasado con el aplazamiento a 2028. |
| Demo Pazo do Val | Primera implementación desde oct 2026 | VPS Hostinger | Odoo, PostgreSQL, n8n, Power BI y Nginx con Docker Compose. Se enseña en 20 minutos. |
| Producto de clínicas ("Primera Respuesta") | Definido | PENDIENTE | WhatsApp Business API → n8n → Claude → Google Calendar. |
| saldanadigital.com | En producción | Hostinger | Ver la deuda en `contexto/saldana-digital.md`, sección 8. |
| Calendario corregido de outreach a bodegas | Documento | Drive, carpeta inv_bodegas | Su supuesto de visita presencial en octubre no se pudo cumplir. |
| Landing de Diagnóstico Express | Falta conectar el webhook de n8n | PENDIENTE | Pertenece al track de República Dominicana: fuera de alcance. |
| AdegaFlow AI | Congelado | Repos `adegaflow-ai` y `AdegaFlow` | Fuera de alcance. |
