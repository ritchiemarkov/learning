---
title: "Insiemi e intervalli [...]"
description: "JavaScript.info in italiano: Insiemi e intervalli [...]"
sourceTutorial: true
prev: {"text": "Escaping, caratteri speciali", "link": "/javascript/tutorial/regexp-escaping"}
next: {"text": "Quantificatori +, *, ? and", "link": "/javascript/tutorial/regexp-quantifiers"}
---

# Insiemi e intervalli [...]

> **JavaScript.info · Ilya Kantor e contributori.** [Originale inglese](https://javascript.info/regexp-character-sets-and-ranges) · [Edizione italiana](https://it.javascript.info/regexp-character-sets-and-ranges) · [Fonti e licenza](/javascript/fonti).

Alcuni caratteri o classi di caratteri inseriti all'interno di parantesi quadre `[…]` significano "cerca qualsiasi carattere tra quelli forniti".

## Insiemi

Per esempio, `[eao]` significa uno qualunque dei 3 caratteri: `'a'`, `'e'`, od `'o'`.

Questo è chiamato un *insieme* o *set*. I set posso essere usati in una regexp insieme ad altri caratteri:

```js
// trova [t o m], e quindi "op"
alert( "Mop top".match(/[tm]op/gi) ); // "Mop", "top"
```

Si noti che sebbene ci siano più caratteri nel set, questi corrispondano esattamente a un carattere nel match.

Quindi il seguente esempio non dà alcuna corrispondenza:

```js
// trova "V", poi ['o' o 'i'], quindi "la"
alert( "Voila".match(/V[oi]la/) ); // null, nessuna corrispondenza
```

Il modello di ricerca risulta quindi:

- `V`,
- poi *una* di queste lettere `[oi]`,
- quindi `la`.

Significa che ci dovrebbe essere una corrispondenza per `Vola` o `Vila`.

## Intervalli

Le parentesi quadre possono contenere anche *intervalli di caratteri*.

Per esempio, `[a-z]` indica un carattere nell'intervallo che va da `a` a `z`, e `[0-5]` indica un numero tra `0` e `5`.

Nell'esempio seguente cercheremo una `"x"` seguita da due numeri o lettere da `A` a `F`:

```js
alert( "Exception 0xAF".match(/x[0-9A-F][0-9A-F]/g) ); // xAF
```

Il modello `[0-9A-F]` ha due intervalli: cerca un carattere che sia una cifra da `0` a `9` o una lettera da `A` a `F`.

Se volessimo cercare anche lettere minuscole, possiamo aggiungere l'intervallo `a-f`: `[0-9A-Fa-f]`, o aggiungere il flag `i`.

Possiamo anche usare classi di caratteri dentro `[…]`.

Per esempio, se volessimo cercare un carattere di parola `\w` o un trattino `-`, allora l'insieme sarà `[\w-]`.

È anche possibile combinare diverse classi, es `[\s\d]` significa "uno spazio o un numero".


::: tip Le classi di caratteri sono abbreviazioni per determinati set di caratteri
Per esempio:

- **\d** -- è la stessa cosa di `[0-9]`,
- **\w** -- è la stessa cosa di `[a-zA-Z0-9_]`,
- **\s** -- è la stessa cosa di `[\t\n\v\f\r ]` e pochi altri rari caratteri Unicode.
:::

### Esempio: multi lingua \w

Dal momento che la classe di caratteri `\w` è una scorciatoia per `[a-zA-Z0-9_]`, non può trovare geroglifici cinesi, lettere cirilliche, ecc.

Possiamo allora scrivere un modello più universale, che cerca un carattere di parola in qualunque lingua. Questo è reso facile dalle proprietà Unicode: `[\p{Alpha}\p{M}\p{Nd}\p{Pc}\p{Join_C}]`.

Decifriamolo. Similarmente a `\w`, stiamo creando un nostro insieme che include i caratteri con le seguenti proprietà Unicode:

- `Alphabetic` (`Alpha`) - per le lettere,
- `Mark` (`M`) - per gli accenti,
- `Decimal_Number` (`Nd`) - per i numeri,
- `Connector_Punctuation` (`Pc`) - per il trattino basso `'_'` e caratteri simili,
- `Join_Control` (`Join_C`) - due codici speciali `200c` e `200d`, usati nelle legature, a.e. in Arabo.

Un esempio di utilizzo:

```js
let regexp = /[\p{Alpha}\p{M}\p{Nd}\p{Pc}\p{Join_C}]/gu;

let str = `Hi 你好 12`;

// Trova tutte le lettere e i numeri:
alert( str.match(regexp) ); // H,i,你,好,1,2
```

Naturalmente possiamo modificare questo modello: aggiungere proprietà Unicode o rimuoverle. Le proprietà Unicode sono descritte meglio nell'articolo [Unicode: flag "u"](/javascript/tutorial/regexp-unicode).


::: warning Le proprietà Unicode non sono supportate da IE
Le proprietà Unicode `p{…}` non sono implementate in IE. Se ne abbiamo davvero bisogno possiamo utilizzare la libreria [XRegExp](http://xregexp.com/).

In alternativa possiamo utilizzare soltanto un intervallo di caratteri nella lingua che ci interessa, a.e.  `[а-я]` per le lettere cirilliche.
:::

## Esclusione di intervalli

Oltre ai normali intervalli, è possibile creare dei modelli di "esclusione", come `[^…]`.

Sono contraddistinti da un accento circonflesso `^` all'inizio e trovano corrispondenza in qualunque carattere *tranne quelli indicati*.

Per esempio:

- `[^aeyo]` -- qualunque carattere tranne  `'a'`, `'e'`, `'y'` o `'o'`.
- `[^0-9]` -- qualunque carattere tranne un numero, come `\D`.
- `[^\s]` -- qualunque carattere che non sia uno spazio, come `\S`.

L'esempio seguente cerca qualunque carattere eccetto lettere, numeri e spazi:

```js
alert( "alice15@gmail.com".match(/[^\d\sA-Z]/gi) ); // @ e .
```

## L'escape dentro […]

In genere quando vogliamo trovare esattamente un carattere speciale, dobbiamo effettuarne l'escape: `\.`. Se abbiamo bisogno di un backslash, allora dobbiamo usare `\\`, e così via.

Dentro le parentesi quadre, possiamo usare la stragrande maggioranza di caratteri speciali senza la necessità di effettuarne l'escape:

- I simboli `. + ( )` non necessitano mai di escaping.
- Il trattino `-` non è preceduto da caratteri di escape all'inizio o alla fine (dove non definisce un intervallo).
- Un accento circonflesso `^` è soggetto ad escape solo all'inizio (dove significa esclusione).
- La parentesi quadra di chiusura `]` dev'essere sempre soggetta ad escape (se abbiamo bisogno di cercare questo simbolo).

In altre parole, tutti i caratteri speciali sono consentiti senza necessità di escape, eccetto quando significano qualcosa all'interno delle parentesi quadre.

Un punto `.` all'interno delle parentesi quadre significa soltanto un punto. Il modello `[.,]` cercherebbe uno dei caratteri: o un punto o una virgola.

Nell'esempio seguente la regexp `[-().^+]` effettua la ricerca per uno dei caratteri `-().^+`:

```js
// Non necessita di escape
let regexp = /[-().^+]/g;

alert( "1 + 2 - 3".match(regexp) ); // Corrispondono +, -
```

...Ma se decidete di effettuare l'escape "per ogni evenienza", il risultato non cambierebbe:

```js
// Escape di ogni carattere
let regexp = /[\-\(\)\.\^\+]/g;

alert( "1 + 2 - 3".match(regexp) ); // funziona ugualmente: +, -
```

## Intervalli e flag "u"

Se ci sono coppie surrogate nel set, il flag `u` è necessario affinché la ricerca funzioni correttamente.

Per esempio, cerchiamo `[𝒳𝒴]` nella stringa `𝒳`:

```js
alert( '𝒳'.match(/[𝒳𝒴]/) ); // mostra uno strano carattere, come [?]
// (la ricerca è stata eseguita in modo errato, viene restituito mezzo-carattere)
```

Il risultato non è corretto, perché di base le espressioni regolari "non sanno nulla" riguardo le coppie surrogate.

Il motore delle espressioni regolari pensa che `[𝒳𝒴]` -- non sono due, ma quattro caratteri:
1. metà alla sinistra di `𝒳` `(1)`,
2. metà alla destra di `𝒳` `(2)`,
3. metà alla sinistra di `𝒴` `(3)`,
4. metà alla destra di `𝒴` `(4)`.

Possiamo vedere il suo codice in questo modo:

```js
for(let i=0; i<'𝒳𝒴'.length; i++) {
  alert('𝒳𝒴'.charCodeAt(i)); // 55349, 56499, 55349, 56500
};
```

Quini, l'esempio qui sopra trova e visualizza la metà alla sinistra di `𝒳`.

Se aggiungiamo il flag `u`, allora il comportamento sarà corretto:

```js
alert( '𝒳'.match(/[𝒳𝒴]/u) ); // 𝒳
```

Una situazione simile si verifica quando si cerca un intervallo, come `[𝒳-𝒴]`.

Se dimentichiamo di aggiungere il flag `u`, ci sarà un errore:

```js
'𝒳'.match(/[𝒳-𝒴]/); // Errore: Invalid regular expression
```

La ragione è che senza il flag `u` le coppie surrogate sono percepite come due caratteri, quindi `[𝒳-𝒴]` è interpretato come `[<55349><56499>-<55349><56500>]` (ogni coppia surrogata è sostituita con i suoi codici). Ora è facile osservare che l'intervallo `56499-55349` non è valido: il suo codice iniziale `56499` è maggiore di quello finale `55349`. Questa è la ragione formale dell'errore.

Con il flag `u` il modello funziona correttamente:

```js
// cerca i caratteri da 𝒳 a 𝒵
alert( '𝒴'.match(/[𝒳-𝒵]/u) ); // 𝒴
```

## Esercizi

### 1 · Java[^script]

Abbiamo una regexp `/Java[^script]/`.

Cosa corrisponde nella stringa `Java`? E nella stringa `JavaScript`?

::::: details Soluzione

Risposte: **no, sì**.

- Nello script `Java` non c'è corrispondenza, dato che per `[^script]` si intende "qualunque carattere eccetto quelli dati". Quindi la regexp cerca `"Java"` seguito da uno di tali caratteri, ma c'è la fine della stringa, non ci sono caratteri dopo di esso.

    ```js
    alert( "Java".match(/Java[^script]/) ); // null
    ```
- Sì, poiché `[^script]` trova il carattere `"S"` che non è uno di `script`. Considerato che la regexp fa distinzione tra maiuscole e minuscole (non c'è il flag `i`), tratta `"S"` come un carattere differente da `"s"`.

    ```js
    alert( "JavaScript".match(/Java[^script]/) ); // "JavaS"
    ```

:::::

### 2 · Trova l'orario come hh:mm o hh-mm

L'orario può essere nel formato `ore:minuti` o `ore-minuti`. Entrambi, ore e minuti, hanno 2 numeri:  `09:00` o `21-30`.

Scrivete una regexp per trovare l'orario:

```js
let regexp = /your regexp/g;
alert( "Breakfast at 09:00. Dinner at 21-30".match(regexp) ); // 09:00, 21-30
```

P.S. In questo esercizio considereremo che l'orario è sempre corretto, non c'è necessità di filtrare stringhe come "45:67". Più tardi ci occuperemo anche di questo tipo di problema.

::::: details Soluzione

Risposta: `\d\d[-:]\d\d`.

```js
let regexp = /\d\d[-:]\d\d/g;
alert( "Breakfast at 09:00. Dinner at 21-30".match(regexp) ); // 09:00, 21-30
```

Fate attenzione al fatto che il trattino `'-'` ha un significato speciale tra le parentesi quadre, ma solo tra gli altri caratteri, non quando è all'inizio o alla fine, quindi non c'è bisogno dell'escape.

:::::

