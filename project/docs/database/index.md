# Database: SQL e PostgreSQL

**Prerequisito:** la [API Node.js](/backend/) funziona con dati in memoria. Le lezioni sono da scrivere; qui definiamo ciò che servirà per conservare i dati davvero.

SQL è il linguaggio con cui lavoreremo sui dati relazionali. PostgreSQL è il sistema di database che eseguirà le query. Partiremo dal funzionamento delle tabelle e dalle query scritte direttamente.

## Cosa impareremo

1. Tabelle, righe, colonne e tipi dei dati.
2. Chiavi primarie, chiavi esterne e relazioni.
3. `SELECT`, `INSERT`, `UPDATE` e `DELETE`.
4. Filtri, ordinamento e `JOIN`.
5. Vincoli: dati obbligatori, unicità e coerenza dei riferimenti.
6. Query parametrizzate per separare input e istruzioni SQL.
7. Migrazioni: modificare lo schema in modo ripetibile.
8. Transazioni e indici di base, quando un'operazione ne ha bisogno.

## Progetto previsto

Sostituiremo l'array in memoria della API con una tabella delle attività. Poi modelleremo gli utenti e il collegamento fra un'attività e il suo proprietario.

Il browser continuerà a usare la API: le credenziali del database appartengono al backend. Il controllo dell'accesso ai dati sarà applicato dal server, non solo dai filtri dell'interfaccia.

## Verifica della tappa

Crea un'attività, riavvia il backend e verifica che esista ancora. Spiega le chiavi della tabella e scrivi una query che legga soltanto le attività di un utente. Verifica anche che un dato non valido venga rifiutato dai vincoli previsti.

Dopo SQL potremo valutare un ORM, uno strumento che aiuta a lavorare con il database dal codice: conoscere le query rimane utile per capire ciò che fa.

Prossima tappa: [applicazione completa](/fullstack/). Riferimento: [Tutorial PostgreSQL](https://www.postgresql.org/docs/current/tutorial.html).
