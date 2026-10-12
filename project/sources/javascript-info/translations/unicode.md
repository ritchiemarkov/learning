# Unicode e rappresentazione delle stringhe

```warn header="Approfondimento"
Questo capitolo entra nei dettagli delle stringhe. È utile quando lavori con emoji, caratteri matematici, ideogrammi e altri simboli meno comuni. Puoi affrontarlo dopo le basi.
```

Le stringhe JavaScript usano Unicode. Occorre distinguere il punto di codice Unicode dalla sua rappresentazione: nelle operazioni sulle stringhe JavaScript conta spesso il numero di unità di codice UTF-16, non il numero di caratteri visibili.

Possiamo inserire un carattere tramite il suo codice esadecimale in tre modi:

- `\xXX`: esattamente due cifre esadecimali, da `00` a `FF`. Questa forma copre i primi 256 caratteri Unicode, fra cui l'alfabeto latino e vari simboli comuni.

  ```js
  alert("\x7A"); // z
  alert("\xA9"); // ©, simbolo di copyright
  ```

- `\uXXXX`: esattamente quattro cifre esadecimali, da `0000` a `FFFF`. I punti di codice superiori a `U+FFFF` richiedono una coppia di surrogate quando usiamo questa notazione.

  ```js
  alert("\u00A9"); // ©, come \xA9
  alert("\u044F"); // я, lettera cirillica
  alert("\u2191"); // ↑, freccia verso l'alto
  ```

- `\u{X…XXXXXX}`: da una a sei cifre esadecimali, con valore fra `0` e `10FFFF`, il massimo punto di codice Unicode. Questa forma permette di rappresentare anche i caratteri oltre `U+FFFF` direttamente.

  ```js
  alert("\u{20331}"); // 佫, un carattere cinese poco comune
  alert("\u{1F60D}"); // 😍
  ```

## Coppie di surrogate

Molti caratteri comuni hanno una rappresentazione UTF-16 con una sola unità di codice di 16 bit. Unità di queste dimensioni permettono 65.536 valori distinti, insufficienti per tutti i punti di codice Unicode.

I punti di codice oltre `U+FFFF` sono quindi rappresentati da due unità di codice, dette **coppia di surrogate**. Come conseguenza, la loro lunghezza JavaScript è `2`:

```js
alert('𝒳'.length); // 2, X maiuscola matematica corsiva
alert('😂'.length); // 2, faccina con lacrime di gioia
alert('𩷶'.length); // 2, un carattere cinese poco comune
```

In ciascuna stringa vediamo un solo simbolo, ma `length` conta le due unità UTF-16. Anche l'accesso tramite indice considera separatamente le due metà:

```js
alert('𝒳'[0]); // prima metà della coppia: da sola non rappresenta il simbolo
alert('𝒳'[1]); // seconda metà della coppia
```

Le due parti non rappresentano quel carattere separatamente. La prima surrogate ha un valore nell'intervallo `0xD800..0xDBFF`; la seconda nell'intervallo `0xDC00..0xDFFF`. Questi intervalli sono riservati alle surrogate.

Per lavorare con i punti di codice JavaScript offre [String.fromCodePoint](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fromCodePoint) e [codePointAt](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/codePointAt). A differenza di `String.fromCharCode` e `charCodeAt`, possono gestire la coppia come un unico punto di codice.

```js
// charCodeAt legge soltanto la prima unità UTF-16 di 𝒳.
alert('𝒳'.charCodeAt(0).toString(16)); // d835

// codePointAt legge il punto di codice rappresentato dalle due unità.
alert('𝒳'.codePointAt(0).toString(16)); // 1d4b3
```

Se partiamo dall'indice `1`, tuttavia, entrambi leggono soltanto la seconda metà:

```js
alert('𝒳'.charCodeAt(1).toString(16)); // dcb3
alert('𝒳'.codePointAt(1).toString(16)); // dcb3
// È soltanto la seconda metà del simbolo originale.
```

Troverai altri modi di attraversare le stringhe nel capitolo <info:iterable>. Per esigenze più complesse, come contare ciò che una persona percepisce come un carattere, servono anche i concetti di cluster grafemico e segmentazione.

````warn header="Tagliare una stringa in un punto arbitrario può spezzare un simbolo"
Non possiamo assumere che `str.slice(0, 4)` mantenga interi tutti i punti di codice:

```js
alert('hi 😂'.slice(0, 4)); // conserva solo la prima metà dell'emoji
```

La stringa risultante contiene una surrogate isolata. Quando lavori con emoji e altri simboli fuori dal piano di base, considera questa differenza fra indici, punti di codice e caratteri visibili.
````

## Segni diacritici e normalizzazione

In molte lingue un simbolo comprende un carattere di base e un segno sopra o sotto. La lettera `a`, per esempio, può comparire come `àáâäãåā`.

Molti caratteri composti hanno un punto di codice proprio. Le combinazioni possibili sono però troppe per assegnarne uno a ciascuna. Unicode permette anche sequenze formate da una base seguita da uno o più segni combinanti.

Per esempio, `S` seguita dal segno «punto sopra» `\u0307` viene visualizzata come `Ṡ`:

```js
alert('S\u0307'); // Ṡ
```

Possiamo aggiungere anche il «punto sotto» `\u0323`:

```js
alert('S\u0307\u0323'); // Ṩ
```

Questo dà grande flessibilità, ma significa che stringhe visivamente uguali possono contenere sequenze diverse:

```js
let s1 = 'S\u0307\u0323'; // S + punto sopra + punto sotto
let s2 = 'S\u0323\u0307'; // S + punto sotto + punto sopra

alert(`s1: ${s1}, s2: ${s2}`);
alert(s1 == s2); // false, anche se l'aspetto è lo stesso
```

La **normalizzazione Unicode** porta le sequenze a una forma normalizzata. JavaScript la espone attraverso [normalize](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/normalize):

```js
alert('S\u0307\u0323'.normalize() == 'S\u0323\u0307'.normalize()); // true
```

In questo caso la sequenza di tre punti di codice può essere composta nell'unico punto `\u1E68`, una S con entrambi i punti:

```js
alert('S\u0307\u0323'.normalize().length); // 1
alert('S\u0307\u0323'.normalize() == '\u1e68'); // true
```

Questo non succede per tutte le combinazioni: dipende dall'esistenza di un carattere precomposto e dalle regole di normalizzazione. Per approfondire le forme disponibili consulta [Unicode Normalization Forms](https://www.unicode.org/reports/tr15/).
