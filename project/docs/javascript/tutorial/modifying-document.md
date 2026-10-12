---
title: "Modificare il documento"
description: "JavaScript.info in italiano: Modificare il documento"
sourceTutorial: true
prev: {"text": "Attributi e proprietà", "link": "/javascript/tutorial/dom-attributes-and-properties"}
next: {"text": "Stili e classi", "link": "/javascript/tutorial/styles-and-classes"}
---

# Modificare il documento

> **JavaScript.info · Ilya Kantor e contributori.** [Originale inglese](https://javascript.info/modifying-document) · [Edizione italiana](https://it.javascript.info/modifying-document) · [Fonti e licenza](/javascript/fonti).

La modifica del DOM è la chiave della creazione di pagine dinamiche.

Vedremo come creare elementi "al volo" e come modificare il contenuto della pagina già esistente.

## Esempio: mostrare un messaggio

Dimostriamolo con un esempio. Aggiungeremo un messaggio alla pagina, più carino di `alert`.

Sarà così:

```html
<style>
.alert {
  padding: 15px;
  border: 1px solid #d6e9c6;
  border-radius: 4px;
  color: #3c763d;
  background-color: #dff0d8;
}
</style>


<div class="alert">
  <strong>Hi there!</strong> You've read an important message.
</div>

```

Questo era l'esempio con HTML. Ora creiamo lo stesso `div` con JavaScript (presupponendo che lo stile sia già in HTML/CSS).

## Creare un elemento

Per creare nodi DOM, ci sono due metodi:

`document.createElement(tag)`
: Crea un nuovo *nodo elemento* con il tag fornito:

    ```js
    let div = document.createElement('div');
    ```

`document.createTextNode(text)`
  Crea un nuovo *nodo di testo* con il testo fornito:

    ```js
    let textNode = document.createTextNode('Here I am');
    ```

Nella maggior parte dei casi abbiamo bisogno di creare un nodo elemento, come il `div` per il messaggio.

### Creare un messaggio

Creare un messaggio necessita di tre passaggi:

```js
// 1. Creare l'elemento <div> 
let div = document.createElement('div');

// 2. Impostare la sua classe ad "alert"
div.className = "alert";

// 3. Riempirlo con il contenuto
div.innerHTML = "<strong>Hi there!</strong> You've read an important message.";
```

Abbiamo creato l'elemento, ma al momento è solo una variabile chiamata `div`, non è ancora nella pagina, perciò non possiamo vederlo.

## I metodi d'inserimento
   
Per rendere visibile `div`, dobbiamo inserirlo da qualche parte nel `document`. Per esempio dentro all'elemento `body`, referenziato da `document.body`.

C'è un metodo speciale per questo, `append`: `document.body.append(div)`.

Qui il codice completo:

```html
<style>
.alert {
  padding: 15px;
  border: 1px solid #d6e9c6;
  border-radius: 4px;
  color: #3c763d;
  background-color: #dff0d8;
}
</style>

<script>
  let div = document.createElement('div');
  div.className = "alert";
  div.innerHTML = "<strong>Hi there!</strong> You've read an important message.";


  document.body.append(div);

</script>
```

Qui abbiamo chiamato `append` su `document.body`, ma possiamo chiamare `append` su qualsiasi elemento e mettervi dentro un altro elemento. Ad esempio, possiamo appendere qualcosa a `div` chiamando `div.append(anotherElement)`.

Ecco altri metodi d'inserimento; specificano i differenti posti dove inserire un elemento:

- `node.append(...nodi o stringhe)` -- appende nodi o stringhe *alla fine* di `node`,
- `node.prepend(...nodi o stringhe)` -- inserisce nodi o stringhe *all'inizio* di `node`,
- `node.before(...nodi o stringhe)` –- inserisce nodi o stringhe *prima* di `node`,
- `node.after(...nodi o stringhe)` –- inserisce nodi o stringhe *dopo* `node`,
- `node.replaceWith(...nodi o stringhe)` –- rimpiazza `node` con i nodi o le stringhe passate.

Gli argomenti di questi metodi sono liste arbitrarie di nodi DOM da inserire, o stringhe di testo (che diventano automaticamente nodi testo).

Vediamoli in azione.

Ecco un esempio dell'utilizzo di questi metodi per aggiungere elementi a una lista e del testo prima/dopo di essa:

```html
<ol id="ol">
  <li>0</li>
  <li>1</li>
  <li>2</li>
</ol>

<script>
  ol.before('before'); // inserisce la stringa "before" prima di <ol>
  ol.after('after'); // inserisce la stringa "after" dopo <ol>

  let liFirst = document.createElement('li');
  liFirst.innerHTML = 'prepend';
  ol.prepend(liFirst); // inserisce liFirst all'inizio di <ol>

  let liLast = document.createElement('li');
  liLast.innerHTML = 'append';
  ol.append(liLast); // inserisce liLast alla fine di <ol>
</script>
```

Ecco uno schema visivo di cosa fanno questi metodi:

![](/javascript-info/2-ui/1-document/07-modifying-document/before-prepend-append-after.svg)

La lista finale sarà:

```html
before
<ol id="ol">
  <li>prepend</li>
  <li>0</li>
  <li>1</li>
  <li>2</li>
  <li>append</li>
</ol>
after
```

Come già detto, questi metodi possono inserire nodi multipli e pezzi di testo in una singola chiamata.

Ad esempio, qui vengono inseriti una stringa e un elemento:

```html
<div id="div"></div>
<script>
  div.before('<p>Hello</p>', document.createElement('hr'));
</script>
```

Nota: il testo viene inserito "come testo", non "come HTML", con i dovuti escape per caratteri come `<` o `>`.

Quindi l'HTML finale sarà:

```html

&lt;p&gt;Hello&lt;/p&gt;

<hr>
<div id="div"></div>
```

In altre parole, le stringhe sono inserite in sicurezza, come con `elem.textContent`.

Quindi, questi metodi possono essere usati solo per inserire nodi o pezzi di testo.

E se volessimo inserire stringhe HTML "come HTML", con tutti i tag e le altre funzionalità, come con `elem.innerHTML`?

## insertAdjacentHTML/Text/Element

Per questo abbiamo a disposizione un altro metodo, molto versatile: `elem.insertAdjacentHTML(where, html)`.


Il primo parametro è una parola-codice che specifica dove inserire in relazione a `elem`. Deve essere una delle seguenti:

- `"beforebegin"` -- inserisce `html` immediatamente prima di `elem`,
- `"afterbegin"` -- inserisce `html` dentro `elem`, all'inizio,
- `"beforeend"` -- inserisce `html` dentro `elem`, alla fine,
- `"afterend"` -- inserisce `html` immediatamente dopo `elem`.

Il secondo parametro è una stringa HTML, che viene inserita "come HTML"

Ad esempio:

```html
<div id="div"></div>
<script>
  div.insertAdjacentHTML('beforebegin', '<p>Hello</p>');
  div.insertAdjacentHTML('afterend', '<p>Bye</p>');
</script>
```

...Porterebbe a:

```html
<p>Hello</p>
<div id="div"></div>
<p>Bye</p>
```

Così possiamo appendere HTML alla pagina.

Qui un'immagine delle varianti d'inserimento:

![](/javascript-info/2-ui/1-document/07-modifying-document/insert-adjacent.svg)

Possiamo facilmente notare similarità tra questa immagine e le precedenti. I punti di inserimento sono gli stessi, ma questo metodo inserisce HTML. 

Il metodo ha due fratelli:

- `elem.insertAdjacentText(where, text)` -- la stessa sintassi, ma una stringa `text` viene inserita "come testo" invece che come HTML,
- `elem.insertAdjacentElement(where, elem)` -- la stessa sintassi, ma inserisce un elemento.

Questi metodi esistono per rendere la sintassi "uniforme". Nella pratica, nella maggioranza dei casi solo `insertAdjacentHTML` viene utilizzato, perché per elementi e testo abbiamo i metodi `append/prepend/before/after`; questi sono più brevi da scrivere e possono inserire nodi/pezzi di testo.

Ecco un variante alternativa per mostrare un messaggio:

```html
<style>
.alert {
  padding: 15px;
  border: 1px solid #d6e9c6;
  border-radius: 4px;
  color: #3c763d;
  background-color: #dff0d8;
}
</style>

<script>
  document.body.insertAdjacentHTML("afterbegin", `<div class="alert">
    <strong>Hi there!</strong> You've read an important message.
  </div>`);
</script>
```

## Rimozione di nodi

Per rimuovere un nodo, abbiamo a disposizione il metodo `node.remove()`.

Facciamo sparire il nostro messaggio dopo un secondo:

```html
<style>
.alert {
  padding: 15px;
  border: 1px solid #d6e9c6;
  border-radius: 4px;
  color: #3c763d;
  background-color: #dff0d8;
}
</style>

<script>
  let div = document.createElement('div');
  div.className = "alert";
  div.innerHTML = "<strong>Hi there!</strong> You've read an important message.";

  document.body.append(div);

  setTimeout(() => div.remove(), 1000);

</script>
```

Nota: se vogliamo *muovere* un elemento in un altro posto, non c'è bisogno di rimuoverlo dal vecchio. 

**Tutti i metodi d'inserimento rimuovono automaticamente i nodi dal vecchio posto.**

Ad esempio, scambiamo degli elementi:

```html
<div id="first">First</div>
<div id="second">Second</div>
<script>
  // nessun bisogno di chiamare remove
  second.after(first); // prende #second e inserisce #first dopo
</script>
```

## Clonare nodi: cloneNode

Come inserire uno o più messaggi simili? 

Potremmo scrivere una funzione a mettervi dentro il codice. Ma l'alternativa sarebbe *clonare* il `div` esistente e modificare il testo dentro (se necessario).

Qualche volta, quando abbiamo un grosso elemento, questo potrebbe rivelarsi più facile e veloce.

La chiamata a `elem.cloneNode(true)` crea un clone "profondo" dell'elemento, con tutti gli attributi e i sub-elementi. Se chiamiamo `elem.cloneNode(false)`, l'elemento viene clonato senza i suoi elementi figlio.

Un esempio copiando un messaggio:

```html
<style>
.alert {
  padding: 15px;
  border: 1px solid #d6e9c6;
  border-radius: 4px;
  color: #3c763d;
  background-color: #dff0d8;
}
</style>

<div class="alert" id="div">
  <strong>Hi there!</strong> You've read an important message.
</div>

<script>

  let div2 = div.cloneNode(true); // clona il messaggio
  div2.querySelector('strong').innerHTML = 'Bye there!'; // modifica il clone

  div.after(div2); // mostra il clone dopo il div esistente

</script>
```

## DocumentFragment
`DocumentFragment` è uno speciale nodo DOM che serve come wrapper a liste di nodi.

Possiamo appendervi altri nodi, ma quando viene inserito da qualche parte, viene sostituito con il suo contenuto. 

Nell'esempio sotto, `getListContent` genera un frammento con elementi `<li>`, che dopo vengono inseriti in `<ul>`.

```html
<ul id="ul"></ul>

<script>
function getListContent() {
  let fragment = new DocumentFragment();

  for(let i=1; i<=3; i++) {
    let li = document.createElement('li');
    li.append(i);
    fragment.append(li);
  }

  return fragment;
}


ul.append(getListContent()); // (*)

</script>
```

Nota, nell'ultima riga `(*)` appendiamo `DocumentFragment`, ma questo viene
"sciolto", e la risultante struttura sarà:
```html
<ul>
  <li>1</li>
  <li>2</li>
  <li>3</li>
</ul>
```

`DocumentFragment` è raramente utilizzato esplicitamente. Perché appendere elementi a un nodo speciale quando possiamo invece ritornare un array di nodi? Riscriviamo l'esempio:

```html
<ul id="ul"></ul>

<script>
function getListContent() {
  let result = [];

  for(let i=1; i<=3; i++) {
    let li = document.createElement('li');
    li.append(i);
    result.push(li);
  }

  return result;
}


ul.append(...getListContent()); // append + "..." operator = friends!

</script>
```

Menzioniamo `DocumentFragment` principalmente perché vi sono alcuni concetti che vi si basano, come un elemento [template](/javascript/tutorial/template-element), che vedremo molto più avanti. 

## Metodi vecchia scuola di inserimento/rimozione
Vi sono dei metodi di manipolazione del DOM "vecchia scuola", che esistono per motivi storici. 

Questi metodi vengono dai vecchi tempi. Oggi non c'è ragione per utilizzarli, giacché i metodi moderni come `append`, `prepend`, `before`, `after`, `remove`, `replaceWith`, sono più flessibili. 

L'unica ragione per cui li elenchiamo è che possiamo ancora trovarli in molti vecchi script:

`parentElem.appendChild(node)`
: Appende `node` come ultimo figlio di `parentElem`.
  

    Il seguente esempio aggiunge un nuovo `<li>` alla fine di `<ol>`:

    ```html
    <ol id="list">
      <li>0</li>
      <li>1</li>
      <li>2</li>
    </ol>

    <script>
      let newLi = document.createElement('li');
      newLi.innerHTML = 'Hello, world!';

      list.appendChild(newLi);
    </script>
    ```

`parentElem.insertBefore(node, nextSibling)`
: Inserisce `node`, prima di `nextSibling`, dentro `parentElem`.

    Il codice seguente inserisce una nuova lista di elementi prima del secondo `<li>`:

    ```html
    <ol id="list">
      <li>0</li>
      <li>1</li>
      <li>2</li>
    </ol>
    <script>
      let newLi = document.createElement('li');
      newLi.innerHTML = 'Hello, world!';

    
      list.insertBefore(newLi, list.children[1]);
    
    </script>
    ```
    Per inserire `newLi` come primo elemento, possiamo fare così:

    ```js
    list.insertBefore(newLi, list.firstChild);
    ```

`parentElem.replaceChild(node, oldChild)`
: Rimpiazza `oldChild` con `node` tra i figli di `parentElem`.

`parentElem.removeChild(node)`
: Rimuove `node` da `parentElem` (presupponendo che `node` sia suo figlio).

    Il seguente esempio rimuove il primo `<li>` da `<ol>`:

    ```html
    <ol id="list">
      <li>0</li>
      <li>1</li>
      <li>2</li>
    </ol>

    <script>
      let li = list.firstElementChild;
      list.removeChild(li);
    </script>
    ```

Tutti questi metodi ritornano i nodi inseriti/rimossi. In altre parole, `parentElem.appendChild(node)` ritorna `node`. Ma solitamente il valore ritornato non viene utilizzato, è il metodo che ci interessa.

## Una parola su "document.write"

C'è un altro metodo, molto vecchio, per aggiungere qualcosa a una pagina web:  `document.write`.

La sintassi:

```html
<p>Somewhere in the page...</p>

<script>
  document.write('<b>Hello from JS</b>');
</script>

<p>The end</p>
```

La chiamata a `document.write(html)` inserisce `html` nella pagina "all'istante". La stringa `html` può essere generata dinamicamente, quindi in un certo senso è flessibile. Possiamo utilizzare JavaScript per creare una pagina web completa e per scrivervi. 

Il metodo viene dai tempi in cui non c'era un DOM, nessun standart... Tempi molto vecchi. E' ancora vivo perché vi sono script che lo utilizzano. 

Negli script moderni possiamo trovarlo raramente a causa della seguente importante limitazione:

**La chiamata a `document.write` funziona solo mentre la pagina sta caricando.**
  
Se lo chiamiamo dopo, il contenuto esistente del documento viene cancellato.

Ad esempio:

```html
<p>After one second the contents of this page will be replaced...</p>

<script>
  // document.write dopo 1 secondo
  // questo dopo che la pagina ha caricato, quindi il contenuto esistente viene cancellato
  setTimeout(() => document.write('<b>...By this.</b>'), 1000);
</script>

```

Perciò è inutilizzabile dopo il caricamento della pagina, a differenza dei metodi del DOM che abbiamo visto sopra. 

Questo è il lato negativo.

Ma c'è anche un lato positivo. Tecnicamente, quando `document.write` viene chiamato mentre il browser sta leggendo ("analizzando") l'HTML, e vi scrive qualcosa, il browser tratta quel contenuto come se fosse stato dal principio nel testo HTML.

Quindi lavora molto velocemente, perché *non viene modificato il DOM*. Scrive direttamente nel testo della pagina, quando il DOM non è ancora stato costruito.

Perciò se abbiamo bisogno di aggiungere dinamicamente molto testo all'HTML, siamo in fase di caricamento della pagina e la velocità conta, potrebbe essere utile. Ma in pratica questo capita raramente. Di solito troviamo questo metodo in uno script solo perché è vecchio. 

## Riepilogo

  Metodi per creare nuovi nodi:
    - `document.createElement(tag)` -- crea un elemento con il dato tag,
    - `document.createTextNode(value)` -- crea un nodo di testo (raramente utilizzato),
    - `elem.cloneNode(deep)` -- clona un elemento, se `deep==true` include tutti i discendenti.

- Inserzione e rimozione:
    - `node.append(...nodi o stringhe)` -- inserisce dentro `node`, alla fine,
    - `node.prepend(...nodi o stringhe)` -- inserisce dentro `node`, all'inizio,
    - `node.before(...nodi o stringhe)` –- inserisce subito prima di `node`,
    - `node.after(...nodi o stringhe)` –- inserisce subito dopo `node`,
    - `node.replaceWith(...nodi o stringhe)` –- rimpiazza `node`.
    - `node.remove()` –- rimuove `node`.

    Le stringhe di testo vengono inserite "come testo".

- Ci sono anche metodi "vecchia scuola":
    - `parent.appendChild(node)`
    - `parent.insertBefore(node, nextSibling)`
    - `parent.removeChild(node)`
    - `parent.replaceChild(newElem, node)`

    Tutti questi metodi ritornano `node`.

- Data HTML come `html`, `elem.insertAdjacentHTML(where, html)` inserisce in base al valore di `where`:
    - `"beforebegin"` -- inserisce `html` subito prima di `elem`,
    - `"afterbegin"` -- inserisce `html` in `elem`, all'inizio,
    - `"beforeend"` -- inserisce `html` in `elem`, alla fine,
    - `"afterend"` -- inserisce `html` subito dopo `elem`.

    Ci sono altri metodi simili, `elem.insertAdjacentText` e `elem.insertAdjacentElement`, che inseriscono stringhe di testo ed elementi, ma vengono raramente utilizzati.

- Per appendere HTML a una pagina prima che questa carichi:
    - `document.write(html)`

    Dopo che la pagina ha caricato la sua chiamata cancella il contenuto della pagina. Si trova principalmente in vecchi script.

## Esercizi

### 1 · createTextNode vs innerHTML vs textContent

Abbiamo `elem`, un elemento DOM vuoto, e una stringa`text`.

Quali di questi 3 comandi fanno esattamente la stessa cosa?

1. `elem.append(document.createTextNode(text))`
2. `elem.innerHTML = text`
3. `elem.textContent = text`

::::: details Soluzione

Risposta: **1 e 3**.

Entrambi i commandi risultano nell'aggiunta di `text` "come testo" dentro a `elem`.
Ecco un esempio:

```html
<div id="elem1"></div>
<div id="elem2"></div>
<div id="elem3"></div>
<script>
  let text = '<b>text</b>';

  elem1.append(document.createTextNode(text));
  elem2.innerHTML = text;
  elem3.textContent = text;
</script>
```

:::::

### 2 · Ripulisci l'elemento

Crea una funzione `clear(elem)` che rimuova tutto da un elemento.

```html
<ol id="elem">
  <li>Hello</li>
  <li>World</li>
</ol>

<script>
  function clear(elem) { /* il tuo codice */ }

  clear(elem); // Ripulisce la lista
</script>
```

::::: details Soluzione

Prima, vediamo come *non* farlo:

```js
function clear(elem) {
  for (let i=0; i < elem.childNodes.length; i++) {
      elem.childNodes[i].remove();
  }
}
```

Questo non funziona perché la chiamata a `remove()` muove la collezione `elem.childNodes`, quindi gli elementi partono ogni volta dall'indice `0`. Ma `i` aumenta, perciò alcuni elementi verranno saltati.

Il loop `for..of` fa lo stesso.

La corretta variante potrebbe essere:

```js
function clear(elem) {
  while (elem.firstChild) {
    elem.firstChild.remove();
  }
}
```

C'è un modo più semplice per fare lo stesso:

```js
function clear(elem) {
  elem.innerHTML = '';
}
```

:::::

### 3 · Perché rimane "aaa"?

Nell'esempio sotto, la chiamata a `table.remove()` rimuove la tabella dal documento.

Ma se eseguiamo il codice, potrai vedere che il testo `"aaa"` è ancora visibile. 

Perché?

```html
<table id="table">
  aaa
  <tr>
    <td>Test</td>
  </tr>
</table>

<script>
  alert(table); // la tabella, come dovrebbe essere

  table.remove();
  // perché aaa è ancora nel documento?
</script>
```

::::: details Soluzione

L'HTML nel task è incorretto. Questa è la ragione della stranezza.

Il browser deve sistemarlo automaticamente. Ma non vi può essere testo dentro a `<table>`: secondo la specifica, solo gli specifici tag per le tabelle sono permessi. Perciò il browser aggiunge `"aaa"` *prima* di `<table>`.

Ora è ovvio perché, rimuovendo la tabella, il testo rimane.

La domanda può facilmente trovare risposta esplorando il DOM con gli strumenti del browser. Mostra `"aaa"` prima di `<table>`.

Lo standard HTML specifica in dettaglio come processare cattivo HTML, e questo comportamento del browser è corretto.

:::::

### 4 · Crea una lista

Scrivi un'interfaccia per creare una lista dagli input dell'utente.

Per ogni elemento della lista:

1. Chiedi all'utente il contenuto utilizzando  `prompt`.
2. Crea il `<li>` con il contenuto e aggiungilo a `<ul>`.
3. Continua fino a quando l'utente non interrompe l'input (premendo `key:Esc` o inserendo un contenuto vuoto)

Tutti gli elementi devono essere creati dinamicamente.

Se l'utente inserisce tag HTML, questi devono essere trattati come testo.

[Apri l’esempio nella fonte originale](https://it.javascript.info/modifying-document).

::::: details Soluzione

Nota l'utilizzo di `textContent` per assegnare il contenuto a `<li>`.

:::::

### 5 · Crea un albero da un oggetto

Scrivi una funzione `createTree` che crea una lista `ul/li` annidata partendo dall'oggetto annidato.

Ad esempio:

```js
let data = {
  "Fish": {
    "trout": {},
    "salmon": {}
  },

  "Tree": {
    "Huge": {
      "sequoia": {},
      "oak": {}
    },
    "Flowering": {
      "apple tree": {},
      "magnolia": {}
    }
  }
};
```

La sintassi:

```js
let container = document.getElementById('container');

createTree(container, data); // creates the tree in the container

```

Il risultato (l'albero) dovrebbe somigliare a questo:

[Apri l’esempio nella fonte originale](https://it.javascript.info/modifying-document).

Scegli uno dei due metodi per risolvere la task:

1. Crea l'HTML per l'albero e assegnala a `container.innerHTML`.
2. Crea i nodi dell'albero e appendili utilizzando i metodi del DOM.

Sarebbe grandioso se riuscissi con entrambi.

P.S. L'albero non dovrebbe avere elementi "extra" -ad esempio`<ul></ul>` vuoti- come foglie.

::::: details Soluzione

Il modo più semplice per percorrere l'oggetto è utilizzando la ricorsione.

1. [La soluzione con innerHTML](https://javascript.info/create-object-tree).
2. [La soluzione con DOM](https://javascript.info/create-object-tree).

:::::

### 6 · Mostra i discendenti dentro a un albero

C'è un albero organizzato come `ul/li` annidati.

Scrivi il codice che aggiunge a ogni `<li>` il numero dei suoi discendenti. Salta le foglie (i nodi senza figli).

Il risultato:

[Apri l’esempio nella fonte originale](https://it.javascript.info/modifying-document).

::::: details Soluzione

Per appendere testo a ogni `<li>` possiamo modificare il nodo di testo `data`.

:::::

### 7 · Crea un calendario
Scrivi una funzione `createCalendar(elem, year, month)`.

La sua chiamata dovrebbe creare un calendario con il dato anno/mese e metterlo dentro a `elem`.

Il calendario dovrebbe essere una tabella dove una settimana è `<tr>` e un giorno è `<td>`. La cima della tabella dovrebbe essere un `<th>` con i nomi dei giorni: il primo giorno dovrebbe essere lunedì e così via fino a domenica.

Ad esempio, `createCalendar(cal, 2012, 9)` dovrebbe generare un elemento `cal` con il seguente calendario:

[Apri l’esempio nella fonte originale](https://it.javascript.info/modifying-document).

P.S. Per questa task è sufficiente creare il calendario, non è necessario che sia cliccabile.

::::: details Soluzione

Creeremo una tabella come stringa, `"<table>...</table>"`, e poi la assegneremo a `innerHTML`.

L'algoritmo:

1. Crea il header della tabella con `<th>` e i nomi dei giorni. 
2. Crea l'oggetto data `d = new Date(year, month-1)`. Questo è il primo giorno di `month` (prendendo in considerazione che in Javascript i mesi partono da `0`, non da `1`).
3. Le prime celle fino al primo del mese `d.getDay()` sono vuote. Riempiamole con `<td></td>`.
4. Aumentiamo il giorno in `d`: `d.setDate(d.getDate()+1)`. Se `d.getMonth()` non è ancora il mese successivo, aggiungi la nuova cella `<td>` al calendario. Se questo è una domenica, aggiungi una nuova linea <code>"&lt;/tr&gt;&lt;tr&gt;"</code>.
5. Se il mese è finito ma la fila della tabella non è ancora piena, aggiungi un `<td>` vuoto in modo da renderla rettangolare.

:::::

### 8 · Orologio colorato con setInterval

Crea un orologio colorato come quello dell'esempio:

[Apri l’esempio nella fonte originale](https://it.javascript.info/modifying-document).

Usa HTML/CSS per lo styling, JavaScript aggiorna solo il tempo negli elementi.

::::: details Soluzione

First, let's make HTML/CSS.

Each component of the time would look great in its own `<span>`:

```html
<div id="clock">
  <span class="hour">hh</span>:<span class="min">mm</span>:<span class="sec">ss</span>
</div>
```

Also we'll need CSS to color them.

The `update` function will refresh the clock, to be called by `setInterval` every second:

```js
function update() {
  let clock = document.getElementById('clock');

  let date = new Date(); // (*)

  let hours = date.getHours();
  if (hours < 10) hours = '0' + hours;
  clock.children[0].innerHTML = hours;

  let minutes = date.getMinutes();
  if (minutes < 10) minutes = '0' + minutes;
  clock.children[1].innerHTML = minutes;

  let seconds = date.getSeconds();
  if (seconds < 10) seconds = '0' + seconds;
  clock.children[2].innerHTML = seconds;
}
```

In the line `(*)` we every time check the current date. The calls to `setInterval` are not reliable: they may happen with delays.

The clock-managing functions:

```js
let timerId;

function clockStart() { // run the clock  
  if (!timerId) { // only set a new interval if the clock is not running
    timerId = setInterval(update, 1000);
  }
  update(); // (*)
}

function clockStop() {
  clearInterval(timerId);
  timerId = null; // (**)
}
```

Nota che la chiamata a `update()` non è programmata solo in `clockStart()`, ma immediatamente dopo l'esecuzione della linea `(*)`. Altrimenti il visitatore dovrebbe aspettare fino alla prima esecuzione di `setInterval`. E l'orologio sarebbe vuoto fino ad allora. 

E' altresì importante impostare il nuovo intervallo in `clockStart()` solo quando l'orologio non sta andando. Altrimenti cliccare il bottone start svariate volte imposterebbe multipli intervali concorrenti. Ancora peggio: terremmo solo il `timerID` dell'ultimo intervallo, perdendo la referenza a tutti gli altri. Così non potremmo più fermare l'orologio! Nota che dobbiamo rimuovere il `timerID` quando l'orologio viene fermato alla linea `(**)`, in modo da permettergi di ricominciare eseguendo `clockStart()`.

:::::

### 9 · Inserisci l'HTML nella lista

Scrivi il codice per inserire `<li>2</li><li>3</li>` tra i due `<li>` sotto:

```html
<ul id="ul">
  <li id="one">1</li>
  <li id="two">4</li>
</ul>
```

::::: details Soluzione

Quando abbiamo bisogno di inserire dell'HTML da qualche parte, `insertAdjacentHTML` è la scelta migliore
  
La soluzione:

```js
one.insertAdjacentHTML('afterend', '<li>2</li><li>3</li>');
```

:::::

### 10 · Ordina la tabella

Ecco una tabella:

```html
<table>
<thead>
  <tr>
    <th>Name</th><th>Surname</th><th>Age</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>John</td><td>Smith</td><td>10</td>
  </tr>
  <tr>
    <td>Pete</td><td>Brown</td><td>15</td>
  </tr>
  <tr>
    <td>Ann</td><td>Lee</td><td>5</td>
  </tr>
  <tr>
    <td>...</td><td>...</td><td>...</td>
  </tr>
</tbody>
</table>
```

Potrebbero esserci più file dentro.

Scrivi il codice per ordinarla in base alla colonna `"name"`.

::::: details Soluzione

La soluzione è breve, ma potrebbe sembrare difficile, quindi la commenteremo in dettaglio:

```js
let sortedRows = Array.from(table.tBodies[0].rows) // 1
  .sort((rowA, rowB) => rowA.cells[0].innerHTML.localeCompare(rowB.cells[0].innerHTML));

table.tBodies[0].append(...sortedRows); // (3)
```

L'algoritmo passo per passo:

1. Trova tutti i `<tr>` dentro `<tbody>`. 
2. Ordinali comparando il contenuto del primo `<td>` (il campo con il nome).
3. Ora inserisci i nodi nel giusto ordine con `.append(...sortedRows)`.

Non dobbiamo rimuovere gli elementi della fila, solo "re-inserirli", lasciano automaticamente il vecchio posto.

P.S. Nel nostro caso c'è un esplicito `<tbody>` nella tabella; ma se anche non vi fosse, la struttura DOM lo include sempre e comunque.

:::::

