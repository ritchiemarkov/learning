---
title: "Array"
description: "JavaScript.info in italiano: Array"
sourceTutorial: true
prev: {"text": "Stringhe", "link": "/javascript/tutorial/string"}
next: {"text": "Metodi per gli array", "link": "/javascript/tutorial/array-methods"}
---

# Array

> **JavaScript.info · Ilya Kantor e contributori.** [Originale inglese](https://javascript.info/array) · [Edizione italiana](https://it.javascript.info/array) · [Fonti e licenza](/javascript/fonti).

Gli oggetti consentono la memorizzazione di una collezione di valori associati alle rispettive chiavi.

Ma spesso abbiamo bisogno di una *collezione ordinata*, dove abbiamo un primo, un secondo, un terzo elemento e così via. Ad esempio, abbiamo bisogno di memorizzare una lista di cose: utenti, beni, elementi HTML etc.

Non è conveniente utilizzare un oggetto per questo tipo di lavori, poiché non avremmo alcun metodo per gestire l'ordine degli elementi. Non possiamo inserire una nuova proprietà "tra" due già esistenti.  Gli oggetti non sono stati pensati per questo scopo.

Esistono delle speciali strutture dati chiamate `Array`, che consentono la memorizzazione di collezioni ordinate. 

## Dichiarazione

Ci sono due differenti sintassi per la creazioni di un array vuoto:

```js
let arr = new Array();
let arr = [];
```

Nella maggioranza dei casi, la seconda sintassi è quella preferita. Possiamo già fornire degli elementi da inserire, all'interno delle parentesi quadre:

```js
let fruits = ["Apple", "Orange", "Plum"];
```

Gli elementi di un array sono numerati a partire dallo zero.

Possiamo ottenere un elemento tramite il suo numero di indice:

```js
let fruits = ["Apple", "Orange", "Plum"];

alert( fruits[0] ); // Apple
alert( fruits[1] ); // Orange
alert( fruits[2] ); // Plum
```

Possiamo rimpiazzare un elemento:

```js
fruits[2] = 'Pear'; // ora ["Apple", "Orange", "Pear"]
```

...o aggiungerne uno nuovo:

```js
fruits[3] = 'Lemon'; // ora ["Apple", "Orange", "Pear", "Lemon"]
```

Il numero degli elementi dell'array è `length`:

```js
let fruits = ["Apple", "Orange", "Plum"];

alert( fruits.length ); // 3
```

Possiamo anche utilizzare `alert` per mostrare l'intero array.

```js
let fruits = ["Apple", "Orange", "Plum"];

alert( fruits ); // Apple,Orange,Plum
```

Un array può memorizzare elementi di qualsiasi tipo.

Ad esempio:

```js
// insieme di valori
let arr = [ 'Apple', { name: 'John' }, true, function() { alert('hello'); } ];

// prende l'oggetto all'indice 1 e ne mostra il nome
alert( arr[1].name ); // John

// prende la funzione all'indice 3 e la esegue
arr[3](); // hello
```



:::: tip Virgola pendente
Gli array, proprio come gli oggetti, possono terminare con una virgola:
```js
let fruits = [
  "Apple",
  "Orange",
  "Plum",
];
```

La "virgola pendente" rende più semplice inserire/rimuovere elementi, perché tutte le linee seguono la stessa struttura.
::::


## I metodi pop/push, shift/unshift

Una [queue](https://en.wikipedia.org/wiki/Queue_(abstract_data_type)) (coda) è una delle più comuni applicazioni di un array. In ambito informatico, questa è una collezione ordinata che consente due operazioni:

- `push` inserisce un elemento in coda.
- `shift` per estrarre un elemento dall'inizio, e scorrere in avanti la coda, di modo che il secondo elemento diventa il primo.

![](/javascript-info/1-js/05-data-types/04-array/queue.svg)

Gli array supportano entrambe le operazioni.

Nella pratica non è strano incontrare questo "tipo" di array. Ad esempio una coda di messaggi che devono essere mostrati sullo schermo.

Esiste un altro caso d'uso degli array -- la struttura dati chiamata [stack](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)). 

Questa supporta due operazioni:

- `push` aggiunge un elemento in coda.
- `pop` estrae un elemento dalla coda.

Quindi gli elementi vengono sempre aggiunti o presi dalla "fine".

Uno stack viene spesso illustrato come un pacco di carte: le nuove carte vengono aggiunte sempre in cima o da lì estratte:

![](/javascript-info/1-js/05-data-types/04-array/stack.svg)

Negli gli stack, l'ultimo elemento inserito viene prelevato per primo. Questo comportamento viene definito LIFO (Last-In-First-Out). Nel caso delle code, il comportamento viene chiamato FIFO (First-In-First-Out).

Gli array in JavaScript possono implementare sia una queue che uno stack. C'è la possibilità di aggiungere/rimuovere elementi sia in cima che in coda.

In informatica questa struttura dati si chiama [deque](https://en.wikipedia.org/wiki/Double-ended_queue).

**Metodi che operano sulla coda di un array:**

`pop`
: Estrae l'ultimo elemento dell'array e lo ritorna:

    ```js
    let fruits = ["Apple", "Orange", "Pear"];

    alert( fruits.pop() ); // rimuove "Pear" e lo ritorna con alert

    alert( fruits ); // Apple, Orange
    ```

`push`
: Inserisce l'elemento in coda all'array:

    ```js
    let fruits = ["Apple", "Orange"];

    fruits.push("Pear");

    alert( fruits ); // Apple, Orange, Pear
    ```

    La chiamata `fruits.push(...)` è equivalente a `fruits[fruits.length] = ...`.

**Metodi che operano sull'inizio dell'array:**

`shift`
: Estrae il primo elemento dell'array e lo ritorna:

    ```js
    let fruits = ["Apple", "Orange", "Pear"];

    alert( fruits.shift() ); // rimuove Apple e lo ritorna con alert

    alert( fruits ); // Orange, Pear
    ```

`unshift`
: Aggiunge l'elemento alla testa dell'array:

    ```js
    let fruits = ["Orange", "Pear"];

    fruits.unshift('Apple');

    alert( fruits ); // Apple, Orange, Pear
    ```

I metodi `push` e `unshift` possono aggiungere anche più elementi in una volta sola:

```js
let fruits = ["Apple"];

fruits.push("Orange", "Peach");
fruits.unshift("Pineapple", "Lemon");

// ["Pineapple", "Lemon", "Apple", "Orange", "Peach"]
alert( fruits );
```

## Internamente


Un array è uno speciale tipo di oggetto. Le parentesi quadre utilizzate per accedere alla proprietà `arr[0]` derivano dalla sintassi utilizzata con gli oggetti. Questo equivale a `obj[key]`, dove `arr` è l'oggetto, mentre i numeri vengono utilizzati come chiavi.

Inoltre estendono gli oggetti fornendo speciali metodi per operare ordinatamente su collezioni di dati, e contengono la proprietà `length`. Ma internamente rimane sempre un oggetto.

Ricordate, ci sono solo 7 tipi di base in JavaScript. Gli array sono oggetti e si comportano come tali. 

Ad esempio, vengono copiati per riferimento:

```js
let fruits = ["Banana"]

let arr = fruits; // copia per riferimento (due variabili fanno riferimento allo stesso array)

alert( arr === fruits ); // true
 
arr.push("Pear"); // modifica l'array per riferimento

alert( fruits ); // Banana, Pear - ora sono 2 elementi
```

... Ma ciò che li rende realmente speciali è la loro rappresentazione interna. Il motore prova a memorizzare gli elementi in aree di memoria contigue, uno dopo l'altro, proprio come nelle illustrazioni di questo capitolo, e ci sono anche altre ottimizzazioni per rendere gli array molto veloci.

Se iniziamo a trattare gli array come oggetti ordinari tutte le ottimizzazioni vengono meno.

Ad esempio, tecnicamente possiamo fare:

```js
let fruits = []; // crea una array

fruits[99999] = 5; // assegna una proprietà con indice maggiore della sua lunghezza

fruits.age = 25; // crea una proprietà con un nome a scelta
```

Questo è possibile, perché gli array sono comunque degli oggetti. Possiamo aggiungervi qualsiasi proprietà.

Ma *l'engine* si accorgerà che stiamo utilizzando gli array come comuni oggetti. Le ottimizzazioni specifiche per gli array non sono studiate per questi casi, e verranno quindi disattivate.

I modi per usare incorrettamente un array:

- Aggiungere una proprietà non numerica, come `arr.test = 5`. 
- Creare buchi: aggiungendo `arr[0]` e poi `arr[1000]` (lasciando spazio vuoto tra di loro).
- Riempire l'array nell'ordine inverso, ad esempio `arr[1000]`, `arr[999]`.

E' molto conveniente pensare agli array come delle speciali strutture utili a lavorare con *dati ordinati*. Forniscono speciali metodi utili a questo scopo, inoltre sono attentamente ottimizzati dal motore JavaScript per lavorare con dati ordinati e memorizzati in posizioni contigue. Quindi se doveste aver bisogno di utilizzare una proprietà con una chiave arbitraria, molto probabilmente un oggetto soddisferà le vostre necessità.

## Performance

I metodi `push/pop` vengono eseguiti rapidamente, mentre `shift/unshift` sono più lenti.

![](/javascript-info/1-js/05-data-types/04-array/array-speed.svg)

Perché è più veloce eseguire operazioni sulla coda degli array rispetto a quelle sulla testa? Andiamo a vedere cosa accade durante l'esecuzione:

```js
fruits.shift(); // prende 1 elemento dall'inizio
```

Non è sufficiente prelevare e rimuovere l'elemento con l'indice `0`. Gli altri elementi dovranno essere rinumerati.

L'operazione di `shift` deve seguire 3 passi:

1. Rimuovere l'elemento con indice `0`.
2. Spostare tutti gli elementi a sinistra, rinumerare gli indici da `1` a `0`, da `2` a `1` e cosi via.
3. Aggiornare la proprietà `length`.

![](/javascript-info/1-js/05-data-types/04-array/array-shift.svg)

**Maggiore sarà il numero di elementi, maggiore sarà il tempo richiesto, e maggiori saranno il numero di operazioni in memoria.**

Una cosa simile accade con `unshift`: per aggiungere un elemento in testa all'array, abbiamo prima bisogno di spostare tutti gli elementi a destra e aggiornare gli indici.
Invece con `push/pop`? Non richiedono lo spostamento di nulla in memoria. Per poter prelevare un elemento dalla coda, il metodo `pop` pulisce l'indirizzo e decrementa `length`.

Le azioni eseguite da `pop`:

```js
fruits.pop(); // prende 1 elemento dalla fine
```

![](/javascript-info/1-js/05-data-types/04-array/array-pop.svg)

**Il metodo `pop` non richiede spostamenti, perché ogni elemento mantiene il suo indice. Questo è il motivo per cui risulta essere un'operazione molto veloce.**

Una cosa simile accade con il metodo `push`.

## Cicli

Uno dei modi più vecchi per eseguire cicli sugli elementi di un array è il `for` utilizzando gli indici:

```js
let arr = ["Apple", "Orange", "Pear"];


for (let i = 0; i < arr.length; i++) {

  alert( arr[i] );
}
```

Per gli array c'è un'altra forma di ciclo, `for..of`:

```js
let fruits = ["Apple", "Orange", "Plum"];

// itera sugli elementi dell'array
for (let fruit of fruits) {
  alert( fruit );
}
```

Il ciclo `for..of` non fornisce il numero d'indice dell'elemento corrente, solo il suo valore; in molte situazioni questo è più che sufficiente. E più breve.

Tecnicamente, poiché gli array sono oggetti, è anche possibile utilizzare `for..in`:

```js
let arr = ["Apple", "Orange", "Pear"];


for (let key in arr) {

  alert( arr[key] ); // Apple, Orange, Pear
}
```

Non è comunque un'ottima idea. Si possono verificare diversi errori:

1. Il ciclo `for..in` itera su *tutte le proprietà*, non solo su quelle numeriche.

    Ci sono anche degli oggetti chiamati "array-like" (simili ad array), nei browser e in altri ambienti, che *assomigliano ad array*. Infatti come proprietà possiedono `length` e degli indici, ma allo stesso tempo contengono proprietà e metodi di tipo non numerico, di cui solitamente non abbiamo bisogno. Il ciclo `for..in` li passerà tutti. Quindi se stiamo utilizzando degli oggetti array-like, questi "extra" potrebbero rivelarsi un problema.

2. Il ciclo `for..in` è ottimizzato per gli oggetti generici, non gli array, e può risultare quindi 10-100 volte più lento. Ovviamente rimane comunque un'operazione molto veloce. Può essere un problema solo in caso si verifichino ingorghi. 

Generalmente, non dovremmo utilizzare `for..in` per gli array.


## Una parola riguardo "length"

La proprietà `length` si aggiorna automaticamente ad ogni modifica. Volendo essere precisi non ne rappresenta la lunghezza, ma l'ultimo indice numerico più uno.

Ad esempio, un singolo elemento con un indice molto alto fornisce un altrettanto grande lunghezza:

```js
let fruits = [];
fruits[123] = "Apple";

alert( fruits.length ); // 124
```

Ovviamente questo non è il modo corretto di utilizzare un array. 

Un'altra cosa interessante riguardo la proprietà `length` è che è sovrascrivibile.

Se provassimo ad incrementarla manualmente, non accadrebbe nulla di interessante. Se invece la decrementiamo, l'array verrà troncato. Il processo è irreversibile. Vediamo un esempio:

```js
let arr = [1, 2, 3, 4, 5];

arr.length = 2; // tronca a 2 elementi
alert( arr ); // [1, 2]

arr.length = 5; // ritorna alla lunghezza precedente
alert( arr[3] ); // undefined: i valori non vengono ritornati
```

Quindi il modo più semplice per ripulire un array è: `arr.length = 0;`.


## new Array()
C'è un ulteriore sintassi per creare un array:

```js
let arr = new Array("Apple", "Pear", "etc");
```

Viene utilizzata raramente, le parentesi `[]` risultano più brevi. Anche se c'è una caratteristica interessante che va osservata.

Se utilizziamo `new Array` con un solo argomento di tipo numerico, allora verrà creato un array *vuoto, ma con lunghezza data*.

Quindi vediamo come ci si potrebbe sparare da soli al piede:

```js
let arr = new Array(2); // creerà un array [2] ?

alert( arr[0] ); // undefined! nessun elemento.

alert( arr.length ); // length 2
```

Nel codice sopra, `new Array(number)` ha tutti gli elementi `undefined`.

Per evitare queste spiacevoli sorprese, solitamente si utilizzano le parentesi quadre, a meno di non sapere davvero che cosa si sta facendo.

## Array multi-dimensionali

Gli array possono contenere oggetti che sono a loro volta array. Possiamo quindi utilizzare questa proprietà per creare array multi-dimensionali, ad esempio per memorizzare matrici:

```js
let matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
];

alert( matrix[1][1] ); // l'elemento centrale
```

## toString

Gli array hanno una propria implementazione del metodo `toString`, il quale ritorna la lista degli elementi separati da una virgola.

Ad esempio:


```js
let arr = [1, 2, 3];

alert( arr ); // 1,2,3
alert( String(arr) === '1,2,3' ); // true
```

Proviamo anche:

```js
alert( [] + 1 ); // "1"
alert( [1] + 1 ); // "11"
alert( [1,2] + 1 ); // "1,21"
```

Gli array non possiedono `Symbol.toPrimitive`, e nemmeno `valueOf`; implementano solamente la conversione `toString`, quindi `[]` diventa una stringa vuota, `[1]` diventa `"1"` e `[1,2]` diventa `"1,2"`.

Quando l'operatore di somma binaria `"+"` aggiunge qualcosa ad una stringa, converte tutto a stringa, quindi l'esempio di prima sarà equivalente a:

```js
alert( "" + 1 ); // "1"
alert( "1" + 1 ); // "11"
alert( "1,2" + 1 ); // "1,21"
```

## Non confrontate gli array con ==

In JavaScript gli array, a differenza di altri linguaggi di programmazione, non dovrebbero essere confrontati con l'operatore `==`.

Questo operatore non offre alcun tipo di trattamento speciale per gli array: li considera come oggetti.

Ricordando velocemente le regole:

- Due oggetti sono uguali con `==` solamente se fanno riferimento allo stesso oggetto.
- Se uno dei due argomenti forniti all'operatore `==` è un oggetto, e l'altro è un tipo primitivo, allora l'oggetto viene convertito a primitivo, come spiegato nel capitolo [Conversione da oggetto a primitivi](/javascript/tutorial/object-toprimitive).
- ...Con l'eccezione di `null` e `undefined` che sono uguali solamente tra di loro.

Il confronto stretto con l'operatore `===` è ancora più semplice, poiché non converte i tipi. 

Quindi, se confrontiamo array con `==`, non saranno mai equivalenti, a meno chè non confrontiamo due variabili che fanno riferimento allo stesso array.

Ad esempio:
```js
alert( [] == [] ); // false
alert( [0] == [0] ); // false
```

Questi array sono tecnicamente oggetti differenti. Quindi non si equivalgono. L'operatore `==` non effettua il confronto elemento per elemento.

Anche il confronto con tipi primitivi potrebbe dare risultati strani:

```js
alert( 0 == [] ); // true

alert('0' == [] ); // false
```

Qui, in entrambi i casi, stiamo confrontando un tipo primitivo con un array. Quindi l'array `[]` viene convertito in tipo primitivo per effettuare il confronto e diventa una stringa vuota `''`. 

Successivamente il processo di confronto procede come descritto nel capitolo [Conversione di tipi](/javascript/tutorial/type-conversions):

```js
// dopo averlo convertito, l'array [] equivale a ''
alert( 0 == '' ); // true, poiché '' viene convertito nel numero 0

alert('0' == '' ); // false, nessuna conversione di tipo, sono stringhe differenti
```

Quindi, come possiamo confrontare gli array?

Molto semplice: non utilizzando l'operatore`==`. Invece, vanno confrontati con un ciclo che confronta ogni elemento dei due array, oppure utilizzando uno dei metodi di iterazione che vedremo nel prossimo capitolo.

## Riepilogo

Gli array sono uno speciale tipo di oggetto, studiati per immagazzinare e gestire collezioni ordinate di dati.

- La dichiarazione:

    ```js
    // parentesi quadre (usuale)
    let arr = [item1, item2...];

    // new Array (eccezionalmente raro)
    let arr = new Array(item1, item2...);
    ```

    La chiamata a `new Array(number)` crea un array con la lunghezza data, ma senza elementi.

- La proprietà `length` è la lunghezza dell'array; in realtà, per essere precisi, contiene l'indice dell'ultimo elemento più uno. Questo valore viene aggiornato automaticamente. 
- Se decrementiamo manualmente `length`, l'array viene troncato.

Possiamo eseguire sugli arrays le seguenti operazioni:

- `push(...items)` aggiunge `items` in coda.
- `pop()` rimuove un elemento dalla coda e lo ritorna.
- `shift()` rimuove un elemento dalla testa e lo ritorna.
- `unshift(...items)` aggiunge un elemento alla testa.

Per iterare sugli elementi di un array:

- `for (let i = 0; i < arr.length; i++)` - il più veloce, compatibile con i vecchi browsers.
- `for (let item of arr)` - la moderna sintassi, solo per gli elementi.
- `for (let i in arr) ` - da non usare.

Per confrontare gli array, non utilizzate l'operatore  `==` (lo stesso vale per `>`, `<` ecc), poiché non riservano alcun trattamento speciale per gli array. Li trattano come degli oggetti comuni, e solitamente non è quello che vogliamo.

Piuttosto si possono utilizzare i cicli come `for..of` per confrontare ogni elemento dei due array.

Continueremo con lo studio degli array e di altri metodi per aggiungere, rimuovere, estrarre elementi ed ordinarli, nel prossimo capitolo [Metodi per gli array](/javascript/tutorial/array-methods).

## Esercizi

### 1 · L'array è stato copiato?

Cosa mostrerà il codice sotto?

```js
let fruits = ["Apples", "Pear", "Orange"];

// inserisci un nuovo elemento dentro a "copy"
let shoppingCart = fruits;
shoppingCart.push("Banana");

// che cosa c'è in fruits?
alert( fruits.length ); // ?
```

::::: details Soluzione

La risposta è `4`:


```js
let fruits = ["Apples", "Pear", "Orange"];

let shoppingCart = fruits;

shoppingCart.push("Banana");


alert( fruits.length ); // 4

```

Questo perché gli array sono oggetti. Quindi `shoppingCart` e `fruits` sono riferimenti allo stesso array.

:::::

### 2 · Operazioni sugli array.

Proviamo 5 operazioni su un array.

1. Create un array `styles` con gli elementi "Jazz" e "Blues".
2. Aggiungete "Rock-n-Roll" in coda.
3. Rimpiazzate l'elemento al centro con "Classics". Il codice che utilizzerete per trovare il centro dovrebbe funzionare con qualsiasi array, anche di lunghezza dispari.
4. Prelevate il primo elemento dell'array e mostratelo.
5. Aggiungete in testa `Rap` e `Reggae` .

Le evoluzioni dell'array:

```js
Jazz, Blues
Jazz, Blues, Rock-n-Roll
Jazz, Classics, Rock-n-Roll
Classics, Rock-n-Roll
Rap, Reggae, Classics, Rock-n-Roll
```

::::: details Soluzione

```js
let styles = ["Jazz", "Blues"];
styles.push("Rock-n-Roll");
styles[Math.floor((styles.length - 1) / 2)] = "Classics";
alert( styles.shift() );
styles.unshift("Rap", "Reggae");
```

:::::

### 3 · Chiamata di funzione

Qual è il risultato? Perché?

```js
let arr = ["a", "b"];

arr.push(function() {
  alert( this );
})

arr[2](); // ?
```

::::: details Soluzione

La chiamata `arr[2]()` è sintatticamente equivalente a `obj[method]()`; al posto di `obj` abbiamo `arr`, e al posto di `method` abbiamo `2`.

Quindi abbiamo una chiamata al metodo `arr[2]`. Naturalmente, riceve il riferimento a `this` e ritorna l'array:

```js
let arr = ["a", "b"];

arr.push(function() {
  alert( this );
})

arr[2](); // a,b,function(){...}
```

L'array ha 3 valori: inizialmente ne ha due, successivamente viene aggiunta la funzione.

:::::

### 4 · Somma dei numeri inseriti

Scrivete una funzione  `sumInput()` che:

- Richiede all'utente dei valori tramite `prompt` e memorizza i valori in un array.
- Termina se l'utente inserisce un valore non numerico, una stringa vuota, o preme "Cancel".
- Calcola e ritorna la somma degli elementi dell'array.

P.S. Lo `0` è un numero valido, non deve interrompere l'input.

[Apri l’esempio nella fonte originale](https://it.javascript.info/array).

::::: details Soluzione

Da notare un dettaglio sottile ma importante. Non convertiamo immediatamente `value` ad un numero subito dopo averlo prelevato con `prompt`, perchè successivamente tramite `value = +value` non saremmo in grado di distinguere una stringa vuota da uno zero. Quindi è necessario eseguire la conversione in un secondo momento.


```js
function sumInput() {
 
  let numbers = [];

  while (true) {

    let value = prompt("A number please?", 0);

    // should we cancel?
    if (value === "" || value === null || !isFinite(value)) break;

    numbers.push(+value);
  }

  let sum = 0;
  for (let number of numbers) {
    sum += number;
  }
  return sum;
}

alert( sumInput() ); 
```

:::::

### 5 · Il sub-array massimo

Come input si ha un array di numeri, ad esempio `arr = [1, -2, 3, 4, -9, 6]`.

Il compito è: trovate il sub-array contiguo di `arr` con la massima somma degli elementi.

Scrivete la funzione `getMaxSubSum(arr)` che ritorna quella somma.

Ad esempio: 

```js
getMaxSubSum([-1, 2, 3, -9]) == 5 //(la somma degli elementi selezionati)
getMaxSubSum([2, -1, 2, 3, -9]) == 6
getMaxSubSum([-1, 2, 3, -9, 11]) == 11
getMaxSubSum([-2, -1, 1, 2]) == 3
getMaxSubSum([100, -9, 2, -3, 5]) == 100
getMaxSubSum([1, 2, 3]) == 6 //(include tutti)
```

Se tutti gli elementi sono negativi, non prendiamo nulla (il sotto-array è vuoto), quindi la somma è zero:

```js
getMaxSubSum([-1, -2, -3]) = 0
```

Provate a pensare ad una soluzione rapida: [O(n<sup>2</sup>)](https://en.wikipedia.org/wiki/Big_O_notation) o addirittura O(n) se riuscite.

::::: details Soluzione

#### La soluzione più lenta

Possiamo calcolare tutte le somme possibili.

La via più semplice è di prendere ogni elemento e calcolare la somma di tutti i sotto-array possibili.

Ad esempio, per `[-1, 2, 3, -9, 11]`:

```js
// Starting from -1:
-1
-1 + 2
-1 + 2 + 3
-1 + 2 + 3 + (-9)
-1 + 2 + 3 + (-9) + 11

// Starting from 2:
2
2 + 3
2 + 3 + (-9)
2 + 3 + (-9) + 11

// Starting from 3:
3
3 + (-9)
3 + (-9) + 11

// Starting from -9
-9
-9 + 11

// Starting from 11
11
```

Il codice è un ciclo annidato: il ciclo esterno processa tutti gli elementi dell'array, quello interno esegue le somme a partire dall'elemento corrente.

```js
function getMaxSubSum(arr) {
  let maxSum = 0; // if we take no elements, zero will be returned

  for (let i = 0; i < arr.length; i++) {
    let sumFixedStart = 0;
    for (let j = i; j < arr.length; j++) {
      sumFixedStart += arr[j];
      maxSum = Math.max(maxSum, sumFixedStart);
    }
  }

  return maxSum;
}

alert( getMaxSubSum([-1, 2, 3, -9]) ); // 5
alert( getMaxSubSum([-1, 2, 3, -9, 11]) ); // 11
alert( getMaxSubSum([-2, -1, 1, 2]) ); // 3
alert( getMaxSubSum([1, 2, 3]) ); // 6
alert( getMaxSubSum([100, -9, 2, -3, 5]) ); // 100
```

La soluzione ha una complessità di [O(n<sup>2</sup>)](https://en.wikipedia.org/wiki/Big_O_notation). In altre parole, se l'array fosse 2 volte più grande, l'algoritmo lavorerebbe 4 volte più lentamente.

Per grandi array (1000, 10000 o più elementi) questi algoritmi possono portare ad enormi attese.

#### Soluzione performante

Iniziamo ad esaminare l'array mantenendo la somma parziale degli elementi nella variabile `s`. Se `s` diventa negativa, allora assegniamo `s=0`. La somma di tutte queste `s` sarà la risposta.

Se la risposta vi sembra troppo vaga, date un'occhiata al codice:

```js
function getMaxSubSum(arr) {
  let maxSum = 0;
  let partialSum = 0;

  for (let item of arr) { // for each item of arr
    partialSum += item; // add it to partialSum
    maxSum = Math.max(maxSum, partialSum); // remember the maximum
    if (partialSum < 0) partialSum = 0; // zero if negative
  }

  return maxSum;
}

alert( getMaxSubSum([-1, 2, 3, -9]) ); // 5
alert( getMaxSubSum([-1, 2, 3, -9, 11]) ); // 11
alert( getMaxSubSum([-2, -1, 1, 2]) ); // 3
alert( getMaxSubSum([100, -9, 2, -3, 5]) ); // 100
alert( getMaxSubSum([1, 2, 3]) ); // 6
alert( getMaxSubSum([-1, -2, -3]) ); // 0
```

L'algoritmo richiede esattamente uno solo scorrimento dell'array, quindi la complessità è O(n).

Potete trovare maggiori dettagli riguardo l'algoritmo qui: [Maximum subarray problem](http://en.wikipedia.org/wiki/Maximum_subarray_problem). Se ancora non vi risulta ovvio il funzionamento, esaminate più in dettaglio il codice fornito sopra.

:::::

