---
title: "Operatori condizionali: if, '?'"
description: "JavaScript.info in italiano: Operatori condizionali: if, '?'"
sourceTutorial: true
prev: {"text": "Confronti", "link": "/javascript/tutorial/comparison"}
next: {"text": "Operatori logici", "link": "/javascript/tutorial/logical-operators"}
---

# Operatori condizionali: if, '?'

> **JavaScript.info · Ilya Kantor e contributori.** [Originale inglese](https://javascript.info/ifelse) · [Edizione italiana](https://it.javascript.info/ifelse) · [Fonti e licenza](/javascript/fonti).

Qualche volta abbiamo bisogno di eseguire certe azioni solo nel caso valgano determinate condizioni.

Per questo c'è l'istruzione `if` e l'operatore condizionale di valutazione a cui ci riferiremo, per semplicità, con "l'operatore punto di domanda" `?`.

## L'istruzione "if" 

L'istruzione `if(...)` valuta una condizione (racchiusa nelle parentesi); se il risultato è `true`, esegue il codice che segue `if`.

Ad esempio:

```js
let year = prompt('In which year was ECMAScript-2015 specification published?', '');


if (year == 2015) alert( 'You are right!' );

```

Nell'esempio sopra, la condizione è un semplice controllo di uguaglianza: `year == 2015`, ma potrebbe essere qualcosa di molto più complesso.

Se dobbiamo eseguire più di un'istruzione, queste vanno raggruppate tramite parentesi graffe:

```js
if (year == 2015) {
  alert( "That's correct!" );
  alert( "You're so smart!" );
}
```

E' consigliabile raggruppare sempre il codice all'interno delle parentesi graffe `{}`, quando si usa un `if`, anche se contiene una sola istruzione. La leggibilità ne guadagna.

## Conversione booleana

L'istruzione `if (…)` valuta la condizione tra le parentesi e converte il risultato al tipo booleano.

Ricordiamo le regole di conversione viste nel capitolo [Conversione di tipi](/javascript/tutorial/type-conversions):

- Il numero `0`, una stringa vuota `""`, `null`, `undefined` e `NaN` diventano `false`. Per questo vengono chiamati valori "falsi".
- Gli altri valori diventano `true`, quindi vengono chiamati "veri".

Quindi, il codice nell'esempio sotto, non verrà mai eseguito:

```js
if (0) { // 0 è falso
  ...
}
```

...Nel seguente esempio, invece, verrà sempre eseguito:

```js
if (1) { // 1 è vero
  ...
}
```

Possiamo anche passare un valore già valutato in precedenza, come qui:

```js
let cond = (year == 2015); // l'uguaglianza diventa vera o falsa

if (cond) {
  ...
}
```

## La clausola "else" 

L'istruzione `if` può essere seguita da un blocco opzionale "else". Questo viene eseguito quando la condizione è falsa.

Ad esempio:
```js
let year = prompt('In which year was the ECMAScript-2015 specification published?', '');

if (year == 2015) {
  alert( 'You guessed it right!' );
} else {
  alert( 'How can you be so wrong?' ); // qualsiasi valore tranne 2015
}
```

## Condizione multiple: "else if"

Qualche volta vorremmo testare diverse varianti di una condizione. Per questo esiste la clausola `else if`.

Ad esempio:

```js
let year = prompt('In which year was the ECMAScript-2015 specification published?', '');

if (year < 2015) {
  alert( 'Too early...' );
} else if (year > 2015) {
  alert( 'Too late' );
} else {
  alert( 'Exactly!' );
}
```

Nel codice sopra JavaScript controlla anzitutto la prima condizione, `year < 2015`. Se risulta falsa va alla successiva condizione `year > 2015` ed esegue il codice dentro le parentesi graffe, altrimenti esegue il codice dentro al blocco `else`.

Ci possono essere molti blocchi `else if`. L'`else` finale è opzionale.

## Operatore condizionale '?'

Qualche volta abbiamo bisogno di assegnare un valore ad una variabile in base ad una certa condizione.

Ad esempio:

```js
let accessAllowed;
let age = prompt('How old are you?', '');


if (age > 18) {
  accessAllowed = true;
} else {
  accessAllowed = false;
}


alert(accessAllowed);
```

Esiste un operatore "condizionale", o "punto interrogativo", che ci consente di farlo in maniera più breve e semplice.

L'operatore viene rappresentato dal punto interrogativo `?`.  Il termine formale è "ternario", perché richiede tre operatori. E' l'unico operatore in JavaScript che ne accetta così tanti.

La sintassi è:
```js
let result = condition ? value1 : value2;
```

La `condition` viene valutata; se risulta vera, viene ritornato `value1`, altrimenti viene ritornato `value2`.

Ad esempio:

```js
let accessAllowed = (age > 18) ? true : false;
```

Tecnicamente, potremmo omettere le parentesi attorno ad `age > 18`. L'operatore condizionale ha una precedenza molto bassa, viene eseguito dopo gli operatori di confronto `>`.

Il risultato dell'esempio sotto è uguale a quello precedente:

```js
// l'operatore di confronto "age > 18" viene eseguito per primo
// (non c'è bisogno di racchiuderlo tra parentesi)
let accessAllowed = age > 18 ? true : false;
```

Ma le parentesi rendono il codice più leggibile, quindi è consigliabile utilizzarle.


:::: tip Da sapere
Nell'esempio sopra sarebbe possibile omettere anche l'operatore ternario, perchè l'operatore di confronto `>` ritorna già di suo `true/false`:

```js
// stesso risultato (risulterà in `true` o `false`, a seconda del valore di `age`)
let accessAllowed = age > 18;
```
::::

## Multipli operatori '?'

Una sequenza di operatori `?` consente di ritornare un valore che dipende da più condizioni.

Ad esempio:
```js
let age = prompt('age?', 18);

let message = (age < 3) ? 'Hi, baby!' :
  (age < 18) ? 'Hello!' :
  (age < 100) ? 'Greetings!' :
  'What an unusual age!';

alert( message );
```

Potrebbe essere difficile, inizialmente, capirne la logica. Ma dopo averlo guardato da più vicino ci accorgeremo che è una semplice sequenza di condizioni.

1. Il primo operatore "?" controlla `age < 3`.
2. Se è vero -- ritorna `'Hi, baby!'`, altrimenti -- segue la colonna `":"`, controlla `age < 18`.
3. Se questo è vero -- ritorna `'Hello!'`, altrimenti -- segue la colonna `":"`, controlla `age < 100`.
4. Se questo è vero -- ritorna `'Greetings!'`, altrimenti -- segue la colonna `":"`, ritorna `'What an unusual age!'`.

La stessa logica riscritta utilizzando `if..else`:

```js
if (age < 3) {
  message = 'Hi, baby!';
} else if (age < 18) {
  message = 'Hello!';
} else if (age < 100) {
  message = 'Greetings!';
} else {
  message = 'What an unusual age!';
}
```

## Uso non tradizionale dell'operatore '?'

Qualche volta l'operatore `?` si utilizza per rimpiazzare l'istruzione `if`:

```js
let company = prompt('Which company created JavaScript?', '');


(company == 'Netscape') ?
   alert('Right!') : alert('Wrong.');

```

In base alla valutazione della condizione `company == 'Netscape'`, viene eseguita la prima o la seconda parte (e il rispettivo `alert`).

Qui non assegniamo il risultato ad una variabile. L'idea è di eseguire un codice differente a seconda della condizione.

**Non è consigliabile utilizzare l'operatore ternario in questo modo.**

La notazione risulta essere molto più breve rispetto all'istruzione `if`; questo viene sfruttato da molti programmatori, ma risulta meno leggibile.

Compariamo il codice sopra con una versione che utilizza `if` invece dell'operatore ternario `?`:
```js
let company = prompt('Which company created JavaScript?', '');


if (company == 'Netscape') {
  alert('Right!');
} else {
  alert('Wrong.');
}

```

I nostri occhi esaminano il codice verticalmente. I costrutti che si estendono per qualche riga risultano più semplici da capire piuttosto di un'unica istruzione che si estende orrizontalmente.

L'idea dell'operatore ternario `?` è di ritornare, in base a una condizione, un valore piuttosto di un altro. Va quindi utilizzato solo in questo tipo di situazioni. Per eseguire diversi codici è consigliabile utilizzare il costrutto `if`.

## Esercizi

### 1 · if (una stringa con zero)

L'`alert` verrà mostrato?

```js
if ("0") {
  alert( 'Hello' );
}
```

::::: details Soluzione

**Certo.**

Qualunque stringa -ad eccezione di quella vuota (`"0"` non lo è)- diventa `true` in contesto booleano.

Possiamo eseguirlo e controllare:

```js
if ("0") {
  alert( 'Hello' );
}
```

:::::

### 2 · Il nome di JavaScript

Usando il costrutto `if..else`, scrivi un codice che chieda: 'What is the "official" name of JavaScript?'

Se l'utente digita "ECMAScript", ritorna "Right!", altrimenti-- ritorna: "Didn't know? ECMAScript!"

![](/javascript-info/1-js/02-first-steps/10-ifelse/2-check-standard/ifelse_task2.svg)

[Apri l’esempio nella fonte originale](https://it.javascript.info/ifelse).

::::: details Soluzione

[html run src="ifelse_task2/index.html"]

:::::

### 3 · Mostra il segno

Utilizzando `if..else`, scrivi un codice che preleva un numero tramite `prompt` e lo mostra con un `alert`:

- `1`, se il valore è maggiore di zero,
- `-1`, se è minore di zero,
- `0`, se è uguale a zero.

In questo esercizio supporremo che l'input sia sempre un numero.

[Apri l’esempio nella fonte originale](https://it.javascript.info/ifelse).

::::: details Soluzione

```js
let value = prompt('Type a number', 0);

if (value > 0) {
  alert( 1 );
} else if (value < 0) {
  alert( -1 );
} else {
  alert( 0 );
}
```

:::::

### 4 · Riscrivi 'if' con '?'

Riscrivi il seguente `if` utilizzando l'operatore ternario `'?'`:

```js
let result;

if (a + b < 4) {
  result = 'Below';
} else {
  result = 'Over';
}
```

::::: details Soluzione

```js
let result = (a + b < 4) ? 'Below' : 'Over';
```

:::::

### 5 · Riscrivi 'if..else' con '?'

Riscrivi `if..else` utilizzando più volte l'operatore ternario `'?'`.

Per migliorare la leggibilità, è consigliato dividere il codice in più linee.

```js
let message;

if (login == 'Employee') {
  message = 'Hello';
} else if (login == 'Director') {
  message = 'Greetings';
} else if (login == '') {
  message = 'No login';
} else {
  message = '';
}
```

::::: details Soluzione

```js
let message = (login == 'Employee') ? 'Hello' :
  (login == 'Director') ? 'Greetings' :
  (login == '') ? 'No login' :
  '';
```

:::::

