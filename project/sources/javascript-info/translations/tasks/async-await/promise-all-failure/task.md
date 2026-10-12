# Promise.all e operazioni ancora in corso

`Promise.all` è utile per avviare operazioni indipendenti in parallelo, ma il suo rifiuto non cancella le altre operazioni.

Immagina una connessione a un servizio remoto:

```js
let database;

function connect() {
  database = {
    async query(isOk) {
      if (!isOk) throw new Error('Query failed');
    }
  };
}

function disconnect() {
  database = null;
}

function delay(fn, ms) {
  return new Promise((resolve, reject) => {
    setTimeout(() => fn().then(resolve, reject), ms);
  });
}

async function run() {
  connect();
  try {
    await Promise.all([
      delay(() => database.query(true), 100),
      delay(() => database.query(false), 200),
      delay(() => database.query(false), 300)
    ]);
  } catch (error) {
    console.log('Error handled (or was it?)');
  }
  disconnect();
}

run();
```

La seconda operazione fallisce e il `catch` interviene. Tuttavia il codice può produrre un altro errore non gestito.

Spiega perché la terza operazione è ancora programmata, che cosa succede dopo `disconnect()` e come mantenere la connessione fino al completamento di tutte le operazioni.
