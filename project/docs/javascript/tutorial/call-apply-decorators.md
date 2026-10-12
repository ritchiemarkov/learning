---
title: "*Decorators* e forwarding, call/apply"
description: "JavaScript.info in italiano: *Decorators* e forwarding, call/apply"
sourceTutorial: true
prev: {"text": "Pianificazione: setTimeout e setInterval", "link": "/javascript/tutorial/settimeout-setinterval"}
next: {"text": "Function binding", "link": "/javascript/tutorial/bind"}
---

# *Decorators* e forwarding, call/apply

> **JavaScript.info · Ilya Kantor e contributori.** [Originale inglese](https://javascript.info/call-apply-decorators) · [Edizione italiana](https://it.javascript.info/call-apply-decorators) · [Fonti e licenza](/javascript/fonti).

JavaScript offre una flessibilità eccezionale quando si tratta di funzioni. Possono essere passate, usate come oggetti, ed ora vedremo come inoltrarle (*forward*) e decorarle (*decorate*).

## Caching trasparente

Immaginiamo di avere una funzione `slow(x)` che richiede alla CPU molte risorse, ma i suoi risultati sono stabili. In altre parole, per lo stesso valore di `x` ritorna sempre il medesimo risultato.

Se la funzione viene chiamata spesso, potremmo voler memorizzare nella cache (ricordare) i risultati, per evitare di dedicare tempo extra nel ripetere gli stessi calcoli.

Ma invece di aggiungere quella funzionalità in `slow ()`, andremo a creare una funzione *wrapper* (che incapsula o avvolge), che aggiunge il caching. Come vedremo, ci sono molti vantaggi in questo metodo.

Ecco il codice e la sua descrizione:

```js
function slow(x) {
  // qui può esserci un duro lavoro per la CPU
  alert(`Called with ${x}`);
  return x;
}

function cachingDecorator(func) {
  let cache = new Map();

  return function(x) {
    if (cache.has(x)) {    // se questa chiave è già presente in cache
      return cache.get(x); // leggi il risultato
    }

    let result = func(x);  // altrimenti chiama func

    cache.set(x, result);  // e metti in cache (memorizza) il risultato
    return result;
  };
}

slow = cachingDecorator(slow);

alert( slow(1) ); // slow(1) viene messo in cache
alert( "Again: " + slow(1) ); // lo stesso

alert( slow(2) ); // slow(2) viene messo in cache
alert( "Again: " + slow(2) ); // lo stesso della linea precedente
```

Nel codice precedente `cachingDecorator` è un *decorator*: una speciale funzione che prende come argomento un'altra funzione e ne altera il comportamento.

L'idea è quella di poter chiamare `cachingDecorator` con qualsiasi funzione per applicare la funzionalità di *caching*. È fantastico, perché in questo modo possiamo avere molte funzioni che utilizzano tale caratteristica, e tutto ciò che dobbiamo fare è applicare ad esse `cachingDecorator`.

Separando la funzionalità di caching dalla funzione principale abbiamo anche il vantaggio di mantenere il codice semplice.

Il risultato di `cachingDecorator(func)` è un "involucro" (*wrapper*): `function(x)` che "incapsula" (*wraps*) la chiamata di `func(x)` nella logica di caching:

![](/javascript-info/1-js/06-advanced-functions/09-call-apply-decorators/decorator-makecaching-wrapper.svg)

Per un codice esterno, la funzione "incapsulata" `slow` continua a fare la stessa cosa. Ma, in aggiunta al suo comportamento, ha ricevuto la funzionalità di caching.

Per riassumere, ci sono diversi vantaggi nell'usare separatamente `cachingDecorator` invece di modificare direttamente il codice di` slow`:

- Il *decorator* `cachingDecorator` è riutilizzabile, possiamo applicarlo ad altre funzioni.
- La logica di cache è separata, non aumenta la complessità della funzione `slow`.
- In caso di bisogno possiamo combinare *decorators* multipli (come vedremo più avanti).

## Utilizzo di "func.call" per il contesto

Il *decorator* con funzione di caching menzionato prima, non è adatto a lavorare con i metodi degli oggetti.

Ad esempio, nel codice seguente, `worker.slow()` smette di funzionare dopo la *decoration*:

```js
// prepariamo worker.slow per essere messo in cache
let worker = {
  someMethod() {
    return 1;
  },

  slow(x) {
    // compito terribilmente impegnativo per la CPU
    alert("Called with " + x);
    return x * this.someMethod(); // (*)
  }
};

// stesso codice di prima
function cachingDecorator(func) {
  let cache = new Map();
  return function(x) {
    if (cache.has(x)) {
      return cache.get(x);
    }

    let result = func(x); // (**)

    cache.set(x, result);
    return result;
  };
}

alert( worker.slow(1) ); // il metodo originale funziona

worker.slow = cachingDecorator(worker.slow); // ora mettiamolo in cache


alert( worker.slow(2) ); // Errore! Error: Cannot read property 'someMethod' of undefined

```

L'errore avviene alla linea `(*)` la quale cerca di accedere a `this.someMethod`, ma fallisce. Riesci a capire il motivo?

Il motivo è che il *wrapper* chiama la funzione originale come `func(x)` alla linea `(**)`. E, quando chiamata in questo modo, la funzione prende `this = undefined`.

Osserveremmo la stessa cosa se provassimo a eseguire:

```js
let func = worker.slow;
func(2);
```

Quindi, il *wrapper* passa la chiamata al metodo originale, ma senza il contesto `this`. Da qui l'errore.

Correggiamolo.

C'è uno speciale metodo di funzione integrato [func.call(context, ...args)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/call) che permette di chiamare una funzione impostando esplicitamente `this`.

La sintassi è:

```js
func.call(context, arg1, arg2, ...)
```

Esegue `func` passando `this` come primo argomento ed i successivi come normali argomenti.

In poche parole, queste due chiamate fanno praticamente la stessa cosa:
```js
func(1, 2, 3);
func.call(obj, 1, 2, 3)
```

Entrambe chiamano `func` con gli argomenti `1`, `2` e `3`. L'unica differenza è che `func.call` imposta anche `this` su `obj`.

Prendiamo il codice sottostante come esempio, chiamiamo `sayHi` usando il contesto di oggetti differenti: `sayHi.call(user)` invoca `sayHi` passando `this=user`, e nella linea seguente imposta `this=admin`:

```js
function sayHi() {
  alert(this.name);
}

let user = { name: "John" };
let admin = { name: "Admin" };

// usiamo call per passare oggetti differenti come "this"
sayHi.call( user ); // John
sayHi.call( admin ); // Admin
```

Qui, invece, usiamo `call` per chiamare `say` passando il contesto e l'argomento frase:


```js
function say(frase) {
  alert(this.name + ': ' + frase);
}

let user = { name: "John" };

// user diventa this e "Hello" diventa il primo argomento (frase)
say.call( user, "Hello" ); // John: Hello
```

Nel nostro caso possiamo usare `call` nel *wrapper* per passare il contesto alla funzione originale:

```js
let worker = {
  someMethod() {
    return 1;
  },

  slow(x) {
    alert("Called with " + x);
    return x * this.someMethod(); // (*)
  }
};

function cachingDecorator(func) {
  let cache = new Map();
  return function(x) {
    if (cache.has(x)) {
      return cache.get(x);
    }

    let result = func.call(this, x); // ora "this" è passato nel modo corretto

    cache.set(x, result);
    return result;
  };
}

worker.slow = cachingDecorator(worker.slow); // ora abilitiamo il caching

alert( worker.slow(2) ); // funziona
alert( worker.slow(2) ); // funziona, non viene chiamato l'originale dalla cache
```

Ora funziona tutto correttamente.

Per renderlo ancora più chiaro, vediamo più approfonditamente come viene passato `this`:

1. Dopo la *decoration* `worker.slow` diventa il *wrapper* `function (x) { ... }`.
2. Quindi quando viene eseguito `worker.slow(2)`, il *wrapper* prende `2` come argomento e `this=worker` (è l'oggetto prima del punto).
3. All'interno del *wrapper*, assumendo che il risultato non sia stato ancora messo in cache, `func.call(this, x)` passa `this` (`=worker`) e l'argomento (`=2`) al metodo originale.

## Passando argomenti multipli

Rendiamo `cachingDecorator` un po' più universale. Finora abbiamo lavorato solamente con funzioni con un solo argomento.

Come fare per gestire il caching del metodo con argomenti multipli `worker.slow`?

```js
let worker = {
  slow(min, max) {
    return min + max; // il solito processo terribilmente assetato di CPU
  }
};

// dovrebbe ricordare le chiamate con lo stesso argomento
worker.slow = cachingDecorator(worker.slow);
```
Precedentemente, con un singolo argomento `x` potevamo usare `cache.set(x, result)` per salvare il risultato, e `cache.get(x)` per richiamarlo. Ma ora abbiamo bisogno di memorizzare il risultato per più combinazioni di argomenti `(min,max)`, e il comando `Map` prende un solo argomento come chiave.

Sono possibili diverse soluzioni:

1. Implementare una nuova (o usarne una di terze parti) struttura simile a *map*, ma più versatile e che permetta chiavi multiple.
2. Usare *maps* annidate: `cache.set(min)` sarà un `Map` che conterrà le coppie `(max, result)`. Quindi potremo avere `result` come `cache.get(min).get(max)`.
3. Unire i due valori in uno. Nel nostro caso potemmo usare una semplice stringa `"min,max"` come chiave del `Map`. 
Per maggiore flessibilità potremmo dotare il decorator di una funzione di *hashing*, che sappia trasformare più valori in uno solo.

Per molte applicazioni pratiche, la terza soluzione è sufficiente, quindi ci atterremo ad essa.

Non abbiamo bisogno di passare solo `x`, ma anche gli altri argomenti in `func.call`.  
Ricordiamo che in una `function()` sono disponibili tutti i suoi argomenti tramite il *pseudo-array* `arguments`. Quindi `func.call(this, x)` può essere sostituito con `func.call(this, ...arguments)`.

Il seguente è `cachingDecorator` migliorato:

```js
let worker = {
  slow(min, max) {
    alert(`Called with ${min},${max}`);
    return min + max;
  }
};

function cachingDecorator(func, hash) {
  let cache = new Map();
  return function() {

    let key = hash(arguments); // (*)

    if (cache.has(key)) {
      return cache.get(key);
    }


    let result = func.call(this, ...arguments); // (**)


    cache.set(key, result);
    return result;
  };
}

function hash(args) {
  return args[0] + ',' + args[1];
}

worker.slow = cachingDecorator(worker.slow, hash);

alert( worker.slow(3, 5) ); // funziona
alert( "Again " + worker.slow(3, 5) ); // anche qui funziona (dalla cache)
```

Ora funziona con qualsiasi numero di argomenti (anche la funzione hash dovrebbe essere sistemata per consentire un numero qualsiasi di argomenti. Un modo interessante per farlo sarà trattato di seguito).

Ci sono due cambiamenti:

- Nella linea `(*)` viene chiamato `hash` per creare una chiave unica da `arguments`. In questo caso abbiamo usato una semplice funzione di unione che trasforma gli argomenti `(3, 5)` nella chiave `"3,5"`. Casi più complessi potrebbero richiedere approcci differenti per la funzione di *hashing*.
- Successivamente `(**)` usa `func.call(this, ...arguments)` per passare alla funzione originale sia il contesto che tutti gli argomenti ricevuti dal *wrapper*.

## func.apply

Anziché `func.call(this, ...arguments)` potremmo usare `func.apply(this, arguments)`.

La sintassi del metodo [func.apply](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/apply) è:

```js
func.apply(context, args)
```

Questo esegue `func` impostando `this=context` ed usando l'oggetto (simil-array) `args` come lista di argomenti.

L'unica differenza di sintassi tra `call` e` apply` è che `call` si aspetta una lista di argomenti, mentre` apply` vuole un oggetto simil-array.

Queste due chiamate sono praticamente identiche:

```js
func.call(context, ...args); // passa un array come lista, usando la sintassi spread
func.apply(context, args);   // è uguale all'uso di call
```

Eseguono la medesima chiamata a `func` con un dati contesto ed argomenti.

C'è solo una sottile differenza:

- La sintassi `...` permette di passare `args` *iterabili* come lista a `call`.
- `apply` accetta solo *simil-array* `args`.

Quindi, se ci aspettiamo un iterabile usiamo `call`, se invece ci aspettiamo un array, usiamo ` apply`.

E per oggetti che sono sia iterabili che simil-array, come un vero array, possiamo usarne uno qualsiasi, ma `apply` sarà probabilmente più veloce, perché è meglio ottimizzato nella maggior parte dei motori JavaScript.

Il passaggio di tutti gli argomenti insieme al contesto a un'altra funzione è chiamato *call forwarding* (inoltro di chiamata).

Questa è la sua forma più semplice:

```js
let wrapper = function() {
  return func.apply(this, arguments);
};
```

Quando un codice esterno chiama il `wrapper`, è indistinguibile dalla chiamata della funzione originale `func`.


## Prendere in prestito un metodo
Ora facciamo un ulteriore piccolo miglioramento nella funzione di hashing:

```js
function hash(args) {
  return args[0] + ',' + args[1];
}
```

Per ora funziona solo su due argomenti. Sarebbe meglio se potesse unire un numero qualsiasi di `args`.

La soluzione più immediata sarebbe usare il metodo [arr.join](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/join):

```js
function hash(args) {
  return args.join();
}
```

...Sfortunatamente non funziona, perché stiamo chiamando `hash(arguments)`, e l'oggetto `arguments` è sia iterabile che simil-array, ma non è un vero array.

Quindi chiamare `join` su di esso darebbe errore, come possiamo vedere di seguito:

```js
function hash() {

  alert( arguments.join() ); // Error: arguments.join is not a function

}

hash(1, 2);
```

Tuttavia, c'è un modo semplice per utilizzare il metodo `join`:

```js
function hash() {

  alert( [].join.call(arguments) ); // 1,2

}

hash(1, 2);
```

Il trucco è chiamato *method borrowing*.

Prendiamo (in prestito) il metodo `join` da un normale array (`[].join`) ed usiamo `[].join.call` per eseguirlo nel contesto di `arguments`.

Perché funziona?

Perché l'algoritmo interno del metodo nativo `arr.join(glue)` è molto semplice.

Preso quasi letteralmente dalla specifica:

1. Imposta `glue` come primo argomento, o, se non ci sono argomenti, una virgola `","`.
2. Imposta `result` come stringa vuota.
3. Aggiungi `this[0]` a `result`.
4. Aggiungi `glue` e `this[1]`.
5. Aggiungi `glue` e `this[2]`.
6. ...Continua fino a che `this.length` elementi sono stati "incollati".
7. Ritorna `result`.


Quindi, tecnicamente prende `this` ed unisce `this[0]`, `this[1]` ...ecc. E' scritto intenzionalmente in modo da permette l'uso di un simil-array come `this` (non è una coincidenza se molti metodi seguono questa pratica). E' per questo motivo che funziona anche con `this=arguments`.

## Decorators e proprietà di funzione

In genere è sicuro sostituire una funzione o un metodo con una sua versione "decorata", tranne per una piccola cosa. Se la funzione originale aveva proprietà associate, come `func.calledCount` o qualsiasi altra cosa, allora quella decorata non le fornirà. Perché quello è un *wrapper*, quindi bisogna stare attenti a come lo si usa.

Es. nell'esempio sopra, se la funzione `slow` avesse avuto delle proprietà, allora `cachingDecorator(slow)` sarebbe stato un *wrapper* senza di esse.

Alcuni *decorators* possono fornire le proprie proprietà. Per esempio, un *decorator* può contare quante volte una funzione è stata invocata e quanto tempo ha impiegato, ed esporre queste informazioni tramite le proprietà del *wrapper*.

Esiste un modo per creare *decorators* che mantengono l'accesso alle proprietà della funzione, ma questo richiede l'uso di uno speciale oggetto `Proxy` per racchiudere una funzione. Ne parleremo più avanti nell'articolo [Proxy e Reflect](/javascript/tutorial/proxy).

## Riepilogo

*Decorator* è un *wrapper* attorno a una funzione che ne altera il comportamento. Il compito principale è ancora svolto dalla funzione.

I *decorators* possono essere visti come "caratteristiche" o "aspetti" che possono essere aggiunti a una funzione. Possiamo aggiungerne uno o aggiungerne molti. E tutto questo senza cambiarne il codice!

Per implementare `cachingDecorator`, abbiamo studiato i metodi:

- [func.call(context, arg1, arg2...)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/call) -- chiama `func` con un dato contesto ed argomenti.
- [func.apply(context, args)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/apply) -- chiama `func` passando `context` come `this` ed un simil-array `args` come lista di argomenti.

Generalmente il *call forwarding* viene eseguito usando `apply`:

```js
let wrapper = function() {
  return original.apply(this, arguments);
};
```

Abbiamo anche visto un esempio di *method borrowing*, quando prendiamo un metodo da un oggetto ed usiamo `call` per chiamarlo nel contesto di un altro oggetto. È abbastanza comune prendere metodi array e applicarli ad `argomenti`. L'alternativa è utilizzare l'oggetto parametri `...rest` che è un vero array.

Esisto molti usi dei *decorators*, vediamone alcuni risolvendo i tasks di questo capitolo.

## Esercizi

### 1 · decorator spia

Crea un decorator `spy(func)` che restituisca un wrapper che salva tutte le chiamate alla funzione nella sua proprietà `calls`.

Ogni chiamata viene salvata come un array di argomenti.

Ad esempio:

```js
function work(a, b) {
  alert( a + b ); // work è una funzione o un metodo arbitrario
}


work = spy(work);


work(1, 2); // 3
work(4, 5); // 9

for (let args of work.calls) {
  alert( 'call:' + args.join() ); // "call:1,2", "call:4,5"
}
```

P.S. Questo decorator a volte è utile per fare *unit-testing*. La sua forma avanzata è `sinon.spy` nella libreria [Sinon.JS](http://sinonjs.org/).

::::: details Soluzione

Il wrapper restituito da `spy (f)` dovrebbe memorizzare tutti gli argomenti e quindi usare `f.apply` per inoltrare la chiamata.

:::::

### 2 · decorator ritardante

Crea il decorator `delay(f, ms)` che ritarda ogni chiamata ad `f` di `ms` millisecondi.

Ad esempio:

```js
function f(x) {
  alert(x);
}

// crea i wrappers
let f1000 = delay(f, 1000);
let f1500 = delay(f, 1500);

f1000("test"); // visualizza "test" dopo 1000ms
f1500("test"); // visualizza "test" dopo 1500ms
```

In altre parole, `delay(f, ms)` ritorna una variante di `f` ritardata di `ms`.

Nel codice sopra, `f` è una funzione con un solo argomento, ma la tua soluzione potrebbe passare molti argomenti ed il contesto `this`.

::::: details Soluzione

La soluzione:

```js
function delay(f, ms) {

  return function() {
    setTimeout(() => f.apply(this, arguments), ms);
  };

}

let f1000 = delay(alert, 1000);

f1000("test"); // mostra "test" dopo 1000ms
```

Qui, nota come viene utilizzata un arrow function. come sappiamo le arrow functions non hanno un proprio `this` nè `arguments`, quindi `f.apply(this, arguments)` prende `this` e `arguments` dal wrapper.

Se passassimo una funzione regolare, `setTimeout` la chiamerebbe senza argomenti e` this = window` (supponendo essere in un browser). 

Possiamo anche passare il `this` corretto usando una variabile intermedia, ma è un po' più complicato:

```js
function delay(f, ms) {

  return function(...args) {
    let savedThis = this; // memorizzalo in una variabile intermedia
    setTimeout(function() {
      f.apply(savedThis, args); // usalo qui
    }, ms);
  };

}
```

:::::

### 3 · Debounce decorator

Il risultato del decorator `debounce(f, ms)` è un wrapper che sospende le chiamate a `f` finché non ci sono `ms` millisecondi di inattività (nessuna chiamata, "periodo di *cooldown*"), quindi invoca `f` una volta, con gli ultimi argomenti.

In altre parole, `debounce` è come una segretaria che riceve "telefonate" e aspetta finché non ci sono `ms` di silenzio. Solo allora trasferisce le informazioni sull'ultima chiamata al "capo" (chiama effettivamente `f`).

Ad esempio, avevamo una funzione `f` e l'abbiamo sostituita con `f = debounce(f, 1000)`.

Se la funzione incapsulata viene chiamata a 0 ms, 200 ms e 500 ms, e quindi non ci sono chiamate, la `f` effettiva verrà chiamata solo una volta, a 1500 ms. Cioè dopo il periodo di *cooldown* di 1000 ms dall'ultima chiamata.

![](/javascript-info/1-js/06-advanced-functions/09-call-apply-decorators/03-debounce/debounce.svg)

... E riceverà gli argomenti dell'ultima chiamata, tutte le altre chiamate vengono ignorate.

Ecco il codice, (usa il *debounce decorator* dalla [Libreria Lodash](https://lodash.com/docs/4.17.15#debounce)):

```js
let f = _.debounce(alert, 1000);

f("a");
setTimeout( () => f("b"), 200);
setTimeout( () => f("c"), 500);
// la funzione di debounced attende 1000ms dopo l'ultima chiamata, quini esegue: alert("c")
```

Ora un esempio pratico. Diciamo che l'utente digita qualcosa, e vorremmo inviare una richiesta al server quando l'input è finito.

Non ha senso inviare la richiesta per ogni carattere digitato. Vorremmo invece aspettare, e poi elaborare l'intero risultato.

In un browser web, possiamo impostare un gestore di eventi -- una funzione che viene chiamata ad ogni modifica di un campo di input. Normalmente, un gestore di eventi viene chiamato molto spesso, per ogni tasto digitato. Ma se utilizziamo un `debounce` di 1000 ms, verrà chiamato solo una volta, dopo 1000 ms dopo l'ultimo input.


> [Esempio interattivo nell’articolo originale](https://it.javascript.info/call-apply-decorators).


Quindi, `debounce` è un ottimo modo per elaborare una sequenza di eventi: che si tratti di una sequenza di pressioni di tasti, movimenti del mouse o qualsiasi altra cosa.

Aspetta il tempo specificato dopo l'ultima chiamata, quindi esegue la sua funzione, che può elaborare il risultato.

Il compito è implementare il decorator `debounce`.

Suggerimento: sono solo poche righe se ci pensi :)

::::: details Soluzione

```js
function debounce(func, ms) {
  let timeout;
  return function() {
    clearTimeout(timeout);
    timeout = setTimeout(() => func.apply(this, arguments), ms);
  };
}

```

Una chiamata a `debounce` restituisce un wrapper. Quando viene chiamato, pianifica la chiamata della funzione originale dopo tot `ms` e annulla il precedente timeout.

:::::

### 4 · Throttle decorator

Creare un "throttling" decorator `throttle(f, ms)` -- che ritorna un wrapper.

Quando viene chiamato più volte, passa la chiamata a `f` al massimo una volta ogni `ms` millisecondi.

Rispetto al *debounce decorator* abbiamo un decorator completamente diverso:
- `debounce` esegue la funzione una volta, dopo il periodo di "cooldown". Valido per processare il risultato finale.
- `throttle` la esegue non più spesso dell'intervallo di tempo `ms`. Valido per aggiornamenti regolari ma non troppo frequenti.

In altre parole, `throttle` è come una segretaria che accetta telefonate, ma le passa al capo (chiama `f`) non più di una volta ogni `ms` millisecondi.

Vediamo l'applicazione nella vita reale, per capire meglio tale esigenza e per vedere da dove nasce.

**Ad esempio, vogliamo tenere traccia dei movimenti del mouse.**

In un browser possiamo impostare una funzione da eseguire ad ogni movimento del mouse, e ottenere la posizione del puntatore mentre si sposta. Durante un utilizzo attivo del mouse, questa funzione di solito viene eseguita molto frequentemente, può essere qualcosa come 100 volte al secondo (ogni 10 ms).

**Vorremmo aggiornare alcune informazioni sulla pagina web quando il puntatore si sposta.**

... Ma l'aggiornamento della funzione `update()` è troppo pesante per farlo ad ogni micro-movimento. Inoltre, non ha senso aggiornare più spesso di una volta ogni 100 ms.

Quindi la andremo ad inserire nel decorator, usando `throttle(update, 100)` come funzione da eseguire ad ogni movimento del mouse, invece dell'originale `update()`. Il decorator verrà chiamato spesso, ma inoltrerà la chiamata a `update()` al massimo una volta ogni 100 ms.

Visivamente, sarà simile a questo:

1. Per il primo movimento del mouse la variante *decorata* passa immediatamente la chiamata ad `update`. Questo è importante, l'utente vede immediatamente una reazione al suo movimento.
2. Successivamente, per i movimenti del mouse entro lo scadere di `100ms`, non accade nulla. La variante decorata ignora le chiamate.
3. Allo scadere dei `100ms` viene chiamato un ulteriore `update` con le ultime coordinate.
4. Infine, il mouse si ferma da qualche parte. La variante decorata attende la scadenza dei `100ms` e poi esegue `update` con le ultime coordinate. Quindi, cosa abbastanza importante, vengono elaborate le coordinate finali del mouse.

Un esempio del codice:

```js
function f(a) {
  console.log(a);
}

// f1000 passa ad f un massimo di una chiamata ogni 1000 ms
let f1000 = throttle(f, 1000);

f1000(1); // visualizza 1
f1000(2); // (throttling, 1000ms non ancora scaduti)
f1000(3); // (throttling, 1000ms non ancora scaduti)

// allo scadere dei 1000 ms...
// ...visualizza 3, il valore intermedio 2 viene ignorato
```

P.S. Gli argomenti e il contesto `this` passati a `f1000` dovrebbero essere passati alla funzione `f` originale.

::::: details Soluzione

```js
function throttle(func, ms) {

  let isThrottled = false,
    savedArgs,
    savedThis;

  function wrapper() {

    if (isThrottled) { // (2)
      savedArgs = arguments;
      savedThis = this;
      return;
    }
    isThrottled = true;

    func.apply(this, arguments); // (1)

    setTimeout(function() {
      isThrottled = false; // (3)
      if (savedArgs) {
        wrapper.apply(savedThis, savedArgs);
        savedArgs = savedThis = null;
      }
    }, ms);
  }

  return wrapper;
}
```

La chiamata a `throttle(func, ms)` ritorna `wrapper`.

1. Durante la prima chiamata, il `wrapper` semplicemente esegue `func` ed imposta lo stato cooldown (`isThrottled = true`).
2. In questo stato, tutte le chiamate vengono memorizzate in `savedArgs/savedThis`. Va notato che sia il contesto che gli argomenti sono ugualmente importanti e dovrebbero essere memorizzati. Ne abbiamo bisogno contemporaneamente per riprodurre la chiamata.
3. Dopo che sono passati `ms` millisecondi, `setTimeout` scatta. Lo stato cooldown viene rimosso (`isThrottled = false`) e, nel caso fossero state ignorate delle chiamate, `wrapper` viene eseguito con gli ultimi argomenti e contesto memorizzati.

Il terzo passaggio non esegue `func`, ma `wrapper`, perché non abbiamo bisogno solo di eseguire `func`, ma anche di impostare nuovamente lo stato di cooldown ed il timeout per resettarlo.

:::::

