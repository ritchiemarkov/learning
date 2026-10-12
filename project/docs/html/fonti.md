# Fonti HTML e metodo della ricerca

**Ricerca: 12 ottobre 2026.** Abbiamo confrontato le sette lezioni iniziali con quattro tipi di fonti ufficiali, perché un corso e una specifica rispondono a domande diverse.

| Fonte | Perché la usiamo | Come entra nel sito |
| --- | --- | --- |
| [WHATWG · HTML Living Standard](https://html.spec.whatwg.org/multipage/) | Regole normative, modelli di contenuto, sintassi e comportamenti | Baseline dell'inventario e riferimenti dei casi limite |
| [WHATWG · Indici](https://html.spec.whatwg.org/multipage/indices.html) | Elementi conformi, attributi e gestori di eventi | Snapshot con 113 elementi, 144 nomi/180 contesti e 89 handler |
| [MDN · Elementi](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements) e [globali](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes) | Esempi, spiegazioni e compatibilità per sviluppatori | Confronto delle categorie e distinzione di funzioni recenti |
| [Google/web.dev · Learn HTML](https://web.dev/learn/html) | Percorso didattico dall'inizio agli argomenti avanzati | Mappa dei 20 moduli nella pagina di copertura |
| [WAI · Struttura](https://www.w3.org/WAI/tutorials/page-structure/), [form](https://www.w3.org/WAI/tutorials/forms/), [tabelle](https://www.w3.org/WAI/tutorials/tables/), [immagini](https://www.w3.org/WAI/tutorials/images/decision-tree/) e [media](https://www.w3.org/WAI/media/av/) | Come rendere strutture e contenuti utilizzabili | Criteri manuali, alternative, nomi e associazioni |
| [W3C · Internazionalizzazione](https://www.w3.org/International/questions/qa-html-language-declarations) | Lingue, codifica e testo bidirezionale | Lezione dedicata e prove sui frammenti multilingue |
| [Google Search Central · Dati strutturati](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data) | Interpretazione dei metadati da parte di un consumatore concreto | Confini fra HTML, Schema.org, JSON-LD e risultati di ricerca |

## Come abbiamo costruito il catalogo

L'indice WHATWG consultato riportava «Last Updated 9 October 2026». Abbiamo estratto nomi, URL delle definizioni, attributi specifici e grammatiche dei valori, separando i sei livelli `h1`–`h6`. Le radici SVG/MathML e la famiglia dei custom elements hanno voci separate.

Nel repository `project/sources/html/inventory.json` registra fonte, data e SHA-256 della pagina consultata. `curation.json` contiene descrizioni italiane e collegamenti didattici. Il generatore offline `project/scripts/build-html-reference.py` verifica che ogni voce della fonte abbia una descrizione e una lezione esistente. La build VitePress verifica anche i collegamenti interni.

Un inventario completo non dimostra che ogni condizione della specifica sia riscritta nel corso: per vincoli dettagliati ogni voce rimanda alla definizione originale. Le lezioni aggiunte sono spiegazioni ed esempi scritti per Learning, non traduzioni integrali di MDN o Google. Le fonti precise sono riportate in fondo a ogni lezione.

## Documentazione da tenere vicina

Consulta il [riferimento degli elementi](/html/riferimento-elementi) per il significato, il [riferimento degli attributi](/html/riferimento-attributi) per contesti e valori e la [pagina di copertura](/html/copertura) per capire cosa è misurato. Per un documento completo usa [Nu HTML Checker](https://validator.w3.org/nu/), integrandolo con le [prove WAI](https://www.w3.org/WAI/test-evaluate/preliminary/).
