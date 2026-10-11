# La prima applicazione completa

**Prerequisiti:** frontend in JavaScript/TypeScript, API Node.js e basi SQL. Le lezioni sono da scrivere; questa è la destinazione del primo percorso frontend e backend.

Il progetto sarà una **lista di attività di studio** con interfaccia nel browser, API sul server e dati persistenti. Una base full stack significa saper spiegare e collegare questi livelli.

## Cosa aggiungeremo

1. Collegamento del frontend alla API, con stati di caricamento, errore e lista vuota.
2. Contratto dei dati e validazione sul server.
3. Autenticazione: riconoscere l'utente tramite un meccanismo consolidato.
4. Autorizzazione: ogni utente può leggere e modificare solo le proprie attività.
5. Sessioni, cookie e protezioni appropriate al modello di autenticazione scelto.
6. Gestione dei segreti, degli errori e dei dati sensibili.
7. Test mirati della logica, degli endpoint e di un flusso completo.
8. Deploy di frontend, backend e database, con configurazione degli ambienti e backup dei dati.

## Come sapremo che funziona

- Un utente crea, modifica e completa un'attività dalla pagina.
- Dopo aver ricaricato la pagina e riavviato il backend, i dati rimangono.
- Un secondo utente non può leggere o modificare le attività del primo, anche chiamando direttamente la API.
- Input non valido e risorse inesistenti producono risposte comprensibili.
- Un problema di rete viene mostrato senza far credere all'utente che il salvataggio sia riuscito.

## Gli strumenti lungo il percorso

Git e terminale si praticano dall'inizio. Usiamo gli strumenti del browser per ispezionare HTML, CSS, console e richieste di rete. In questa tappa colleghiamo le verifiche del browser a quelle del server e del database.

Il sito delle lezioni è già online su Cloudflare Pages. L'hosting della futura applicazione con backend e database sarà una scelta separata: valuteremo soluzioni e limiti gratuiti quando avremo qualcosa da pubblicare.

## E poi?

Dopo aver costruito il flusso completo, useremo [un framework frontend](/frontend/) per organizzare l'interfaccia in componenti. In seguito passeremo a [Rust](/rust/).

[Torna alla roadmap](/percorso).
