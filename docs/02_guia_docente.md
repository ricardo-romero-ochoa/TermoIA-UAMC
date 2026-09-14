# Guía de uso docente

## 1. Propósito

TermoIA-UAMC es un repositorio abierto para una UEA de Introducción a la Termodinámica de 12 semanas. La IA se utiliza como **interlocutor falible**, no como autoridad. El ciclo transversal es:

> **Predecir → Interrogar → Verificar → Explicar → Documentar (PIVED).**

El objetivo es que el estudiantado aprenda a justificar una afirmación termodinámica incluso si la respuesta de IA desaparece.

## 2. Antes del trimestre

1. Fije la versión que utilizará, por ejemplo `v1.1.0`.
2. Revise el [Mapa del curso](00_mapa_curso.md), la [Política de IA](04_politica_ia.md) y las [rúbricas](06_evaluacion_rubricas.md).
3. Defina las ponderaciones en `config/evaluacion.yml` si necesita adaptarlas.
4. Publique a estudiantes el sitio de GitHub Pages, no la vista de archivos de GitHub, como puerta de entrada principal.
5. Mantenga claves, exámenes no liberados y datos de estudiantes fuera del repositorio público.

## 3. Cómo operar una actividad PIVED

### Predecir

Antes de usar IA, el estudiante formula una predicción, diagrama, ecuación, hipótesis o explicación inicial. Esto deja evidencia del razonamiento previo.

### Interrogar

La IA puede actuar como tutor socrático, adversario conceptual, generador de hipótesis, crítico de soluciones o traductor entre representaciones. Evite convertir la tarea en “pide la solución”.

### Verificar

Toda afirmación relevante debe contrastarse de forma independiente mediante una o más de estas vías:

- derivación;
- análisis dimensional;
- caso límite;
- cálculo;
- ley física;
- simulación;
- experimento;
- fuente académica adecuada.

Preguntar lo mismo a otra IA **no cuenta** como verificación independiente.

### Explicar

El estudiante reconstruye la conclusión con razonamiento propio, dejando explícitos sistema, frontera, supuestos, signos, unidades y criterio físico.

### Documentar

Cuando la IA influya en un producto evaluado, use la [Bitácora de IA](plantillas/bitacora_ia.md).

## 4. Estructura sugerida para una sesión de 120 minutos

| Tiempo | Actividad |
|---|---|
| 0–15 min | activación, fenómeno o predicción individual |
| 15–35 min | construcción conceptual y formalización |
| 35–55 min | resolución inicial sin IA |
| 55–80 min | interacción o auditoría de IA |
| 80–105 min | verificación independiente |
| 105–115 min | síntesis y explicación final |
| 115–120 min | cierre metacognitivo |

La estructura es orientativa. No todas las sesiones necesitan IA.

## 5. Ruta sin IA en tiempo real

Ninguna calificación debe depender de una suscripción. El [Banco de salidas de IA para estudiantes](actividades/banco_salidas_ia_estudiante.md) permite auditar respuestas pre-generadas con los mismos criterios.

## 6. DUA

El diseño ofrece múltiples medios de:

- **representación:** texto, ecuaciones, diagramas, gráficas, simulaciones y demostraciones;
- **acción y expresión:** texto, esquema, presentación, audio con transcripción, notebook o mapa conceptual cuando el resultado de aprendizaje lo permita;
- **implicación:** problemas auténticos, contextos biomoleculares, trabajo individual/colaborativo y elección entre casos.

Cambiar el formato no reduce el rigor. Consulte [DUA y accesibilidad](05_dua_accesibilidad.md) y la [Matriz DUA–IA](11_matriz_dua_ia.md).

## 7. Prácticas

Las tres prácticas de bajo costo son:

1. [Calorimetría de mezclas](practicas/P01_calorimetria_mezclas.md).
2. [Hielo, sal y potencial químico](practicas/P02_hielo_sal_potencial_quimico.md).
3. [Osmosis en tejido vegetal](practicas/P03_osmosis_tejido_vegetal.md).

La IA puede ayudar a generar hipótesis o criticar interpretaciones, pero nunca a fabricar datos u observaciones.

## 8. Evaluación

La configuración inicial propone:

| Componente | Porcentaje |
|---|---:|
| Actividades formativas y bitácora IA | 20 % |
| Problemas y micro-simulaciones | 20 % |
| Tres prácticas experimentales | 24 % |
| Evaluaciones integradoras | 20 % |
| Proyecto final y defensa | 16 % |

Evalúe principalmente: definición del sistema, supuestos, variables, signos, unidades, relaciones termodinámicas, interpretación, verificación, corrección de errores, trazabilidad y capacidad de defensa.

## 9. Defensa oral

Para productos importantes, una defensa breve de 3–5 minutos es útil. Preguntas típicas:

- ¿Cuál es el sistema y cuál su frontera?
- ¿Cuál es el supuesto más importante?
- ¿Qué parte de la salida de IA rechazaste o corregiste?
- ¿Cómo verificaste esta ecuación?
- ¿Qué límite debe recuperar tu expresión?
- ¿Qué cambiaría si modificamos esta condición?

Esto produce mejor evidencia de aprendizaje que intentar “detectar IA” en un texto.

## 10. Al finalizar el trimestre

Registre erratas, barreras de accesibilidad, actividades realmente utilizadas y cambios pedagógicos útiles. Incorpore mejoras en una versión nueva sin alterar IDs estables cuando el objetivo esencial de la actividad se mantenga.
