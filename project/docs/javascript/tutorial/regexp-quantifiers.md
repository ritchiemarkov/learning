---
title: "Quantificatori +, *, ? and"
description: "JavaScript.info in italiano: Quantificatori +, *, ? and"
sourceTutorial: true
prev: {"text": "Insiemi e intervalli [...]", "link": "/javascript/tutorial/regexp-character-sets-and-ranges"}
next: {"text": "Modalità greedy e lazy dei quantificatori", "link": "/javascript/tutorial/regexp-greedy-and-lazy"}
---

# Quantificatori +, *, ? and {n}

> **JavaScript.info · Ilya Kantor e contributori.** [Originale inglese](https://javascript.info/regexp-quantifiers) · [Edizione italiana](https://it.javascript.info/regexp-quantifiers) · [Fonti e licenza](/javascript/fonti).

Se si ha una stringa come la seguente: `+7(903)-123-45-67` e si vogliono trovare tutti i numeri che contiene ma, diversamente da prima, non siamo interessati alle singole cifre bensì agli interi numeri: `7, 903, 123, 45, 67`.

Se definisce numero un sequenza di una o più cifre `\d`, per marcare quanti ne servono si deve aggiungere in coda un *quantificatore*.

## Quantità {n}

Il quantificatore più semplice è un numero tra parentesi graffe `{n}`.

Un quantificatore si appende a un carattere (o a una classe di caratteri `[...]` un set, ecc..) specificando quante volte questo debba essere ripetuto.
Si riportano alcune forme avanzate, eccone alcuni esempi:

Il conteggio esatto: `{5}`
: `\d{5}` denota esattamente 5 cifre, identico a `\d\d\d\d\d`.

    Nell'esempio sottostante si cerca un numero a 5 cifre:
    
    ```js
    alert( "Ho 12345 anni".match(/\d{5}/) ); //  "12345"
    ```

    Si può aggiungere `\b` per escludere i numeri più lunghi: `\b\d{5}\b`.

L'intervallo: `{3,5}`, trova da 3 a 5 ripetizioni.
: Per trovare i numeri da 3 a 5 cifre si possono mettere i limiti tra parentesi graffe: `\d{3,5}`

    ```js
    alert( "Non ho 12 anni 12, ma 1234".match(/\d{3,5}/) ); // "1234"
    ```

    Si può tralasciare il limite superiore.

    In questo caso la regexp `\d{3,}` cercherà successioni di cifre lunghe `3` o più:

    ```js
    alert( "Non ho 12 anni, ma 345678".match(/\d{3,}/) ); // "345678"
    ```

Torniamo alla stringa: `+7(903)-123-45-67`.

Un numero è una sequenza di una o più cifre in successione, dunque l'espressione regolare sarà `\d{1,}`:

```js
let str = "+7(903)-123-45-67";

let numeri = str.match(/\d{1,}/g);

alert(numeri); // 7,903,123,45,67
```

## Abbreviazioni 

Sono presenti abbreviazioni per i quantificatori di uso più comune:

`+`
: Significa "uno o più", identico a `{1,}`.

    Ad esempio, `\d+` cerca i numeri:

    ```js
    let str = "+7(903)-123-45-67";

    alert( str.match(/\d+/g) ); // 7,903,123,45,67
    ```

`?`
: Significa "zero o uno" identico a `{0,1}`. In altri termini rende il simbolo opzionale.

    Ad esempio, il pattern `ou?r` cerca `o` seguito opzionalmente da `u`, quindi da `r`.

    Dunque, `colou?r` trova sia `color` che `colour`:

    ```js
    let str = "In Inglese \"colore\" si scrive sia \"color\" che \"colour\"?";

    alert( str.match(/colou?r/g) ); // color, colour
    ```

`*`
: Significa "zero o più", lo stesso che `{0,}`. Significa che il carattere può esserci, essere ripetuto o mancare.

    Ad esempio, `\d0*` cerca una cifra seguita da un numero arbitrario di zeri:

    ```js
    alert( "100 10 1".match(/\d0*/g) ); // 100, 10, 1
    ```

    Confronto con `'+'` (uno o più):

    ```js
    alert( "100 10 1".match(/\d0+/g) ); // 100, 10
    // 1 non compare, poiché 0+ richiede almeno uno 0
    ```

## Altri esempi

I quantificatori si usano spesso; essi costituiscono i blocchi principali per espressioni regolari complesse, si riportano in seguito altri esempi.

Regexp "frazione decimale" (un numero con la virgola): `\d+,\d+`
: In funzione:
    ```js
    alert( "0 1 12,345 7890".match(/\d+,\d+/g) ); // 12,345
    ```

Regexp "Apertura di un tag HTML senza attributi" come, ad esempio, `<span>` oppure `<p>`: `/<[a-z]+>/i`
: In funzione:

    ```js
    alert( "<body> ... </body>".match(/<[a-z]+>/gi) ); // <body>
    ```

    Cerchiamo il carattere `'<'` seguito da una o più lettere latine one or more Latin letters, quindi  `'>'`.

Regexp "Apertura di un tag HTML senza attributi" (migliorato): `/<[a-z][a-z0-9]*>/i`
: Espressione regolare migliore: secondo lo standard, il nome di un tag HTML può avere cifre in qualsiasi posizione tranne la prima `<h1>`.

    ```js
    alert( "<h1>Hi!</h1>".match(/<[a-z][a-z0-9]*>/gi) ); // <h1>
    ```

Regexp "Apertura o chiusura di un tag HTML senza attributi": `/<\/?[a-z][a-z0-9]*>/i`
: Aggiungiamo una slash opzionale `/?` prima del nome tag, dobbiamo farne l'escape altrimenti JavaScript penserebbe che sia la fine del pattern.

We added an optional slash `/?` near the beginning of the pattern. Had to escape it with a backslash, otherwise JavaScript would think it is the pattern end.

```js
alert( "<h1>Hi!</h1>".match(/<\/?[a-z][a-z0-9]*>/gi) ); // <h1>, </h1>
```


::: tip Per rendere una espressione regolare più precisa, spesso dobbiamo renderla anche più complessa
Possiamo vederne una regola comune in questo esempio: più l'espressione regolare è precisa -- più è lunga e complicata.

Ad esempio, per i tag HTML è possibile usare un'espressione regolare più semplice: `<\w+>`.

...Ma poiché `\w` intercetta qualsiasi lettera dell'alfabeto latino e il carattere `'_'`, la regexp intercetta anche dei non-tag, come `<_>`. Dunque è molto più semplice del pattern `<[a-z][a-z0-9]*>`, ma anche meno affidabile.

Basta accontentarsi di `<\w+>` o è necessario `<[a-z][a-z0-9]*>`?

La risposta è che nella vita reale entrambi sono accettabili; dipende però dal bilanciamento tra l'avere molte corrispondenze "extra" da filtrare in altri modi rispetto all'avere un'espressione regolare più complessa.
:::

## Esercizi

### 1 ·  Come trovare i puntini di sospensione "..." ?

Si crei un'espressione regolare che individui i puntini di sospensione: 3 (o più) punti in fila

Prova:

```js
let reg = /la tua regex/g;
alert( "Ciao!... come va?.....".match(reg) ); // ..., .....
```

::::: details Soluzione

Soluzione:

```js
let reg = /\.{3,}/g;
alert( "Ciao!... Come va?.....".match(reg) ); // ..., .....
```

Si noti che il punto è un carattere speciale pertanto è stato necessario farne l'escape inserendolo come `\.`.

:::::

### 2 · Regexp per la ricerca di colori espressi in formato HTML

Si crei un'espressione regolare per trovare i colori HTML in notazione `#ABCDEF`: all'inizio un carattere `#` quindi 6 cifre esadecimali.

Un esempio di uso:

```js
let reg = /...la tua regexp.../

let str = "color:#121212; background-color:#AA00ef bad-colors:f#fddee #fd2 #12345678";

alert( str.match(regexp) )  // #121212,#AA00ef
```

P.S. In questo esercizio non � richiesto di intercettare i colori espressi anche in altri formati come: `#123` o `rgb(1,2,3)` ecc.

::::: details Soluzione

Dobbiamo cercare il carattere `#` seguito da 6 cifre esadecimalis.

Possiamo descrivere una cifra esadecimale con il `[0-9a-fA-F]`, oppure, usando il flag `i` possiamo usare `[0-9a-f]`.

Dunque si cerchino 6 pattern usando il quantificatore `{6}`.

Il risultato sar� l'espressione regolare: `/#[a-f0-9]{6}/gi`.

```js
let regexp = /#[a-f0-9]{6}/gi;

let str = "color:#121212; background-color:#AA00ef bad-colors:f#fddee #fd2"

alert( str.match(regexp) );  // #121212,#AA00ef
```

Il problema � che cos� si trova il colore anche in sequenze pi� lunghe di 6 caratteri:

```js
alert( "#12345678".match( /#[a-f0-9]{6}/gi ) ) // #123456
```

Per sisolvere tale problema si pu� aggiungere `\b` in coda all'espressione:

```js
// Un valore corrispondente colore
alert( "#123456".match( /#[a-f0-9]{6}\b/gi ) ); // #123456

// Un valore non corrispondente a un colore
alert( "#12345678".match( /#[a-f0-9]{6}\b/gi ) ); // null
```

:::::

