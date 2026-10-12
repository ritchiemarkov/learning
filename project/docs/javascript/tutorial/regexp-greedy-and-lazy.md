---
title: "Modalità greedy e lazy dei quantificatori"
description: "JavaScript.info in italiano: Modalità greedy e lazy dei quantificatori"
sourceTutorial: true
prev: {"text": "Quantificatori +, *, ? and", "link": "/javascript/tutorial/regexp-quantifiers"}
next: {"text": "I gruppi di acquisizione (capturing group)", "link": "/javascript/tutorial/regexp-groups"}
---

# Modalità greedy e lazy dei quantificatori

> **JavaScript.info · Ilya Kantor e contributori.** [Originale inglese](https://javascript.info/regexp-greedy-and-lazy) · [Edizione italiana](https://it.javascript.info/regexp-greedy-and-lazy) · [Fonti e licenza](/javascript/fonti).

I quantificatori sono molto semplici a prima vista, ma in realtà possono rivelarsi complicati.

Dovremmo comprendere appieno come funziona la ricerca se intendiamo cercare qualcosa di più complesso di `/\d+/`.

Prendiamo ad esempio la seguente esercitazione.

Abbiamo bisogno di rimpiazzare tutti i doppi apici `"..."` in un testo con le virgolette basse: `«...»`, che sono preferite nella tipografia di molti paesi.

Ad esempio: `"Hello, world"` dovrebbe diventare `«Hello, world»`. Esistono altre virgolette, come `„Witam, świat!”` in Polonia o `「你好，世界」` in Cina, in questo caso, tuttavia, scegliamo `«...»`.

Innanzitutto dobbiamo individuare le stringhe tra doppi apici per poi sostituirli.

Un'espressione regolare come `/".+"/g` (una stringa di lunghezza variabile racchiusa da doppi apici) può sembrare efficace, ma non lo è!

Verifichiamo:

```js
let regexp = /".+"/g;

let str = 'a "witch" and her "broom" is one';

alert( str.match(regexp) ); // "witch" and her "broom"
```

Non funziona come desideravamo!

Invece di trovare i due riscontri `"witch"` e `"broom"`, ne trova solo uno: `"witch" and her "broom"`.

Questo fenomeno può essere descritto così: "l'avidità è la causa di tutti i mali".

## La ricerca in modalità greedy (avida)

Per trovare un riscontro, l'interprete dell'espressione regolare usa il seguente algoritmo:

- Per ogni posizione nella stringa
    - Cerca un riscontro del pattern in quella posizione.
    - Se non c'è un riscontro, passa alla posizione successiva.

Questa procedura generica non ci spiega con evidenza perché l'espressione regolare fallisca, quindi approfondiamo come funziona la ricerca per il pattern `".+"`.

1. Il primo carattere del pattern è un doppio apice `"`.

    L'interprete dell'espressione regolare lo cerca alla posizione zero della stringa `a "witch" and her "broom" is one`, ma in quel punto trova `a`, pertanto non c'è immediata corrispondenza.

    Quindi procede: passa alle successive posizioni nella stringa sorgente e prova a trovare lì il primo carattere del pattern, prima fallisce nuovamente, e poi trova finalmente il doppio apice nella terza posizione:

    ![](/javascript-info/9-regular-expressions/10-regexp-greedy-and-lazy/witch_greedy1.svg)

2. Rilevato il doppio apice, tenta di trovare riscontro per il resto del pattern. Verifica se il resto della stringa sia conforme a `.+"`.

    Nel nostro esempio il successivo carattere del pattern è `.` (un punto) che indica "qualsiasi carattere tranne una nuova riga". Trova pertanto corrispondenza nel carattere successivo della stringa `'w'`:

    ![](/javascript-info/9-regular-expressions/10-regexp-greedy-and-lazy/witch_greedy2.svg)

3. Successivamente il punto trova ulteriori riscontri per via del quantificatore `.+`. L'interprete dell'espressione regolare aggiunge un carattere dopo l'altro.

    Fino a quando? Tutti i caratteri corrispondono al punto, quindi si ferma solo quando raggiunge la fine della stringa:

    ![](/javascript-info/9-regular-expressions/10-regexp-greedy-and-lazy/witch_greedy3.svg)

4. A questo punto cessa di ripetere `.+` e prova a trovare il prossimo carattere del pattern. Si tratta del doppio apice `"`. C'è un problema però: la stringa è finita, non ci sono più caratteri!

    L'interprete dell'espressione regolare capisce di aver preso troppi caratteri per `.+` e comincia a *retrocedere*.

    In altre parole accorcia di un carattere la corrispondenza per il quantificatore:

    ![](/javascript-info/9-regular-expressions/10-regexp-greedy-and-lazy/witch_greedy4.svg)

    A questo punto presume che `.+` finisca un carattere prima della fine della stringa e verifica la corrispondenza del resto del pattern da quella posizione.

    Se ci fosse stato un doppio apice, la ricerca sarebbe terminata, ma l'ultima carattere è una `'e'`, nessun riscontro quindi.

5. Allora l'interprete diminuisce di un ulteriore carattere il numero delle ripetizioni di `.+`:

    ![](/javascript-info/9-regular-expressions/10-regexp-greedy-and-lazy/witch_greedy5.svg)

    Anche il carattere `'n'` non soddisfa la ricerca di `'"'`.

6. L'interprete continua a retrocedere: diminuisce le ripetizioni per `'.'` finché il resto del pattern (nel nostro caso `'"'`) non trova riscontro:

    ![](/javascript-info/9-regular-expressions/10-regexp-greedy-and-lazy/witch_greedy6.svg)

7. La ricerca è completa.

8. Il primo riscontro è quindi `"witch" and her "broom"`. Se l'espressione regolare ha il flag `g`, allora la ricerca proseguirà a partire dalla fine della prima corrispondenza. Non ci sono più doppi apici nel resto della stringa `is one`e, pertanto, non c'è nessun altro risultato.

Probabilmente non è quello che ci aspettavamo, ma funziona così.

**In modalità greedy (quella predefinita) un quantificatore viene ripetuto quante più volte possibile.**

L'interprete della regexp aggiunge quanti più caratteri possibili alla corrispondenza con `.+`, successivamente retrocede di un carattere alla volta se il resto del pattern non trova riscontro.

L'obiettivo della nostra esercitazione non è questo, proprio in questi casi viene in soccorso la modalità lazy.

## Modalità lazy (pigra)

La modalità lazy di un quantificatore è l'opposto della modalità greedy. Significa: "ripeti il minor numero di volte".

Possiamo abilitarla mettendo un punto interrogativo `'?'` dopo il quantificatore, così che diventi `*?` o `+?` o ancora `??` per `'?'`.

Ricapitoliamo per chiarezza: di norma il punto interrogativo `?` è di per sé un quantificatore (zero o un carattere), ma se aggiunto *dopo un altro quantificatore (anche dopo se stesso)* assume un altro significato: cambia la modalità di ricerca da greedy a lazy.

La regexp `/".+?"/g` soddisfa le nostre esigenze: trova `"witch"` e `"broom"`:

```js
let regexp = /".+?"/g;

let str = 'a "witch" and her "broom" is one';

alert( str.match(regexp) ); // "witch", "broom"
```

Per comprendere distintamente cosa sia cambiato, seguiamo la ricerca passo dopo passo.

1. Il primo step non cambia: trova l'inizio del pattern `'"'` nella terza posizione:

    ![](/javascript-info/9-regular-expressions/10-regexp-greedy-and-lazy/witch_greedy1.svg)

2. Anche il secondo step è simile: l'interprete trova una corrispondenza per il punto `'.'`:

    ![](/javascript-info/9-regular-expressions/10-regexp-greedy-and-lazy/witch_greedy2.svg)

3. Da questo punto la ricerca procede in modo differente. Dal momento che il quantificatore è in modalità lazy `+?`, l'interprete non prova a cercare il punto più di una volta, si ferma e cerca subito la corrispondenza con il resto del pattern  `'"'`:

    ![](/javascript-info/9-regular-expressions/10-regexp-greedy-and-lazy/witch_lazy3.svg)

    Se ci fosse un doppio apice a questo punto la ricerca sarebbe già terminata, ma c'è una `'i'` e quindi nessuna corrispondenza.
4. L'interprete della regexp allora aumenta il numero delle ripetizioni per il punto e riprova:

    ![](/javascript-info/9-regular-expressions/10-regexp-greedy-and-lazy/witch_lazy4.svg)

    Ancora nessun risultato. Il numero delle ripetizioni, pertanto, si accresce di volta in volta...
5. ...finché viene riscontrata la corrispondenza con il resto del pattern:

    ![](/javascript-info/9-regular-expressions/10-regexp-greedy-and-lazy/witch_lazy5.svg)

6. La ricerca successiva inizia dalla fine della corrispondenza corrente e produce un altro risultato:

    ![](/javascript-info/9-regular-expressions/10-regexp-greedy-and-lazy/witch_lazy6.svg)

In questo esempio abbiamo visto come funziona la modalità lazy per `+?`. I quantificatori `*?` e `??` operano in modo simile: aumentano il numero delle ripetizioni solo se il resto del pattern non ha corrispondenza in una data posizione.

**La modalità lazy è abilitata unicamente per il quantificatore seguito da `?`.**

Gli altri quantificatori continuano ad operare in modalità greedy.

Per esempio:

```js
alert( "123 456".match(/\d+ \d+?/) ); // 123 4
```

1. Il pattern `\d+` cerca quanti più caratteri gli è possibile (modalità greedy), e si ferma quindi dopo aver trovato `123`, perché il carattere successivo è una spaziatura `' '`.
2. Segue la corrispondenza dello spazio nel pattern.
3. A questo punto c'è `\d+?`. Il quantificatore è modalità lazy, perciò trova solo una cifra `4` e prova a verificare se il resto del pattern è soddisfatto.

    Nel pattern, tuttavia, non c'è niente dopo `\d+?`.

    La modalità lazy non ripete nulla se non c'è un motivo. Il pattern è finito e conclude la ricerca. La nostra corrispondenza è `123 4`.


::: tip Ottimizzazioni
I moderni motori delle regexp possono ottimizzare internamente i loro algoritmi per essere più rapidi. Potrebbero quindi operare in modo leggermente diverso da quanto abbiamo spiegato prima.

Ma per comprendere come funzionino le espressioni regolari e come implementarle non abbiamo bisogno di conoscere questi dettagli. Si tratta di meccanismi interni per ottimizzarne il rendimento.

Del resto è difficile ottimizzare le espressioni regolari complesse, pertanto la ricerca potrebbe anche funzionare esattamente come indicato.
:::

## Un approccio alternativo

Con le espressioni regolari, spesso abbiamo a disposizione diversi modi di ottenere lo stesso risultato.

Nel nostro caso potremmo trovare le stringhe tra doppi apici senza la modalità lazy, usando la regexp `"[^"]+"`:

```js
let regexp = /"[^"]+"/g;

let str = 'a "witch" and her "broom" is one';

alert( str.match(regexp) ); // "witch", "broom"
```

La regexp `"[^"]+"` restituisce il risultato corretto, perché cerca un doppio apice `'"'`, seguito da uno o più caratteri che non siano doppi apici `[^"]` e successivamente un doppio apice di chiusura.

Quando l'interprete della regexp cerca `[^"]+` si arresta quando incontra il doppio apice di chiusura e termina il suo lavoro.

Si noti che questa logica non rimpiazza i quantificatori lazy!

Sono due approcci differenti. Talvolta ci serve uno, a volte l'altro.

**Guardiamo un esempio in cui i quantificatori lazy falliscono e questa variante funziona a dovere.**

Se volessimo, per esempio, trovare dei link di questo tipo `<a href="..." class="doc">`, con qualsiasi contenuto per `href`.

Quale espressione regolare dovremmo usare?

La prima idea potrebbe essere: `/<a href=".*" class="doc">/g`.

Proviamo:
```js
let str = '...<a href="link" class="doc">...';
let regexp = /<a href=".*" class="doc">/g;

// Funziona!
alert( str.match(regexp) ); // <a href="link" class="doc">
```

Ha funzionato. Ma vediamo, cosa succede se ci sono più link nel testo?

```js
let str = '...<a href="link1" class="doc">... <a href="link2" class="doc">...';
let regexp = /<a href=".*" class="doc">/g;

// Ops! Due link in una sola corrispondenza!
alert( str.match(regexp) ); // <a href="link1" class="doc">... <a href="link2" class="doc">
```

Il risultato adesso è errato per lo stesso motivo dell'esempio di prima con "witches". Il quantificatore `.*` ha preso troppi caratteri.

Possiamo rappresentare la corrispondenza in questo modo:

```html
<a href="....................................." class="doc">
<a href="link1" class="doc">... <a href="link2" class="doc">
```

Modifichiamo allora il pattern rendendo lazy il quantificatore `.*?`:

```js
let str = '...<a href="link1" class="doc">... <a href="link2" class="doc">...';
let regexp = /<a href=".*?" class="doc">/g;

// Funziona!
alert( str.match(regexp) ); // <a href="link1" class="doc">, <a href="link2" class="doc">
```

Ora sembra funzionare, ci sono due riscontri:

```html
<a href="....." class="doc">    <a href="....." class="doc">
<a href="link1" class="doc">... <a href="link2" class="doc">
```

Ma proviamo ancora su un testo differente:

```js
let str = '...<a href="link1" class="wrong">... <p style="" class="doc">...';
let regexp = /<a href=".*?" class="doc">/g;

// Corrispondenza errata!
alert( str.match(regexp) ); // <a href="link1" class="wrong">... <p style="" class="doc">
```

Ora fallisce. La corrispondenza include non solo il link, ma anche molto altro testo dopo di esso, incluso `<p...>`.

Perché?

Ecco quello che sta succedendo:

1. Per prima cosa la regexp trova la prima parte del link `<a href="`.
2. Dopo cerca `.*?`: considera un solo carattere (in modalità lazy!), verifica se c'è riscontro con `" class="doc">` (nessuna).
3. Successivamente prende un altro carattere per `.*?`, e così via...fino al raggiungimento di `" class="doc">`.

Ma il problema è: quella parte è già al di fuori del link `<a...>`, in un altro tag `<p>`. Non è quello che desideriamo.

Ecco la rappresentazione della corrispondenza con il testo allineato:

```html
<a href="..................................." class="doc">
<a href="link1" class="wrong">... <p style="" class="doc">
```

Ricapitoliamo, abbiamo bisogno del pattern per cercare `<a href="...something..." class="doc">`, ma entrambe le varianti greedy e lazy danno problemi.

Un'alternativa corretta potrebbe essere: `href="[^"]*"`. Essa prenderà tutti i caratteri dentro l'attributo `href` fino al doppio apice più vicino. Proprio quello di cui abbiamo bisogno!

Ecco un esempio funzionante:

```js
let str1 = '...<a href="link1" class="wrong">... <p style="" class="doc">...';
let str2 = '...<a href="link1" class="doc">... <a href="link2" class="doc">...';
let regexp = /<a href="[^"]*" class="doc">/g;

// Funziona!
alert( str1.match(regexp) ); // null, è corretto che non ci sia alcun riscontro
alert( str2.match(regexp) ); // <a href="link1" class="doc">, <a href="link2" class="doc">
```

## Riepilogo

I quantificatori possono funzionare in due modalità differenti:

Greedy
: L'interprete delle espressioni regolari, in via predefinita, prova a ripetere un quantificatore quante più volte possibile. Per esempio, `\d+` considera tutte le cifre disponibili. Quando diventa impossibile trovarne ancora (non ci sono più cifre o è finita la stringa), allora continua a cercare la corrispondenza con il resto del pattern. Se non trova riscontro allora retrocede, diminuisce il numero di ripetizioni e prova ancora.

Lazy
: Abilitata dal punto interrogativo `?` dopo il quantificatore. L'interprete delle regexp prova la corrispondenza del resto del pattern prima di ogni ripetizione di un carattere quantificato.

Come abbiamo visto, la modalità lazy non è una "panacea" per i problemi della ricerca greedy. Un'alternativa può essere una ricerca greedy "calibrata", avvalendoci delle esclusioni come nel pattern `"[^"]+"`.

## Esercizi

### 1 · Individuate la corrispondenza per /d+? d+?/

Quale è la corrispondenza in questo caso?

```js
alert( "123 456".match(/\d+? \d+?/g) ); // ?
```

::::: details Soluzione

Il risultato è: `123 4`.

Inizialmente il quantificatore lazy `\d+?` prova a prendere il minor numero di cifre, ma deve raggiungere lo spazio, perciò include `123`.

Il secondo `\d+?` prende una cifra soltanto perché è sufficiente.

:::::

### 2 · Trovate i commenti HTML

Trovate tutti i commenti HTML nel testo:

```js
let regexp = /your regexp/g;

let str = `... <!-- My -- comment
 test --> ..  <!----> ..
`;

alert( str.match(regexp) ); // '<!-- My -- comment \n test -->', '<!---->'
```

::::: details Soluzione

Abbiamo bisogno di trovare l'inizio del commento `<!--`, e dopo tutto quello che c'è fino a `-->`.

Una variante accettabile è `<!--.*?-->`, il quantificatore lazy fa sì che la ricerca si fermi prima di `-->`. Dobbiamo, inoltre, aggiungere il flag `s` in modo che il punto includa gli a capo.

In caso contrario i commenti multilinea non verranno trovati:

```js
let regexp = /<!--.*?-->/gs;

let str = `... <!-- My -- comment
 test --> ..  <!----> ..
`;

alert( str.match(regexp) ); // '<!-- My -- comment \n test -->', '<!---->'
```

:::::

### 3 · Trovate i tag HTML

Create un'espressione regolare per trovare tutti i tag HTML (di apertura e di chiusura) con i loro attributi.

Ecco un esempio d'uso:

```js
let regexp = /your regexp/g;

let str = '<> <a href="/"> <input type="radio" checked> <b>';

alert( str.match(regexp) ); // '<a href="/">', '<input type="radio" checked>', '<b>'
```

In questo caso presumiamo che gli attributi dei tag non contengano `<` e `>` dentro i doppi apici per semplificare l'esercizio.

::::: details Soluzione

La soluzione è `<[^<>]+>`.

```js
let regexp = /<[^<>]+>/g;

let str = '<> <a href="/"> <input type="radio" checked> <b>';

alert( str.match(regexp) ); // '<a href="/">', '<input type="radio" checked>', '<b>'
```

:::::

