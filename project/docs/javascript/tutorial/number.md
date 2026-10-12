---
title: "Numeri"
description: "JavaScript.info in italiano: Numeri"
sourceTutorial: true
prev: {"text": "Metodi dei tipi primitivi", "link": "/javascript/tutorial/primitives-methods"}
next: {"text": "Stringhe", "link": "/javascript/tutorial/string"}
---

# Numeri

> **JavaScript.info · Ilya Kantor e contributori.** [Originale inglese](https://javascript.info/number) · [Edizione italiana](https://it.javascript.info/number) · [Fonti e licenza](/javascript/fonti).

Nella versione moderna di JavaScript ci sono due differenti tipi di numeri:

1. I numeri regolari, che vengono memorizzati nel formato a 64 bit [IEEE-754](https://en.wikipedia.org/wiki/IEEE_754-2008_revision), conosciuti anche come "numeri in virgola mobile con doppia precisione". Questi sono i numeri che utilizziamo la maggior parte del tempo, e sono quelli di cui parleremo in questo capitolo.

2. I BigInt, che vengono utilizzati per rappresentare numeri interi di lunghezza arbitraria. Talvolta possono tornare utili, poiché i numeri regolari non possono eccedere <code>2<sup>53</sup></code> od essere inferiori di <code>-2<sup>53</sup></code>. Poiché i BigInt vengono utilizzati in alcune aree speciali, gli abbiamo dedicato un capitolo [BigInt](/javascript/tutorial/bigint).

Quindi in questo capitolo parleremo dei numeri regolari.

## Diversi modi di scrivere un numero

Immaginiamo di dover scrivere 1 milione. La via più ovvia è:

```js
let billion = 1000000000;
```

Possiamo anche usare il carattere underscore `_` come separatore:

```js
let billion = 1_000_000_000;
```

Qui il carattere `_` gioca il ruolo di "zucchero sintattico", cioè rende il numero più leggibile. Il motore JavaScript semplicemente ignorerà i caratteri `_` tra le cifre, quindi è equivalente al milione scritto sopra.

Nella vita reale però cerchiamo di evitare di scrivere lunghe file di zeri per evitare errori. E anche perché siamo pigri. Solitamente scriviamo qualcosa del tipo `"1ml"` per un milione o `"7.3ml"` 7 milioni e 300mila. Lo stesso vale per i numeri più grandi.

In JavaScript, possiamo abbreviare un numero inserendo la lettera `"e"` con il numero di zeri a seguire:

```js
let billion = 1e9;  // 1 miliardo, letteralmente: 1 e 9 zeri

alert( 7.3e9 );  // 7.3 miliardi (equivale a 7300000000 o 7_300_000_000)
```

In altre parole, `"e"` moltiplica il numero `1` seguito dal numero di zeri dati.


```js
1e3 = 1 * 1000 // e3 significa *1000
1.23e6 = 1.23 * 1000000 // e6 significa *1000000
```

Ora proviamo a scrivere qualcosa di molto piccolo. Ad esempio, 1 microsecondo (un milionesimo di secondo): 

```js
let ms = 0.000001;
```

Come prima, l'utilizzo di `"e"` può aiutare. Se volessimo evitare di scrivere esplicitamente tutti gli "0", potremmo scrivere:

```js
let ms = 1e-6; // sei zeri alla sinistra di 1
```

Se contiamo gli zeri in `0.000001`, ce ne sono 6. Quindi ovviamente `1e-6`.  

In altre parole, un numero negativo dopo `"e"` significa una divisione per 1 seguito dal numero di zeri dati:

```js
// -3 divide 1 con 3 zeri
1e-3 = 1 / 1000; // 0.001

// -6 divide 1 con 6 zeri
1.23e-6 = 1.23 / 1000000; // 0.00000123
```

### Numeri esadecimali, binari e ottali

I numeri [esadecimali](https://en.wikipedia.org/wiki/Hexadecimal) (hexadecimal o hex) sono largamente utilizzati in JavaScript per rappresentare colori, codifiche di caratteri, e molte altre cose. Quindi ovviamente esiste un modo per abbreviarli: `0x` e poi il numero.

Ad esempio:

```js
alert( 0xff ); // 255
alert( 0xFF ); // 255 (equivalente)
```

I sistemi binario e ottale sono utilizzati raramente, ma sono comunque supportati con l'utilizzo dei prefissi `0b` e `0o`:


```js
let a = 0b11111111; // forma binaria di 255
let b = 0o377; // forma ottale di 255

alert( a == b ); // true, lo stesso numero 255 da entrambe le parti
```

Ci sono solo 3 sistemi di numerazione con questo livello di supporto. Per gli altri sistemi, dovremmo utilizzare la funzione `parseInt` (che vedremo più avanti in questo capitolo).

## toString(base)

Il metodo `num.toString(base)` ritorna una rappresentazione in stringa del numero `num` con il sistema di numerazione fornito `base`.

Ad esempio:
```js
let num = 255;

alert( num.toString(16) );  // ff
alert( num.toString(2) );   // 11111111
```

La `base` può variare da `2` a `36`. Di default vale `10`.

Altri casi di uso comune sono:

- **base=16** si utilizza per colori in esadecimale, codifiche di caratteri, i caratteri supportati sono `0..9` o `A..F`.
- **base=2** viene utilizzato per debugging o operazioni bit a bit, i caratteri accettati sono `0` o `1`.
- **base=36** la base massima, i caratteri possono andare da `0..9` o `A..Z`. L'intero alfabeto latino viene utilizzato per rappresentare un numero. Un caso divertente di utilizzo per la base `36` è quando abbiamo bisogno che un identificatore molto lungo diventi qualcosa di più breve, come ad esempio per accorciare gli url. Possiamo semplicemente rappresentarlo in base `36`:

    ```js
    alert( 123456..toString(36) ); // 2n9c
    ```


::: warning Due punti per chiamare un metodo
Da notare che i due punti in `123456..toString(36)` non sono un errore. Se vogliamo chiamare un metodo direttamente da un numero, come `toString` nell'esempio sopra, abbiamo bisogno di inserire due punti `..`.

Se inseriamo un solo punto: `123456.toString(36)`, otterremo un errore, perché la sintassi JavaScript implica una parte decimale a seguire del primo punto. Se invece inseriamo un ulteriore punto, allora JavaScript capirà che la parte decimale è vuota e procederà nel chiamare il metodo.

Potremmo anche scrivere `(123456).toString(36)`.
:::

## Arrotondare

Una delle operazioni più utilizzate quando lavoriamo con i numeri è l'arrotondamento.

Ci sono diverse funzioni integrate per eseguire questa operazione:

`Math.floor`
: Arrotonda per difetto: `3.1` diventa `3`, e `-1.1` diventa `-2`.

`Math.ceil`
: Arrotonda per eccesso: `3.1` diventa `4`, e `-1.1` diventa `-1`.

`Math.round`

: Arrotonda all'intero più vicino: `3.1` diventa `3`, `3.6` diventa `4`, e `3.5` viene arrotondato anch'esso a `4`.

`Math.trunc` (non supportato da Internet Explorer)
: Rimuove tutto dopo la virgola decimale senza arrotondare: `3.1` diventa `3`, `-1.1` diventa `-1`.

Qui abbiamo una tabella che riassume le principali differenze:

|   | `Math.floor` | `Math.ceil` | `Math.round` | `Math.trunc` |
|---|---------|--------|---------|---------|
|`3.1`|  `3`    |   `4`  |    `3`  |   `3`   |
|`3.6`|  `3`    |   `4`  |    `4`  |   `3`   |
|`-1.1`|  `-2`    |   `-1`  |    `-1`  |   `-1`   |
|`-1.6`|  `-2`    |   `-1`  |    `-2`  |   `-1`   |


Queste funzioni coprono tutti i possibili casi quando trattiamo numeri con una parte decimale. Come potremmo fare se volessimo arrotondare il numero ad `n` cifre dopo la virgola?

Ad esempio, abbiamo `1.2345` e vogliamo arrotondarlo a due cifre dopo la virgola, tenendo solo `1.23`.

Ci sono due modi per farlo:

1. Moltiplica e dividi.

    Ad esempio, per arrotondare un numero alla seconda cifra decimale, possiamo moltiplicare il numero per `100`,  chiamare la funzione di arrotondamento e dividerlo nuovamente.
    ```js
    let num = 1.23456;

    alert( Math.round(num * 100) / 100 ); // 1.23456 -> 123.456 -> 123 -> 1.23
    ```

2. Il metodo [toFixed(n)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/toFixed) arrotonda il numero a `n` cifre dopo la virgola e ritorna una rappresentazione in stringa del risultato.
        
    ```js
    let num = 12.34;
    alert( num.toFixed(1) ); // "12.3"
    ```

    Questo metodo arrotonderà per difetto o per eccesso in base al valore più vicino, similmente a `Math.round`:

    ```js
    let num = 12.36;
    alert( num.toFixed(1) ); // "12.4"
    ```

    Da notare che il risultato di `toFixed` è una stringa. Se la parte decimale è più breve di quanto richiesto, verranno aggiunti degli zeri:

    ```js
    let num = 12.34;
    alert( num.toFixed(5) ); // "12.34000", aggiunti gli zeri per renderlo esattamente di 5 cifre decimali
    ```

    Possiamo convertire il risultato al tipo numerico utilizzando la somma unaria o chiamando il metodo `Number()`: `+num.toFixed(5)`.

## Calcoli imprecisi

Internamente, un numero è rappresentato in formato 64-bit [IEEE-754](https://en.wikipedia.org/wiki/IEEE_754-2008_revision), quindi vengono utilizzati esattamente 64 bit per rappresentare un numero: 52 vengono utilizzati per rappresentare le cifre, 11 per la parte decimale, e infine 1 bit per il segno.

Se un numero è troppo grande, tale da superare i 64 bit disponibili, come ad esempio un numero potenzialmente infinito:

```js
alert( 1e500 ); // Infinity
```

Potrebbe essere poco ovvio, ma quello che accade è la perdita di precisione.

Consideriamo questo test (falso!):

```js
alert( 0.1 + 0.2 == 0.3 ); // false
```

Esatto, se provassimo a confrontare il risultato della somma tra `0.1` e `0.2` con `0.3`, otterremmo `false`. 

Strano! Quale può essere il risultato se non `0.3`?

```js
alert( 0.1 + 0.2 ); // 0.30000000000000004
```

Ouch! Un confronto errato di questo tipo può generare diverse conseguenze. Immaginate di progettare un sito di e-shop in cui i visitatori aggiungono al carrello articoli da `$0.10` e `$0.20`. Poi come prezzo totale viene mostrato `$0.30000000000000004`. Questo risultato lascerebbe sorpreso chiunque.

Ma perché accade questo?

Un numero viene memorizzato nella sua forma binaria, una sequenza di "1" e "0". I numeri con virgola come `0.1`, `0.2` che visti nella loro forma decimale sembrano semplici, sono in realtà una sequenza infinita di cifre nella forma binaria.

In altre parole, cos'è `0.1`? Vale 1 diviso 10 `1/10`, "un decimo". Nel sistema decimale questi numeri sono facilmente rappresentabili. Prendiamo invece "un terzo": `1/3`. Diventa un numero con infiniti decimali `0.33333(3)`. 

Quindi, le divisioni per potenze di `10` funzionano molto bene nel sistema decimale, non vale lo stesso con la divisione per `3`. Per la stessa ragione, nel sistema binario le divisioni per potenze di `2` sono una garanzia, ma `1/10` diventa una sequenza infinita di cifre.

Non esiste alcun modo per rappresentare *esattamente 0.1* o *esattamente 0.2* usando il sistema binario, proprio come non è possibile memorizzare "un terzo" come decimale.

Il formato numerico IEEE-754 cerca di risolvere questo arrotondando al più vicino numero possibile. Questo tipo di arrotondamento non ci consente di vedere le "piccole perdite di precisione", quindi il numero viene mostrato come `0.3`. Ma comunque è presente una perdita.

Possiamo vedere un esempio:
```js
alert( 0.1.toFixed(20) ); // 0.10000000000000000555
```

E quando sommiamo due numeri, la loro "perdita di precisione" viene incrementata.

Questo è il motivo per cui `0.1 + 0.2` non vale esattamente `0.3`.


::: tip Non solo JavaScript
Lo stesso problema esiste in molti altri linguaggi di programmazione.

PHP, Java, C, Perl, Ruby hanno lo stesso tipo di problema, poiché si basano sullo stesso formato numerico. 
:::

Possiamo risolvere questo problema? Certamente, ci sono diverse soluzioni:

1. Possiamo arrotondare il risultato con un metodo [toFixed(n)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/toFixed):

```js
let sum = 0.1 + 0.2;
alert( sum.toFixed(2) ); // 0.30
```

Da notare che `toFixed` ritorna sempre una stringa. Viene cosi garantito che ci siano almeno due cifre dopo la virgola decimale. Questo ci torna molto utile se abbiamo un e-shopping e vogliamo mostrare `$0.30`. Per tutti gli altri casi possiamo semplicemente chiamare la conversione con l'operatore di somma unaria:

```js
let sum = 0.1 + 0.2;
alert( +sum.toFixed(2) ); // 0.3
```

2. Possiamo temporaneamente convertire i numeri ad interi per eseguire le operazioni e poi riconvertirli. In questo modo:

```js
alert( (0.1 * 10 + 0.2 * 10) / 10 ); // 0.3
alert( (0.28 * 100 + 0.14 * 100) / 100); // 0.4200000000000001
```

Questo funziona perché quando facciamo `0.1 * 10 = 1` e `0.2 * 10 = 2` entrambi diventano interi, non vi è quindi perdita di precisione. 

3. Se abbiamo a che fare con dei prezzi, la miglior soluzione rimane quella di memorizzare tutti i prezzi in centesimi, evitando quindi di utilizzare i numeri con virgola. Ma cosa succede se proviamo ad applicare uno sconto del 30%? Nella pratica, evitare completamente questo problema è difficile, in alcuni casi possono tornare utili entrambe le soluzioni viste sopra.

Quindi, l'approccio moltiplicazione/divisione riduce gli errori, ma non li elimina completamente.

Talvolta possiamo evitare le frazioni. Ad esempio se abbiamo a che fare con un negozio, allora possiamo memorizzare i prezzi in centesimi piuttosto che in euro.


:::: tip La cosa divertente
Provate ad eseguire questo:

```js
// Ciao! Sono un numero autoincrementante!
alert( 9999999999999999 ); // mostra 10000000000000000
```

Questo esempio ha lo stesso problema: perdita di precisione. Per la rappresentazione di un numero sono disponibili 64bit, ne vengono utilizzati 52 per le cifre, questi potrebbero non essere sufficienti. Quindi le cifre meno significative vengono perse.

JavaScript non mostra errori in questi casi. Semplicemente fa del suo meglio per "farci stare" il numero, anche se il formato non è "grande" abbastanza.
::::


::: tip Due zeri
Un'altra conseguenza divertente della rappresentazione interna è l'esistenza di due zeri: `0` e `-0`.

Questo perché il segno viene rappresentato con un solo bit, in questo modo ogni numero può essere positivo o negativo, lo stesso vale per lo zero.

Nella maggior parte dei casi questa differenza è impercettibile, poiché gli operatori sono studiati per trattarli allo stesso modo.
:::

## Test: isFinite e isNaN

Ricordate questi due valori numerici speciali?

- `Infinity` (e `-Infinity`) è uno speciale valore che è più grande (o più piccolo) di qualsiasi altro numero.
- `NaN` rappresenta un errore.

Questi appartengono al tipo `number`, ma non sono dei numeri "normali", esistono quindi delle funzioni dedicate per la loro verifica:


- `isNaN(value)` converte l'argomento al tipo numerico e successivamente verifica se è un `NaN`:

    ```js
    alert( isNaN(NaN) ); // true
    alert( isNaN("str") ); // true
    ```

    Ma abbiamo veramente bisogno di questa funzione? Non possiamo semplicemente usare il confronto `=== NaN`? Purtroppo la risposta è no. Il valore `NaN` è unico in questo aspetto, non è uguale a niente, nemmeno a se stesso:

    ```js
    alert( NaN === NaN ); // false
    ```

- `isFinite(value)` converte l'argomento al tipo numerico e ritorna `true` se questo è un numero diverso da `NaN/Infinity/-Infinity`:

    ```js
    alert( isFinite("15") ); // true
    alert( isFinite("str") ); // false, perché rappresenta un valore speciale: NaN
    alert( isFinite(Infinity) ); // false, perché rappresenta un valore speciale: Infinity
    ```

In alcuni casi `isFinite` viene utilizzato per verificare se una stringa qualunque è un numero:


```js
let num = +prompt("Enter a number", '');

// risulterà true se non verrà inserito Infinity, -Infinity o un NaN
alert( isFinite(num) );
```

Da notare che una stringa vuota o contenente solo spazi viene trattata come `0` in qualsiasi funzione numerica, compresa `isFinite`.  


::: tip Confronto con `Object.is`

Esiste uno speciale metodo integrato [Object.is](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/is) che confronta valori proprio come `===`, ma risulta molto più affidabile in due casi limite:

1. Funziona con `NaN`: `Object.is(NaN, NaN) === true`, e questo è un bene. 
2. I valori `0` e `-0` sono diversi: `Object.is(0, -0) === false`, tecnicamente sarebbero uguali, però internamente vengono rappresentati con il bit di segno, che in questo caso è diverso.

In tutti gli altri casi, `Object.is(a, b)` equivale a `a === b`. 

Questo metodo di confronto viene spesso utilizzato in JavaScript. Quando un algoritmo interno ha necessità di verificare che due valori siano esattamente la stessa cosa, si utilizza `Object.is` (internamente chiamato [SameValue](https://tc39.github.io/ecma262/#sec-samevalue)).
:::


## parseInt e parseFloat

Conversioni numeriche come `+` o `Number()` sono rigorose. Se il valore non è esattamente un numero, falliscono:

```js
alert( +"100px" ); // NaN
```

L'unica eccezione tollerata è la presenza di spazi all'inizio o alla fine della stringa, poiché vengono ignorati.

Ma nella vita reale spesso abbiamo valori in unità, come `"100px"` o `"12pt"` in CSS. In molti stati il simbolo della valuta va dopo il saldo, quindi abbiamo `"19€"` e vorremmo estrarre un valore numerico.

Questo è il motivo per cui sono stati pensati `parseInt` e `parseFloat`.

Questi metodi "leggono" numeri dalla stringa finché ne sono in grado. In caso di errore, vengono ritornati i numeri raccolti. La funzione `parseInt` ritorna un intero, analogamente `parseFloat` ritorna un numero in virgola mobile:

```js
alert( parseInt('100px') ); // 100
alert( parseFloat('12.5em') ); // 12.5

alert( parseInt('12.3') ); // 12, viene ritornata solamente la parte intera
alert( parseFloat('12.3.4') ); // 12.3, il secondo punto interrompe la lettura
```

Ci possono essere situazioni in cui `parseInt/parseFloat` ritornano `NaN`. Questo accade quando non viene letta nessuna cifra:

```js
alert( parseInt('a123') ); // NaN, il primo simbolo interrompe la lettura
```


:::: tip Il secondo argomento di `parseInt(str, radix)`
La funzione `parseInt()` possiede un secondo parametro opzionale. Questo specifica la base del sistema numerale utilizzato, quindi `parseInt` può anche analizzare stringhe di numeri esadecimali, binari e cosi via:

```js
alert( parseInt('0xff', 16) ); // 255
alert( parseInt('ff', 16) ); // 255, senza 0x funziona ugualmente

alert( parseInt('2n9c', 36) ); // 123456
```
::::

## Altre funzioni matematiche

JavaScript ha un oggetto integrato [Math](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/Math) che contiene una piccola libreria di funzioni e costanti matematiche.

Un paio di esempi:

`Math.random()`
: Ritorna un numero casuale tra 0 e 1 (1 escluso)

    ```js
    alert( Math.random() ); // 0.1234567894322
    alert( Math.random() ); // 0.5435252343232
    alert( Math.random() ); // ... (numero casuale)
    ```

`Math.max(a, b, c...)` / `Math.min(a, b, c...)`
: Ritorna il maggiore/minore fra una lista di argomenti.

    ```js
    alert( Math.max(3, 5, -10, 0, 1) ); // 5
    alert( Math.min(1, 2) ); // 1
    ```

`Math.pow(n, power)`
: Ritorna `n` elevato alla `power`

    ```js
    alert( Math.pow(2, 10) ); // 2 alla 10 = 1024
    ```

Ci sono molte altre funzioni e costanti nell'oggetto `Math`, incluse quelle trigonometriche, che potete trovare nella [documentazione dell'oggetto Math](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/Math).


## Riepilogo

Per scrivere numeri molto grandi:

- Accodate una `"e"` con il numero di zeri. Come: `123e6` che vale `123` con 6 zeri.
- Un numero negativo dopo `"e"` divide il numero dato per 1 seguito dal numero di zeri dati. Per numeri tipo "un milionesimo".

Per diversi sistemi numerici:

- Potete scrivere direttamente in esadecimale (`0x`), ottale (`0o`) e binario (`0b`) 
- `parseInt(str, base)` analizza un numero intero con un qualsiasi sistema numerico con base: `2 ≤ base ≤ 36`.
- `num.toString(base)` converte un numero ad una stringa utilizzando il sistema numerico fornito in `base`.

Per convertire a numeri valori del tipo `12pt` e `100px`:

- Utilizzate parseInt/parseFloat per un conversione "soft", i quali provano a leggere un numero da una stringa e ritornano ciò che sono riusciti ad estrarre prima di interrompersi.

Per i numeri con la virgola:

- Arrotondate usando `Math.floor`, `Math.ceil`, `Math.trunc`, `Math.round` o `num.toFixed(precision)`.
- Ricordatevi che c'è una perdita di precisione quando operate con numeri decimali.

Altre funzioni matematiche:

- Guardate l'oggetto [Math](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/Math) in caso di necessità. La libreria non è molto ampia, ma è in grado di coprire le necessità di base.

## Esercizi

### 1 · Sommate i numeri forniti dall'utente

Create uno script che richiede due numeri all'utente (tramite prompt) e successivamente mostra la somma.

[Apri l’esempio nella fonte originale](https://it.javascript.info/number).

P.S. Fate attenzione ai tipi.

::::: details Soluzione

```js
let a = +prompt("The first number?", "");
let b = +prompt("The second number?", "");

alert( a + b );
```

Notate la somma unaria `+` prima di `prompt`. Converte immediatamente la stringa in numero.

Altrimenti `a` e `b` vengono interpretate come stringhe e la loro somma sarebbe la loro concatenazione, cioè : `"1" + "2" = "12"`.

:::::

### 2 · Perchè 6.35.toFixed(1) == 6.3?

Come da documentazione `Math.round` e `toFixed` arrotondano al numero più vicino: per difetto con decimali da `0..4`, per eccesso con decimali da `5..9`.

Ad esempio:

```js
alert( 1.35.toFixed(1) ); // 1.4
```

Un altro esempio simile, perchè `6.35` viene arrotondato a `6.3`, e non a `6.4`?

```js
alert( 6.35.toFixed(1) ); // 6.3
```

Come possiamo arrotondare correttamente `6.35`?

::::: details Soluzione

Internamente il decimale `6.35` possiede una rappresentazione binaria infinita. Come sempre in questi casi, viene memorizzato con una perdita di precisione.

Vediamo infatti:

```js
alert( 6.35.toFixed(20) ); // 6.34999999999999964473
```

La perdita di precisione può causare sia incremento che decremento del numero. In questo caso diventa leggermente più piccolo, questa è la spiegazione per cui viene arrotondato per difetto.

Mentre `1.35`?

```js
alert( 1.35.toFixed(20) ); // 1.35000000000000008882
```

In questo caso la perdita di precisione rende il numero più grande, quindi viene arrotondato per eccesso.

**Come possiamo risolvere il problema di `6.35` se vogliamo che venga arrotondato correttamente?**

Dovremmo prima avvicinarlo il più possibile ad un numero intero:

```js
alert( (6.35 * 10).toFixed(20) ); // 63.50000000000000000000
```

Notate che `63.5` non provoca perdita di precisione. Infatti la parte decimale `0.5` vale `1/2`. I decimali che sono potenze di `2` vengono rappresentati perfettamente nel sistema binario, ora possiamo quindi arrotondare il numero:


```js
alert( Math.round(6.35 * 10) / 10); // 6.35 -> 63.5 -> 64(rounded) -> 6.4
```

:::::

### 3 · Ripeti finché non viene inserito un numero

Create una funzione `readNumber` che richiede (tramite prompt) all'utente un numero, quest'azione va ripetuta finché l'utente non inserisce un numero valido.

Il valore va poi restituito come numero.

L'utente potrebbe anche interrompere il processo con una linea vuota o premendo "CANCEL". In questo caso la funzione dovrebbe ritornare `null`.

[Apri l’esempio nella fonte originale](https://it.javascript.info/number).

::::: details Soluzione

```js
function readNumber() {
  let num;

  do {
    num = prompt("Enter a number please?", 0);
  } while ( !isFinite(num) );

  if (num === null || num === '') return null;
  
  return +num;
}

alert(`Read: ${readNumber()}`);
```

La soluzione risulta essere leggermente più complessa poiché è necessario trattare i casi `null`/righa vuota.

In questo modo possiamo quindi accettare input finché non viene inserito un "numero valido". Sia `null` (cancel) sia una riga vuota soddisfano questa condizione, poiché la loro forma numerica vale `0`.

Dopo esserci fermati, abbiamo bisogno di di gestire i casi `null` e righa vuota diversamente (ritornando `null`), poiché convertirli alla forma numerica li "trasformerrebbe" in `0`.

:::::

### 4 · Un ciclo infinito occasionale

Questo è un ciclo infinito. Non terminerà mai. Perchè?

```js
let i = 0;
while (i != 10) {
  i += 0.2;
}
```

::::: details Soluzione

Questo accade perché `i` non sarà mai uguale `10`.

Eseguitelo per vedere il *vero* risultato di `i`:

```js
let i = 0;
while (i < 11) {
  i += 0.2;
  if (i > 9.8 && i < 10.2) alert( i );
}
```

Nessuno di questi sarà esattamente `10`.

Questo tipo di errori accadono a causa della perdita di precisione quando sommiamo decimali come `0.2`.

Conclusione: evitate controlli di uguaglianza quando utilizzate numeri decimali.

:::::

### 5 · Un numero random fra min e max

La funzione integrata `Math.random()` crea un valore random compreso tra `0` e `1` (`1` escluso).

Scrivete la funzione `random(min, max)` per generare un numero random in virgola mobile che va da `min` a `max` (`max` escluso).

Esempi:

```js
alert( random(1, 5) ); // 1.2345623452
alert( random(1, 5) ); // 3.7894332423
alert( random(1, 5) ); // 4.3435234525
```

::::: details Soluzione

Abbiamo bisogno di far "scorrere" 'intervallo da 0..1 a `min`.. `max`.

Questo può essere ottenuto con due passi:

1. Se moltiplichiamo un numero casuale compreso tra 0..1 per `max-min`, l'intervallo dei possibili valori cresce da `0..1` a `0..max-min`.
2. Ora se aggiungiamo `min`, il possibile intervallo si estende da `min` a `max`.

La funzione:

```js
function random(min, max) {
  return min + Math.random() * (max - min);
}

alert( random(1, 5) ); 
alert( random(1, 5) ); 
alert( random(1, 5) ); 
```

:::::

### 6 · Un intero casuale tra min e max

Create una funzione `randomInteger(min, max)` che genera un numero *intero* casuale compreso tra `min` e `max` inclusi `min` e `max`.

Qualsiasi numero nell'intervallo `min..max` deve poter apparire con la stessa probabilità.


Esempi:

```js
alert( randomInteger(1, 5) ); // 1
alert( randomInteger(1, 5) ); // 3
alert( randomInteger(1, 5) ); // 5
```

Potete utilizzare la soluzione dell'[esercizio precedente](https://it.javascript.info/task/random-min-max) come base.

::::: details Soluzione

#### La soluzione più semplice non funziona

La più semplice, ma errata soluzione genera un valore compreso tra `min` e `max` e lo arrotonda:

```js
function randomInteger(min, max) {
  let rand = min + Math.random() * (max - min); 
  return Math.round(rand);
}

alert( randomInteger(1, 3) );
```

La funzione esegue correttamente, ma il risultato è logicamente errato. La probabilità di ottenere i limiti `min` e `max` è due volte minore di qualsiasi altro numero.

Se provate ad eseguire il codice sopra molte bolte, potrete notare che `2` apparirà molto spesso.

Questo accade perché `Math.round()` genera un numero casuale nell'intervallo `1..3` e lo arrotonda:

```js
values from 1    ... to 1.4999999999  become 1
values from 1.5  ... to 2.4999999999  become 2
values from 2.5  ... to 2.9999999999  become 3
```

Ora possiamo vedere chiaramente che `1` ha due volte meno probabilità del `2`. Lo stesso vale per il `3`.

#### La soluzione corretta

Ci sono diverse soluzioni funzionanti. Una di queste consiste nell'"aggiustare" i bordi dell'intervallo. Per assicurare i casi limite, possiamo generare valori casuali compresi tra `0.5 to 3.5`, questa tecnica fornirebbe all'intero intervallo la stessa probabilità:

```js

function randomInteger(min, max) {
  // now rand is from  (min-0.5) to (max+0.5)
  let rand = min - 0.5 + Math.random() * (max - min + 1);
  return Math.round(rand);
}


alert( randomInteger(1, 3) );
```

Un modo alternativo potrebbe essere l'utilizzo di `Math.floor` su un numero casuale nell'intervallo `min` - `max+1`:

```js

function randomInteger(min, max) {
  // here rand is from min to (max+1)
  let rand = min + Math.random() * (max + 1 - min);
  return Math.floor(rand);
}


alert( randomInteger(1, 3) );
```

Ora l'intero intervallo viene considerato allo stesso modo:

```js
values from 1  ... to 1.9999999999  become 1
values from 2  ... to 2.9999999999  become 2
values from 3  ... to 3.9999999999  become 3
```

L'intero intervall ha la stessa lunghezza, rendendo la distribuzione uniforme.

:::::

