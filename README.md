# TermoIA-UAMC

**Repositorio abierto de enseñanza y aprendizaje con inteligencia artificial auditable y Diseño Universal para el Aprendizaje (DUA) para Introducción a la Termodinámica, Licenciatura en Biología Molecular, UAM Cuajimalpa.**

**Versión:** 1.1.0 · **Fecha de liberación:** 2026-09-14 · **Idioma principal:** español

## Comenzar

- [START_HERE.md](START_HERE.md)
- Estudiantes: `docs/03_guia_estudiante.md`
- Docentes: `docs/02_guia_docente.md`
- Activar el sitio: [GITHUB_PAGES_SETUP.md](GITHUB_PAGES_SETUP.md)

La interfaz recomendada para estudiantes es **GitHub Pages**. El repositorio conserva las fuentes, notebooks, historial y metadatos de citación.

## Principio pedagógico

> **Predecir → Interrogar → Verificar → Explicar → Documentar (PIVED).**

La IA funciona como interlocutor falible. Una salida generada no cuenta como evidencia por sí sola: debe auditarse mediante termodinámica, matemáticas, simulación, experimento o fuentes académicas.

## Contenido

- 12 semanas y 36 actividades con IDs estables `TIA-Wxx-Sy`;
- 3 prácticas experimentales de bajo costo;
- 4 notebooks reproducibles;
- banco de respuestas de IA para trabajo sin acceso a un modelo en tiempo real;
- política de IA, bitácoras, rúbricas y matriz DUA–IA;
- sitio MkDocs/Material desplegable automáticamente con GitHub Actions;
- metadatos de citación y ruta GitHub → release → Zenodo/DOI.

## Estructura pública

```text
TermoIA-UAMC/
├── START_HERE.md
├── GITHUB_PAGES_SETUP.md
├── PRIVATE_MATERIALS.md
├── mkdocs.yml
├── requirements-docs.txt
├── .github/workflows/pages.yml
├── docs/
│   ├── index.md
│   ├── semanas/
│   ├── practicas/
│   ├── actividades/
│   ├── plantillas/
│   └── notebooks/
├── config/
└── tools/
```

Las claves docentes, datos de estudiantes y evaluaciones reservadas **no forman parte del repositorio público**.

## Construcción local del sitio

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements-docs.txt
python tools/validate_repo.py
mkdocs serve
```

Para la compilación estricta usada en CI:

```bash
mkdocs build --strict
```

## Citación

Use **Cite this repository** cuando GitHub reconozca `CITATION.cff`. Para versiones archivadas, cree un release y vincule el repositorio con Zenodo. Cite siempre la versión específica utilizada.

## Licencias

- Materiales docentes: **CC BY 4.0**.
- Código y notebooks: **MIT**.
