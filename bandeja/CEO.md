# Bandeja del CEO

Este es tu único canal hacia el equipo. Escribe debajo de cada sección; la siguiente sesión lo procesa todo, lo archiva en `bandeja/archivo/` y deja este archivo limpio. Lo que no esté aquí no existe para el equipo.

## Preguntas del equipo
Responde debajo de cada una. Con las cuatro primeras basta para arrancar la Fase 1.

1. **Fecha límite.** ¿En qué fecha tienen que estar firmadas las LOIs para presentar el expediente? (`fecha_limite_lois`, AAAA-MM-DD)
   > 1 de diciembre de 2026 (2026-12-01). Ya está en parametros.json.

2. **Formato de LOI.** ¿Qué debe contener una LOI según quien lleva el expediente? ¿Sirve tal cual la C06 del Kit DFO?
   > Supongo que sí, la C06 del Kit DFO. Sin validar todavía con quien lleva el expediente.

3. **Activos.** El equipo necesita el Kit DFO, el pipeline ACD, el diagnóstico de Contagal y la base de 165 bodegas. ¿Los subes a `activos/` o incluyes el conector de Google Drive en la tarea programada?
   > Están en Google Drive, carpeta SALDAÑA DIGITAL. La tarea programada tiene el conector de Drive.

4. **Cuentas cálidas.** ¿Qué pasó después de lo último registrado?
   - Albamar: al 9 de octubre la llamada no se había celebrado.
   - Pulsa Asesores: se ofreció a ayudar con la carta de intención y le respondiste el 25 de septiembre.
   - Terra Brava: ¿es un contacto cálido o está quemada?
   - Contagal: ¿sigue cerrada?
   > De estas, solo sigue abierta Albamar. Pulsa Asesores, Terra Brava y Contagal quedan fuera.

5. **Canales en marcha.**
   - ¿Contactaste a Valora, DPI Estrategia o EOSA para Re-acciona?
   - ¿Están activos los visitantes de El Escorial?
   - ¿Salió algo con el ángulo de control de peso a clínicas?
   > 

6. **Precios.** Conviven varias versiones (ver `contexto/oferta-y-activos.md`, sección 2). ¿Fijas tú la arquitectura o quieres que `oferta-entrega` te proponga una para aprobar?
   > 

7. **Facturación.** ¿Cómo se cobraría hoy una ACD pagada por un cliente español, antes de la resolución? Confírmalo con quien lleva el expediente. (`jurisdiccion`)
   > 

8. **Horas y capital.** Del diseño del 28 de octubre se trasladan 6 h/semana, 40 USD/hora de coste sombra y un capital de 3.000 USD con 600 de reserva. ¿Siguen valiendo para Saldaña Digital?
   > 

## Aprobaciones
Una línea por decisión:
- `APROBADO APR-###`
- `RECHAZADO APR-### — motivo`
- `CAMBIOS APR-### — qué cambiar`

## OEF ejecutadas
`OEF-### | hecha / fallida / delegada a <quién> | horas | coste | evidencia (enlace o descripción)`

## Eventos comerciales
Todo lo que pasó con una cuenta y el equipo no puede ver: envíos hechos, respuestas, llamadas, reuniones, LOIs y pagos.
`AAAA-MM-DD | cuenta | contacto / seguimiento / respuesta / conversacion / loi_firmada / pago / descartada | detalle`

## Dinero movido
`AAAA-MM-DD | concepto | importe | ingreso cobrado / gasto ejecutado | OEF o APR relacionado | comprobante`

## Instrucciones del CEO
Texto libre.

2026-11-01: la fecha límite está a 30 días. En la primera sesión, procesa estas respuestas, pasa directamente a la Fase 1 y entrégame el Acta de Activación con su APR en esa misma sesión. La validación del formato de LOI con quien lleva el expediente es una OEF de esta semana.

2026-11-01: el expediente no exige un número fijo de LOIs; lo ideal son 3 a 5. Planifica para 3 LOIs sólidas antes del 1 de diciembre y trata la 4.ª y la 5.ª como mejora, no como condición. Prefiero 3 LOIs con intención real a 5 débiles.
