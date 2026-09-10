# TermoIA-UAMC

**Repositorio abierto de actividades de enseñanza y aprendizaje con inteligencia artificial y Diseño Universal para el Aprendizaje (DUA) para la UEA 4603003, Introducción a la Termodinámica, Licenciatura en Biología Molecular, UAM Cuajimalpa.**

**Versión:** 1.0.0 · **Fecha de liberación:** 2026-09-10 · **Idioma principal:** español

## Propósito

TermoIA-UAMC convierte un curso de termodinámica de 12 semanas en una secuencia reproducible de experiencias de aprendizaje en las que la IA se usa como **interlocutor falible**, no como fuente de autoridad. El ciclo transversal es:

> **Predecir → interrogar/retar a la IA → verificar → explicar → documentar evidencia.**

El repositorio está pensado para ser permanente, versionable y citable. Los contenidos nucleares no dependen de una marca o modelo de IA; las actividades pueden ejecutarse con un asistente generativo disponible, con un modelo local o, cuando no haya acceso, con el banco de salidas de IA incluido en el repositorio.

## Contexto curricular

- Institución: Universidad Autónoma Metropolitana, Unidad Cuajimalpa.
- División: Ciencias Naturales e Ingeniería.
- Licenciatura: Biología Molecular.
- UEA: **Introducción a la Termodinámica (4603003)**.
- Estructura adoptada del syllabus docente: **12 semanas, 6 h por semana**, organizadas normalmente en tres sesiones de 2 h; las prácticas pueden ocupar bloques distintos.
- Alcance: termodinámica clásica y biomolecular introductoria. **No se incluye estadística inferencial**.
- Prácticas: tres experiencias de bajo costo y sin equipo especializado de laboratorio.

## Qué hace diferente a este repositorio

1. **IA auditable:** toda salida relevante de IA se trata como una afirmación que debe clasificarse, verificarse y, si procede, corregirse.
2. **DUA desde el diseño:** cada actividad ofrece opciones equivalentes de representación, acción/expresión y participación sin reducir el nivel conceptual.
3. **Evidencia de aprendizaje trazable:** cada actividad tiene un ID estable (`TIA-Wxx-Sy`) y produce un artefacto verificable.
4. **Permanencia tecnológica:** los prompts son agnósticos al proveedor y existe una ruta sin IA en tiempo real.
5. **Ciencia abierta docente:** incluye metadatos de citación, versionado semántico, licencias y una ruta explícita GitHub → release → Zenodo/DOI.
6. **Evaluación compatible con recursos abiertos:** se evalúa razonamiento, verificación, provenance y defensa, no la capacidad de ocultar el uso de herramientas.

## Mapa del repositorio

```text
TermoIA-UAMC/
├── README.md
├── CITATION.cff
├── codemeta.json
├── .zenodo.json
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE-MATERIALS.md
├── LICENSE-CODE.txt
├── mkdocs.yml
├── requirements.txt
├── environment.yml
├── config/
│   ├── course.yml
│   └── evaluacion.yml
├── docs/
│   ├── index.md
│   ├── 00_mapa_curso.md
│   ├── 01_modelo_pedagogico.md
│   ├── 02_guia_docente.md
│   ├── 03_guia_estudiante.md
│   ├── 04_politica_ia.md
│   ├── 05_dua_accesibilidad.md
│   ├── 06_evaluacion_rubricas.md
│   ├── 07_bibliografia.md
│   ├── 08_versionado_citacion.md
│   └── 09_operacion_trimestral.md
├── semanas/
│   └── semana_01.md ... semana_12.md
├── practicas/
│   ├── P01_calorimetria_mezclas.md
│   ├── P02_hielo_sal_potencial_quimico.md
│   └── P03_osmosis_tejido_vegetal.md
├── actividades/
│   ├── catalogo.csv
│   ├── banco_salidas_ia_estudiante.md
│   └── banco_salidas_ia_clave_docente.md
├── plantillas/
│   ├── bitacora_ia.md
│   ├── ficha_actividad.md
│   ├── informe_practica.md
│   └── evidencia_multiformato.md
├── notebooks/
│   ├── 01_primera_ley.ipynb
│   ├── 02_entropia_mezcla.ipynb
│   ├── 03_gibbs_equilibrio.ipynb
│   └── 04_union_ligando.ipynb
└── tools/
    ├── generate_problem.py
    └── validate_repo.py
```

## Inicio rápido

**Docente:** lea `docs/02_guia_docente.md`, congele la versión del repositorio que usará durante el trimestre y publique a estudiantes el mapa de curso y la política de IA. Las ponderaciones sugeridas están en `config/evaluacion.yml` y pueden modificarse sin alterar el núcleo pedagógico.

**Estudiante:** lea `docs/03_guia_estudiante.md` y `docs/04_politica_ia.md`. Para cualquier actividad que use IA, conserve una bitácora siguiendo `plantillas/bitacora_ia.md`.

**Notebooks:**

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

## Principio de evaluación

Una respuesta producida por IA no obtiene crédito por sí sola. El crédito proviene de la **decisión humana justificable**: identificar supuestos, escoger el sistema y las fronteras, establecer signos y unidades, derivar o reconstruir la relación usada, contrastar la salida con física básica y explicar por qué la conclusión es válida o inválida.

## Citación

Use la función **“Cite this repository”** de GitHub cuando `CITATION.cff` esté publicado. Para una versión archivada, cree un release y deposite la versión en Zenodo; después actualice el DOI en `CITATION.cff` y `.zenodo.json` en la siguiente versión. Consulte `docs/08_versionado_citacion.md`.

## Licencias

- Materiales docentes, textos, guías y plantillas: **CC BY 4.0**, ver `LICENSE-MATERIALS.md`.
- Código y notebooks: **MIT**, ver `LICENSE-CODE.txt`.

## Estado

`v1.0.0` es una primera versión completa y utilizable. Los cambios sustantivos al diseño pedagógico deben documentarse en `CHANGELOG.md` y conservar IDs estables cuando el objetivo de aprendizaje no cambie.
