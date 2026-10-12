---
title: "WeakMap e WeakSet"
description: "JavaScript.info in italiano: WeakMap e WeakSet"
sourceTutorial: true
prev: {"text": "Map e Set", "link": "/javascript/tutorial/map-set"}
next: {"text": "Object.keys, values, entries", "link": "/javascript/tutorial/keys-values-entries"}
---

# WeakMap e WeakSet

> **JavaScript.info · Ilya Kantor e contributori.** [Originale inglese](https://javascript.info/weakmap-weakset) · [Edizione italiana](https://it.javascript.info/weakmap-weakset) · [Fonti e licenza](/javascript/fonti).

Come abbiamo già visto nel capitolo [Garbage collection ("Spazzatura")](/javascript/tutorial/garbage-collection), il motore JavaScript mantiene un valore in memoria fino a che questo risulta accessibile (e potrebbe potenzialmente essere utilizzato).

Ad esempio:
```js
let john = { name: "John" };

// l'oggetto è accessibile, john è un suo riferimento

// sovrascriviamo il riferimento
john = null;


// l'oggetto verrà rimosso dalla memoria

```

Solitamente, le proprietà di un oggetto o gli elementi di un array o di qualsiasi altra struttura dati vengono considerati accessibili fino a che questi rimangono mantenuti in memoria.

Ad esempio, se inseriamo un oggetto in un array, fino a che l'array rimane "vivo", anche l'oggetto rimarrà in memoria, anche se non sono presenti riferimenti.

Come nell'esempio:

```js
let john = { name: "John" };

let array = [ john ];

john = null; // sovrascriviamo il riferimento


// john è memorizzato all'interno dell'array
// quindi non verrà toccato dal garbage collector
// possiamo estrarlo tramite array[0]

```

O, se utilizziamo un oggetto come chiave in una `Map`, fino a che la `Map` esiste, anche l'oggetto esisterà. Occuperà memoria e non potrà essere ripulito dal garbage collector.

Ad esempio:

```js
let john = { name: "John" };

let map = new Map();
map.set(john, "...");

john = null; // sovrascriviamo il riferimento


// john viene memorizzato all'interno di map,
// possiamo estrarlo utilizzando map.keys()

```

`WeakMap` è fondamentalmente diverso sotto questo aspetto. Infatti non previene la garbage-collection degli oggetti utilizzati come chiave.

Vediamo cosa significa questo, utilizzando degli esempi.

## WeakMap

La prima differenza tra `Map` e `WeakMap` è che le chiavi devono essere oggetti, non valori primitivi:

```js
let weakMap = new WeakMap();

let obj = {};

weakMap.set(obj, "ok"); // funziona


// non possiamo utilizzare una stringa come chiave
weakMap.set("test", "Whoops"); // Errore, perché "test" non è un oggetto

```

Ora, se utilizziamo un oggetto come chiave, e non ci sono altri riferimenti a quell'oggetto -- questo verrà rimosso dalla memoria (e dalla map) automaticamente.

```js
let john = { name: "John" };

let weakMap = new WeakMap();
weakMap.set(john, "...");

john = null; // sovrascriviamo il riferimento

// john è stato rimosso dalla memoria!
```

Confrontiamolo con l'esempio di `Map` visto sopra. Ora, se `john` esiste solo come chiave della `WeakMap` -- verrà eliminato automaticamente dalla map (e anche dalla memoria).

`WeakMap` non supporta gli iteratori e i metodi `keys()`, `values()`, `entries()`, quindi non c'è alcun modo di ottenere tutte le chiavi o i valori tramite questi metodi.

`WeakMap` possiede solamente i seguenti metodi:

- `weakMap.get(key)`
- `weakMap.set(key, value)`
- `weakMap.delete(key)`
- `weakMap.has(key)`

Perché questa limitazione? Per ragioni tecniche. Se un oggetto ha perso tutti i riferimenti (come `john` nel codice sopra), allora verrà automaticamente eliminato. Ma tecnicamente non è specificato esattamente *quando avverrà la pulizia*.

Sarà il motore JavaScript a deciderlo. Potrebbe decidere di effettuare subito la pulizia della memoria oppure aspettare più oggetti per eliminarli in blocco. Quindi, tecnicamente il numero degli elementi di una `WeakMap` non è conosciuto. Il motore potrebbe già aver effettuato la pulizia oppure no, o averlo fatto solo parzialmente. Per questo motivo, i metodi che accedono a `WeakMap` per intero non sopo supportati.

Dove potremmo avere bisogno di una struttura simile?

## Caso d'uso: dati aggiuntivi

Il principale campo di applicazione di `WeakMap` è quello di un *additional data storage*.

Se stiamo lavorando con un oggetto che "appartiene" ad un altro codice, magari una libreria di terze parti, e vogliamo memorizzare alcuni dati associati ad esso, che però dovrebbero esistere solamente finché l'oggetto esiste - allora una `WeakMap` è proprio ciò di cui abbiamo bisogno.

Inseriamo i dati in una `WeakMap`, utilizzando l'oggetto come chiave; quando l'oggetto verrà ripulito dal garbage collector, anche i dati associati verranno ripuliti.

```js
weakMap.set(john, "secret documents");
// se john muore, i documenti segreti verranno distrutti automaticamente
```

Proviamo a guardare un esempio.

Immaginiamo di avere del codice che tiene nota del numero di visite per ogni utente. L'informazione viene memorizzata in un map: l'utente è la chiave, mentre il conteggio delle visite è il valore. Quando l'utente esce, vogliamo smettere di mantenere in memoria il conteggio delle visite.

Qui vediamo un esempio di conteggio utilizzando `Map`:

```js
// 📁 visitsCount.js
let visitsCountMap = new Map(); // map: user => conteggio visite

// incrementa il conteggio delle visite
function countUser(user) {
  let count = visitsCountMap.get(user) || 0;
  visitsCountMap.set(user, count + 1);
}
```

E qui abbiamo un'altra porzione di codice, magari in un altro file, che la utilizza:

```js
// 📁 main.js
let john = { name: "John" };

countUser(john); // conta le sue visite

// più tadi John se ne va
john = null;
```

Ora, l'oggetto `john` dovrebbe essere ripulito dal garbage collector, ma rimane in memoria, in quanto chiave in `visitsCountMap`.

Dobbiamo ripulire `visitsCountMap` quando rimuoviamo l'utente, altrimenti continuerà a crescere nella memoria indefinitamente. Una pulizia di questo tipo potrebbe essere complessa in architetture più elaborate.

Possiamo risolvere questo problema utilizzando una `WeakMap`:

```js
// 📁 visitsCount.js
let visitsCountMap = new WeakMap(); // weakmap: user => conteggio visite

// incrementa il conteggio delle visite
function countUser(user) {
  let count = visitsCountMap.get(user) || 0;
  visitsCountMap.set(user, count + 1);
}
```

Ora non dobbiamo più ripulire `visitsCountMap`. Una volta che `john` non sarà più accessibile, ad eccezione che come chiave della `WeakMap`, verrà rimosso dalla memoria, insieme a tutte le informazioni associate contenute nella `WeakMap`.

## Caso d'uso: caching

Un altro caso d'uso comune è il caching. Possiamo memorizzare i risultati di una funzione, così che le successive chiamate alla funzione possano riutilizzarli.

Per fare questo possiamo utilizzare una `Map` (non la scelta ottimale):

```js
// 📁 cache.js
let cache = new Map();

// calcola e memorizza il risultato
function process(obj) {
  if (!cache.has(obj)) {
    let result = /* calcola il risultato per */ obj;

    cache.set(obj, result);
  }

  return cache.get(obj);
}


// Ora utilizziamo process() in un altro file:


// 📁 main.js
let obj = {/* ipotizziamo di avere un oggetto */};

let result1 = process(obj); // calcolato

// ...più tardi, da un'altra parte del codice...
let result2 = process(obj); // prendiamo il risultato dalla cache

// ...più avanti, quando non abbiamo più bisogno dell'oggetto:
obj = null;

alert(cache.size); // 1 (Ouch! L'oggetto è ancora in cache, sta occupando memoria!)
```

Per chiamate multiple di `process(obj)` con lo stesso oggetto, il risultato viene calcolato solamente la prima volta, le successive chiamate lo prenderanno dalla `cache`. Il lato negativo è che dobbiamo ricordarci di pulire la `cache` quando non è più necessaria.

Se sostituiamo `Map` con `WeakMap`, il problema si risolve. I risultati in cache vengono automaticamente rimossi una volta che l'oggetto viene ripulito dal garbage collector.

```js
// 📁 cache.js

let cache = new WeakMap();


// calcola e memorizza il risultato
function process(obj) {
  if (!cache.has(obj)) {
    let result = /* calcola il risultato per */ obj;

    cache.set(obj, result);
  }

  return cache.get(obj);
}

// 📁 main.js
let obj = {/* un oggetto */};

let result1 = process(obj);
let result2 = process(obj);

// ...più tardi, quando non abbiamo più bisogno dell'oggetto
obj = null;

// Non possiamo ottenere la dimensione della cache, poiché è una WeakMap,
// ma è 0 oppure lo sarà presto
// Quando un oggetto viene ripulito dal garbage collector, anche i dati associati vengono ripuliti
```

## WeakSet

`WeakSet` si comporta in maniera simile:

- E' analogo a `Set`, ma possiamo aggiungere solamente oggetti a `WeakSet` (non primitivi).
- Un oggetto esiste in un set solamente finché rimane accessibile in un altro punto del codice.
- Come `Set`,  supporta `add`, `has` e `delete`, ma non `size`, `keys()` e nemmeno gli iteratori.

Il fatto che sia "weak" la rende utile come spazio di archiviazione aggiuntivo. Non per dati arbitrari, ma piuttosto per questioni di tipo "si/no". Il fatto di appartenere ad un `WeakSet` può significare qualcosa sull'oggetto.

Ad esempio, possiamo aggiungere gli utenti ad un `WeakSet` per tenere traccia di chi ha visitato il nostro sito:

```js
let visitedSet = new WeakSet();

let john = { name: "John" };
let pete = { name: "Pete" };
let mary = { name: "Mary" };

visitedSet.add(john); // John ci ha visitato
visitedSet.add(pete); // Poi Pete
visitedSet.add(john); // John di nuovo

// visitedSet ha 2 utenti ora

// controlliamo se John ci ha visitato
alert(visitedSet.has(john)); // true

// controlliamo se Mary ci ha visitato
alert(visitedSet.has(mary)); // false

john = null;

// visitedSet verrà ripulito automaticamente
```

La maggior limitazione di `WeakMap` e `WeakSet` è l'assenza di iteratori, e la mancanza della possibilità di ottenere tutti gli elementi contenuti. Potrebbe sembrare un inconveniente, ma non vieta a `WeakMap/WeakSet` di compiere il proprio lavoro -- essere una struttura "addizionale" per memorizzare informazioni relative a dati memorizzati in un altro posto.

## Riepilogo

`WeakMap` è una collezione simile a `Map`, ma permette di utilizzare solamente oggetti come chiavi; inoltre, la rimozione di un oggetto rimuove anche il valore associato.

`WeakSet` è una collezione simile a `Set`, che memorizza solamente oggetti, e li rimuove completamente una volta che diventano inaccessibili.

Il loro principale vantaggio è che possiedono un riferimento debole agli oggetti, in questo modo possono essere facilmente ripuliti dal garbage collector.

Il lato negativo è di non poter utilizzare `clear`, `size`, `keys`, `values`...

`WeakMap` e `WeakSet` vengono utilizzati come strutture dati "secondarie" in aggiunta a quelle "principali". Una volta che l'oggetto viene rimosso dalla struttura dati "principale", se l'unico riferimento rimasto è una chiave di `WeakMap` o `WeakSet`, allora verrà rimosso.

## Esercizi

### 1 · Memorizzare le bandiere non visualizzate

Abbiamo un array di messaggi:

```js
let messages = [
  {text: "Hello", from: "John"},
  {text: "How goes?", from: "John"},
  {text: "See you soon", from: "Alice"}
];
```

Il vostro codice vi può accedere, ma i messaggi sono gestiti dal codice di qualcun altro. Vengono aggiunti nuovi messaggi, quelli vecchi vengono rimossi, e voi non avete modo di sapere quando ciò accade.

Ora, quale struttura dati potresti utilizzare per memorizzare quali messaggi "sono stati letti"? La struttura deve calzare bene al problema, e rispondere alla domanda  "è stato letto?".

P.S. Quando un messaggio viene rimosso da `messages`, dovrebbe essere rimosso anche dalla vostra struttura.

P.P.S. Non dovremmo modificare l'oggetto messagge. Poichè se viene gestito dal codice di qualcun altro, aggiungere nuove proprietà potrebbe avere conseguenze disastrose.

::::: details Soluzione

Memorizziamo i messaggi letti in `WeakSet`:

```js
let messages = [
  {text: "Hello", from: "John"},
  {text: "How goes?", from: "John"},
  {text: "See you soon", from: "Alice"}
];

let readMessages = new WeakSet();

//due messaggi sono stati letti
readMessages.add(messages[0]);
readMessages.add(messages[1]);
// readMessages ha due elementi

//...leggiamo nuovamente il primo messaggio!
readMessages.add(messages[0]);
// readMessages ha 2 elementi unici

//risposta: message[0] è stato letto?
alert("Read message 0: " + readMessages.has(messages[0])); // true

messages.shift();
// ora readMessages ha un elemento (tecnicamente la memoria potrebbe essere ripulita dopo)
```

La struttura `WeakSet` consente di memorizzare un insieme di messaggi e di verificare facilmente la presenza di un dato messaggio.

Viene ripulita automaticamente. Il lato negativo è che non possiamo eseguire iterazioni. Non possiamo ottenere direttamente "tutti i messaggi letti". Ma possiamo farlo iterando su tutti i messaggi e filtrando tutti quelli che sono presenti nel set.

Another, different solution could be to add a property like `message.isRead=true` to a message after it's read. As messages objects are managed by another code, that's generally discouraged, but we can use a symbolic property to avoid conflicts.

Un'altra soluzione potrebbe essere aggiungere una proprietà come `message.isRead=true`, ma farlo potrebbe essere pericoloso, se questo oggetto viene gestito dal codice di un'altra persona;  per evitare conflitti possiamo utilizzare un *symbol*.

Come qui:
```js
//la proprietà simbolica è visibile solo al nostro codice 
let isRead = Symbol("isRead");
messages[0][isRead] = true;
```

Ora anche se qualcun altro utilizza `for..in` per avere accesso a tutte le proprietà di messages, la nostra proprietà sarà segreta.


Although symbols allow to lower the probability of problems, using `WeakSet` is better from the architectural point of view.
Sebbene i simboli permettano una minore probabilità di problemi, utilizzare `weakSet` è meglio da un punto di vista architetturale.

:::::

### 2 · Memorizzare le date di lettura

Abbiamo un array di messaggi come nel [compito precedente](https://it.javascript.info/task/recipients-read). La situazione è simile.

```js
let messages = [
  {text: "Hello", from: "John"},
  {text: "How goes?", from: "John"},
  {text: "See you soon", from: "Alice"}
];
```

Ora la domanda è: quale struttura di dati converrebbe utilizzare per memorizzare l'informazione: "quando è stato letto il messaggio?".

Nel compito precedente la necessità era semplicemente di memorizzare la lettura del messaggio. Ora abbiamo bisogno di memorizzare anche la data; anche in questo caso, se il messaggio viene eliminato questa dovrebbe sparire.

::::: details Soluzione

Per memorizzare una data possiamo utilizzare `WeakMap`:

```js
let messages = [
  {text: "Hello", from: "John"},
  {text: "How goes?", from: "John"},
  {text: "See you soon", from: "Alice"}
];

let readMap = new WeakMap();

readMap.set(messages[0], new Date(2017, 1, 1));
// Oggetto di tipo Date che studieremo più avanti
```

:::::

