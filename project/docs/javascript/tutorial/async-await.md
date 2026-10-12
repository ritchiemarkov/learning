---
title: "Async/await"
description: "JavaScript.info in italiano: Async/await"
sourceTutorial: true
prev: {"text": "Microtasks", "link": "/javascript/tutorial/microtask-queue"}
next: {"text": "I generatori", "link": "/javascript/tutorial/generators"}
---

# Async/await

> **JavaScript.info · Ilya Kantor e contributori.** [Originale inglese](https://javascript.info/async-await) · [Edizione italiana](https://it.javascript.info/async-await) · [Fonti e licenza](/javascript/fonti).

Esiste una sintassi speciale per lavorare con le promise in un modo più comodo, chiamata async/await. È sorprendentemente facile da capire e usare.


## Async functions

Iniziamo con la parola chiave `async`. Può essere messa prima di una funzione, come nell'esempio sotto:

```js
async function f() {
  return 1;
}
```

La parola "async" prima di una funzione significa una cosa semplice: la funzione ritorna sempre una promise. Gli altri valori sono "avvolti" wrapped in una promise risolta automaticamente.

Per esempio, questa funzione ritorna una promise risolta con il risultato di `1`, proviamola:

```js
async function f() {
  return 1;
}

f().then(alert); // 1
```

...Possiamo anche ritornare esplicitamente una promise, sarebbe lo stesso:

```js
async function f() {
  return Promise.resolve(1);
}

f().then(alert); // 1
```

Così, `async` assicura che la funzione ritorni una promise, e "avvolge" (wraps) le non-promise al suo interno. Abbastanza semplice, vero? Ma non sono quello. C'è un'altra parola chiave, `await`, che funziona solo nelle funzioni `async`, ed è piuttosto cool.

## Await

La sintassi:

```js
// funziona solo all'interno delle funzioni async
let value = await promise;
```

La parola chiave `await` fa attendere JavaScript fino a quando la promise è ferma (settles) e ritorna il suo risultato.

Ecco un esempio con una promise che si risolve in un secondo:
```js
async function f() {

  let promise = new Promise((resolve, reject) => {
    setTimeout(() => resolve("fatto!"), 1000)
  });


  let result = await promise; // attende fino a quando la promise si risolve (*)


  alert(result); // "fatto!"
}

f();
```

L'esecuzione della funzione "va in pausa" alla linea `(*)` e riprende quando la promise si ferma (settles), con `result` che diventa il suo risultato. Così il codice sopra mostra "fatto!" in un secondo.

Enfatizziamo: `await` fa letteralmente attendere JavaScript fino a quando la promise si ferma, poi va avanti con il risultato. Questo non costa alcuna risorsa della CPU, perché il motore può fare altri lavori nel frattempo: eseguire altri script, gestire eventi etc.

È solo una sintassi più elegante per ottenere il risultato della promise `promise.then`, più facile da leggere e da scrivere.


:::: warning Non possiamo usare `await` nelle normali funzioni
Se proviamo ad utilizzare `await` in una funzione non asincrona, otterremmo un errore di sintassi:

```js
function f() {
  let promise = Promise.resolve(1);

  let result = await promise; // Syntax error

}
```

Avremo questo errore se non mettiamo `async` prima di una funzione. Come detto, `await` funziona solo all'interno di una funzione asincrona (`async function`).
::::

Prendiamo l'esempio `showAvatar()` dal capitolo [Concatenamento di promise (promise chaining)](/javascript/tutorial/promise-chaining) e riscriviamolo usando `async/await`:

1. Avremo bisogno di sostituire le chiamate `.then` con `await`.
2. Inoltre dovremo rendere la funzione asincrona (`async`) per farli lavorare.

```js
async function showAvatar() {

  // legge il nostro JSON
  let response = await fetch('/article/promise-chaining/user.json');
  let user = await response.json();

  // legge l'utente GitHub
  let githubResponse = await fetch(`https://api.github.com/users/${user.name}`);
  let githubUser = await githubResponse.json();

  // show the avatar
  let img = document.createElement('img');
  img.src = githubUser.avatar_url;
  img.className = "promise-avatar-example";
  document.body.append(img);

  // wait 3 seconds
  await new Promise((resolve, reject) => setTimeout(resolve, 3000));

  img.remove();

  return githubUser;
}

showAvatar();
```

Piuttosto pulito e facile da leggere, vero? Molto meglio che prima.


:::: tip `await` Non funzionerà nel codice di livello più alto
Le persone che hanno appena iniziato ad utilizzare `await` tendono a dimenticare il fatto che non possiamo utilizzare `await` nel codice di livello piú alto. Per esempio, questo non funzionerà:

For instance:

```js
// we assume this code runs at top level, inside a module
let response = await fetch('/article/promise-chaining/user.json');
let user = await response.json();

console.log(user);
```

Possiamo "avvolgerlo" wrap in una funzione async anonima, come qui:

```js
(async () => {
  let response = await fetch('/article/promise-chaining/user.json');
  let user = await response.json();
  ...
})();
```

::::

:::: tip `await` accetta i "thenables"
Come `promise.then`, `await` permette di usare gli oggetti "thenable" (quelli con un metodo `then`). L' idea è che un oggetto di terze parti possa non essere una promise, ma essere promise-compatibile: se supporta `.then`, è abbastanza per usarlo con `await`.

Ecco una dimostrazione: la classe `Thenable` class, l'`await` sotto accetta:

```js
class Thenable {
  constructor(num) {
    this.num = num;
  }
  then(resolve, reject) {
    alert(resolve);
    // risolve con this.num*2 dopo 1000ms
    setTimeout(() => resolve(this.num * 2), 1000); // (*)
  }
}

async function f() {
  // attende per 1 secondo, poi il risultato diventa 2
  let result = await new Thenable(1);
  alert(result);
}

f();
```

Se `await` riceve un oggetto non-promise con `.then`, chiama quel metodo passando le funzioni native `resolve`, `reject` come argomenti. Poi `await` fino a quando una delle due viene chiamata (nell'esempio sopra avviene nella linea `(*)`) e poi procede con il risultato.
::::


:::: tip Methods async delle classi
Per dichiarare un metodo async di una classe, basta precederlo con `async`:

```js
class Waiter {

  async wait() {

    return await Promise.resolve(1);
  }
}

new Waiter()
  .wait()
  .then(alert); // 1 (this is the same as (result => alert(result)))
```
Il significato è lo stesso: assicura che il valore ritornato sia una promise ed abilita `await`.

::::
## Gestione degli errori

Se una promise si risolve normalmente, allora `await promise` ritorna il risultato. Ma nel caso di un rigetto (rejection), solleva l'errore, proprio come se in quella linea ci fosse stato un `throw`.

Questo codice:

```js
async function f() {

  await Promise.reject(new Error("Whoops!"));

}
```

...È lo stesso di questo:

```js
async function f() {

  throw new Error("Whoops!");

}
```

Nelle situazioni reali, la promise può prendere del tempo prima di venire rigettata. In quel caso ci sarà un ritardo prima che `await` sollevi un errore.

Possiamo catturare l'errore utilizzando `try..catch`, allo stesso modo che con un regolare `throw`:

```js
async function f() {

  try {
    let response = await fetch('http://no-such-url');
  } catch(err) {

    alert(err); // TypeError: failed to fetch

  }
}

f();
```

In caso di errore, il controllo salta al blocco `catch`. Possiamo anche "avvolgere" (wrap) più linee:

```js
async function f() {

  try {
    let response = await fetch('/no-user-here');
    let user = await response.json();
  } catch(err) {
    // cattura gli errori sia in fetch che in response.json
    alert(err);
  }
}

f();
```

Se non abbiamo `try..catch`, allora la promise generata dalla chiamata della funzione async `f()` viene rigettata. Possiamo aggiungere `.catch` per gestirla:

```js
async function f() {
  let response = await fetch('http://no-such-url');
}

// f() diventa una promise rigettata

f().catch(alert); // TypeError: failed to fetch // (*)

```

Se ci dimentichiamo di aggiungere `.catch` qui, allora otterremo un errore di una promise non gestito (visibile nella console). Possiamo catturare usando un gestore di eventi globale come descritto nel capitolo [Gestione degli errori con le promise](/javascript/tutorial/promise-error-handling).



::: tip `async/await` and `promise.then/catch`
Quando usiamo `async/await`, raramente abbiamo bisogno di `.then`, perché `await` gestisce l'attesa per noi. E possiamo usare un normale `try..catch` invece di `.catch`. Questo è spesso (non sempre) più conveniente.

Ma al livello più alto del codice, quando siamo fuori da qualunque funzione `async`, non siamo sintatticamente in grado id usare `await`, così è una pratica normale usare `.then/catch` per gestire il risultato finale degli errori che "cadono attraverso" (falling-through).

Come nella linea `(*)` dell'esempio sopra.
:::


:::: tip `async/await` funziona bene con `Promise.all`
Quando dobbiamo attendere per più promise, possiamo avvolgerle (wrap) in `Promise.all` e poi attendere (`await`):

```js
// attende per l'array dei risultati
let results = await Promise.all([
  fetch(url1),
  fetch(url2),
  ...
]);
```

In caso di errore, si propaga come di solito: dalla promise fallita a `Promise.all`, poi diventa una eccezione che possiamo catturare usando `try..catch` attorno alla chiamata.

::::

## Riepilogo

La parola chiave `async` prima di una funzione ha due effetti:

1. Fa sempre ritornare una promise.
2. Permette di usare `await` al suo interno.

La parola chiave `await` prima di una promise fa attendere JavaScript fino a quando la promise è ferma, e poi:

1. Se c'è un errore, l'eccezione è generata, come se `throw error` fosse stato chiamato in quel punto.
2. Altrimenti, ritorna il risultato.

Insieme forniscono una ottima struttura per scrivere codice asincrono che sia facile sia da leggere che da scrivere.

Con `async/await` raramente avremo bisogno di scrivere `promise.then/catch`, ma comunque non dovremo dimenticare che sono sempre basate su promise, perché a volte (e.s. nello scope più esterno) dovremo usare questi metodi. Inoltre `Promise.all` è una buona cosa per attendere per più task contemporaneamente.

## Esercizi

### 1 · Promise.all e operazioni ancora in corso

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

::::: details Soluzione

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

:::::

### 2 · Rewrite using async/await

Rewrite this example code from the chapter [Concatenamento di promise (promise chaining)](/javascript/tutorial/promise-chaining) using `async/await` instead of `.then/catch`:

```js
function loadJson(url) {
  return fetch(url)
    .then(response => {
      if (response.status == 200) {
        return response.json();
      } else {
        throw new Error(response.status);
      }
    });
}

loadJson('no-such-user.json')
  .catch(alert); // Error: 404
```

::::: details Soluzione

Le note sono sotto il codice:

```js
async function loadJson(url) { // (1)
  let response = await fetch(url); // (2)

  if (response.status == 200) {
    let json = await response.json(); // (3)
    return json;
  }

  throw new Error(response.status);
}

loadJson('no-such-user.json')
  .catch(alert); // Error: 404 (4)
```

Note:

1. La funzione `loadJson` diventa `async`.
2. Tutti i `.then` interni sono sostituiti con `await`.
3. Possiamo ritornare `response.json()` invece di aspettarlo (awaiting for it), come qui:

    ```js
    if (response.status == 200) {
      return response.json(); // (3)
    }
    ```

    Poi il codice esterno avrebbe dovuto attendere (`await)` che la promise risolvesse. Nel nostro caso non è importante.
4. L'errore sollevato da `loadJson` è gestito da `.catch`. Non possiamo usare `await loadJson(…)` qui, perchè non siamo in una funzione `async`.

:::::

### 3 · Riscrivere "rethrow"  con async/await

Sotto puoi trovare l'esempio "rethrow". Riscriverlo usando `async/await` invece di `.then/catch`.

Sbarazzarsi della ricorsione a favore di un ciclo in `demoGithubUser`: con `async/await` diventa facile da fare.

```js
class HttpError extends Error {
  constructor(response) {
    super(`${response.status} for ${response.url}`);
    this.name = 'HttpError';
    this.response = response;
  }
}

function loadJson(url) {
  return fetch(url)
    .then(response => {
      if (response.status == 200) {
        return response.json();
      } else {
        throw new HttpError(response);
      }
    });
}

// Ask for a user name until github returns a valid user
function demoGithubUser() {
  let name = prompt("Enter a name?", "iliakan");

  return loadJson(`https://api.github.com/users/${name}`)
    .then(user => {
      alert(`Full name: ${user.name}.`);
      return user;
    })
    .catch(err => {
      if (err instanceof HttpError && err.response.status == 404) {
        alert("No such user, please reenter.");
        return demoGithubUser();
      } else {
        throw err;
      }
    });
}

demoGithubUser();
```

::::: details Soluzione

Non ci sono trucchi qui. Basta sostituire `.catch` with `try...catch` dentro `demoGithubUser` e aggiungere `async/await` quando necessario:

```js
class HttpError extends Error {
  constructor(response) {
    super(`${response.status} for ${response.url}`);
    this.name = 'HttpError';
    this.response = response;
  }
}

async function loadJson(url) {
  let response = await fetch(url);
  if (response.status == 200) {
    return response.json();
  } else {
    throw new HttpError(response);
  }
}

// Ask for a user name until github returns a valid user
async function demoGithubUser() {

  let user;
  while(true) {
    let name = prompt("Enter a name?", "iliakan");

    try {
      user = await loadJson(`https://api.github.com/users/${name}`);
      break; // no error, exit loop
    } catch(err) {
      if (err instanceof HttpError && err.response.status == 404) {
        // loop continues after the alert
        alert("No such user, please reenter.");
      } else {
        // unknown error, rethrow
        throw err;
      }
    }      
  }


  alert(`Full name: ${user.name}.`);
  return user;
}

demoGithubUser();
```

:::::

### 4 · Call async from non-async

Abbiamo una funzione "regolare". Come chiamare `async` da questa ed usare il suo risultato?

```js
async function wait() {
  await new Promise(resolve => setTimeout(resolve, 1000));

  return 10;
}

function f() {
  // ...cosa bisonga scrivere qui?
  // dobbiamo chiamare async wait() ed aspettare per ricevere 10
  // ricorda, non possiamo usare "await"
}
```

P.S. Il task è tecnicamente molto semplice, ma la domanda è piuttosto comune per gli sviluppatori nuovi ad async/await.

::::: details Soluzione

That's the case when knowing how it works inside is helpful.

Just treat `async` call as promise and attach `.then` to it:
```js
async function wait() {
  await new Promise(resolve => setTimeout(resolve, 1000));

  return 10;
}

function f() {
  // shows 10 after 1 second

  wait().then(result => alert(result));

}

f();
```

:::::

