---
title: "Metodi di prototype, objects senza __proto__"
description: "JavaScript.info in italiano: Metodi di prototype, objects senza __proto__"
sourceTutorial: true
prev: {"text": "Native prototypes", "link": "/javascript/tutorial/native-prototypes"}
next: {"text": "Sintassi base delle classi", "link": "/javascript/tutorial/class"}
---

# Metodi di prototype, objects senza __proto__

> **JavaScript.info · Ilya Kantor e contributori.** [Originale inglese](https://javascript.info/prototype-methods) · [Edizione italiana](https://it.javascript.info/prototype-methods) · [Fonti e licenza](/javascript/fonti).

Nel primo capitolo di questa sezione, abbiamo menzionato il fatto che esistono metodi piu moderni per impostare il prototype.

La proprietà `__proto__` viene considerata datata, e in un certo senso anche deprecata (negli standard JavaScript per i browser).

Alcuni dei metodi più moderni sono:

- [Object.create(proto, [descriptors])](mdn:js/Object/create) -- crea un oggetto vuoto, impostando il `proto` come `[[Prototype]]` e dei descrittori di proprietà opzionali.
- [Object.getPrototypeOf(obj)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/getPrototypeOf) -- ritorna il `[[Prototype]]` di `obj`.
- [Object.setPrototypeOf(obj, proto)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/setPrototypeOf) -- imposta il `[[Prototype]]` di `obj` a `proto`.

Questi metodi dovrebbero sempre essere preferiti a `__proto__`.

Ad esempio:

```js
let animal = {
  eats: true
};

// creiamo un nuovo oggetto con animal come prototype

let rabbit = Object.create(animal);


alert(rabbit.eats); // true


alert(Object.getPrototypeOf(rabbit) === animal); // true



Object.setPrototypeOf(rabbit, {}); // cambia il prototype di rabbit a {}

```

`Object.create` supporta un secondo argomento opzionale: il property descriptors (descrittori di proprietà). Possiamo fornire proprietà aggiuntive al nuovo oggetto, in questo modo:

```js
let animal = {
  eats: true
};

let rabbit = Object.create(animal, {
  jumps: {
    value: true
  }
});

alert(rabbit.jumps); // true
```

I descrittori vanno forniti nel formato descritto nel capitolo [Attributi e descrittori di proprietà](/javascript/tutorial/property-descriptors).

Possiamo utilizzare `Object.create` per clonare un oggetto in maniera più efficace rispetto al copiare le proprietà con un `for..in`:

```js
let clone = Object.create(Object.getPrototypeOf(obj), Object.getOwnPropertyDescriptors(obj));
```

Questa chiamata crea una copia esatta di `obj`, inculdendo tutte le proprietà: enumerable e non-enumerable, e i relativi setters/getters -- tutto, impostando anche il giusto `[[Prototype]]`.

## Una breve storia

Se contiamo tutti i modi che abbiamo a disposizione per gestire `[[Prototype]]`, questi sono molti! Abbiamo moltissime modalità per fare la stessa cosa!

Perché?

Motivazioni storiche.

- La proprietà `"prototype"` di un costruttore è disponibile fin dai primi tempi in JavaScript.
- Più tardi, nel 2012, è apparso nello standard `Object.create`. Il quale permette di creare oggetti fornendogli un prototype, ma non consente di impostarlo o di ottenerlo. Quindi i browser implementarono il metodo non-standard `__proto__`, come proprietà di accesso per impostare o otternere il prototype in qualsiasi momento.
- Più tardi, nel 2015, `Object.setPrototypeOf` e `Object.getPrototypeOf` vennero aggiunti allo standard, con le stesse funzionalità di `__proto__`. Poiché `__proto__` era di fatto implementato ovunque, entrò in un fase di deprecazione, nella sezione Annex B dello standard, ovvero: opzionale per gli ambienti non-browser.

Ad oggi abbiamo molti metodi a nostra disposizione.

Perché `__proto__` è stato rimpiazzato dalle funzioni `getPrototypeOf/setPrototypeOf`? Questa è una domanda interessante; dobbiamo capire perché l'utilizzo di `__proto__` non è una buona pratica. Continuate a leggere per avere la risposta.


::: warning Non cambiate il `[[Prototype]]` ad oggetti esistenti se la velocità è importante
Tecnicamente, possiamo impostare/ottenere il `[[Prototype]]` in qualsiasi momento. Ma solitamente lo impostiamo in fase di creazione dell'oggetto e successivamente non lo modifichiamo più: `rabbit` eredita da `animal`, e questo non dovrebbe cambiare.

I motori JavaScript sono altamente ottimizzati per questo. Cambiare il prototype durante l'esecuzione, con `Object.setPrototypeOf` o `obj.__proto__=` è un operazione molto lenta, poiché vanifica le ottimizzazioni interne fatte per le operazioni di accesso alle proprietà. Quindi evitate questa pratica, a meno che non siate consci di ciò che state facendo, e la velocità di esecuzione non è un problema per voi.
:::

## "Very plain" objects
Come sappiamo, gli oggetti possono essere utilizzati come un array associativo per memorizzare coppie chiave/valore.

...Ma se proviamo a memorizzare chiavi *fornite dall'utente* (ad esempio, un dizionario con vocaboli forniti dall'utente), noteremo un piccolo bug: tutte le chiavi funzioneranno senza problemi, ad eccezione di `"__proto__"`.

Vediamo un esempio:

```js
let obj = {};

let key = prompt("What's the key?", "__proto__");
obj[key] = "some value";

alert(obj[key]); // [object Object], non "some value"!
```

In questo esempio, se l'utente digita `__proto__`, l'assegnazione è ignorata!

Questo non dovrebbe sorprenderci. La proprietà `__proto__` è speciale: deve contenere un oggetto o `null`. Una stringa non può fungere da prototype.

Ma il nostro *intento* non è quello di implementare questo comportamento, giusto? Vogliamo semplicemente memorizzare una coppia chiave/valore, ma utilizzando come chiave il termine `"__proto__"` questo non viene memorizzato correttamente. Quindi, questo è un bug!

In questo caso le conseguenze non sono così terribili. Ma in altri casi potremmo assegnarli oggetti, andando a modificare il valore del prototype. Risultato: l'esecuzione fallirà in maniera imprevedibile.

Ancora peggio -- solitamente gli sviluppatori non pensano affatto a questa eventualità. Questo lo rende un bug veramente difficile da trovare e può portare a diverse vulnerabilità, specialmente se il codice viene eseguito server-side.

Questi comportamenti inaspettati accadono anche se proviamo ad assegnare la chiave `toString`, la quale è una funzione di default, e lo stesso vale per gli altri metodi integrati.

Come possiamo evitare questo problema?

Come prima cosa, possiamo semplicemente utilizzare `Map` per la memorizzazione dei valori al posto di un oggetto, in questo modo non avremo problemi.

Ma `Object` potrebbe esserci utile, perché i creatori del linguaggio hanno pensato a questo problema molto tempo fa.

`__proto__` non è una proprietà di un oggetto, ma una proprietà di accesso per `Object.prototype`:

![](/javascript-info/1-js/08-prototypes/04-prototype-methods/object-prototype-2.svg)

Quindi, se `obj.__proto__` viene letta o impostata, il corrispondende getter/setter viene chiamato dal suo prototype, il quale legge/imposta il `[[Prototype]]`.

Come detto all'inizio di questa sezione: `__proto__` è un modo per accedere al `[[Prototype]]`, non è il `[[Prototype]]` stesso.

Ora, se il nostro scopo è quello di utilizzare un oggetto come array associativo, e vogliamo evitare questo tipo di problemi, possiamo farlo in questo modo:

```js

let obj = Object.create(null);


let key = prompt("What's the key?", "__proto__");
obj[key] = "some value";

alert(obj[key]); // "some value"
```

`Object.create(null)` crea un oggetto vuoto senza un prototype (`[[Prototype]]` vale `null`):

![](/javascript-info/1-js/08-prototypes/04-prototype-methods/object-prototype-null.svg)

Quindi, non si ha alcun getter/setter ereditato per `__proto__`. D'ora in poi verrà trattata come una comune proprietà; l'esempio visto sopra funzionerà senza problemi.

Questo tipo di oggetti vengono chiamati "very plain" ("molto semplici") o "pure dictionary" ("dizionari puri"), poiché sono molto più semplici dei normali plain object `{...}`.

Il lato negativo di questi oggetti è che mancano di tutti i metodi integrati, ad esempio `toString`:

```js

let obj = Object.create(null);


alert(obj); // Error (non esiste toString)
```

...Ma questo può andarci bene per gli array associativi.

Da notare che molti dei metodi relativi agli oggetti sono come `Object.something(...)`, ad esempio `Object.keys(obj)` -- non sono contenuti all'interno del prototype, quindi continueranno a funzionare anche con questo tipo di oggetti:


```js
let chineseDictionary = Object.create(null);
chineseDictionary.hello = "你好";
chineseDictionary.bye = "再见";

alert(Object.keys(chineseDictionary)); // hello,bye
```

## Riepilogo

I metodi moderni per impostare e leggere il prototype sono:

- [Object.create(proto, [descriptors])](mdn:js/Object/create) -- crea un oggetto vuoto utilizzando `proto` come `[[Prototype]]` (può essere anche `null`) e dei property descriptors (descrittori di proprietà).
- [Object.getPrototypeOf(obj)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/getPrototypeOf) -- ritorna il `[[Prototype]]` di `obj` (equivale a `__proto__`).
- [Object.setPrototypeOf(obj, proto)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/setPrototypeOf) -- imposta il `[[Prototype]]` di `obj` a `proto` (equivale a `__proto__`).

La proprietà integrata `__proto__`, utilizzata come getter/setter, non è sicura nel caso in cui volessimo inserire in un oggetto chiavi fornite dall'utente. Un utente potrebbe inserire `"__proto__"` come chiave, che genererebbe un errore; potrebbe non avere gravi conseguenze, ma generalmente non è prevedibile.

Le alternative disponibili sono: usare `Object.create(null)` per creare un "very plain" object, senza `__proto__`, o in alternativa, utilizzare `Map`.

Inoltre, `Object.create` consente di creare una shallow-copy ('copia non profonda') di un oggetto, compresi i suoi property descriptors:

```js
let clone = Object.create(Object.getPrototypeOf(obj), Object.getOwnPropertyDescriptors(obj));
```

Abbiamo anche chiarito che `__proto__` è un getter/setter per `[[Prototype]]` e risiede in `Object.prototype`, proprio come gli altri metodi.

Possiamo creare un oggetto senza prototype utilizzando `Object.create(null)`. Questo tipo di oggetti vengono utilizzati come "puri dizionari", e non causano problemi nel caso in cui venga utilizzata `"__proto__"` come chiave.

Altri metodi:

- [Object.keys(obj)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/keys) / [Object.values(obj)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/values) / [Object.entries(obj)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/entries) -- ritorna un array di stringhe contenente le proprietà enumerable, i valori e le coppie chaive/valore.
- [Object.getOwnPropertySymbols(obj)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/getOwnPropertySymbols) -- ritorna un array con tutte le chiavi di tipo Symbol che appartengono all'oggetto.
- [Object.getOwnPropertyNames(obj)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/getOwnPropertyNames) -- ritorna un array di stringhe con tutte le proprietà che appartengono all'oggetto.
- [Reflect.ownKeys(obj)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/ownKeys) -- ritorna un array con tutte le chiavi che appartengono all'oggetto.
- [obj.hasOwnProperty(key)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/hasOwnProperty): ritorna `true` se `obj` possiede una sua chiave `key` (non ereditata).

Tutti i metodi che ritornano le proprietà di un oggetto  (come `Object.keys` e le altre) -- ritornano le proprietà "possedute". Se vogliamo ottenere anche le proprietà ereditate dobbiamo utilizzare un ciclo `for..in`.

## Esercizi

### 1 · Aggiungi toString al dizionario

Abbiamo un oggetto `dictionary`, creato come `Object.create(null)`, in cui memorizziamo coppie `key/value`.

Aggiungi un metodo `dictionary.toString()`, il quale dovrebbe ritornare un lista di chiavi separate da virgola. Il metodo `toString` non deve essere mostrato nei cicli `for..in`.

Dovrebbe funzionare così:

```js
let dictionary = Object.create(null);


// il tuo codice per aggiungere il metodo toString


// aggiungiamo dei valori
dictionary.apple = "Apple";
dictionary.__proto__ = "test"; // __proto__ è una proprietà comune in questo caso

// nel ciclo compaiono solo apple e __proto__ 
for(let key in dictionary) {
  alert(key); // "apple", poi "__proto__"
}  

// la tua implementazione di toString in azione
alert(dictionary); // "apple,__proto__"
```

::::: details Soluzione

Il metodo `Object.keys` mostra tutte le proprietà enumerabili di un oggetto.

Per rendere `toString` non-enumerable, dobbiamo definirlo utilizzando un property descriptor. La sintassi che ci permette di farlo è `Object.create`, che ci consente di fornire dei property descriptors come secondo argomento.

```js

let dictionary = Object.create(null, {
  toString: { // definiamo la proprietà toString
    value() { // il valore è una funzione
      return Object.keys(this).join();
    }
  }
});


dictionary.apple = "Apple";
dictionary.__proto__ = "test";

// apple e __proto__ appaiono nel ciclo
for(let key in dictionary) {
  alert(key); // "apple", poi "__proto__"
}  

// vengono elencate le proprietà separate da una virgola
alert(dictionary); // "apple,__proto__"
```

Possiamo crare una proprietà utilizzando un descriptor. Di default i flag vengono impostati a `false`. Quindi nel codice sopra, `dictionary.toString` è non-enumerable.

Vedi il capitolo [property descriptors](/javascript/tutorial/property-descriptors) se hai bisogno di ripassare l'argomento.

:::::

### 2 · La differenza tra chiamate

Creiamo un nuovo oggetto `rabbit`:

```js
function Rabbit(name) {
  this.name = name;
}
Rabbit.prototype.sayHi = function() {
  alert(this.name);
};

let rabbit = new Rabbit("Rabbit");
```

Queste chiamata fanno la stessa cosa o no?

```js
rabbit.sayHi();
Rabbit.prototype.sayHi();
Object.getPrototypeOf(rabbit).sayHi();
rabbit.__proto__.sayHi();
```

::::: details Soluzione

La prima chiamata ha `this == rabbit`, le altre hanno `this` uguale a `Rabbit.prototype`, perché è l'oggetto prima del punto.

Quindi, solamente la prima chiamata mostra `Rabbit`, le altre mostrano `undefined`:

```js
function Rabbit(name) {
  this.name = name;
}
Rabbit.prototype.sayHi = function() {
  alert( this.name );
}

let rabbit = new Rabbit("Rabbit");

rabbit.sayHi();                        // Rabbit
Rabbit.prototype.sayHi();              // undefined
Object.getPrototypeOf(rabbit).sayHi(); // undefined
rabbit.__proto__.sayHi();              // undefined
```

:::::

