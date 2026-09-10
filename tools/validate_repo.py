#!/usr/bin/env python3
from pathlib import Path
import csv, json, sys

ROOT=Path(__file__).resolve().parents[1]
errors=[]

# Required files
required=['README.md','CITATION.cff','.zenodo.json','config/course.yml','actividades/catalogo.csv']
for rel in required:
    if not (ROOT/rel).exists(): errors.append(f"Falta {rel}")

# Weeks
for w in range(1,13):
    p=ROOT/f'semanas/semana_{w:02d}.md'
    if not p.exists(): errors.append(f"Falta {p.relative_to(ROOT)}")

# Stable IDs and uniqueness
cat=ROOT/'actividades/catalogo.csv'
if cat.exists():
    with cat.open(encoding='utf-8') as f:
        rows=list(csv.DictReader(f))
    ids=[r['id'] for r in rows]
    if len(rows)!=36: errors.append(f"Catálogo debe tener 36 actividades, tiene {len(rows)}")
    if len(set(ids))!=len(ids): errors.append('Hay IDs duplicados')
    for w in range(1,13):
        for s in range(1,4):
            aid=f'TIA-W{w:02d}-S{s}'
            if aid not in ids: errors.append(f'Falta {aid}')

# JSON metadata
for rel in ['.zenodo.json','codemeta.json']:
    try: json.loads((ROOT/rel).read_text(encoding='utf-8'))
    except Exception as e: errors.append(f'{rel}: JSON inválido: {e}')

if errors:
    print('VALIDATION FAILED')
    for e in errors: print('-',e)
    sys.exit(1)
print('VALIDATION OK: estructura completa, 12 semanas, 36 IDs únicos y JSON válido.')
