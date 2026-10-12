---
title: "Costruttore, operatore \"new\""
description: "JavaScript.info in italiano: Costruttore, operatore \"new\""
sourceTutorial: true
prev: {"text": "Metodi degli oggetti,\"this\"", "link": "/javascript/tutorial/object-methods"}
next: {"text": "Concatenamento opzionale '?.'", "link": "/javascript/tutorial/optional-chaining"}
---

# Costruttore, operatore "new"

> **JavaScript.info · Ilya Kantor e contributori.** [Originale inglese](https://javascript.info/constructor-new) · [Edizione italiana](https://it.javascript.info/constructor-new) · [Fonti e licenza](/javascript/fonti).

La sintassi `{...}` ci consente di creare un oggetto. Ma spesso abbiamo bisogno di creare multipli oggetti simili, come ad esempio più utenti, oggetti del menu e molto altro.

Questo può essere fatto utilizzando un costruttore e l'operatore `"new"`.

## Costruttore

Tecnicamente un costruttore è una normale funzione. Ma ci sono due convenzioni:

1. Vengono denominati con la prima lettera maiuscola.
2. Questi dovrebbero essere eseguiti solo con l'operatore `"new"`.

Ad esempio:

```js
function User(name) {
  this.name = name;
  this.isAdmin = false;
}


let user = new User("Jack");


alert(user.name); // Jack
alert(user.isAdmin); // false
```

Quando una funzione viene eseguita con `new`, esegue questi passaggi:

1. Un nuovo oggetto, vuoto, viene creato ed assegnato a `this`.
2. Viene eseguito il corpo della funzione. Solitamente questo modifica `this`, aggiungendo nuove proprietà.
3. Viene ritornato il valore assegnato a `this`.

In altre parole, `new User(...)` fa qualcosa del genere:

```js
function User(name) {

  // this = {};  (implicito)


  // aggiungiamo proprietà a this
  this.name = name;
  this.isAdmin = false;


  // return this;  (implicito)

}
```

Quindi `let user = new User("Jack")` dà lo stesso risultato di:

```js
let user = {
  name: "Jack",
  isAdmin: false
};
```

Ora, se vogliamo creare altri utenti, possiamo chiamare `new User("Ann")`, `new User("Alice")` e cosi via. Molto più rapido rispetto all'utilizzare ogni volta oggetti letterali; risulta anche più facile da leggere.

Questo è il principale scopo dei costruttori -- implementare codice riutilizzabile per la creazione di oggetti.

Ribadiamo -- tecnicamente, ogni funzione (eccetto le arrow functions, siccome non hanno `this`) può essere utilizzata come costruttore. Ovvero: ogni funzione può essere eseguita con `new`. La "prima lettera maiuscola" è semplicemente una convenzione, per rendere esplicito che la funzione deve essere eseguita con `new`.


:::: tip new function() { ... }
Se abbiamo molte linee di codice utili alla creazione di un unico oggetto, possiamo raggrupparle in un costruttore richiamato contestualmente, come qui:

```js
// create a function and immediately call it with new
let user = new function() { 
  this.name = "John";
  this.isAdmin = false;

  // ...altro codice per la creazione di user
  // magari logiche complesse e istruzioni
  // variabili locali etc
};
```

Il costruttore non può essere chiamato nuovamente, perché non è salvato da nessuna parte; viene solo creato e chiamato. Questo trucco consente di incapsulare un codice che costruisce un singolo oggetto, senza necessità di riutilizzo futuro.
::::

## Costruttori modalità test: new.target


::: tip Tecniche avanzate
La sintassi presentata nella seguente sezione viene utilizzata raramente; potete tranquillamente saltarla se non vi interessa sapere proprio tutto.
:::

Dentro la funzione, possiamo controllare quando questa viene chiamata con `new` e quando senza, utilizzando una speciale proprietà `new.target`.

Questa risulta 'undefined' per le chiamate normali, mentre contiene la funzione se viene chiamata con  `new`:


```js
function User() {
  alert(new.target);
}

// senza "new":

User(); // undefined


// con "new":

new User(); // function User { ... }

```

Questo può essere utilizzato per consentire ad entrambe le chiamate di funzionare (con `new` e senza), quindi sia in in "modalità costruttore" che in "modalità regolare".

Possiamo anche fare in modo che le chiamate con *new* e quelle regolari facciano la stessa cosa, come in questo esempio:

```js
function User(name) {
  if (!new.target) { // se mi esegui senza new 
    return new User(name); // ...Aggiungo new al posto tuo
  }

  this.name = name;
}

let john = User("John"); // reindirizza la chiamata a new User
alert(john.name); // John
```

Questo approccio viene adottato in alcune librerie per rendere la sintassi più flessibile. Rende possibile la chiamata della funzione sia con `new` che senza.

Ma non è un'ottima cosa utilizzare la doppia sintassi ovunque, perché omettendo `new` il codice perde in leggibilità. Con la parola chiave `new` possiamo sapere con certezza che si sta creando un nuovo oggetto.

## Return nel costruttore


Solitamente, i costruttori non hanno l'istruzione `return`. Il loro compito è di eseguire tutto ciò che è necessario a creare l'oggetto lavorando su `this`; quest'ultimo sarà il risultato.

Se decidiamo di inserire un'istruzione di `return`, vanno seguite delle semplici regole:

- Se `return` viene invocato con un oggetto, questo verrà ritornato al posto di `this`.
- Se `return` viene invocato con un tipo primitivo, verrà ignorato.

In altre parole, `return` con un oggetto ritorna quell'oggetto; in tutti gli altri casi verrà ritornato `this`.

Ad esempio, qui `return` sovrascrive `this` ritornando un oggetto:

```js
function BigUser() {

  this.name = "John";

  return { name: "Godzilla" };  // <-- ritorna questo oggetto
}

alert( new BigUser().name );  // Godzilla
```

Qui invece abbiamo un esempio con un `return` vuoto (potremmo anche ritornare un qualsiasi valore di tipo primitivo):

```js
function SmallUser() {

  this.name = "John";

  return; // <-- returns this
}

alert(new SmallUser().name);  //John
```

Solitamente i costruttori non hanno l'istruzione `return`. Abbiamo comunque riportato, per completezza, quel che succede se si tenta di ritornare un oggetto.


:::: tip Omettere le parentesi
Possiamo anche omettere le parentesi dopo `new`, se non ci sono argomenti:

```js
let user = new User; // <-- no parentheses
// same as
let user = new User();
```

L'omissione delle parentesi non viene considerata come "buona programmazione", la sintassi comunque lo permette.
::::

## Metodi in un costruttore

Utilizzare costruttori per creare degli oggetti ci dà un grande vantaggio in termini di flessibilità. Il costruttore può avere dei parametri che definiscono come costruire l'oggetto, e cosa "metterci dentro".

Ovviamente, possiamo aggiunger a `this` non solo proprietà, ma anche metodi.

Ad esempio, `new User(name)` crea un oggetto con un nome (passato come `name`) e un metodo `sayHi`:

```js
function User(name) {
  this.name = name;

  this.sayHi = function() {
    alert( "My name is: " + this.name );
  };
}


let john = new User("John");

john.sayHi(); // My name is: John


/*
john = {
   name: "John",
   sayHi: function() { ... }
}
*/
```

Per creare oggetti più complessi, esiste una sintassi più avanzata, [classes](https://it.javascript.info/classes), che copriremo più avanti.

## Riepilogo

- Le funzioni di costruzione, o meglio, i costruttori, sono solo delle normali funzioni; seguono però una convenzione comune che prevede di denominarle con la prima lettera maiuscola.
- Un costruttore dovrebbe essere chiamato solamente utilizzando `new`. Questo tipo di chiamata implica la creazione di un oggetto vuoto, `this`, che verrà popolato entro la fine della funzione.

Possiamo utilizzare i costruttori per costruire molti oggetti simili tra loro.

JavaScript fornisce costruttori per la maggior parte degli oggetti integrati nel linguaggio: come `Date` per le date, `Set` per gli insiemi e molti altri che studieremo più avanti.


::: tip Oggetti, ci ritorneremo!
In questo capitolo abbiamo coperto solamente le basi degli oggetti e dei costruttori. Era necessario conoscerne le basi per capire meglio i data types e le funzioni che studieremo nel prossimo capitolo.

Dopo questo, ritorneremo sugli oggetti e li analizzeremo più in dettaglio nei capitoli [prototypes](https://it.javascript.info/prototypes) e [classes](https://it.javascript.info/classes).
:::

## Esercizi

### 1 · Due funzioni – un oggetto

E' possibile creare due funzioni `A` e `B` tali che `new A()==new B()`?

```js
function A() { ... }
function B() { ... }

let a = new A;
let b = new B;

alert( a == b ); // true
```

Se pensi che sia possibile, prova a scrivere il codice.

::::: details Soluzione

Si, è possibile.

Se una funzione ritorna un oggetto, questo verrà ritornato da `new` invece di `this`.

Quindi, le due funzioni potrebbero ritornare un oggetto definito esternamente `obj`:

```js
let obj = {};

function A() { return obj; }
function B() { return obj; }

alert( new A() == new B() ); // true
```

:::::

### 2 · Create una nuova Calculator

Scrivete un costruttore `Calculator` che crea oggetti con 3 metodi:

- `read()` richiede due valori utilizzando `prompt` e li memorizza nelle proprietà dell'oggetto.
- `sum()` ritorna la somma delle proprietà.
- `mul()` ritorna il prodotto delle proprietà.

Ad esempio:

```js
let calculator = new Calculator();
calculator.read();

alert( "Sum=" + calculator.sum() );
alert( "Mul=" + calculator.mul() );
```

[Apri l’esempio nella fonte originale](https://it.javascript.info/constructor-new).

::::: details Soluzione

```js
function Calculator() {

  this.read = function() {
    this.a = +prompt('a?', 0);
    this.b = +prompt('b?', 0);
  };

  this.sum = function() {
    return this.a + this.b;
  };

  this.mul = function() {
    return this.a * this.b;
  };
}

let calculator = new Calculator();
calculator.read();

alert( "Sum=" + calculator.sum() );
alert( "Mul=" + calculator.mul() );
```

:::::

### 3 · Create un nuovo Accumulator

Scrivete un costruttore `Accumulator(startingValue)`.

L'oggetto che viene creato dovrebbe:

- Salvare il "valore corrente" nella proprietà `value`. Il valore di partenza viene impostato prendendo il valore passato all'argomentto del costruttore `startingValue`.
- Il metodo `read()` dovrebbe richiedere tramite `prompt` un numero e sommarlo a `value`.

In altre parole, la proprietà `value` è la somma di tutti i numeri inseriti dall'utente partendo dal valore iniziale `startingValue`.

Qui una demo del codice:

```js
let accumulator = new Accumulator(1); // initial value 1

accumulator.read(); // adds the user-entered value
accumulator.read(); // adds the user-entered value

alert(accumulator.value); // shows the sum of these values
```

[Apri l’esempio nella fonte originale](https://it.javascript.info/constructor-new).

::::: details Soluzione

```js
function Accumulator(startingValue) {
  this.value = startingValue;

  this.read = function() {
    this.value += +prompt('How much to add?', 0);
  };

}

let accumulator = new Accumulator(1);
accumulator.read();
accumulator.read();
alert(accumulator.value);
```

:::::

