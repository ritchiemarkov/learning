#!/usr/bin/env python3
"""Adatta snapshot locali di JavaScript.info a VitePress, senza eseguire il codice importato."""
import argparse, hashlib, html, json, re, shutil, subprocess
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('--italian', type=Path, required=True)
parser.add_argument('--english', type=Path, required=True)
args = parser.parse_args()
PROJECT = Path(__file__).resolve().parents[1]
IT, EN = args.italian.resolve(), args.english.resolve()
OUT = PROJECT / 'docs/javascript/tutorial'
ASSETS = PROJECT / 'docs/public/javascript-info'
OVERRIDES = PROJECT / 'sources/javascript-info/translations'
OUT.mkdir(parents=True, exist_ok=True)

def slug(path): return re.sub(r'^\d+-', '', path.parent.name)
def title(text):
    match = re.search(r'^#\s+(.+)', text, re.M)
    return re.sub(r'<(/?[^>]+)>', r'\1', re.sub(r'\s*\{[^}]*\}\s*$', '', match.group(1))).strip() if match else 'Lezione'
def order(path):
    return tuple((int(re.match(r'\d+', p).group()) if re.match(r'\d+', p) else 999, p) for p in path.parts)

italian = {slug(p): p for p in IT.glob('*/**/article.md')}
english = sorted(EN.glob('*/**/article.md'), key=lambda p: order(p.relative_to(EN)))
articles = []
for original in english:
    key = slug(original)
    override = OVERRIDES / f'{key}.md'
    source = override if override.exists() else italian.get(key)
    if source is None:
        raise SystemExit(f'Manca la traduzione: {key}')
    text = source.read_text()
    articles.append({'slug': key, 'title': title(text), 'source': source, 'original': original,
                     'source_dir': original.parent if source == override else source.parent,
                     'relative': str(original.relative_to(EN)), 'new_translation': source == override})
lookup = {a['slug']: a for a in articles}
assets = set()
external_examples = 0

def target_link(dest, source_dir):
    if dest.startswith('/javascript/'):
        return dest
    if dest.startswith('sandbox:'):
        return 'https://javascript.info/' + slug(source_dir / 'article.md')
    if dest.startswith('info:'):
        key = dest[5:].split('#')[0]
        return '/javascript/tutorial/' + key if key in lookup else 'https://it.javascript.info/' + dest[5:]
    if dest.startswith('mdn:'):
        tail = dest[4:]
        if tail.startswith('js/'):
            tail = 'Web/JavaScript/Reference/Global_Objects/' + tail[3:]
        elif tail.startswith('api/'):
            tail = 'Web/API/' + tail[4:]
        return 'https://developer.mozilla.org/en-US/docs/' + tail
    if dest.startswith('/'):
        key = dest[1:].split('#')[0]
        # I frammenti originali possono avere titoli diversi dopo la traduzione.
        return '/javascript/tutorial/' + key if key in lookup else 'https://it.javascript.info' + dest
    if re.match(r'^(https?:|mailto:|#|data:)', dest): return dest
    raw = dest.split('#')[0].split('?')[0]
    file = (source_dir / raw).resolve()
    if file.is_file() and file.suffix.lower() in {'.svg','.png','.jpg','.jpeg','.gif','.webp'}:
        root = IT if file.is_relative_to(IT) else EN
        rel = file.relative_to(root)
        output = ASSETS / rel
        output.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(file, output)
        assets.add(str(rel))
        return '/javascript-info/' + str(rel)
    # File di esempio e sorgenti rimangono accessibili nel repository originale.
    if file.exists() and (file.is_relative_to(IT) or file.is_relative_to(EN)):
        root = IT if file.is_relative_to(IT) else EN
        repo = 'it.javascript.info' if root == IT else 'en.javascript.info'
        rel = file.relative_to(root)
        return f'https://github.com/javascript-tutorial/{repo}/tree/master/{rel}'
    return 'https://it.javascript.info/' + dest.lstrip('./')


def prose(line, source_dir):
    line = re.sub(r'<info:([^>]+)>', lambda m: '[' + lookup.get(m[1].split('#')[0], {}).get('title', m[1]) + '](' + target_link('info:' + m[1], source_dir) + ')', line)
    line = re.sub(r'(!?\[[^\]]*\]\()([^\s)]+)([^)]*\))', lambda m: m[1] + target_link(m[2],source_dir) + m[3], line)
    line = re.sub(r'`(?:pattern|subject|match):([^`]+)`', r'`\1`', line)
    line = line.replace('{{', '&#123;&#123;').replace('}}', '&#125;&#125;')
    return line


def convert(text, source_dir, key):
    global external_examples
    text = text.lstrip('\ufeff\n')
    # Metadati del renderer originale (libs, importance...) non sono metadati VitePress.
    if not text.startswith('#'):
        marker = re.search(r'^---\s*$', text, re.M)
        if marker: text = text[marker.end():].lstrip()
    text = text.replace('*!*','').replace('*/!*','')
    # Una fence di chiusura del sorgente italiano è attaccata alla frase successiva.
    text = re.sub(r'^(`{3,})(Il codice server-side[^\n]*)$', r'\1\n\n\2', text, flags=re.M)
    text = text.replace('Node.jd', 'Node.js')
    lines = text.splitlines()
    output = []
    stack = []
    skipping = False
    for line in lines:
        m = re.match(r'^(\s*)(`{3,})(.*)$', line)
        if m:
            indent, fence, info = m.groups()
            if not info.strip() and stack and len(fence) >= stack[-1][0]:
                length, kind = stack.pop()
                if kind == 'skip': skipping = False
                elif kind == 'container': output.append(':' * length)
                else: output.append(indent + '`' * length)
                continue
            language = info.strip().split(' ',1)[0]
            if language in {'smart','warn','quote','compare','online','offline'}:
                if language in {'online','offline'}:
                    stack.append((len(fence),'skip'))
                    skipping = True
                    output.extend(['', f'> [Esempio interattivo nell’articolo originale](https://it.javascript.info/{key}).', ''])
                elif language == 'compare':
                    stack.append((len(fence),'container'))
                    output.extend(['', ':' * len(fence) + ' info In sintesi'])
                else:
                    header = re.search(r'header="((?:\\.|[^"\\])*)"', info)
                    label = header.group(1).replace('\\"','"') if header else {'smart':'Da sapere','warn':'Attenzione','quote':'Nota'}[language]
                    label = re.sub(r'</?(?:u|em|strong|span)(?:\s[^>]*)?>', '', label)
                    output.extend(['', ':' * len(fence) + ' ' + ('warning' if language == 'warn' else 'tip') + ' ' + label])
                    stack.append((len(fence),'container'))
                continue
            if skipping: continue
            # I flag run/edit/autorun appartengono al renderer originale, non al linguaggio.
            if language and language not in {'js','javascript','html','css','http','json','text','bash','xml','sql','svg','diff',''}:
                language = 'text'
            output.append(indent + fence + language)
            stack.append((len(fence),'code'))
            continue
        if skipping: continue
        if stack and stack[-1][1] == 'code':
            output.append(line)
            continue
        if re.match(r'^\s*\[(iframe|include|demo|codemirror|codetabs|edit)\b',line):
            external_examples += 1
            output.append(f'[Apri l’esempio nella fonte originale](https://it.javascript.info/{key}).')
            continue
        if re.match(r'^\s*\[(?:\w+)=',line): continue
        # Le dimostrazioni HTML del renderer originale non vengono eseguite nella documentazione.
        if line.strip() == '<div class="domtree"></div>':
            output.append(f'[Visualizza il diagramma DOM nella fonte](https://it.javascript.info/{key}).')
            continue
        if line.strip() in {'<script>', '</script>'}:
            output.append('')
            continue
        if line.strip().startswith('drawHtmlTree('): continue
        output.append(prose(line, source_dir))
    while stack:
        length, kind = stack.pop()
        if kind == 'container': output.append(':' * length)
        elif kind == 'code': output.append('`' * length)
    return '\n'.join(output).strip() + '\n'

manifest = []
task_count = 0
for i, a in enumerate(articles):
    key = a['slug']
    raw = a['source'].read_text()
    body = convert(raw, a['source_dir'], key)
    # Un titolo originale può avere un identificatore usato dal vecchio motore.
    body = re.sub(r'^(#{1,6} .+?)\s+\[#?[a-z0-9_-]+\]\s*$', r'\1', body, flags=re.M)
    meta = {'title': a['title'], 'description': 'JavaScript.info in italiano: ' + a['title'], 'sourceTutorial': True}
    for side, j in [('prev',i-1),('next',i+1)]:
        if 0<=j<len(articles): meta[side]={'text':articles[j]['title'],'link':'/javascript/tutorial/'+articles[j]['slug']}
    header = '---\n' + '\n'.join(k + ': ' + json.dumps(v,ensure_ascii=False) for k,v in meta.items()) + '\n---\n\n'
    notice = f'> **JavaScript.info · Ilya Kantor e contributori.** [Originale inglese](https://javascript.info/{key}) · [Edizione italiana](https://it.javascript.info/{key}) · [Fonti e licenza](/javascript/fonti).\n\n'
    # Il banner segue il titolo, prima dell'articolo.
    match = re.search(r'^# .+$',body,re.M)
    if match: body=body[:match.end()]+'\n\n'+notice+body[match.end():].lstrip()
    tasks_dir = italian.get(key, a['original']).parent
    task_map = {re.sub(r'^\d+-','',p.parent.name):p for p in tasks_dir.glob('*/task.md')}
    for original_task in a['original'].parent.glob('*/task.md'):
        task_key = re.sub(r'^\d+-','',original_task.parent.name)
        if task_key not in task_map:
            translated_task = OVERRIDES / 'tasks' / key / task_key / 'task.md'
            if not translated_task.exists(): raise SystemExit(f'Manca la traduzione dell’esercizio: {key}/{task_key}')
            task_map[task_key] = translated_task
    tasks = sorted(task_map.values(),key=lambda p:order(p.parent))
    if tasks: body += '\n## Esercizi\n\n'
    for number, task in enumerate(tasks,1):
        exercise = convert(task.read_text(),task.parent,key)
        exercise = re.sub(r'^# (.+)$', f'### {number} · '+r'\1',exercise,count=1,flags=re.M)
        body += exercise+'\n'
        solution = task.parent/'solution.md'
        if solution.exists():
            answer = convert(solution.read_text(),task.parent,key)
            answer = re.sub(r'^#{1,3} (.+)$', r'#### \1', answer, flags=re.M)
            body += '::::: details Soluzione\n\n'+answer+'\n:::::\n\n'
        task_count+=1
    (OUT/f'{key}.md').write_text(header+body)
    manifest.append({'slug':key,'title':a['title'],'english_source':a['relative'],
                     'italian_source':str(italian[key].relative_to(IT)) if key in italian else None,
                     'translation':'Learning' if a['new_translation'] else 'javascript-tutorial/it.javascript.info',
                     'sha256':hashlib.sha256(raw.encode()).hexdigest(),'tasks':len(tasks)})

# Indice e sidebar seguono l'ordine delle fonti, con gli argomenti avanzati separati.
GROUP_NAMES = {
 '01-getting-started':'Introduzione','02-first-steps':'Fondamenti','03-code-quality':'Qualità del codice',
 '04-object-basics':'Oggetti: le basi','05-data-types':'Tipi di dato e strutture',
 '06-advanced-functions':'Funzioni avanzate','07-object-properties':'Proprietà degli oggetti',
 '08-prototypes':'Prototipi ed ereditarietà','09-classes':'Classi','10-error-handling':'Errori',
 '11-async':'Promise e async/await','12-generators-iterators':'Generatori e iterazione avanzata',
 '13-modules':'Moduli','99-js-misc':'Approfondimenti sul linguaggio',
 '1-document':'Documento e DOM','2-events':'Eventi','3-event-details':'Eventi delle interfacce',
 '4-forms-controls':'Form e controlli','5-loading':'Caricamento delle risorse','99-ui-misc':'Approfondimenti sul browser',
 '3-frames-and-windows':'Finestre e frame','4-binary':'Dati binari e file','5-network':'Richieste di rete',
 '6-data-storage':'Memorizzazione nel browser','7-animation':'Animazione','8-web-components':'Web Components',
 '9-regular-expressions':'Espressioni regolari'}
groups = {}
for a in articles:
    parts = Path(a['relative']).parts
    group = parts[1] if parts[0] in {'1-js','2-ui'} else parts[0]
    groups.setdefault((parts[0],group),[]).append({'text':a['title'],'link':'/javascript/tutorial/'+a['slug']})
sidebar = [{'text':'JavaScript','items':[{'text':'Come seguire il corso','link':'/javascript/'},{'text':'Tutti i capitoli','link':'/javascript/indice'},{'text':'Fonti e licenza','link':'/javascript/fonti'}]}]
index = '# JavaScript.info: tutti i capitoli\n\n**175 articoli in italiano**, organizzati secondo il tutorial di Ilya Kantor. Gli esercizi con le relative soluzioni si trovano in fondo alle lezioni.\n\nSegui prima il [percorso di base](/javascript/); gli approfondimenti rimangono disponibili per dopo. [Fonti e licenza](/javascript/fonti).\n\n'
for part,name in [('1-js','Parte 1 · Il linguaggio'),('2-ui','Parte 2 · Browser e DOM'),('extra','Parte 3 · Argomenti aggiuntivi')]:
    entries=[]
    index+='## '+name+'\n\n'
    for (p,g),items in groups.items():
        if (part=='extra' and p not in {'1-js','2-ui'}) or p==part:
            label=GROUP_NAMES.get(g,g)
            entries.append({'text':label,'collapsed':True,'items':items})
            index+='### '+label+'\n\n'+'\n'.join('- ['+x['text']+']('+x['link']+')' for x in items)+'\n\n'
    sidebar.append({'text':name,'collapsed':True,'items':entries})
(PROJECT/'docs/javascript/indice.md').write_text(index)
(PROJECT/'docs/.vitepress/javascript-sidebar.json').write_text(json.dumps(sidebar,ensure_ascii=False,indent=2)+'\n')
(PROJECT/'sources/javascript-info/manifest.json').write_text(json.dumps({'articles':manifest,'article_count':len(articles),'task_count':task_count,'assets':sorted(assets),'source_revisions':{lang:subprocess.check_output(['git','-C',str(root),'rev-parse','HEAD'],text=True).strip() for root,lang in [(IT,'it'),(EN,'en')]} },ensure_ascii=False,indent=2)+'\n')
for root,lang in [(IT,'it'),(EN,'en')]:
    shutil.copy2(root/'LICENSE.md',PROJECT/f'sources/javascript-info/LICENSE-{lang}.md')
    shutil.copy2(root/'LICENSE.md',ASSETS/f'LICENSE-{lang}.txt')
print(json.dumps({'articles':len(articles),'tasks':task_count,'assets':len(assets),'translations':sum(a['new_translation'] for a in articles)},ensure_ascii=False))
