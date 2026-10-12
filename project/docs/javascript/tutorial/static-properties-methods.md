---
title: "Proprietà e metodi statici"
description: "JavaScript.info in italiano: Proprietà e metodi statici"
sourceTutorial: true
prev: {"text": "Ereditarietà delle classi", "link": "/javascript/tutorial/class-inheritance"}
next: {"text": "Proprietà e metodi privati e protetti", "link": "/javascript/tutorial/private-protected-properties-methods"}
---

# Proprietà e metodi statici

> **JavaScript.info · Ilya Kantor e contributori.** [Originale inglese](https://javascript.info/static-properties-methods) · [Edizione italiana](https://it.javascript.info/static-properties-methods) · [Fonti e licenza](/javascript/fonti).

Possiamo anche assegnare metodi alle classi stesse, non solamente al loro `"prototype"`. Questi metodi sono detti *statici*.

All'interno della classe, questi vengono preceduti dalla keyword `static`, come possiamo vedere nell'esempio:

```js
class User {

  static staticMethod() {

    alert(this === User);
  }
}

User.staticMethod(); // true
```

Questo avrà lo stesso effetto di assegnarla direttamente come proprietà:

```js
class User { }

User.staticMethod = function() {
  alert(this === User);
};

User.staticMethod(); // true
```

Il valore di `this` nella chiamata `User.staticMethod()` è rappresentato dal costruttore dell classe `User` (la regola dell' "oggetto prima del punto").

Solitamente, i metodi statici vengono utilizzati per rappresentare funzioni che appartengono alla classe, ma non ad un oggetto in particolare.

Ad esempio, potremmo avere degli oggetti di tipo `Article` e necessitare di una funzione per confrontarli. Una soluzione naturale sarebbe quella di aggiungere il metodo `Article.compare`, come nell'esempio:

```js
class Article {
  constructor(title, date) {
    this.title = title;
    this.date = date;
  }


  static compare(articleA, articleB) {
    return articleA.date - articleB.date;
  }

}

// usage
let articles = [
  new Article("HTML", new Date(2019, 1, 1)),
  new Article("CSS", new Date(2019, 0, 1)),
  new Article("JavaScript", new Date(2019, 11, 1))
];


articles.sort(Article.compare);


alert( articles[0].title ); // CSS
```

Qui `Article.compare` sta "al di sopra" degli articoli, poiché ha lo scopo di confrontarli. Non è un metodo di un articolo, ma piuttosto dell'intera classe.

Un altro esempio comune è quello del "factory method" (un particolare design pattern). Immaginiamo di avere bisogno di diverse modalità di creazione di un articolo:

1. Creazione con i parametri forniti (`title`, `date` etc).
2. Creazione di un articolo vuoto con la data di oggi.
3. ...o qualsiasi altra modalità.

Il primo metodo può essere implementato tramite il costruttore. Mentre per il secondo, possiamo creare un metodo statico appartenente alla classe.

Come `Article.createTodays()` nell'esempio:

```js
class Article {
  constructor(title, date) {
    this.title = title;
    this.date = date;
  }


  static createTodays() {
    // ricorda, this = Article
    return new this("Today's digest", new Date());
  }

}

let article = Article.createTodays();

alert( article.title ); // Today's digest
```

Ora, ogni volta in cui avremo bisogno di crare un "today's digest", possiamo invocare `Article.createTodays()`. Ripetiamolo nuovamente, questo non è un metodo per uno specifico articolo, ma piuttosto un metodo dell'intera classe.

I metodi statici vengono utilizzati anche nelle classi database-related (relative a database), per poter cercare/salvare/rimuovere elementi dal database, come nell'esempio:

```js
// assumiamo che Article sia una classe speciale per la gestione degli articoli
// metodo statico per la rimozione di un articolo:
Article.remove({id: 12345});
```

## Proprietà statiche

[recent browser=Chrome]

E' anche possibile definire proprietà statiche, queste sono molto simili alle proprietà della classe, ma sono precedute dalla keyword `static`:

```js
class Article {
  static publisher = "Ilya Kantor";
}

alert( Article.publisher ); // Ilya Kantor
```

Lo stesso che si otterrebbe con un assegnazione diretta ad `Article`:

```js
Article.publisher = "Ilya Kantor";
```

## Ereditarietà delle proprietà e dei metodi statici
Anche le proprietà ed i metodi statici vengono ereditati.

Ad esempio, `Animal.compare` e `Animal.planet` nel codice sotto, vengono ereditate e diventano quindi accessibili come `Rabbit.compare` e `Rabbit.planet`:

```js
class Animal {
  static planet = "Earth";

  constructor(name, speed) {
    this.speed = speed;
    this.name = name;
  }

  run(speed = 0) {
    this.speed += speed;
    alert(`${this.name} runs with speed ${this.speed}.`);
  }


  static compare(animalA, animalB) {
    return animalA.speed - animalB.speed;
  }


}

// Eredita da Animal
class Rabbit extends Animal {
  hide() {
    alert(`${this.name} hides!`);
  }
}

let rabbits = [
  new Rabbit("White Rabbit", 10),
  new Rabbit("Black Rabbit", 5)
];


rabbits.sort(Rabbit.compare);


rabbits[0].run(); // Black Rabbit runs with speed 5.

alert(Rabbit.planet); // Earth
```

Ora, quando invochiamo `Rabbit.compare`, verrà invocato il metodo `Animal.compare` ereditato.

Come funziona? Nuovamente, utilizzando il prototypes. Come potrete aver già intuito, `extends` fornisce a `Rabbit` il  riferimento a `[[Prototype]]` di `Animal`.

![](/javascript-info/1-js/09-classes/03-static-properties-methods/animal-rabbit-static.svg)

![](/javascript-info/1-js/09-classes/03-static-properties-methods/animal-rabbit-static.svg)

1. La funzione `Rabbit` eredita dalla funzione di `Animal` .
2. `Rabbit.prototype` eredita il prototye di `Animal.prototype`.

Come risultato, l'ereditarietà funziona sia per i metodi regolari che per quelli statici.

Ora, verifichiamo quanto detto guardando al codice:

```js
class Animal {}
class Rabbit extends Animal {}

// per proprietà statiche
alert(Rabbit.__proto__ === Animal); // true

// per proprietà regolari
alert(Rabbit.prototype.__proto__ === Animal.prototype); // true
```

## Riepilogo

I metodi statici vengono utilizzati per funzionalità che appartengono all'intera classe. Non hanno nulla a che fare con l'istanza della classe.

Ad esempio, un metodo per il confronto `Article.compare(article1, article2)` o un factory method `Article.createTodays()`.

Queste vengono precedute dalla keyword `static` all'interno della dichiarazione della classe.

Le proprietà statiche vengono utilizzate quando si ha intenzione di memorizzare dati relativi alla classe, che non sono quindi legati ad un'istanza precisa.

La sintassi è:

```js
class MyClass {
  static property = ...;

  static method() {
    ...
  }
}
```

Tecnicamente, le dichiarazioni di proprietà statiche equivalgono all'assegnazione diretta alla classe stessa:

```js
MyClass.property = ...
MyClass.method = ...
```

Le proprietà ed i metodi statici vengono ereditati.

Nel caso in cui `class B extends A` il prototype della classe `B` punta ad `A`: `B.[[Prototype]] = A`. Quindi se un campo non viene trovato in `B`, la ricerca continuerà in `A`.

## Esercizi

### 1 · Class extends Object?

Come ormai sappiamo, tutti gli oggetti, normalmente ereditano da `Object.prototype` ed hanno accesso ai metodi generici di `Object`, come `hasOwnProperty` etc.

Ad esempio:

```js
class Rabbit {
  constructor(name) {
    this.name = name;
  }
}

let rabbit = new Rabbit("Rab");


// hasOwnProperty viene ereditato da Object.prototype
alert( rabbit.hasOwnProperty('name') ); // true

```

Ma se lo invocassimo esplicitamente in questo modo: `"class Rabbit extends Object"`, allora il risultato sarebbe diverso da un semplice `"class Rabbit"`?

Qual'è la differenza?

Qui vediamo un esempio (perché non funziona? è possibile sistemarlo?):

```js
class Rabbit extends Object {
  constructor(name) {
    this.name = name;
  }
}

let rabbit = new Rabbit("Rab");

alert( rabbit.hasOwnProperty('name') ); // Error
```

::::: details Soluzione

Come prima cosa, cerchiamo di capire perché il codice non funziona.

La motivazione appare piuttosto ovvia se proviamo ad eseguire il codice. Un classe che eredita, deve invocare `super()`. Diversamente, il valore di `"this"` non sarà "definito".

Vediamo come sistemarlo:

```js
class Rabbit extends Object {
  constructor(name) {

    super(); // dobbiamo chiamare il costruttore padre della classe da cui stiamo ereditando

    this.name = name;
  }
}

let rabbit = new Rabbit("Rab");

alert( rabbit.hasOwnProperty('name') ); // true
```

Ma non è tutto.

Anche dopo questo fix, c'è ancora un grande differenza tra `"class Rabbit extends Object"` e `class Rabbit`.

Come già sappiamo, la sintassi "extends" imposta due prototype:

1. Tra `"prototype"` del costruttore (per i metodi).
2. Tra i costruttori stessi (per i metodi statici).

Nel nostro caso, `class Rabbit extends Object` significa:

```js
class Rabbit extends Object {}

alert( Rabbit.prototype.__proto__ === Object.prototype ); // (1) true
alert( Rabbit.__proto__ === Object ); // (2) true
```

In questo modo, tramite `Rabbit` abbiamo accesso ai metodi statici di `Object`, come nell'esempio:

```js
class Rabbit extends Object {}


// normalmente invochiamo Object.getOwnPropertyNames
alert ( Rabbit.getOwnPropertyNames({a: 1, b: 2})); // a,b

```

Ma se non estendiamo l'oggetto, con`extends Object`, allora `Rabbit.__proto__` non sarà impostato a `Object`.

Qui una demo:

```js
class Rabbit {}

alert( Rabbit.prototype.__proto__ === Object.prototype ); // (1) true
alert( Rabbit.__proto__ === Object ); // (2) false (!)
alert( Rabbit.__proto__ === Function.prototype ); // come qualsiasi funzione di default


// errore, funzione non esistente in Rabbit
alert ( Rabbit.getOwnPropertyNames({a: 1, b: 2})); // Error

```

Quindi `Rabbit`, in questo caso, non fornisce l'accesso ai metodi statici di `Object`.

In ogni caso, `Function.prototype` possiede metodi "generici", come `call`, `bind` etc. Questi saranno disponibili in entrambi i casi, grazie al costruttore di `Object`, `Object.__proto__ === Function.prototype`.

Come mostrato in figura:

![](/javascript-info/1-js/09-classes/03-static-properties-methods/3-class-extend-object/rabbit-extends-object.svg)

Quindi, per riassumere, ci sono due principali differenze:

| class Rabbit | class Rabbit extends Object  |
|--------------|------------------------------|
| --             | dobbiamo invocare `super()` nel costruttore |
| `Rabbit.__proto__ === Function.prototype` | `Rabbit.__proto__ === Object` |

:::::

