# Saldaña Digital: contexto del negocio

Carga inicial: 1 de noviembre de 2026, a partir del historial de trabajo del CEO hasta esa fecha. Todo lo que aquí figura como estado de una cuenta debe darse por [SUPUESTO] hasta que el CEO lo confirme o se verifique contra su correo. La Directora mantiene este archivo; `oferta-entrega` mantiene `contexto/oferta-y-activos.md`.

## 1. Qué es

Consultoría de auditoría y automatización comercial. El CEO opera como persona física con el nombre comercial Saldaña Digital. Nació en República Dominicana; el foco actual es Galicia, donde Saldaña Digital es además la base del expediente de residencia por cuenta propia del CEO (RD 1155/2024). El plan de viabilidad está aprobado por UPTA.

Tesis comercial: los negocios consolidados no pierden ventas por falta de demanda, sino entre el primer contacto y el cobro. Saldaña Digital mide esa fuga con datos públicos y solo implanta lo que tiene retorno calculable.

Diferencial declarado: método de multinacional aplicado a negocios sin departamento de datos. El CEO tiene más de 20 años en operaciones y tecnología en multinacionales de logística y telecomunicaciones, un MBA y un máster en Data Science en curso.

Restricciones personales del CEO que condicionan el plan:
- Reside en República Dominicana y trabaja en remoto. No hay presencia en Galicia salvo viaje planificado; toda presencia física se planifica como OEF o con visitantes delegados.
- Mantiene un empleo senior en una multinacional de logística. Sus horas son limitadas y no ofrece nada que pueda parecer competencia con su empleador.

## 2. Verticales

- **Gestorías y despachos:** canal caliente. Funcionan mejor como canal de derivación hacia su cartera que como cliente final. El CEO no compite con ellos: no hace contabilidad, fiscalidad ni laboral.
- **Clínicas estéticas y dentales:** la estética es la entrada más rápida. Producto: respuesta por WhatsApp Business API → n8n → Claude → cita en Google Calendar, con recordatorio. Solo Google Calendar, para mantener la replicabilidad 80/20. Ángulo nuevo decidido el 30 de oct: programas médicos de control de peso.
- **Bodegas, agroalimentario y turismo rural en Galicia:** universo de 165 bodegas de la DO Rías Baixas mapeadas. Fricciones típicas: visitas sin reserva online, venta directa sin carrito, datos dispersos, señales públicas descuidadas. Demo: Pazo do Val.

Los clientes se describen por vertical o perfil de valor, nunca como "PYME".

## 3. Calendario de cada vertical

- **Bodegas:** vendimia de agosto a septiembre, a veces hasta octubre (en 2026 empezó unas tres semanas antes). Durante la vendimia no atienden propuestas. Octubre y noviembre son la ventana receptiva.
- **Gestorías:** se cierran del 1 al 20 de los meses de vencimiento trimestral. Observado en octubre de 2026; se supone igual en enero, abril y julio [SUPUESTO]. Enero suma los resúmenes anuales [ESTIMADO].
- **Clínicas:** el cuarto trimestre está cargado antes de Navidad (criterio del CEO).

## 4. Historial comercial hasta octubre de 2026

Volumen: más de 100 envíos en frío desde `direccion@saldanadigital.com` (Outlook) entre agosto y septiembre. El tope inicial de 20 contactos por semana se superó; el cuello de botella de volumen se considera resuelto. Las respuestas no se han convertido en LOIs.

Qué se ha probado:
- **Bodegas, tanda 1** (22–24 ago): unos 12 correos con dos plantillas ("reserva de visitas" y "venta directa de botellas"). Cero respuestas, atribuidas a la vendimia.
- **Bodegas, correo individual a Albamar** (23 ago) sobre su dominio caído. Respuesta positiva.
- **Gestorías, tandas 1 a 3** (31 ago – 3 sep): presentación (traslado a Galicia), hipótesis de fricción del vertical, cifra con supuesto declarado, diagnóstico gratuito con datos públicos sobre tres negocios de su ciudad y llamada de 20 minutos. Sin precio ni comisión. Un seguimiento el 8 sep (versión sin Verifactu ni caso Sofigal).
- **Clínicas** (31 ago y 13 sep): ángulo de fricción entre la solicitud web y la cita confirmada.
- **Campaña de "carta de intención" a bodegas de O Salnés** (19–21 sep): unas 30 cuentas, con el asunto "Carta de intención – digitalización operativa en [empresa]", segmentadas con el Informe ARDÁN Galicia 2026 del Igape. No consta ninguna respuesta.
- **Aperturas fuera de vertical:** instaladoras, solar e industrial (7–23 sep), conserveras (4 sep) y una ETT de Zaragoza (diagnóstico externo preparado).

Lo que sí ha funcionado:
- Un diagnóstico externo real entregado: a Contagal, sobre tres instaladoras de Vigo (Plus Control, Instalaciones Clima y Sofigal). Mostró fugas concretas: identidad fragmentada, reseñas que no llegan a los directorios y subvenciones que no se comunican. Es la mejor prueba de ejecución disponible, con los nombres anonimizados.
- Las respuestas positivas vinieron de tres sitios: un correo individual con una observación concreta de esa cuenta (el dominio caído de Albamar), el canal de gestorías con oferta de diagnóstico gratuito (Contagal) y la red del CEO (Pulsa Asesores). Las plantillas de bodegas por vertical no obtuvieron ninguna.

## 5. Lecciones

1. En bodegas, una observación verificada y específica de la cuenta generó respuesta; la plantilla del vertical no [ESTIMADO sobre una sola respuesta].
2. Pedir una carta de intención en frío, sin relación previa, no ha producido respuestas registradas.
3. Objeción de canal (Contagal): "lo competitivo en España es el remoto; trasladarse encarece el servicio". Además ya trabajaban con un proveedor remoto.
4. Objeción de cliente (Gallud, vía Pulsa Asesores): "ya estamos automatizando por nuestra cuenta". Un diagnóstico no encaja ahí, pero el contacto se ofreció a ayudar con la carta de intención.
5. Bodegas pequeñas: el propietario tiene poco tiempo y no recibe visitas (Castro Brey).
6. Calendario: el bajo volumen de respuestas de agosto y septiembre en bodegas se atribuye a la vendimia, no al mensaje [SUPUESTO].
7. Errores operativos reales, que originan las reglas de higiene:
   - Envíos duplicados (Maspymes, Cuidadent, IDEOdental).
   - Un correo con "[Nombre]" sin rellenar (Maspymes).
   - Dos mensajes distintos a la misma cuenta en 24 horas (Tomada de Castro).
   - Un contacto de la lista de quemados incluido en una tanda (Santiago Roma).
   - Un correo enviado a un buzón de pruebas en vez de a la bodega (Vía Romana, que nunca fue contactada).
   - Un seguimiento enviado a una cuenta ya cerrada (Contagal).

## 6. Red, canales e instituciones

- **Oficina Económica de Galicia / Igape:** relación activa. El Igape facilitó la base ARDÁN. El CEO envió el formulario de expertos colaboradores Igape-OEG el 22 sep.
- **Igape Re-acciona:** decisión de octubre: entrar como subcontratista a través de colaboradores acreditados (Valora, DPI Estrategia, EOSA) en lugar de acreditarse directamente. Objetivo original: piloto entre octubre y noviembre y LOI antes de diciembre.
- **Polo de Emprendimiento (O Porriño):** reunión con Susana en octubre de 2026.
- **Pulsa Asesores (Juan Andrés, vinculado a Gallud):** se ofreció a ayudar con la carta de intención. El CEO le respondió el 25 sep. Es el contacto más cercano a una LOI.
- **Compañera del máster que trabaja en una gestoría:** posible puente cálido al canal gestorías.
- **Gestora colegiada en Valencia:** validadora del enfoque de la ACD. No es cliente ni fuente de LOI, porque está fuera de Galicia.
- **Visitantes en El Escorial:** una o dos personas españolas disponibles para visitar clínicas en El Escorial y San Lorenzo de El Escorial, presentar el proyecto y pasar el contacto al CEO.

## 7. Clientes previos

Barrancolí Consulting, Speedster (República Dominicana), Llamoto (rediseño web; parece haber cerrado) y France Energie. No consta permiso para citarlos como referencia.

## 8. Web: saldanadigital.com

WordPress con Elementor en Hostinger, publicada en octubre de 2026. Embudo: diagnóstico gratuito → ACD desde 900 € → implantación → acompañamiento. Tiene páginas por vertical, una demo de Pazo do Val bajo petición, un blog de 2 artículos (3 de octubre) y una página aparte para República Dominicana.

Deuda revisada el 1 de noviembre de 2026, por orden de gravedad:
1. El aviso legal y la política de privacidad publican textos de relleno: "[pendiente: NIF/NIE]", "[confirmar: nombre y apellidos legales]" y "[pendiente: domicilio que figura en el expediente]". Incumple la LSSI y el RGPD y deja ver el expediente a cualquiera.
2. La página `/despachos` usa como gancho los plazos de Verifactu de 2027. Hacienda anunció el 5 de octubre de 2026 un aplazamiento a octubre de 2028, pendiente de publicarse en el BOE.
3. El enlace de WhatsApp del pie apunta a `wa.me/@saldanadigital`. El número para páginas de cliente es el 18496539171.
4. Hay llamadas a la acción que no llevan a lo que prometen ("ver la demo" y "hablemos 20 minutos" acaban en el formulario de diagnóstico; el Calendly anuncia 20 minutos y su URL es `/30min`).

## 9. Contradicciones abiertas (para la Fase 0)

1. **Precios.** Conviven varias versiones: ACD de 900 a 1.490 €, acompañamiento de 1.800 €/mes y proyectos desde 4.500 €; las hipótesis del 6 oct (ACD de 750 a 1.100 €, proyecto ancla de 3.500 a 5.500 €, acompañamiento de 600 a 900 €/mes); la oferta de clínicas del 30 oct (1.500 € más 290 €/mes); y el material antiguo de gestorías (590 € con comisión de 236 €). El dossier de gestorías habla de un reparto del 40%. Hay que fijar una arquitectura única.
2. **Terra Brava:** figura como contacto cálido con invitación a visita y, a la vez, en la lista de quemados.
3. **Contagal:** cerrada por decisión del CEO el 21 sep, pero el 23 sep recibió un seguimiento.
4. **Albamar:** al 9 de octubre la llamada no se había celebrado. Se desconoce el estado posterior.
5. **Pulsa Asesores:** se desconoce qué pasó tras la respuesta del 25 sep.
6. **Re-acciona y visitantes de El Escorial:** no consta si se activaron.
7. **Facturación antes de la resolución:** cómo se cobraría hoy una ACD pagada en España (parámetro `jurisdiccion`).
8. **Formato de LOI:** qué contenido exige quien lleva el expediente (el Kit DFO incluye una plantilla, la C06).
