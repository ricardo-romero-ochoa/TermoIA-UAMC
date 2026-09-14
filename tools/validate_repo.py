#!/usr/bin/env python3
from pathlib import Path
import csv, json, sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

required = [
    'README.md', 'START_HERE.md', 'CITATION.cff', '.zenodo.json',
    'mkdocs.yml', 'requirements-docs.txt', '.github/workflows/pages.yml',
    'config/course.yml', 'docs/actividades/catalogo.csv',
    'docs/03_guia_estudiante.md', 'docs/02_guia_docente.md'
]
for rel in required:
    if not (ROOT / rel).exists():
        errors.append(f'Falta {rel}')

for w in range(1, 13):
    p = ROOT / f'docs/semanas/semana_{w:02d}.md'
    if not p.exists():
        errors.append(f'Falta {p.relative_to(ROOT)}')

for p in [
    'docs/practicas/P01_calorimetria_mezclas.md',
    'docs/practicas/P02_hielo_sal_potencial_quimico.md',
    'docs/practicas/P03_osmosis_tejido_vegetal.md'
]:
    if not (ROOT / p).exists():
        errors.append(f'Falta {p}')

cat = ROOT / 'docs/actividades/catalogo.csv'
if cat.exists():
    with cat.open(encoding='utf-8') as f:
        rows = list(csv.DictReader(f))
    ids = [r['id'] for r in rows]
    if len(rows) != 36:
        errors.append(f'Catálogo debe tener 36 actividades, tiene {len(rows)}')
    if len(set(ids)) != len(ids):
        errors.append('Hay IDs duplicados')
    for w in range(1, 13):
        for s in range(1, 4):
            aid = f'TIA-W{w:02d}-S{s}'
            if aid not in ids:
                errors.append(f'Falta {aid}')

for rel in ['.zenodo.json', 'codemeta.json']:
    try:
        json.loads((ROOT / rel).read_text(encoding='utf-8'))
    except Exception as e:
        errors.append(f'{rel}: JSON inválido: {e}')

# Public release must not contain teacher keys or student data.
for forbidden in [
    ROOT / 'docs/actividades/banco_salidas_ia_clave_docente.md',
    ROOT / 'actividades/banco_salidas_ia_clave_docente.md'
]:
    if forbidden.exists():
        errors.append(f'Material privado expuesto: {forbidden.relative_to(ROOT)}')

# Lightweight validation of files referenced by MkDocs nav and local Markdown links.
try:
    import re
    cfg = (ROOT / 'mkdocs.yml').read_text(encoding='utf-8')
    for rel in re.findall(r':\s+([A-Za-z0-9_./-]+\.(?:md|ipynb))\s*$', cfg, flags=re.M):
        if not (ROOT / 'docs' / rel).exists():
            errors.append(f'mkdocs.yml referencia archivo inexistente: docs/{rel}')
    link_re = re.compile(r'\[[^]]+\]\(([^)]+)\)')
    for md in (ROOT / 'docs').rglob('*.md'):
        for target in link_re.findall(md.read_text(encoding='utf-8')):
            if target.startswith(('http://','https://','#','mailto:')):
                continue
            target = target.split('#',1)[0].split('?',1)[0]
            if not target:
                continue
            dest = (md.parent / target).resolve()
            try:
                dest.relative_to((ROOT / 'docs').resolve())
            except ValueError:
                errors.append(f'Enlace de documentación escapa docs/ en {md.relative_to(ROOT)}: {target}')
                continue
            if not dest.exists():
                errors.append(f'Enlace local roto en {md.relative_to(ROOT)}: {target}')
except Exception as e:
    errors.append(f'No se pudo validar navegación/enlaces: {e}')

workflow = (ROOT / '.github/workflows/pages.yml').read_text(encoding='utf-8') if (ROOT / '.github/workflows/pages.yml').exists() else ''
for token in ['actions/configure-pages@v5', 'actions/upload-pages-artifact@v4', 'actions/deploy-pages@v4', 'mkdocs build --strict']:
    if token not in workflow:
        errors.append(f'Workflow Pages incompleto: falta {token}')

if errors:
    print('VALIDATION FAILED')
    for e in errors:
        print('-', e)
    sys.exit(1)

print('VALIDATION OK: sitio publicable, navegación consistente, 12 semanas, 36 IDs únicos, 3 prácticas y sin clave docente pública.')
