---
title: "Modo multilinea, flag \"m\""
description: "JavaScript.info in italiano: Modo multilinea, flag \"m\""
sourceTutorial: true
prev: {"text": "Inizio stringa ^ e fine $", "link": "/javascript/tutorial/regexp-anchors"}
next: {"text": "Confine di parola: \\b", "link": "/javascript/tutorial/regexp-boundary"}
---

# Modo multilinea, flag "m"

> **JavaScript.info · Ilya Kantor e contributori.** [Originale inglese](https://javascript.info/regexp-multiline-mode) · [Edizione italiana](https://it.javascript.info/regexp-multiline-mode) · [Fonti e licenza](/javascript/fonti).

Il modo multilinea si abilita col flag `/.../m`.

Esso modifica il comportamento dei soli `^` e `$`.

In modalità multilinea essi non trovano corrispondenza solo con l'inizio e la fine della stringa ma anche con gli inizi e fine di linea.

## Inizio linea ^

Nell'esempio sotto riportato il testo è distribuito su più linee. Il pattern `/^\d+/gm` prende un numero dall'inizio di ogni riga:

```js
let str = `1o posto: Winnie
2o posto: Piglet
33o posto: Eeyore`;


alert( str.match(/^\d+/gm) ); // 1, 2, 33

```

Il motore di regex si sposta sul testo alla ricerca di un inizio riga `^`, quando lo trova -- continua a trovare la corrispondenza col resto del pattern `\d+`.
Mentre senza il flag  `/.../m` troverebbe corrispondenza solo col primo numero:

```js
let str = `1o posto: Winnie
2o posto: Piglet
33o posto: Eeyore`;


alert( str.match(/^\d+/g) ); // 1

```

Questo accade perché il comportamento default del caret `^` trova corrispondenza solo con l'inizio del testo, mentre in modalità multilinea trova all'inizio di ogni riga.


::: tip Da sapere
"Inizio di linea" formalmente significa "immediatamente dopo un'interruzione di linea": il test `^` in modalità multilinea trova tutte le posizioni precedute dal carattere di nuova linea `\n`.

And at the text start.
:::

## Fine linea $

Il simbolo di dollaro `$` si comporta in modo simile.

L'espressione regolare `\w+$` trova l'ultima parola in ogni stringa.

```js
let str = `1o posto: Winnie
2o posto: Piglet
33o posto: Eeyore`;

alert( str.match(/\w+$/gim) ); // Winnie,Piglet,Eeyore
```

Senza il flag `/.../m` il dollaro `$` troverebbe corrispondenza solo con la fine dell'intera stringa, dunque risulterebbe solo l'ultima parola dell'intero testo.

## Ancore ^$ rispetto \n (a-capo)

Per trovare un fine linea è possibile usare non solo `^` e `$`, ma anche il carattere a-capo `\n`.

La prima differenza è che, contrariamente alle ancore, il carattere `\n` "consuma" il carattere a-capo aggiungendolo al risultato.

Ad esempio qui lo usiamo al posto di `$`:

```js
let str = `1o posto: Winnie
2o posto: Piglet
33o posto: Eeyore`;
alert( str.match(/\w+\n/gim) ); // Winnie\n,Piglet\n
```

Qui ogni corrispondenza è una parola più il carattere a-capo.

Un'altra differenza -- l' a-capo `\n` non trova corrispondenza a fine stringa. Questo è il motivo per cui `Eeyore` non è trovato nell'esempio sopra.

Pertanto le ancore sono migliori: sono più vicine a ciò che si vuole estrarre.
