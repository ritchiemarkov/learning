# JavaScript: il corso di JavaScript.info

Per questa tappa usiamo **The Modern JavaScript Tutorial di Ilya Kantor**, in italiano. Trovi qui [tutti i 175 capitoli](/javascript/indice), con le tre parti del tutorial e gli esercizi in fondo agli articoli.

Il testo arriva dall'[edizione italiana](https://it.javascript.info/). Abbiamo aggiunto traduzioni e adattamenti per i quattro capitoli che mancavano o erano ancora in inglese. [Fonti, modifiche e licenza](/javascript/fonti).

**Prerequisiti:** aver costruito una pagina con HTML e CSS. Per il primo giro segui il percorso di base sotto; gli argomenti avanzati rimangono nell'indice completo per quando serviranno.

## Come usare gli esempi

Gli esempi sono mostrati come codice da copiare nella console, in un file JavaScript o in un documento HTML, secondo la lezione. Gli esercizi hanno soluzioni espandibili: prova il compito prima di aprirle.

I pulsanti Play, le sandbox e alcune dimostrazioni del sito originale usano il suo ambiente di esecuzione. Qui trovi i collegamenti per aprirli nella fonte; il codice delle lezioni non viene eseguito automaticamente dentro la documentazione.

## Primo giro: le basi del linguaggio

Segui in ordine le sezioni **Introduzione** e **Fondamenti** della prima parte:

1. [Introduzione a JavaScript](/javascript/tutorial/intro): che cosa fa il linguaggio e dove viene eseguito.
2. [Console del browser](/javascript/tutorial/devtools): dove provare il codice e leggere gli errori.
3. [Hello, world!](/javascript/tutorial/hello-world): inserire uno script nella pagina.
4. [Struttura del codice](/javascript/tutorial/structure) e [modalità rigorosa](/javascript/tutorial/strict-mode).
5. [Variabili](/javascript/tutorial/variables), [tipi di dato](/javascript/tutorial/types) e [conversioni](/javascript/tutorial/type-conversions).
6. [Operatori](/javascript/tutorial/operators), [confronti](/javascript/tutorial/comparison), [condizioni](/javascript/tutorial/ifelse) e [operatori logici](/javascript/tutorial/logical-operators).
7. [Cicli](/javascript/tutorial/while-for), [switch](/javascript/tutorial/switch) e [funzioni](/javascript/tutorial/function-basics).
8. [Function expression](/javascript/tutorial/function-expressions) e [arrow function](/javascript/tutorial/arrow-functions-basics).

Completa gli esercizi di ogni articolo. Usa [il riepilogo dei fondamenti](/javascript/tutorial/javascript-specials) per verificare ciò che ricordi.

## Secondo giro: dati, qualità e asincronia

- [Debugging nel browser](/javascript/tutorial/debugging-chrome), stile del codice e commenti.
- [Oggetti](/javascript/tutorial/object), [riferimenti e copie](/javascript/tutorial/object-copy), metodi e `this`.
- [Stringhe](/javascript/tutorial/string), [array](/javascript/tutorial/array) e [metodi degli array](/javascript/tutorial/array-methods).
- [Destructuring](/javascript/tutorial/destructuring-assignment), [JSON](/javascript/tutorial/json) e [rest/spread](/javascript/tutorial/rest-parameters-spread).
- [Scope e closure](/javascript/tutorial/closure).
- [Gestione degli errori](/javascript/tutorial/try-catch).
- [Promise](/javascript/tutorial/promise-basics) e [async/await](/javascript/tutorial/async-await).
- [Moduli](/javascript/tutorial/modules-intro), import ed export.

Prototipi e classi meritano un passaggio successivo. Descrittori, generatori, Proxy, WeakRef e i dettagli interni di Unicode sono approfondimenti: puoi consultarli dall'indice senza farli diventare un ostacolo al primo progetto.

## Terzo giro: il browser

Nella seconda parte studiamo come il codice interagisce con la pagina:

1. [Ambiente del browser](/javascript/tutorial/browser-environment) e [albero DOM](/javascript/tutorial/dom-nodes).
2. Ricerca degli elementi, proprietà dei nodi e [modifica del documento](/javascript/tutorial/modifying-document).
3. [Stili e classi](/javascript/tutorial/styles-and-classes).
4. [Eventi](/javascript/tutorial/introduction-browser-events), [propagazione](/javascript/tutorial/bubbling-and-capturing) e [delegazione](/javascript/tutorial/event-delegation).
5. [Form e controlli](/javascript/tutorial/form-elements), eventi degli input e invio dei form.

Dalla terza parte prendiamo subito [fetch](/javascript/tutorial/fetch) e [localStorage](/javascript/tutorial/localstorage). Approfondiremo HTTP e le API nella tappa backend.

## Il nostro progetto

Costruiremo una lista delle attività di studio con:

- aggiunta di un'attività tramite un form;
- completamento e rimozione delle attività;
- aggiornamento del DOM e gestione degli eventi;
- salvataggio nel browser con `localStorage`;
- una piccola richiesta asincrona con stati di caricamento ed errore.

Questo laboratorio sarà una nostra applicazione delle lezioni, distinta dal testo originale del tutorial. Il salvataggio locale vale per quel browser: più avanti useremo backend e database per condividere i dati fra dispositivi.

## Quando passare a TypeScript

Saprai completare il progetto, spiegare funzioni, array, oggetti ed eventi e gestire un'operazione asincrona. Non occorre finire ogni approfondimento prima di andare avanti.

La prossima tappa sarà [TypeScript](/typescript/), poi [HTTP e Node.js](/backend/). [Torna alla roadmap](/percorso).
