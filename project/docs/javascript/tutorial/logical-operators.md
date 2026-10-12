---
title: "Operatori logici"
description: "JavaScript.info in italiano: Operatori logici"
sourceTutorial: true
prev: {"text": "Operatori condizionali: if, '?'", "link": "/javascript/tutorial/ifelse"}
next: {"text": "Nullish coalescing operator '??'", "link": "/javascript/tutorial/nullish-coalescing-operator"}
---

# Operatori logici

> **JavaScript.info · Ilya Kantor e contributori.** [Originale inglese](https://javascript.info/logical-operators) · [Edizione italiana](https://it.javascript.info/logical-operators) · [Fonti e licenza](/javascript/fonti).

In JavaScript ci sono quattro operatori logici: `||` (OR), `&&` (AND), e `!` (NOT), `??` (Nullish Coalescing). Qui abbiamo trattato i primi tre, l'operatore `??` sarà approfondito nel prossimo articolo. 

Nonostante si chiamino "logici", possono essere applicati a valori di qualsiasi tipo, non solo ai booleani (i risultati stessi possono essere di qualunque tipo).

Vediamoli nei dettagli.

## || (OR)

L'operatore "OR" viene rappresentato da due linee verticali:

```js
result = a || b;
```

Nella programmazione classica, l'OR logico è utilizzato per manipolare solo tipi booleani. Se almeno un argomento è `true`, allora il risultato sarà `true`, altrimenti sarà `false`.

In JavaScript questo operatore è un po' più potente. Ma prima vediamo come si comporta con i valori booleani.

Ci sono quattro combinazioni logiche possibili:

```js
alert( true || true );   // true
alert( false || true );  // true
alert( true || false );  // true
alert( false || false ); // false
```

Come possiamo vedere, il risultato è sempre `true`, tranne nei casi in cui entrambi gli operandi sono `false`.

Se un operando non è di tipo booleano, allora viene momentaneamente convertito per la valutazione.

Ad esempio, il numero `1` viene considerato come `true`, il numero `0` come `false`:

```js
if (1 || 0) { // funziona proprio come ( true || false )
  alert( 'truthy!' );
}
```

La maggior parte delle volte, OR `||` viene utilizzato in un `if` per verificare se *almeno una* delle condizioni è vera.

Ad esempio:

```js
let hour = 9;


if (hour < 10 || hour > 18) {

  alert( 'The office is closed.' );
}
```

Possiamo passare molteplici condizioni:

```js
let hour = 12;
let isWeekend = true;

if (hour < 10 || hour > 18 || isWeekend) {
  alert( 'The office is closed.' ); // l'Ufficio è chiuso
}
```

## OR "||" trova il primo valore vero
La logica descritta sopra è ovvia. Adesso proviamo ad addentrarci in qualche caratteristica "extra" di JavaScript.

Si può estendere l'algoritmo come segue.

Dati svariati operandi: 

```js
result = value1 || value2 || value3;
```

L'operatore OR `||` si comporta come segue:

- Valuta gli operandi da sinistra a destra.
- Ogni operando viene convertito a booleano. Se il risultato è `true`, il logical OR si ferma e ritorna il valore originale dell'operando.
- Se tutti gli operandi sono stati valutati e nessuno è `true`, ritorna l'ultimo operando.

Un valore viene ritornato nella sua forma originale, non nella sua conversione booleana.

In altre parole, una catena di OR `"||"` ritorna il primo valore vero; se invece non ce ne sono ritorna l'ultimo valore.

Ad esempio:

```js
alert( 1 || 0 ); // 1 (1 è vero)

alert( null || 1 ); // 1 (1 è il primo valore true)
alert( null || 0 || 1 ); // 1 (il primo valore true)

alert( undefined || null || 0 ); // 0 (tutti falsi, ritorna l'ultimo valore)
```

Questo ci permette alcuni utilizzi interessanti rispetto al "puro e classico OR booleano"boolean-only OR".

1. **Trovare il primo valore vero in una lista di variabili o espressioni.**

    Immaginiamo di avere diverse variabili, `firstName`, `lastName` e `nickName`, tutte opzionali (possono quindi essere *undefined* o avere valori falsi).

    Possiamo utilizzare OR `||` per selezionare quella che contiene un valore e mostrarlo (oppure mostrare `"Anonymous"` se nessuna variabile è definita):

    ```js
    let firstName = "";
    let lastName = "";
    let nickName = "SuperCoder";

    
    alert( firstName || lastName || nickName || "Anonymous"); // SuperCoder
    
    ```

    Se tutte le variabili sono false, verrà mostrato `"Anonymous"`.

2. **Valutazione a Corto-Circuito.**

    Gli operandi, oltre che valori, possono essere anche espressioni arbitrarie. L'operatore OR esegue la valutazione da sinistra a destra e si ferma al primo risultato vero, il quale viene ritornato. Il processo è chiamato "valutazione a corto-circuito" perché cerca di concludersi il prima possibile, senza dover elaborare tutti gli operandi. 

    Il logical OR è particolarmente utile quando il secondo argomento causerebbe un *side-effect* come l'assegnazione di una variabile o la chiamata a una funzione.
    Nell'esempio che segue solo il secondo messaggio verrà mostrato. 

    ```js
    true || alert("not printed");
    false || alert("printed");
    ```
   Nella prima linea l'operatore OR trova subito un valore vero e ferma immediatamente la valutazione, quindi *alert* non viene eseguito.
   Si può utilizzare questa funzionalità per eseguire un commando nel caso in cui la prima parte della condizione sia falsa. 

## && (AND)

L'operatore AND viene rappresentato con `&&`:

```js
result = a && b;
```

Nella programmazione classica AND ritorna `true` se entrambi gli operandi sono veri, altrimenti ritorna `false`:

```js
alert( true && true );   // true
alert( false && true );  // false
alert( true && false );  // false
alert( false && false ); // false
```

Un esempio con `if`:

```js
let hour = 12;
let minute = 30;

if (hour == 12 && minute == 30) {
  alert( 'The time is 12:30' );
}
```

Proprio come per OR, anche per AND è consentito qualsiasi valore come operando:

```js
if (1 && 0) { // valutato come true && false
  alert( "won't work, because the result is falsy" );
}
```


## AND "&&" trova il primo valore falso

Dati svariati operandi:

```js
result = value1 && value2 && value3;
```

L'operatore AND `&&` si comporta come segue:

- Valuta gli operandi da sinistra a destra.
- Ogni operando viene convertito a booleano. Se il risultato è `false`, si ferma e ritorna il valore originale dell'operando.
- Se tutti gli operandi precedenti sono stati valutati e nessuno è `false`, ritorna l'ultimo operando.

In altre parole, AND ritorna il primo valore falso, altrimenti ritorna l'ultimo valore.

Le regole sono molto simili a quelle dell'OR. La differenza è che AND ritorna il primo valore *falso* mentre OR ritorna il primo valore *vero*.

Esempi:

```js
// se il primo operando è vero,
// AND ritorna il secondo operando:
alert( 1 && 0 ); // 0
alert( 1 && 5 ); // 5

// se il primo operando è falso
// AND lo ritorna. Il secondo operando viene ignorato
alert( null && 5 ); // null
alert( 0 && "no matter what" ); // 0
```

Possiamo anche passare diversi valori in una sola riga. Nota come il primo valore falso viene ritornato non appena raggiunto:

```js
alert( 1 && 2 && null && 3 ); // null
```

Quando tutti i valori sono veri, viene ritornato l'ultimo valore:

```js
alert( 1 && 2 && 3 ); // 3, l'ultimo
```


:::: tip Precedenza di AND `&&` è maggiore dell'OR `||`
La precedenza dell'operatore AND `&&` è maggiore di quella dell'OR `||`.

Quindi il codice `a && b || c && d` è analogo all'espressione: `(a && b) || (c && d)`.
::::


:::: warning Non rimpiazzate `if` con `||` o `&&`
Talvolta, le persone utilizzano l'operatore AND `&&` come una "scorciatoia" dell'espressione `if`".
Proprio come l'OR, anche AND `&&` può qualche volta rimpiazzare `if`.

Ad esempio:

```js
let x = 1;

(x > 0) && alert( 'Greater than zero!' );
```

Le azioni nella parte destra di `&&` vengono eseguite solamente se la valutazione non si ferma prima. Cioè: solo se `(x > 0)` è vera.

Il codice sopra è sostanzialmente analogo a:

```js
let x = 1;

if (x > 0) alert( 'Greater than zero!' );
```

La variante con `&&` sembra essere più corta. Ma l'istruzione `if` è più ovvia e tende ad essere più leggibile.

Quindi è consigliato usare ogni costrutto solo per i suoi scopi. Usate un `if` se volete imporre una condizione. Utilizzate invece `&&` se volete un AND.
::::

## ! (NOT)

L'operatore booleano NOT viene rappresentato dal punto esclamativo `!`.

La sintassi è piuttosto semplice:

```js
result = !value;
```

L'operatore accetta un solo argomento e si comporta come segue:

1. Converte l'operando a booleano: `true/false`.
2. Ritorna il valore inverso.

Ad esempio:

```js
alert( !true ); // false
alert( !0 ); // true
```

Un doppio NOT `!!` viene talvolta utilizzato per convertire un valore al tipo booleano:

```js
alert( !!"non-empty string" ); // true
alert( !!null ); // false
```

Quello che accade è che il primo NOT converte l'operando a booleano e ritorna il suo inverso, e il secondo NOT lo *inverte nuovamente*. Il risultato è un valore di tipo booleano.

C'è un modo molto più lungo per fare la stessa cosa, usare la funzione `Boolean`, integrata in JavaScript:

```js
alert( Boolean("non-empty string") ); // true
alert( Boolean(null) ); // false
```

La precedenza del NOT `!` è la più alta fra tutti gli operatori logici; viene sempre eseguita per prima e precede sia `&&` che `||`.

## Esercizi

### 1 · Qual è il risultato dell'OR?

Quale sarà il risultato del codice sotto?

```js
alert( null || 2 || undefined );
```

::::: details Soluzione

La risposta è `2`, questo è il primo valore vero.

```js
alert( null || 2 || undefined );
```

:::::

### 2 · Qual è il risultato dell'alert con l'OR?

Cosa mostrerà il codice sotto?

```js
alert( alert(1) || 2 || alert(3) );
```

::::: details Soluzione

La risposta: prima `1`, poi `2`.

```js
alert( alert(1) || 2 || alert(3) );
```

La chiamata ad `alert` non ritorna alcun valore; ossia `undefined`.

1. Il primo OR `||` valuta l'operando sinistro `alert(1)`. Questo mostra il primo messaggio, `1`.
2. La funzione `alert` ritorna `undefined`, quindi OR prosegue con il secondo operando, alla ricerca di un valore vero.
3. Il secondo operando `2` è vero; quindi l'esecuzione si ferma, viene ritornato `2` e mostrato dall'alert esterno.

Non ci sarà il `3`, perchè la valutazione non arriva a `alert(3)`.

:::::

### 3 · Qual è il risultato dell'AND?

Cosa mostrerà l'esecuzione di questo codice?

```js
alert( 1 && null && 2 );
```

::::: details Soluzione

La risposta è: `null`, perchè è il primo valore falso nella lista.

```js
alert( 1 && null && 2 );
```

:::::

### 4 · Qual è il risultato degli alert?

Cosa mostrerà questo codice?

```js
alert( alert(1) && alert(2) );
```

::::: details Soluzione

La risposta è: `1`, e poi `undefined`.

```js
alert( alert(1) && alert(2) );
```

La chiamata `alert` ritorna `undefined` (mostra solo un messaggio, quindi non ha nessuna valore significativo di ritorno).

Per questo `&&`, valutato l'operando di sinistra (che mostra `1`), si ferma: `undefined` è un valore falso e `&&` lo ritorna immediatamente.

:::::

### 5 · Il risultato di OR AND OR

Cosa verrà mostrato?

```js
alert( null || 2 && 3 || 4 );
```

::::: details Soluzione

La risposta è: `3`.

```js
alert( null || 2 && 3 || 4 );
```

La precedenza di AND `&&` è maggiore di `||`, quindi verrà eseguito per primo.

Il risultato di `2 && 3 = 3`, quindi l'espressione diventa:

```
null || 3 || 4
```

Adesso il risultato è il primo valore vero: `3`.

:::::

### 6 · Controlla l'intervallo

Scrivi una condizione `if` per controllare che `age` sia compresa tra `14` e `90` estremi inclusi.

"Inclusi" significa che `age` può valere anche `14` o `90`.

::::: details Soluzione

```js
if (age >= 14 && age <= 90)
```

:::::

### 7 · Controlla l'intervallo fuori

Scrivi una condizione `if` che controlli la variabile `age`; questa NON deve essere compresa tra `14` e `90` (inclusi).

Scrivi due varianti: la prima utilizzando NOT `!`, la seconda -- senza.

::::: details Soluzione

La prima variante:

```js
if (!(age >= 14 && age <= 90))
```

La seconda variante:

```js
if (age < 14 || age > 90)
```

:::::

### 8 · Un indovinello con "if"

Quali di questi `alert` verranno eseguiti?

Quale sarà il risultato delle espressioni all'interno dei vari `if(...)`?

```js
if (-1 || 0) alert( 'first' );
if (-1 && 0) alert( 'second' );
if (null || -1 && 1) alert( 'third' );
```

::::: details Soluzione

La risposta: il primo e il terzo verranno eseguiti.

I dettagli:

```js
// Viene eseguito
// Il risultato di -1 || 0 = -1 è vero
if (-1 || 0) alert( 'first' );

// Non viene eseguito
// -1 && 0 = 0, falso
if (-1 && 0) alert( 'second' );

// Eseguito
// L'operatore && ha la precedenza su ||,
// quindi -1 && 1 vengono eseguiti per primi; la catena dentro `if` diventa:
// null || -1 && 1  ->  null || 1  ->  1
if (null || -1 && 1) alert( 'third' );
```

:::::

### 9 · Controlla il login

Scrivi il codice che richiede un login tramite `prompt`.

Se l'utente digita `"Admin"`, si richiede una password tramite `prompt`; se l'input è una stringa vuota o `key:Esc` -- mostra "Canceled."; se  è diversa da `"Admin"`, mostra "I don't know you".

La passoword viene controllata secondo i seguenti criteri:

- Se è uguale a "TheMaster", mostra "Welcome!",
- Un stringa diversa da "TheMaster" -- mostra "Wrong password",
- Una stringa vuota o `key:Esc` -- mostra "Canceled."

Lo schema:

![](/javascript-info/1-js/02-first-steps/11-logical-operators/9-check-login/ifelse_task.svg)

Utilizza blocchi `if` annidati e tieni a mente la leggibilità del codice.

Suggerimento: passare un input vuoto tramite prompt ritorna una stringa vuota `''`. Premere `key:ESC` metre il prompt è aperto ritorna `null`.

[Apri l’esempio nella fonte originale](https://it.javascript.info/logical-operators).

::::: details Soluzione

```js
let userName = prompt("Who's there?", '');

if (userName === 'Admin') {

  let pass = prompt('Password?', '');

  if (pass === 'TheMaster') {
    alert( 'Welcome!' );
  } else if (pass === '' || pass === null) {
    alert( 'Canceled' );
  } else {
    alert( 'Wrong password' );
  }

} else if (userName === '' || userName === null) {
  alert( 'Canceled' );
} else {
  alert( "I don't know you" );
}
```

Nota l'indentazione vericale all'interno del blocco `if`. Tecnicamente non è richiesto, ma rende il codice molto più leggibile.

:::::

