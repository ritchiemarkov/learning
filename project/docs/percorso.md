# Roadmap: dal frontend al backend

Il nostro obiettivo è saper costruire una piccola applicazione web completa: un'interfaccia nel browser, un server che gestisce le richieste e un database che conserva i dati. **Partiamo con HTML, CSS e JavaScript; aggiungiamo TypeScript, poi il backend. Rust viene dopo questa base.**

Questa è una proposta di percorso: le tappe si adattano a ciò che impari, senza scadenze fisse. Sono disponibili le sette lezioni HTML e il [corso JavaScript.info in italiano](/javascript/), con 175 capitoli. CSS e le altre sezioni descrivono gli obiettivi e i progetti delle lezioni da scrivere.

## Frontend, backend e database

| Parte | Dove lavora | Responsabilità nel nostro progetto |
| --- | --- | --- |
| Frontend | Nel browser | Mostra le attività, raccoglie input, comunica con il server |
| Backend | Sul server | Valida i dati, applica le regole, controlla chi può accedere |
| Database | Gestito dal backend | Conserva attività e utenti, anche dopo un riavvio |

Una **API** è il punto di contatto: il browser invia una richiesta HTTP e il backend restituisce una risposta, spesso con dati JSON. Il frontend non si collega direttamente al database.

## L'ordine delle tappe

| Tappa | Cosa impariamo | Cosa costruiamo |
| --- | --- | --- |
| 1 · [HTML](/html/) | Struttura, semantica, link, immagini, form e accessibilità | Pagina personale completa |
| 2 · [CSS](/css/) | Cascata, box model, tipografia, Flexbox, Grid e responsive design | Stile della pagina, da telefono a desktop |
| 3 · [JavaScript](/javascript/) | Tipi, funzioni, array, oggetti, DOM, eventi, moduli e asincronia | Lista di attività con salvataggio locale |
| 4 · [TypeScript](/typescript/) | Tipi statici, inferenza, union, narrowing e tipi dei dati | Migrazione della lista a TypeScript |
| 5 · [HTTP e API](/backend/#http-e-api) | Richieste, risposte, metodi, status code e JSON | Lettura di dati da una API di esercizio |
| 6 · [Backend con Node.js](/backend/#node-js-e-typescript) | Server, rotte, validazione, errori e configurazione | API per creare, leggere, modificare ed eliminare attività |
| 7 · [SQL e PostgreSQL](/database/) | Tabelle, relazioni, query, vincoli e migrazioni | Salvataggio delle attività in un database |
| 8 · [Prima applicazione completa](/fullstack/) | Integrazione, autenticazione, autorizzazione, test e deploy | Lista di attività per utenti diversi |
| 9 · [Un framework frontend](/frontend/) | Componenti, stato, routing e gestione dei dati | Riorganizzazione dell'interfaccia con React oppure Vue |
| 10 · [Rust](/rust/) | Tipi, ownership, borrowing, errori e Cargo | Programma da terminale; poi, se utile, una piccola API |

Git, terminale, strumenti del browser e lettura degli errori ci accompagnano dall'inizio. Accessibilità, debugging e verifica del comportamento fanno parte di ogni progetto.

## Perché TypeScript dopo JavaScript?

TypeScript aggiunge un controllo statico dei tipi a JavaScript. Aiuta a individuare errori mentre scrivi, ma per usarlo bene devi capire come funziona il programma JavaScript: funzioni, oggetti, eventi e operazioni asincrone.

Prima costruiamo una piccola applicazione in JavaScript, poi la trasformiamo in TypeScript. Vedrai così quale problema risolve ogni tipo. Non serve padroneggiare tutto JavaScript prima di iniziare: basta saper completare il progetto della terza tappa.

I tipi non verificano da soli i dati ricevuti dalla rete. La validazione dei dati a runtime rimane necessaria, soprattutto nel backend.

## Perché Node.js come primo backend?

Node.js permette di usare JavaScript sul server. Continuando con JavaScript e TypeScript, possiamo concentrarci su HTTP, validazione, dati e sicurezza senza imparare contemporaneamente un nuovo linguaggio.

Partiremo con un piccolo server e pochi endpoint. Poi useremo un framework backend, scelto durante la tappa, per organizzare le rotte. SQL si studia direttamente prima di aggiungere strumenti che generano query al nostro posto.

Rust rimane nel percorso: lo affrontiamo dopo aver capito che cosa fa un backend e aver completato un'applicazione con dati persistenti.

## Un progetto che cresce

1. **HTML:** ci presentiamo con una pagina strutturata.
2. **CSS:** rendiamo la pagina leggibile e adattabile agli schermi.
3. **JavaScript:** aggiungiamo una lista delle attività di studio, salvata nel browser.
4. **TypeScript:** descriviamo il modello delle attività e controlliamo i tipi.
5. **Backend e database:** spostiamo la gestione dei dati sul server e li conserviamo in PostgreSQL.
6. **Applicazione completa:** ogni utente vede e modifica le proprie attività; verifichiamo i flussi e pubblichiamo.
7. **Framework:** riorganizziamo un'interfaccia che già comprendiamo in componenti.
8. **Rust:** riprendiamo lo stesso problema con un programma da terminale e confrontiamo gli approcci.

## Quando passare alla tappa successiva

| Dopo | Dovresti riuscire a… |
| --- | --- |
| HTML | Scrivere un documento completo, collegare pagine e dare etichette ai controlli |
| CSS | Creare un layout leggibile su schermi diversi e spiegare spazi, cascata e focus |
| JavaScript | Gestire eventi, modificare il DOM, usare array e oggetti, salvare dati e spiegare `async`/`await` |
| TypeScript | Modellare un'attività, restringere una union e correggere errori di tipo senza ricorrere sistematicamente ad `any` |
| HTTP e Node.js | Spiegare una richiesta, implementare le operazioni sui dati e rifiutare input non validi |
| SQL | Scrivere query parametrizzate e spiegare chiavi, relazioni e vincoli |
| Applicazione completa | Collegare i livelli, controllare l'accesso ai dati e verificare un flusso completo |

Questi sono punti di controllo, non esami. Se un punto è incerto, facciamo un esercizio mirato prima di aggiungere complessità.

## Come studiamo

Per JavaScript seguiamo [JavaScript.info](/javascript/): prima linguaggio e browser, poi gli approfondimenti dell'[indice completo](/javascript/indice). La fonte è il tutorial di Ilya Kantor con la traduzione italiana della comunità; trovi [attribuzione e licenza](/javascript/fonti) nella sezione dedicata. Il nostro progetto applica queste lezioni a una lista di attività.

Ogni lezione seguirà questo formato:

1. **Obiettivo:** una capacità concreta da acquisire.
2. **Spiegazione:** un concetto alla volta, con parole semplici.
3. **Esempio:** codice breve da eseguire e modificare.
4. **Esercizio:** un compito da provare prima di aprire la soluzione.
5. **Verifica:** risultato atteso, errori comuni e una domanda da spiegare a parole tue.

Sessioni di 20–30 minuti sono un buon punto di partenza. Conta la capacità di costruire e spiegare ciò che hai fatto, più del numero di lezioni lette.

## Il nostro punto di partenza: HTML

Per HTML servono un editor, un browser e una cartella `esercizi`. Puoi aprire i file `.html` direttamente nel browser. Node.js serve per avviare questo sito VitePress, ma non per i primi esercizi.

Le sette lezioni coprono documento, sintassi, testo, liste, link, immagini, semantica e form. Nel [progetto finale](/html/progetto) riunisci le basi. Tabelle per dati, audio/video e metadati più approfonditi potranno diventare esercizi successivi, quando il progetto ne avrà bisogno.

::: tip Inizia qui
Apri [La prima pagina](/html/prima-pagina). Per adesso il nostro compito è costruire e capire una pagina HTML completa.
:::

## Strumenti e pubblicazione

Le lezioni sono file Markdown in `project/docs`. La documentazione è già pubblicata con GitHub e Cloudflare Pages. Pubblicare in futuro un backend con database sarà un passaggio separato: scegliere l'hosting non serve ancora per questi esercizi.

Per avviare il sito in locale dalla cartella del repository:

```bash
cd project
npm ci
npm run docs:dev
```

Per verificare la versione pubblicabile:

```bash
npm run docs:build
npm run docs:preview
```

La configurazione del deploy è nel `README.md` del repository.

## Riferimenti per il percorso

- [MDN Curriculum](https://developer.mozilla.org/en-US/curriculum/): fondamentali frontend.
- [TypeScript: guida per chi inizia](https://www.typescriptlang.org/docs/handbook/typescript-from-scratch.html): rapporto fra JavaScript e TypeScript.
- [Introduzione a Node.js](https://nodejs.org/en/learn/getting-started/introduction-to-nodejs): JavaScript sul server.
- [Tutorial PostgreSQL](https://www.postgresql.org/docs/current/tutorial.html): introduzione ai database relazionali e a SQL.
