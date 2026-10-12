---
title: "Variable scope, closure"
description: "JavaScript.info in italiano: Variable scope, closure"
sourceTutorial: true
prev: {"text": "Parametri resto e operatore di espansione", "link": "/javascript/tutorial/rest-parameters-spread"}
next: {"text": "Il vecchio \"var\"", "link": "/javascript/tutorial/var"}
---

# Variable scope, closure

> **JavaScript.info · Ilya Kantor e contributori.** [Originale inglese](https://javascript.info/closure) · [Edizione italiana](https://it.javascript.info/closure) · [Fonti e licenza](/javascript/fonti).

JavaScript è un linguaggio fortemente orientato alle funzioni. Fornisce molta libertà. Una funzione può essere creata in qualsiasi momento, copiata su una variabile o passata come argomento ad un'altra funzione e richiamata da qualsiasi punto del codice.

Sappiamo che una funzione può accedere alle variabili esterne, questa caratteristica viene spesso utilizzata.

Cosa accade quando una variabile esterna cambia? La funzione utilizza il valore più recente o quello presente al momento della creazione della funzione?

Inoltre, cosa accade quando una funzione viene spostata in un altro punto del codice e viene richiamata -- avrebbe accesso alle variabile esterne della nuova posizione?

In questa situazione linguaggi diversi si comportano in maniera diversa, in questo capitolo ci occuperemo del comportamento di JavaScript.


::: tip Qui parleremo delle variabili `let/const`
In JavaScript, ci esistono 3 modi per dichiarare una variabile: `let`, `const` (metodologie più moderne), e `var` (metodo utilizzato in passato).

- In questo articolo utilizzeremo `let`.
- Variabili, dichiarate tramite `const`, quindi in questo articolo parleremo anche di `const`.
- Il vecchio `var` ha alcune differenze importanti, di cui parleremo nell'articolo [Il vecchio "var"](/javascript/tutorial/var).
:::

## Blocchi di codice

Se una variabile viene dichiarata all'interno di un blocco di codice `{...}`, questa sarà visibile solamente all'interno di quel blocco di codice.

Ad esempio:

```js
{
  // facciamo alcune operazioni con variabili locali che non dovrebbero essere visibili all'esterno

  let message = "Hello"; // visibile solamente all'interno di questo blocco

  alert(message); // Hello
}

alert(message); // Error: message is not defined
```

Possiamo utilizzare i blocchi di codice per isolare pezzi di codice, definendo delle variabili che gli appartengono:

```js
{
  // mostra message
  let message = "Hello";
  alert(message);
}

{
  // show another messa ge
  let message = "Goodbye";
  alert(message);
}
```


:::: tip Ci sarebbe un errore senza blocchi
Da notare, senza blocchi separati ci sarebbe un errore, nel caso in cui usassimo `let` con un nome di variabile già esistente:

```js
// mostra message
let message = "Hello";
alert(message);

// mostra un altro message

let message = "Goodbye"; // Error: variable already declared

alert(message);
```
::::

Per `if`, `for`, `while` e cosi via, le variabili dichiarate all'interno di `{...}` sono visibili solo al suo interno:

```js
if (true) {
  let phrase = "Hello!";

  alert(phrase); // Hello!
}

alert(phrase); // Error, no such variable!
```

Qui, quando termina `if`, l'espressione `alert` non avrà accesso a `phrase`, quindi verrà emesso un errore.

Questo è ottimo, poiché ci consente di creare variabili locali al blocco di codice, specifiche per un branch di `if`.

The similar thing holds true for `for` and `while` loops:

```js
for (let i = 0; i < 3; i++) {
  // la variabile i è visibile solamente all'interno del for
  alert(i); // 0, then 1, then 2
}

alert(i); // Error, no such variable
```

Visually, `let i` is outside of `{...}`. But the `for` construct is special here: the variable, declared inside it, is considered a part of the block.

## Funzioni annidate

Una funzione si definisce "annidata" quando viene creata all'interno di un'altra funzione.

E' molto semplice farlo in JavaScript.

Possiamo utilizzare questo concetto per organizzare il codice, come in questo esempio:

```js
function sayHiBye(firstName, lastName) {

  // helper nested function to use below
  function getFullName() {
    return firstName + " " + lastName;
  }

  alert( "Hello, " + getFullName() );
  alert( "Bye, " + getFullName() );

}
```

Qui la funzione *annidata*  `getFullName()` è stata creata per comodità. Può accedere alle variabili esterne quindi può ritornarne il nome completo. Le funzioni annidate sono abbastanza comuni in JavaScript.

Un'altra cosa interessante, una funzione annidata può essere ritornata: sia come proprietà di un nuovo oggetto (se la funzione esterna crea un oggetto con dei metodi) o come risultato stesso. Può essere salvata e utilizzata da qualsiasi altra parte. Non ha importanza dove, avrà comunque accesso alle stesse variabili esterne.

Nell'esempio sotto, `makeCounter` crea una funzione "contatore" che ritorna il numero successivo ad ogni invocazione:

```js
function makeCounter() {
  let count = 0;

  return function() {
    return count++;
  };
}

let counter = makeCounter();

alert( counter() ); // 0
alert( counter() ); // 1
alert( counter() ); // 2
```

Nonostante siano semplici, varianti leggermente modificate di questo codice hanno usi pratici, ad esempio, come [generatore di numeri casuali](https://en.wikipedia.org/wiki/Pseudorandom_number_generator) per generare valori casuali per tests automatici. Quindi l'esempio non è cosi.

Come funziona? Se creiamo contatori multipli, saranno indipendenti? Come vengono gestite le variabili?

Conoscere queste cose è ottimo per una conoscenza generale di JavaScript è può essere utile nella gestione di scenari più complessi. Quindi proviamo ad entrare più nel dettaglio.

## Lexical Environment


::: warning Here be dragons!
The in-depth technical explanation lies ahead.

As far as I'd like to avoid low-level language details, any understanding without them would be lacking and incomplete, so get ready.
:::

For clarity, the explanation is split into multiple steps.

### Step 1. Variabili

In JavaScript, ogni funzione in esecuzione, blocco di codice `{...}`, e lo script nella sua interezza possiedono un oggetto interno associato (nascosto), anche conosciuto come *Lexical Environment*.

The Lexical Environment object consists of two parts:

1. *Environment Record (Registro d'Ambiente)* -- un oggetto che memorizza tutte le variabili locali e le sue proprietà (ed altre informazioni utili come il valore di `this`).
2. Un riferimento al *lexical environment esterno*, quello associato al codice esterno.

**Una variabile è solamente una proprietà di uno speciale oggetto interno, `Environment Record`. "Ottenere o modificare una variabile" significa "ottenere o modificare una proprietà di questo oggetto".**

In questo semplice esempio senza funzioni, esiste solamente un Lexical Environment:

![lexical environment](/javascript-info/1-js/06-advanced-functions/03-closure/lexical-environment-global.svg)

Questo è quello che viene chiamato Lexical Environment *globale*, associato all'interno script.

On the picture above, the rectangle means Environment Record (variable store) and the arrow means the outer reference. The global Lexical Environment has no outer reference, that's why the arrow points to `null`.

Mentre il codice inizia la sua esecuzione e procede, il Lexical Environment cambia.

Qui un codice leggermente più complesso:

![lexical environment](/javascript-info/1-js/06-advanced-functions/03-closure/closure-variable-phrase.svg)

I rettangoli nella parte destra dimostrano come il Lexical Enviroment globale cambia durante l'esecuzione:
Rectangles on the right-hand side demonstrate how the global Lexical Environment changes during the execution:

1. Quando il codice inizia la sua esecuzione, il Lexical Environment viene popolato con tutte le variabili dichiarate.
    - Inizialmente, queste sono in uno stato "non inizializzato". Questo è uno speciale stato interno, significa che JavaScript è a conoscenza dell'esistenza della variabile, ma ci si può fare riferimento fino a quando questa non viene dichiarata con `let`. E' equivalente a dire che la variabile non esiste.
2. Successivamente appare la dichiarazione `let phrase`. Non si ha ancora nessuna assegnazione, quindi il suo valore è `undefined`. Da questo momento in poi possiamo utilizzare la variabile.
3. A `phrase` viene assegnato un valore.
4. Il valore di `phrase` viene modificato.

Per ora tutto sembra semplice, vero?

- Una variabile è una proprietà di uno speciale oggetto interno, associato al blocco/funzione/script in esecuzione.
- Lavorare con le variabili significa concretamente lavorare con le proprietà di un oggetto.


::: tip Lexical Environment è un oggetto definito dalla specifica
"Lexical Environment" è un oggetto definito dalla specifica: esiste solamente in forma "teorica" nella [specifica di linguaggio](https://tc39.es/ecma262/#sec-lexical-environments) per descrivere come le cose funzionano. Non abbiamo modo di ottenere questo oggetto nel nostro codice e manipolarlo direttamente.

JavaScript engines also may optimize it, discard variables that are unused to save memory and perform other internal tricks, as long as the visible behavior remains as described.
:::

### Step 2. Dichiarazione di funzioni

Anche una funzione è un valore, come una variabile.

**La differenza è che la dichiarazione di funzione viene inizializzata istantaneamente.**

Quando viene creato il Lexical Environment, un dichiarazione di funzione diventa immediatamente una funzione pronta per essere utilizzata (a differenza di `let`, che rimane inutilizzabile fino alla sua dichiarazione).

Questo è il motivo per cui possiamo utilizzare una funzione, ancora prima della sua dichiarazione.

Ad esempio, qui vediamo lo stato iniziale del Lexical Environment globale, quando aggiungiamo una funzione:

![](/javascript-info/1-js/06-advanced-functions/03-closure/closure-function-declaration.svg)

Naturalmente, questo comportamento si applica solamente alle dichiarazioni di funzione, non vale per le espressioni di funzione, dove assegniamo una funzione ad una variabile, come ad esempio `let say = function(name)...`.

### Step 3. Lexical Environment interno ed esterno

Quando una funzione sta eseguendo, all'inizio della chiamata, viene creato un nuovo Lexical Environment per memorizzare le variabili locali e i parametri della chiamata.

Ad esempio, per `say("John")`, funzionerebbe in questo modo:

<!--
    ```js
    let phrase = "Hello";

    function say(name) {
     alert( `${phrase}, ${name}` );
    }

    say("John"); // Hello, John
    ```text

![](lexical-environment-simple.svg)

Durante l'esecuzione della funzione abbiamo due Lexical Environments: quello interno (utilizzato dalla funzione) e quello esterno (globale):

- Il Lexical Environment interno corrisponde all'esecuzione di `say`. Possiede una sola proprietà: `name`, l'argomento della funzione. Abbiamo invocato `say("John")`, quindi il valore di `name` è `"John"`.
- Il Lexical Environment esterno è quello globale. Possiede la variabile `phrase` e la funzione stessa.


**Quando il codice vuole accedere ad una variabile -- questa viene ricercata prima nel Lexical Environment interno, poi in quello esterno, poi quello ancora più esterno e cosi via fino ad arrivare a quello globale.**

Se una variabile non viene trovata, allora verrà lanciato un errore in strict mode (senza `use strict`, un assegnazione ad una variabile non esistente creerà una nuova variabile globale).

In questo esempio la ricerca procede:

- La variabile `name`, utilizzata da `alert` all'interno di `say`, viene trovata immediatamente nel Lexical Environment interno.
- Quando vuole accedere a `phrase`, non sarà in grado di trovare alcuna variabile `phrase` localmente, quindi seguirà il riferimento verso il Lexical Environment esterno.

![lexical environment lookup](lexical-environment-simple-lookup.svg)


### Step 4. Ritornare una funzione

Torniamo all'esempio di `makeCounter`.

```js
function makeCounter() {
  let count = 0;

  return function() {
    return count++;
  };
}

let counter = makeCounter();
```

All'inizio di ogni chiamata a `makeCounter()`, viene creato un nuovo Lexical Environment, dove memorizzare le variabili necessarie all'esecuzione di `makeCounter`.

![](closure-makecounter.svg)

La differenza è che durante l'esecuzione di `makeCounter()`, viene creata una piccola funzione annidata: `return count++`. Non viene eseguita subito, viene solamente creata.

Tutte le funzioni ricordano il Lexical Environment in cui vengono create. Tecnicamente, non c'è nulla di magico: tutte le funzione possiedono la proprietà nascosta `[[Environment]]`, che memorizza il riferimento al Lexical Environment in cui la funzione è stata creata:

![](closure-makecounter-environment.svg)

Quindi, `counter.[[Environment]]` possiede il riferimento al Lexical Environment `{count: 0}`. Questo è il modo in cui le funzioni memorizzano il contesto in cui sono state create, non ha importanza il posto in cui verranno chiamate. Il riferimento `[[Environment]]` viene impostato a tempo di creazione della funzione e non viene più modificato.

Più tardi, quando viene chiamato `counter()`, verrà creato un nuovo Lexical Environment locale, in cui verrà memorizzato il riferimento al Lexical Environment esterno `counter.[[Environment]]`:

![](closure-makecounter-nested-call.svg)

Quindi, quando il codice all'interno di `counter()` cercherà la variabile `count` nel suo Lexical Environment (vuoto, poiché non possiede variabili locali), poi cercherà nel Lexical Environment esterno, quindi quello della chiamata `makeCounter()`, dove riuscirà a trovare la variabili e potrà modificarla.

**Una variabile viene aggiornata nel Lexical Environment in cui si trova.**

Qui vediamo lo stato dopo l'esecuzione:

![](closure-makecounter-nested-call-2.svg)

If we call `counter()` multiple times, the `count` variable will be increased to `2`, `3` and so on, at the same place.


::: tip Closure
Esiste un termine generale in programmazione, "closure", che gli sviluppatori dovrebbero conoscere.

Una [closure](https://en.wikipedia.org/wiki/Closure_(computer_programming)) è una funzione che ricorda le sue variabili esterne ed è in grado di accedervi. In alcuni linguaggi questo non è possibile, oppure è richiesto che la funzione venga scritta in un determinato modo. Ma come spiegato sopra, in JavaScript, tutte le funzioni sono closure di natura (esiste una sola eccezione, che verrà tratta nel capitolo [La sintassi "new Function"](/javascript/tutorial/new-function)).

That is: they automatically remember where they were created using a hidden `[[Environment]]` property, and then their code can access outer variables.

When on an interview, a frontend developer gets a question about "what's a closure?", a valid answer would be a definition of the closure and an explanation that all functions in JavaScript are closures, and maybe a few more words about technical details: the `[[Environment]]` property and how Lexical Environments work.
:::

## Garbage collection

Solitamente, un Lexical Environment viene rimosso dalla memoria insieme a tutte le sue variabili dopo che la funzione ha completato la sua esecuzione. Questo avviene perché non si hanno più riferimenti ad essa. Come ogni altro oggetto in JavaScript, viene mantenuto in memoria solamente finché risulta essere raggiungibile.

Tuttavia, se una funzione annidata risulta essere ancora raggiungibile, allora avremmo una proprietà `[[Environment]]` che fa riferimento al Lexical Environment.

In questo caso il Lexical Environment risulta essere ancora raggiungibile dopo aver completato l'esecuzione, quindi rimane in memoria.

Ad esempio:
  return function() {
    alert(value);
  }
}

let g = f(); // g.[[Environment]] memorizza un riferimento al Lexical Environment
// della corrispondente chiamata a f()
```

Da notare che se `f()` viene chiamata più volte, e la funzione risultata viene memorizzata, allora tutti i relativi Lexical Environment verranno mantenuti in memoria. Nel codice sotto, tutti e 3:

- Da notare che se `f()` viene invocata più volte, e vengono memorizzate delle funzioni, allora anche i corrispondenti Lexical Environment vengono mantenuti in memoria. E' il caso dell'esempio qui sotto:

    ```js
    function f() {
      let value = Math.random();

      return function() { alert(value); };
    }

    // 3 functions in array, every one of them links to Lexical Environment
    // from the corresponding f() run
    //         LE   LE   LE
    let arr = [f(), f(), f()];
    ```

Nel codice sotto, dopo aver rimosso la funzione annidata, il Lexical Environment interno (e anche `value`) viene rimosso dalla memoria:

    ```js
    function f() {
      let value = 123;

  return function() {
    alert(value);
  }
}

let g = f(); // finché g esiste, il valore rimane in memoria

    g = null; // ...and now the memory is cleaned up
    ```

### Ottimizzazioni nel mondo reale

Come abbiamo visto, in teoria fino a che una funzione rimane viva, anche tutte le variabili esterne vengono mantenute in memoria.

Ma nella pratica, i motori JavaScript cercano di ottimizzare questa situazione. Monitorano l'utilizzo delle variabili, e se si rendono conto che una variabile esterna non verrà mai utilizzata, allora la rimuovono.

**Un importante effetto collaterale in V8 (Chrome, Opera) è che queste variabili non sono disponibili durante il debugging.**

Provate ad eseguire il codice d'esempio qui sotto in Chrome con aperta la finestra degli strumenti da sviluppatore.

Quando si arresta, scrivete nella console `alert(value)`.

```js
function f() {
  let value = Math.random();

  function g() {
    debugger; // in console: type alert(value); No such variable!
  }

  return g;
}

let g = f();
g();
```

Come avrete notato -- non esiste questa variabile! In teoria, dovrebbe essere accessibile, ma il motore la ha rimossa.

Questo può portare a divertenti (soprattutto se avete poco tempo a disposizione) problemi in fase di debugging. Uno di questi -- potremmo visualizzare una variabile esterne che ha lo stesso nome, piuttosto di quella desiderata:

```js
let value = "Surprise!";

function f() {
  let value = "the closest value";

  function g() {
    debugger; // in console: type alert(value); Surprise!
  }

  return g;
}

let g = f();
g();
```


::: warning Ci incontriamo!
Questa caratteristica di V8 va tenuta a mente. Se state facendo debugging con Chrome/Opera, presto o tardi vi ci imbatterete.

Questo non è un problema del debugger, ma piuttosto una caratteristica di V8. In futuro potrebbe essere risolta.
Potrete sempre testarlo provando ad eseguire il codice sopra.
:::
```

## Esercizi

### 1 · Does a function pickup latest changes?

The function sayHi uses an external variable name. When the function runs, which value is it going to use?

```js
let name = "John";

function sayHi() {
  alert("Hi, " + name);
}

name = "Pete";

sayHi(); // what will it show: "John" or "Pete"?
```

Such situations are common both in browser and server-side development. A function may be scheduled to execute later than it is created, for instance after a user action or a network request.

So, the question is: does it pick up the latest changes?

::::: details Soluzione

The answer is: **Pete**.

A function gets outer variables as they are now, it uses the most recent values.

Old variable values are not saved anywhere. When a function wants a variable, it takes the current value from its own Lexical Environment or the outer one.

:::::

### 2 · Which variables are available?

The function `makeWorker` below makes another function and returns it. That new function can be called from somewhere else.

Will it have access to the outer variables from its creation place, or the invocation place, or both?

```js
function makeWorker() {
  let name = "Pete";

  return function() {
    alert(name);
  };
}

let name = "John";

// create a function
let work = makeWorker();

// call it
work(); // what will it show?
```

Which value it will show? "Pete" or "John"?

::::: details Soluzione

The answer is: **Pete**.

The `work()` function in the code below gets `name` from the place of its origin through the outer lexical environment reference:

![](/javascript-info/1-js/06-advanced-functions/03-closure/2-closure-variable-access/lexenv-nested-work.svg)

So, the result is `"Pete"` here.

But if there were no `let name` in `makeWorker()`, then the search would go outside and take the global variable as we can see from the chain above. In that case the result would be `"John"`.

:::::

### 3 · Sono indipendenti i contatori?

Qui costruiamo due contatori: `counter` e `counter2` utilizzando la stessa funzione `makeCounter`.

Sono indipendenti? Cosa mostrerà il secondo contatore? `0,1` oppure `2,3` o qualcos altro?

```js
function makeCounter() {
  let count = 0;

  return function() {
    return count++;
  };
}

let counter = makeCounter();
let counter2 = makeCounter();

alert( counter() ); // 0
alert( counter() ); // 1


alert( counter2() ); // ?
alert( counter2() ); // ?

```

::::: details Soluzione

La risposta corretta è: **0,1.**

Le funzioni `counter` e `counter2` vengono create da diverse invocazioni di `makeCounter`.

Quindi ognuna di esse possiede Lexical Environment indipendente, onguno con la propria varaibile `count`.

:::::

### 4 · Oggetto contatore

Qui l'oggetto contatore viene creato con il costruttore.

Funziona? Cosa mostra?

```js
function Counter() {
  let count = 0;

  this.up = function() {
    return ++count;
  };
  this.down = function() {
    return --count;
  };
}

let counter = new Counter();

alert( counter.up() ); // ?
alert( counter.up() ); // ?
alert( counter.down() ); // ?
```

::::: details Soluzione

Ovviamente funziona.

Entrambe le funzioni annidate vengono create all'interno dello stesso Lexical Environment, quindi hanno accesso alla stessa variabile `count`:

```js
function Counter() {
  let count = 0;

  this.up = function() {
    return ++count;
  };
  
  this.down = function() {
    return --count;
  };
}

let counter = new Counter();

alert( counter.up() ); // 1
alert( counter.up() ); // 2
alert( counter.down() ); // 1
```

:::::

### 5 · Funzionie interna ad if

Guardate il codice. Quale sarà il risultato della chiamata all'ultima riga?

```js
let phrase = "Hello";

if (true) {
  let user = "John";

  function sayHi() {
    alert(`${phrase}, ${user}`);
  }
}


sayHi();

```

::::: details Soluzione

Il risultato sarà **un errore**.

La funzione `sayHi` viene dichiarata internamente ad un blocco `if`, per questo è visibile solamente al suo interno. Non è accessibile esternamente.

:::::

### 6 · Somma con le closure

Scrivete la funzione `sum` che funziona in questo modo: `sum(a)(b) = a+b`.

Esattamente, due parentesi tonde (non è un errore).

Ad esempio:

```js
sum(1)(2) = 3
sum(5)(-1) = 4
```

::::: details Soluzione

Perchè la seconda parentesi funzioni, la prima deve ritornare una funzione.

Come in questo esempio:

```js
function sum(a) {

  return function(b) {
    return a + b; // takes "a" from the outer lexical environment
  };

}

alert( sum(1)(2) ); // 3
alert( sum(5)(-1) ); // 4
```

:::::

### 7 · Is variable visible?

What will be the result of this code?

```js
let x = 1;

function func() {
  console.log(x); // ?

  let x = 2;
}

func();
```

P.S. There's a pitfall in this task. The solution is not obvious.

::::: details Soluzione

The result is: **error**.

Try running it:

```js
let x = 1;

function func() {

  console.log(x); // ReferenceError: Cannot access 'x' before initialization

  let x = 2;
}

func();
```

In this example we can observe the peculiar difference between a "non-existing" and "uninitialized" variable.

As you may have read in the article [](/javascript/tutorial/closure), a variable starts in the "uninitialized" state from the moment when the execution enters a code block (or a function). And it stays uninitalized until the corresponding `let` statement.

In other words, a variable technically exists, but can't be used before `let`.

The code above demonstrates it.

```js
function func() {

  // the local variable x is known to the engine from the beginning of the function,
  // but "uninitialized" (unusable) until let ("dead zone")
  // hence the error


  console.log(x); // ReferenceError: Cannot access 'x' before initialization

  let x = 2;
}
```

This zone of temporary unusability of a variable (from the beginning of the code block till `let`) is sometimes called the "dead zone".

:::::

### 8 · Filter su funzioni

Abbiamo a disposizione un metodo integrato `arr.filter(f)` per gli array. Questo filtra tutti gli elementi attraverso la funzione `f`. Se ritorna `true `, allora quell'elemento viene ritornato.

Create un insieme di filtri "pronti all'uso":

- `inBetween(a, b)` -- tra `a` e `b` o uguale.
- `inArray([...])` -- contenuto nell'array.

Il loro utilizzo dovrebbe essere:

- `arr.filter(inBetween(3,6))` -- seleziona solo i valori compresi tra 3 e 6.
- `arr.filter(inArray([1,2,3]))` -- seleziona solo gli elementi che corrispondono a `[1,2,3]`.

Ad esempio:

```js
/* .. your code for inBetween and inArray */
let arr = [1, 2, 3, 4, 5, 6, 7];

alert( arr.filter(inBetween(3, 6)) ); // 3,4,5,6

alert( arr.filter(inArray([1, 2, 10])) ); // 1,2
```

::::: details Soluzione

#### Filter inBetween

```js
function inBetween(a, b) {
  return function(x) {
    return x >= a && x <= b;
  };
}

let arr = [1, 2, 3, 4, 5, 6, 7];
alert( arr.filter(inBetween(3, 6)) ); // 3,4,5,6
```

#### Filter inArray

```js
function inArray(arr) {
  return function(x) {
    return arr.includes(x);
  };
}

let arr = [1, 2, 3, 4, 5, 6, 7];
alert( arr.filter(inArray([1, 2, 10])) ); // 1,2
```

:::::

### 9 · Ordinare per campo

Abbiamo un array di oggetti da ordinare:

```js
let users = [
  { name: "John", age: 20, surname: "Johnson" },
  { name: "Pete", age: 18, surname: "Peterson" },
  { name: "Ann", age: 19, surname: "Hathaway" }
];
```

Il modo più classico per farlo sarebbe:

```js
// by name (Ann, John, Pete)
users.sort((a, b) => a.name > b.name ? 1 : -1);

// by age (Pete, Ann, John)
users.sort((a, b) => a.age > b.age ? 1 : -1);
```

Possiamo renderlo anche più breve, ad esempio:

```js
users.sort(byField('name'));
users.sort(byField('age'));
```

Quindi, piuttosto che scrivere una funzione, utilizziamo `byField(fieldName)`.

Scrivete la funzione `byField`.

::::: details Soluzione



:::::

### 10 · Funzione crea eserciti

Il seguente codice crea un array di `shooters`.

Ogni funzione è pensata per ritornare il numero, Ma qualcosa non va...

```js
function makeArmy() {
  let shooters = [];

  let i = 0;
  while (i < 10) {
    let shooter = function() { // shooter function
      alert( i ); // should show its number
    };
    shooters.push(shooter);
    i++;
  }

  return shooters;
}

let army = makeArmy();

army[0](); // the shooter number 0 shows 10
army[5](); // and number 5 also outputs 10...
// ... all shooters show 10 instead of their 0, 1, 2, 3...
```

Perché tutti gli eserciti possiedono lo stesso numero di militari? Modificate il codice in modo tale che funzioni correttamente.

::::: details Soluzione

Esaminiamo cosa accade dentro `makeArmy`, e la soluzioni ci apparirà ovvia.

1. Crea un array vuoto `shooters`:

    ```js
    let shooters = [];
    ```
2. Lo riempie con un ciclo `shooters.push(function...)`.

    Ogni elemento è una funzione, quindi l'array finale risulterà essere:

    ```js
    shooters = [
      function () { alert(i); },
      function () { alert(i); },
      function () { alert(i); },
      function () { alert(i); },
      function () { alert(i); },
      function () { alert(i); },
      function () { alert(i); },
      function () { alert(i); },
      function () { alert(i); },
      function () { alert(i); }
    ];
    ```

3. L'array viene ritornato dalla funzione.

Successivamente, la chiamata `army[5]()` recupererà l'elemento `army[5]` dall'array (cioè una funzione) e la invocherà.

Ora perché tutte le funzione mostrano lo stesso risultato, `10`?

Questo accade perché non c'è alcuna variabile locale `i` interna alla funzione `shooter`. Quando questa funzione viene invocata, prende `i` dal lexical environment esterno.

Quale sarà il valore di `i`?

Se guardiamo il codice:

```js
function makeArmy() {
  ...
  let i = 0;
  while (i < 10) {
    let shooter = function() { // shooter function
      alert( i ); // dovrebbe mostrare il suo numero
    };
    shooters.push(shooter); // aggiunge function all'array
    i++;
  }
  ...
}
```

Possiamo notare che la funzione `shooter` viene creata nel lexical environment di `makeArmy()`. Ma quando invochiamo `army[5]()`, `makeArmy` ha già terminato l'esecuzione, ed il valore finale di `i` è `10` (`while` si ferma a `i=10`).

Il risultato è che tutte le funzioni `shooter` prendono lo stesso valore dal lexical envrironment esterno, in cui l'ultimo valore è `i=10`.

![](/javascript-info/1-js/06-advanced-functions/03-closure/10-make-army/lexenv-makearmy-empty.svg)

Come puoi vedere qui sotto, a ogni iterazione del blocco `while {...}` viene creato un nuovo lexical environment. Quindi, per correggere, possiamo copiare il valore di `i` in una variabile all'interno del blocco `while {...}` stesso, così:

```js
function makeArmy() {
  let shooters = [];

  let i = 0;
  while (i < 10) {
    
      let j = i;
    
      let shooter = function() { // shooter function
        alert( j ); // dovrebbe mostrare il suo numero
      };
    shooters.push(shooter);
    i++;
  }

  return shooters;
}

let army = makeArmy();

// Ora il codice funziona correttamente
army[0](); // 0
army[5](); // 5
```

Qui `let j = i` dichiara la variabile `j` "locale all'iterazione" e copia `i` al suo interno. I tipi primitivi vengo copiato "per valore", quindi otteniamo una copia indipendente di `i`, appartenente all'iterazione corrente del ciclo.

Shooters funziona correttamente, perché il valore di `i` è un po' più vicino. Non è nel Lexical Environment di `makeArmy()`, ma nel Lexical Environment che corrisponde all'iterazione corrente del ciclo:

![](/javascript-info/1-js/06-advanced-functions/03-closure/10-make-army/lexenv-makearmy-while-fixed.svg)

Questo tipo di problema può anche essere evitato usando `for` all'inizio, in questo modo:

```js
function makeArmy() {

  let shooters = [];


  for(let i = 0; i < 10; i++) {

    let shooter = function() { // shooter function
      alert( i ); // dovrebbe mostrare il suo numero
    };
    shooters.push(shooter);
  }

  return shooters;
}

let army = makeArmy();

army[0](); // 0
army[5](); // 5
```

Essenzialmente è la stessa cosa, perché ad ogni iterazione `for` viene generato un nuovo lexical environment, con la propria variabile `i`. Quindi `shooter` generato in ogni iterazione fa riferimento alla propria `i`, in quella stessa iterazione.

![](/javascript-info/1-js/06-advanced-functions/03-closure/10-make-army/lexenv-makearmy-for-fixed.svg)

:::::

