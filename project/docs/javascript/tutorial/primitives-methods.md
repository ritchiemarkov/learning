---
title: "Metodi dei tipi primitivi"
description: "JavaScript.info in italiano: Metodi dei tipi primitivi"
sourceTutorial: true
prev: {"text": "Conversione da oggetto a primitivi", "link": "/javascript/tutorial/object-toprimitive"}
next: {"text": "Numeri", "link": "/javascript/tutorial/number"}
---

# Metodi dei tipi primitivi

> **JavaScript.info · Ilya Kantor e contributori.** [Originale inglese](https://javascript.info/primitives-methods) · [Edizione italiana](https://it.javascript.info/primitives-methods) · [Fonti e licenza](/javascript/fonti).

JavaScript ci consente di trattare i tipi primitivi (stringhe, numeri, etc.) come se fossero oggetti.

Mette a disposizione diversi metodi per farlo, che molto presto studieremo, prima però dobbiamo capire come funzionano, perché ovviamente i tipi primitivi non sono oggetti (cercheremo quindi di fare chiarezza).

Vediamo quali sono i punti chiave che distinguono i tipi primitivi dagli oggetti.

Un primitivo

- E' un valore di tipo primitivo.
- Esistono 6 tipi primitivi: `string`, `number`, `bigint`, `boolean`, `symbol`, `null` e `undefined`.

Un oggetto

- E' in grado di memorizzare molti valori come proprietà.
- Può essere creato con `{}`, ad esempio: `{name: "John", age: 30}`. Ci sono altri tipi di oggetto in JavaScript; le funzioni ad esempio sono oggetti.

Uno dei principali vantaggi degli oggetti, è che questi possono essere utilizzati per memorizzare funzioni come loro proprietà.

```js
let john = {
  name: "John",
  sayHi: function() {
    alert("Hi buddy!");
  }
};

john.sayHi(); // Hi buddy!
```

In questo esempio abbiamo creato un oggetto `john` con il metodo `sayHi`.

Esistono diversi oggetti built-in (integrati nel linguaggio), come quelli dedicati alla manipolazione delle date, degli errori, degli elementi HTML, etc. I quali possiedono diverse proprietà e metodi.

Ma tutte queste caratteristiche hanno un costo!

Gli oggetti sono più "pesanti" dei tipi primitivi. Richiedono risorse extra per supportarne il pieno funzionamento. Ma poiché queste proprietà sono fondamentali, JavaScript cerca di ottimizzarne l'utilizzo della memoria.

## Un primitivo come un oggetto

Questo è il paradosso contro cui si è scontato il creatore di JavaScript:

- Esistono molte operazioni che uno sviluppatore vorrebbe poter fare con i diversi tipi primitivi, come una stringhe o un numeri. Sarebbe molto bello poter accedere a dei metodi per questi tipi di dato.
- I tipi primitivi devono essere veloci e il più leggeri possibile.

La soluzione sembra un po' strana:

1. I primitivi rimangono primitivi. Contengono un singolo valore.
2. Il linguaggio consente di accedere alle proprietà e ai metodi di stringhe, numeri, booleani e symbol.
3. Quando questo accade, viene creato uno speciale "oggetto contenitore" che fornisce le funzionalità extra, successivamente questo verrà distrutto.

Gli "oggetti contenitore" sono diversi per ogni primitiva e sono chiamati: `String`, `Number`, `Boolean` e `Symbol`. Questi forniscono diversi insiemi di metodi.

Ad esempio, esiste un metodo [str.toUpperCase()](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/String/toUpperCase) che ritorna la stringa con la prima lettera maiuscola.

Funziona in questo modo:

```js
let str = "Hello";

alert( str.toUpperCase() ); // HELLO
```

Semplice, vero?  Questo è quello che accade realmente in `str.toUpperCase()`:

1. La stringa `str` è una variabile primitiva. Quindi nel momento in cui si accede ad una sua proprietà, viene creato uno speciale oggetto che memorizza il valore della stringa, e contiene metodi utili come `toUpperCase()`.
2. Questo metodo viene eseguito e ritorna una nuova stringa (mostrata da `alert`).
3. L'oggetto speciale viene distrutto, lasciando solamente la primitiva `str`.

In questo modo i primitivi possono sfruttare i vantaggi forniti dall'utilizzo dei metodi, rimanendo allo stesso tempo molto leggeri.

JavaScript cerca di ottimizzare il più possibile questo processo. In alcuni casi riesce ad evitare la creazione di oggetti inutili. Nonostance ciò, deve comunque aderire alle specifiche, quindi il comportamento deve essere simile a quello che si avrebbe con la creazione di un oggetto.

Un variabile di tipo number ha dei propri metodi, ad esempio [toFixed(n)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/toFixed) che arrotonda il numero alla precisione richiesta:

```js
let n = 1.23456;

alert( n.toFixed(2) ); // 1.23
```

Vedremo più nello specifico altri metodi nei capitoli [Numeri](/javascript/tutorial/number) e [Stringhe](/javascript/tutorial/string).



:::: warning I costruttori di `String/Number/Boolean` vengono utilizzati solo internamente
Alcuni linguaggi come Java ci consento di creare "oggetti contenitori" esplicitamente utilizzando la sintassi `new Number(1)` o `new Boolean(false)`.

In JavaScript, è altrettanto possibile per ragioni storiche, ma è altamente **sconsigliato**. Poiché molte cose potrebbero non funzionare come dovrebbero.

Ad esempio:

```js
alert( typeof 0 ); // "number"

alert( typeof new Number(0) ); // "object"!
```

Gli oggetti valutati da un `if` sono sempre true, quindi il seguente alert verrà mostrato sempre:

```js
let zero = new Number(0);

if (zero) { // zero è true, perché è un oggetto
  alert( "zero is truthy?!?" );
}
```

In altre parole, utilizzare le stesse funzioni con `String/Number/Boolean` senza `new` è completamente sicuro. Poiché le variabili primitive verranno convertite all'oggetto corrispondente: ad una stringa, ad un numero, o ad un bool.

Ad esempio, il seguente codice è corretto:
```js
let num = Number("123"); // converte una string in number
```
::::



:::: warning null/undefined non hanno metodi
I primitivi speciali `null` e `undefined` sono delle eccezioni. Non possiedono degli speciali "oggetti contenitori", quindi non forniscono metodi. In questo senso, sono "molto primitivi".

Un tentativo di accedere ad una proprietà con questi tipi di valore, ritornerà un errore:

```js
alert(null.test); // errore
```

## Riepilogo

- I primitivi, ad eccezione di `null` e `undefined` forniscono molti metodi utili. Li studieremo nei prossimi capitoli.
- Formalmente, questi metodi lavorano su oggetti temporanei, JavaScript però è ottimizzato per sfruttare al meglio le risorse, non risultano quindi molto "costosi".
::::

## Esercizi

### 1 · Posso aggiungere una proprietà ad una stringa?

Considerate il seguente codice:

```js
let str = "Hello";

str.test = 5;

alert(str.test);
```

Cosa ne pensate, potrebbe funzionare? Cosa verrebbe mostrato?

::::: details Soluzione

Provate ad eseguirlo:

```js
let str = "Hello";

str.test = 5; // (*)

alert(str.test);
```

Potremmo ottenere due diversi risultati:
1. `undefined`
2. Un errore (strict mode).

Perché? Proviamo ad esaminare cosa succede alla riga `(*)`:

1. Quando si prova ad accedere ad una proprietà di `str`, viene creato un "oggetto contenitore".
2. L'operazione di accesso viene eseguito su questo. Quindi l'oggetto ottiene la proprietà `test`.
3. L'operazione termina e "l'oggetto contenitore" viene distrutto.

Quindi, nell'ultima riga di codice, `str` non possiede alcuna traccia di quella proprietà. Viene creato un nuovo oggetto per ogni operazione su un tipo stringa.

**Questo esempio mostra chiaramente che le variabili primitive non sono oggetti.**

Le variabili di tipo primitivo infatti non possono memorizzare dati.

:::::

