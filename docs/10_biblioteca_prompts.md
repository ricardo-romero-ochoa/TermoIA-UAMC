# Biblioteca de prompts funcionales y agnósticos al proveedor

Los prompts se describen por **función pedagógica**, no por marca de IA. Deben adaptarse al problema concreto. La regla transversal es: pedir supuestos, evitar que el modelo dé autoridad a su propia respuesta y exigir una verificación externa.

## 1. Tutor socrático

> No me des la solución. Hazme una pregunta a la vez para que yo identifique sistema, frontera, variables, proceso y ley termodinámica aplicable. Si mi respuesta contiene un error, señala únicamente la categoría del error y pídeme corregirlo.

## 2. Auditor dimensional

> Revisa esta derivación solo en dimensiones, unidades y consistencia de símbolos. No corrijas todavía la física. Devuelve una tabla con expresión, dimensión esperada, dimensión obtenida y punto a revisar.

## 3. Adversario termodinámico

> Intenta refutar mi conclusión usando un contraejemplo físicamente posible o un límite del modelo. Separa: error lógico, supuesto no declarado, excepción real y simple cambio de condiciones.

## 4. Detector de confusión termodinámica/cinética

> Marca cada frase de mi explicación como termodinámica, cinética, ambas o ninguna. Señala cualquier inferencia de velocidad basada únicamente en ΔG, K, entalpía o entropía.

## 5. Traductor de representaciones

> Convierte mi explicación en: (a) un diagrama de sistema y frontera descrito en texto, (b) una lista de ecuaciones mínimas y (c) una gráfica cualitativa descrita verbalmente. No añadas física nueva. Yo verificaré que las tres representaciones sean equivalentes.

## 6. Generador de límites

> Para esta ecuación, propón tres límites físicos simples que deberían recuperarse (por ejemplo variable→0, concentraciones iguales, estado de equilibrio). No evalúes la ecuación; solo especifica qué debería ocurrir en cada límite.

## 7. Crítico experimental

> Propón cinco fuentes de discrepancia para este experimento. Para cada una indica: mecanismo físico, variable afectada y signo esperado del sesgo cuando pueda predecirse. No uses “error humano” como explicación genérica.

## 8. Examinador oral

> Hazme cinco preguntas crecientes sobre mi solución. Incluye obligatoriamente una sobre supuestos, una sobre unidades/signos, una sobre un límite, una sobre interpretación biológica y una que cambie una condición del problema. No me des respuestas hasta el final.

## 9. Auditor de código

> Revisa este código como implementación de un modelo termodinámico. Separa errores de programación, errores matemáticos y errores de modelado físico. No asumas que un resultado numérico plausible es correcto.

## 10. Simplificación accesible controlada

> Reescribe esta explicación para reducir carga lingüística sin eliminar ecuaciones, supuestos, condiciones de validez ni vocabulario técnico indispensable. Después lista cualquier precisión científica que pudiera haberse perdido al simplificar.

## Regla de uso

Un prompt bueno no es el que produce la respuesta más larga, sino el que hace más fácil **verificar, refutar o reconstruir** la salida.
