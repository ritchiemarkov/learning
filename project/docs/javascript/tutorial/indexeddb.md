---
title: "IndexedDB"
description: "JavaScript.info in italiano: IndexedDB"
sourceTutorial: true
prev: {"text": "LocalStorage, sessionStorage", "link": "/javascript/tutorial/localstorage"}
next: {"text": "Curve di Bezier", "link": "/javascript/tutorial/bezier-curve"}
---

# IndexedDB

> **JavaScript.info · Ilya Kantor e contributori.** [Originale inglese](https://javascript.info/indexeddb) · [Edizione italiana](https://it.javascript.info/indexeddb) · [Fonti e licenza](/javascript/fonti).

IndexedDB è un database integrato nel browser, più potente di `localStorage`:

- conserva valori strutturati associati a chiavi di diversi tipi;
- offre transazioni per raggruppare operazioni;
- permette ricerche tramite intervalli di chiavi e indici;
- può gestire più dati di `localStorage`, entro le quote del browser.

È particolarmente utile nelle applicazioni offline, anche insieme ai Service Worker. Per una semplice applicazione client-server potrebbe essere più di ciò che serve.

L'interfaccia nativa, descritta nella [specifica IndexedDB](https://www.w3.org/TR/IndexedDB/), usa eventi. Possiamo lavorare con Promise e `async`/`await` tramite una libreria come [idb](https://github.com/jakearchibald/idb). Prima capiremo l'API nativa, poi il wrapper.


::: tip Dove sono i dati?
I dati sono gestiti nel profilo del browser. Browser e profili diversi hanno memorizzazioni separate. Non è un database sul nostro server e l'utente può cancellarlo dalle impostazioni del browser.
:::

## Aprire il database

Per iniziare apriamo una connessione:

```js
let openRequest = indexedDB.open(name, version);
```

`name` è il nome del database e `version` è un intero positivo, normalmente `1` per un nuovo database. I database appartengono all'origine corrente, definita da protocollo, host e porta: un sito non accede ai database di un'altra origine.

La chiamata restituisce una richiesta da osservare tramite eventi:

- `success`: la connessione è pronta e `openRequest.result` contiene il database;
- `error`: l'apertura non è riuscita;
- `upgradeneeded`: occorre creare o aggiornare la struttura del database.

IndexedDB gestisce la **versione dello schema**. Quando pubblichiamo un'app aggiornata, ogni utente può avere un database locale con una struttura precedente. Se la versione richiesta supera quella esistente, l'evento `upgradeneeded` permette la migrazione.

Lo stesso evento arriva quando il database non esiste ancora: la sua versione precedente è considerata `0`.

```js
let openRequest = indexedDB.open("store", 1);

openRequest.onupgradeneeded = function() {
  // Il database non esiste ancora: crea la struttura necessaria.
};

openRequest.onerror = function() {
  console.error("Error", openRequest.error);
};

openRequest.onsuccess = function() {
  let db = openRequest.result;
  // Usa la connessione db.
};
```

Per una seconda versione gestiamo sia chi parte da zero sia chi aveva già la versione `1`:

```js
let openRequest = indexedDB.open("store", 2);

openRequest.onupgradeneeded = function(event) {
  let db = openRequest.result;
  switch (event.oldVersion) {
    case 0:
      // Crea la struttura della versione 1.
      // Nessun break: applica poi anche il passaggio successivo.
    case 1:
      // Aggiorna la struttura alla versione 2.
  }
};
```

Solo dopo il successo dell'aggiornamento arriva `success`. Per cancellare il database:

```js
let deleteRequest = indexedDB.deleteDatabase(name);
// Osserva deleteRequest.onsuccess, onerror e, se necessario, onblocked.
```


::: warning Non puoi aprire un database con una versione precedente a quella esistente
Se il database è alla versione `3` e il codice chiede la versione `2`, l'apertura produce un errore. Può succedere quando viene caricato codice vecchio dalla cache. Gestisci l'errore, suggerisci un aggiornamento della pagina e configura correttamente la cache dell'applicazione.
:::

### Aggiornamenti con più schede aperte

Immagina una scheda con una connessione alla versione `1`. Pubblichiamo l'app aggiornata e una seconda scheda cerca di passare alla versione `2`.

Le due schede condividono il database. Per aggiornare lo schema devono essere chiuse le vecchie connessioni. IndexedDB invia `versionchange` alle connessioni esistenti; se rimangono aperte, la nuova richiesta riceve `blocked`.

```js
let openRequest = indexedDB.open("store", 2);

openRequest.onupgradeneeded = function() {
  // Crea o aggiorna lo schema.
};
openRequest.onerror = function() {
  console.error(openRequest.error);
};

openRequest.onsuccess = function() {
  let db = openRequest.result;
  db.onversionchange = function() {
    db.close();
    alert("Database is outdated, please reload the page.");
  };
};

openRequest.onblocked = function() {
  // Un'altra scheda mantiene una connessione precedente.
  alert("Please close other tabs of this application.");
};
```

`db.onversionchange` avvisa la connessione che blocca una migrazione; `openRequest.onblocked` avvisa la nuova connessione che sta aspettando. Possiamo offrire un flusso più curato, per esempio chiedere di terminare le operazioni prima di ricaricare. L'importante è non lasciare l'applicazione bloccata senza spiegazioni.

## Object store

Un **object store** è il contenitore dei dati, analogo per alcuni aspetti a una tabella o collezione. Un database può avere uno store per gli utenti, uno per i prodotti e così via. Il nome non limita i valori agli oggetti: possono esserci anche valori primitivi.

IndexedDB usa la [clonazione strutturata](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Structured_clone_algorithm). Supporta più tipi di `JSON.stringify`, compresi molti oggetti complessi e riferimenti circolari. Funzioni e nodi DOM, invece, non sono valori clonabili per questa memorizzazione.

**Ogni record deve avere una chiave unica nello store.** Le chiavi possono essere numeri validi, stringhe, date valide, dati binari o array di chiavi valide.

![](/javascript-info/6-data-storage/03-indexeddb/indexeddb-structure.svg)

La chiave può essere fornita alla scrittura, estratta da una proprietà dell'oggetto o generata automaticamente.

```js
// Sintassi: db.createObjectStore(name, keyOptions)
db.createObjectStore('books', {keyPath: 'id'});
```

- `name` identifica lo store.
- `keyPath` indica la proprietà da usare come chiave, per esempio `id`.
- `autoIncrement: true` abilita la generazione di chiavi numeriche.

Se manca una chiave interna e non è abilitata la generazione automatica, devi fornire la chiave quando scrivi il valore.

**Creare o cancellare store e modificare gli indici richiede una transazione di aggiornamento della versione**, normalmente nel gestore `upgradeneeded`.

Puoi organizzare le migrazioni in passaggi numerati oppure esaminare gli store esistenti tramite `db.objectStoreNames.contains(name)`:

```js
let openRequest = indexedDB.open("db", 2);

openRequest.onupgradeneeded = function() {
  let db = openRequest.result;
  if (!db.objectStoreNames.contains('books')) {
    db.createObjectStore('books', {keyPath: 'id'});
  }
};
```

Per eliminare uno store durante un aggiornamento:

```js
db.deleteObjectStore('books');
```

## Transazioni

Una transazione raggruppa operazioni che devono riuscire o essere annullate insieme. Pensa a un acquisto: sottrarre il denaro e aggiungere il prodotto devono essere due parti di un'unica operazione coerente.

**Le operazioni sui dati IndexedDB avvengono sempre in una transazione.**

```js
let transaction = db.transaction('books', 'readwrite');
```

Il primo argomento può essere il nome di uno store o un array di nomi. La modalità può essere:

- `readonly`: legge i dati, ed è la modalità predefinita;
- `readwrite`: legge e modifica i dati.

Esiste anche la transazione `versionchange`, creata durante l'aggiornamento dello schema: permette di creare, modificare e cancellare store e indici.


::: tip Perché distinguere le modalità?
Più transazioni di lettura possono lavorare sugli stessi store. Le transazioni di scrittura con ambiti sovrapposti richiedono coordinamento e possono dover aspettare le precedenti. Dichiarare l'ambito e la modalità aiuta il browser a pianificare le operazioni.
:::

Per aggiungere un libro:

```js
let transaction = db.transaction("books", "readwrite");
let books = transaction.objectStore("books");
let book = { id: 'js', price: 10, created: new Date() };
let request = books.add(book);

request.onsuccess = function() {
  console.log("Book added to the store", request.result);
};
request.onerror = function() {
  console.log("Error", request.error);
};
```

I passaggi sono: creare la transazione, ottenere lo store, inviare una richiesta e gestirne il risultato.

I metodi di scrittura principali sono:

- `put(value, key)`: inserisce o sostituisce il valore con quella chiave;
- `add(value, key)`: inserisce un nuovo valore; una chiave già esistente produce `ConstraintError`.

Il secondo argomento serve solo quando lo store richiede una chiave esterna. Il risultato di una scrittura riuscita è la chiave del record; un eventuale errore è in `request.error`.

## Commit automatico

Una transazione può contenere più richieste. Normalmente viene completata automaticamente quando non restano richieste pendenti e non ne vengono aggiunte mentre è attiva.

Non serve una chiamata di chiusura nell'esempio precedente. L'API moderna include anche `commit()` per richiedere esplicitamente il commit quando non intendiamo aggiungere altre richieste, ma l'autocommit rimane il comportamento usuale.

**Non inserire operazioni asincrone indipendenti, come una richiesta di rete, nel mezzo della transazione presumendo che rimanga attiva.**

```js
let request1 = books.add(book);

request1.onsuccess = function() {
  fetch('/').then(() => {
    // La transazione potrebbe essere già terminata.
    // books.add(anotherBook) può generare TransactionInactiveError.
  });
};
```

Le transazioni devono essere brevi anche per evitare che altre scritture restino in attesa. Prepara prima i dati con la rete, poi apri la transazione ed esegui le operazioni IndexedDB. In alternativa crea una nuova transazione per il passaggio successivo.

Per sapere che l'intera transazione è riuscita usa `complete`:

```js
transaction.oncomplete = function() {
  console.log("Transaction is complete");
};
```

Il successo di una singola richiesta non garantisce il successo finale di tutte le scritture. Per annullare la transazione:

```js
transaction.abort();
```

Le modifiche vengono annullate e arriva l'evento `abort`.

## Gestione degli errori

Una scrittura può fallire per input non valido, una chiave duplicata, quote insufficienti o altri problemi. Un errore di richiesta non gestito normalmente interrompe la transazione e ne annulla le modifiche.

Se intendiamo gestire un errore recuperabile e proseguire, possiamo impedirne l'effetto predefinito:

```js
let transaction = db.transaction("books", "readwrite");
let book = { id: 'js', price: 10 };
let request = transaction.objectStore("books").add(book);

request.onerror = function(event) {
  if (request.error.name === "ConstraintError") {
    console.log("Book with such id already exists");
    event.preventDefault(); // Evita l'annullamento automatico per questo errore.
    // Qui possiamo scegliere una chiave alternativa.
  }
};

transaction.onabort = function() {
  console.log("Error", transaction.error);
};
```

### Delegazione degli eventi

Gli eventi di errore delle richieste possono propagarsi verso transazione e database. Possiamo quindi centralizzare la gestione:

```js
db.onerror = function(event) {
  let request = event.target;
  console.log("Error", request.error);
};
```

Se un errore è stato completamente gestito sul posto, `stopPropagation()` ne impedisce la propagazione:

```js
request.onerror = function(event) {
  if (request.error.name === "ConstraintError") {
    console.log("Book with such id already exists");
    event.preventDefault();
    event.stopPropagation();
  }
};
```

`preventDefault()` e `stopPropagation()` hanno ruoli diversi: il primo impedisce l'effetto predefinito sull'annullamento, il secondo evita che il gestore esterno riceva quell'errore.

## Ricerca

Possiamo cercare tramite la chiave primaria o, dopo aver creato un indice, tramite un'altra proprietà del record.

### Ricerca per chiave

I metodi accettano una chiave precisa o un intervallo `IDBKeyRange`:

- `IDBKeyRange.lowerBound(lower, open)`: valori maggiori o uguali a `lower`; con `open: true` esclude il limite;
- `IDBKeyRange.upperBound(upper, open)`: valori minori o uguali a `upper`;
- `IDBKeyRange.bound(lower, upper, lowerOpen, upperOpen)`: intervallo fra due limiti;
- `IDBKeyRange.only(key)`: una sola chiave.

Gli argomenti booleani sono opzionali e, per impostazione predefinita, i limiti sono inclusi.

Metodi dello store:

- `get(query)`: il primo valore corrispondente;
- `getAll(query, count)`: un array di valori, eventualmente limitato;
- `getKey(query)`: la prima chiave corrispondente;
- `getAllKeys(query, count)`: un array di chiavi;
- `count(query)`: il numero di record corrispondenti.

```js
books.get('js');
books.getAll(IDBKeyRange.bound('css', 'html'));
books.getAll(IDBKeyRange.upperBound('html', true));
books.getAll();
books.getAllKeys(IDBKeyRange.lowerBound('js', true));
```

Gli store sono ordinati per chiave. Le richieste che restituiscono più record rispettano quell'ordine.

### Ricerca per proprietà tramite un indice

Un indice associa i valori di una proprietà alle chiavi dei record che la possiedono:

```js
objectStore.createIndex(name, keyPath, options);
```

- `name` è il nome dell'indice;
- `keyPath` è il percorso della proprietà da indicizzare;
- `unique: true` vieta due record con lo stesso valore indicizzato;
- `multiEntry: true`, quando la proprietà è un array, indicizza separatamente i suoi elementi.

Creiamo un indice per il prezzo durante l'aggiornamento dello schema:

```js
openRequest.onupgradeneeded = function() {
  let db = openRequest.result;
  let books = db.createObjectStore('books', {keyPath: 'id'});
  books.createIndex('price_idx', 'price');
};
```

Il prezzo può essere condiviso da più libri, quindi non richiediamo unicità. Non è un array, perciò `multiEntry` non serve.

![](/javascript-info/6-data-storage/03-indexeddb/indexeddb-index.svg)

Il browser mantiene aggiornato l'indice quando i dati cambiano. Per cercare usiamo gli stessi metodi disponibili sullo store:

```js
let transaction = db.transaction("books");
let books = transaction.objectStore("books");
let priceIndex = books.index("price_idx");
let request = priceIndex.getAll(10);

request.onsuccess = function() {
  // getAll restituisce un array, vuoto se non trova record.
  console.log("Books", request.result);
};
```

Per trovare i libri con prezzo minore o uguale a `5`:

```js
let request = priceIndex.getAll(IDBKeyRange.upperBound(5));
```

L'indice è ordinato per la proprietà indicizzata: qui i risultati seguono il prezzo.

## Eliminare record

`delete(query)` elimina i record con la chiave o nell'intervallo specificato:

```js
books.delete('js');
```

Per eliminare in base a un'altra proprietà, cerchiamo prima la chiave primaria con l'indice e poi la usiamo sullo store:

```js
let transaction = db.transaction("books", "readwrite");
let books = transaction.objectStore("books");
let priceIndex = books.index("price_idx");
let request = priceIndex.getKey(5);

request.onsuccess = function() {
  let id = request.result;
  if (id !== undefined) books.delete(id);
};
```

Questo esempio elimina il primo record trovato. Per eliminarli tutti bisogna attraversare tutti i risultati. Per svuotare l'intero store:

```js
books.clear();
```

## Cursori

`getAll` e `getAllKeys` caricano i risultati in un array. Per molti dati può essere preferibile un **cursore**, che attraversa i record uno per volta.

```js
let request = store.openCursor(query, direction);
// openKeyCursor restituisce le chiavi senza caricare i valori.
```

La query può essere una chiave o un intervallo. Le direzioni sono:

- `next`: ordine crescente, predefinito;
- `prev`: ordine decrescente;
- `nextunique`, `prevunique`: saltano le chiavi di indice ripetute.

**La stessa richiesta invia più eventi `success`, uno per ogni risultato.**

```js
let transaction = db.transaction("books");
let books = transaction.objectStore("books");
let request = books.openCursor();

request.onsuccess = function() {
  let cursor = request.result;
  if (cursor) {
    console.log(cursor.key, cursor.value);
    cursor.continue();
  } else {
    console.log("No more books");
  }
};
```

`continue()` passa al risultato successivo; con una chiave può avanzare verso di essa. `advance(count)` salta un numero di risultati. Alla fine `request.result` è `null`.

Possiamo aprire un cursore anche su un indice. In quel caso `cursor.key` è la chiave dell'indice, mentre `cursor.primaryKey` è la chiave primaria dello store:

```js
let request = priceIndex.openCursor(IDBKeyRange.upperBound(5));

request.onsuccess = function() {
  let cursor = request.result;
  if (cursor) {
    console.log(cursor.key, cursor.primaryKey, cursor.value);
    cursor.continue();
  } else {
    console.log("No more books");
  }
};
```

## Un wrapper basato su Promise

Gestire manualmente `onsuccess` e `onerror` per ogni operazione può essere ripetitivo. [idb](https://github.com/jakearchibald/idb) espone una versione dell'API che usa Promise.

In un progetto con dipendenze installate puoi importare `openDB` da `idb`. L'esempio seguente usa l'API documentata attuale della libreria, aggiornando il frammento più vecchio presente nella fonte:

```js
import { openDB } from 'idb';

const db = await openDB('store', 1, {
  upgrade(db) {
    db.createObjectStore('books', {keyPath: 'id'});
  }
});

const transaction = db.transaction('books', 'readwrite');
const books = transaction.objectStore('books');

try {
  await books.add({id: 'js', price: 10});
  await books.add({id: 'css', price: 12});
  await transaction.done;
  console.log('Books saved');
} catch (err) {
  console.error('Error', err);
}
```

Il modulo deve essere eseguito in un ambiente che risolve il pacchetto `idb`, per esempio un progetto Vite con la dipendenza installata. È anche disponibile l'importazione browser indicata nella documentazione della libreria.

### Gestione degli errori con Promise

`try`/`catch` intercetta i rifiuti delle Promise attese con `await`. Un rifiuto non gestito può produrre `unhandledrejection` su `window`:

```js
window.addEventListener('unhandledrejection', event => {
  console.error('Unhandled error', event.reason);
});
```

Non sostituisce una gestione locale ragionata degli errori. `event.target` qui non è automaticamente la richiesta IndexedDB originale.

### Il problema della transazione inattiva

Le Promise non eliminano le regole di vita delle transazioni. Anche con `await`, una richiesta di rete fra due operazioni può lasciare che la transazione termini:

```js
const transaction = db.transaction('books', 'readwrite');
const books = transaction.objectStore('books');

await books.add({id: 'js', price: 10});
await fetch('/api/example');
// La transazione potrebbe essere già conclusa:
// await books.add({id: 'css', price: 12});
```

La soluzione rimane: raccogli prima i dati esterni, poi esegui la sequenza di operazioni sul database, oppure apri una nuova transazione.

### Accedere agli oggetti nativi

Il wrapper converte le richieste in Promise e aggiunge funzionalità agli oggetti IndexedDB. Se serve l'oggetto originale, la versione attuale offre `unwrap`; con `wrap` possiamo avvolgere di nuovo un oggetto nativo:

```js
import { unwrap, wrap } from 'idb';

const nativeDb = unwrap(db);
const wrappedDb = wrap(nativeDb);
```

Le proprietà disponibili dipendono dalla versione della libreria. Il vecchio accesso tramite `promise.request` mostrato nella fonte non è l'API consigliata della versione attuale.

## Riepilogo

IndexedDB è un database locale al browser, utile per dati strutturati e applicazioni offline.

1. Apri il database con un nome e una versione.
2. Crea store e indici durante l'aggiornamento dello schema.
3. Apri una transazione con ambito e modalità appropriati.
4. Cerca tramite la chiave primaria o un indice.
5. Usa i cursori per attraversare molti record.
6. Attendi il completamento dell'intera transazione e gestisci gli errori.

Il wrapper `idb` rende più comodo usare `async`/`await`, mantenendo le regole delle transazioni. [Apri la dimostrazione del tutorial originale](https://javascript.info/indexeddb).

Questo capitolo è una traduzione con adattamento: chiarisce la clonazione strutturata e aggiorna commit, cursori e API di `idb`. Riferimenti: [specifica IndexedDB](https://www.w3.org/TR/IndexedDB/), [MDN IDBTransaction](https://developer.mozilla.org/en-US/docs/Web/API/IDBTransaction) e [documentazione idb](https://github.com/jakearchibald/idb).
