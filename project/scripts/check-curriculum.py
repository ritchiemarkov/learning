#!/usr/bin/env python3
"""Check offline inventories, curriculum routes, lesson structure and coverage maps."""
import importlib.util
import json
import re
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('html_reference', PROJECT / 'scripts/build-html-reference.py')
reference = importlib.util.module_from_spec(spec)
spec.loader.exec_module(reference)
for name, content in reference.render().items():
    assert (PROJECT / 'docs/html' / name).read_text() == content, f'HTML reference drift: {name}'

for area, expected in [('html', 26), ('css', 35)]:
    lessons = []
    for path in (PROJECT / 'docs' / area).glob('*.md'):
        text = path.read_text()
        match = re.match(r'# (\d+) ·', text)
        if match:
            lessons.append(int(match[1]))
            assert '**Obiettivo:**' in text, f'Missing objective: {path}'
            assert '## Esercizio' in text, f'Missing exercise: {path}'
            assert '::: details' in text, f'Missing solution or verification: {path}'
            assert 'https://' in text, f'Missing source: {path}'
    assert sorted(lessons) == list(range(1, expected + 1)), (area, lessons)

curriculum = json.loads((PROJECT / 'sources/css/curriculum.json').read_text())
assert len(curriculum['google_modules']) == 37
assert len({m['url'] for m in curriculum['google_modules']}) == 37
assert [e['number'] for e in curriculum['lessons']] == list(range(1, 36))
for module in curriculum['google_modules']:
    assert module['lessons'], module
    for slug in module['lessons']:
        assert (PROJECT / f'docs/css/{slug}.md').is_file(), slug
coverage = (PROJECT / 'docs/css/copertura.md').read_text()
for module in curriculum['google_modules']:
    assert f'[{module["title"]}]({module["url"]})' in coverage, f'Missing coverage row: {module["title"]}'

for area in ('html', 'css'):
    sidebar = json.loads((PROJECT / f'docs/.vitepress/{area}-sidebar.json').read_text())
    links = set()
    def visit(items):
        for item in items:
            if 'link' in item:
                links.add(item['link'])
                route = item['link'].strip('/')
                path = PROJECT / 'docs' / (route + (('/index.md') if item['link'].endswith('/') else '.md'))
                assert path.is_file(), item['link']
            visit(item.get('items', []))
    visit(sidebar)
    for path in (PROJECT / f'docs/{area}').glob('*.md'):
        if re.match(r'# \d+ ·', path.read_text()):
            assert f'/{area}/{path.stem}' in links, f'Missing sidebar entry: {path}'

print('Curriculum verified: HTML 26 lessons and full snapshot inventory; CSS 35 lessons and 37/37 Google topic mappings.')
