---
title: "Cicli: while e for"
description: "JavaScript.info in italiano: Cicli: while e for"
sourceTutorial: true
prev: {"text": "Nullish coalescing operator '??'", "link": "/javascript/tutorial/nullish-coalescing-operator"}
next: {"text": "L'istruzione \"switch\"", "link": "/javascript/tutorial/switch"}
---

# Cicli: while e for

> **JavaScript.info · Ilya Kantor e contributori.** [Originale inglese](https://javascript.info/while-for) · [Edizione italiana](https://it.javascript.info/while-for) · [Fonti e licenza](/javascript/fonti).

Abbiamo spesso bisogno di eseguire la stessa azione più volte di fila.

Ad esempio, quando abbiamo bisogno di ritornare, una dopo l'altra, della merce da una lista; o anche solo eseguire lo stesso codice per ogni numero da 1 a 10.

I *cicli* sono un modo di ripetere una stessa parte di codice più volte.

## Il ciclo "while" 

Il ciclo `while` ha la seguente sintassi:

```js
while (condition) {
  // codice
  // "corpo del ciclo"
}
```

Fino a che la `condition` è `true`, il `code` nel corpo del ciclo viene eseguito.

Ad esempio, il ciclo qui sotto mostra `i` fino a che `i < 3`:

```js
let i = 0;
while (i < 3) { // mostra 0, poi 1, poi 2
  alert( i );
  i++;
}
```

Un'esecuzione del codice nel corpo del ciclo viene chiamata *un'iterazione*. Il ciclo nell'esempio sopra fa tre iterazioni.

Se nell'esempio sopra non ci fosse `i++`, il ciclo si ripeterebbe per sempre; in teoria: in pratica, il browser ha dei metodi per bloccare questi cicli. In JavaScript server-side è necessario arrestare il processo.

Qualsiasi espressione o variabile può essere utilizzata come condizione di un ciclo, non solo un confronto come `i < 3`. Il ciclo `while` converte le espressioni al tipo booleano, che vengono poi valutate.

Ad esempio, un modo più breve di scrivere `while (i != 0)` potrebbe essere `while (i)`:

```js
let i = 3;

while (i) { // quando i diventa 0, la condizione diventa falsa e il ciclo si conclude

  alert( i );
  i--;
}
```


:::: tip Le parentesi non sono richieste per un corpo composto da una singola linea di codice
Se il corpo del ciclo ha una singola istruzione, possiamo omettere le parentesi `{…}`:

```js
let i = 3;

while (i) alert(i--);

```
::::

## Il ciclo "do..while" 

La condizione da controllare può essere messa *dopo* il corpo del ciclo. Lo si fa utilizzando la sintassi `do..while`:

```js
do {
  // corpo del ciclo
} while (condition);
```

Il ciclo esegue prima il corpo, poi controlla la condizione; se questa è vera, esegue nuovamente il corpo.

Ad esempio:

```js
let i = 0;
do {
  alert( i );
  i++;
} while (i < 3);
```

Questa tipo di sintassi viene usata molto raramente, ad eccezione dei casi in cui si vuole che il corpo del ciclo venga eseguito **almeno una volta**. Questo avviene ancor *prima* del controllo della condizione. La forma più comune, comunque, è `while(…) {…}`.

## Il ciclo "for" 

Il ciclo `for` è forse il più utilizzato.

La sua sintassi è:

```js
for (begin; condition; step) {
  // ... corpo del ciclo ...
}
```
Cerchiamo ora di capire, tramite esempi, il suo funzionamento. 
Il ciclo sotto esegue `alert(i)` fino a quando la variabile `i` è più piccola di 3. A ogni iterazione, il valore di `i` aumenta di 1.

```js
for (let i = 0; i < 3; i++) { // mostra 0, poi 1, poi 2
  alert(i);
}
```

Esaminiamo l'istruzione `for` parte per parte:

| Parte |          |                                                                            |
|-------|----------|----------------------------------------------------------------------------|
| begin | `i = 0`    | Viene eseguito una volta sola, all'entrata nel ciclo.                          |
| condition | `i < 3`| Viene controllata prima di ogni iterazione; se falsa, il ciclo si interrompe.|
| body | `alert(i)`| Viene eseguito fino a quando la condizione è vera.
| step| `i++`      | Viene eseguito ad ogni iterazione, dopo il corpo, fintato che la condizione è `true`.|

L'iterazione, generalmente, funziona nel modo seguente:
```
Eseguiamo begin
→ (if condition → run body and run step)
→ (if condition → run body and run step)
→ (if condition → run body and run step)
→ ...
```

Ricapitolando: `begin` viene eseguito per primo, *una volta sola*; subito dopo, inizia l'iterazione. Se `condition`, dopo la conversione a booleano, è `true`, vengono eseguiti `body` e `step`; se è `false`, il ciclo si interrompe. 

Se i cicli vi sono nuovi, forse vi sarà d'aiuto tornare indietro agli esempi e provare a riprodurli, passo passo, su un foglio di carta.

Ecco esattamente, in dettaglio, ciò che avviene nel nostro codice:

```js
// for (let i = 0; i < 3; i++) alert(i)

// inizia l'esecuzione, viene dichiarata la variabile i
let i = 0
// if(condition == true) → esegue il corpo e avanza
if (i < 3) { alert(i); i++ }
// if(condition == true) → esegue il corpo e avanza
if (i < 3) { alert(i); i++ }
// if(condition == true) → esegue il corpo e avanza
if (i < 3) { alert(i); i++ }
// ...si conclude, perché ora i == 3 e la condizione i < 3 == false
```


:::: tip Dichiarazioni di variabili inline
Qui il "counter", che utilizzeremo nella nostra *condition*, è una variabile: `i`. Viene dichiarata all'interno del corpo del ciclo ed è accessibile solo al suo interno. Questo tipo di espressione si chiama "dichiarazione di una variabile *inline*". 

```js
for (let i = 0; i < 3; i++) { //'i' è definito, e accessibile, solo dentro il corpo del ciclo
  alert(i); // 0, 1, 2
}
alert(i); // errore, nessuna variabile 'i' fuori dal corpo del ciclo
```

Invece di definire una nuova variabile, possiamo utilizzarne una già esistente:

```js
let i = 0;

for (i = 0; i < 3; i++) { // utilizza una variabile esistente
  alert(i); // 0, 1, 2
}

alert(i); // 3; la variabile `i` è accessibile (è stata dichiarata fuori dal corpo del ciclo)
```

::::


### Parti opzionali

Ogni parte del ciclo `for` è opzionale.

Ad esempio, possiamo omettere `begin` se non abbiamo bisogno di una variabile per la nostra `condition`.

Come in questo esempio:

```js
let i = 0; // la variabile 'i' è stata già dichiarata e assegnata

for (; i < 3; i++) { // saltiamo "begin"
  alert( i ); // 0, 1, 2
}
```

Possiamo anche rimuovere lo`step`:

```js
let i = 0;

for (; i < 3;) {
  alert( i++ ); //la variabile 'i' viene incrementata nel corpo del ciclo
}
```

Il ciclo, nell'esempio sopra, diventa uguale ad un `while (i < 3)`.

Possiamo rimuovere tutto, ma questo risulterebbe in un ciclo infinito:

```js
for (;;) {
  // esegue il corpo del ciclo senza mai terminare
}
```

Nota che le due `;` del ciclo `for` devono essere presenti, altrimenti vi sarebbe un errore di sintassi.

## Interrompere un ciclo 

Normalmente un ciclo termina quando la condizione diventa falsa.

Ma è possibile forzare l'uscita in qualsiasi momento. C'è una speciale direttiva per fare questo: `break`.

Ad esempio, il ciclo sotto richiede all'utente una serie di numeri, e termina quando nessun numero viene inserito: 

```js
let sum = 0;

while (true) {

  let value = +prompt("Enter a number", '');


  if (!value) break; // (*)


  sum += value;

}
alert( 'Sum: ' + sum );
```

La direttiva `break` viene attivata alla linea `(*)`, quando l'utente inserisce una linea vuota o annulla la procedura di input. Questo ferma il ciclo immediatamente, passando il controllo alla prima linea successiva al ciclo. In questo caso, `alert`.

La combinazione "ciclo infinito + `break` quando necessario" è utile in situazioni in cui la condizione deve essere verificata in un punto differente dall'inizio/fine del ciclo (questo può avvenire in un qualsiasi altro punto del corpo).

## Vai alla prossima iterazione
La direttiva `continue` è una versione leggera del `break`. Non blocca l'intero ciclo: interrompe solo l'iterazione corrente e forza il ciclo a passare all'iterazione successiva.

Possiamo utilizzarla se abbiamo finito con le operazioni che ci interessano e vogliamo passare all'iterazione seguente.

Il ciclo sotto usa `continue` per ritornare *solo* i valori dispari:

```js
for (let i = 0; i < 10; i++) {

  // se condizione == true (`i` è pari) salta la restante parte di codice a passa alla prossima iterazione
  if (i % 2 == 0) continue;
  //se `i` è dispari, esegui codice
  alert(i); // 1, poi 3, 5, 7, 9 (nota le due condizioni sopra: abbiamo solo i con un valore dispari, e inferiore a 10)
}
```

Per i valori pari di `i` la direttiva `continue` interrompe l'esecuzione del corpo e passa il controllo alla successiva iterazione del `for` (`i` viene incrementato, poi si controlla che la condizione sia true). Di conseguenza, l'`alert` viene seguito solo con i valori dispari.


:::: tip La direttiva `continue` aiuta a diminuire i livelli di nidificazione
Un ciclo che mostra *solo* valori dispari potrebbe essere:

```js
for (let i = 0; i < 10; i++) {

  if (i % 2) { //la condizione == 0 quando un numero è pari; 0, ricordiamo, convertito a booleano, è false
    alert( i );
  }

}
```

Ovviamente possiamo raccogliere il codice in un blocco `if` piuttosto di usare `continue`. Dal punto di vista tecnico l'esempio sopra è identico a quello che lo precede, che invece utilizza `continue`. Nell'esempio sopra il codice dentro il corpo di `if` è una semplice chiamata ad `alert`; ma se il codice fosse più lungo di un paio di righe si rischierebbe di perdere in leggibilità.
::::


:::: warning Vietato `break/continue` alla desta di '?'
Va notato che questo costrutto sintattico non è un espressione e non può quindi essere utilizzato con l'operatore ternario `?`. In particolare, direttive come  `break/continue` non sono permesse.

Ad esempio, se prendiamo questo codice:

```js
if (i > 5) {
  alert(i);
} else {
  continue;
}
```

...E lo riscriviamo utilizzando l'operatore ternario:


```js
(i > 5) ? alert(i) : continue; // continue non è consentito qui
```

...Questo smetterà di funzionare. Un codice come quello sopra risulterà in un errore di sintassi:


Questa è solo un'altra ragione per cui non utilizzare l'operatore ternario `?` piuttosto di `if`.
::::

## Etichette break/continue

Qualche volta abbiamo bisogno di uscire da una serie di cicli annidati in un *colpo solo*.

Ad esempio, nel codice sotto abbiamo due cicli `for` che usano `(i, j)` nelle proprie condizioni; fino a quando le variabili sono minori di 3, il ciclo viene eseguito; dentro al ciclo più interno un prompt mostra le due variabili 
`(i, j)` in una stringa di testo:

```js
for (let i = 0; i < 3; i++) {

  for (let j = 0; j < 3; j++) {

    let input = prompt(`Value at coords (${i},${j})`, '');

    // come potremmo fare per uscire di qui e proseguire verso Done (sotto)?

  }
}

alert('Done!');
```

Abbiamo bisogno di un modo per bloccare il processo se l'utente annulla l'input.

Un semplice `break` dopo la variabile `input` interromperebbe solo il ciclo più interno. Questo non è sufficiente. I *label* ci vengono in soccorso.

Un *label* ("etichetta") è un identificatore seguito da ":" e da un ciclo:
```js
labelName: for (...) {
  ...
}
```

L'istruzione `break <labelName>` interrompe il ciclo e passa il controllo a *label*.

Come nell'esempio:

```js
outer: for (let i = 0; i < 3; i++) {

  for (let j = 0; j < 3; j++) {

    let input = prompt(`Value at coords (${i},${j})`, '');

    // se si ha una stringa vuota, allora si esce da entrambi i cicli
    if (!input) break outer; // (*)

    // fa qualcosa con i valori...
  }
}
alert('Done!');
```

Nel codice sopra `break outer` interrompe il ciclo e va all'etichetta chiamata `outer`.

Quindi il controllo va da `(*)` a `alert('Done!')`.

Possiamo anche spostare l'etichetta in un'altra linea:

```js
outer:
for (let i = 0; i < 3; i++) { ... }
```

Anche la direttiva `continue` può essere utilizzata con un'etichetta. In questo caso l'esecuzione salta alla prossima iterazione del ciclo con quell'etichetta.


:::: warning I *label* non equivalgono a "goto"
I *label* non permettono di saltare in un punto arbitrario del codice.

Ad esempio, non è possibile:
```js
break label;  // non salta all'etichetta sotto

label: for (...)
```

La direttiva `break` deve essere all'interno del blocco di codice. Tecnicamente l'etichettatura funzionerà con qualsiasi blocco di codice, ad esempio:
```js
label: {
  // ...
  break label; // funziona
  // ...
}
```

...Comunque, nel 99.9% dei casi, `break` viene usato nei cicli, come abbiamo visto negli esempi precedenti.

La chiamata a `continue` è possibile solo dall'interno di un ciclo
::::

## Riepilogo

Abbiamo visto tre tipi di cicli:

- `while` -- La condizione viene controllata prima di ogni iterazione.
- `do..while` -- La condizione viene controllata dopo una prima iterazione.
- `for (;;)` -- La condizione viene controllata prima di ogni iterazione; sono possibili altre condizioni all'interno del ciclo.

Per creare un ciclo infinito, si usa il costrutto `while(true)`. Questo tipo di cicli, come tutti gli altri, possono essere interrotti con la direttiva `break`.

Se non si ha più intenzione di fare nulla nell'iterazione corrente e si vuole quindi saltare alla successiva, possiamo usare la direttiva `continue`.

`break/continue` supportano le etichette prima del ciclo. Un etichetta è l'unico modo per `break/continue` di uscire da cicli annidati ed arrivare ciclo esterno.

## Esercizi

### 1 · Valore all'ultimo ciclo

Qual è l'ultimo valore mostrato da *alert* in questo codice? Perché?

```js
let i = 3;

while (i) {
  alert( i-- );
}
```

::::: details Soluzione

La risposta è: `1`.

```js
let i = 3;

while (i) {
  alert( i-- );
}
```

Ogni iterazione del ciclo decrementa `i` di `1`. Il controllo `while(i)` interrompe il ciclo quando `i = 0`.

Quindi, gli step del ciclo sono ("loop unrolled"):

```js
let i = 3;

alert(i--); //mostra 3, decrementa i a 2

alert(i--) // mostra 2, decrementa i a 1

alert(i--) // mostra 1, decrementa i a 0

// finito, `i` è ora 0, che convertito a booleano è falso
```

:::::

### 2 · Quali valori mostrerà il ciclo while?

Per ogni iterazione del ciclo, scrivi quali valori verranno mostrati e poi confrontali con la soluzione.

Entrambi i cicli mostreranno gli stessi valori in `alert`, o no?

1. La forma prefissa `++i`:

    ```js
    let i = 0;
    while (++i < 5) alert( i );
    ```
2. La forma postfissa `i++`

    ```js
    let i = 0;
    while (i++ < 5) alert( i );
    ```

::::: details Soluzione

L'esercizio dimostrava come le forme prefissa/postfissa possono portare a risultati differenti.

1. **Da 1 a 4**

    ```js
    let i = 0;
    while (++i < 5) alert( i );
    ```

    Il primo valore è `i = 1`, perchè `++i` incrementa prima `i` e poi ritorna il nuovo valore. Quindi il primo confronto è `1 < 5` e `alert` mostra `1`.

    Poi seguono `2, 3, 4…` -- i valori vengono mostrati uno dopo l'altro. Il confronto utilizza sempre il valore incrementato, perchè `++` è posto prima della variabile.

    Ultima iterazione, `i = 4` viene incrementato a `5`, il confronto `while(5 < 5)` risulta `false`, e il ciclo termina. `5` non viene mostrato.

2. **Da 1 a 5**

    ```js
    let i = 0;
    while (i++ < 5) alert( i );
    ```

    Il primo valore è ancora `i = 1`. La forma postfissa `i++` incrementa `i` e ritorna il *vecchio* valore, quindi il confronto `i++ < 5` utilizza `i = 0` (a differenza di `++i < 5`).

    La chiamata ad `alert` è separata. E' un istruzione che viene eseguita dopo l'incremento di `i` e il controllo della condizione. Quindi `i = 1`.

    Seguono `2, 3, 4…`

    Fermiamoci a `i = 4`. La forma prefissa `++i` incrementerebbe ed utilizzerebbe `5` nel controllo della condizione `i < 5`. Qui però stiamo usando la forma postfissa `i++`. Quindi incrementa `i`a `5`, ma ritorna il vecchio valore. Il confronto è dunque `while(4 < 5)` -- vero; il controllo passa alla chiamata `alert`.

    Il valore `i = 5` è l'ultimo, perchè nell'iterazione successiva avremmo `while(5 < 5)` e la condizione sarebbe falsa.

:::::

### 3 · Quali valori verranno mostrati dal ciclo "for"?

Per ogni ciclo scrivete quali valori verranno mostrati. Poi confrontateli con la soluzione.

I due `alert` mostreranno gli stessi valori?

1. Forma postfissa:

    ```js
    for (let i = 0; i < 5; i++) alert( i );
    ```
2. Forma prefissa:

    ```js
    for (let i = 0; i < 5; ++i) alert( i );
    ```

::::: details Soluzione

**La risposta: da `0` a `4` in entrambi i casi.**

```js
for (let i = 0; i < 5; ++i) alert( i );

for (let i = 0; i < 5; i++) alert( i );
```

Questo può essere facilmente dedotto dall'algoritmo  `for`:

1. Esegue come prima cosa `i = 0` (una sola volta)
2. Verifica la condizione `i < 5`
3. Se è `true` -- esegue il corpo del ciclo, dove si trova `alert(i)`, poi incrementa `i` di 1

L'incremento `i++` è separato dal controllo della condizione(2). E' un'istruzione differente.

Il valore ritornato non viene utilizzato, quindi non c'è differenza tra `i++` e `++i`.

:::::

### 4 · Mostra i numeri pari con un ciclo 'for'

Utilizzate il ciclo `for` per mostrare i numeri pari da `2` a `10`.

[Apri l’esempio nella fonte originale](https://it.javascript.info/while-for).

::::: details Soluzione

```js
for (let i = 2; i <= 10; i++) {
  if (i % 2 == 0) {
    alert( i );
  }
}
```

Utilizziamo l'operatore modulo `%` per controllare che un numero sia pari.

:::::

### 5 · Sostituisci "for" con "while"

Riscrivi il ciclo `for` utilizzando la sintassi `while`, ma senza alterarne la funzionalità (l'output deve rimanere lo stesso).

```js
for (let i = 0; i < 3; i++) {
  alert( `number ${i}!` );
}
```

::::: details Soluzione

```js
let i = 0;
while (i < 3) {
  alert( `number ${i}!` );
  i++;
}
```

:::::

### 6 · Ripeti fino a quando l'input è corretto 

Scrivi un ciclo che richieda (tramite *prompt*) un numero maggiore di `100`. Se l'utente inserisce un numero non valido -- chiedete di inserirlo nuovamente.

Il ciclo deve continuare a richiede un numero fintanto che l'utente non inserisce un numero maggiore di `100`, oppure annulla l'input (sia premendo *cancel* che inserendo una riga vuota).

Possiamo assumere che l'utente inserisca solo numeri. Non c'è quindi bisogno di implementare alcun tipo di logica per un input di tipo non numerico.

[Apri l’esempio nella fonte originale](https://it.javascript.info/while-for).

::::: details Soluzione

```js
let num;

do {
  num = prompt("Enter a number greater than 100?", 0);
} while (num <= 100 && num);
```

Il ciclo `do..while` si ripete fintanto che entrambe le condizioni non risultano vere:

1. Il controllo `num <= 100` -- controlla se il valore non risulti ancora maggiore di `100`.
2. Il controllo `&& num` diventa falso quando `num` è `null` o una stringa. Quindi il ciclo `while` termina.

P.S. Se `num` è `null` allora la condizione `num <= 100` è `true`, quindi senza la seconda condizione il ciclo non terminerebbe nel caso in cui l'utente prema CANCEL. Entrambe le condizioni sono necessarie.

:::::

### 7 · Mostra i numeri primi

Un valore intero maggiore di `1` si definisce [primo](https://it.wikipedia.org/wiki/Numero_primo) se non può essere diviso, senza [resto](https://it.wikipedia.org/wiki/Resto), da nessun numero ad eccezione di `1` e se stesso.

In altre parole, `n > 1` è primo se non può essere diviso da nessun altro numero ad eccezione di `1` e `n`.

Ad esempio, `5` è primo perchè non può essere diviso senza resto da `2`, `3` o `4`.

**scrivi un codice che mostri i numeri primi nell'intervallo da `2` a `n`.**

Per `n = 10` il risultato sarà `2,3,5,7`.

P.S. Il codice dovrebbe funzionare per qualsiasi numero `n`, non solo per un valore numerico prefissato.

::::: details Soluzione

Ci sono diversi possibili algoritmi per il nostro scopo.

Usiamo un ciclo annidato:

```js
For each i in the interval {
  check if i has a divisor from 1..i
  if yes => the value is not a prime
  if no => the value is a prime, show it
}
```

Il codice usa un'etichetta:

```js
let n = 10;

nextPrime:
for (let i = 2; i <= n; i++) { // per ogni i...

  for (let j = 2; j < i; j++) { // controlla i suoi divisori..
    if (i % j == 0) continue nextPrime; // se è divisibile per uno di essi, non è un numero primo; passa a prossima iterazione
  }

  alert( i ); // un numero primo
}
```

Ci sono molti modi per ottimizzare questo algoritmo. Ad esempio, potremmo controllare i divisori di `2` fino alla radice di `i`. In ogni caso, se vogliamo essere veramete efficenti su grandi intervalli, abbiamo bisogno di cambiare approcio ed affidarci ad algoritmi matematici più avanzati e complessi, come [Quadratic sieve](https://en.wikipedia.org/wiki/Quadratic_sieve), [General number field sieve](https://en.wikipedia.org/wiki/General_number_field_sieve) etc.

:::::

