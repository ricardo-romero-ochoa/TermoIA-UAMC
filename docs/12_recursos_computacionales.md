# Recursos computacionales

Los notebooks sirven para explorar relaciones termodinámicas y visualizar consecuencias de los modelos. La programación es una herramienta; la interpretación física sigue siendo el objetivo.

## Notebooks disponibles

1. [Primera ley](notebooks/01_primera_ley.ipynb)
2. [Entropía de mezcla](notebooks/02_entropia_mezcla.ipynb)
3. [Energía de Gibbs y equilibrio](notebooks/03_gibbs_equilibrio.ipynb)
4. [Unión ligando–receptor](notebooks/04_union_ligando.ipynb)

Los enlaces descargan los archivos `.ipynb`. Si clonas el repositorio también puedes ejecutarlos localmente con JupyterLab.

## Ejecución local

```bash
python -m venv .venv
```

Activa el entorno:

=== "Windows"

    ```powershell
    .venv\Scripts\activate
    ```

=== "Linux/macOS"

    ```bash
    source .venv/bin/activate
    ```

Instala dependencias y abre JupyterLab:

```bash
pip install -r requirements.txt
jupyter lab
```
