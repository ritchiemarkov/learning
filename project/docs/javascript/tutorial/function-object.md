---
title: "Oggetto funzione, NFE"
description: "JavaScript.info in italiano: Oggetto funzione, NFE"
sourceTutorial: true
prev: {"text": "Oggetto globale", "link": "/javascript/tutorial/global-object"}
next: {"text": "La sintassi \"new Function\"", "link": "/javascript/tutorial/new-function"}
---

# Oggetto funzione, NFE

> **JavaScript.info · Ilya Kantor e contributori.** [Originale inglese](https://javascript.info/function-object) · [Edizione italiana](https://it.javascript.info/function-object) · [Fonti e licenza](/javascript/fonti).

Come già sappiamo, in JavaScript le funzioni sono valori.

Inoltre ogni valore ha un tipo. Di che tipo è una funzione?

In JavaScript, le funzioni sono oggetti.

Un ottimo modo per pensare alle funzioni è quello di immaginarle come "oggetti attivi" (che compiono azioni). Oltre a invocarli, possiamo trattarli come veri e propri oggetti: aggiungendo/rimuovendo proprietà, passarli per riferimento.


## La proprietà "name" 

Gli oggetti funzione contengono alcune proprietà utili.

Ad esempio, il nome di una funzione è accessible tramite la proprietà "name":

```js
function sayHi() {
  alert("Hi");
}

alert(sayHi.name); // sayHi
```

Inoltre l'assegnazione della proprietà `name` è intelligente. Funziona anche se dichiariamo la funzione per assegnazione ad una variabile:

```js
let sayHi = function() {
  alert("Hi");
};

alert(sayHi.name); // sayHi (funziona!)
```

Funziona anche nel caso in cui l'assegnazione viene effettuata come valore di default:

```js
function f(sayHi = function() {}) {
  alert(sayHi.name); // sayHi (funziona!)
}

f();
```

Nelle specifiche, questa caratteristica viene chiamata "contextual name" ("nome prelevato dal contesto"). Se la funzione non ne fornisce uno, allora durante l'assegnazione questo viene ricavato dal contesto.

Anche i metodi dell'oggetto possiedono la proprietà `name`:

```js
let user = {

  sayHi() {
    // ...
  },

  sayBye: function() {
    // ...
  }

}

alert(user.sayHi.name); // sayHi
alert(user.sayBye.name); // sayBye
```

Non sta accadendo nulla di magico. Anche se ci sono dei casi in cui non c'è alcun modo di ricavare il nome dal contesto. In questi casi, la proprietà `name` sarà vuota, come nell'esempio:

```js
// funzione creata all'interno dell'array
let arr = [function() {}];

alert( arr[0].name ); // <stringa vuota>
// il motore non ha alcun modo di ricavare il nome corretto, per questo sarà vuoto
```

Nella pratica però, la maggior parte delle funzioni possiedono un nome.

## La proprietà "length" 

Esiste un'altra proprietà molto utile, "length" che ritorna il numero di parametri della funzione, ad esempio:

```js
function f1(a) {}
function f2(a, b) {}
function many(a, b, ...more) {}

alert(f1.length); // 1
alert(f2.length); // 2
alert(many.length); // 2
```

Da questo esempio possiamo notare che i parametri di resto non vengono contati.

La proprietà `length` viene spesso utilizzata per ispezionare un funzione che opera su altre funzioni.

Ad esempio, nel codice sotto la funzione `ask` accetta una `question` da porre, e un numero arbitrario di `handler` (gestori) da invocare.

Una volta che l'utente ha fornito la risposta, la funzione invoca gli handlers. Possiamo fornire due tipi di handlers:

- Una funzione con zero argomenti, che viene in invocata solamente nel caso in cui l'utente fornisca una risposta positiva.
- Una funzione con argomenti, che viene invocata in entrambi i casi e ritorna una risposta.

L'idea è quella di avere un semplice handles senza argomenti, per gestire i casi positivi (la variante più frequente), ma siamo comunque in grado di fornire un gestore universale.

Per invocare `handlers` nel modo corretto, esaminiamo la proprietà `length`:

```js
function ask(question, ...handlers) {
  let isYes = confirm(question);

  for(let handler of handlers) {
    if (handler.length == 0) {
      if (isYes) handler();
    } else {
      handler(isYes);
    }
  }

}

// per risposte positive, entrambi gli handler vengono chiamati
// per le risposte negative, solamente la seconda
ask("Question?", () => alert('You said yes'), result => alert(result));
```

Questo è un caso particolare di quello che viene chiamato [polimorfismo](https://en.wikipedia.org/wiki/Polymorphism_(computer_science)) -- trattare gli argomenti in maniera differente in base al loro tipo, o nel nostro caso in base a `length`. Quest'idea ha delle utili applicazioni nelle librerie JavaScript.

## Proprietà aggiuntive

Possiamo anche aggiungere delle proprietà.

In questo esempio aggiungiamo la proprietà `counter` per tenere traccia delle chiamate totali:

```js
function sayHi() {
  alert("Hi");

  
  // andiamo a contare quante volte verrà invocata
  sayHi.counter++;
  
}
sayHi.counter = 0; // valore iniziale

sayHi(); // Hi
sayHi(); // Hi

alert( `Called ${sayHi.counter} times` ); // Chiamata 2 volte
```


::: warning Una proprietà non è una variabile
Una proprietà assegnata ad una funzione, come `sayHi.counter = 0` non definisce una variabile locale `counter`. In altre parole, una proprietà `counter` ed una variabile `let counter` sono due cose separate.

Possiamo quindi trattare una funzione come un oggetto, memorizzare proprietà, ma non avranno alcun effetto sull'esecuzione. Le variabili non utilizzano mai le proprietà della funzione e vice versa. Sono come due mondi paralleli.
:::

Le proprietà delle funzioni possono rimpiazzare le closure in alcun casi. Ad esempio, possiamo riscrivere la funzione contatore del capitolo [Variable scope, closure](/javascript/tutorial/closure) sfruttando una proprietà della funzione:

```js
function makeCounter() {
  // piuttosto di:
  // let count = 0

  function counter() {
    return counter.count++;
  };

  counter.count = 0;

  return counter;
}

let counter = makeCounter();
alert( counter() ); // 0
alert( counter() ); // 1
```

Ora `count` viene memorizzato direttamente nella funzione, non nel Lexical Environment esterno.

Questa soluzione è migliori o peggiore rispetto ad una closure?

La principale differenza è che se il valore di `count` sta su una variabile esterna, allora il codice al suo esterno non vi può accedere. Solamente le funzioni annidate possono modificarla. Se invece questa è legata ad una funzione, possono accadere cose simili:

```js
function makeCounter() {

  function counter() {
    return counter.count++;
  };

  counter.count = 0;

  return counter;
}

let counter = makeCounter();


counter.count = 10;
alert( counter() ); // 10

```

Quindi non c'è alcuna scelta migliore, ogni caso va analizzato.

## Named Function Expression

Named Function Expression (Espressione di Funzione con Nome), o NFE, è un termine per riferirsi alle espressioni di funzioni che hanno un nome.

Ad esempio, prendiamo una normale espressione di funzione:

```js
let sayHi = function(who) {
  alert(`Hello, ${who}`);
};
```

E diamogli un nome:

```js
let sayHi = function func(who) {
  alert(`Hello, ${who}`);
};
```

Abbiamo ottenuto qualcosa? Qual'è lo scopo di aggiungere il nome `"func"`?

Innanzitutto vale la pena notare che continua ad essere un espressione di funzione. Aggiungere il nome `"func"` dopo `function` non la rende una dichiarazione di funzione, perché viene comunque creata come una parte di un assegnazione.

Quindi aggiungere un nome non provoca assolutamente nessuno danno.

La funzione rimane comunque disponibile come `sayHi()`:

```js
let sayHi = function func(who) {
  alert(`Hello, ${who}`);
};

sayHi("John"); // Hello, John
```

Ci sono due cose che rendono speciale il nome `func`:

1. Consente alla funzione di riferirsi a se stessa internamente.
2. Non è visibile all'esterno della funzione.

Ad esempio, la funzione `sayHi` qui sotto, chiama nuovamente se stessa con `"Guest"` se non viene fornito alcun `who`:

```js
let sayHi = function func(who) {
  if (who) {
    alert(`Hello, ${who}`);
  } else {

    func("Guest"); // utilizza func per richiamare se stessa

  }
};

sayHi(); // Hello, Guest

// Questo non funziona:
func(); // Errore, func non è definita (non è visibile all'esterno)
```

Perché utilizziamo `func`? Forse potremmo semplicemente chiamare `sayHi` per le chiamate annidate?

In realtà, in molti è possibile:

```js
let sayHi = function(who) {
  if (who) {
    alert(`Hello, ${who}`);
  } else {

    sayHi("Guest");

  }
};
```

Il problema con questo codice è che il valore di `sayHi` potrebbe cambiare. La funzione potrebbe essere trasferita su un'altra variabile, e il codice diventerebbe errato:

```js
let sayHi = function(who) {
  if (who) {
    alert(`Hello, ${who}`);
  } else {

    sayHi("Guest"); // Errore: sayHi non è una funzione

  }
};

let welcome = sayHi;
sayHi = null;

welcome(); // Errore, la chiamata annidata a sayHi non è più in funzione!
```

Questo accade perché la funzione prende `sayHi` dal suo lexical environment esterno. Non c'è alcun `sayHi` locale, quindi viene utilizzata la variabile esterna. Nell'esempio sopra al momento della chiamata il valore di `sayHi` è `null`.

La possibilità di aggiungere un nome ad un espressione di funzione è pensato proprio per risolvere questo tipo di problemi.

Sfruttiamo questa caratteristica per sistemare il codice:

```js
let sayHi = function func(who) {
  if (who) {
    alert(`Hello, ${who}`);
  } else {

    func("Guest"); // Ora è tutto okay

  }
};

let welcome = sayHi;
sayHi = null;

welcome(); // Hello, Guest (la chiamata annidata funziona correttamente)
```

Ora funzione, perché il nome `"func"` è locale alla funzione. Non viene prelevato dall'esterno. Le specifiche garantisco che in questo modo si avrà sempre un riferimento alla funzione corrente.

Il codice esterno continuerà ad utilizzare la variabile `sayHi` o `welcome`. E `func` servirà da "nome interno" della funzione.


::: tip Tutto questo non vale per la dichiarazione di funzione
La caratteristica del "nome interno" è disponibile solamente per le espressioni di funzione, non per le dichiarazioni di funzione. Per le dichiarazioni di funzione, non c'è alcun modo per aggiungere un ulteriore "nome interno".

Talvolta, nel caso in cui avessimo bisogno di un nome interno, potrebbe essere sensato riscrivere la dichiarazione di funzione come espressione di funzione.
:::

## Riepilogo

Le funzioni sono oggetti.

Qui abbiamo visto le proprietà:

- `name` -- il nome della funzione. Non esiste solamente quando viene fornito nella definizione della funzione, ma anche nel caso di assegnazioni o proprietà di un oggetto.
- `length` -- il numero di argomenti nella definizione della funzione. I parametri di resto non vengono contati.

Se una funzione viene dichiarata come espressione di funzione (non nel principale flusso di codice), e possiede un nome, questa viene definita una Named Function Expression. Il nome può essere utilizzato internamente per auto-riferimenti, per chiamate ricorsive e altri contesti simili.

Inoltre, una funzione può possedere diverse proprietà aggiuntive. Molte librerie JavaScript fanno largo utilizzo di questa caratteristica.

Queste creano una funzione "principale" e ci attaccano molte altre funzioni di "supporto". Ad esempio la libreria [jquery](https://jquery.com) definisce una funzione chiamata `$`. La libreria [lodash](https://lodash.com) definisce una funzione `_`. E ci aggiunge `_.clone`, `_.keyBy` e altre proprietà (vedi la [documentazione](https://lodash.com/docs). In realtà, lo fanno anche per diminuire la sporcizia nello spazio globale, in questo modo una libreria fornisce una sola variabile globale. Questo riduce la probabilità di conflitti tra nomi.

Quindi una funzione, oltre ad essere utile, può fornire un insieme di altre funzionalità grazie alle proprietà.

## Esercizi

### 1 · Impostare e decrementare il contatore

Modificate il codice di `makeCounter()` in modo tale che il counter possa essere anche decrementato e reimpostato:

- `counter()` dovrebbe ritornare il prossimo numero (come già fa).
- `counter.set(value)` dovrebbe impostare il contatore a `value`.
- `counter.decrease()` dovrebbe decremetare il contatore di 1.

Vedi il codice in sandbox per un esempio completo.

P.S. Potete usare sia una closure che una proprietà di funzione. O scrivere entrambe le varianti.

::::: details Soluzione

La soluzione utilizza `count` come variabile locale, ma i metodi aggiuntivi sono scritti dentro `counter`. Condividono lo stesso lexical environment esterno e possono accedere al valore di `count`.

:::::

### 2 · Sommare con un numero arbitrario di parentesi

Scrivete una funzione `sum` che funzioni in questo modo:

```js
sum(1)(2) == 3; // 1 + 2
sum(1)(2)(3) == 6; // 1 + 2 + 3
sum(5)(-1)(2) == 6
sum(6)(-1)(-2)(-3) == 0
sum(0)(1)(2)(3)(4)(5) == 15
```

P.S. Aiuto: potresti impostare una conversione "toPrimitive" del tuo oggetto.

::::: details Soluzione

1. Per far si che che funzioni *comunque*, il risultato di `sum` deve essere una funzione.
2. Questa funzione deve tenere in memoria il valore corrente.
3. Come richiesto dall'esercizio, la funzione deve essere convertita in numero quando viene utilizzata con `==`. Le funzioni sono oggetti, quindi la conversione avviene come descritto nel capitolo [Conversione da oggetto a primitivi](/javascript/tutorial/object-toprimitive), e possiamo fornire un nostro metodo che si occupi di trasformare la funzione in tipo numerico.

Il codice:

```js
function sum(a) {

  let currentSum = a;

  function f(b) {
    currentSum += b;
    return f;
  }

  f.toString = function() {
    return currentSum;
  };

  return f;
}

alert( sum(1)(2) ); // 3
alert( sum(5)(-1)(2) ); // 6
alert( sum(6)(-1)(-2)(-3) ); // 0
alert( sum(0)(1)(2)(3)(4)(5) ); // 15
```

Da notare che la funzione `sum` esegue una sola volta. Ritorna una funzione `f`.

Poi, in ogni chiamata successiva, `f` aggiunge il suo parametro alla somma presente in `currentSum`, e ritorna se stessa.

**Non c'è ricorsione nell'ultima linea di `f`.**

Una ricorsione appare in questo modo:

```js
function f(b) {
  currentSum += b;
  return f(); // <-- chiamata ricorsiva
}
```

Nel nostro caso, semplicemente ritorniamo una funzione, senza effettuare alcuna chiamata:

```js
function f(b) {
  currentSum += b;
  return f; // <-- non viene invocata, ritorna solamente se stessa
}
```

Questa `f` verrà utilizzata nella chiamata successiva, e ritornerà ancora se stessa, tutte le volte che sarà necessario. Quindi, quando la utilizzeremo come numero o stringa, `toString` ritorna la `currentSum`. Possiamo anche utilizzare `Symbol.toPrimitive` o `valueOf` per la conversione.

:::::

