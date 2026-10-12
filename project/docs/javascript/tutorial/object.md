---
title: "Oggetti"
description: "JavaScript.info in italiano: Oggetti"
sourceTutorial: true
prev: {"text": "Polyfills e transpilers", "link": "/javascript/tutorial/polyfills"}
next: {"text": "Oggetti: riferimento e copia", "link": "/javascript/tutorial/object-copy"}
---

# Oggetti

> **JavaScript.info · Ilya Kantor e contributori.** [Originale inglese](https://javascript.info/object) · [Edizione italiana](https://it.javascript.info/object) · [Fonti e licenza](/javascript/fonti).

Come sappiamo dal capitolo *Tipi di dati*, in Javascript ci sono otto tipi di dati. Sette di loro sono chiamati "primitivi", perché i loro valori contengono sempre un singolo elemento (una stringa, un numero, un booleano ecc).

Gli oggetti, invece, vengono utilizzati per catalogare vari tipi di dati ed altri elementi più complessi. In Javascript, essi permeano ogni aspetto del linguaggio. Dobbiamo perciò comprenderli bene prima di procedere nello studio approfondito di un qualsiasi altro argomento.

Un oggetto può essere creato tramite le parentesi graffe `{...}`, con un'opzionale lista di proprietà. Una proprietà è una coppia "chiave: valore", dove "chiave" è una stringa (detta anche "nome di proprietà"), mentre "valore" può essere qualsiasi cosa.

Possiamo immaginare un oggetto come un archivio con dei documenti catalogati. Ogni dato viene archiviato utilizzando una specifica chiave. E' facile trovare un file quando se ne conosce il nome, oppure aggiungerne di nuovi o rimuovere quelli vecchi.

![](/javascript-info/1-js/04-object-basics/01-object/object.svg)

Un oggetto vuoto ("archivio vuoto") può essere creato utilizzando una delle due sintassi:

```js
let user = new Object(); // sintassi "costruttore oggetto"
let user = {};  // sintassi "oggetto letterale"
```

![](/javascript-info/1-js/04-object-basics/01-object/object-user-empty.svg)

Solitamente vengono utilizzate le parentesi graffe `{...}`. Questo tipo di dichiarazione viene chiamata *object literal* ("oggetto letterale").

## Le proprietà dei literal

Possiamo inserire subito delle proprietà in `{...}` come una coppia "key: value":

```js
let user = {     // un oggetto
  name: "John",  // una chiave "name" memorizza il valore "John"
  age: 30        // una chiave "age" memorizza 30
};
```

Una proprietà ha una chiave (conosciuta anche come "nome" o "identificatore") prima dei due punti `":"`, ed un valore alla sua destra.

Nell'oggetto `user` ci sono due proprietà:

1. La prima proprietà ha come nome `"name"` e come valore `"John"`.
2. La seconda ha come nome `"age"` e come valore `30`.

L'oggetto `user` può essere visto come un archivio con due file etichettati come "name" ed "age".

![user object](/javascript-info/1-js/04-object-basics/01-object/object-user.svg)

Possiamo aggiungere, rimuovere o leggere un file in qualsiasi momento.

I valori delle proprietà sono accessibili utilizzando la notazione puntata:

```js
// ritorna i campi dell'oggetto:
alert( user.name ); // John
alert( user.age ); // 30
```

Il valore può essere di qualsiasi tipo. Aggiungiamo un booleano:

```js
user.isAdmin = true;
```

![user object 2](/javascript-info/1-js/04-object-basics/01-object/object-user-isadmin.svg)

Per rimuovere una proprietà, possiamo utilizzare l'operatore `delete`:

```js
delete user.age;
```

![user object 3](/javascript-info/1-js/04-object-basics/01-object/object-user-delete.svg)

Possiamo anche utilizzare nomi di proprietà composti da più parole ("multi-parola"), ma devono essere racchiusi tra virgolette:

```js
let user = {
  name: "John",
  age: 30,
  "likes birds": true  // un nome di proprietà composto da più parole deve essere racchiuso tra virgolette
};
```

![](/javascript-info/1-js/04-object-basics/01-object/object-user-props.svg)

L'ultima proprietà in lista può terminare con una virgola:
```js
let user = {
  name: "John",
  age: 30,
}
```
Rende più facile l'aggiunta/rimozione/spostamento delle proprietà, poiché tutte le righe hanno una virgola.

## Parentesi quadre

Per le proprietà con nomi "multi-parola" l'accesso con la notazione puntata non funziona:

```js
// questo darebbe un errore di sintassi
user.likes birds = true
```
Questo perché il punto richiede che la chiave che segue sia un identificatore valido. Un identificatore non deve avere spazi (oltre a seguire le altre limitazioni già studiate).

Per aggirare questo vincolo esiste una "notazione con parentesi quadre":

```js
let user = {};

// set
user["likes birds"] = true;

// get
alert(user["likes birds"]); // true

// delete
delete user["likes birds"];
```

Ora funziona. Da notare che la stringa all'interno delle parentesi va comunque messa tra virgolette (singole o doppie).

Le parentesi quadre permettono di passare il nome della proprietà come risultato di un espressione -- a differenza delle stringhe letterali --, ad esempio una variabile:

```js
let key = "likes birds";

// lo stesso di user["likes birds"] = true;
user[key] = true;
```

Qui la variabile `key` può essere calcolata durante il run-time o dipendere dall'input dell'utente. Successivamente possiamo utilizzarla per accedere alla proprietà. Questa caratteristica ci fornisce una grande flessibilità.

Ad esempio:

```js
let user = {
  name: "John",
  age: 30
};

let key = prompt("What do you want to know about the user?", "name");

// accesso tramite variabile
alert( user[key] ); // John (se si inserisce "name")
```

La notazione puntata non può essere utilizzata in questo modo:

```js
let user = {
  name: "John",
  age: 30
};

let key = "name";
alert( user.key ) // undefined
```

### Proprietà calcolate

Possiamo utilizzare le parentesi quadre al momento della creazione di un oggetto letterale. Questo metodo viene chiamato *calcolo delle proprietà*.

Ad esempio:

```js
let fruit = prompt("Which fruit to buy?", "apple");

let bag = {

  [fruit]: 5, // il nome della proprietà viene preso dalla variabile fruit

};

alert( bag.apple ); // 5 se fruit="apple"
```

La logica dietro le proprietà calcolate è semplice: `[fruit]` significa che il nome della proprietà deve essere preso da `fruit`.

Quindi, se un utente inserisce `"apple"`, `bag` diventerà `{apple: 5}`.

Essenzialmente, questo funziona allo stesso modo di:
```js
let fruit = prompt("Which fruit to buy?", "apple");
let bag = {};

// prende il nome della proprietà dalla variabile fruit
bag[fruit] = 5;
```

...Ma è meno carino.

Possiamo utilizzare anche espressioni più complesse all'interno delle parentesi quadre:

```js
let fruit = 'apple';
let bag = {
  [fruit + 'Computers']: 5 // bag.appleComputers = 5
};
```

Le parentesi quadre sono molto più potenti della notazione puntata. Ci permettono di assegnare qualsiasi nome, ma sono più "ingombranti".
La maggior parte delle volte, quando il nome della proprietà è conosciuto e semplice, la notazione puntata viene preferita. Se invece necessitiamo di qualcosa di più complesso, possiamo utilizzare le parentesi quadre.


## Abbreviazione per il valore di una proprietà

Spesso usiamo delle variabili esistenti come valori per i nomi delle proprietà.

Ad esempio:

```js
function makeUser(name, age) {
  return {
    name: name,
    age: age
    // ...altre proprietà
  };
}

let user = makeUser("John", 30);
alert(user.name); // John
```

Nell'esempio sopra, le proprietà hanno lo stesso nome delle varibili. Il caso d'uso di creare una proprietà da una variabile è molto comune, tanto che, per comodità, esiste una speciale *abbreviazione* .

Invece di scrivere `name:name` possiamo semplicemente scrivere `name`, come in questo esempio:

```js
function makeUser(name, age) {

  return {
    name, // equivalente a name: name
    age   // equivalente a age: age
    // ...
  };

}
```
Possiamo usare entrambe le proprietà, normale e abbreviata, nello stesso oggetto:

```js
let user = {
  name,  // equivalente a name:name
  age: 30
};
```
## Limitazioni per i nomi di una proprietà

Come già sappiamo, una variabile non può avere il nome uguale ad una parola chiave riservata al linguaggio come "for", "let", "return" etc.

Ma per le proprietà degli oggetti, non ci sono restrizioni:

```js
// queste variabili sono tutte corrette
let obj = {
  for: 1,
  let: 2,
  return: 3
};

alert( obj.for + obj.let + obj.return );  // 6
```

In breve, non ci sono limitazioni per i nomi delle proprietà. Possono essere stringhe o simboli (un tipo di dato speciale che andremo ad analizzare più avanti).

Nomi di proprietà con altri tipi "primitivi" vengono automaticamente convertiti a stringhe.

Ad esempio, un numero `0` diventa una stringa `"0"` quando viene utilizzato come chiave di una proprietà:

```js
let obj = {
  0: "test" // equivale a "0": "test"
};

// entrambi gli alert accedono alla stessa proprietà (il numero 0 viene convertito nella stringa "0")
alert( obj["0"] ); // test
alert( obj[0] ); // test (stessa proprietà)
```

Esiste una piccola falla per la proprietà `__proto__`. Non possiamo impostarla ad un valore diverso dal tipo oggetto:

```js
let obj = {};
obj.__proto__ = 5; // assegnamo un numero
alert(obj.__proto__); // [object Object] - il valore è un oggetto, non ha funzionato come ci si aspettava
```

Come possiamo osservare nel codice sopra, l'assegnazione del numero intero `5` è stata ignorata.

Studieremo più nel dettaglio `__proto__` nel [capitolo](/javascript/tutorial/prototype-inheritance), e vedremo come [sistemare](/javascript/tutorial/prototype-methods) questo comportamento.

## Controllo di esistenza, operatore "in"

Un'importante caratteristica degli oggetti, in Javascript, è che è possibile accedere a una qualsiasi proprietà. Non ci sarà alcun errore se la proprietà non esiste! 

L'accesso ad una variabile non esistente ritornerà `undefined`. Possiamo quindi facilmente verificare se una properietà esiste:

```js
let user = {};

alert( user.noSuchProperty === undefined ); // true significa "nessuna properietà"
```

Esiste anche uno speciale operatore `"in"` per lo stesso scopo.

La sintassi è:
```js
"key" in object
```

Ad esempio:

```js
let user = { name: "John", age: 30 };

alert( "age" in user ); // true, significa che user.age esiste
alert( "blabla" in user ); // false, significa che user.blabla non esiste
```

Da notare che alla sinistra di `in` deve esserci il *nome di una proprietà*. Questa, solitamente, è una stringa.

Se omettiamo le virgolette attorno alla proprietà da cercare, verrà cercata una variabile con quel nome e verrà utilizzato il suo valore. Ad esempio:

```js
let user = { age: 30 };

let key = "age";
alert( key in user ); // true, prende il nome da key e controlla l'esistenza della proprietà
```


:::: tip Utilizzare "in" con le proprietà che contengono `undefined`
Solitamente, il confronto stretto con `"=== undefined"` funziona correttamente. Ma c'è un particolare caso in cui questo fallisce, mentre con `"in"` funziona correttamente.

Questo accade quando una proprietà esiste, ma contiene `undefined`:

```js
let obj = {
  test: undefined
};

alert( obj.test ); // è undefined, quindi -- non esiste la proprietà?

alert( "test" in obj ); // true, la proprietà esiste!
```


Nel codice sopra, tecnicamente, la proprietà `obj.test` esiste. Quindi l'operatore `in` funziona.

Situazioni come questa capitano raramente, perché solitamente non si assegna `undefined`. Si usa più comunemente `null` per valori "sconosciuti" o "vuoti". Quindi l'operatore `in` è più un ospite "esotico" nel codice.


## Il ciclo "for..in" 

Per attraversare tutte le chiavi di un oggetto, esiste una speciale forma di ciclo: `for..in`. Questo è completamente diverso da `for(;;)`.

La sintassi:

```js
for (key in object) {
  // esegue il corpo del ciclo per ogni proprietà dell'oggetto
}
```

Ad esempio, proviamo a mostrare tutte le proprietà di `user`:

```js
let user = {
  name: "John",
  age: 30,
  isAdmin: true
};

for (let key in user) {
  // keys
  alert( key );  // name, age, isAdmin
  // valori delle keys
  alert( user[key] ); // John, 30, true
}
```

Da notare che tutti i costrutti "for" ci consentono di dichiarare delle variabili da utilizzare all'interno del ciclo stesso, come `let key` in questo esempio.

Inoltre possiamo utilizzare qualsiasi altra variabile al posto di `key`. Ad esempio `"for(let prop in obj)"` è molto utilizzato.


### Ordinato come un oggetto

Gli oggetti sono ordinati? In altre parole, se iteriamo un oggetto, otterremo le sue proprietà nello stesso ordine in cui le abbiamo aggiunte? 

Una risposta breve è: "sono ordinati in modo speciale": le proprietà che hanno numeri interi come chiavi vengono ordinate, le altre appaiono seguendo l'ordine di creazione. Seguiranno maggiori dettagli.

Per fare un esempio, consideriamo un oggetto con dei prefissi telefonici:

```js
let codes = {
  "49": "Germany",
  "41": "Switzerland",
  "44": "Great Britain",
  // ..,
  "1": "USA"
};


for (let code in codes) {
  alert(code); // 1, 41, 44, 49
}

```

L'oggetto può essere utilizzato per suggerire una lista di opzioni all'utente. Se stiamo sviluppando un sito dedicato al pubblico tedesco propbabilmente vorrano vedersi apparire come primo valore `49`.

Se proviamo ad eseguire il codice, vedremo un risultato totalmente inaspettato:

- USA (1) viene per primo
- po Switzerland (41) e a seguire gli altri.

I prefissi telefonici seguono un ordine crescente; questo accade perché sono numeri interi. Quindi vedremo `1, 41, 44, 49`.


:::: tip Proprietà degli interi? Cos'è?
La "proprietà degli interi" è un termine che indica una stringa che può essere convertita da e ad un intero senza subire modifiche.

Quindi "49" segue la proprietà degli interi, perché quando viene trasformato in un numero intero e riportato a stringa, rimane uguale. Ad esempio "+49" e "1.2" non lo sono:

```js
// Math.trunc è una proprietà integrata che rimuove la parte decimale
alert( String(Math.trunc(Number("49"))) ); // "49", rimane uguale
alert( String(Math.trunc(Number("+49"))) ); // "49", è diverso da "+49" ⇒ non è un numero intero
alert( String(Math.trunc(Number("1.2"))) ); // "1", è diverso da "1.2" ⇒ non è un numero intero
```
::::

...Differentemente, se le chiavi non sono numeri interi, vengono restituite nell'ordine di creazione, ad esempio:

```js
let user = {
  name: "John",
  surname: "Smith"
};
user.age = 25; // aggiungiamone un'altra


// le proprietà non intere vengono elencate nell'ordine di creazione

for (let prop in user) {
  alert( prop ); // name, surname, age
}
```

Quindi per sistemare il problema con i prefissi telefonici, possiamo "barare" rendendo i prefissi non interi. Questo lo otteniamo inserendo un `"+"` prima di ogni numero.

Come nel codice sotto:

```js
let codes = {
  "+49": "Germany",
  "+41": "Switzerland",
  "+44": "Great Britain",
  // ..,
  "+1": "USA"
};

for (let code in codes) {
  alert( +code ); // 49, 41, 44, 1
}
```

Ora funziona come previsto.

## Riepilogo
Gli oggetti sono arrays associativi con diverse caratteristiche speciali:

Possono memorizzare proprietà (coppie di chiave-valore) in cui:
- Il nome della proprietà (chiave) deve essere composta da una o più stringhe o simboli (solitamente stringhe).
- I valori possono essere di qualsiasi tipo.

Per accedere ad una proprietà possiamo utilizzare:
- La notazione puntata: `obj.property`.
- La notazione con parentesi quadre `obj["property"]`. Questa notazione consente di accettare chiavi dalle variabili, come `obj[varWithKey]`.

Operatori specifici:
- Per cancellare una proprietà: `delete obj.prop`.
- Per controllare se un una proprietà con un certo nome esiste: `"key" in obj`.
- Per iterare un oggetto: `for(let key in obj)`.

Gli oggetti vengono assegnati e copiati per riferimento. In altre parole, la variabile non memorizza il "valore dell'oggetto", ma piuttosto un "riferimento" (indirizzo di memoria). Quindi copiando questa variabile o passandola come argomento ad una funzione, fornirà un riferimento all'oggetto e non una copia. Tutte le operazioni effettuate su un oggetto copiato per riferimento (come aggiungere/rimuovere proprietà) vengono effettuate sullo stesso oggetto.

Quello che abbiamo studiato in questo capitolo viene chiamato "oggetto semplice", o solo `Object`.

Ci sono altri tipi di oggetti in Javascript:

- `Array` per memorizzare dati ordinati,
- `Date` per memorizzare informazioni riguardo date e orari,
- `Error` per memorizzare informazioni riguardo errori.
- ...e molti altri.


Ognuno di questi ha le sue caratteristiche speciali che studieremo più avanti. Qualche volta le persone dicono cose tipo "Array type" ("tipo Array") o "Date type" ("tipo Data"), ma formalmente non sono dei tipi, appartengono al tipo di dato "object". Sono semplicemente delle estensioni.

Gli oggetti in JavaScript sono molto potenti. Qui abbiamo grattato solamente la superficie, l'argomento è veramente ampio. Lavoreremo molto con gli oggetti per impararne ulteriori caratteristiche.
::::

## Esercizi

### 1 · Hello, object

Scrivi il seguente codice, una riga per ogni azione:

1. Crea un oggetto vuoto `user`.
2. Aggiungi la proprietà `name` con valore `John`.
3. Aggiungi la proprietà `surname` con valore `Smith`.
4. Cambia il valore di `name` con `Pete`.
5. Rimuovi la proprietà `name` dall'oggetto.

::::: details Soluzione

```js
let user = {};
user.name = "John";
user.surname = "Smith";
user.name = "Pete";
delete user.name;
```

:::::

### 2 · Controlla se è vuoto

Scrivi la funzione `isEmpty(obj)` che ritorna `true` se l'oggetto non ha proprietà, altrimenti ritorna `false`.

Dovrebbe funzionare con queste istruzioni:

```js
let schedule = {};

alert( isEmpty(schedule) ); // true

schedule["8:30"] = "get up";

alert( isEmpty(schedule) ); // false
```

::::: details Soluzione

E' sufficiente eseguire un ciclo e ritornare `false` se l'oggetto contiene almeno una proprietà.

```js
function isEmpty(obj) {
  for (let key in obj) {
    return false;
  }
  return true;
}
```

:::::

### 3 · Oggetti costanti?

E' possibile modificare un oggetto dichiarato con `const`? Cosa ne pensi?

```js
const user = {
  name: "John"
};


// does it work?
user.name = "Pete";

```

::::: details Soluzione

Certo, funziona senza problemi.

La keyword `const` protegge la variabile solo da riassegnazioni. 

In altre parole, `user` memorizza un riferimento all'oggetto. Questo non può cambiare. Ma l'oggetto contenuto non ha nessun vincolo.

```js
const user = {
  name: "John"
};


// funziona (abbiamo cambiato una properietà dell'oggetto)
user.name = "Pete";


// errore (abbiamo cercato di cambiare tutto valore in un colpo solo)
user = 123;
```

:::::

### 4 · Somma le proprietà dell'oggetto

Abbiamo un oggetto che memorizza il salario dei dipendenti del team:

```js
let salaries = {
  John: 100,
  Ann: 160,
  Pete: 130
}
```

Scrivi il codice per sommare tutti i salari contenuti e memorizza il risultato in `sum`. Dovrebbe essere `390`.

Se `salaries` è vuoto il risultato dovrebbe essere `0`.

::::: details Soluzione

```js
let salaries = {
  John: 100,
  Ann: 160,
  Pete: 130
};

let sum = 0;
for (let key in salaries) {
  sum += salaries[key];
}

alert(sum); // 390
```

:::::

### 5 · Moltiplica le proprietà numeriche per 2

Crea una funzione `multiplyNumeric(obj)` che moltiplica tutte le prprietà numeriche di `obj` per `2`.

Ad esempio:

```js
// before the call
let menu = {
  width: 200,
  height: 300,
  title: "My menu"
};

multiplyNumeric(menu);

// after the call
menu = {
  width: 400,
  height: 600,
  title: "My menu"
};
```

Nota che `multiplyNumeric` non deve ritornare nulla. Deve solamente modificare l'oggetto.

P.S. Usa `typeof` per controllare il tipo.

::::: details Soluzione

function multiplyNumeric(obj) {
  for (let key in obj) {
    if (typeof obj[key] == 'number') {
      obj[key] *= 2;
    }
  }
}

:::::

