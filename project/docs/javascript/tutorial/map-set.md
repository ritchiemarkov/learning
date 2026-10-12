---
title: "Map e Set"
description: "JavaScript.info in italiano: Map e Set"
sourceTutorial: true
prev: {"text": "Iteratori", "link": "/javascript/tutorial/iterable"}
next: {"text": "WeakMap e WeakSet", "link": "/javascript/tutorial/weakmap-weakset"}
---

# Map e Set

> **JavaScript.info · Ilya Kantor e contributori.** [Originale inglese](https://javascript.info/map-set) · [Edizione italiana](https://it.javascript.info/map-set) · [Fonti e licenza](/javascript/fonti).

Finora abbiamo appreso le nozioni di base riguardo le seguenti strutture dati:

- Oggetti, per la memorizzazione di collezioni identificate da una chiave.
- Array, per la memorizzazione di collezioni ordinate.

Queste però non sono sufficienti. Esistono ulteriori strutture dati, come `Map` e `Set`.

## Map

[Map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map) è una collezione di dati identificati da chiavi, proprio come un `Object` (Oggetto). La principale differenza è che `Map` accetta chiavi di qualsiasi tipo.

I metodi e le proprietà sono:

- `new Map()` -- crea la mappa.
- `map.set(key, value)` -- memorizza il valore `value` con la chiave `key`.
- `map.get(key)` -- ritorna il valore associato alla chiave `key`, `undefined` nel caos in cui `key` non esista.
- `map.has(key)` -- ritorna `true` se la chiave `key` esiste, `false` altrimenti.
- `map.delete(key)` -- rimuove il valore con la chiave `key`.
- `map.clear()` -- rimuove tutti gli elementi.
- `map.size` -- ritorna il numero di elementi contenuti.

Ad esempio:

```js
let map = new Map();

map.set('1', 'str1');   // una chiave di tipo stringa
map.set(1, 'num1');     // una chiave di tipo numerico
map.set(true, 'bool1'); // una chiave di tipo booleano

// ricordi gli oggetti standard? convertirebbero le chiavi a stringa
// Map invece mantiene il tipo, quindi i seguenti esempi sono differenti:
alert( map.get(1)   ); // 'num1'
alert( map.get('1') ); // 'str1'

alert( map.size ); // 3
```

Come abbiamo potuto osservare, a differenza degli oggetti, le chiavi non vengono convertite a stringa. Sono quindi ammesse chiavi di qualunque tipo.


::: tip `map[key]` non è il modo corretto di utilizzare una `Map`
Anche se `map[key]` funziona, ad esempio possiamo impostare `map[key] = 2`, questo equivale a trattare`map` come un oggetto semplice, con tutte le limitazioni correlate.

Quindi dovremmo utilizzare i metodi dedicati a `map`: `set`, `get` e gli altri.
:::

**Map può utilizzare anche oggetti come chiave.**

Ad esempio:

```js
let john = { name: "John" };

// per ogni utente, memorizziamo il contatore delle visite
let visitsCountMap = new Map();

// john è la chiave
visitsCountMap.set(john, 123);

alert( visitsCountMap.get(john) ); // 123
```

Il fatto di poter utilizzare oggetti come chiavi è una delle caratteristiche più importanti fornite dalla struttura dati `Map`. In un normale `Object` una chiave di tipo stringa può andare bene, ma non vale lo stesso per le chiavi di tipo oggetto.

Proviamo:

```js
let john = { name: "John" };
let ben = { name: "Ben" };

visitsCountObj[ben] = 234; // proviamo ad utilizzare l'oggetto ben come chiave
visitsCountObj[john] = 123; // proviamo ad utilizzare l'oggetto jhon come chiave, l'oggetto ben verrà sostituito


//  Questo è quello che otteniamo!
alert( visitsCountObj["[object Object]"] ); // 123

```

Dal momento che `visitsCountObj` è un oggetto, converte tutte le chiavi, come `john` e `ben`, a stringhe, quindi otteniamo la chiave `"[object Object]"`. Senza dubbio non ciò che ci aspettavamo.


::: tip Come `Map` confronta le chiavi
Per verificare l'equivalenza delle chiavi, `Map`utilizza l'algoritmo [SameValueZero](https://tc39.github.io/ecma262/#sec-samevaluezero). E' quasi la stessa cosa dell'uguaglianza stretta `===`, con la differenza che `NaN` viene considerato uguale a `NaN`. Quindi anche `NaN` può essere utilizzato come chiave.

L'algoritmo di confronto non può essere né cambiato né modificato.
:::


:::: tip concatenamento
Ogni chiamata a `map.set` ritorna la mappa stessa, quindi possiamo concatenare le chiamate:

```js
map.set('1', 'str1')
  .set(1, 'num1')
  .set(true, 'bool1');
```
::::

## Iterare su Map

Per iterare attraverso gli elementi di `Map`, esistono 3 metodi:

- `map.keys()` -- ritorna un oggetto per iterare sulle chiavi,
- `map.values()` -- ritorna un oggetto per iterare sui valori,
- `map.entries()` -- ritorna un oggetto per iterare sulle coppie `[key, value]`, ed è il metodo utilizzato di default nel ciclo `for..of`.

Ad esempio:

```js
let recipeMap = new Map([
  ['cucumber', 500],
  ['tomatoes', 350],
  ['onion',    50]
]);

// itera sulle chiavi (vegetables)
for (let vegetable of recipeMap.keys()) {
  alert(vegetable); // cucumber, tomatoes, onion
}

// itera sui valori (amounts)
for (let amount of recipeMap.values()) {
  alert(amount); // 500, 350, 50
}

// itera sulle voci [key, value]
for (let entry of recipeMap) { // equivale a recipeMap.entries()
  alert(entry); // cucumber,500 (and so on)
}
```


::: tip Viene utilizzato l'ordine di inserimento
L'iterazione segue l'ordine di inserimento dei valori. `Map` mantiene l'ordine, a differenza degli `Object`.
:::

Inoltre, `Map` possiede un suo metodo `forEach`, simile a quello utilizzato dagli `Array`:

```js
// esegue la funzione per ogni coppia (chiave, valore)
recipeMap.forEach( (value, key, map) => {
  alert(`${key}: ${value}`); // cucumber: 500 etc
});
```

## Object.entries: Map da Object

Durante la fase di creazione di una `Map`, possiamo passarle un array (o qualsiasi altra struttura dati iterabile) con coppie chiave/valore per inizializzare la `Map`, come nel seguente esempio:

```js
// array di coppie [chiave, valore] 
let map = new Map([
  ['1',  'str1'],
  [1,    'num1'],
  [true, 'bool1']
]);

alert( map.get('1') ); // str1
```

Se abbiamo un semplice oggetto, e vogliamo utilizzarlo per creare una `Map`, possiamo utilizzare un metodo integrato degli oggetti [Object.entries(obj)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/entries) il quale ritorna un array di coppie chiave/valore nello stesso formato.

Quindi possiamo creare una `Map` da un oggetto, così:

```js
let obj = {
  name: "John",
  age: 30
};


let map = new Map(Object.entries(obj));


alert( map.get('name') ); // John
```

In questo esempio, `Object.entries` ritorna un array di coppie chiave/valore: `[ ["name","John"], ["age", 30] ]`. Che è quello di cui `Map` ha bisogno.


## Object.fromEntries: Object da Map

Abbiamo appena visto come creare una `Map` partendo da un oggetto con `Object.entries(obj)`.

Esiste un metodo `Object.fromEntries` che fa esattamente l'opposto: dato un array di coppie `[key, value]`, ne crea un oggetto:

```js
let prices = Object.fromEntries([
  ['banana', 1],
  ['orange', 2],
  ['meat', 4]
]);

// ora prices = { banana: 1, orange: 2, meat: 4 }

alert(prices.orange); // 2
```

Possiamo utilizzare il metodo `Object.fromEntries` per ottenere un oggetto partendo da una `Map`.

Ad esempio, memorizziamo i dati in una `Map`, ma abbiamo bisogno di passarla ad un codice di terze parti che si aspetta un oggetto.

Quindi:

```js
let map = new Map();
map.set('banana', 1);
map.set('orange', 2);
map.set('meat', 4);


let obj = Object.fromEntries(map.entries()); // costruisce un oggetto (*)


// fatto!
// obj = { banana: 1, orange: 2, meat: 4 }

alert(obj.orange); // 2
```

Una chiamata a `map.entries()` ritorna un array di coppie chiave/valore, esattamente nel formato richiesto da `Object.fromEntries`.

Possiamo rendere la riga `(*)` ancora più corta:
```js
let obj = Object.fromEntries(map); // omettendo .entries()
```

L'espressione è equivalente, poiché `Object.fromEntries` si aspetta di ricevere un oggetto iterabile come argomento. Non necessariamente un array. E l'iterazione standard per `Map` ritorna le stesse coppie chiave/valore di `map.entries()`. Quindi abbiamo ottenuto un oggetto con le stesse coppie chiave/valore della `map`.

## Set

Un `Set` è un tipo di collezione speciale - "set di valori" (senza chiavi), dove ogni valore può apparire una sola volta.

I suoi metodi principali sono:

- `new Set(iterable)` -- crea il set, e se gli viene fornito un oggetto `iterabile` (solitamente un array), ne copia i valori nel set.
- `set.add(value)` -- aggiunge un valore, ritorna il set.
- `set.delete(value)` -- rimuove il valore, ritorna `true` se `value` esiste, altrimenti `false`.
- `set.has(value)` -- ritorna `true` se il valore esiste nel set, altrimenti `false`.
- `set.clear()` -- rimuove tutti i valori dal set.
- `set.size` -- ritorna il numero dei valori contenuti.

La principale caratteristica dei set è che ripetute chiamate di `set.add(value)` con lo stesso valore non fanno nulla. Questo è il motivo per cui in un `Set` ogni valore può comparire una sola volta.

Ad esempio, abbiamo diversi arrivi di visitatori, e vorremmo ricordarli tutti. Ma visite ripetute dello stesso utente non dovrebbe portare a duplicati. Un visitatore deve essere conteggiato una volta sola.

`Set` è esattamente la struttura dati che fa al caso nostro:

```js
let set = new Set();

let john = { name: "John" };
let pete = { name: "Pete" };
let mary = { name: "Mary" };

// visitatori, alcuni potrebbero tornare più volte
set.add(john);
set.add(pete);
set.add(mary);
set.add(john);
set.add(mary);

// set mantiene solo valori unici
alert( set.size ); // 3

for (let user of set) {
  alert(user.name); // John (poi Pete e Mary)
}
```

L'alternativa a `Set` potrebbe essere un array di visitatori, e un codice per verificare ogni inserimento ed evitare duplicati, utilizzando [arr.find](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/find). Ma la performance sarebbe molto inferiore, perché questo metodo attraversa tutto l'array per verificare ogni elemento. `Set` è ottimizzato internamente per il controllo di unicità.

## Iterare un Set

Possiamo iterare un set sia con `for..of` che con `forEach`:

```js
let set = new Set(["oranges", "apples", "bananas"]);

for (let value of set) alert(value);

// equivalente con forEach:
set.forEach((value, valueAgain, set) => {
  alert(value);
});
```

Da notare una cosa divertente. La funzione callback fornita a `forEach` ha 3 argomenti: un `value`, poi *lo stesso valore* `valueAgain`, e poi l'oggetto riferito da `this`. Proprio così, lo stesso valore appare due volte nella lista degli argomenti.

Questo accade per questioni di compatibilità con `Map`, in cui la funzione callback fornita al `forEach` possiede tre argomenti. E' un po' strano, ma in alcuni casi può aiutare rimpiazzare `Map` con `Set`, e vice versa.

Sono supportati anche i metodi di iterazione di `Map`:

- `set.keys()` -- ritorna un oggetto per iterare sui valori,
- `set.values()` -- lo stesso di `set.keys()`, per compatibilità con `Map`,
- `set.entries()` -- ritorna un oggetto per iterare sulle voci `[value, value]`, esiste per compatibilità con `Map`.

## Riepilogo

`Map` è una collezione di valori identificati da chiave.

Metodi e proprietà:

- `new Map([iterable])` -- crea la mappa, accetta un oggetto iterabile (opzionale, e.g. array) di coppie `[key,value]` per l'inizializzazione.
- `map.set(key, value)` -- memorizza il valore con la chiave fornita.
- `map.get(key)` -- ritorna il valore associato alla chiave, `undefined` se la `key` non è presente nella `Map`.
- `map.has(key)` -- ritorna `true` se la `key` esiste, `false` altrimenti.
- `map.delete(key)` -- rimuove il valore associato alla chiave.
- `map.clear()` -- rimuove ogni elemento dalla mappa.
- `map.size` -- ritorna il numero di elementi contenuti nella `map`.

Le differenze da un `Object` standard:

- Le chiavi possono essere di qualsiasi tipo, anche oggetti.
- Possiede metodi aggiuntivi, come la proprietà `size`.

`Set` è una collezione di valori unici.

Metodi e proprietà:

- `new Set([iterable])` -- crea un set, accetta un oggetto iterabile (opzionale, e.g. array) per l'inizializzazione.
- `set.add(value)` -- aggiunge un valore (non fa nulla nel caso in cui il valore sia già contenuto nel set), e ritorna il set.
- `set.delete(value)` -- rimuove il valore, ritorna `true` se `value` esiste, `false` altrimenti.
- `set.has(value)` -- ritorna `true` se il valore esiste nel set, `false` altrimenti.
- `set.clear()` -- rimuove tutti i valori dal set.
- `set.size` -- ritorna il numero di valori contenuti.

L'iterazione su `Map` e `Set` segue sempre l'ordine di inserimento, quindi possono essere definite delle collezioni ordinate; non è però possibile riordinare gli elementi oppure ottenere un valore tramite il suo indice.

## Esercizi

### 1 · Filtrare gli elementi dell'array unici

Avete un array `arr`.

Create una funzione `unique(arr)` che ritorni un array con tutti gli elementi unici presi da `arr`.

Ad esempio:

```js
function unique(arr) {
  /* your code */
}

let values = ["Hare", "Krishna", "Hare", "Krishna",
  "Krishna", "Krishna", "Hare", "Hare", ":-O"
];

alert( unique(values) ); // Hare, Krishna, :-O
```

P.S. Qui vengono utilizzate stringhe, ma potrebbero essere valori di qualsiasi tipo.

P.P.S. utilizzate `Set` per memorizzare valori unici.

::::: details Soluzione



:::::

### 2 · Filtrare anagrammi

Gli [anagrammi](https://en.wikipedia.org/wiki/Anagram) sono parole che hanno le stesse lettere, ma in un ordine differente.

Ad esempio:

```
nap - pan
ear - are - era
cheaters - hectares - teachers
```

Scrivete una funzione `aclean(arr)` che ritorna un array ripulito dagli anagrammi.

Ad esempio:

```js
let arr = ["nap", "teachers", "cheaters", "PAN", "ear", "era", "hectares"];

alert( aclean(arr) ); // "nap,teachers,ear" or "PAN,cheaters,era"
```

Da ogni gruppo di anagrammi dovrebbe rimanere solamente una parola, non ha importanza quale.

::::: details Soluzione

Per trovare tutti gli anagrammi, dividiamo ogni parola in lettere ed ordiniamole. Con le lettere ordinate, tutti gli anagrammi sono uguali.

Ad esempio:

```
nap, pan -> anp
ear, era, are -> aer
cheaters, hectares, teachers -> aceehrst
...
```

Utilizzeremo la variante con le lettere ordinate come chiave di una map per memorizzare un solo valore:

```js
function aclean(arr) {
  let map = new Map();

  for (let word of arr) {
    // dividi la parola in lettere, ordinale e ricongiungile 

    let sorted = word.toLowerCase().split('').sort().join(''); // (*)

    map.set(sorted, word);
  }

  return Array.from(map.values());
}

let arr = ["nap", "teachers", "cheaters", "PAN", "ear", "era", "hectares"];

alert( aclean(arr) );
```

L'ordinamento delle lettere è fatto dalla concatenazione di chiamate alla riga `(*)`.

Per convenzione le dividiamo in più linee:

```js
let sorted = word // PAN
  .toLowerCase() // pan
  .split('') // ['p','a','n']
  .sort() // ['a','n','p']
  .join(''); // anp
```

Due parole diverse `'PAN'` e `'nap'` possiedono la stessa forma in lettere ordinate `'anp'`.

La prossima lettera inserirà la parola nella map:

```js
map.set(sorted, word);
```

Se abbiamo già incontrato una parola con la stessa forma, la sovrascriviamo con quella nuova, in modo tale da avere sempre una sola occorrenza all'interno della map. 

Alla fine `Array.from(map.values())` prende un iteratore sui valori di `map` (non abbiamo bisogno delle chiavi nel risultato) e ne ritorna un array.

Qui potremmo anche utilizzare un normale oggetto piuttosto di `Map`, poiché le chiavi sono stringhe.

Questo è un esempio di possibile soluzione:

```js
function aclean(arr) {
  let obj = {};

  for (let i = 0; i < arr.length; i++) {
    let sorted = arr[i].toLowerCase().split("").sort().join("");
    obj[sorted] = arr[i];
  }

  return Object.values(obj);
}

let arr = ["nap", "teachers", "cheaters", "PAN", "ear", "era", "hectares"];

alert( aclean(arr) );
```

:::::

### 3 · Chiavi iterabili

Vorremmo avere un array di `map.keys()` in una variabile, quindi potergli applicare un metodo specifico degli arrays, ad esempio `.push`.

Ma c'è un problema:

```js
let map = new Map();

map.set("name", "John");

let keys = map.keys();


// Error: keys.push is not a function
keys.push("more");

```

Perché? Come possiamo sistemare il codice per rendere `keys.push` funzionante?

::::: details Soluzione

Questo accade perchè `map.keys()` ritorna un oggetto iterabile, non un array.

Possiamo convertirlo in un array utilizzando `Array.from`:


```js
let map = new Map();

map.set("name", "John");


let keys = Array.from(map.keys());


keys.push("more");

alert(keys); // name, more
```

:::::

