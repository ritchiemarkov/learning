# Copertura HTML: cosa significa il 100%

**Prima dell'audit avevamo sette lezioni introduttive. Non coprivano tutto HTML.** Il confronto con WHATWG, MDN, Google/web.dev e WAI ha portato a 26 lezioni, un catalogo di elementi e attributi e una rubrica di prove pratiche.

Ricerca e inventario consultati il **12 ottobre 2026**; la fonte WHATWG riportava **9 ottobre 2026** come ultimo aggiornamento. HTML è un Living Standard: il conteggio è riferito a questo snapshot, non una promessa su ogni futura modifica.

## Il perimetro misurabile

| Inventario | Voci documentate / voci dello snapshot | Cosa è verificato |
| --- | --- | --- |
| Elementi HTML nominati conformi | **113 / 113 · 100%** | Descrizione italiana, lezione collegata e definizione ufficiale |
| Nomi degli attributi nell'indice | **144 / 144 · 100%** | Significato, contesti, grammatica dei valori e definizione |
| Righe attributo–contesto dell'indice | **180 / 180 · 100%** | Anche i nomi riutilizzati con significati diversi |
| Attributi gestori di eventi | **89 / 89 · 100%** | Evento e contesto, con rinvio alla specifica e al corso JS |
| Radici SVG/MathML e custom elements | **3 / 3 voci di integrazione** | Due radici esterne e una famiglia aperta, non tutti i loro possibili elementi |

Apri [tutti gli elementi](/html/riferimento-elementi) o [attributi ed eventi](/html/riferimento-attributi). Il controllo del repository verifica corrispondenza dell'inventario, descrizioni non vuote, lezioni esistenti e pagine generate senza divergenze. **Misura la completezza del catalogo, non la profondità uniforme di ogni argomento né le competenze di chi legge.**

## Audit delle aree didattiche

| Area | Prima: sette lezioni | Ora: dove studiarla |
| --- | --- | --- |
| Documento, sintassi, testo e liste | Basi presenti | Basi + [sintassi e DOM](/html/sintassi-dom), [testo](/html/testo-avanzato) |
| Metadati e caricamento | Charset, title, viewport | [Head completo](/html/metadati), [risorse](/html/sicurezza-prestazioni) |
| Struttura e navigazione | Regioni principali | [Liste, sezioni, ricerca e link](/html/navigazione) |
| Tabelle | Assenti | [Tabelle e associazioni](/html/tabelle) |
| Immagini | Src, alt, dimensioni | [Responsive, picture e mappe](/html/immagini-responsive) |
| Audio e video | Assenti | [Media, tracce e alternative](/html/audio-video) |
| Iframe, object, embed e grafica | Assenti | [Contenuti incorporati](/html/contenuti-incorporati) |
| Form | Input text/email, checkbox/radio, textarea | [22 tipi e tutti i controlli](/html/controlli-form), [invio e vincoli](/html/invio-validazione) |
| Attributi globali | Id/class e alcuni esempi | [Globali, famiglie e API](/html/attributi-globali) |
| Accessibilità | Label, alt e introduzione alla tastiera | [Nomi, focus e verifiche](/html/accessibilita-focus) |
| Interazioni native | Assenti | [Details, dialog e popover](/html/interazioni-native) |
| Lingue e bidi | Lang sulla radice | [Internazionalizzazione e ruby](/html/internazionalizzazione) |
| Script e componenti | Rinviati a JS | [Markup di script, template e slot](/html/script-template), approfondimenti JS collegati |
| Dati strutturati | Assenti | [Microdati e SEO](/html/microdati-seo) |
| Obsoleto e nuove funzioni | Assenti | [Compatibilità e migrazioni](/html/compatibilita) |
| Verifica pratica | Pagina personale | [Laboratorio e rubrica completa](/html/laboratorio-completo) |

## Confronto con Google Learn HTML

I 20 moduli didattici di [Learn HTML](https://web.dev/learn/html), esclusi benvenuto e conclusione, hanno questi punti di ingresso nel nostro corso. È una mappa degli argomenti; non è un'importazione del testo di Google.

| Modulo Google | Nel nostro percorso |
| --- | --- |
| Overview of HTML | [Introduzione](/html/) |
| Document structure | [Prima pagina](/html/prima-pagina), [Sintassi e DOM](/html/sintassi-dom) |
| Metadata | [Metadati](/html/metadati) |
| Semantic HTML | [Semantica](/html/semantica) |
| Headings and sections | [Navigazione e struttura](/html/navigazione) |
| Attributes | [Globali](/html/attributi-globali), [riferimento](/html/riferimento-attributi) |
| Text basics | [Testo e liste](/html/testo-liste) |
| Links | [Link e immagini](/html/link-immagini), [navigazione](/html/navigazione) |
| Lists | [Testo e liste](/html/testo-liste), [liste avanzate](/html/navigazione) |
| Navigation | [Navigazione](/html/navigazione) |
| Tables | [Tabelle](/html/tabelle) |
| Forms | [Form](/html/form), [controlli](/html/controlli-form), [invio](/html/invio-validazione) |
| Images | [Immagini responsive](/html/immagini-responsive) |
| Audio and Video | [Media](/html/audio-video) |
| Template, slot, and shadow | [Componenti](/html/script-template) |
| HTML APIs | [Globali](/html/attributi-globali), [componenti](/html/script-template), [corso JS](/javascript/) |
| Focus | [Accessibilità e focus](/html/accessibilita-focus) |
| Other inline text elements | [Testo avanzato](/html/testo-avanzato), [lingue](/html/internazionalizzazione) |
| Details and summary | [Interazioni native](/html/interazioni-native) |
| Dialog | [Interazioni native](/html/interazioni-native) |

## Confini del corso e onestà del dato

Lo standard HTML comprende anche algoritmi per browser, navigazione, event loop, worker, comunicazione e storage. Questi non sono tutti insegnati nelle lezioni di markup: proseguono nel [tutorial JavaScript](/javascript/indice) o rimangono riferimenti normativi per implementatori. Analogamente, ARIA, HTTP, SVG, MathML e Schema.org hanno specifiche proprie.

I contenuti obsoleti sono separati dal conteggio conforme. Gli attributi di famiglie aperte (`data-*`, `aria-*`), i vocabolari dei metadati e ogni possibile valore non hanno un inventario finito da sommare ai tag. Non dichiariamo «100% dell'intera piattaforma web» né «tutti i browser supportano tutto».

Per misurare l'apprendimento usa la [rubrica del laboratorio](/html/laboratorio-completo): ogni capacità richiede una prova. Per nuove funzioni verifica la compatibilità alla data del progetto. Per aggiornare lo snapshot va rifatto il confronto con lo standard, curando nuove voci prima di ripubblicare una percentuale.

Fonti e metodo: [bibliografia ragionata](/html/fonti).
