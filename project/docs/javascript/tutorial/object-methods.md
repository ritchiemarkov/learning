---
title: "Metodi degli oggetti,\"this\""
description: "JavaScript.info in italiano: Metodi degli oggetti,\"this\""
sourceTutorial: true
prev: {"text": "Garbage collection (\"Spazzatura\")", "link": "/javascript/tutorial/garbage-collection"}
next: {"text": "Costruttore, operatore \"new\"", "link": "/javascript/tutorial/constructor-new"}
---

# Metodi degli oggetti,"this"

> **JavaScript.info · Ilya Kantor e contributori.** [Originale inglese](https://javascript.info/object-methods) · [Edizione italiana](https://it.javascript.info/object-methods) · [Fonti e licenza](/javascript/fonti).

Gli oggetti solitamente vengono creati per rappresentare entità del mondo reale, come utenti, prodotti e molto altro:

```js
let user = {
  name: "John",
  age: 30
};
```

Inoltre, nel mondo reale, un utente può *agire*: selezionare qualcosa dalla lista degli acquisti, effettuare login, logout etc.

In JavaScript le azioni vengono rappresentate tramite le funzioni.

## Esempio di un metodo

Per iniziare, insegniamo a `user` a salutare:

```js
let user = {
  name: "John",
  age: 30
};


user.sayHi = function() {
  alert("Hello!");
};


user.sayHi(); // Hello!
```

Qui abbiamo appena utilizzato un'espressione di funzione per creare una funzione ed assegnarla alla proprietà `user.sayHi` dell'oggetto.

Successivamente possiamo chiamarla. Ora l'utente può parlare!

Una funzione che è una proprietà di un oggetto si chiama *metodo*.

Quindi, nell'esempio abbiamo un metodo `sayHi` dell'oggetto `user`.

Ovviamente possiamo utilizzare una funzione già dichiarata come metodo:

```js
let user = {
  // ...
};


// prima la dichiariamo
function sayHi() {
  alert("Hello!");
};

// poi la aggiungiamo come metodo
user.sayHi = sayHi;


user.sayHi(); // Hello!
```


::: tip Programmazione orientata agli oggetti
Quando scriviamo codice utilizzando gli oggetti per rappresentare le entità, questa viene definita [programmazione orientata agli oggetti](https://en.wikipedia.org/wiki/Object-oriented_programming), in breve: "OOP".

OOP è una grande cosa, un ambito di interesse con i propri studi. Come scegliere le giuste entità? Come organizzare le interazioni tra loro? Questa è l'architettura di un codice, e ci sono molti libri importanti che trattano questo argomento, come "Design Patterns: Elements of Reusable Object-Oriented Software" di E.Gamma, R.Helm, R.Johnson, J.Vissides oppure "Object-Oriented Analysis and Design with Applications" di G.Booch, e molti altri.
:::
### La forma breve dei metodi

Esiste una sintassi più breve per i metodi in un oggetto letterale:

```js
// questi oggetti fanno la stessa cosa

user = {
  sayHi: function() {
    alert("Hello");
  }
};

// la sintassi più breve risulta più carina
user = {

  sayHi() { // equivalente a "sayHi: function(){...}"

    alert("Hello");
  }
};
```

Come possiamo notare, si può omettere `"function"` e scrivere solamente `sayHi()`.

A dire la verità, la notazione non è proprio uguale. Ci sono delle sottili differenze legate all'ereditarietà degli oggetti (le studieremo più avanti), ma per ora non hanno importanza. Nella maggior parte dei casi la forma breve viene preferita.

## "this" nei metodi

E' molto comune che, per eseguire determinate azioni, un metodo abbia necessità di accedere alle informazioni memorizzate nell'oggetto.

Ad esempio, il codice dentro `user.sayHi()` potrebbe aver bisogno del nome dell'`user`.

**Per accedere all'oggetto, un metodo può utilizzare la parola chiave `this`.**

Il valore di `this` è l'oggetto "prima del punto", quello che ha eseguito la chiamata del metodo.

Ad esempio:

```js
let user = {
  name: "John",
  age: 30,

  sayHi() {

    // "this" is the "current object"
    alert(this.name);

  }

};

user.sayHi(); // John
```

In fase di esecuzione, quando viene chiamato il metodo `user.sayHi()`, il valore di `this` sarà `user`.

Tecnicamente, è possibile accedere all'oggetto anche senza `this`; lo si fa tramite riferimento alla variabile esterna:

```js
let user = {
  name: "John",
  age: 30,

  sayHi() {

    alert(user.name); // "user" piuttosto di "this"

  }

};
```

...Questo codice è instabile. Se decidessimo di copiare `user` in un'altra variabile, ad esempio `admin = user` e sovrascrivere `user` con qualcos'altro, verrebbe allora effettuato l'accesso all'oggetto sbagliato.

Dimostriamolo:

```js
let user = {
  name: "John",
  age: 30,

  sayHi() {

    alert( user.name ); // porta ad un errore

  }

};


let admin = user;
user = null; // sovrascriviamo per rendere tutto più ovvio


admin.sayHi(); // Errore: non possiamo leggere la proprietà 'name' di null

```

Se scriviamo `this.name` piuttosto di `user.name` all'interno di `alert`, il codice funzionerà.

## "this" non ha limiti

In JavaScript, la parola chiave "this" si comporta diversamente da come fa in molti altri linguaggi di programmazione. Essa può essere usata in qualsiasi funzione, anche se non si tratta del metodo di un oggetto.

Non c'è alcun errore di sintassi in un codice come questo:

```js
function sayHi() {
  alert( this.name );
}
```

Il valore di `this` viene valutato al momento dell'esecuzione. E può essere un valore qualsiasi.

Ad esempio, la stessa funzione potrebbe avere diversi "this" quando viene chiamata da oggetti diversi:

```js
let user = { name: "John" };
let admin = { name: "Admin" };

function sayHi() {
  alert( this.name );
}


// utilizziamo la stessa funzione su due oggetti
user.f = sayHi;
admin.f = sayHi;


// queste chiamate hanno un this diverso
// "this" all'interno della funzione è riferito all'oggetto "prima del punto"
user.f(); // John  (this == user)
admin.f(); // Admin  (this == admin)

admin['f'](); // Admin (il punto o le parentesi quadre forniscono entrambi accesso ai metodi - non c'è differenza)
```

La regola è semplice: se viene chiamato `obj.f()`, allora, durante la chiamata di `f`, `this` si riferisce a `obj`. Nell'esempio sopra assume il valore sia di `user` che di `admin`.


:::: tip Invocazione senza un oggetto: `this == undefined`
Possiamo anche chiamare la funzione senza un oggetto:

```js
function sayHi() {
  alert(this);
}

sayHi(); // undefined
```

In questo caso `this`  è `undefined` in modalità strict. Se tentiamo di accedere a `this.name`, ci sarà un errore.

Se non è attiva la modalità *strict* il valore di `this` in questo caso sarà *l'oggetto globale* (`window` in un browser, lo studieremo più avanti nel capitolo [](/javascript/tutorial/global-object)). Questo strano comportamento ha delle motivazioni storiche, che `"use strict"` risolve.

Solitamente questo tipo di chiamate significano un errore di programmazione. Se c'è un `this` all'interno di una funzione, ci si aspetta che sia chiamato da un oggetto.
::::


::: tip Le conseguenze della libertà di `this`
Se avete utilizzato altri linguaggi di programmazione, probabilmente sarete abituati all'idea di un "`this` limitato": quando viene definito un metodo in un oggetto, questo avrà sempre in `this` il riferimento all'oggetto.

In JavaScript `this` è "libero", il suo valore viene calcolato durante l'esecuzione e non dipende da dove il metodo è stato definito, ma piuttosto dall'oggetto "prima del punto".

Il concetto di valutare `this` durante l'esecuzione ha i suoi pregi e difetti. Da una parte una funzione può essere riutilizzata per oggetti diversi, dall'altra questa grande flessibilità può essere fonte di molti errori.

Il nostro scopo non è di giudicare se questa caratteristica del linguaggio sia buona o cattiva, ma di capire come lavorare con essa sfruttandone i benefici ed evitando i problemi.
:::

## Le arrow functions non hanno "this"

Ad esempio, qui `arrow()` usa `this` preso dal metodo esterno `user.sayHi()`:

```js
let user = {
  firstName: "Ilya",
  sayHi() {
    let arrow = () => alert(this.firstName);
    arrow();
  }
};

user.sayHi(); // Ilya
```

Questa è una speciale caratteristica delle arrow functions; è utile quando non vogliamo avere un ulteriore `this`, ma utilizzare quello del contesto esterno. Più avanti nel capitolo [Arrow functions rivisitate](/javascript/tutorial/arrow-functions) studieremo più in dettaglio le arrow functions.


## Riepilogo

- Le funzioni che vengono memorizzate come proprietà di un oggetto vengono dette "metodi".
- I metodi consentono agli oggetti di "agire", come `object.doSomething()`.
- I metodi possono riferirsi all'oggetto tramite `this`.

Il valore `this` viene definito durante l'esecuzione (run-time).
- Quando una funzione viene dichiarata, può utilizzare `this`, ma questo `this` non avrà alcun valore fino a che la funzione non verrà chiamata.
- Una funzione può essere copiata in vari oggetti.
- Quando una funzione viene chiamata come "metodo": `object.method()`, il valore di `this` durante la chiamata si riferisce a `object`.

Da notare che le arrow functions sono speciali: non hanno `this`. Quando si prova ad accedere a `this` in una funzione freccia, questo verrà preso dal contesto esterno.

## Esercizi

### 1 · Utilizzare "this" in un oggetto letterale

Qui la funzione `makeUser` ritorna un oggetto.

Qual è il risultato dell'accesso a `ref`? Perché?

```js
function makeUser() {
  return {
    name: "John",
    ref: this
  };
}

let user = makeUser();

alert( user.ref.name ); //Qual è il risultato?
```

::::: details Soluzione

**Risposta: un errore.**

Provate:
```js
function makeUser() {
  return {
    name: "John",
    ref: this
  };
}

let user = makeUser();

alert( user.ref.name ); // Error: Cannot read property 'name' of undefined
```

Questo avviene perché le regole che impostano `this` non guardano agli oggetti letterali. 

Qui il valore di `this` dentro `makeUser()` è `undefined`, perché viene chiamato dentro una funzione, non un metodo.

Gli oggetti letterali non hanno alcun effetto su `this`. Il valore di `this` è unico per tutta la funzione, quindi i blocchi di codice e gli oggetti letterali che vi si trovano dentro non hanno alcuna importanza.

Quindi `ref: this` prende il `this` della funzione.

Possiamo riscrivere la funzione e ritornare lo stesso `this` con valore `undefined`: 

```js
function makeUser(){
  return this; // questa volta non c'e' un oggetto letterale
}

alert( makeUser().name ); // Error: Cannot read property 'name' of undefined
```
Come possiamo vedere, il risultato di  `alert( makeUser().name )` è lo stesso di `alert( user.ref.name )` nell'esempio precedente.

Qui abbiamo il caso opposto:

```js
function makeUser() {
  return {
    name: "John",

    ref() {
      return this;
    }

  };
}

let user = makeUser();

alert( user.ref().name ); // John
```

Ora funziona, perché `user.ref()` è un metodo. E il valore di `this` si riferisce all'oggetto prima del punto `.`.

:::::

### 2 · Create una calcolatrice

Create un oggetto `calculator` con tre metodi:

- `read()` richiede tramite prompt due valori e li salva come proprietà dell'oggetto.
- `sum()` ritorna la somma dei valori salvati.
- `mul()` moltiplica i valori salvati e ritorna il risultato.

```js
let calculator = {
  // ... your code ...
};

calculator.read();
alert( calculator.sum() );
alert( calculator.mul() );
```

[Apri l’esempio nella fonte originale](https://it.javascript.info/object-methods).

::::: details Soluzione

```js
let calculator = {
  sum() {
    return this.a + this.b;
  },

  mul() {
    return this.a * this.b;
  },

  read() {
    this.a = +prompt('a?', 0);
    this.b = +prompt('b?', 0);
  }
};

calculator.read();
alert( calculator.sum() );
alert( calculator.mul() );
```

:::::

### 3 · Concatenazione

Qui abbiamo un oggetto `ladder` che ci consente di salire e scendere:

```js
let ladder = {
  step: 0,
  up() { 
    this.step++;
  },
  down() { 
    this.step--;
  },
  showStep: function() { // shows the current step
    alert( this.step );
  }
};
```

Ora, se abbiamo bisogno di eseguire più chiamate in sequenza, possiamo:

```js
ladder.up();
ladder.up();
ladder.down();
ladder.showStep(); // 1
ladder.down();
ladder.showStep(); // 0
```

Modificare il codice di `up`, `down` e `showStep` per rendere le chiamate concatenabili, come in questo esempio:

```js
ladder.up().up().down().showStep().down().showStep(); // shows 1 then 0
```

Questo approccio è largamente utilizzato dalle librerie JavaScript.

::::: details Soluzione

La soluzione sta nel ritornare l'oggetto stesso ad ogni chiamata.

```js
let ladder = {
  step: 0,
  up() {
    this.step++;

    return this;

  },
  down() {
    this.step--;

    return this;

  },
  showStep() {
    alert( this.step );

    return this;

  }
};

ladder.up().up().down().showStep().down().showStep(); // shows 1 then 0
```

Possiamo anche scrivere una singola chiamata per riga. Per catene molto lunghe diventa più leggibile:

```js
ladder
  .up()
  .up()
  .down()
  .showStep() // 1
  .down()
  .showStep(); // 0
```

:::::

