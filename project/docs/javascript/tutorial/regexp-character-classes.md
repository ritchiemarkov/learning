---
title: "Classi di caratteri"
description: "JavaScript.info in italiano: Classi di caratteri"
sourceTutorial: true
prev: {"text": "Pattern e flag", "link": "/javascript/tutorial/regexp-introduction"}
next: {"text": "Unicode: flag \"u\"", "link": "/javascript/tutorial/regexp-unicode"}
---

# Classi di caratteri

> **JavaScript.info · Ilya Kantor e contributori.** [Originale inglese](https://javascript.info/regexp-character-classes) · [Edizione italiana](https://it.javascript.info/regexp-character-classes) · [Fonti e licenza](/javascript/fonti).

Consideriamo un compito pratico -- disponiamo di un numero di telefono in questo formato `"+7(903)-123-45-67"`, e abbiamo bisogno di cambiarlo in numeri semplici: `79035419441`.

Per far ciò, possiamo trovare e rimuovere tutto ciò che non è un numero. Le classi di caratteri possono aiutarci a farlo.

Una classe di caratteri è una notazione speciale con la quale si ottengono corrispondenze per ogni simbolo che appartiene a un certo set.

Per iniziare, esploriamo la classe "cifre". È indicata con `\d`. La inseriamo nel pattern, e significa "ogni singolo numero".

Per esempio, troviamo la prima cifra del numero di telefono:

```js
let str = "+7(903)-123-45-67";

let reg = /\d/;

alert( str.match(reg) ); // 7
```

Cercando senza la flag `g`, l'espressione regolare cerca solo la prima corrispondenza, che è la prima cifra `\d`.

Aggiungiamo la flag `g` per trovare tutte le cifre:

```js
let str = "+7(903)-123-45-67";

let reg = /\d/g;

alert( str.match(reg) ); // array di corrispondenze: 7,9,0,3,1,2,3,4,5,6,7

alert( str.match(reg).join('') ); // 79035419441
```

Questa era la classe di caratteri per le cifre. Ci sono anche altre classi di caratteri.

Le più usate sono:

`\d` ("d" è l'iniziale di "digit", cioè cifra)
: Una cifra: un carattere da `0` a `9`.

`\s` ("s" è l'iniziale di "space", spazio)
: Un simbolo di spazio: include spazi, tab, andate a capo.

`\w` ("w" è l'iniziale di "word", parola)
: Un carattere "per formare parole": può essere una lettera dell'alfabeto Inglese o una cifra o un underscore `_` . Lettere non latine (che appartengono ad esempio al cirillico o all'hindi) non fanno parte di `\w`.

Ad esempio, `\d\s\w` vuol dire una "cifra" seguita da un "carattere di spazio" seguita da "un carattere per formare parole", come `"1 a"`.

**Una regexp potrebbe contenere sia simboli regolari sia classi di caratteri.**

Per esempio, `CSS\d` cerca corrispondenze per la stringa `CSS` seguita da una cifra:

```js
let str = "CSS4 è cool";
let reg = /CSS\d/

alert( str.match(reg) ); // CSS4
```

Possiamo anche usare più classi di caratteri:

```js
alert( "I love HTML5!".match(/\s\w\w\w\w\d/) ); // ' HTML5'
```

La corrispondenza (a ogni classe di caratteri  corrisponde un carattere risultante):

![](/javascript-info/9-regular-expressions/02-regexp-character-classes/love-html5-classes.svg)

## Confine di parola: \b

Un confine di parola (word boundary) `\b` è una particolare classe di caratteri.

Non denota un carattere, ma piuttosto un confine tra caratteri.

Ad esempio, `\bJava\b` trova `Java` nella stringa `Hello, Java!`, ma non nella stringa `Hello, JavaScript!`.

```js
alert( "Hello, Java!".match(/\bJava\b/) ); // Java
alert( "Hello, JavaScript!".match(/\bJava\b/) ); // null
```

Il confine ha "larghezza zero" nel senso che solitamente utilizzare una classe di caratteri significa ottenere un carattere nel risultato (come una lettera o un numero), ma non in questo caso.

Il boundary è un test.

Quando il motore delle espressioni regolari sta effettuando la ricerca, si sposta sulla stringa nel tentativo di trovare una corrispondenza. In ogni posizione della stringa esso prova a trovare il pattern.

Quando il pattern contiene `\b`, testa che la posizione nella stringa sia un "confine di parola", cioè si verifica una di queste tre condizioni:

- Tra due caratteri della stringa, dove uno è un carattere appartenente a una parola `\w` e l'altro non lo è.
- All'inizio della stringa, se il primo carattere della stringa è un carattere appartenente a una parola `\w`.
- Alla fine della stringa, se l'ultimo carattere della stringa è un carattere appartenente a una parola `\w`.

Per esempio, nella stringa `Hello, Java!` le seguenti posizioni corrispondono a `\b`:

![](https://it.javascript.info/hello-java-boundaries.svg)

Quindi trova `\bHello\b`, perché:

1. All'inizio della stringa il primo test `\b` ha corrispondenza positiva.
2. Successivamente la parola `Hello` corrisponde.
3. Infine `\b` corrisponde, dato che siamo tra `o` e uno spazio.

Anche il pattern `\bJava\b` corrisponde, ma non `\bHell\b` (perché non c'è il confine di parola dopo `l`) e non `Java!\b` (perché il punto esclamativo non è un carattere appartenente a una parola `\w`, quindi non c'è il confine di parola dopo di lui).


```js
alert( "Hello, Java!".match(/\bHello\b/) ); // Hello
alert( "Hello, Java!".match(/\bJava\b/) );  // Java
alert( "Hello, Java!".match(/\bHell\b/) );  // null (no match)
alert( "Hello, Java!".match(/\bJava!\b/) ); // null (no match)
```

Ancora una volta teniamo conto del fatto che  `\b` fa cercare corrispondenze per il confine di parola al motore, affinché `Java\b` trovi `Java` soltanto quando seguito da un confine di parola.

Solitamente usiamo `\b` per trovare singole parole. Quindi se noi vogliamo che il risultato sia il linguaggio `"Java"`, allora `\bJava\b` troverà corrispondenze per quella esatta parola isolata, e le ignorerà se facente parte di un'altra parola, quindi ad esempio non troverà corrispondenze per `Java` in `JavaScript`.

Un altro esempio: una regexp `\b\d\d\b` cerca numeri isolati composti da due cifre. In altre parole, richiede che prima e dopo del pattern  `\d\d` vi sia un simbolo diverso da `\w` (all'inizio o alla fine della stringa).

```js
alert( "1 23 456 78".match(/\b\d\d\b/g) ); // 23,78
```


::: warning Il confine di parola non funziona con alfabeti non Latini
Il controllo per il confine di parola `\b` verifica la presenza di un confine tra `\w` e qualcos'altro. Ma `\w` può essere una lettera (o numero o underscore), quindi il test non funzionerà per altri caratteri (come il Cirillico o i Geroglifici).

In un secondo momento raggiungeremo le classi di caratteri Unicode che permettono di risolvere task simili per lingue diverse.
:::


## Classi inverse

Per ogni classe di caratteri ne esiste una "classe inversa", indicata con la stessa lettera, ma maiuscola.

L'"inversa" vuol dire che trova corrispondenza per tutti gli altri caratteri, ad esempio:

`\D`
: Non una cifra: qualsiasi carattere eccetto `\d`, ad esempio una lettera.

`\S`
: Non uno spazio: qualsiasi carattere eccetto `\s`, ad esempio una lettera.

`\W`
: Un carattere che non appartenga a una parola: tutto tranne `\w`.

`\B`
: Non-boundary: un test inverso a quello del confine di parola `\b`.

All'inizio del capitolo abbiamo visto come ottenere tutte le cifre che compongono il numero  `+7(903)-123-45-67`.

Un modo era trovare tutte le singole cifre e poi unirle:

```js
let str = "+7(903)-123-45-67";

alert( str.match(/\d/g).join('') ); // 79031234567
```

Un modo alternativo e più breve è quello di trovare tutti i caratteri che non sono numerici `\D` e rimuoverli dalla stringa:


```js
let str = "+7(903)-123-45-67";

alert( str.replace(/\D/g, "") ); // 79031234567
```

## Gli spazi sono caratteri regolari

Di solito prestiamo poca attenzione agli spazi. Per noi le stringhe `1-5` e `1 - 5` sono quasi identiche.

Ma se una regexp non tiene conto degli spazi, potrebbe non funzionare.

Proviamo a trovare cifre separate da un trattino:

```js
alert( "1 - 5".match(/\d-\d/) ); // null, nessuna corrispondenza!
```

Qui sistemiamo le cose aggiungendo gli spazi nella regexp `\d - \d`:

```js
alert( "1 - 5".match(/\d - \d/) ); // 1 - 5, ora funziona
```

**Uno spazio è un carattere. Ha la stessa importanza di ogni altro carattere.**

Ovviamente, gli spazi in una regexp sono necessari solo se li stiamo cercando. Spazi extra (così come qualsiasi altro carattere in eccesso) possono impedire di trovare una corrispondenza:

```js
alert( "1-5".match(/\d - \d/) ); // null, perchè la stringa 1-5 non ha spazi
```

In altre parole, in una espressione regolare tutti i caratteri hanno importanza, compresi gli spazi.

## Un punto rappresenta qualsiasi carattere

Il punto `"."` è una speciale classe di caratteri che trova corrispondenze per "qualsiasi carattere eccetto un'andata a capo".

Per esempio:

```js
alert( "Z".match(/./) ); // Z
```

Oppure nel mezzo di una regexp:

```js
let reg = /CS.4/;

alert( "CSS4".match(reg) ); // CSS4
alert( "CS-4".match(reg) ); // CS-4
alert( "CS 4".match(reg) ); // CS 4 (anche lo spazio è un carattere)
```

Va notato che il punto rappresenta "qualunque carattere" ma non "l'assenza di un carattere". Deve esserci un carattere affinché una corrispondenza venga trovata:

```js
alert( "CS4".match(/CS.4/) ); // null, nessuna corrispondenza perché non c'è carattere tra S e 4
```

### La flag dotall "s"

Di solito un punto non corrisponde a un carattere di andata a capo.

Per esempio, `A.B` trova `A`, e successivamente `B` con qualsiasi carattere si trovi tra di loro, eccetto un'andata a capo.

Questo non corrisponde:

```js
alert( "A\nB".match(/A.B/) ); // null (nessuna corrispondenza)

// un carattere di spazio corrisponderebbe, o una lettera, ma non \n
```

A volte ciò è un inconveniente, perché magari stiamo cercando letteralmente "qualunque carattere", andata a capo inclusa.

Questo è ciò che fa la flag `s`. Se una regexp ce l'ha, allora il punto `"."` corrisponderà letteralmente a qualunque carattere:

```js
alert( "A\nB".match(/A.B/s) ); // A\nB (corrispondenza!)
```

## Riepilogo

Esistono le seguenti classi di caratteri:

- `\d` -- cifre.
- `\D` -- non cifre.
- `\s` -- simboli di spazio, tab, andate a capo.
- `\S` -- tutto tranne `\s`.
- `\w` -- lettere, numeri, underscore `'_'`.
- `\W` -- tutto tranne `\w`.
- `.` -- qualsiasi carattere se abbiamo la flag `'s'`, altrimenti qualsiasi carattere eccetto un'andata a capo.

...Ma non è tutto!

La codifica Unicode, usata da JavaScript per le stringhe, fornisce molte proprietà per i caratteri, come: a quale linguaggio appartiene la lettera (se è una lettera), se è un simbolo d'interpunzione, ecc.

L'attuale JavaScript consente di usare queste proprietà nelle regexp per cercare i caratteri, ad esempio:

- Una lettera cirillica è: `\p{Script=Cyrillic}` o `\p{sc=Cyrillic}`.
- Un trattino (che sia più corto `-` o più lungo `—`): `\p{Dash_Punctuation}` o `\p{pd}`.
- Un simbolo di una valuta, come `$`, `€` o un altro: `\p{Currency_Symbol}` o `\p{sc}`.
- ...E molto di più. Unicode ha molte categorie di caratteri tra cui possiamo scegliere.

Questi pattern necessitano della flag `'u'` per funzionare. Maggiori dettagli nel capitolo [](/javascript/tutorial/regexp-unicode).
