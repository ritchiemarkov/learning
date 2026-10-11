# Backend: HTTP, Node.js e TypeScript

**Prerequisiti:** basi JavaScript e [progetto TypeScript](/typescript/). Le lezioni sono da scrivere; partiremo dalla comunicazione tra browser e server prima di aggiungere un database.

Il backend riceve richieste, controlla i dati, applica le regole e restituisce risposte. L'interfaccia può controllare un form per aiutare l'utente, ma il server deve verificare di nuovo ciò che riceve.

## HTTP e API

Studieremo:

1. URL, percorso, query string, header e corpo della richiesta.
2. Richiesta e risposta: il browser come client.
3. Metodi `GET`, `POST`, `PATCH` e `DELETE`.
4. Status code comuni: successo, input non valido, accesso negato e risorsa assente.
5. JSON: formato dei dati, distinto dagli oggetti JavaScript.
6. `fetch`, `async`/`await`, errori di rete e risposte HTTP non riuscite.
7. Origini e CORS quando frontend e API sono su indirizzi diversi.

**Primo esercizio previsto:** leggere dati da una API di esercizio e mostrare caricamento, risultato, stato vuoto ed errore nell'interfaccia.

## Node.js e TypeScript

Node.js è un ambiente che esegue JavaScript sul server. Useremo TypeScript per descrivere i dati del nostro programma.

Studieremo:

1. Avvio di un programma, npm, moduli e variabili d'ambiente.
2. Un server HTTP essenziale per capire il percorso di una richiesta.
3. Rotte, parametri, corpo JSON e validazione a runtime.
4. Organizzazione in funzioni e moduli con responsabilità chiare.
5. Gestione coerente degli errori e logging utile.
6. Un framework backend per organizzare le rotte, scelto durante la tappa.
7. Test mirati degli endpoint, compresi gli input non validi.

## La nostra prima API

| Operazione | Richiesta prevista |
| --- | --- |
| Leggere le attività | `GET /api/tasks` |
| Creare un'attività | `POST /api/tasks` |
| Modificare un'attività | `PATCH /api/tasks/:id` |
| Eliminare un'attività | `DELETE /api/tasks/:id` |

Inizialmente useremo dati in memoria: al riavvio si perderanno. È un passaggio didattico per capire le rotte; nella [tappa database](/database/) aggiungeremo la persistenza.

## Quando passare a SQL

Sai descrivere una richiesta e una risposta, implementare le quattro operazioni, distinguere errori di rete ed errori HTTP e rifiutare input non validi sul server.

Autenticazione, autorizzazione e protezione dei dati arriveranno nella [prima applicazione completa](/fullstack/), prima di pubblicare una API con utenti reali.

Riferimento: [Introduzione a Node.js](https://nodejs.org/en/learn/getting-started/introduction-to-nodejs). [Torna alla roadmap](/percorso).
