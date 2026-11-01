# Equipo de agentes de Saldaña Digital

Este repositorio es un equipo de agentes de IA dedicado a desarrollar Saldaña Digital en España. Su objetivo principal son LOIs firmadas de clientes españoles para el expediente del CEO; después, ingreso real y recurrencia.

La Directora General (la sesión principal de Claude Code) dirige a seis líderes (subagentes) y reporta solo al CEO. Le entrega Órdenes de Ejecución (OEF) para todo lo que requiere su identidad o su presencia: enviar correos desde sus cuentas, llamar, reunirse, firmar y cobrar.

`CLAUDE.md` es la constitución y se carga sola en cada sesión. `contexto/` es lo que el equipo sabe del negocio. Todo lo demás es estado, plantillas y herramientas.

## Puesta en marcha (una sola vez)

**1. Responde las preguntas de `bandeja/CEO.md`.**
Con las cuatro primeras basta para arrancar. Si conoces ya la fecha límite y la jurisdicción, ponlas también en `estado/parametros.json`.

**2. Sube los activos a `activos/`**, o incluye el conector de Google Drive en la tarea programada. La lista está en `activos/README.md`.

**3. Sube esta carpeta a un repo privado de GitHub.**
Incluye la carpeta oculta `.claude`. No pongas protección de rama en `main`: la tarea programada sube ahí sus cambios.

```bash
cd saldana-agentes
git init -b main
git add -A
git commit -m "Equipo de Saldaña Digital: configuración inicial"
gh repo create saldana-agentes --private --source=. --push
```

Sin `gh`: crea el repo vacío en github.com y haz `git remote add origin <url>` y `git push -u origin main`.

**4. Conecta GitHub a Claude** en claude.ai/code, si no lo está ya.

**5. Crea la tarea programada** en claude.ai/code/routines → *New task*, o con `/schedule` desde Claude Code.
- **Nombre:** Sesión diaria · Directora General
- **Instrucciones:** el bloque de abajo.
- **Trigger:** Schedule → Daily, 6:45 a.m. hora local. Evita la hora en punto: esas ejecuciones pueden arrancar varios minutos tarde.
- **Repositorio:** este repo. **Entorno:** Default.
- **Conectores:** solo los que quieras que el equipo pueda leer (Google Drive para los activos). El equipo no envía nada desde tus cuentas en ningún caso.
- **Modelo:** el que quieras para la Directora. Los líderes usan el que indica su archivo en `.claude/agents/`.

```
Eres la Directora General del equipo de Saldaña Digital. Ejecuta de principio a fin el Protocolo de sesión de CLAUDE.md (sección 15).
Usa la fecha local de estado/parametros.json → zona_horaria.
Al terminar, sube los cambios directamente a la rama main con git push origin HEAD:main. Nunca dejes el trabajo en una rama claude/ y nunca uses force.
Si el push es rechazado, haz git pull --rebase origin main, resuelve conservando ambas versiones de bandeja/CEO.md y vuelve a subir. Si aun así no puedes, explica el motivo en tu respuesta final.
Si la bandeja no trae nada nuevo y todo lo pendiente depende del CEO, escribe un reporte de 3 líneas, sube y termina.
```

**6. Pulsa *Run now*.**
La primera sesión procesa tus respuestas y, si lo bloqueante está resuelto, pasa a la Fase 1 (Plan de Activación).

## Tu rutina como CEO

1. Lee el último `reportes/AAAA-MM-DD.md`, o abre la ejecución en claude.ai/code/routines.
2. Responde en `bandeja/CEO.md`: aprobaciones (`APROBADO APR-007`), OEF ejecutadas, eventos comerciales (envíos hechos, respuestas, llamadas, LOIs), dinero movido e instrucciones. Puedes editarlo desde la app de GitHub en el móvil.
3. Envía tú los lotes de borradores aprobados desde `salidas/borradores/` y anota el envío en la bandeja.
4. La siguiente ejecución lo procesa.

Lo que no esté en la bandeja no existe para el equipo. Un correo que envíes y no anotes no cuenta, y el equipo podría volver a escribir a esa cuenta.

Evita editar la bandeja durante la ejecución diaria. El protocolo resuelve el conflicto, pero es más limpio editar antes o después.

## Controles

- **Pausar:** interruptor de la tarea en claude.ai/code/routines.
- **Ejecutar fuera de horario:** *Run now* en la misma página.
- **Disolver:** el equipo te envía una Propuesta de Disolución con un APR; solo tu `APROBADO` la ejecuta.
- **Cambiar reglas:** edita `CLAUDE.md` o `estado/parametros.json`. Los agentes no los modifican.

## Qué hay en cada sitio

- `CLAUDE.md`: constitución, mandato, gobierno y protocolo de sesión.
- `.claude/agents/`: los seis líderes. Contratar es crear un archivo; aprobar un subequipo es darle la herramienta `Agent` al líder.
- `.claude/settings.json`: límites técnicos (anidación de subequipos a dos niveles, sin force push).
- `contexto/`: el negocio, el historial comercial, la oferta y el inventario de activos.
- `activos/`: tus activos, para que el equipo los use en lugar de rehacerlos.
- `cuentas/`: una ficha por cuenta cualificada.
- `salidas/`: diagnósticos, borradores para enviar, material de cierre y planes de entrega.
- `estado/`: parámetros, foto actual, pipeline comercial, libro contable, horas y decisiones.
- `bandeja/`: tu canal de entrada y su archivo.
- `oef/`, `actas/`, `reportes/`, `sops/`: una pieza por archivo, cada una con su plantilla.
- `herramientas/caja.py`: caja, tramos, horas y alertas. `herramientas/pipeline.py`: embudo, estado por cuenta, higiene de contactos y criterio de corte. Los dos tienen `--verificar`, que comprueba que sus registros solo crecen.

## Límites conocidos

- Las ejecuciones en la nube tienen un mínimo de una hora entre sí y cuentan contra tu plan de Claude. Cada subagente gasta sus propios tokens.
- Cada ejecución clona el repo desde cero: lo que no se sube a `main` se pierde.
- El entorno Default restringe el acceso de red de los scripts. La búsqueda web de los agentes no depende de eso, pero un script que descargue páginas sí.
- Todos los agentes son el mismo modelo con roles distintos. La separación de funciones y permisos reduce el autoengaño, pero no sustituye el criterio del CEO.
- La carga inicial de `estado/pipeline.csv` se hizo a partir del historial de trabajo hasta el 30 de octubre de 2026 y puede tener fechas aproximadas. Las correcciones se añaden como filas nuevas.
