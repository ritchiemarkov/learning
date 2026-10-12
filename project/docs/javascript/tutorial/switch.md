---
title: "L'istruzione \"switch\""
description: "JavaScript.info in italiano: L'istruzione \"switch\""
sourceTutorial: true
prev: {"text": "Cicli: while e for", "link": "/javascript/tutorial/while-for"}
next: {"text": "Funzioni", "link": "/javascript/tutorial/function-basics"}
---

# L'istruzione "switch"

> **JavaScript.info · Ilya Kantor e contributori.** [Originale inglese](https://javascript.info/switch) · [Edizione italiana](https://it.javascript.info/switch) · [Fonti e licenza](/javascript/fonti).

L'istruzione `switch` può essere utile per rimpiazzare multipli `if`.

E' infatti un metodo molto più descrittivo per lavorare con un elemento che può avere svariati valori.

## La sintassi

Un istruzione `switch` possiede uno o più `case` ed opzionalmente un blocco *default*.

Un esempio:

```js
switch(x) {
  case 'value1':  // if (x === 'value1')
    ...
    [break]

  case 'value2':  // if (x === 'value2')
    ...
    [break]

  default:
    ...
    [break]
}
```

- Il valore di `x` viene controllato utilizzando l'uguaglianza stretta con i valori dei blocchi `case` (`value1` e `value2` nell'esempio sopra).
- Se l'uguaglianza viene trovata, `switch` inizia ad eseguire il codice partendo dal corrispondente blocco `case`, fino al `break` più vicino (oppure fino alla fine dello `switch`).
- Se non viene trovata nessuna uguaglianza allora viene eseguito il codice del blocco `default` (se presente).

## Un esempio

Un esempio di `switch`:

```js
let a = 2 + 2;

switch (a) {
  case 3:
    alert( 'Too small' );
    break;

  case 4:
    alert( 'Exactly!' );
    break;

  case 5:
    alert( 'Too big' );
    break;
  default:
    alert( "I don't know such values" );
}
```

Qui lo `switch` inizia confrontando `a` con il primo `case`, il cui valore è `3`. Non vi è corrispondenza.

Poi valuta `4`. C'è una corrispondenza, quindi l'esecuzione inizia da `case 4` fino al `break` più vicino.

**Se non c'è nessun `break` l'esecuzione procede al prossimo `case`.**

Un esempio senza `break`:

```js
let a = 2 + 2;

switch (a) {
  case 3:
    alert( 'Too small' );

  case 4:
    alert( 'Exactly!' );
  case 5:
    alert( 'Too big' );
  default:
    alert( "I don't know such values" );

}
```

Nell'esempio sopra, non essendoci un `break`, abbiamo l'esecuzione sequenziale dei tre `alert`:

```js
alert( 'Exactly!' );
alert( 'Too big' );
alert( "I don't know such values" );
```


:::: tip Qualsiasi espressione può essere un argomento `switch/case`.
Sia `switch` che `case` accettano espressioni arbitrarie.

Ad esempio:

```js
let a = "1";
let b = 0;

switch (+a) {

  case b + 1:
    alert("this runs, because +a is 1, exactly equals b+1");
    break;


  default:
    alert("this doesn't run");
}
```
```
Qui `+a` viene convertito in `1`, che nei `case` viene confrontato con `b + 1`, ed il codice corrispondente viene eseguito. 
```

## Raggruppare i "case"

Possiamo raggruppare diverse varianti di `case` e far loro eseguire lo stesso codice.

Ad esempio, se vogliamo eseguire lo stesso codice per `case 3` e `case 5`:

```js
let a = 3;

switch (a) {
  case 4:
    alert('Right!');
    break;


  case 3: // (*) raggruppiamo due casi
  case 5:
    alert('Wrong!');
    alert("Why don't you take a math class?");
    break;


  default:
    alert('The result is strange. Really.');
}
```

Ora sia `3` che `5` mostreranno lo stesso messaggio.

L'abilità di "raggruppare" più `case` è un effetto collaterale di come `switch/case` funziona senza `break`. Qui l'esecuzione del `case 3` inizia dalla linea `(*)` e prosegue fino a `case 5`, perché non c'è alcun `break`.

## Il tipo conta

Mettiamo in risalto che il confronto di uguaglianza è sempre stretto. I valori devono essere dello stesso tipo perché si possa avere una corrispondenza.

Ad esempio, consideriamo il codice:

```js
let arg = prompt("Enter a value?");
switch (arg) {
  case '0':
  case '1':
    alert( 'One or zero' );
    break;

  case '2':
    alert( 'Two' );
    break;

  case 3:
    alert( 'Never executes!' );
    break;
  default:
    alert( 'An unknown value' );
}
```

1. Per `0` e `1`, viene eseguito il primo `alert`.
2. Per `2` viene eseguito il secondo `alert`.
3. Per `3`, il risultato del `prompt` è una stringa, `"3"`, che non è strettamente uguale `===` al numero `3`. Quindi abbiamo del codice 'morto' nel `case 3`! Verrà quindi eseguito il codice dentro `default`.
::::

## Esercizi

### 1 · Riscrivi il costrutto "switch" come un "if"

Riscrivi il codice utilizzando `if..else` in modo tale che corrisponda al seguente `switch`:

```js
switch (browser) {
  case 'Edge':
    alert( "You've got the Edge!" );
    break;

  case 'Chrome':
  case 'Firefox':
  case 'Safari':
  case 'Opera':
    alert( 'Okay we support these browsers too' );
    break;

  default:
    alert( 'We hope that this page looks ok!' );
}
```

::::: details Soluzione

Per ottenere una corrispondenza precisa con il costrutto `switch`, `if` deve utilizzare l'uguaglianza stretta `'==='`.

Per le stringhe fornite, tuttavia, un semplice `'=='` può bastare.

```js
if(browser == 'Edge') {
  alert("You've got the Edge!");
} else if (browser == 'Chrome'
 || browser == 'Firefox'
 || browser == 'Safari'
 || browser == 'Opera') {
  alert( 'Okay we support these browsers too' );
} else {
  alert( 'We hope that this page looks ok!' );
}
```

Da notare: il costrutto `browser == 'Chrome' || browser == 'Firefox' …` viene diviso in più linee per una maggiore leggibilità.

Il costrutto `switch` risulta però più pulito e descrittivo.

:::::

### 2 · Riscrivi "if" utilizzando "switch"

Riscrivi il codice sotto utilizzando un singolo `switch`:

```js
let a = +prompt('a?', '');

if (a == 0) {
  alert( 0 );
}
if (a == 1) {
  alert( 1 );
}

if (a == 2 || a == 3) {
  alert( '2,3' );
}
```

::::: details Soluzione

I primi due controlli vengono trasformati in due `case` separati. Il terzo controllo viene diviso in due `case` raggruppati:

```js
let a = +prompt('a?', '');

switch (a) {
  case 0:
    alert( 0 );
    break;

  case 1:
    alert( 1 );
    break;

  case 2:
  case 3:
    alert( '2,3' );

    break;

}
```

Da notare: il `break` alla fine non è richiesto. Lo abbiamo messo per rendere il codice pronto ad aggiornamenti futuri.

In futuro, potremmo voler aggiungere un ulteriore `case`, ad esempio `case 4`. E se ci dimentichiamo di aggiungere il `break` prima di scrivere il nuovo `case`, al termine del `case 3` ci sarà un errore. Quindi aggiungere il `break` è una sorta di prevenzione.

:::::

