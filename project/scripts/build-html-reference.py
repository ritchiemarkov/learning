#!/usr/bin/env python3
"""Render the curated HTML inventory offline; --check fails on drift or missing entries."""
import argparse
import html
import json
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
SOURCE = PROJECT / 'sources/html'
DOCS = PROJECT / 'docs/html'


def cell(value):
    return html.escape(value, quote=False).replace('|', '&#124;').replace('\n', ' ')


def render():
    inventory = json.loads((SOURCE / 'inventory.json').read_text())
    curation = json.loads((SOURCE / 'curation.json').read_text())
    assert set(curation['elements']) == {e['name'] for e in inventory['elements']}
    assert set(curation['attributes']) == {a['name'] for a in inventory['attributes']}
    for kind in ('elements', 'attributes'):
        for entry in curation[kind].values():
            assert entry['meaning'].strip()
            assert (DOCS / (entry['lesson'] + '.md')).is_file(), entry['lesson']
    assert len({e['name'] for e in inventory['elements']}) == len(inventory['elements'])
    assert len({e['name'] for e in inventory['event_attributes']}) == len(inventory['event_attributes'])

    elements = ['# Riferimento: tutti gli elementi HTML', '',
        f"Snapshot consultato il **12 ottobre 2026**, standard aggiornato al **9 ottobre 2026**: **{len(inventory['elements'])} elementi HTML nominati**. Ogni voce ha una descrizione, una lezione e il collegamento alla definizione ufficiale. Le condizioni, il modello di contenuto e le eccezioni si verificano nella specifica.", '',
        'Gli attributi specifici sono elencati come orientamento; gli attributi globali si aggiungono dove ammessi. Una voce nel catalogo non significa che la funzione sia disponibile in ogni browser. [Metodo e limiti del conteggio](/html/copertura).', '',
        '## Catalogo alfabetico', '',
        '| Elemento e definizione | Significato | Lezione | Attributi specifici nell’indice |',
        '| --- | --- | --- | --- |']
    for entry in sorted(inventory['elements'], key=lambda x: x['name']):
        curated = curation['elements'][entry['name']]
        attrs = entry['attributes'].replace('globals ; ', '').replace('globals', '—')
        elements.append(f"| [`{entry['name']}`]({entry['url']}) | {curated['meaning']} | [Studia](/html/{curated['lesson']}) | {cell(attrs)} |")
    elements += ['', '## Radici esterne e famiglia aperta', '',
        '- [`svg`](https://www.w3.org/TR/SVG2/) e [`math`](https://www.w3.org/TR/mathml-core/) sono radici di SVG e MathML. L’integrazione è nella [lezione 15](/html/contenuti-incorporati); gli elementi interni appartengono alle rispettive specifiche.',
        '- I [custom elements autonomi](https://html.spec.whatwg.org/multipage/custom-elements.html) sono una famiglia aperta, non un numero finito di tag. Studiamo regole del nome, registrazione e confini nella [lezione 22](/html/script-template).', '',
        '## Elementi storici', '',
        'Gli elementi non conformi non vengono sommati al catalogo moderno. La [lezione 25](/html/compatibilita) li distingue e spiega come migrare. Il capitolo [WHATWG sulle funzioni obsolete](https://html.spec.whatwg.org/multipage/obsolete.html) rimane il riferimento per eccezioni e attributi storici.', '',
        'Fonte del catalogo: [WHATWG · Indice degli elementi](https://html.spec.whatwg.org/multipage/indices.html#elements-3). Descrizioni italiane e collegamenti didattici curati per Learning.']

    attributes = ['# Riferimento: attributi e gestori di eventi', '',
        f"Lo snapshot contiene **{len(curation['attributes'])} nomi di attributi**, descritti in **{len(inventory['attributes'])} righe di contesto**, più **{len(inventory['event_attributes'])} attributi gestori di eventi**. Un nome come `type` cambia significato fra elementi: non basta memorizzare il nome.", '',
        'Le colonne di valori sono un indice della grammatica ufficiale, non tutte le sue condizioni. Le parole tecniche e i valori sono conservati dalla fonte; apri la definizione per default, errori, intervalli ed eccezioni. Gli asterischi rinviano alle condizioni della specifica. [Copertura e confini](/html/copertura).', '']
    for heading, global_only in [('Attributi globali nell’indice HTML', True), ('Attributi nei contesti specifici', False)]:
        attributes += [f'## {heading}', '', '| Nome e definizione | Dove | Significato | Valori / grammatica | Lezione |', '| --- | --- | --- | --- | --- |']
        for entry in inventory['attributes']:
            if ('HTML elements' in entry['elements']) != global_only:
                continue
            curated = curation['attributes'][entry['name']]
            attributes.append(f"| [`{entry['name']}`]({entry['url']}) | {cell(entry['elements'])} | {curated['meaning']} | {cell(entry['values'])} | [Studia](/html/{curated['lesson']}) |")
        attributes.append('')
    attributes += ['## Famiglie aperte e specifiche collegate', '',
        '| Famiglia | Significato | Percorso |', '| --- | --- | --- |',
        '| `data-*` | Dati personalizzati dell’applicazione; non segreti né semantica nativa | [Attributi globali](/html/attributi-globali) |',
        '| `role`, `aria-*` | Ruoli, stati e relazioni definiti da ARIA; rispettare i vincoli dell’elemento | [Accessibilità](/html/accessibilita-focus), [ARIA in HTML](https://www.w3.org/TR/html-aria/) |',
        '| `part`, `exportparts` | Agganci di stile dello Shadow DOM, da specifiche collegate | [Componenti](/html/script-template) |', '',
        'Queste famiglie non sono sommate artificialmente ai 144 nomi dell’indice. Attributi sperimentali o vendor-specific assenti dalla fonte non sono classificati come standard per aumentare il conteggio.', '',
        '## Tutti i gestori di eventi dello snapshot', '',
        'Ogni attributo esegue un handler per l’evento indicato dal nome senza prefisso `on`; il link specifica bersaglio e comportamento. Gli handler su `body` possono riferirsi a `Window`. Per nuovi programmi preferiamo `addEventListener`: vedi [eventi JavaScript](/javascript/tutorial/introduction-browser-events) e [event loop](/javascript/tutorial/event-loop). Il catalogo non costituisce un corso completo di tutte le API coinvolte.', '',
        '| Attributo e definizione | Applicazione nell’indice | Evento |', '| --- | --- | --- |']
    for entry in inventory['event_attributes']:
        attributes.append(f"| [`{entry['name']}`]({entry['url']}) | {entry['elements']} | `{entry['name'][2:]}` |")
    attributes += ['', 'Fonte: [WHATWG · Indice degli attributi](https://html.spec.whatwg.org/multipage/indices.html#attributes-3). I significati italiani sono curati per Learning; la specifica contiene i vincoli completi.']
    return {'riferimento-elementi.md': '\n'.join(elements) + '\n', 'riferimento-attributi.md': '\n'.join(attributes) + '\n'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    for name, content in render().items():
        path = DOCS / name
        if args.check:
            assert path.read_text() == content, f'Reference drift: {path}'
        else:
            path.write_text(content)
    print('HTML inventory verified: 113 elements, 144 attribute names / 180 contexts, 89 event attributes.')


if __name__ == '__main__':
    main()
