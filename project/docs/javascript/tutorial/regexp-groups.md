---
title: "I gruppi di acquisizione (capturing group)"
description: "JavaScript.info in italiano: I gruppi di acquisizione (capturing group)"
sourceTutorial: true
prev: {"text": "Modalità greedy e lazy dei quantificatori", "link": "/javascript/tutorial/regexp-greedy-and-lazy"}
next: {"text": "Riferimenti all'indietro (backreference) nei pattern: \\N e \\kname", "link": "/javascript/tutorial/regexp-backreferences"}
---

# I gruppi di acquisizione (capturing group)

> **JavaScript.info · Ilya Kantor e contributori.** [Originale inglese](https://javascript.info/regexp-groups) · [Edizione italiana](https://it.javascript.info/regexp-groups) · [Fonti e licenza](/javascript/fonti).

Una parte del pattern può essere racchiusa tra parentesi `(...)`, diventando così un "gruppo di acquisizione" (capturing group).

Ciò comporta due conseguenze:

1. Possiamo acquisire una parte della corrispondenza come elemento separato all'interno di un array di risultati.
2. Se poniamo un quantificatore dopo le parentesi, questo si applica all'intero gruppo di acquisizione.

## Esempi

Vediamo come operano le parentesi attraverso degli esempi.

### Esempio: gogogo

Senza parentesi, il pattern `go+` significa: il carattere `g` seguito da `o` ripetuto una o più volte. Per esempio `goooo` o `gooooooooo`.

Le parentesi raggruppano i caratteri, pertanto `(go)+` significa `go`, `gogo`, `gogogo` e così via.

```js
alert( 'Gogogo now!'.match(/(go)+/ig) ); // "Gogogo"
```

### Esempio: dominio

Facciamo un esempio un po' più complesso, un'espressione regolare per cercare il dominio di un sito.

Per esempio:

```
mail.com
users.mail.com
smith.users.mail.com
```

Come possiamo vedere, un dominio consiste in parole ripetute, un punto segue ciascuna parola tranne l'ultima.

Tradotto in un'espressione regolare diventa `(\w+\.)+\w+`:

```js
let regexp = /(\w+\.)+\w+/g;

alert( "site.com my.site.com".match(regexp) ); // site.com,my.site.com
```

La ricerca funziona, ma il pattern non trova riscontro con domini contenenti un trattino, es. `my-site.com`, perché il trattino non appartiene alla classe `\w`.

Possiamo correggere il tiro rimpiazzando `\w` con `[\w-]` in ogni parola eccetto l'ultima: `([\w-]+\.)+\w+`.

### Esempio: email

Il precedente esempio può essere esteso. A partire da questo possiamo creare un'espressione regolare per le email.

Il formato delle email è: `name@domain`. Qualsiasi parola può essere "name", sono consentiti trattini e punti. L'espressione regolare diventa `[-.\w]+`.

Ecco il pattern:

```js
let regexp = /[-.\w]+@([\w-]+\.)+[\w-]+/g;

alert("my@mail.com @ his@site.com.uk".match(regexp)); // my@mail.com, his@site.com.uk
```

Questa regexp non è perfetta, ma per lo più funziona e aiuta a correggere errori di battitura accidentali. L'unica verifica davvero efficace per un'email può essere fatta soltanto inviandone una.

## I contenuti tra parentesi nella corrispondenza

I gruppi tra parentesi sono numerati da sinistra verso destra. Il motore di ricerca memorizza il contenuto associato a ciascuno di essi e consente di recuperarlo nel risultato.

Il metodo `str.match(regexp)`, se `regexp` non ha il flag `g`, cerca la prima corrispondenza e la restituisce in un array:

1. Nell'indice `0`: l'intera corrispondenza.
2. Nell'indice `1`: il contenuto del primo gruppo tra parentesi.
3. Nell'indice `2`: il contenuto del secondo.
4. ...e così via...

Ad esempio se volessimo trovare i tag HTML `<.*?>` per elaborarli, sarebbe conveniente averne il contenuto (ciò che è all'interno delle parentesi uncinate) in una variabile separata.

Racchiudiamo il contenuto tra parentesi, in questo modo: `<(.*?)>`.

Adesso otterremo sia l'intero tag `<h1>` sia il suo contenuto `h1` nell'array di risultati:

```js
let str = '<h1>Hello, world!</h1>';

let tag = str.match(/<(.*?)>/);

alert( tag[0] ); // <h1>
alert( tag[1] ); // h1
```

### Gruppi annidati

Le parentesi possono essere annidate. Anche in questo caso la numerazione procede da sinistra verso destra.

Per esempio durante la ricerca del tag in `<span class="my">` potrebbe interessarci:

1. L'intero contenuto del tag: `span class="my"`.
2. Il nome del tag: `span`.
3. Gli attributi del tag: `class="my"`.

Aggiungiamo le parentesi a questo scopo: `<(([a-z]+)\s*([^>]*))>`.

Ecco come sono numerate (da sinistra verso destra, a partire dalla parentesi di apertura):

![](/javascript-info/9-regular-expressions/11-regexp-groups/regexp-nested-groups-pattern.svg)

In azione:

```js
let str = '<span class="my">';

let regexp = /<(([a-z]+)\s*([^>]*))>/;

let result = str.match(regexp);
alert(result[0]); // <span class="my">
alert(result[1]); // span class="my"
alert(result[2]); // span
alert(result[3]); // class="my"
```

L'indice zero di `result` contiene sempre l'intera corrispondenza.

Seguono i gruppi, numerati da sinistra verso destra, a partire dalla parentesi di apertura. Il primo gruppo è `result[1]`, esso racchiude l'intero contenuto del tag.

Troviamo il gruppo della seconda parentesi `([a-z]+)` in `result[2]` ed a seguire il nome del tag `([^>]*)` in `result[3]`.

Ed ecco la rappresentazione del contenuto di ciascun gruppo nella stringa:

![](/javascript-info/9-regular-expressions/11-regexp-groups/regexp-nested-groups-matches.svg)

### Gruppi opzionali

Anche se un gruppo è opzionale e non ha alcun riscontro (ad esempio ha il quantificatore `(...)?`), l'elemento corrispondente è comunque presente nell'array `result` ed equivale a `undefined`.

Consideriamo per esempio la regexp `a(z)?(c)?` che cerca la `"a"` facoltativamente seguita da `"z"` e da `"c"`.

Se la eseguiamo sulla stringa con la singola lettera `a`, questo è il risultato:

```js
let match = 'a'.match(/a(z)?(c)?/);

alert( match.length ); // 3
alert( match[0] ); // a (l'intera corrispondenza)
alert( match[1] ); // undefined
alert( match[2] ); // undefined
```

L'array è costituito da `3` elementi, ma tutti i gruppi sono vuoti.

Ed ora ecco un riscontro più articolato per la stringa `ac`:

```js
let match = 'ac'.match(/a(z)?(c)?/)

alert( match.length ); // 3
alert( match[0] ); // ac (l'intera corrispondenza)
alert( match[1] ); // undefined, perché non c'è riscontro per (z)?
alert( match[2] ); // c
```

La lunghezza dell'array resta in ogni caso: `3`, ma non c'è riscontro per il gruppo `(z)?`, quindi il risultato è `["ac", undefined, "c"]`.

## Ricerca di tutte le corrispondenze con gruppi: matchAll


::: warning `matchAll` è un nuovo metodo, potrebbe essere necessario un polyfill
Il metodo `matchAll` non è supportato nei browser più datati.

Potrebbe essere richiesto un polyfill come <https://github.com/ljharb/String.prototype.matchAll>.
:::

Quando cerchiamo tutte le corrispondenze (flag `g`), il metodo `match` non restituisce il contenuto dei gruppi.

Cerchiamo ad esempio tutti i tag in una stringa:

```js
let str = '<h1> <h2>';

let tags = str.match(/<(.*?)>/g);

alert( tags ); // <h1>,<h2>
```

Il risultato è un array di riscontri, ma senza i dettagli di ciascuno di essi. Nella pratica comune, tuttavia, nel risultato ci occorre il contenuto dei gruppi di acquisizione.

Per ottenerlo, dovremmo utilizzare la ricerca con il metodo `str.matchAll(regexp)`.

È stato aggiunto al linguaggio JavaScript molto tempo dopo `match`, come sua "versione nuova e migliorata".

Proprio come `match` cerca le corrispondenze, ma ci sono 3 differenze:

1. Non restituisce un array, ma un oggetto iterabile.
2. Quando è presente il flag `g`, restituisce ogni riscontro come un array i cui elementi corrispondono ai gruppi.
3. Se non c'è alcun riscontro, non restituisce `null`, bensì un oggetto iterabile vuoto.

Per esempio:

```js
let results = '<h1> <h2>'.matchAll(/<(.*?)>/gi);

// results, non è un array ma un oggetto iterabile
alert(results); // [object RegExp String Iterator]

alert(results[0]); // undefined (*)

results = Array.from(results); // convertiamolo in un array

alert(results[0]); // <h1>,h1 (primo tag)
alert(results[1]); // <h2>,h2 (secondo tag)
```

Come possiamo notare la prima differenza è davvero rilevante, lo dimostra la linea `(*)`. Non possiamo ricavare la corrispondenza come `results[0]` perché quell'oggetto non è uno pseudo array. Possiamo convertirlo in un `Array` a tutti gli effetti tramite `Array.from`. Trovate ulteriori dettagli sugli pseudo array e sugli iterabili nell'articolo [Iteratori](/javascript/tutorial/iterable).

Non occorre la conversione con `Array.from` se adoperiamo un ciclo iterativo sui risultati:

```js
let results = '<h1> <h2>'.matchAll(/<(.*?)>/gi);

for(let result of results) {
  alert(result);
  // primo alert: <h1>,h1
  // secondo: <h2>,h2
}
```

...Oppure se ci avvaliamo della sintassi destrutturata:

```js
let [tag1, tag2] = '<h1> <h2>'.matchAll(/<(.*?)>/gi);
```

Ogni elemento dell'oggetto di risultati restituito da `matchAll` ha lo stesso formato del risultato di `match` senza il flag `g`: si tratta di un array con le proprietà aggiuntive `index` (la posizione del riscontro nella stringa) e `input` (la stringa sorgente):

```js
let results = '<h1> <h2>'.matchAll(/<(.*?)>/gi);

let [tag1, tag2] = results;

alert( tag1[0] ); // <h1>
alert( tag1[1] ); // h1
alert( tag1.index ); // 0
alert( tag1.input ); // <h1> <h2>
```


::: tip Perché il risultato di `matchAll` è un oggetto iterabile e non un array?
Perché questo metodo è progettato in questo modo? La ragione è semplice, per l'ottimizzazione.

La chiamata a `matchAll` non esegue la ricerca. Al contrario, restituisce un oggetto iterabile inizialmente privo di risultati. La ricerca è eseguita ogni volta che richiediamo un elemento, ad esempio all'interno di un ciclo iterativo.

Verranno pertanto trovati tutti i risultati necessari, non di più.

Considerate che potrebbero esserci anche 100 riscontri nel testo, ma potremmo decidere che sono sufficienti le prime cinque iterazioni di un ciclo `for..of` e interrompere con `break`. L'interprete a quel punto non sprecherà tempo a recuperare gli altri 95 risultati.
:::

## I gruppi nominati

Ricordare i gruppi con i rispettivi numeri è difficoltoso. È fattibile per i pattern semplici, ma per quelli più complessi contare le parentesi è scomodo. Abbiamo a disposizione un'opzione decisamente migliore: dare un nome alle parentesi.

Per farlo inseriamo `?<name>` subito dopo la parentesi di apertura.

Cerchiamo una data, ad esempio, nel formato "year-month-day":

```js

let dateRegexp = /(?<year>[0-9]{4})-(?<month>[0-9]{2})-(?<day>[0-9]{2})/;

let str = "2019-04-30";

let groups = str.match(dateRegexp).groups;

alert(groups.year); // 2019
alert(groups.month); // 04
alert(groups.day); // 30
```

Come potete osservare, troviamo i gruppi dentro la proprietà `.groups`.

Per cercare tutte le date, possiamo aggiungere il flag `g`.

Abbiamo inoltre bisogno di `matchAll` per ottenere sia le corrispondenze sia il dettaglio dei gruppi:

```js
let dateRegexp = /(?<year>[0-9]{4})-(?<month>[0-9]{2})-(?<day>[0-9]{2})/g;

let str = "2019-10-30 2020-01-01";

let results = str.matchAll(dateRegexp);

for(let result of results) {
  let {year, month, day} = result.groups;

  alert(`${day}.${month}.${year}`);
  // primo alert: 30.10.2019
  // secondo: 01.01.2020
}
```

## Sostituire testo con i gruppi di acquisizione

Il metodo `str.replace(regexp, replacement)`, che sostituisce tutti i riscontri con `regexp` in `str`, consente di usare il contenuto tra parentesi nella stringa `replacement`. Per farlo si usa `$n`, dove `n` indica il numero del gruppo.

Ad esempio,

```js
let str = "John Bull";
let regexp = /(\w+) (\w+)/;

alert( str.replace(regexp, '$2, $1') ); // Bull, John
```

Per i gruppi nominati il riferimento sarà `$<name>`.

Rimoduliamo, ad esempio, le date da "year-month-day" a "day.month.year":

```js
let regexp = /(?<year>[0-9]{4})-(?<month>[0-9]{2})-(?<day>[0-9]{2})/g;

let str = "2019-10-30, 2020-01-01";

alert( str.replace(regexp, '$<day>.$<month>.$<year>') );
// 30.10.2019, 01.01.2020
```

## I gruppi non acquisiti e l'uso di ?:

Talvolta abbiamo bisogno delle parentesi per applicare correttamente un quantificatore, ma non vogliamo il loro contenuto nel risultato.

Un gruppo può essere escluso aggiungendo `?:` dopo la parentesi di apertura.

Se desideriamo, ad esempio, cercare `(go)+`, ma non vogliamo il contenuto tra le parentesi (`go`) in un elemento dell'array, scriveremo: `(?:go)+`.

Nell'esempio qui di seguito otterremo solo il nome `John` come elemento distinto nel risultato:

```js
let str = "Gogogo John!";


// ?: esclude 'go' dall'acquisizione
let regexp = /(?:go)+ (\w+)/i;


let result = str.match(regexp);

alert( result[0] ); // Gogogo John (l'intera corrispondenza)
alert( result[1] ); // John
alert( result.length ); // 2 (non ci sono ulteriori elementi nell'array)
```

## Riepilogo

Le parentesi raggruppano insieme una parte dell'espressione regolare, in modo che il quantificatore si applichi al gruppo nel suo insieme.

I gruppi tra parentesi sono numerati da sinistra verso destra, e, facoltativamente, si può attribuire loro un nome `(?<name>...)`.

Il contenuto di un gruppo può essere ottenuto nei risultati:

- Il metodo `str.match` restituisce i gruppi di acquisizione solo se non è presente il flag `g`.
- Il metodo `str.matchAll` restituisce in ogni caso i gruppi di acquisizione.

Se le parentesi non hanno alcun nome, il loro contenuto è disponibile nell'array dei risultati col rispettivo numero. I gruppi nominati sono disponibili anche nella proprietà `groups`.

Possiamo usare, inoltre, il contenuto tra parentesi nella sostituzione di stringhe con `str.replace`: in base al numero `$n` o in base al nome `$<name>`.

Un gruppo può essere escluso dalla numerazione aggiungendo `?:` dopo la parentesi di apertura. Di solito si fa se abbiamo bisogno di applicare un quantificatore ad un intero gruppo, ma non vogliamo che quel gruppo compaia come elemento distinto nell'array dei risultati. In quel caso non possiamo nemmeno usare un riferimento a tali gruppi nella sostituzione di stringhe.

## Esercizi

### 1 · Verificate il MAC-address

Il [MAC-address](https://it.wikipedia.org/wiki/Indirizzo_MAC) di un'interfaccia di rete è composto da 6 coppie di cifre esadecimali separati dai due punti.

Per esempio: `'01:32:54:67:89:AB'`.

Scrivi una regexp che controlli se una stringa sia un MAC-address.

Uso:
```js
let reg = /la tua regexp/;

alert( reg.test('01:32:54:67:89:AB') ); // true

alert( reg.test('0132546789AB') ); // false (non ci sono i due punti)

alert( reg.test('01:32:54:67:89') ); // false (5 coppie, devono essere 6)

alert( reg.test('01:32:54:67:89:ZZ') ) // false (ZZ alla fine)
```

::::: details Soluzione

Un numero esadecimale a due cifre è `[0-9a-f]{2}` (dando per scontato che il flag `i` sia presente).

Dobbiamo trovare quel numero `NN`, seguito da `:NN` ripetuto 5 volte.

L'espressione regolare è: `[0-9a-f]{2}(:[0-9a-f]{2}){5}`

Osserviamo, a questo punto, che la corrispondenza dovrebbe catturare tutto il testo: dall'inizio alla fine. A questo scopo racchiudiamo il pattern all'interno di `^...$`.

Quindi:

```js
let regexp = /^[0-9a-f]{2}(:[0-9a-f]{2}){5}$/i;

alert( regexp.test('01:32:54:67:89:AB') ); // true

alert( regexp.test('0132546789AB') ); // false (non ci sono i due punti)

alert( regexp.test('01:32:54:67:89') ); // false (5 numeri invece di 6)

alert( regexp.test('01:32:54:67:89:ZZ') ) // false (ZZ alla fine)
```

:::::

### 2 · Trovate un colore nel formato #abc o #abcdef

Scrivete un'espressione regolare che trovi i colori nel formato `#abc` o `#abcdef`. In altre parole: `#` seguito da 3 o 6 cifre esadecimali.

Esempio d'uso:
```js
let regexp = /your regexp/g;

let str = "color: #3f3; background-color: #AA00ef; and: #abcd";

alert( str.match(regexp) ); // #3f3 #AA00ef
```

P.S. Dovrebbe trovare esattamente 3 o 6 cifre esadecimali. I valori con 4 cifre, come `#abcd`, non dovrebbero dar luogo a corrispondenza.

::::: details Soluzione

L'espressione regolare per cercare il codice di un colore di 3 cifre `#abc` è : `/#[a-f0-9]{3}/i`.

Possiamo aggiungere esattamente 3 ulteriori cifre esadecimali opzionali. Non abbiamo bisogno di altro. Il codice di un colore è composto da 3 o 6 cifre.

Usiamo il quantificatore `{1,2}` a questo scopo: avremo `/#([a-f0-9]{3}){1,2}/i`.

In questo caso il pattern `[a-f0-9]{3}` è racchiuso tra parentesi per applicare ad esso il quantificatore `{1,2}`.

Eccolo in azione:

```js
let regexp = /#([a-f0-9]{3}){1,2}/gi;

let str = "color: #3f3; background-color: #AA00ef; and: #abcd";

alert( str.match(regexp) ); // #3f3 #AA00ef #abc
```

C'è un piccolo problema adesso: il pattern `#abc` trovato in `#abcd`. Per evitarlo possiamo aggiungere `\b` alla fine:

```js
let regexp = /#([a-f0-9]{3}){1,2}\b/gi;

let str = "color: #3f3; background-color: #AA00ef; and: #abcd";

alert( str.match(regexp) ); // #3f3 #AA00ef
```

:::::

### 3 · Trovate tutti i numeri

Scrivete un'espressione regolare che cerchi tutti i numeri decimali e interi, con virgola mobile e negativi.

Un esempio d'uso:

```js
let regexp = /your regexp/g;

let str = "-1.5 0 2 -123.4.";

alert( str.match(regexp) ); // -1.5, 0, 2, -123.4
```

::::: details Soluzione

Un numero positivo con una parte decimale opzionale è: `\d+(\.\d+)?`.

Aggiungiamo all'inizio il segno meno facoltativo `-`:

```js
let regexp = /-?\d+(\.\d+)?/g;

let str = "-1.5 0 2 -123.4.";

alert( str.match(regexp) );   // -1.5, 0, 2, -123.4
```

:::::

### 4 · Analizzate un'espressione

Un'espressione aritmetica consiste in 2 numeri e un operatore tra di essi, ad esempio:

- `1 + 2`
- `1.2 * 3.4`
- `-3 / -6`
- `-2 - 2`

L'operatore è uno fra: `"+"`, `"-"`, `"*"` o `"/"`.

Potrebbero esserci ulteriori spazi all'inizio, alla fine o tra gli elementi.

Create una funzione `parse(expr)` che riceva un'espressione e restituisca un array di 3 elementi:

1. Il primo numero.
2. L'operatore.
3. Il secondo numero.

Ad esempio:

```js
let [a, op, b] = parse("1.2 * 3.4");

alert(a); // 1.2
alert(op); // *
alert(b); // 3.4
```

::::: details Soluzione

L'espressione regolare per un numero è: `-?\d+(\.\d+)?`. L'abbiamo creata nell'esercizione precedente.

Per trovare un operatore usiamo `[-+*/]`. Il trattino `-` va posto all'inizio nelle parentesi quadre, in mezzo significherebbe un intervallo di caratteri, mentre noi vogliamo soltanto il carattere `-`.

Dovremmo fare l'escape dello slash `/` dentro una regexp JavaScript `/.../`, lo faremo dopo.

Abbiamo bisogno di un numero, un operatore, e quindi un altro numero. Tra di essi ci possono essere spazi opzionali.

Ecco l'intera espressione regolare: `-?\d+(\.\d+)?\s*[-+*/]\s*-?\d+(\.\d+)?`.

Questa consta di 3 parti, intervallate da `\s*`:
1. `-?\d+(\.\d+)?` - il primo numero,
1. `[-+*/]` - l'operatore,
1. `-?\d+(\.\d+)?` - il secondo numero.

Per rendere ciascuna di queste parti un elemento separato dell'array di risultati le racchiudiamo tra parentesi: `(-?\d+(\.\d+)?)\s*([-+*/])\s*(-?\d+(\.\d+)?)`.

In azione:

```js
let regexp = /(-?\d+(\.\d+)?)\s*([-+*\/])\s*(-?\d+(\.\d+)?)/;

alert( "1.2 + 12".match(regexp) );
```

Il risultato include:

- `result[0] == "1.2 + 12"` (l'intera corrispondenza)
- `result[1] == "1.2"` (il primo gruppo `(-?\d+(\.\d+)?)`, il primo numero compresa la parte decimale)
- `result[2] == ".2"` (il secondo gruppo`(\.\d+)?`, la prima parte decimale)
- `result[3] == "+"` (il terzo gruppo `([-+*\/])`, l'operatore)
- `result[4] == "12"` (il quarto gruppo `(-?\d+(\.\d+)?)`, il secondo numero)
- `result[5] == undefined` (il quinto gruppo `(\.\d+)?`, l'ultima parte decimale è assente, quindi equivale ad undefined)

Il nostro scopo è ottenere i numeri e l'operatore, senza l'intera corrispondenza o le parti decimali, quindi "puliamo" un po' il risultato.

L'intera corrispondenza (il primo elemento dell'array) possiamo rimuoverla con `result.shift()`.

I gruppi che contengono le parti decimali (gli elementi 2 e 4) `(.\d+)` li escludiamo aggiungendo  `?:` all'inizio: `(?:\.\d+)?`.

La soluzione finale:

```js
function parse(expr) {
  let regexp = /(-?\d+(?:\.\d+)?)\s*([-+*\/])\s*(-?\d+(?:\.\d+)?)/;

  let result = expr.match(regexp);

  if (!result) return [];
  result.shift();

  return result;
}

alert( parse("-1.23 * 3.45") );  // -1.23, *, 3.45
```

:::::

