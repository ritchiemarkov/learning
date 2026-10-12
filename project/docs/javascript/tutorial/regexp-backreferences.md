---
title: "Riferimenti all'indietro (backreference) nei pattern: \\N e \\kname"
description: "JavaScript.info in italiano: Riferimenti all'indietro (backreference) nei pattern: \\N e \\kname"
sourceTutorial: true
prev: {"text": "I gruppi di acquisizione (capturing group)", "link": "/javascript/tutorial/regexp-groups"}
next: {"text": "Alternanza (OR) |", "link": "/javascript/tutorial/regexp-alternation"}
---

# Riferimenti all'indietro (backreference) nei pattern: \N e \k<name>

> **JavaScript.info · Ilya Kantor e contributori.** [Originale inglese](https://javascript.info/regexp-backreferences) · [Edizione italiana](https://it.javascript.info/regexp-backreferences) · [Fonti e licenza](/javascript/fonti).

Possiamo usare il contenuto dei gruppi di acquisizione `(...)` non soltanto nel risultato o nella stringa di sostituzione, ma anche all'interno del pattern stesso.

## Riferimento all'indietro per numero: \N

Ci si può riferire ad un gruppo nel pattern usando `\N`, in cui `N` indica il numero del gruppo.

Per comprendere chiaramente perché sia utile, consideriamo l'esercitazione seguente.

Dobbiamo trovare le stringhe tra apici: sia quelli singoli `'...'` sia quelli doppi `"..."`, entrambi devono dare luogo a riscontro.

Come trovarli?

Potremmo mettere i due tipi di apici all'interno di parentesi quadre: `['"](https://it.javascript.info/*?)['"]`, ma in questo modo troveremmo anche le stringhe con apici misti come `"...'` e `'..."`. Questo porterebbe a risultati inesatti quando un tipo di apice compare tra due dell'altro tipo, come nella stringa `"She's the one!"`:

```js
let str = `He said: "She's the one!".`;

let regexp = /['"](.*?)['"]/g;

// Il risultato non è quello che vorremmo
alert( str.match(regexp) ); // "She'
```

Come possiamo osservare, il pattern ha trovato un apice di apertura `"`, quindi il testo fino al successivo apice `'` che chiude la corrispondenza.

Per accertarci che il pattern trovi l'apice di chiusura uguale a quello di apertura, possiamo racchiuderlo in un gruppo di acquisizione e fare riferimento ad esso: `(['"])(.*?)\1`.

Ecco il codice corretto:

```js
let str = `He said: "She's the one!".`;


let regexp = /(['"])(.*?)\1/g;


alert( str.match(regexp) ); // "She's the one!"
```

Ora funziona! L'interprete dell'espressione regolare trova il primo apice `(['"])` e lo memorizza. Questo è il primo gruppo di acquisizione.

Più avanti nel pattern `\1` significa "trova lo stesso testo del primo gruppo", nel nostro caso esattamente lo stesso apice.

Similmente `\2` indicherebbe il contenuto del secondo gruppo, `\3` quello del terzo gruppo, e così via.


::: tip Da sapere
Se nel gruppo usiamo `?:` non sarà possibile riferirsi ad esso. I gruppi esclusi dall'acquisizione `(?:...)` non sono memorizzati dall'interprete.
:::


::: warning Non fare confusione: nel pattern `pattern:\1`, nelle sostituzioni `pattern:$1`
Nelle sostituzioni di stringa si adopera il segno di dollaro: `$1`, mentre nel contesto di un pattern il backslash `\1`.
:::

## Riferimento all'indietro per nome: `\k<name>`

Se un'espressione regolare ha tante parentesi, è opportuno dare loro dei nomi.

Per riferirsi ad un gruppo nominato si usa `\k<name>`.

Nell'esempio sotto il gruppo con gli apici è nominato `?<quote>`, pertanto il riferimento è `\k<quote>`:

```js
let str = `He said: "She's the one!".`;


let regexp = /(?<quote>['"])(.*?)\k<quote>/g;


alert( str.match(regexp) ); // "She's the one!"
```
