---
title: "Confine di parola: \\b"
description: "JavaScript.info in italiano: Confine di parola: \\b"
sourceTutorial: true
prev: {"text": "Modo multilinea, flag \"m\"", "link": "/javascript/tutorial/regexp-multiline-mode"}
next: {"text": "Escaping, caratteri speciali", "link": "/javascript/tutorial/regexp-escaping"}
---

# Confine di parola: \b

> **JavaScript.info · Ilya Kantor e contributori.** [Originale inglese](https://javascript.info/regexp-boundary) · [Edizione italiana](https://it.javascript.info/regexp-boundary) · [Fonti e licenza](/javascript/fonti).

Il confine di parola `\b` è un test, proprio come `^` e `$`.

Quando l'interprete delle regexp (il modulo software che cerca all'interno delle espressioni regolari) incontra `\b`, verifica se la posizione nella stringa sia un confine di parola.

Ci sono tre differenti posizioni che qualificano il confine di parola:

- Ad inizio stringa, se il primo carattere di essa è un carattere di parola `\w`.
- Tra due caratteri di una stringa, laddove il primo sia un carattere di parola `\w` e l'altro no.
- A fine stringa, se l'ultimo carattere è un carattere di parola `\w`.

Ad esempio, la regexp `\bJava\b` troverà corrispondenza in `Hello, Java!`, dove `Java` è una parola a sé, ma non troverà alcuna corrispondenza in `Hello, JavaScript!`.

```js
alert( "Hello, Java!".match(/\bJava\b/) ); // Java
alert( "Hello, JavaScript!".match(/\bJava\b/) ); // null
```

Nella stringa `Hello, Java!` trovano riscontro in `\b` le seguenti posizioni:

![](/javascript-info/9-regular-expressions/06-regexp-boundary/hello-java-boundaries.svg)

Pertanto la corrispondenza con il pattern `\bHello\b` viene trovata perché:

1. All'inizio della stringa trova riscontro con il primo test `\b`.
2. Successivamente identifica la parola `Hello`.
3. Infine trova ancora corrispondenza con il test `\b`, dal momento che la posizione corrente è tra una `o` e una virgola.

Viene quindi individuato il pattern `\bHello\b`, ma non `\bHell\b` (perché non c'è un confine di parola dopo la `l`) e non `Java!\b` (perché il punto esclamativo non è un carattere di parola `\w`, quindi non c'è confine di parola dopo di esso).

```js
alert( "Hello, Java!".match(/\bHello\b/) ); // Hello
alert( "Hello, Java!".match(/\bJava\b/) );  // Java
alert( "Hello, Java!".match(/\bHell\b/) );  // null (nessuna corrispondenza)
alert( "Hello, Java!".match(/\bJava!\b/) ); // null (nessuna corrispondenza)
```

Possiamo usare `\b` anche con i numeri non solo con le parole.

Il pattern `\b\d\d\b`, ad esempio, cerca due caratteri numerici a sé stanti. In altre parole, cerca un numero di due cifre delimitato da caratteri differenti da `\w`, come spazi o punteggiatura (o l'inizio/la fine della stringa).

```js
alert( "1 23 456 78".match(/\b\d\d\b/g) ); // 23,78
alert( "12,34,56".match(/\b\d\d\b/g) ); // 12,34,56
```


::: warning Il confine di parola `pattern:\b` funziona solo con l'alfabeto latino
Il test di confine parola `\b` controlla che ci sia `\w` da un lato della posizione e che non ci sia `\w` dall'altro lato.

Ma `\w` significa una lettera dell'alfabeto latino `a-z` (o un numero o un underscore), pertanto il test non è efficace per altri caratteri, es. caratteri cirillici o simboli grafici.
:::

## Esercizi

### 1 · Trovate l'orario

L'orario ha il formato: `ore:minuti`. Sia ore sia minuti sono formati da due cifre, come `09:00`.

Create una regexp per trovare l'orario nella stringa: `Breakfast at 09:00 in the room 123:456.`

P.S. In questo esercizio non c'è bisogno di controllare la correttezza dell'orario, quindi `25:99` è considerato un risultato valido.
P.P.S. La regexp non dovrebbe restituire `123:456`.

::::: details Soluzione

Risposta: `\b\d\d:\d\d\b`.

```js
alert( "Colazione alle 09:00 nella stanza 123:456.".match( /\b\d\d:\d\d\b/ ) ); // 09:00
```

:::::

