---
title: "Metodi per gli array"
description: "JavaScript.info in italiano: Metodi per gli array"
sourceTutorial: true
prev: {"text": "Array", "link": "/javascript/tutorial/array"}
next: {"text": "Iteratori", "link": "/javascript/tutorial/iterable"}
---

# Metodi per gli array

> **JavaScript.info · Ilya Kantor e contributori.** [Originale inglese](https://javascript.info/array-methods) · [Edizione italiana](https://it.javascript.info/array-methods) · [Fonti e licenza](/javascript/fonti).

Gli array forniscono una gran quantità di metodi. Per rendere le cose più semplici, in questo capitolo li abbiamo divisi per gruppi.

## Aggiungere/rimuovere elementi 

Conosciamo già i metodi che consentono di aggiungere e rimuovere elementi:

- `arr.push(...items)` -- aggiunge un elemento in coda,
- `arr.pop()` -- estrae un elemento dalla coda,
- `arr.shift()` -- estrae un elemento dalla testa,
- `arr.unshift(...items)` -- aggiunge un elemento in testa.

Vediamone altri.

### splice

Come cancellare un elemento dall'array?

Gli array sono oggetti, quindi possiamo provare ad utilizzare `delete`:

```js
let arr = ["I", "go", "home"];

delete arr[1]; // rimuove "go"

alert( arr[1] ); // undefined

// ora arr = ["I",  , "home"];
alert( arr.length ); // 3
```

L'elemento viene rimosso, ma l'array ha ancora 3 elementi, possiamo vederlo tramite `arr.length == 3`.

Non è una sorpresa, perché `delete obj.key` rimuove un valore dalla `key`. Questo è tutto quello che fa. Può andare bene per gli oggetti. Con gli array vorremmo che il resto degli elementi scalassero, andando ad occupare il posto che si è liberato. Per questo ci aspetteremmo di avere un array più corto.

Per questo scopo sono stati sviluppati dei metodi dedicati.

Il metodo [arr.splice](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice) è un coltellino svizzero per array. Può fare qualsiasi cosa: aggiungere e rimuovere elementi, ovunque.

La sintassi è:

```js
arr.splice(start[, deleteCount, elem1, ..., elemN])
```

Modifica l'array partendo dall'indice `start`; rimuove `deleteCount` elementi ed inserisce `elem1, ..., elemN`. Infine ritorna un array contenente gli elementi rimossi.

Questo metodo è facile da capire tramite esempi.

Proviamo ad eliminare degli elementi:

```js
let arr = ["I", "study", "JavaScript"];


arr.splice(1, 1); // a partire da indice 1 rimuove 1 elemento


alert( arr ); // ["I", "JavaScript"]
```

Facile, vero? Ha rimosso `1` elemento, a partire dall'elemento `1`.

Nel prossimo esempio, rimuoviamo 3 elementi e li rimpiazziamo con altri due:

```js
let arr = ["I", "study", "JavaScript", "right", "now"];

// rimuove i primi 3 elementi e li rimpiazza con altri
arr.splice(0, 3, "Let's", "dance");

alert( arr ) // ora ["Let's", "dance", "right", "now"]
```

Possiamo vedere l'array ritornato da `splice` contenente gli elementi rimossi:

```js
let arr = ["I", "study", "JavaScript", "right", "now"];

// rimuove i primi 2 elementi
let removed = arr.splice(0, 2);

alert( removed ); // "I", "study" <-- array di elementi rimossi
```

Il metodo `splice` è anche in grado di inserire elementi senza alcuna rimozione. Per ottenere questo dobbiamo impostare `deleteCount` a `0`:

```js
let arr = ["I", "study", "JavaScript"];

// da indice 2
// ne rimuove 0
// poi inserisce "complex" e "language"
arr.splice(2, 0, "complex", "language");

alert( arr ); // "I", "study", "complex", "language", "JavaScript"
```


:::: tip Sono permessi indici negativi
In questo come in altri metodi dedicati agli array, sono permessi indici negativi. Essi specificano la posizione dalla fine dell'array, come:

```js
let arr = [1, 2, 5];

// dall'indice -1 (un passo dalla fine)
// cancella 0 elementi,
// poi inserisce 3 e 4
arr.splice(-1, 0, 3, 4);

alert( arr ); // 1,2,3,4,5
```
::::

### slice

Il metodo [arr.slice](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice) è più semplice di `arr.splice`.

La sintassi è:

```js
arr.slice([start], [end])
```

Ritorna un nuovo array contente tutti gli elementi a partire da `"start"` fino ad `"end"` (`"end"` escluso). Sia `start` che `end` possono essere negativi; in tal caso si inizierà a contare dalla coda dell'array.

Funziona come `str.slice`, ma crea dei sotto-array piuttosto che sotto-stringhe.

Ad esempio:

```js
let arr = ["t", "e", "s", "t"];

alert( arr.slice(1, 3) ); // e,s (copia da 1 a 3)

alert( arr.slice(-2) ); // s,t (copia da -2 fino alla fine)
```

Possiamo anche utilizzarlo senza argomenti: `arr.slice()` crea una copia di `arr`. Questo tipo di chiamata è spesso utilizzata per creare una copia con cui poter liberamente lavorare senza modificare l'array originale. 

### concat

Il metodo [arr.concat](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/concat) crea un nuovo array che include valori di altri array, o elementi aggiuntivi.

La sintassi è:

```js
arr.concat(arg1, arg2...)
```

Accetta un numero arbitrario di argomenti -- sia array che valori.

Il risultato è un nuovo array contenente gli elementi di `arr`, seguiti da `arg1`, `arg2` etc.

Se un argomento `argN` è un array, tutti i suoi elementi vengono copiati. Altrimenti viene copiato solamente l'argomento stesso.

Un esempio:

```js
let arr = [1, 2];

// unisce arr con [3,4]
alert( arr.concat([3, 4])); // 1,2,3,4

// unisce arr con [3,4] e [5,6]
alert( arr.concat([3, 4], [5, 6])); // 1,2,3,4,5,6

// unisce arr con [3,4], poi aggiunge i valori 5 e 6
alert( arr.concat([3, 4], 5, 6)); // 1,2,3,4,5,6
```

Normalmente copia elementi da un array. Gli altri oggetti, anche se assomigliano molto ad un array, vengono aggiunti interamente:

```js
let arr = [1, 2];

let arrayLike = {
  0: "something",
  length: 1
};

alert( arr.concat(arrayLike) ); // 1,2,[object Object]
```

...Se, invece, un oggetto simile ad un array possiede la proprietà `Symbol.isConcatSpreadable`, allora viene trattato come un array e i suoi elementi vengono copiati:

```js
let arr = [1, 2];

let arrayLike = {
  0: "something",
  1: "else",

  [Symbol.isConcatSpreadable]: true,

  length: 2
};

alert( arr.concat(arrayLike) ); // 1,2,something,else
```

## Iterate: forEach

Il metodo [arr.forEach](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach) consente di eseguire una funzione su ogni elemento dell'array.

La sintassi:
```js
arr.forEach(function(item, index, array) {
  // ... fa qualcosa con l'elemento
});
```

Ad esempio, il codice sotto mostra ogni elemento dell'array:

```js
// per ogni elemento chiama alert
["Bilbo", "Gandalf", "Nazgul"].forEach(alert);
```

Invece questo codice ne mostra anche la posizione:

```js
["Bilbo", "Gandalf", "Nazgul"].forEach((item, index, array) => {
  alert(`${item} is at index ${index} in ${array}`);
});
```

Il risultato di questa funzione (sempre che ci sia) viene scartato.


## Ricerca in un array

Ora vedremo dei metodi per effettuare ricerche in un array.

### indexOf/lastIndexOf e include

I metodi [arr.indexOf](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/indexOf), [arr.lastIndexOf](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/lastIndexOf) e [arr.includes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/includes) hanno la stessa sintassi, e fanno praticamente la stessa cosa della loro controparte per stringhe, ma operano su elementi invece che su caratteri:

- `arr.indexOf(item, from)` cerca un `item` a partire dall'indirizzo `from`, e ritorna l'indirizzo in cui è stato trovato, altrimenti ritorna `-1`.
- `arr.lastIndexOf(item, from)` -- lo stesso, ma esegue la ricerca a partire da destra verso sinistra.
- `arr.includes(item, from)` -- cerca un `item` a partire dall'indice `from`, e ritorna `true` se lo trova.

Ad esempio:

```js
let arr = [1, 0, false];

alert( arr.indexOf(0) ); // 1
alert( arr.indexOf(false) ); // 2
alert( arr.indexOf(null) ); // -1

alert( arr.includes(1) ); // true
```

Da notare che questi metodi usano il confronto `===`. Quindi, se cerchiamo `false`, troveremo esattamente `false` e non zero.

Se vogliamo solo verificare la presenza di un elemento, senza voler conoscere l'indirizzo, è preferibile utilizzare il metodo `arr.includes`.

Inoltre, una piccola differenza è che `includes` gestisce correttamente `NaN`, a differenza di `indexOf/lastIndexOf`:

```js
const arr = [NaN];
alert( arr.indexOf(NaN) ); // -1 (dovrebbe essere 0, ma l'uguaglianza === non funziona con NaN)
alert( arr.includes(NaN) );// true (corretto)
```

### find e findIndex

Immaginiamo di avere un array di oggetti. Come possiamo trovare un oggetto che soddisfi specifiche condizioni?

In questi casi si utilizza il metodo [arr.find](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/find).

La sintassi è:
```js
let result = arr.find(function(item, index, array) {
  // se viene ritornato true, viene ritornato l'elemento e l'iterazione si ferma
  // altrimenti ritorna undefined
});
```

La funzione viene chiamata per ogni elemento dell'array:

- `item` è l'elemento.
- `index` è il suo indice.
- `array` è l'array stesso.

Se la chiamata ritorna `true`, la ricerca viene interrotta e viene ritornato `item`. Se non viene trovato nulla verrà ritornato `undefined`.

Ad esempio, abbiamo un array di utenti, ognuno con i campi `id` e `name`. Cerchiamo quello con `id == 1`:

```js
let users = [
  {id: 1, name: "John"},
  {id: 2, name: "Pete"},
  {id: 3, name: "Mary"}
];

let user = users.find(item => item.id == 1);

alert(user.name); // John
```

 Gli array di oggetti sono molto comuni, quindi il metodo `find` risulta molto utile.

Da notare che nell'esempio noi forniamo a `find` un singolo argomento `item => item.id == 1`. Gli altri parametri di `find` sono raramente utilizzati.

Il metodo [arr.findIndex](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/findIndex) fa essenzialmente la stessa cosa, ma ritorna l'indice in cui è stata trovata la corrispondenza piuttosto di ritornare l'oggetto stesso; se l'oggetto non viene trovato ritorna `-1`.

### filter

Il metodo `find` cerca un singola occorrenza dell'elemento, la prima, e se trovata ritorna `true`.

Se vogliamo cercare più occorrenze, possiamo utilizzare [arr.filter(fn)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter).

La sintassi è pressoché la stessa di `find`, ma ritorna un array contenente tutte le corrispondenze trovate:

```js
let results = arr.filter(function(item, index, array) {
  // se un item è true viene messo dentro results e l'iterazione continua
  // ritorna un array vuoto qualora nessun elemento ritornasse true
});
```

Ad esempio:

```js
let users = [
  {id: 1, name: "John"},
  {id: 2, name: "Pete"},
  {id: 3, name: "Mary"}
];

// ritorna un array con i primi due users
let someUsers = users.filter(item => item.id < 3);

alert(someUsers.length); // 2
```

## Trasformare un array

Questa sezione di occupa dei metodi che trasformano o riordinano gli array.

### map

Il metodo [arr.map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map) è uno dei più utili e maggiormente utilizzati.

La sintassi è:

```js
let result = arr.map(function(item, index, array) {
  // ritorna il nuovo valore piuttosto di item
})
```

La funzione viene chiamata per ogni elemento dell'array e ritorna un array con i risultati.

Ad esempio, qui trasformiamo ogni elemento nella propria `length`:

```js
let lengths = ["Bilbo", "Gandalf", "Nazgul"].map(item => item.length);
alert(lengths); // 5,7,6
```

### sort(fn)

Il metodo [arr.sort](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort) ordina l'array *sul posto*, ovvero cambia la posizione originale dei suoi elementi.

Ritorna altresì l'array riordinato, ma il risultato viene di solito ignorato, essendo l'`arr` originale modificato.

Ad esempio:

```js
let arr = [ 1, 2, 15 ];

// il metodo riordina il contenuto di arr (e lo ritorna)
arr.sort();

alert( arr );  // 1, 15, 2
```

Notate qualcosa di strano nel risultato?

L'ordine degli elementi è diventato `1, 15, 2`. Errato. Ma perché?

**Di default gli elementi vengono ordinati come stringhe.**

Letteralmente, tutti gli elementi vengono convertiti in stringhe e confrontati. Quindi, viene applicato l'algoritmo di ordinamento lessicografico, perciò `"2" > "15"`.

Per utilizzare un ordinamento arbitrario, dobbiamo fornire una funzione come argomento di `arr.sort()`.

La funzione dovrebbe essere simile a questa:
```js
function compare(a, b) {
  if (a > b) return 1; // se il primo valore è maggiore del secondo
  if (a == b) return 0; // se i valori sono uguali
  if (a < b) return -1; // se il primo valore è inferiore al secondo
}
```

Ad esempio, per ordinare dei numeri:

```js
function compareNumeric(a, b) {
  if (a > b) return 1;
  if (a == b) return 0;
  if (a < b) return -1;
}

let arr = [ 1, 2, 15 ];


arr.sort(compareNumeric);


alert(arr);  // 1, 2, 15
```

Ora funziona come dovrebbe.

Proviamo un attimo a capire cosa sta succedendo. L'array `arr` può contenere qualsiasi cosa, giusto? Può contenere numeri, stringhe, elementi HTML o qualsiasi altra cosa. Abbiamo quindi un insieme di *qualcosa*. Per poterlo ordinare abbiamo bisogno di una *funzione di ordinamento* che sappia ordinare gli elementi passati come argomenti. L'ordinamento di default è di tipo stringa.

Il metodo `arr.sort(fn)` implementa un algoritmo di ordinamento. Non dovremmo preoccuparci di come funzioni esattamente (la maggior parte delle volte è un [quicksort](https://en.wikipedia.org/wiki/Quicksort) ottimizzato). Questo algoritmo attraverserà l'intero array e confronterà i suoi valori; tutto quello che dobbiamo fare sarà fornirgli una funzione `fn` che esegua il confronto.

In ogni caso, se mai volessimo conoscere quali elementi vengono comparati -- nulla ci vieta di utilizzare `alert`:

```js
[1, -2, 15, 2, 0, 8].sort(function(a, b) {
  alert( a + " <> " + b );
  return a - b;
});
```

L'algoritmo potrebbe confrontare un elemento più volte durante il processo, sebbene tenti di fare il minor numero di confronti possibili.



:::: tip Una funzione di confronto può ritornare qualsiasi numero
In realtà, ad una funzione di confronto è solamente richiesto di ritornare un numero positivo per dire "maggiore" ed uno negativo per dire "minore".

Questo consente di scrivere funzioni più brevi:

```js
let arr = [ 1, 2, 15 ];

arr.sort(function(a, b) { return a - b; });

alert(arr);  // 1, 2, 15
```
::::


:::: tip Le arrow functions sono le migliori
Ricordate le [arrow functions](https://it.javascript.info/function-expressions-arrows#arrow-functions)? Possiamo utilizzarle per più conciso il codice di ordinamento:

```js
arr.sort( (a, b) => a - b );
```

Questa funziona esattamente come le altre versioni sopra, ma è più breve.
::::


:::: tip Use `localeCompare` for strings
Ricordate  l'algoritmo di comparazione delle [strings](/javascript/tutorial/string)? Di default, compara le lettere usando il loro codice.

Per molti alfabeti è meglio utilizzare `str.localeCompare` per ordinare correttamente lettere come `Ö`.

Per esempio, ordiniamo alcuni paesi in tedesco:

```js
let countries = ['Österreich', 'Andorra', 'Vietnam'];

alert( countries.sort( (a, b) => a > b ? 1 : -1) ); // Andorra, Vietnam, Österreich (wrong)

alert( countries.sort( (a, b) => a.localeCompare(b) ) ); // Andorra,Österreich,Vietnam (correct!)
```
::::

### reverse

Il metodo [arr.reverse](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reverse) inverte l'ordine degli elementi contenuti in `arr`.

Ad esempio:

```js
let arr = [1, 2, 3, 4, 5];
arr.reverse();

alert( arr ); // 5,4,3,2,1
```

Inoltre ritorna `arr` dopo averlo invertito.

### split e join

Vediamo una situazione reale. Stiamo scrivendo un'applicazione di messaggistica, e l'utente inserisce una lista di destinatari: `John, Pete, Mary`. Per noi sarebbe più comodo avere un array di nomi piuttosto di una singola stringa. Come possiamo ottenerlo?

Il metodo [str.split(delim)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split) fa esattamente questo. Divide la stringa in un array utilizzando il delimitatore `delim`.

Nell'esempio sotto, utilizziamo come delimitatore una virgola seguita da uno spazio:

```js
let names = 'Bilbo, Gandalf, Nazgul';

let arr = names.split(', ');

for (let name of arr) {
  alert( `A message to ${name}.` ); // A message to Bilbo (e altri name)
}
```

Il metodo `split` ha un secondo argomento opzionale di tipo numerico -- è un limite di lunghezza per l'array. Se questo argomento viene fornito, allora gli elementi extra verranno ignorati. Ma nella pratica è raramente utilizzato:

```js
let arr = 'Bilbo, Gandalf, Nazgul, Saruman'.split(', ', 2);

alert(arr); // Bilbo, Gandalf
```


:::: tip Split in lettere
La chiamata a `split(s)` con l'argomento vuoto, dividerà la stringa in un array di lettere:

```js
let str = "test";

alert( str.split('') ); // t,e,s,t
```
::::

La chiamata ad [arr.join(separatore)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/join) fa esattamente l'inverso di `split`. Crea una stringa con gli elementi di `arr` incollati tra loro dal `separatore`.

Ad esempio:

```js
let arr = ['Bilbo', 'Gandalf', 'Nazgul'];

let str = arr.join(';'); // incolla l'array utilizzando ;

alert( str ); // Bilbo;Gandalf;Nazgul
```

### reduce/reduceRight
Quando vogliamo iterare su un array -- possiamo utilizzare `forEach`, `for` o `for..of`.

Quando invece abbiamo la necessità di iterare e ritornare dati per ogni elemento -- possiamo usare `map`.

I metodi [arr.reduce](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce) e [arr.reduceRight](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduceRight) fanno parte della stessa categoria, ma sono leggermente più complessi. Vengono utilizzati per calcolare un singolo valore basato sul contenuto dell'array.

La sintassi è:

```js
let value = arr.reduce(function(accumulator, item, index, array) {
  // ...
}, [initial]);
```

La funzione viene applicata ad ogni elemento dell'array uno dopo l'altro, passando il risultato alla chiamata successiva.

Argomenti:

- `accumulator` -- è il risultato della precedente chiamata, uguale ad `initial` per la prima chiamata (se `initial` viene fornito).
- `item` -- è l'attuale elemento dell'array.
- `index` -- la sua posizione.
- `array` -- l'array.

Quando la funzione è stata applicata, il risultato viene passato alla chiamata successiva.

Sembra complicato, ma non lo è se pensate al primo argomento come un "accumulatore" che memorizza il risultato delle precedenti esecuzioni. E alla fine diventa il risultato di `reduce`.

Il modo più semplice per spiegarlo è tramite esempi.

Qui otterremo una somma degli elementi dell'array in una riga:

```js
let arr = [1, 2, 3, 4, 5];

let result = arr.reduce((sum, current) => sum + current, 0);

alert(result); // 15
```

Qui abbiamo utilizzato la variante più comune di `reduce` con solo 2 argomenti.

Proviamo a vedere nel dettaglio cosa succede.

1. Nella prima esecuzione, `sum` è il valore iniziale (l'ultimo argomento di `reduce`), cioè `0`, e `current` è il primo elemento dell'array, cioè `1`. Quindi il risultato è `1`.
2. Nella seconda esecuzione, `sum = 1`; gli sommiamo il secondo elemento dell'array(`2`) e ritorniamo il risultato.
3. Nella terza esecuzione, `sum = 3`; gli sommiamo l'elemento successivo, e cosi via...

Il flusso di calcolo:

![](/javascript-info/1-js/05-data-types/05-array-methods/reduce.svg)

O nella forma tabellare, in cui ogni riga rappresenta una chiamata di funzione:

|   |`sum`|`current`|result|
|---|-----|---------|---------|
|prima chiamata|`0`|`1`|`1`|
|seconda chiamata|`1`|`2`|`3`|
|terza chiamata|`3`|`3`|`6`|
|quarta chiamata|`6`|`4`|`10`|
|quinta chiamata|`10`|`5`|`15`|


Come abbiamo potuto osservare, il risultato della chiamata precedente diventa il primo argomento della chiamata successiva.

Possiamo anche omettere il valore iniziale:

```js
let arr = [1, 2, 3, 4, 5];

// rimosso il valore iniziale da reduce (no 0)
let result = arr.reduce((sum, current) => sum + current);

alert( result ); // 15
```

Il risultato sarebbe lo stesso. Questo perché se non c'è un valore iniziale, allora `reduce` prende il primo elemento dell'array come valore iniziale ed inizia l'iterazione dal secondo elemento.

La tabella dei calcoli è uguale a quella precedente, viene saltata solo la prima riga.

Questo tipo di utilizzo richiede particolare cura. Se l'array è vuoto, allora `reduce` effettua la chiamata senza valore iniziale e provoca un errore.

Vediamo un esempio:

```js
let arr = [];

// Errore: Riduzione di un array vuoto senza valore iniziale
// se il valore iniziale esistesse, reduce lo restituirebbe all'array vuoto.
arr.reduce((sum, current) => sum + current);
```


Quindi è fortemente consigliato di specificare sempre un valore iniziale.

Il metodo [arr.reduceRight](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduceRight) fa esattamente la stessa cosa, ma da destra verso sinistra.


## Array.isArray

Gli array non sono un tipo di dato a sé del linguaggio. Sono basati sulla sintassi degli oggetti.

Quindi `typeof` non aiuta a distinguere un oggetto da un array:

```js
alert(typeof {}); // object
alert(typeof []); // lo stesso
```

...Ma gli array vengono utilizzati cosi spesso che esiste un metodo dedicato per questo: [Array.isArray(value)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/isArray). Ritorna `true` se `value` è un array, `false` altrimenti.

```js
alert(Array.isArray({})); // false

alert(Array.isArray([])); // true
```

## la maggior parte dei metodi accetta "thisArg"

Quasi tutti i metodi degli array che richiedono una funzione -- come `find`, `filter`, `map`, fatta eccezione per `sort`, accettano un parametro opzionale `thisArg`.

Questo parametro non è stato spiegato nella sezione sopra, perché viene raramente utilizzato. Studiamolo per completezza.

Vediamo la sintassi di questi metodi:

```js
arr.find(func, thisArg);
arr.filter(func, thisArg);
arr.map(func, thisArg);
// ...
// thisArg è l'ultimo argomento opzionale
```

Il valore del parametro `thisArg` diventa `this` per `func`.

Ad esempio, qui utilizziamo il metodo di un oggetto come filtro e `thisArg` ci risulta utile:

```js
let army = {
  minAge: 18,
  maxAge: 27,
  canJoin(user) {
    return user.age >= this.minAge && user.age < this.maxAge;
  }
};

let users = [
  {age: 16},
  {age: 20},
  {age: 23},
  {age: 30}
];


// trova tutti gli users più giovani di user
let soldiers = users.filter(army.canJoin, army);


alert(soldiers.length); // 2
alert(soldiers[0].age); // 20
alert(soldiers[1].age); // 23
```

Nella chiamata sopra, utilizziamo `army.canJoin` come filtro e forniamo `army` come contesto. Se non avessimo fornito il contesto, `users.filter(army.canJoin)` avrebbe chiamato `army.canJoin` come funzione a sé stante, con `this=undefined`. Che avrebbe provocato un errore.


Una chiamata a `user.filter(army.canJoin, army)` può essere sostituita da 
`users.filter(user => army.canJoin(user))`, che fa lo stesso. L'ultima versione viene utilizzata più spesso e per molte persone è più semplice da capire.

## Riepilogo

Un breve riepilogo dei metodi per array:

- Per aggiungere/rimuovere elementi:
  - `push(...items)` -- aggiunge elementi in coda,
  - `pop()` -- estrae un elemento dalla coda,
  - `shift()` -- estrae un elemento dalla testa,
  - `unshift(...items)` -- aggiunge un elemento alla testa.
  - `splice(pos, deleteCount, ...items)` -- all'indice `pos` cancella `deleteCount` elementi e al loro posto inserisce `items`.
  - `slice(start, end)` -- crea un nuovo array e copia al suo interno gli elementi da `start` fino ad `end` (escluso).
  - `concat(...items)` -- ritorna un nuovo array: copia tutti gli elementi di quello corrente e ci aggiunge `items`. Se uno degli `items` è un array, allora vengono presi anche i suoi elementi.

- Ricercare elementi:
  - `indexOf/lastIndexOf(item, pos)` -- cerca `item` a partire da `pos`, e ritorna l'indice, oppure `-1` se non lo trova.
  - `includes(value)` -- ritorna `true` se l'array contiene `value`, altrimenti `false`.
  - `find/filter(func)` -- filtra gli elementi tramite una funzione, ritorna il primo/tutti i valori che ritornano `true`.
  - `findIndex` è simile a `find`, ma ritorna l'indice piuttosto del valore.

- Per iterare sugli elementi:
  - `forEach(func)` -- invoca `func` su ogni elemento; non ritorna nulla.

- Per modificare un array:
  - `map(func)` -- crea un nuovo array con i risultati della chiamata `func` su tutti i suoi elementi.
  - `sort(func)` -- ordina l'array "sul posto", e lo ritorna.
  - `reverse()` -- inverte l'array sul posto, e lo ritorna.
  - `split/join` -- converte una stringa in array e vice versa.
  - `reduce/reduceRight(func, initial)` -- calcola un singolo valore chiamando `func` per ogni elemento e passando un risultato temporaneo tra una chiamata e l'altra

- Un altro metodo utile:
  - `Array.isArray(arr)` controlla che `arr` sia un array.

Da notare che i metodi `sort`, `reverse` e `splice` modificano l'array stesso.

I metodi elencati sono quelli utilizzati più spesso e sono in grado di coprire il 99% dei casi d'uso. Ce ne sono altri che possono tornare utili:

- [arr.some(fn)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some)/[arr.every(fn)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/every) controlla l'array.

  La funzione `fn` viene invocata su ogni elemento dell'array in maniera simile a `map`. Se qualcuno/tutti i risultati sono `true`, ritorna `true`, altrimenti `false`.
  
  Questi metodi si comportano quasi come gli operatori `||` e `&&`: se `fn` ritorna un valore vero, `arr.some()` ritorna immediatamente  `true` e conclude l'iterazione; se `fn` ritorna un valore falso, `arr.every()` ritorna immediatamente `false` e smette di iterare.

  Possiamo utilizzare `every` per confrontare gli array:
  ```js
  function arraysEqual(arr1, arr2) {
    return arr1.length === arr2.length && arr1.every((value, index) => value === arr2[index]);
  }

  alert( arraysEqual([1, 2], [1, 2])); // true
  ```

- [arr.fill(value, start, end)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/fill) -- riempie l'array con `value` da `start` fino a `end`.

- [arr.copyWithin(target, start, end)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/copyWithin) -- copia gli elementi da `start` fino a `end` dentro *se stesso*,  nella posizione `target` (sovrascrivendo gli elementi contenuti).

- [arr.flat(depth)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/flat)/[arr.flatMap(fn)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/flatMap) crea un nuovo array monodimensionale partendo da un array multidimensionale.

Per la lista completa, vedere il [manuale](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array).

A prima vista potrebbero sembrare molti metodi da ricordare. Ma in realtà è molto più semplice di quanto sembri.

Tenente sempre un occhio al riassunto fornito sopra. Provate anche a risolvere gli esercizi di questo capitolo.

In futuro quando avrete bisogno di fare qualcosa con un array, e non saprete come fare -- tornate qui, guardate il riassunto e trovate il metodo corretto. Gli esempi vi aiuteranno molto. In poco tempo vi risulterà naturale ricordare questi metodi, senza troppi sforzi.

## Esercizi

### 1 · Traducete border-left-width in borderLeftWidth

Scrivete una funzione `camelize(str)` che trasforma le parole separate da un trattino come "la-mia-stringa" nella notazione a cammello "laMiaStringa".

Quindi: rimuove tutti i trattini; ogni parola dopo un trattino avrà una lettera maiuscola.

Esempi:

```js
camelize("background-color") == 'backgroundColor';
camelize("list-style-image") == 'listStyleImage';
camelize("-webkit-transition") == 'WebkitTransition';
```

P.S. Suggerimento: usate `split` per dividere una stringa in un array, trasformatela e infinite riunite tutto con `join`.

::::: details Soluzione



:::::

### 2 · Filtri

Scrivete una funzione `filterRange(arr, a, b)` che accetta come argomento un array `arr`, filtra gli elementi tra `a` e `b` e ne ritorna un array. 

La funzione non dovrebbe modificare l'array. Dovrebbe invece ritornare il nuovo array.

Ad esempio:

```js
let arr = [5, 3, 8, 1];

let filtered = filterRange(arr, 1, 4); 

alert( filtered ); // 3,1 (i valori filtrati)

alert( arr ); // 5,3,8,1 (non modificato)
```

::::: details Soluzione

```js
function filterRange(arr, a, b) {
  //aggiunte parentesi attorno all'espressione per una migliore leggibilità
  return arr.filter(item => (a <= item && item <= b));
}

let arr = [5, 3, 8, 1];

let filtered = filterRange(arr, 1, 4);

alert( filtered ); // 3,1 (i valori filtrati)

alert( arr ); // 5,3,8,1 (non modificato)
```

:::::

### 3 · Filtrare un range "sul post"

Scrivi una funzione `filterRangeInPlace(arr, a, b)` che prenda un array `arr` e ne rimuova tutti i valori, tranne quelli contenuti tra `a` e `b`. Il test è: `a ≤ arr[i] ≤ b`.

La funzione dovrebbe solamente modificare l'array. Senza ritornare nulla.

Ad esempio:
```js
let arr = [5, 3, 8, 1];

filterRangeInPlace(arr, 1, 4); // rimuove tutti i numeri tranne quelli da 1 a 4

alert( arr ); // [3, 1]
```

::::: details Soluzione

```js
function filterRangeInPlace(arr, a, b) {

  for (let i = 0; i < arr.length; i++) {
    let val = arr[i];

    // rimuove se fuori dal range
    if (val < a || val > b) {
      arr.splice(i, 1);
      i--;
    }
  }

}

let arr = [5, 3, 8, 1];

filterRangeInPlace(arr, 1, 4); // rimossi tutti i numeri tranne quelli da 1 a 4

alert( arr ); // [3, 1]
```

:::::

### 4 · Riordinare in ordine decrescente

```js
let arr = [5, 2, 1, -10, 8];

// ... il tuo codice per ordinare in ordine decrescente

alert( arr ); // 8, 5, 2, 1, -10
```

::::: details Soluzione

```js
let arr = [5, 2, 1, -10, 8];

arr.sort((a, b) => b - a);

alert( arr );
```

:::::

### 5 · Copiare e ordinare un array

Abbiamo un array di stringhe `arr`. Vorremmo ottenerne una sua copia ordinata, mantenenendo `arr` inalterato.

Create una funzione `copySorted(arr)` che ritorni questo tipo di copia.

```js
let arr = ["HTML", "JavaScript", "CSS"];

let sorted = copySorted(arr);

alert( sorted ); // CSS, HTML, JavaScript
alert( arr ); // HTML, JavaScript, CSS (nessuna modifica)
```

::::: details Soluzione

Possiamo utilizzare `slice()` per fare una copia e solo dopo riordinarla:

```js
function copySorted(arr) {
  return arr.slice().sort();
}

let arr = ["HTML", "JavaScript", "CSS"];


let sorted = copySorted(arr);


alert( sorted );
alert( arr );
```

:::::

### 6 · Map di nomi

Avete un array di oggetti `user`; ognuno di essi ha la proprietà `user.name`. Scrivete il codice che converte gli oggetti in un array di nomi.

Ad esempio:

```js
let john = { name: "John", age: 25 };
let pete = { name: "Pete", age: 30 };
let mary = { name: "Mary", age: 28 };

let users = [ john, pete, mary ];

let names = /* ... il vostro codice */

alert( names ); // John, Pete, Mary
```

::::: details Soluzione

```js

let john = { name: "John", age: 25 };
let pete = { name: "Pete", age: 30 };
let mary = { name: "Mary", age: 28 };

let users = [ john, pete, mary ];

let names = users.map(item => item.name);

alert( names ); // John, Pete, Mary
```

:::::

### 7 · Create una calcolatrice estensibile

Create un costruttore `Calculator` che crei oggetti calcoltrice "estensibili".

Il compito consiste in due parti.

1. La prima parte consiste nell'implementare il metodo `calculate(str)` che accetti una stringa come `"1 + 2"` nel formato "NUMERO operatore NUMERO" (delimitata da spazi) e ne ritorni il risultato. Dovrebbe saper interpretare sia `+` che `-`.

    Esempio d'uso:

    ```js
    let calc = new Calculator;

    alert( calc.calculate("3 + 7") ); // 10
    ```
2. Successivamente aggiungete il metodo `addMethod(name, func)` che ha lo scopo di insegnare alla calcolatrice una nuova operazione. Questo prende il nome dell'operatore `name` e i due argomenti della funzione `func(a,b)` che lo implementa.

    Ad esempio, proviamo ad aggiungere la moltiplicazione `*`, divisione `/` e la potenza `**`:

    ```js
    let powerCalc = new Calculator;
    powerCalc.addMethod("*", (a, b) => a * b);
    powerCalc.addMethod("/", (a, b) => a / b);
    powerCalc.addMethod("**", (a, b) => a ** b);

    let result = powerCalc.calculate("2 ** 3");
    alert( result ); // 8
    ```

- Non è richiesta la gestione delle parentesi o di operazioni complesse.
- I numeri e l'operatore sono separati esattamente da un singolo spazio.
- Se ne hai voglia potresti provare ad aggiungere un minimo di gestione degli errori.

::::: details Soluzione

- Da notare come vengono memorizzati i metodi. Vengono semplicemente aggiunti all'interno dell'oggetto.
- Tutti i test e le conversioni numeriche vegono effettuati nel metodo `calculate`. In futuro potrebbe essere esteso per supportare espressioni molto più complesse.

:::::

### 8 · Map di oggetti

Avete un array di oggetti `user`, ognuno di questi possiede `name`, `surname` e `id`.

Scrivete il codice per creare un altro array che derivi da questo, sempre composto da oggetti con `id` e `fullName`, dove `fullName` viene generato da `name` e `surname`.

Un esempio:

```js
let john = { name: "John", surname: "Smith", id: 1 };
let pete = { name: "Pete", surname: "Hunt", id: 2 };
let mary = { name: "Mary", surname: "Key", id: 3 };

let users = [ john, pete, mary ];


let usersMapped = /* ... il vostro codice ... */


/*
usersMapped = [
  { fullName: "John Smith", id: 1 },
  { fullName: "Pete Hunt", id: 2 },
  { fullName: "Mary Key", id: 3 }
]
*/

alert( usersMapped[0].id ) // 1
alert( usersMapped[0].fullName ) // John Smith
```

Quindi, in realtà avrete bisogno di mappare un array di oggetti in un altro. Provate ad utilizzare `=>`.

::::: details Soluzione

```js
let john = { name: "John", surname: "Smith", id: 1 };
let pete = { name: "Pete", surname: "Hunt", id: 2 };
let mary = { name: "Mary", surname: "Key", id: 3 };

let users = [ john, pete, mary ];


let usersMapped = users.map(user => ({
  fullName: `${user.name} ${user.surname}`,
  id: user.id
}));


/*
usersMapped = [
  { fullName: "John Smith", id: 1 },
  { fullName: "Pete Hunt", id: 2 },
  { fullName: "Mary Key", id: 3 }
]
*/

alert( usersMapped[0].id ); // 1
alert( usersMapped[0].fullName ); // John Smith
```
Da notare che nell'arrow function abbiamo bisogno di utilizzare un'ulteriore parentesi. 

Non possiamo scrivere semplicemente:
```js
let usersMapped = users.map(user => {
  fullName: `${user.name} ${user.surname}`,
  id: user.id
});
```

Se ricordate, ci sono due tipi di arrow function: senza corpo `value => expr` e con il corpo `value => {...}`.

Qui JavaScript tratterà `{` come l'inzio del corpo della funzione, non l'inizio dell'oggetto. Questo trucco viene utilizzato per racchiuderle nelle normali parentesi:

```js
let usersMapped = users.map(user => ({
  fullName: `${user.name} ${user.surname}`,
  id: user.id
}));
```

Ora funziona.

:::::

### 9 · Riordinare oggetti per età

Scrivete una funzione `sortByAge(users)` che accetti un array di oggetti con proprietà `age` e lo riordini per `age`.

Ad esempio:

```js
let john = { name: "John", age: 25 };
let pete = { name: "Pete", age: 30 };
let mary = { name: "Mary", age: 28 };

let arr = [ pete, john, mary ];

sortByAge(arr);

// ora: [john, mary, pete]
alert(arr[0].name); // John
alert(arr[1].name); // Mary
alert(arr[2].name); // Pete
```

::::: details Soluzione

```js
function sortByAge(arr) {
  arr.sort((a, b) => a.age - b.age);
}

let john = { name: "John", age: 25 };
let pete = { name: "Pete", age: 30 };
let mary = { name: "Mary", age: 28 };

let arr = [ pete, john, mary ];

sortByAge(arr);

// ordinato: [john, mary, pete]
alert(arr[0].name); // John
alert(arr[1].name); // Mary
alert(arr[2].name); // Pete
```

:::::

### 10 · Rimescolare un array

Scrivete una funzione `shuffle(array)` che rimescoli (riordini casualmente) gli elementi di un array.

Esecuzioni multiple di `shuffle` dovrebbero portare a diversi ordinamenti degli elementi. Ad esempio:

```js
let arr = [1, 2, 3];

shuffle(arr);
// arr = [3, 2, 1]

shuffle(arr);
// arr = [2, 1, 3]

shuffle(arr);
// arr = [3, 1, 2]
// ...
```

Tutti gli elementi ordinati dovrebbero avere una probabilità identica. Ad esempio, `[1,2,3]` può essere riordinato come `[1,2,3]` o `[1,3,2]` o `[3,1,2]` etc; ognuno dei casi deve avere la stessa probabilità.

::::: details Soluzione

La soluzione più semplice potrebbe essere:

```js

function shuffle(array) {
  array.sort(() => Math.random() - 0.5);
}


let arr = [1, 2, 3];
shuffle(arr);
alert(arr);
```

Questa in qualche modo funziona, perché `Math.random() - 0.5` è un numero casuale che può essere sia positivo che negativo, quindi la funzione riordina gli elementi casualmente.

Con questa funzione di ordinamento, non tutte le permutazioni hanno la stessa probabilità.

Ad esempio, considerando il codice sotto. Esegue `shuffle` 1000000 di volte e conta il numero di occorrenze di tutti i risultati possibili:

```js
function shuffle(array) {
  array.sort(() => Math.random() - 0.5);
}

// counts of appearances for all possible permutations
let count = {
  '123': 0,
  '132': 0,
  '213': 0,
  '231': 0,
  '321': 0,
  '312': 0
};

for (let i = 0; i < 1000000; i++) {
  let array = [1, 2, 3];
  shuffle(array);
  count[array.join('')]++;
}

// show counts of all possible permutations
for (let key in count) {
  alert(`${key}: ${count[key]}`);
}
```

Un esempio di risultato possibile (dipende dal motore JS):

```js
123: 250706
132: 124425
213: 249618
231: 124880
312: 125148
321: 125223
```
Possiamo chiaramente vedere che le combinazioni `123` e `213` appaiono molto più spesso delle altre.

Il risultato del codice potrebbe variare in base al motore JavaScript, ma già possiamo notare che questo tipo di approccio è inaccettabile.

Perché non funziona? Generalmente parlando, `sort` è una "scatola nera": gli passiamo un array ed una funzione di confronto e ci aspettiamo di ottenere l'array ordinato. Ma a causa della difficoltà nell'implementazione della casualità la scatola nera potrebbe funzionare male; quanto male, dipende dal motore JavaScript.

Esistono altri modi per questo compito. Ad esempio, c'è un ottimo algoritmo chiamato [Fisher-Yates shuffle](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle). L'idea è di attraversare l'array in ordine inverso e di scambiare l'elemento con un altro casuale, che venga prima di lui:

```js
function shuffle(array) {
  for (let i = array.length - 1; i > 0; i--) {
    let j = Math.floor(Math.random() * (i + 1)); // indice casuale da 0 a i

    //scambia gli elementi array[i] e array[j]
    // usiamo la sintassi "destructuring assignment" 
    //troverai maggiori dettagli su questa sintassi nei capitoli seguenti
    //potrebbe essere scritto come
    // let t = array[i]; array[i] = array[j]; array[j] = t
    [array[i], array[j]] = [array[j], array[i]];
  }
}
```

Proviamo ad eseguire lo stesso test:

```js
function shuffle(array) {
  for (let i = array.length - 1; i > 0; i--) {
    let j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
}

// counts of appearances for all possible permutations
let count = {
  '123': 0,
  '132': 0,
  '213': 0,
  '231': 0,
  '321': 0,
  '312': 0
};

for (let i = 0; i < 1000000; i++) {
  let array = [1, 2, 3];
  shuffle(array);
  count[array.join('')]++;
}

// show counts of all possible permutations
for (let key in count) {
  alert(`${key}: ${count[key]}`);
}
```

Un possibile risultato:

```js
123: 166693
132: 166647
213: 166628
231: 167517
312: 166199
321: 166316
```

Ora sembra funzionare: tutte lo occorrenze appaiono con la stessa probabilità.

Inoltre, anche le performance dell'algoritmo Fisher-Yates sono migliori, poichè non è richiesto alcun riordinamento.

:::::

### 11 · Ottenere l'età media+

Scrivete una funzione `getAverageAge(users)` che accetti un array di oggetti con la proprietà `age` e ritorni l'età media.

La formula della media è: `(age1 + age2 + ... + ageN) / N`.

Ad esempio:

```js
let john = { name: "John", age: 25 };
let pete = { name: "Pete", age: 30 };
let mary = { name: "Mary", age: 29 };

let arr = [ john, pete, mary ];

alert( getAverageAge(arr) ); // (25 + 30 + 29) / 3 = 28
```

::::: details Soluzione

```js
function getAverageAge(users) {
  return users.reduce((prev, user) => prev + user.age, 0) / users.length;
}

let john = { name: "John", age: 25 };
let pete = { name: "Pete", age: 30 };
let mary = { name: "Mary", age: 29 };

let arr = [ john, pete, mary ];

alert( getAverageAge(arr) ); // 28
```

:::::

### 12 · Filtrare un array per ottenere elementi unici

Abbiamo un array `arr`.

Create una funzione `unique(arr)` che ritorni un array con elementi unici.

Ad esempio:

```js
function unique(arr) {
  /* your code */
}

let strings = ["Hare", "Krishna", "Hare", "Krishna",
  "Krishna", "Krishna", "Hare", "Hare", ":-O"
];

alert( unique(strings) ); // Hare, Krishna, :-O
```

::::: details Soluzione

Attraversiamo gli elementi dell'array:
- Per ogni elemento controlliamo se l'array risultante già lo contiene.
- Se lo troviamo, passiamo al prossimo, altrimenti lo aggiungiamo.

```js
function unique(arr) {
  let result = [];

  for (let str of arr) {
    if (!result.includes(str)) {
      result.push(str);
    }
  }

  return result;
}

let strings = ["Hare", "Krishna", "Hare", "Krishna",
  "Krishna", "Krishna", "Hare", "Hare", ":-O"
];

alert( unique(strings) ); // Hare, Krishna, :-O
```

Il codice funziona, ma c'è un potenziale problema di performace.

Il metodo `result.includes(str)` internamente attraversa l'array `result` e confronta ogni elemento con `str` per trovare una corrispondenza.

Quindi se ci sono `100` elementi in `result` e nessuna corrispondenza con `str`, attraverseremo l'intero array `result` eseguendo essattamente `100` confronti. Se l'array `result` è grande, ad esempio `10000`, ci sarebbero `10000` di confronti.

Non è propriamente un problema, perché il motore JavaScript è molto rapido, quindi un array grande `10000` è questione di pochi microsecondi.

Ma dovremo eseguire questo test per ogni elemento di `arr` nel ciclo `for`.

Quindi se `arr.length` è `10000` avremmo qualcosa come `10000*10000` = 100 milioni di confronti. Sono molti.

Quindi la soluzione funziona bene solo con array di piccola taglia.

Più avanti nel capitolo [Map e Set](/javascript/tutorial/map-set) vedremo come ottimizare questo metodo.

:::::

### 13 · Create un oggetto da un array

Immaginiamo di ricevere un array di utenti nella forma `{id:..., name:..., age... }`.

Scrivi una funzione `groupById(arr)` che ricavi un oggetto da esso, con `id` come chiave e gli elementi dell'array come valori

Ad esempio:

```js
let users = [
  {id: 'john', name: "John Smith", age: 20},
  {id: 'ann', name: "Ann Smith", age: 24},
  {id: 'pete', name: "Pete Peterson", age: 31},
];

let usersById = groupById(users);

/*
// dopo la chiamata dovremmo avere:

usersById = {
  john: {id: 'john', name: "John Smith", age: 20},
  ann: {id: 'ann', name: "Ann Smith", age: 24},
  pete: {id: 'pete', name: "Pete Peterson", age: 31},
}
*/
```

Una funzione simile è molto utile quando si lavora con dati provenienti da un server.

In questo esercizio sappiamo che `id` è unico. Non ci saranno due array con lo stesso `id`.

Per favore utilizza il metodo `.reduce` nella soluzione.

::::: details Soluzione



:::::

