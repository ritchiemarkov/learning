---
title: "Il tipo Reference"
description: "JavaScript.info in italiano: Il tipo Reference"
sourceTutorial: true
prev: {"text": "Currying", "link": "/javascript/tutorial/currying-partials"}
next: {"text": "BigInt", "link": "/javascript/tutorial/bigint"}
---

# Il tipo Reference

> **JavaScript.info · Ilya Kantor e contributori.** [Originale inglese](https://javascript.info/reference-type) · [Edizione italiana](https://it.javascript.info/reference-type) · [Fonti e licenza](/javascript/fonti).

::: warning Caratteristica avanzata di linguaggio
Questo articolo tratta un argomento avanzato, utile per capire meglio alcuni casi limite.

Non è di fondamentale importanza. Molti sviluppatori esperti vivono bene senza esserne a conoscenza. Continua la lettura se sei interessato a sapere come funzionano le cose internamente.
:::

Un'invocazione di un metodo valutata dinamicamente può perdere il `this`.

Ad esempio:

```js
let user = {
  name: "John",
  hi() { alert(this.name); },
  bye() { alert("Bye"); }
};

user.hi(); // funziona

// ora invochiamo user.hi o user.bye in base al nome

(user.name == "John" ? user.hi : user.bye)(); // Errore!

```

Nell'ultima riga abbiamo un operatore condizionale che sceglie tra `user.hi` o `user.bye`. In questo caso il risultato è `user.hi`.

Successivamente il metodo viene invocato immediatamente con le parentesi `()`. Ma non funziona correttamente!

Come potete vedere, l'invocazione genera un errore, perché il valore di `"this"` all'interno della chiamata diventa `undefined`.

Questo invece funziona (object punto metodo):
```js
user.hi();
```

Questo no (valutazione del metodo):
```js
(user.name == "John" ? user.hi : user.bye)(); // Errore!
```

Perché? Se vogliamo capire il motivo, dobbiamo addentrarci nei dettagli del funzionamento della chiamata `obj.method()`.

## Il tipo Reference spiegato

Guardando da più vicino, possiamo notare due operazioni nell'istruzione `obj.method()`:

1. Primo, il punto `'.'` recupera la proprietà `obj.method`.
2. Successivamente le parentesi `()` la eseguono.

Quindi, come vengono passate le informazioni riguardo al `this` dalla prima alla seconda parte?

Se spostiamo queste istruzioni in righe separate, allora `this` verrà sicuramente perso:

```js
let user = {
  name: "John",
  hi() { alert(this.name); }
}


// dividiamo l'accesso e l'invocazione in due righe
let hi = user.hi;
hi(); // Errore, perché this è undefined

```

Qui `hi = user.hi` assegna la funzione alla variabile, e nell'ultima riga è completamente autonoma, quindi non si ha alcun `this`.

**Per rendere l'invocazione `user.hi()` funzionante, JavaScript applica un trucco -- il punto `'.'` non ritorna una funzione, ma piuttosto un valore del tipo speciale [Reference](https://tc39.github.io/ecma262/#sec-reference-specification-type).**

Il tipo Reference è un "tipo descritto dalla specifica". Non possiamo utilizzarlo esplicitamente, ma viene utilizzato internamente dal linguaggio.

Il valore del tipo Reference è una combinazione di tre valori `(base, name, strict)`, dove:

- `base` è l'oggetto.
- `name` è il nome della proprietà.
- `strict` vale true se `use strict` è attivo.

Il risultato dell'accesso alla proprietà `user.hi` non è una funzione, ma un valore di tipo Reference. Per `user.hi` in strict mode vale:

```js
// valore di tipo Reference
(user, "hi", true)
```

Quando le parentesi `()` vengono invocate in un tipo Reference, queste ricevono tutte le informazioni riguardo l'oggetto ed il metodo, e possono quindi impostare correttamente il valore di `this` (`=user` in questo caso).

Il tipo Reference è uno speciale tipo "intermedio" utilizzato internamente, con lo scopo di passare le informazioni dal punto `.` all'invocazione con le parentesi `()`.

Qualsiasi altra operazione come un assegnazione `hi = user.hi` scarta completamente il tipo Reference, accede al valore `user.hi` (una funzione) e lo ritorna. Quindi qualsiasi ulteriore operazione "perderà" `this`.

Quindi, come risultato, il valore di `this` viene passato correttamente solo se la funzione viene invocata direttamente utilizzando il punto `obj.method()` o la sintassi con le parentesi quadre `obj['method']()` (in questo caso si equivalgono). Esistono diversi modi per evitare questo problema, come [func.bind()](/javascript/tutorial/bind).

## Riepilogo

Il tipo Reference è un tipo interno del linguaggio.

La lettura di una proprietà, con il punto `.` in `obj.method()` non ritorna esattamente il valore della proprietà, ma uno speciale "tipo reference" che memorizza sia il valore della proprietà che l'oggetto a cui accedere.

Questo accade per consentire che la successiva invocazione con `()` imposti correttamente il `this`.

Per tutte le altre operazioni, il tipo reference diventa automaticamente il valore della proprietà (una funzione nel nostro caso).

Il meccanismo descritto è nascosto ai nostri occhi. Ha importanza solo in alcuni casi, ad esempio quando un metodo viene ottenuto dinamicamente dall'oggetto, utilizzando un'espressione.

## Esercizi

### 1 · Controllo di sintassi

Qual'è il risultato di questo codice?


```js
let user = {
  name: "John",
  go: function() { alert(this.name) }
}

(user.go)()
```

P.S. C'è una trappola :)

::::: details Soluzione

**Errore**!

Provatelo:

```js
let user = {
  name: "John",
  go: function() { alert(this.name) }
}

(user.go)() // error!
```

La maggior parte dei browser non vi darà informazioni necessarie per capire cosa è andato storto.

**L'errore viene causato dalla mancanza di un punto e virgola dopo `user = {...}`.**

JavaScript non inserisce automaticamente un punto e virgola prima di `(user.go)()`, quindi leggerà il codice in questo modo:

```js
let user = { go:... }(user.go)()
```

Possiamo anche vedere questa come una comune espressione, è sintatticamente una chiamata all'oggetto `{ go: ... }` come una funzione con argomento `(user.go)`. E questo avviene nella stessa riga di `let user`, quindi l'oggetto `user` non è ancora stato definito, quindi c'è un errore. 

Se inseriamo un punto e virgola, tutto funziona correttamente:

```js
let user = {
  name: "John",
  go: function() { alert(this.name) }
};

(user.go)() // John
```

Da notare che le parentesi su `(user.go)` non fanno nulla. Solitamente servono ad organizzare l'ordine delle operazioni, in questo  caso è presente un `.` che verrebbe comunque eseguito per primo, non hanno quindi alcun effetto. L'unico errore stava nel punto e virgola.

:::::

### 2 · Spiegate il valore di "this"

Nel codice sotto vogliamo chiamare il metodo `user.go()`  volte di fila.

Ma le chiamate `(1)` e `(2)` funzionano diversamente da `(3)` e `(4)`. Perché?

```js
let obj, method;

obj = {
  go: function() { alert(this); }
};

obj.go();               // (1) [object Object]

(obj.go)();             // (2) [object Object]

(method = obj.go)();    // (3) undefined

(obj.go || obj.stop)(); // (4) undefined
```

::::: details Soluzione

Vediamo la spiegazione.

1. Questa è una normale chiamata ad un metodo dell'oggetto.

2. Stessa cosa, le parentesi non cambiano l'ordine delle operazioni, il punto viene eseguito per primo in ogni caso.

3. Qui abbiamo una chiamata più complessa `(expression).method()`. La chiamata viene interpretata come fosse divisa in due righe:

    ```js
    f = obj.go; // calculate the expression
    f();        // call what we have
    ```

    Qui `f()` viene eseguita come una funzione, senza `this`.

4. Molto simile a `(3)`, alla sinistra del punto `.` abbiamo un espressione.

Per spiegare il comportamento di `(3)` e `(4)` dobbiamo ricordare che la proprietà di accesso (il punto o le parentesi quadre) ritornano un valore di tipo riferimento.  

Qualsiasi operazione tranne la chiamata ad un metodo (come l'assegnazione `=` o `||`) trasforma questo riferimento in un valore oridnario, che non porta più le informazioni necessarie per impostare `this`.

:::::

