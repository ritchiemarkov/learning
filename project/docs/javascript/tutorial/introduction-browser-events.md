---
title: "Introduzione agli eventi del browser"
description: "JavaScript.info in italiano: Introduzione agli eventi del browser"
sourceTutorial: true
prev: {"text": "Coordinate", "link": "/javascript/tutorial/coordinates"}
next: {"text": "Bubbling e capturing", "link": "/javascript/tutorial/bubbling-and-capturing"}
---

# Introduzione agli eventi del browser

> **JavaScript.info · Ilya Kantor e contributori.** [Originale inglese](https://javascript.info/introduction-browser-events) · [Edizione italiana](https://it.javascript.info/introduction-browser-events) · [Fonti e licenza](/javascript/fonti).

*Un evento* è un segnale che sta ad indicare che è avvenuto qualcosa. Tutti i nodi DOM generano questi segnali (anche se gli eventi non sono limitati al DOM).

Ecco quindi una lista, degli eventi DOM più utili:

**Eventi del mouse:**
- `click` -- quando si clicca col mouse su un elemento (i dispositivi touch lo generano tramite il tocco).
- `contextmenu` -- quando si clicca col tasto destro su un elemento.
- `mouseover` / `mouseout` -- quando il cursore passa sopra/abbandona un elemento.
- `mousedown` / `mouseup` -- quando viene premuto/rilasciato il pulsante del mouse su un elemento.
- `mousemove` -- quando si sposta il mouse.

**Eventi da tastiera:**
- `keydown` e `keyup` -- quando viene premuto e rilasciato un tasto.

**Eventi degli elementi del form:**
- `submit` -- quando l'utente invia un `<form>`.
- `focus` --  quando l'utente attiva il focus su un elemento, ad esempio su un `<input>`.

**Eventi del Document:**
- `DOMContentLoaded` -- quando l'HTML viene caricato e processato, e la costruzione del DOM è stata completata.

**Eventi dei CSS:**
- `transitionend` -- quando termina un'animazione CSS (CSS-animation).

Ci sono molti altri eventi più specifici, che verranno affrontati in dettaglio nei prossimi capitoli.

## Gestori di evento

Per reagire agli eventi possiamo assegnare un *gestore* (handler). Questo non è altro che una funzione che viene eseguita contestualmente alla generazione di un evento.

I gestori, quindi, sono un modo per eseguire codice JavaScript al verificarsi delle azioni dell'utente ed esistono vari modi per assegnare un evento. 

Partiamo dal più semplice.

### Attributo HTML

Un gestore può essere impostato in HTML con un attributo chiamato `on<event>`.

Ad esempio, per assegnare un gestore al `click` di un `input`, possiamo usare `onclick`:

```html
<input value="Cliccami" onclick="alert('Click!')" type="button">
```

Al click del mouse, il codice dentro `onclick` verrà eseguito.

Nota bene che dentro `onclick` useremo gli apici singoli, in quanto l'attributo stesso è già inserito all'interno di apici doppi. Se ci dimenticassimo che il codice stesse dentro l'attributo, ed usassimo gli apici doppi come in questo caso:  `onclick="alert("Click!")"`, il codice non funzionerebbe.

Un attributo HTML non è un buon posto per scrivere tanto codice, quindi è molto meglio creare una funzione JavaScript per poterla richiamare.

In questo esempio, al click viene eseguita la funzione `countRabbits()`:

```html
<script>
  function countRabbits() {
    for(let i=1; i<=3; i++) {
      alert("Coniglio numero " + i);
    }
  }
</script>

<input type="button" onclick="countRabbits()" value="Conta i conigli!">
```
Come sappiamo, gli attributi HTML non sono case-sensitive, quindi scrivere `ONCLICK` va bene tanto quanto `onClick` e `onCLICK`...ma solitamente vengono scritti in minuscolo: `onclick`.

### Proprietà del DOM

Possiamo assegnare un gestore usando una proprietà DOM `on<event>`.

Ad esempio, `elem.onclick`:

```html
<input id="elem" type="button" value="Cliccami">
<script>

  elem.onclick = function() {
    alert('Grazie');
  };

</script>
```

Se il gestore viene assegnato usando un attributo HTML, il browser lo riconosce, crea una nuova funzione partendo dal contenuto dell'attributo e la scrive nella proprietà del DOM.

In sostanza, questa modalità equivale alla precedente.

I due codici messi a confronto, infatti, lavorano alla stessa maniera:

1. Solo HTML:

    ```html
    <input type="button" onclick="alert('Click!')" value="Button">
    ```
2. HTML + JS:

    ```html
    <input type="button" id="button" value="Button">
    <script>
    
      button.onclick = function() {
        alert('Click!');
      };
    
    </script>
    ```
L'unica differenza è che nel primo esempio, l'attributo HTML viene usato per inizializzare il `button.onclick`, invece nel secondo per inizializzare lo script.

**Dal momento che c'è solo una proprietà `onclick`, non è possibile assegnare più di un gestore evento.**

Aggiungendo un gestore tramite JavaScript, si va a sovrascrivere il gestore esistente:

```html
<input type="button" id="elem" onclick="alert('Prima')" value="Click me">
<script>

  elem.onclick = function() { // sovrascrive il gestore precedente
    alert('Dopo'); // viene mostrato solo questo
  };

</script>
```

Per rimuovere un gestore, assegnare `elem.onclick = null`.

## Accedere all'elemento: this

Il valore di `this` all'interno di un gestore è l'elemento contenente il gestore.

Qui il `button` mostra il suo contenuto tramite `this.innerHTML`:

```html
<button onclick="alert(this.innerHTML)">Cliccami</button>
```

## Possibili errori

Se stai affrontando da poco l'argomento degli eventi, nota bene alcune sottigliezze.

Possiamo impostare come gestore una funzione esistente:

```js
function sayThanks() {
  alert('Grazie!');
}

elem.onclick = sayThanks;
```

Ma attenzione: la funzione deve essere assegnata scrivendo `sayThanks`, e non `sayThanks()`.

```js
// corretto
button.onclick = sayThanks;

// errato
button.onclick = sayThanks();
```

Se aggiungessimo le parentesi, allora `sayThanks()` diverrebbe una chiamata a funzione. Di conseguenza il valore dell'assegnazione dell'ultima riga dell'esempio, sarebbe il risultato della chiamata, ossia `undefined` (dato che la funzione non restituisce nulla), e verrebbe assegnato ad `onclick`. Ovviamente così non potrebbe andare bene, ed inoltre non sarebbe nemmeno l'effetto voluto.

...D'altra parte, però, nel markup abbiamo bisogno delle parentesi:

```html
<input type="button" id="button" onclick="sayThanks()">
```

La differenza è molto semplice: quando il browser legge l'attributo, crea una funzione che fa da gestore, il cui corpo è il contenuto dell'attributo.

Quindi il markup crea questa proprietà:
```js
button.onclick = function() {

  sayThanks(); // <-- il contenuto dell'attributo va a finire qui

};
```

**Non usare `setAttribute` per i gestori.**

Ed ancora, una chiamata del genere non funzionerà:

```js
// un click sul <body> genera errori,
// perché gli attributi sono sempre stringhe, e la funzione diventa una stringa
document.body.setAttribute('onclick', function() { alert(1) });
```

**Il case della proprietà DOM è rilevante.**

Assegnare un gestore a `elem.onclick`, e non a `elem.ONCLICK`, in quanto le proprietà del DOM sono case-sensitive.

## addEventListener

Il problema principale della sopracitata maniera di assegnare i gestori è che non abbiamo modo di assegnare dei gestori multipli a un evento.

Ipotizziamo che una parte del nostro codice serva ad evidenziare un pulsante al click, e che un altro serva a mostrare un messaggio al medesimo click.

Per fare questo sarebbe bello poter assegnare due eventi distinti, ma sappiamo che ogni nuova proprietà DOM con lo stesso nome, sovrascriverà la precedente:

```js
input.onclick = function() { alert(1); }
// ...
input.onclick = function() { alert(2); } // sostituisce il gestore precedente
```

Gli sviluppatori degli standard web hanno intuito la cosa tempo addietro, e hanno suggerito un modo alternativo per trattare i gestori, usando i metodi speciali `addEventListener` e `removeEventListener`, i quali non sono affetti da questi problemi.

Ecco la sintassi per aggiungere un gestore:

```js
element.addEventListener(event, handler, [options]);
```

`event`
: Nome dell'evento, ad esempio `"click"`.

`handler`
: La funzione che fa da gestore.

`options`
: Un oggetto opzionale aggiuntivo con delle proprietà:
    - `once`: se `true`, il listener viene rimosso automaticamente una volta innescato.
    - `capture`: la fase in cui deve essere gestito l'evento, argomento affrontato più avanti nel capitolo [Bubbling e capturing](/javascript/tutorial/bubbling-and-capturing). Per ragioni storiche, `options` possono essere anche `false/true`, ed è equivale a scrivere `{capture: false/true}`.
    - `passive`: se `true`, il gestore non chiamerà `preventDefault()`, anche questo, verrà spiegato successivamente nel capitolo [Azioni predefinite del browser](/javascript/tutorial/default-browser-action).

Per rimuovere l'evento, si usa `removeEventListener`:

```js
element.removeEventListener(event, handler, [options]);
```


:::: warning La rimozione richiede la stessa identica funzione
Per rimuovere un gestore dobbiamo passare come parametro, la stessa funzione che abbiamo usato per l'assegnazione.

Il seguente codice non fa quello che ci aspetteremmo:

```js
elem.addEventListener( "click" , () => alert('Grazie!'));
// ....
elem.removeEventListener( "click", () => alert('Grazie!'));
```

Il gestore non verrà rimosso, perchè `removeEventListener` prende come parametro un'altra funzione: è certamente con lo stesso codice, ma questo non ha alcuna rilevanza, dal momento che è un oggetto funzione differente (fanno riferimento a due differenti indirizzi di memoria).

La maniera corretta per farlo è questa:

```js
function handler() {
  alert( 'Thanks!' );
}

input.addEventListener("click", handler);
// ....
input.removeEventListener("click", handler);
```

Nota bene: se non assegnassimo la funzione a una variabile, non potremmo rimuoverla: non c'è alcun modo di "risalire" ai gestori assegnati tramite `addEventListener`.
::::

Chiamate multiple a `addEventListener` permettono di aggiungere gestori multipli:

```html
<input id="elem" type="button" value="Click me"/>

<script>
  function handler1() {
    alert('Grazie!');
  };

  function handler2() {
    alert('Grazie di nuovo!');
  }


  elem.onclick = () => alert("Ciao");
  elem.addEventListener("click", handler1); // Grazie!
  elem.addEventListener("click", handler2); // Grazie di nuovo!

</script>
```

Come visto nell'esempio, possiamo impostare i gestori *in entrambi i modi* sia con l'ausilio di una proprietà DOM che di `addEventListener`. Generalmente però, scegliamo un solo approccio.


:::: warning Per alcuni eventi, i gestori funzionano solo con `addEventListener`
Esistono eventi che non possono essere assegnati tramite una proprietà DOM, ma solo con `addEventListener`.

Un esempio di ciò, è l'evento `DOMContentLoaded`, innescato quando viene completamente caricato il documento e costruita tutta la struttura del DOM.

```js
// non viene mai eseguito
document.onDOMContentLoaded = function() {
  alert("DOM costruito");
};
```

```js
// in questo modo funziona
document.addEventListener("DOMContentLoaded", function() {
  alert("DOM costruito");
});
```
Conseguentemente, `addEventListener` è più universale, benché questi eventi siano un'eccezione più che la regola.
::::

## Oggetto evento

Per gestire correttamente un evento, vorremmo saperne di più su cosa è avvenuto. Non solamente se è stato un "click" o un "keydown", ma, ad esempio, quali erano le coordinate del puntatore? Che tasto è stato premuto? E così via.

Quando c'è un evento, il browser crea un *oggetto evento* (event object), inserisce i dettagli al suo interno e lo passa come argomento al gestore.

Ecco un esempio per ottenere le coordinate dall'oggetto evento:

```html
<input type="button" value="Clicami" id="elem">

<script>
  elem.onclick = function(event) {
    // mostra il tipo di evento, l'elemento e le coordinate del click
    alert(event.type + " su " + event.currentTarget);
    alert("Coordinate: " + event.clientX + ":" + event.clientY);
  };
</script>
```

Alcune proprietà dell'oggetto `event`:

`event.type`
: Tipo di evento, in questo caso è un `"click"`.

`event.currentTarget`
: L'elemento che ha gestito l'evento. Questo è equivalente a `this`, ma se il gestore è una arrow function, o se il suo `this` è legato a qualcos'altro, possiamo usare `event.currentTarget`.

`event.clientX / event.clientY`
: Coordinate del cursore relative alla Window, per eventi del puntatore.

Esistono tante altre proprietà., molte delle quali dipendono dal tipo di evento: gli eventi della tastiera hanno un gruppo di proprietà, gli eventi del puntatore un altro ancora, e li studieremo più avanti quando andremo a vedere i vari eventi nel dettaglio.


:::: tip L'oggetto evento è disponibile anche nei gestori HTML
Anche se assegniamo un gestore dentro l'HTML, possiamo usare l'oggetto `evento`:

```html
<input type="button" onclick="alert(event.type)" value="Event type">
```

Questo è possibile perché quando il browser legge l'attributo, crea un gestore con questa forma:  `function(event) { alert(event.type) }`. Il primo argomento viene chiamato `"event"`, e il corpo è preso dall'attributo.
::::


## Gestori oggetto: handleEvent

Con `addEventListener` possiamo assegnare non solo una funzione, ma anche un oggetto. Quando viene generato un evento, viene chiamato il suo metodo `handleEvent`.

Ad esempio:

```html
<button id="elem">Cliccami</button>

<script>
  let obj = {
    handleEvent(event) {
      alert(event.type + " su " + event.currentTarget);
    }
  };

  elem.addEventListener('click', obj);
</script>
```

Come possiamo osservare, se `addEventListener` riceve un oggetto come gestore, allora chiama `obj.handleEvent(event)` nel caso ci sia un evento.

Possiamo usare anche una classe:

```html
<button id="elem">Cliccami</button>

<script>
  class Menu {
    handleEvent(event) {
      switch(event.type) {
        case 'mousedown':
          elem.innerHTML = "Premuto un pulsante del mouse";
          break;
        case 'mouseup':
          elem.innerHTML += "...e rilasciato.";
          break;
      }
    }
  }


  let menu = new Menu();
  elem.addEventListener('mousedown', menu);
  elem.addEventListener('mouseup', menu);

</script>
```

L'oggetto gestisce entrambi gli eventi. Nota bene che usando `addEventListener` dobbiamo impostare esplicitamente gli eventi affinché rimangano in ascolto.


Nel nostro esempio, l'oggetto `menu` rimane in ascolto solamente per `mousedown` e `mouseup`, e nessun altro tipo di evento.
Tuttavia, il metodo `handleEvent` non deve necessariamente fare tutto il lavoro da solo. Può infatti chiamare altri metodi specifici per tipologia di evento:

```html
<button id="elem">Cliccami</button>

<script>
  class Menu {
    handleEvent(event) {
      // mousedown -> onMousedown
      let method = 'on' + event.type[0].toUpperCase() + event.type.slice(1);
      this[method](event);
    }

    onMousedown() {
      elem.innerHTML = "Premuto il pulsante del mouse";
    }

    onMouseup() {
      elem.innerHTML += "...e rilasciato.";
    }
  }

  let menu = new Menu();
  elem.addEventListener('mousedown', menu);
  elem.addEventListener('mouseup', menu);
</script>
```

Qui i gestori sono chiaramente separati, il che può essere più comodo da gestire.

## Riepilogo

Ci sono 3 modalità per assegnare dei gestori di evento:

1. Attributo HTML: `onclick="..."`.
2. Proprietà DOM: `elem.onclick = function`.
3. Metodi: `elem.addEventListener(event, handler[, phase])` per aggiungerlo, `removeEventListener` per rimuoverlo.

Gli attributi HTML vengono usati raramente, perchè un JavaScript nel bel mezzo di un tag HTML, non solo è un po' strano, ma è anche avulso dal contesto. Inoltre in questo modo non vi si può inserire dentro tanto codice.

Le proprietà DOM si possono usare, ma non potremo assegnare più di un gestore per un particolare evento. In molti casi questa limitazione non è troppo pesante.

L'ultimo modo è il più flessibile, ma è anche il più lungo da scrivere. Alcuni eventi funzionano solo con quest'ultima modalità, ad esempio `transitionend` e `DOMContentLoaded` (affrontato più avanti). Inoltre `addEventListener` supporta gli oggetti come gestori di evento. In questo caso, però, verrà chiamato il metodo  `handleEvent` al verificarsi degli eventi.

Non importa come assegni un gestore, in ogni caso il primo argomento passato sarà un oggetto evento, contenente i dettagli su ciò che è avvenuto.

Nei prossimi capitoli, avremo modo di approfondire il tema degli eventi in generale e le loro differenti tipologie.

## Esercizi

### 1 · Nascondere al click

Aggiungi del codice JavaScript al pulsante `button` per nascondere `<div id="text">` al click.

Demo:

[Apri l’esempio nella fonte originale](https://it.javascript.info/introduction-browser-events).

::::: details Soluzione



:::::

### 2 · Nascondere sé stesso

Create un pulsante che nasconde sé stesso al click.


> [Esempio interattivo nell’articolo originale](https://it.javascript.info/introduction-browser-events).

::::: details Soluzione

Qui potete usare `this` nel gestore per fare riferimento all'"elemento stesso":

```html
<input type="button" onclick="this.hidden=true" value="Clicca per nascondere">
```

:::::

### 3 · Quale gestore verrà eseguito?

Nella variabile c'è un pulsante. Non vi sono gestori assegnati.

Dopo aver eseguito questo codice, quali gestori verranno eseguiti al click sul pulsante? Quale alert verrà mostrato?

```js
button.addEventListener("click", () => alert("1"));

button.removeEventListener("click", () => alert("1"));

button.onclick = () => alert(2);
```

::::: details Soluzione

Risposta: `1` e `2`.

Il primo gestore verrà innescato, poiché non viene rimosso da `removeEventListener`. Per rimuovere il gestore dobbiamo passare esattamente la stessa funzione che era stata assegnata. E nel codice viene passata una nuova funzione, che è identica, ma è comunque una nuova funzione.

Per poter rimuovere un oggetto funzione, dobbiamo salvarci un suo riferimento:

```js
function handler() {
  alert(1);
}

button.addEventListener("click", handler);
button.removeEventListener("click", handler);
```

Il gestore `button.onclick` aggiunto ad `addEventListener` funziona perfettamente.

:::::

### 4 · Sposta la palla sul campo

Sposta la palla sul campo al click. Così:

[Apri l’esempio nella fonte originale](https://it.javascript.info/introduction-browser-events).

Requisiti:

- Il centro della palla, al click, dovrà essere esattamente sotto il puntatore (possibilmente senza attraversare i bordi del campo).
- Le animazioni CSS sono ben accette.
- La palla non deve attraversare i confini del campo.
- Allo scroll della pagina, lo script non si deve rompere.

Note:

- Il codice dovrebbe funzionare anche con differenti tipi di palle e campi, senza essere legato a nessun valore prefissato.
- Usa le proprietà `event.clientX/event.clientY` per le coordinate del click.

::::: details Soluzione

Per prima cosa dobbiamo scegliere un metodo per posizionare la palla.

Non possiamo usare `position:fixed` per questo, perché lo scorrimento della pagina sposterebbe la palla dal campo.

Dobbiamo quindi usare `position:absolute` per la palla, e per rendere il posizionamento stabile, posizionare anche `field` stesso ("static" se non diversamente specificato). 

In questo modo a palla verrà posizionata in relazione al campo:

```css
#field {
  width: 200px;
  height: 150px;
  position: relative;
}

#ball {
  position: absolute;
  left: 0; /* relativo all'antenato più vicino (field) */
  top: 0;
  transition: 1s all; /* Una animazione CSS impostata su left/top fa volare la palla */
}
```

Il prossimo passo sarà quello di assegnare correttamente `ball.style.left/top`, le cui coordinate saranno relazionate alla dimensione del campo.

Osserviamo la figura:

![](/javascript-info/2-ui/2-events/01-introduction-browser-events/04-move-ball-field/move-ball-coords.svg)

`event.clientX/clientY` sono le coordinate del click relative alla window (N.d.T. l'oggetto window).

Per ottenere le coordinate `left` relative al campo, dobbiamo sottrarre il valore del limite sinistro del campo e la sua larghezza:

```js
let left = event.clientX - fieldCoords.left - field.clientLeft;
```

Normalmente, `ball.style.left` significa "limite destro dell'elemento" (la palla). Ma se assegnassimo questo valore di `left`, sotto il puntatore si verrebbe a posizionare, appunto, il limite destro della palla, e non il suo centro.

Per poter centrare la palla, dobbiamo spostarla tenendo conto della metà della sua altezza e metà della sua larghezza.

Quindi il `left` definitivo sarebbe:

```js
let left = event.clientX - fieldCoords.left - field.clientLeft - ball.offsetWidth/2;
```

Le coordinate in verticale vengono calcolate usando la stessa logica. 

Nota bene che larghezza e altezza della palla devono essere note nel momento in cui accediamo a  `ball.offsetWidth`. Dovrebbero essere specificate nell'HTML o nel CSS.

:::::

### 5 · Create un menù a scorrimento

Create un menù che si apra e chiuda al click:

[Apri l’esempio nella fonte originale](https://it.javascript.info/introduction-browser-events).

P.S.: HTML e CSS del codice della pagina andranno modificati.

::::: details Soluzione

#### HTML e CSS
Per prima cosa creiamo l'HTML ed il CSS.

Un menù è un componente grafico indipendente nella pagina, quindi è bene inserirlo all'interno di un singolo elemento genitore del DOM.

Una lista di elementi del menù può essere rappresentata da una lista di `ul/li`.

Ecco la struttura d'esempio:

```html
<div class="menu">
  <span class="title">Dolciumi (cliccami)!</span>
  <ul>
    <li>Torte</li>
    <li>Ciambelle</li>
    <li>Miele</li>
  </ul>
</div>
```

Usiamo `<span>` per il titolo perché `<div>`, avendo un `display:block` implicito, occuperebbe il 100% della larghezza disponibile.

```html
<div style="border: solid red 1px" onclick="alert(1)">Dolciumi (cliccami)!</div>
```

Impostando un `onclick` su di esso, intercetterà i click alla destra del testo.

Dato che `<span>` ha un `display: inline` implicito, occupa esattamente lo spazio necessario per la visualizzazione del testo:

```html
<span style="border: solid red 1px" onclick="alert(1)">Dolciumi (cliccami)!</span>
```

#### Azionamento del menù

L'azionamento del menù dovrebbe cambiare la direzione della freccia e mostrare/nascondere la lista degli elementi.

Tutte queste modifiche sono gestite perfettamente dai CSS. In JavaScript dovremmo solamente etichettare lo stato corrente del menù aggiungendo/rimuovendo la classe `.open`.

Senza di essa, il menù risulterebbe chiuso:

```css
.menu ul {
  margin: 0;
  list-style: none;
  padding-left: 20px;
  display: none;
}

.menu .title::before {
  content: '▶ ';
  font-size: 80%;
  color: green;
}
```

...invece con `.open`, la frecca si modifica e la lista si apre:

```css
.menu.open .title::before {
  content: '▼ ';
}

.menu.open ul {
  display: block;
}
```

:::::

### 6 · Aggiungete un pulsante di chiusura

Avete una lista di messaggi.

Aggiungete tramite JavaScript un pulsante di chiusura nell'angolo in alto a destra di ogni messaggio.

Il risultato dovrebbe essere simile a questo:

[Apri l’esempio nella fonte originale](https://it.javascript.info/introduction-browser-events).

::::: details Soluzione

Per aggiungere un pulsante possiamo usare sia `position:absolute` (e quindi il suo contenitore dovrà avere `position:relative`) oppure `float:right`. `float:right` ha il vantaggio di non fare sovrapporre il pulsante al testo,  `position:absolute` invece ci dà un po' più di libertà. La scelta è tua.

Quindi per ogni contenitore il codice potrebbe essere come questo:
```js
pane.insertAdjacentHTML("afterbegin", '<button class="remove-button">[x]</button>');
```

Il `<button>` diventa `pane.firstChild`, e gli possiamo aggiungere un gestore come questo:

```js
pane.firstChild.onclick = () => pane.remove();
```

:::::

### 7 · Carosello

Create un "carosello", una raccolta di immagini che possono essere fatte scorrere cliccando sulle frecce.

[Apri l’esempio nella fonte originale](https://it.javascript.info/introduction-browser-events).

Successivamente possiamo aggiungere più funzionalità: scorrimento infinito, caricamento dinamico etc.

P.S. Per questo compito, la struttura HTML/CSS rappresenta il 90% di tutta la soluzione.

::::: details Soluzione

Una striscia di immagini può essere rappresentata con una lista `ul/li` di immagini `<img>`.

Normalmente, sono strisce che si sviluppano tantissimo in larghezza, quindi creiamo un `<div>` a larghezza fissa attorno ad esse per "tagliarle", di modo che sia visibile sola una parte di esse:

![](/javascript-info/2-ui/2-events/01-introduction-browser-events/07-carousel/carousel1.svg)

Per rendere la lista visibile in orizzontale, dobbiamo applicare le proprietà CSS corrette per gli elementi `<li>`, come `display: inline-block`.

Per `<img>` dovremmo anche sistemare `display`, dato che per impostazione predefinita è `inline`. Ci sono spazi aggiuntivi riservati negli elementi `inline` per le "codine dei caratteri", e possiamo usare `display:block` per rimuoverle.

Per creare lo scorrimento possiamo spostare l'elemento `<ul>`. Ci sono varie maniere per farlo, ad esempio cambiando il `margin-left` oppure (prestazioni migliori) usare `transform: translateX()`:

![](/javascript-info/2-ui/2-events/01-introduction-browser-events/07-carousel/carousel2.svg)

Il `<div>` esterno avendo una larghezza fissa, fa sì che le immagini "in più" vengono tagliate.

Tutto il carosello è un "componente grafico" auto-contenuto nella pagina, quindi è bene avvolgerlo dentro un singolo `<div class="carousel">`, inserendo le stilizzazioni dentro quest'ultimo.

:::::

