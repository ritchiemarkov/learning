---
title: "Inizio stringa ^ e fine $"
description: "JavaScript.info in italiano: Inizio stringa ^ e fine $"
sourceTutorial: true
prev: {"text": "Unicode: flag \"u\"", "link": "/javascript/tutorial/regexp-unicode"}
next: {"text": "Modo multilinea, flag \"m\"", "link": "/javascript/tutorial/regexp-multiline-mode"}
---

# Inizio stringa ^ e fine $

> **JavaScript.info · Ilya Kantor e contributori.** [Originale inglese](https://javascript.info/regexp-anchors) · [Edizione italiana](https://it.javascript.info/regexp-anchors) · [Fonti e licenza](/javascript/fonti).

L'accento circonflesso  `'^'` e il simbolo del dollaro `'$'` sono caratteri che hanno un significato speciale nelle regexp. Vengono chiamati "ancoraggi" (anchor).

Il simbolo `^` trova corrispondenza all'inizio del testo, e il dollaro `$` la trova alla fine del testo.

Per esempio, vediamo se il testo inizia con `Mary`:

```js
let str1 = "Mary had a little lamb, it's fleece was white as snow";
let str2 = 'Everywhere Mary went, the lamp was sure to go';

alert( /^Mary/.test(str1) ); // true
alert( /^Mary/.test(str2) ); // false
```

Il pattern `^Mary` vuol dire: "la stringa inizia e subito dopo c'è Mary".

Ora verifichiamo se il testo finisce con una email.

Per trovare corrispondenza con un'email, possiamo usare la regexp `[-.\w]+@([\w-]+\.)+[\w-]{2,20}`.

Per testare se la stringa finisca con una email, aggiungiamo `$` al pattern:

```js
let reg = /[-.\w]+@([\w-]+\.)+[\w-]{2,20}$/g;

let str1 = 'My email is mail@site.com';
let str2 = 'Everywhere Mary went, the lamp was sure to go';

alert( reg.test(str1) ); // true
alert( reg.test(str2) ); // false
```

Possiamo utilizzare entrambi gli ancoraggi insieme per controllare che la stringa segua uno specifico pattern. È un metodo usato spesso per la validazione.

Per esempio vogliamo controllare che  `str` sia esattamente un colore nella forma `#` più 6 esadecimali. Il pattern per il colore è `#[0-9a-f]{6}`.

Per verificare che l'*intera stringa* vi corrisponda in modo esatto, aggiungiamo `^...$`:

```js
let str = "#abcdef";

alert( /^#[0-9a-f]{6}$/i.test(str) ); // true
```

Il motore delle regexp cerca l'inizio del testo, successivamente il colore, e infine cerca immediatamente la fine del testo. Proprio ciò di cui abbiamo bisogno.


::: tip Gli ancoraggi hanno lunghezza zero
Gli ancoraggi, proprio come `\b`, sono test. Hanno larghezza zero.

In altre parole, non cercano corrispondenze per un carattere, piuttosto forzano il motore delle regexp a cercare la condizione specifica (inizio/fine del testo).
:::

Il comportamento degli ancoraggi cambia se c'è la flag `m` (modalità multi linea). L'approfondiremo meglio nel prossimo capitolo.

## Esercizi

### 1 · Regexp ^$

Quale stringa corrisponde al pattern `^$`?

::::: details Soluzione

L'unica corrispondenza si ha con la stringa vuota: inizia e poi finisce immediatamente.

Questo task dimostra ancora che gli ancoraggi non rappresentano caratteri, bensì test.

La stringa è vuota `""`. Il motore prima fa cerca corrispondenze per `^` (inizio input), ed è presente, e subito dopo cerca la fine `$`, e c'è anch'essa. Quindi c'è corrispondenza.

:::::

