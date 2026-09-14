# Activación de GitHub Pages para TermoIA-UAMC

Este repositorio ya incluye el workflow `.github/workflows/pages.yml`. No necesitas crear una rama `gh-pages` ni ejecutar `mkdocs gh-deploy`.

## Después de subir el repositorio a GitHub

1. Abre el repositorio en GitHub.
2. Entra en **Settings**.
3. En la barra lateral, entra en **Pages**.
4. En **Build and deployment**, busca **Source**.
5. Selecciona **GitHub Actions**.
6. Si el primer workflow automático falló antes de activar Pages, no es un problema; se volverá a ejecutar en el paso siguiente.
7. Vuelve a la pestaña **Actions** del repositorio.
8. Abre el workflow **Deploy TermoIA-UAMC to GitHub Pages**.
9. Si todavía no se ejecutó automáticamente, pulsa **Run workflow**, deja seleccionada la rama `main` y confirma.
10. Espera a que los jobs **build** y **deploy** aparezcan en verde.
11. Vuelve a **Settings → Pages**. GitHub mostrará la URL publicada del sitio.

La URL tendrá normalmente esta forma:

`https://USUARIO.github.io/NOMBRE-DEL-REPOSITORIO/`

Si el repositorio se llama `TermoIA-UAMC`, normalmente será:

`https://USUARIO.github.io/TermoIA-UAMC/`

Ese es el enlace recomendado para compartir con estudiantes.

## Actualizaciones posteriores

Cada `push` a `main` ejecuta automáticamente el workflow, valida el repositorio, reconstruye MkDocs y vuelve a desplegar Pages. No necesitas republicar manualmente.

## Prueba local opcional

```bash
python -m venv .venv
```

Activa el entorno e instala las dependencias del sitio:

```bash
pip install -r requirements-docs.txt
mkdocs serve
```

Abre la dirección local indicada por MkDocs. Para probar exactamente el modo de compilación usado por GitHub:

```bash
python tools/validate_repo.py
mkdocs build --strict
```

## Material privado

No subas el paquete `TermoIA-UAMC-docente-privado-v1.1.0.zip` al repositorio. El sitio público no contiene la clave docente.
