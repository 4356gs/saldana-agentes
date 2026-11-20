# LOTE 1 · Línea EE. UU. · EXP-US-01 (Florida)

Preparado: 2026-11-20 · desarrollo-negocio · canal `email_eeuu` · vertical `inmobiliaria`. Revisado por `riesgo` el 2026-11-20; sus cambios están aplicados.
**Aprobación: APR-006**, un solo APR para el lote entero: correos 1, 2 y 3 de las 9 cuentas.

## 1. Por qué 9 cuentas y no 30

El Acta (§12) prevé 30 cuentas para EXP-US-01. `inteligencia-comercial` presentó 17 candidatas de Florida. Solo 9 cumplen la definición de cuenta cualificada (CLAUDE.md §8): fricción verificada, decisor identificado por cargo, español verificado y correo profesional publicado por la propia cuenta.

- **Seis no llegaron a cualificar** y quedan como `identificada` (EV-0111 a EV-0116):

  | Cuenta | Por qué no entra |
  |---|---|
  | perez-realty-team | Sin decisor identificado |
  | amg-int-realty | Sin decisor identificado |
  | us-prime-realty-orlando | Corredora multioficina, sin decisor identificado |
  | coastline-realty-lake-worth | Correo Gmail y sin decisor |
  | the-cuervo-team | Bajo LPT Realty: herramientas obligatorias de la red sin verificar |
  | xuma-miami | Licencia y correduría sin verificar; actividad mixta |

- **Dos se cualificaron y `riesgo` las sacó del lote (NO APTO).** Su `cualificada` queda anulada con una fila `correccion` y vuelven a `identificada` (EV-0117 a EV-0120). Sus borradores están en `fuera-de-lote/` y no se cargan.

  | Cuenta | Por qué sale |
  |---|---|
  | orlando-realty-consultants | Decisor o broker no verificado; el correo visible en la web es un Gmail |
  | willard-realty-team | Cargo de decisor de Justin Willard no verificado |

  Las dos se pueden recuperar si se verifican en DBPR y Sunbiz.

El resto de EXP-US-01, hasta 30 cuentas, llegará en un **lote 1b antes del 4 de diciembre**, con su propia revisión de `riesgo` y **su propio APR**. No entra en APR-006. Con 9 cuentas, el criterio de éxito del experimento (2 respuestas de interés o 1 conversación seria) se lee sobre una muestra pequeña, y así se dirá en el veredicto.

## 2. Condiciones previas: sin todas ellas no se carga ningún borrador

1. **OEF-004 hecha** (demo funcionando). El correo 1 dice "Monté un asistente".
   - Si OEF-004 no está hecha el 7 de diciembre, no se envía. `desarrollo-negocio` reescribe esa frase para el plan B sin vídeo y `riesgo` la revisa.
   - Si la demo la terminó un técnico delegado, la frase pasa a "Tengo montado un asistente" / "I have an assistant set up".
2. **OEF-005 hecha**, con la dirección postal física literal (buzón virtual en EE. UU.) devuelta en la bandeja.
3. **Firma completa.** Cada borrador lleva en su propia línea una marca de firma: `FIRMA-ES-TU`, `FIRMA-ES-USTED`, `FIRMA-ES-USTEDES` o `FIRMA-EN`.
   - Al cargar los borradores en Outlook, esa línea se sustituye por la firma correspondiente del §3, ya con el teléfono y la dirección.
   - Para completarla faltan dos datos: la dirección (OEF-005) y el teléfono del CEO (pregunta abierta en la bandeja).
   - **Ningún borrador se carga ni se envía con una marca `FIRMA-…` o `ENLACE-VIDEO` en el cuerpo.**
4. **Pregunta 12 del CEO sobre el dominio, respondida.**
5. **Enlace al vídeo** (OEF-004). Sustituye `ENLACE-VIDEO` en los correos 2: un solo enlace, sin acortador ni seguimiento.
6. **El mismo día del envío**, `python3 herramientas/pipeline.py --puede-contactar <cuenta_id>` para cada cuenta. Si responde NO, ese borrador no se carga.
7. **invierte-en-miami-group.** Opera bajo la correduría Miami New Realty, igual que The Cuervo Team opera bajo LPT Realty, y Cuervo quedó fuera por eso.
   - La Directora acepta el riesgo en esta cuenta porque su web, su equipo y su contacto son propios.
   - El CEO puede excluirla antes del envío.

## 3. Firmas

Aprobadas por `riesgo` con la línea de baja conjugada. Solo faltan el teléfono y la dirección.
- **Teléfono:** si es dominicano, va con el formato "número (WhatsApp · República Dominicana)"; si no se tiene, la línea se omite.
- **Dirección:** la literal de OEF-005. Sin ella no se envía.

**FIRMA-ES-TU** (jmc-real-estate-miami)
```
Gelo Saldaña
Saldaña Digital · Automatización comercial
TELÉFONO-PROFESIONAL
DIRECCIÓN-POSTAL-OEF-005

Este es un correo comercial de Saldaña Digital.
Si prefieres no recibir más correos míos, contéstame "baja" y no vuelvo a escribirte.
```

**FIRMA-ES-USTED** (angelica-baez-brokerage, vs-international-properties, invierte-en-miami-group, the-one-palm-group, irm-fincas-raices-orlando)
```
Gelo Saldaña
Saldaña Digital · Automatización comercial
TELÉFONO-PROFESIONAL
DIRECCIÓN-POSTAL-OEF-005

Este es un correo comercial de Saldaña Digital.
Si prefiere no recibir más correos míos, contésteme "baja" y no vuelvo a escribirle.
```

**FIRMA-ES-USTEDES** (florida-home-group-realty)
```
Gelo Saldaña
Saldaña Digital · Automatización comercial
TELÉFONO-PROFESIONAL
DIRECCIÓN-POSTAL-OEF-005

Este es un correo comercial de Saldaña Digital.
Si prefieren no recibir más correos míos, contéstenme "baja" y no vuelvo a escribirles.
```

**FIRMA-EN** (liv-realty-linda-guzman, leonard-real-estate-group)
```
Gelo Saldaña
Saldaña Digital · Sales automation
TELÉFONO-PROFESIONAL
DIRECCIÓN-POSTAL-OEF-005

This is a commercial message from Saldaña Digital.
If you'd rather not hear from me again, reply "unsubscribe" and I won't write again.
```

`TELÉFONO-PROFESIONAL` y `DIRECCIÓN-POSTAL-OEF-005` son marcas de este archivo, no de los borradores, y se sustituyen al montar la firma.

**Registro de cada borrador.**
- Solo dos registros salen de lo que la ficha recoge de la web: jmc (tú) e irm (usted).
- florida-home-group-realty va en ustedes porque se dirige a los dos fundadores.
- Los demás registros en español son [SUPUESTO], elegidos por el cargo del destinatario y por ser un primer contacto. Si el CEO cambia uno, cambia también su marca de firma.

## 4. Orden de envío (hora del Este, de 9:00 a 11:00)

En diciembre, la hora del Este va una hora por detrás de Santo Domingo: las 9:00 del Este son las 10:00 del CEO. Se envía un correo cada 20 o 30 minutos, nunca todos juntos. El máximo es de 10 primeros contactos al día; aquí son 6 y 3.

**Lunes 7 de diciembre de 2026**

| # | Hora del Este | Cuenta | Idioma | Para |
|---|---|---|---|---|
| 1 | 9:00 | angelica-baez-brokerage | ES (usted) | broker@angelicabaezrealtor.com |
| 2 | 9:20 | vs-international-properties | ES (usted) | RealEstate@vsinternationalproperties.com |
| 3 | 9:40 | invierte-en-miami-group | ES (usted) | admin@invierteenmiami.com |
| 4 | 10:00 | the-one-palm-group | ES (usted) | Eric@Theonepalmgroup.com |
| 5 | 10:20 | jmc-real-estate-miami | ES (tú) | team@jmc.realestate |
| 6 | 10:40 | florida-home-group-realty | ES (ustedes) | contact@floridahomegrouprealty.com |

**Martes 8 de diciembre de 2026**

| # | Hora del Este | Cuenta | Idioma | Para |
|---|---|---|---|---|
| 7 | 9:00 | irm-fincas-raices-orlando | ES (usted) | info@fincaraicesorlando.com |
| 8 | 9:30 | liv-realty-linda-guzman | EN | info@LivRealtyHomes.com |
| 9 | 10:00 | leonard-real-estate-group | EN | charlie@LeonardRealEstateGroup.com |

**Direcciones que el CEO confirma en pantalla antes de enviar.** La herramienta las descodificó de un enlace protegido:
- the-one-palm-group: Eric@Theonepalmgroup.com, en la página de equipo.
- florida-home-group-realty: contact@floridahomegrouprealty.com, en el pie o en la página de contacto.

Si una dirección no aparece en la web, ese borrador no se envía y se avisa en la bandeja.

## 5. Seguimientos (en el mismo hilo, solo a quien no respondió)

- **Correo 2 (+5, con el vídeo), por decisión de la Directora:**
  - lunes 14 de diciembre para las cuentas 1 a 6;
  - martes 15 de diciembre para las cuentas 7 a 9;
  - a las mismas horas que el correo 1.
- **Correo 3 (cierre):** el lunes 4 de enero de 2027 para todas las cuentas, espaciado de 9:00 a 11:00 del Este, por las fiestas (Acta §5).
  - Propone dos franjas: miércoles 6 de enero a las 10:00 y jueves 7 de enero a las 15:00, hora del Este (11:00 y 16:00 en Santo Domingo).
  - El CEO las confirma con su agenda antes de cargarlos. Si cambian, se cambian en todos.
- Una cuenta que respondió, aunque sea con una pregunta, no recibe el seguimiento. Se le contesta según el §6.

## 6. Qué hacer según la respuesta

| Respuesta | Siguiente paso |
|---|---|
| Sí, manda el vídeo | Contestar con el enlace y dos franjas para una llamada de 15 minutos. No se envía el correo 2. `ejecucion-fisica` prepara la OEF de la llamada con el guion de la plantilla. |
| ¿Cuánto cuesta? | El precio no se da por correo: "Depende del volumen de consultas. En una llamada de 15 minutos le doy una cifra cerrada", más dos franjas. |
| Ya tengo una herramienta | Preguntar cuál y si responde en español por WhatsApp y agenda sola. Si es que sí a todo, cerrar con cortesía. |
| Baja / unsubscribe | `no_contactar` el mismo día. No se contesta. |
| Fuera de la oficina | Reintentar tras la fecha de vuelta, con al menos 5 días desde el último toque. |
| Rebote | `no_contactar`. No se prueba otra dirección. |

Cada envío, respuesta o baja se registra en `estado/pipeline.csv` solo cuando el CEO lo confirma en la bandeja, con el formato `cuenta_id | correo N | enviado AAAA-MM-DD` o `cuenta_id | respuesta | resumen`. Sin esa confirmación, nada cuenta como contacto.

## 7. Minutos estimados del CEO

Calculados con Python sobre estos supuestos [SUPUESTO]:
- 3 min por cada correo 1: confirmar la dirección, leer, poner la firma y enviar;
- 10 min, una sola vez, para preparar las firmas;
- 1 min extra por cada una de las 2 direcciones que hay que confirmar en pantalla;
- 1,5 min por seguimiento.

| Bloque | Minutos |
|---|---|
| 7 dic (6 correos 1, con la preparación de las firmas) | 30 |
| 8 dic (3 correos 1) | 9 |
| Correos 2 (14 y 15 dic, hasta 9) | 13,5 |
| Correos 3 (4 ene, hasta 9) | 13,5 |
| **Total del lote** | **66 (1,1 h)** |

Si los borradores se cargan en Outlook con el conector de Microsoft 365, la firma la pone el equipo y el tiempo baja. No incluye las llamadas.

## 8. Reglas que cumple este lote

- Cada correo 1 parte de una observación verificada en la ficha de esa cuenta. Ninguna frase habla de zonas ni de quién vive en ellas.
- Ningún correo da precio. El correo 1 no lleva enlace; el correo 2 lleva uno solo (el vídeo).
- Texto plano, sin adjuntos ni imágenes, con asunto veraz. La firma identifica el correo como comercial y lleva la dirección postal y la línea de baja.
- Un solo mensaje por cuenta y día. Ninguna cuenta del lote tiene historial de contacto previo.
- Ningún nombre inventado: los saludos usan nombres publicados por la propia cuenta.
- Los cuerpos no llevan "[Nombre]", "XXX" ni corchetes. Las únicas marcas son las de firma y `ENLACE-VIDEO`, y se sustituyen antes de cargar.
- Ningún correo menciona la ACD, "PYME", "SME" ni el empleador del CEO.
