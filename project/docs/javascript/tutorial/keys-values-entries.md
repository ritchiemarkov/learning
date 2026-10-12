---
title: "Object.keys, values, entries"
description: "JavaScript.info in italiano: Object.keys, values, entries"
sourceTutorial: true
prev: {"text": "WeakMap e WeakSet", "link": "/javascript/tutorial/weakmap-weakset"}
next: {"text": "Assegnamento di destrutturazione", "link": "/javascript/tutorial/destructuring-assignment"}
---

# Object.keys, values, entries

> **JavaScript.info · Ilya Kantor e contributori.** [Originale inglese](https://javascript.info/keys-values-entries) · [Edizione italiana](https://it.javascript.info/keys-values-entries) · [Fonti e licenza](/javascript/fonti).

Facciamo un passo oltre le strutture dati in sé e discutiamo dei metodi di iterazione su di esse. 

Nel capitolo precedente abbiamo visto i metodi `map.keys()`, `map.values()`, `map.entries()`.

Questi sono dei metodi generici, c'è un comune accordo sul loro utilizzo per le strutture dati. Se dovessimo mai creare una nostra struttura dati personale, dovremmo implementare anche questi metodi. 

Vengono supportati da:

- `Map`
- `Set`
- `Array`

Anche gli oggetti supportano dei metodi simili, ma la loro sintassi è leggermente differente.

## Object.keys, values, entries

Per i semplici oggetti, sono disponibili i seguenti metodi:

- [Object.keys(obj)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/keys) -- ritorna un array di chiavi.
- [Object.values(obj)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/values) -- ritorna un array di valori.
- [Object.entries(obj)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/entries) -- ritorna un array di coppie `[key, value]`.

Da notare le differenze (confrontandoli con quelli delle map):

|             | Map              | Object       |
|-------------|------------------|--------------|
| Chiamata | `map.keys()`  | `Object.keys(obj)`, non `obj.keys()` |
| Valore di ritorno     | oggetti iterabile    | Array                     |

La prima differenza è che dobbiamo chiamare `Object.keys(obj)`, non `obj.keys()`.

Perché? La principale motivazione è la flessibilità. Ricordate, gli oggetti sono la base di tutte le strutture complesse in JavaScript. Quindi potremmo avere un nostro oggetto come `order` che implementa il proprio metodo `order.values()`. E potremmo ancora chiamare `Object.values(order)`.

La seconda differenza è che i metodi `Object.*` ritornano un array, non un oggetto iterabile. Questo comportamento è dovuto a ragioni storiche.

Ad esempio:

```js
let user = {
  name: "John",
  age: 30
};
```

- `Object.keys(user) = ["name", "age"]`
- `Object.values(user) = ["John", 30]`
- `Object.entries(user) = [ ["name","John"], ["age",30] ]`

Qui un esempio di utilizzo di `Object.values` per eseguire cicli sui valori delle proprietà:

```js
let user = {
  name: "John",
  age: 30
};

// ciclo sui valori
for (let value of Object.values(user)) {
  alert(value); // John, poi 30
}
```


::: warning Object.keys/values/entries ignorano le proprietà di tipo symbol
Proprio come nel caso del ciclo `for..in`, questi metodi ignorano le proprietà che utilizzano `Symbol(...)` come chiave.

Solitamente questo è un vantaggio. Ma se volessimo ottenere anche le chiavi di tipo symbol, esiste un secondo metodo [Object.getOwnPropertySymbols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/getOwnPropertySymbols)  che ritorna un array di chiavi di tipo symbol. Invece, il metodo [Reflect.ownKeys(obj)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/ownKeys) ritorna *tutte* le chiavi.
:::


## Trasformare gli oggetti

Per gli oggetti mancano molti metodi che sono invece presenti per gli array, ad esempio `map`, `filter` e molti altri.

Se volessimo comunque applicarli, allora possiamo utilizzare `Object.entries` seguito da `Object.fromEntries`:

1. Applichiamo `Object.entries(obj)` per ottenere un array di coppie chiave/valore da `obj`.
2. Applichiamo il metodo, ad esempio `map`.
3. Applichiamo `Object.fromEntries(array)` all'array risultante per ottenere nuovamente un oggetto.

Ad esempio, se abbiamo un oggetto di prezzi che vogliamo raddoppiare:

```js
let prices = {
  banana: 1,
  orange: 2,
  meat: 4,
};


let doublePrices = Object.fromEntries(
  // converte ad array, chiama map, e successivamente fromEntries ci ritorna l'oggetto
  Object.entries(prices).map(([key, value]) => [key, value * 2])
);


alert(doublePrices.meat); // 8
```

Ad un primo sguardo potrebbe risultare complesso, ma diventa molto più familiare dopo un paio di utilizzi. In questo modo possono essere create potenti catene per la trasformazione.

## Esercizi

### 1 · Sommare le proprietà

Abbiamo un oggetto `salaries` con un numero arbitrario di salari. 

Scrivete la funzione `sumSalaries(salaries)` che ritorna la somma di tutti i salari utilizzando `Object.values` e il ciclo `for..of`.

Se `salaries` è vuoto, allora il risultato deve essere `0`.

Ad esempio:

```js
let salaries = {
  "John": 100,
  "Pete": 300,
  "Mary": 250
};

alert( sumSalaries(salaries) ); // 650
```

::::: details Soluzione

```js
function sumSalaries(salaries) {

  let sum = 0;
  for (let salary of Object.values(salaries)) {
    sum += salary;
  }

  return sum; // 650
}

let salaries = {
  "John": 100,
  "Pete": 300,
  "Mary": 250
};

alert( sumSalaries(salaries) ); // 650
```
O, in alternativa, possiamo ottenere la somma utilizzando `Object.values` e `reduce`:

```js
// reduce itera su un array con i salari,
// li sommiamo
// e ritorniamo il risultato
function sumSalaries(salaries) {
  return Object.values(salaries).reduce((a, b) => a + b, 0) // 650
}
```

:::::

### 2 · Conteggio proprietà

Scrivete una funzione `count(obj)` che ritorna il numero di proprietà dell'oggetto:

```js
let user = {
  name: 'John',
  age: 30
};

alert( count(user) ); // 2
```

Cercate di rendere il codice il più breve possibile.

P.S. Ignorate le proprietà di tipo symbol, tenete conto solamente di quelle "regolari".

::::: details Soluzione



:::::

