---
title: "F.prototype"
description: "JavaScript.info in italiano: F.prototype"
sourceTutorial: true
prev: {"text": "Prototypal inheritance", "link": "/javascript/tutorial/prototype-inheritance"}
next: {"text": "Native prototypes", "link": "/javascript/tutorial/native-prototypes"}
---

# F.prototype

> **JavaScript.info · Ilya Kantor e contributori.** [Originale inglese](https://javascript.info/function-prototype) · [Edizione italiana](https://it.javascript.info/function-prototype) · [Fonti e licenza](/javascript/fonti).

Ricordate, nuovi oggetti possono essere creati con un costruttore, come `new F()`.

Se `F.prototype` è un oggetto, l'operatore `new` si prenderà cura di impostare `[[Prototype]]` per il nuovo oggetto.


::: tip Da sapere
JavaScript supporta la prototypal inheritance fin dall'inizio. Fu una delle caratteristiche principali del linguaggio.

Ma all'inizio non c'era un accesso diretto. L'unica cosa su cui ci si poteva affidare era la proprietà `"prototype"` del costruttore, descritta in questo capitolo. Per questo, esistono ancora molti script che ne fanno utilizzo.
:::

Da notare che qui `F.prototype` , sta per una comune proprietà chiamata `"prototype"` in `F`. Sembra molto simile al termine "prototype", ma in questo caso intendiamo realmente riferirci ad una proprietà con questo nome.

Vediamo qui un esempio:

```js
let animal = {
  eats: true
};

function Rabbit(name) {
  this.name = name;
}


Rabbit.prototype = animal;


let rabbit = new Rabbit("White Rabbit"); //  rabbit.__proto__ == animal

alert( rabbit.eats ); // true
```

Impostare `Rabbit.prototype = animal` fa letteralmente quanto segue: "Quando un nuovo `new Rabbit` viene creato, assegna il suo `[[Prototype]]` ad `animal`".

Questo è il risultato:

![](/javascript-info/1-js/08-prototypes/02-function-prototype/proto-constructor-animal-rabbit.svg)

In figura, `"prototype"` è una freccia orrizzontale, ciò significa che è una comune proprietà, mentre `[[Prototype]]` è verticale, quindi `rabbit` eredita da `animal`.


::: tip `F.prototype` viene utilizzato solamente al momento in cui si invoca `new F`
`F.prototype` viene utilizzata solamente quando si invoca `new F`, e si occupa di assegnare `[[Prototype]]` del nuovo oggetto.

Se, dopo la creazione, `F.prototype` cambia (`F.prototype = <another object>`), allora verrà creato un nuovo oggetto con `new F` che avrà un altro oggetto come `[[Prototype]]`, ma gli oggetti già esistenti faranno riferimento a quello vecchio.
:::

## Default F.prototype, la proprietà constructor

Ogni funzione possiede la proprietà `"prototype"` anche se non gliela forniamo direttamente.

Il `"prototype"` di default è un oggetto con un'unica proprietà, il `constructor` che punta alla funzione stessa.

Vediamo un esempio:

```js
function Rabbit() {}

/* default prototype
Rabbit.prototype = { constructor: Rabbit };
*/
```

![](/javascript-info/1-js/08-prototypes/02-function-prototype/function-prototype-constructor.svg)

Possiamo verificarlo:

```js
function Rabbit() {}
// di default:
// Rabbit.prototype = { constructor: Rabbit }

alert( Rabbit.prototype.constructor == Rabbit ); // true
```

Naturalmente, se non facciamo nulla, il `constructor` sarà disponibile a tutti i `rabbit` attraverso `[[Prototype]]`:

```js
function Rabbit() {}
// di default:
// Rabbit.prototype = { constructor: Rabbit }

let rabbit = new Rabbit(); // eredita da {constructor: Rabbit}

alert(rabbit.constructor == Rabbit); // true (dal prototype)
```

![](/javascript-info/1-js/08-prototypes/02-function-prototype/rabbit-prototype-constructor.svg)

Possiamo utilizzare il `constructor` per creare un nuovo oggetto utilizzando lo stesso costruttore dell'oggetto già esistente.

Come nell'esempio:

```js
function Rabbit(name) {
  this.name = name;
  alert(name);
}

let rabbit = new Rabbit("White Rabbit");


let rabbit2 = new rabbit.constructor("Black Rabbit");

```

Questo torna molto utile quando abbiamo un oggetto, ma non sappiamo quale costruttore è stato utilizzato (ad esempio se arriva da una libreria di terze parti), e abbiamo bisogno di crearne un altro dello stesso tipo.

Ma probabilmente la cosa più importante del `"constructor"` è che...

**...JavaScript stesso non garantisce il giusto valore del `"constructor"`.**

E' vero, esiste di default nel `"prototype"` delle funzioni, ma questo è tutto. Ciò che accade dopo -- è  solo nostra responsabilità.

In particolare, se rimpiazziamo completamente il prototype di default, allora non ci sarà alcun `"constructor"`.

Ad esempio:

```js
function Rabbit() {}
Rabbit.prototype = {
  jumps: true
};

let rabbit = new Rabbit();

alert(rabbit.constructor === Rabbit); // false

```

Quindi, per mantenere il `"constructor"` corretto, possiamo decidere di aggiungere/rimuovere proprietà al `"prototype"` di default, invece che sovrascriverlo completamente:

```js
function Rabbit() {}

// Non sovrascriviamo Rabbit.prototype completamente
// aggiungiamo semplicemente una proprietà
Rabbit.prototype.jumps = true
// il Rabbit.prototype.constructor viene cosi preservato
```

O, in alternativa, possiamo ricreare il `constructor` manualmente:

```js
Rabbit.prototype = {
  jumps: true,

  constructor: Rabbit

};

// ora il costruttore è corretto, perché lo abbiamo aggiunto noi
```


## Riepilogo

In questo capitolo abbiamo descritto brevemente il modo in cui impostare il `[[Prototype]]` per gli oggetti generati tramite il costruttore. Più avanti vedremo dei pattern più avanzati su cui fare affidamento.

Il tutto è abbastanza semplice, solo alcune note per renderlo più chiaro:

- La proprietà `F.prototype` (da non confondere con `[[Prototype]]`) imposta `[[Prototype]]` dei nuovi oggetti quando viene invocato `new F()`.
- Il valore di `F.prototype` può essere sia un oggetto che `null`: altri valori verranno ignorati.
- La proprietà `"prototype"` ha un effetto speciale quando impostata in un costruttore, ed invocata con `new`.

Negli oggetti "comuni" la proprietà `prototype` non ha alcun significato speciale:
```js
let user = {
  name: "John",
  prototype: "Bla-bla" // nessuna magia
};
```

Di default tutte le funzioni hanno `F.prototype = { constructor: F }`, quindi possiamo ottenere il costruttore di un oggetto accedendo alla sua proprietà `"constructor"`.

## Esercizi

### 1 · Cambiare "prototype"

Nel codice sotto, andiamo a creare `new Rabbit`, e successivamente proviamo a modificare il suo prototype.

Inizialmente, abbiamo questo codice:

```js
function Rabbit() {}
Rabbit.prototype = {
  eats: true
};

let rabbit = new Rabbit();

alert( rabbit.eats ); // true
```


1. Aggiungiamo una o più stringhe. Cosa mostrerà `alert` ora?

    ```js
    function Rabbit() {}
    Rabbit.prototype = {
      eats: true
    };

    let rabbit = new Rabbit();

    
    Rabbit.prototype = {};
    

    alert( rabbit.eats ); // ?
    ```

2. ...E se il codice è come il seguente (abbiamo rimpiazzato una sola riga)?

    ```js
    function Rabbit() {}
    Rabbit.prototype = {
      eats: true
    };

    let rabbit = new Rabbit();

    
    Rabbit.prototype.eats = false;
    

    alert( rabbit.eats ); // ?
    ```

3. E in questo caso (abbiamo rimpiazzato solo una riga)?

    ```js
    function Rabbit() {}
    Rabbit.prototype = {
      eats: true
    };

    let rabbit = new Rabbit();

    
    delete rabbit.eats;
    

    alert( rabbit.eats ); // ?
    ```

4. L'ultima variante:

    ```js
    function Rabbit() {}
    Rabbit.prototype = {
      eats: true
    };

    let rabbit = new Rabbit();

    
    delete Rabbit.prototype.eats;
    

    alert( rabbit.eats ); // ?
    ```

::::: details Soluzione

Riposte:

1. `true`. 

    L'assegnazione a `Rabbit.prototype` imposta `[[Prototype]]` per i nuovi oggetti, ma non influenza gli oggetti già esistenti. 

2. `false`. 

    Gli oggetti vengono assegnati per riferimento. L'oggetto in `Rabbit.prototype` non viene duplicato, è sempre un oggetto riferito sia da `Rabbit.prototype` che da `[[Prototype]]` di `rabbit`. 

    Quindi quando cambiamo il suo contenuto tramite un riferimento, questo sarà visibile anche attraverso l'altro.

3. `true`.

    Tutte le operazion di `delete` vengono applicate direttamente all'oggetto. Qui `delete rabbit.eats` prova a rimuovere la proprietà `eats` da `rabbit`, ma non esiste. Quindi l'operazione non avrà alcun effetto.

4. `undefined`.

    La proprietà `eats` viene rimossa da prototype, non esiste più.

:::::

### 2 · Crea un oggetto con lo stesso costruttore

Immagina di avere un oggetto arbitrario `obj`, creato da un costruttore -- non sappiamo quale, ma vorremmo poter creare un nuovo oggetto utilizzandolo.

Possiamo farlo in questo modo?

```js
let obj2 = new obj.constructor();
```

Fornite un esempio di costruttore per `obj` che permetta a questo codice di funzionare correttamente. Ed un esempio che non lo farebbe funzionare.

::::: details Soluzione

Possiamo utilizzare questo approccio se siamo sicuri che il `"constructor"` possiede il valore corretto.

Ad esempio, se non tocchiamo il `"prototype"` di default, allora il codice funzionerà di sicuro:

```js
function User(name) {
  this.name = name;
}

let user = new User('John');
let user2 = new user.constructor('Pete');

alert( user2.name ); // Pete (ha funzionato!)
```

Ha funzionato, poiché `User.prototype.constructor == User`.

..Ma se qualcuno, per un qualsiasi motivo, sovrascrivesse `User.prototype` e dimenticasse di ricreare il `constructor` di riferimento a `User`,  allora fallirebbe.

Ad esempio:

```js
function User(name) {
  this.name = name;
}

User.prototype = {}; // (*)


let user = new User('John');
let user2 = new user.constructor('Pete');

alert( user2.name ); // undefined
```

Perché `user2.name` è `undefined`?

Ecco come `new user.constructor('Pete')` funziona:

1. Prima, controlla se esiste `constructor` in `user`. Niente.
2. Successivamente segue la catena di prototype. Il prototype di `user` è `User.prototype`, e anche qui non c'è un `constructor` (perché ci siamo "dimenticati" di impostarlo!).
3. Seguendo la catena, `User.prototype` è un oggetto semplice, il suo prototype è `Object.prototype`. 
4. Infine, per `Object.prototype`, c'è `Object.prototype.constructor == Object`. Quindi verrà utilizzato.

In conclusione, abbiamo `let user2 = new Object('Pete')`. 

Probabilmente, non è quello che avremmo voluto, ossia creare `new User`, non `new Object`. Questo è il risultato del `costruttore` mancante.

(Nel caso tu sia curioso, la chiamata `new Object(...)` converte il suo argomento in un oggetto. Questa è una cosa teorica, in pratica nessuno chiama `new Object` con un valore, e generalmente non usiamo mai `new Object` per creare oggetti.

:::::

