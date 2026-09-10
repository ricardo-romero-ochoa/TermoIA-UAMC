# Guía docente

## Antes del trimestre

1. Fije la versión del repositorio que se usará; no cambie actividades evaluadas a mitad del trimestre sin documentarlo.
2. Ajuste `config/evaluacion.yml` a la ponderación del syllabus vigente.
3. Decida qué herramienta(s) de IA estarán disponibles. No diseñe ninguna actividad que requiera una marca concreta.
4. Explique la política de privacidad y ofrezca la ruta sin IA en tiempo real mediante `actividades/banco_salidas_ia_estudiante.md`.
5. Pruebe los cuatro notebooks o elimine del calendario los que no puedan ejecutarse en el entorno disponible.

## Durante la clase

La regla operativa es **predicción antes de IA**. Si el grupo consulta primero al modelo, se pierde el contraste metacognitivo. Pida que toda salida relevante se marque con una de cinco etiquetas:

- `C`: conceptualmente verificable;
- `M`: matemática/algebraicamente verificable;
- `U`: depende de unidades o convención de signos;
- `E`: requiere evidencia externa;
- `N`: no verificable o no necesario para resolver el problema.

Después, solicite una decisión: **aceptar, corregir, rechazar o dejar indeterminado**.

## Preguntas docentes de alto rendimiento

- ¿Cuál es el sistema y qué cruza su frontera?
- ¿Qué magnitud es función de estado y cuál depende de la trayectoria?
- ¿Qué convención de signos estás usando?
- ¿Qué límite simple debería recuperar tu ecuación?
- ¿La IA está describiendo espontaneidad o velocidad?
- ¿Qué observación invalidaría tu explicación?
- ¿Puedes defender la misma conclusión sin mencionar a la IA?

## Equidad de acceso

No haga depender una calificación de pagar una suscripción. Si un estudiante no puede o no desea usar IA externa, asigne la misma actividad con una salida del banco pre-generado. Evalúe el trabajo de verificación, no el acceso a la herramienta.

## Evaluación oral breve

Para productos importantes, una defensa de 3–5 min por equipo o muestreo aleatorio es más informativa que intentar “detectar IA”. Pregunte por un supuesto, un signo, un límite y una corrección hecha durante el proceso.

## Material público vs evaluación sumativa

El repositorio es público. Por ello, evite guardar exámenes reutilizables con respuestas. Use problemas parametrizados, defensa oral, datos del día o variantes generadas con `tools/generate_problem.py`. El aprendizaje abierto y la evaluación válida son compatibles si se evalúa reconstrucción y transferencia.
