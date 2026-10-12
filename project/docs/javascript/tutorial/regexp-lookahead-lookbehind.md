---
title: "Lookahead e lookbehind"
description: "JavaScript.info in italiano: Lookahead e lookbehind"
sourceTutorial: true
prev: {"text": "Alternanza (OR) |", "link": "/javascript/tutorial/regexp-alternation"}
next: {"text": "Backtracking catastrofico", "link": "/javascript/tutorial/regexp-catastrophic-backtracking"}
---

# Lookahead e lookbehind

> **JavaScript.info · Ilya Kantor e contributori.** [Originale inglese](https://javascript.info/regexp-lookahead-lookbehind) · [Edizione italiana](https://it.javascript.info/regexp-lookahead-lookbehind) · [Fonti e licenza](/javascript/fonti).

Talvolta abbiamo bisogno di trovare soltanto quei riscontri per un pattern che sono seguiti o preceduti da un altro pattern.

Esiste a questo scopo una sintassi speciale denominata "lookahead" e "lookbehind", indicata complessivamente con il termine "lookaround".

Per cominciare troviamo il prezzo in una stringa come `1 turkey costs 30€`. In parole semplici: un numero seguito dal simbolo di valuta `€`.

## Lookahead

La sintassi è: `X(?=Y)`, che significa "cerca `X`, ma trova la corrispondenza solo se seguita da `Y`". Possiamo sostituire `X` e `Y` con un pattern qualsiasi.

Per un numero intero seguito da `€`, la regexp sarà `\d+(?=€)`:

```js
let str = "1 turkey costs 30€";

alert( str.match(/\d+(?=€)/) ); // 30, viene ignorato il numero 1 in quanto non seguito da €
```

Si noti che la parte lookahead è solo un test e pertanto il contenuto tra parentesi `(?=...)` non è incluso nel risultato `30`.

Quando cerchiamo `X(?=Y)` l'interprete dell'espressione regolare trova `X` e successivamente verifica anche la presenza di `Y` subito dopo di esso. In caso contrario la corrispondenza potenziale viene scartata e la ricerca prosegue.

Sono possibili test più complessi, ad esempio `X(?=Y)(?=Z)` significa:

1. Trova `X`.
2. Verifica se `Y` sia subito dopo `X` (non proseguire in caso contrario).
3. Verifica se `Z` sia anch'esso dopo `X` (non proseguire in caso contrario).
4. Se entrambi i test trovano riscontro considera `X` una corrispondenza, diversamente continua la ricerca.

In altre parole, questo pattern significa che stiamo cercando `X` seguito sia da `Y` sia da `Z`.

Il che è possibile solo se i pattern `Y` e `Z` non si escludono a vicenda.

Per esempio, `\d+(?=\s)(?=.*30)` cerca `\d+` seguito da uno spazio `(?=\s)`, e poi c'è `30` da qualche parte dopo di esso `(?=.*30)`:

```js
let str = "1 turkey costs 30€";

alert( str.match(/\d+(?=\s)(?=.*30)/) ); // 1
```

Nella nostra stringa trova esatta corrispondenza nel numero `1`.

## Lookahead negativo

Supponiamo invece di volere nella stessa stringa solo la quantità, non il prezzo. Quindi il numero `\d+`, NON seguito da `€`.

A questo scopo può essere applicato un lookahead negativo.

La sintassi è: `X(?!Y)`, significa "cerca `X`, ma solo se non seguito da `Y`".

```js
let str = "2 turkeys cost 60€";

alert( str.match(/\d+\b(?!€)/g) ); // 2 (il prezzo non costituisce corrispondenza)
```

## Lookbehind

Lookahead permette di porre una condizione per "quello che segue".

Lookbehind è simile, ma cerca quello che precede. Consente quindi di trovare una corrispondenza per un pattern solo se c'è qualcosa prima di esso.

La sintassi è:
- Lookbehind positivo: `(?<=Y)X`, trova `X`, ma solo se c'è `Y` prima di esso.
- Lookbehind negativo: `(?<!Y)X`, trova `X`, ma solo se non c'è alcun `Y` prima di esso.

Cambiamo, ad esempio, il prezzo in dollari USA. Il segno del dollaro è posto di solito prima del numero, per cercare pertanto `$30` useremo `(?<=\$)\d+` un importo preceduto da `$`:

```js
let str = "1 turkey costs $30";

// facciamo l'escape al segno del dollaro \$
alert( str.match(/(?<=\$)\d+/) ); // 30 (salta il numero senza segno di valuta)
```

Se abbiamo bisogno della quantità, il numero, non preceduto da `$`, allora possiamo usare il lookbehind negativo `(?<!\$)\d+`:

```js
let str = "2 turkeys cost $60";

alert( str.match(/(?<!\$)\b\d+/g) ); // 2 (il risultato non include il prezzo)
```

## Gruppi di acquisizione

Generalmente il contenuto dentro le parentesi di lookaround non diventa parte del risultato.

Nel pattern `\d+(?=€)`, ad esempio, il segno `€` non viene acquisito nella corrispondenza. È del tutto normale: stiamo cercando il numero `\d+`, mentre `(?=€)` è solo un test che indica che il numero dovrebbe essere seguito da `€`.

In alcune situazioni, tuttavia, potremmo voler catturare anche l'espressione del lookaround, o una parte di essa. Questo è possibile: è sufficiente racchiudere la parte desiderata all'interno di parentesi aggiuntive.

Nell'esempio sotto, il segno di valuta `(€|kr)` viene acquisito insieme all'importo:

```js
let str = "1 turkey costs 30€";
let regexp = /\d+(?=(€|kr))/; // parentesi addizionali intorno €|kr

alert( str.match(regexp) ); // 30, €
```

Stesso discorso per il lookbehind:

```js
let str = "1 turkey costs $30";
let regexp = /(?<=(\$|£))\d+/;

alert( str.match(regexp) ); // 30, $
```

## Riepilogo

Il lookahead e il lookbehind (comunemente denominati con il termine "lookaround") sono utili quando vogliamo trovare qualcosa in base a ciò viene prima o dopo di esso.

Nel caso di espressioni regolari semplici potremmo ottenere lo stesso risultato manualmente. In altre parole: troviamo ogni riscontro, e quindi filtriamo i risultati in base alla posizione nel ciclo iterativo.

Ricordiamoci che `str.match` (senza il flag `g`) e `str.matchAll` (sempre) restituiscono i risultati in un array con la proprietà `index`, conosciamo pertanto l'esatta posizione della corrispondenza e possiamo stabilirne il contesto.

Generalmente, però, il lookaround è più efficiente.

Tipi di lookaround:

| Pattern            | Tipo             | Riscontri |
|--------------------|------------------|---------|
| `X(?=Y)`   | Lookahead positivo | `X` se seguito da `Y` |
| `X(?!Y)`   | Lookahead negativo | `X` se seguito da `Y` |
| `(?<=Y)X` |  Lookbehind positivo | `X` se dopo `Y` |
| `(?<!Y)X` | Lookbehind negativo | `X` se dopo `Y` |

## Esercizi

### 1 · Trovate gli interi non negativi

Data una stringa di numeri interi, create una regexp che cerchi solo quelli non negativi (lo zero è consentito).

Un esempio d'uso:
```js
let regexp = /your regexp/g;

let str = "0 12 -5 123 -18";

alert( str.match(regexp) ); // 0, 12, 123
```

::::: details Soluzione

La regexp per un numero intero è `\d+`.

Possiamo escludere i numeri negativi anteponendo il segno meno con il lookbehind: `(?<!-)\d+`.

Anche se, nel caso in cui lo provassimo ora, potremmo notare un altro risultato inatteso:

```js
let regexp = /(?<!-)\d+/g;

let str = "0 12 -5 123 -18";

console.log( str.match(regexp) ); // 0, 12, 123, 8
```

Come potete osservare trova `8` da `-18`. Per escluderlo, dobbiamo assicurarci che la regexp non cominci a cercare una corrispondenza di un numero dalla metà di un altro numero non corrispondente.

Possiamo farlo specificando un altro lookbehind negativo: `(?<!-)(?<!\d)\d+`. Ora `(?<!\d)` assicura che la corrispondenza non cominci dopo un altro numero, proprio quello che volevamo.

Potremmo anche unire il tutto in un singolo lookbehind in questo modo:

```js
let regexp = /(?<![-\d])\d+/g;

let str = "0 12 -5 123 -18";

alert( str.match(regexp) ); // 0, 12, 123
```

:::::

### 2 · Inserimento dopo la sezione head

Abbiamo una stringa e un documento HTML.

Scrivete un'espressione regolare che inserisca `<h1>Hello</h1>` subito dopo il tag `<body>`. Il tag può avere degli attributi.

Per esempio:

```js
let regexp = /your regular expression/;

let str = `
<html>
  <body style="height: 200px">
  ...
  </body>
</html>
`;

str = str.replace(regexp, `<h1>Hello</h1>`);
```

Dopo l'inserimento il valore di `str` dovrebbe essere:
```html
<html>
  <body style="height: 200px"><h1>Hello</h1>
  ...
  </body>
</html>
```

::::: details Soluzione

Per inserire qualcosa dopo il tag `<body>` dobbiamo prima trovarlo. A questo scopo possiamo usare l'espressione regolare `<body.*?>`.

In questa esercitazione non abbiamo bisogno di modificare il tag `<body>`. Dobbiamo solo aggiungere del testo dopo di esso.

Ecco come possiamo farlo:

```js
let str = '...<body style="...">...';
str = str.replace(/<body.*?>/, '$&<h1>Hello</h1>');

alert(str); // ...<body style="..."><h1>Hello</h1>...
```

Nella stringa di sostituzione `$&` identifica la stessa corrispondenza, in altre parole, la parte della stringa sorgente che trova riscontro con `<body.*?>`. Essa viene sostituita da se stessa più l'aggiunta di `<h1>Hello</h1>`.

L'uso del lookbehind costituisce un'alternativa:

```js
let str = '...<body style="...">...';
str = str.replace(/(?<=<body.*?>)/, `<h1>Hello</h1>`);

alert(str); // ...<body style="..."><h1>Hello</h1>...
```

Come potete osservare, c'è solo la parte di lookbehind in questa regexp.

Funziona in questo modo:
- Per ogni posizione nella stringa.
- Verifica se è preceduta da `<body.*?>`.
- In caso affermativo abbiamo trovato la corrispondenza.

Il tag `<body.*?>` non verrà restituito. Il risultato di questa regexp è letteralmente una stringa vuota, ma individua le posizioni precedute da `<body.*?>`.

Quindi sostituisce uno "spazio vuoto" preceduto da `<body.*?>`, con `<h1>Hello</h1>`. In altre parole effettua un inserimento dopo `<body>`.

P.S. I flag `s` e `i` potrebbero inoltre risultare utili: `/<body.*?>/si`. Il flag `s` fa in modo che il `.` identifichi anche un carattere di nuova riga, e con il flag `i` otteniamo che `<body>` e `<BODY>` costituiscano entrambi un riscontro.

:::::

