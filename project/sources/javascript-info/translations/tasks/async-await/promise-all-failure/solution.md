`Promise.all` rifiuta la Promise risultante al primo rifiuto e **non cancella gli altri lavori**. Tuttavia installa gestori sulle Promise di ingresso: un loro successivo rifiuto non è automaticamente un rifiuto non gestito.

Nel frammento dell'esercizio l'errore aggiuntivo ha una causa più precisa. Dopo 200 ms il `catch` termina e `disconnect()` imposta `database = null`. Dopo 300 ms la callback del timer prova a valutare `database.query(false)`: questo genera un errore sincrono dentro il timer. La funzione `delay` non lo intercetta, quindi non lo inoltra alla Promise che aveva creato.

Occorre risolvere entrambi i problemi: trasformare anche gli errori sincroni in rifiuti e aspettare che tutti i lavori siano conclusi prima di chiudere la connessione.

```js
function delay(fn, ms) {
  return new Promise(resolve => setTimeout(resolve, ms)).then(fn);
}

async function run() {
  connect();
  try {
    const results = await Promise.allSettled([
      delay(() => database.query(true), 100),
      delay(() => database.query(false), 200),
      delay(() => database.query(false), 300)
    ]);

    const errors = results
      .filter(result => result.status === 'rejected')
      .map(result => result.reason);

    if (errors.length) {
      throw new AggregateError(errors, 'One or more queries failed');
    }
  } catch (error) {
    console.error('Error handled', error);
  } finally {
    disconnect();
  }
}
```

`then(fn)` cattura sia un'eccezione sincrona di `fn` sia il rifiuto di una Promise restituita. `allSettled` aspetta tutte le operazioni; `finally` chiude la connessione quando non sono più in corso.

La soluzione ideale può includere la cancellazione delle richieste ancora pendenti, se il servizio la supporta. Una cancellazione va coordinata con il loro completamento: smettere di aspettare non significa aver fermato il lavoro.

Se vuoi conservare il risultato di ogni operazione e sollevare tutti gli errori insieme, puoi riutilizzare questa funzione:

```js
async function allOrAggregateError(promises) {
  const results = await Promise.allSettled(promises);
  const errors = results
    .filter(result => result.status === 'rejected')
    .map(result => result.reason);

  if (errors.length) {
    throw new AggregateError(errors, 'One or more promises failed');
  }

  return results.map(result => result.value);
}
```

Questo è un adattamento della soluzione originale: chiarisce la differenza fra rifiuto, eccezione nel timer e cancellazione, e usa `Promise.allSettled` per attendere tutti i lavori.
