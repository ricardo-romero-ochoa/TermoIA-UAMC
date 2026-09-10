# Versionado, archivo y citación

## Objetivo de permanencia

Una actividad docente solo es referenciable si una persona puede saber **qué versión** se usó. Por ello TermoIA-UAMC adopta versionado semántico:

- `MAJOR`: cambia la arquitectura pedagógica o los resultados globales.
- `MINOR`: añade semanas, variantes o herramientas compatibles.
- `PATCH`: corrige errores sin cambiar el propósito de una actividad.

## Flujo recomendado GitHub → Zenodo

1. Publique el repositorio en GitHub.
2. Proteja la rama principal y use tags (`v1.0.0`, `v1.0.1`, etc.).
3. Conecte el repositorio a Zenodo.
4. Cree un GitHub Release para `v1.0.0`.
5. Zenodo archivará la versión y asignará DOI de versión y DOI conceptual.
6. En la siguiente revisión, agregue el DOI a `CITATION.cff` y a los metadatos.

## Qué debe citar un tercero

Idealmente: autor, año, título, versión y DOI de la versión utilizada. El DOI conceptual sirve para referirse al proyecto en general; el DOI de versión permite reproducir una implementación concreta.

## IDs estables

Las actividades usan `TIA-W01-S1`, etc. El ID identifica el **objeto pedagógico**, mientras que el tag del repositorio identifica su versión. Esto permite escribir, por ejemplo: “Se aplicó TIA-W05-S3, versión 1.2.0”.

## Núcleo y capa trimestral

Nunca guarde listas de estudiantes, calificaciones o adaptaciones personales en el repositorio público. Las configuraciones de un trimestre deben ir en un directorio local `cohorts/`, ignorado por Git.
