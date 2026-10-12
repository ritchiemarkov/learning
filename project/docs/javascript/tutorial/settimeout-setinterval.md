---
title: "Pianificazione: setTimeout e setInterval"
description: "JavaScript.info in italiano: Pianificazione: setTimeout e setInterval"
sourceTutorial: true
prev: {"text": "La sintassi \"new Function\"", "link": "/javascript/tutorial/new-function"}
next: {"text": "*Decorators* e forwarding, call/apply", "link": "/javascript/tutorial/call-apply-decorators"}
---

# Pianificazione: setTimeout e setInterval

> **JavaScript.info · Ilya Kantor e contributori.** [Originale inglese](https://javascript.info/settimeout-setinterval) · [Edizione italiana](https://it.javascript.info/settimeout-setinterval) · [Fonti e licenza](/javascript/fonti).

Potremmo decidere di non eseguire subito una funzione, ma dopo un certo lasso di tempo. Questo è detto "pianificare una chiamata" ("scheduling a call").

Ci sono due metodi per farlo:

- `setTimeout` permette di eseguire una volta la funzione dopo l'intervallo prescelto.
- `setInterval` permette di eseguire regolarmente la funzione lasciando scorrere l'intervallo di tempo prescelto tra una chiamata e l'altra.

Questi metodi non fanno parte delle specifiche di JavaScript. Ma la maggior parte degli ambienti hanno un pianificatore interno e forniscono questi metodi. In particolare, sono supportati in tutti i browser e in Node.js.

## setTimeout

La sintassi:

```js
let timerId = setTimeout(func|codice, [ritardo], [arg1], [arg2], ...)
```

Parametri:

`func|codice`
: Funzione o stringa (string) di codice da eseguire.
Di solito è una funzione. Per ragioni storiche, si può passare una stringa (string) di codice, ma è sconsigliato.

`ritardo`
: Il ritardo in millisecondi (1000 ms = 1 secondo) prima dell'esecuzione, di base 0.

`arg1`, `arg2`...
: Gli argomenti della funzione (non supportati in IE9-)

Per esempio, questo codice esegue `saluta()` dopo un secondo:

```js
function saluta() {
  alert('Ciao');
}


setTimeout(saluta, 1000);

```

Con gli argomenti:

```js
function saluta(frase, chi) {
  alert( frase + ', ' + chi );
}


setTimeout(saluta, 1000, "Ciao", "Giovanni"); // Ciao, Giovanni

```

Se il primo argomento è una stringa (string), JavaScript crea una funzione dallo stesso.

Quindi funzionerà anche così:

```js
setTimeout("alert('Ciao')", 1000);
```

Ma l'utilizzo delle stringhe (string) è sconsigliato, usiamo piuttosto una funzione come questa:

```js
setTimeout(() => alert('Ciao'), 1000);
```


:::: tip Passa una funzione, ma non la esegue
Gli sviluppatori alle prime armi talvolta fanno l'errore di aggiungere le parentesi `()` dopo la funzione:

```js
// sbagliato!
setTimeout(saluta(), 1000);
```
Non funziona, perché `setTimeout` si aspetta un richiamo a una funzione. Qui `saluta()` esegue la funzione e viene passato a `setTimeout` il *risultato della sua esecuzione*. Nel nostro caso il risultato di `saluta()` è `undefined` (la funzione non restituisce nulla), quindi non viene pianificato niente.
::::

### Annullare con clearTimeout

Una chiamata a `setTimeout` restituisce un "identificatore del timer" (timer identifier) `timerId` che possiamo usare per disattivare l'esecuzione.

La sintassi per annullare:

```js
let timerId = setTimeout(...);
clearTimeout(timerId);
```

Nel codice qui sotto, pianifichiamo la funzione e poi la annulliamo (abbiamo cambiato idea). Ne risulta che non accade niente:

```js
let timerId = setTimeout(() => alert("non accade niente"), 1000);
alert(timerId); // identificatore del timer

clearTimeout(timerId);
alert(timerId); // stesso identificatore (non diventa null dopo la disattivazione)
```

Come possiamo vedere dall'output dell'`alert`, in un browser l'identificatore del timer è un numero. In altri ambienti, potrebbe essere qualcos'altro. Per esempio, Node.js restituisce un oggetto timer con metodi addizionali.

Anche qui, non ci sono specifiche universali per questi metodi, quindi va bene così.

Per i browser, i timer sono descritti nella [sezione Timers](https://www.w3.org/TR/html5/webappapis.html#timers) di HTML5 standard.

## setInterval

Il metodo `setInterval` ha la stessa sintassi di `setTimeout`:

```js
let timerId = setInterval(func|codice, [ritardo], [arg1], [arg2], ...)
```

Tutti gli argomenti hanno lo stesso significato. Ma a diferenza di `setTimeout` non esegue la funzione solo una volta, ma in modo regolare dopo un dato intervallo di tempo.

Per evitare ulteriori chiamate, dobbiamo eseguire `clearInterval(timerId)`.

L'esempio che segue mostrerà un messaggio ogni 2 secondi. Dopo 5 secondi, l'output verrà fermato:

```js
// ripete con un intervallo di 2 secondi
let timerId = setInterval(() => alert('tic'), 2000);

// dopo 5 secondi si ferma
setTimeout(() => { clearInterval(timerId); alert('stop'); }, 5000);
```


::: tip Il tempo passa mentre viene mostrato l'`alert`
Nella maggior parte dei browser, inclusi Chrome e Firefox, il timer interno continua a "ticchettare" mentre viene mostrato `alert/confirm/prompt`.

Quindi, se eseguiamo il codice qui sopra e non chiudiamo la finestra dell'`alert` per qualche istante, l'`alert` successivo verrà mostrato immediatamente e l'intervallo tra i due avvisi sarà più breve di 2 secondi.
:::

## setTimeout annidati

Ci sono due modi per eseguire qualcosa regolarmente.

Uno è `setInterval`. L'altro è un `setTimeout` ricorsivo, come questo:

```js
/** invece di:
let timerId = setInterval(() => alert('tic'), 2000);
*/

let timerId = setTimeout(function tic() {
  alert('tic');

  timerId = setTimeout(tic, 2000); // (*)

}, 2000);
```

Il `setTimeout` qui sopra pianifica la prossima chiamata subito alla fine di quella attuale `(*)`.

Il `setTimeout` ricorsivo è un metodo più flessibile di `setInterval`. In tal modo la chiamata successiva può essere pianificata in modo diverso, a seconda del risultato di quella attuale.

Per esempio, dobbiamo scrivere un servizio che mandi ogni 5 secondi una richiesta al server chiedendo dati, ma, in caso il server sia sovraccarico, dovrebbe aumentare l'intervallo di 10, 20, 40 secondi...

Qui lo pseudocodice:
```js
let ritardo = 5000;

let timerId = setTimeout(function richiesta() {
  ...manda la richiesta...

  if (la richiesta fallisce a causa di sovraccarico del server) {
    // aumenta l'intervallo per la prossima esecuzione
    ritardo *= 2;
  }

  timerId = setTimeout(richiesta, ritardo);

}, ritardo);
```


Inoltre, se le funzioni che stiamo pianificando sono avide di CPU, possiamo misurare il tempo richiesto dall'esecuzione e pianificare la chiamata successiva prima o dopo.

**Il `setTimeout` ricorsivo permette di impostare un ritardo tra le esecuzioni in modo più preciso di `setInterval`.**

Paragoniamo due frammenti di codice. Il primo usa `setInterval`:

```js
let i = 1;
setInterval(function() {
  func(i++);
}, 100);
```

Il secondo usa il `setTimeout` ricorsivo:

```js
let i = 1;
setTimeout(function avvia() {
  func(i++);
  setTimeout(avvia, 100);
}, 100);
```

Per `setInterval` la pianificazione interna eseguirà `func(i++)` ogni 100ms:

![](/javascript-info/1-js/06-advanced-functions/08-settimeout-setinterval/setinterval-interval.svg)

Avete notato?

**Il ritardo reale tra la chiamata `func` di `setInterval` è inferiore a quello del codice!**

È normale, perché il tempo che occorre all'esecuzione di `func` "consuma" una parte dell'intervallo.

È possibile che l'esecuzione di `func`sia più lunga del previsto e richieda più di 100ms.

In tal caso la macchina attende che `func` sia completa, poi verifica la pianificazione e se il tempo è terminato, la esegue di nuovo *immediatamente*.

In casi limite, se la funzione viene eseguita sempre dopo gli ms di `ritardo`, le chiamate avverranno senza alcuna pausa.

Qui c'è l'immagine per il `setTimeout` ricorsivo:

![](/javascript-info/1-js/06-advanced-functions/08-settimeout-setinterval/settimeout-interval.svg)

**Il `setTimeout` ricorsivo garantisce il ritardo fissato (qui 100ms).**

Questo perché una nuova chiamata è pianificata solo alla fine della precedente.


:::: tip La Garbage Collection (letteralmente 'raccolta dei rifiuti') e il callback in setInterval/setTimeout
Quando una funzione viene passata in `setInterval/setTimeout`, viene creata e salvata nella pianificazione una referenza interna per la funzione stessa. Questo evita che la funzione venga eliminata anche se non ci sono altre referenze.

```js
// la funzone resta in memoria finché la pianificazione la esegue
setTimeout(function() {...}, 100);
```

Per `setInterval` la funzione resta in memoria fino a quando viene eseguito `clearInterval`.

C'è un effetto collaterale. Una funzione si riferisce all'ambiente lessicale esterno, quindi, finché vive, vivono anche le variabili esterne. Queste possono richiedere molta più memoria della funzione stessa. Ne consegue che quando non ci serve più la funzione pianificata, è meglio cancellarla, anche se è molto piccola.
::::

## setTimeout con zero-delay (ritardo zero)

C'è un caso speciale: `setTimeout(func, 0)` o semplicemente `setTimeout(func)`.

In questo caso l'esecuzione della `func` viene pianificata quanto prima possibile, ma la pianificazione la esegue solo dopo che il codice corrente è completo.

Quindi la funzione viene pianificata per avviarsi "subito dopo" il codice corrente.

Per esempio, questo produce "Ciao" quindi, immediatamente, "Mondo":

```js
setTimeout(() => alert("Mondo"));

alert("Ciao");
```

La prima linea "mette in calendario" la chiamata dopo 0ms, ma la pianificazione "verifica il calendario" solo dopo che il codice corrente è completo, quindi `"Ciao"` viene per primo, seguito da `"Mondo"`.

Ci sono anche casi di utilizzo avanzato relativi ai browser del timeout zero-delay, li discuteremo nel capitolo [Event loop: microtasks e macrotasks](/javascript/tutorial/event-loop).


:::: tip Zero-delay in effetti non è zero (in un browser)
In un browser c'è un limite a quanto spesso possono essere avviati i timer nidificati. L'[HTML5 standard](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html#timers) dice: "dopo cinque timer nidificati, l'intervallo è costretto a essere di almeno 4 millisecondi".

Vediamo cosa significa con l'esempio qui sotto. La chiamata `setTimeout` riprogramma se stessa con zero-delay. Ogni chiamata ricorda il tempo reale dall'esecuzione precedente nell'array `tempi`. Come sono realmente i ritardi? Vediamo:

```js
let partenza = Date.now();
let tempi = [];

setTimeout(function avvia() {
  tempi.push(Date.now() - partenza); // ricorda il ritardo dalla chiamata precedente

  if (partenza + 100 < Date.now()) alert(tempi); // mostra i ritardi dopo 100ms
  else setTimeout(avvia); // allora riprogramma
});

// un esempio del risultato:
// 1,1,1,1,9,15,20,24,30,35,40,45,50,55,59,64,70,75,80,85,90,95,100
```

I primi timer vengono eseguiti immediatamente (come scritto nelle specifiche), poi vediamo `9, 15, 20, 24...` Entra in gioco il ritardo obbligatorio di 4+ ms fra le esecuzioni.

Una cosa simile accade se usiamo `setInterval` invece di `setTimeout`: `setInterval(f)` esegue `f` alcune volte con zero-delay, dopo di che con 4+ ms di ritardo.

Questo limite viene da tempi remoti e molti script vi si affidano, quindi esiste per ragioni storiche.

Per JavaScript lato server, questo limite non esiste e ci sono altri metodi per pianificare un lavoro asincrono immediato, come [setImmediate](https://nodejs.org/api/timers.html) per Node.js. Quindi questa nota è specifica per i browser.
::::

## Riepilogo

- I metodi `setInterval(func, ritardo, ...arg)` e `setTimeout(func, ritardo, ...arg)` consentono di avviare la `func` regolarmente/una volta dopo `ritardo` millisecondi.
- Per disattivare l'esecuzione, dovremo chiamare `clearInterval/clearTimeout` con il valore restituito da `setInterval/setTimeout`.
- La chiamata nidificata di `setTimeout` è un'alternativa più flessibile a `setInterval`, permettendo di impostare in modo più preciso l'intervallo di tempo *tra*  le esecuzioni.
- Zero-delay si pianifica con `setTimeout(func, 0)` (lo stesso di `setTimeout(func)`) ed è usato per pianificare la chiamata "quanto prima possibile, ma dopo che il codice corrente è completo".
- Il browser limita il ritardo minimo per cinque o più chiamate nidificate di `setTimeout` o `setInterval` (dopo la 5a chiamata) a 4ms. Ciò accade per ragioni storiche.

Da notare che tutti i metodi di pianificazione non *garantiscono* un ritardo preciso.

Per esempio, il timer nel browser può rallentare per molte ragioni:
- La CPU è sovraccarica.
- La scheda del browser è sullo sfondo.
- Il portatile ha la batteria scarica.

Tutto ciò può aumentare l'esecuzione minima del timer (il ritardo minimo) di 300ms o anche 1000ms a seconda del browser e le impostazioni di prestazione a livello dell'OS.

## Esercizi

### 1 · Output ogni secondo

Scrivi una funzione `stampaNumeri(da, a)` che produca un numero ogni secondo, partendo da `da` e finendo con `a`.

Crea due varianti della soluzione.

1. Usando `setInterval`.
2. Usando `setTimeout` ricorsivo.

::::: details Soluzione

Usando `setInterval`:

```js
function stampaNumeri(da, a) {
  let attuale = da;

  let timerId = setInterval(function() {
    alert(attuale);
    if (attuale == a) {
      clearInterval(timerId);
    }
    attuale++;
  }, 1000);
}

// utilizzo:
stampaNumeri(5, 10);
```

Usando `setTimeout` ricorsivo:


```js
function stampaNumeri(da, a) {
  let attuale = da;

  setTimeout(function vai() {
    alert(attuale);
    if (attuale < a) {
      setTimeout(vai, 1000);
    }
    attuale++;
  }, 1000);
}

// utilizzo:
stampaNumeri(5, 10);
```

Nota che in entrambe le soluzioni c'è un ritardo iniziale prima del primo output. La funzione viene eseguita la prima volta dopo `1000ms`.

Se vogliamo che la funzione venga eseguita subito, possiamo aggiugere una chiamata addizionale su di una linea separata, come questa:

```js
function stampaNumeri(da, a) {
  let attuale = da;

  function vai() {
    alert(attule);
    if (attuale == a) {
      clearInterval(timerId);
    }
    attuale++;
  }


  vai();

  let timerId = setInterval(vai, 1000);
}

stampaNumeri(5, 10);
```

:::::

### 2 · Cosa mostrerà setTimeout?

Nel codice qui sotto è pianificata una chiamata con `setTimeout`, poi viene eseguito un calcolo pesante, che richiede più di 100ms per essere completato.

Quando verrà eseguita la funzione pianificata?

1. Dopo il loop.
2. Prima del loop.
3. All'inizio del loop.


Cosa mostrerà l'`alert`?

```js
let i = 0;

setTimeout(() => alert(i), 100); // ?

// ipotizza che il tempo necessario a eseguire questa funzione sia >100ms
for(let j = 0; j < 100000000; j++) {
  i++; 
}
```

::::: details Soluzione

Ogni `setTimeout` verrà eseguito solo dopo che il codice corrente è completo.

La `i` sarà l'ultimo: `100000000`.

```js
let i = 0;

setTimeout(() => alert(i), 100); // 100000000

// ipotizza che il tempo necessario a eseguire questa funzione sia >100ms
for(let j = 0; j < 100000000; j++) {
  i++; 
}
```

:::::

