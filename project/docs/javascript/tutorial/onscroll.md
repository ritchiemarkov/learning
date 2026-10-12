---
title: "Scrolling"
description: "JavaScript.info in italiano: Scrolling"
sourceTutorial: true
prev: {"text": "Tastiera: keydown e keyup", "link": "/javascript/tutorial/keyboard-events"}
next: {"text": "Proprietà dei form e metodi", "link": "/javascript/tutorial/form-elements"}
---

# Scrolling

> **JavaScript.info · Ilya Kantor e contributori.** [Originale inglese](https://javascript.info/onscroll) · [Edizione italiana](https://it.javascript.info/onscroll) · [Fonti e licenza](/javascript/fonti).

L'evento `scroll` permette di reagire allo scroll della pagina o di un elemento. Ci sono poche e semplici operazioni che possiamo compiere in questi casi.

Per esempio:
- Mostrare/nascondere controlli aggiuntivi o informazioni, a seconda della posizione del documento in cui si trova l'utente.
- Caricare più dati quando l'utente scolla fino in fondo alla pagina.

Ecco una piccola funzione per mostrare lo scroll del documento:

```js
window.addEventListener('scroll', function() {
  document.getElementById('showScroll').innerHTML = window.pageYOffset + 'px';
});
```


> [Esempio interattivo nell’articolo originale](https://it.javascript.info/onscroll).


L'evento `scroll` funziona sia sulla `window` che sugli elementi scrollabili.

## Prevenire lo scrolling

Come possiamo rendere qualcosa non scrollabile?

Sicuramente, non possiamo prevenire lo scrolling usando `event.preventDefault()` nel listener `onscroll`, perché quest'ultimo viene generato *dopo* che lo scroll è avvenuto.

Tuttavia, possiamo prevenire lo scrolling con l'utilizzo di `event.preventDefault()` con altri eventi che permettono lo scroll, ad esempio l'evento `keydown` per `key:pageUp` e `key:pageDown`.

Se aggiungiamo un gestore a uno di questi eventi, utilizzando `event.preventDefault()`, allora lo scroll non comincerà affatto.

Ci sono vari modi per inizializzare uno scroll, al punto tale che spesso è più affidabile usare i CSS tramite la proprietà `overflow`.

Ecco alcune attività che potrete risolvere o analizzare per vedere le applicazioni di `onscroll`.

## Esercizi

### 1 · Pagina senza fine

Create una pagina senza fine. Quando un visitatore scrolla fino alla fine della pagina, la data attuale deve essere accodata (cosicché il visitatore possa scrollare ancora).

Come in questo esempio:

[Apri l’esempio nella fonte originale](https://it.javascript.info/onscroll).

È importante notare due caratteristeiche dello scroll:

1. **Lo scroll è "elastico".** Possiamo scrollare un po' oltre rispetto all'inizio o alla fine del documento in alcuni browser o dispositivi (verrà mostrato uno spazio vuoto, e subito dopo il documento "rimbalzerà indietro" in posizione normale).
2. **Lo scroll è impreciso.** Quando scrolliamo alla fine della pagina, potrebbe di fatto andare da 0 a 50px fuori dal reale bordo inferiore del documento.

Quindi, "scrollare fino alla fine" dovrebbe significare che il visitatore è a non più di 100px dalla fine del documento.

P.S. Nei casi reali, mostreremmo "più informazioni" o "più cose".

::::: details Soluzione

Il cuore della soluzione è una funzione che aggiunge continuamente contenuti nella pagina (o carica più cose nei casi reali) una volta arrivati alla fine del documento.

Possiamo chiamarla subito, ed aggiungerla come gestore di `window.onscroll`.

La domanda fondamentale è: "Come possiamo rilevare che la pagina è arrivata alla fine dello scroll?"

Usando le coordinate relative alla finestra.

Il documento è rappresentato (e contenuto) all'interno del tag `<html>`, che è `document.documentElement`.

Possiamo ottenere le coordinate relative alla finestra dell'intero documento con `document.documentElement.getBoundingClientRect()`, la proprietà `bottom` sarà la coordinata relativa alla finestra, della parte bassa del documento.

Per esempio, se l'altezza di tutti il documento HTML è `2000px`, allora avremo che:

```js
// quando siamo all'inizio della pagina
// il top rispetto alla finestra = 0
document.documentElement.getBoundingClientRect().top = 0

// la parte bassa relativa alla finestra = 2000
// il documento è lungo, quindi probabilmente andrà oltre il limite inferiore della finestra
document.documentElement.getBoundingClientRect().bottom = 2000
```

Se scrolliamo verso il basso di `500px`, avremo che:

```js
// la sommità del documento sta sopra la finestra di 500px
document.documentElement.getBoundingClientRect().top = -500
// la parte bassa del documento, invece, sarà 500px un po' più vicina
document.documentElement.getBoundingClientRect().bottom = 1500
```

Quando avremo scrollato la pagina fino alla fine, posto che l'altezza della finestrta sia di `600px`:


```js
// la sommità del documento starà sopra la finestra di 1400px
document.documentElement.getBoundingClientRect().top = -1400
// la parte bassa del documento sarà più in basso rispetto alla finestra di 600px
document.documentElement.getBoundingClientRect().bottom = 600
```

Notate bene che `bottom` non può essere `0`, perché non arriva mai all'inizio della finestra. Il limite basso delle coordinate di `bottom` è l'altezza della finestra (stiamo ponendo il caso che questa sia `600`), e non può scrollare più in alto.

Ricaviamo, quindi, l'altezza della finestra attraverso `document.documentElement.clientHeight`.

Per i nostri scopi, ci serve sapere momento in cui la fine del documento si troverà a non più di `100px`. (che è a: `600-700px`, se l'altezza è di `600`).

Ecco quindi la funzione:

```js
function populate() {
  while(true) {
    // fine del documento
    let windowRelativeBottom = document.documentElement.getBoundingClientRect().bottom;

    // se l'utente non ha scrollato abbastanza (>100px dalla fine)
    if (windowRelativeBottom > document.documentElement.clientHeight + 100) break;
    
    // aggiungiamo più dati
    document.body.insertAdjacentHTML("beforeend", `<p>Date: ${new Date()}</p>`);
  }
}
```

:::::

### 2 · Up/down button

Create un pulsante "inizio della pagina" per venire in aiuto con lo scroll della pagina.

Dovrebbe funzionare così:
- Se la pagina non è stata scrollata per almeno l'altezza della finestra, è invisibile.
- Se la pagina è stata scrollata per più dell'altezza della finestra, deve comparire una freccia "verso l'alto" nell'angolo in alto a sinistra. Se la pagina viene scrollata in alto, scompare.
- Se la freccia viene cliccata, la pagina scrolla verso l'alto.

Come in questo esempio (nell'angolo in alto a sinsitra, scrollare per vedere):

[Apri l’esempio nella fonte originale](https://it.javascript.info/onscroll).

::::: details Soluzione



:::::

### 3 · Caricare immagini visibili

Ipotizziamo di avere un client con connessione lenta e di voler far risparmiare un po' di traffico dal dispositivo mobile.

A questo proposito, decidiamo di non caricare immediatamente le immagini, ma piuttosto di sostituirle con dei segnaposto, così:

```html
<img src="placeholder.svg" width="128" height="128" data-src="real.jpg">
```

Quindi, inizialmente tutte le immagini saranno sostituite da un segnaposto `placeholder.svg`. Quando la pagina viene scrollata fino alla posizione in cui possiamo vedere le singole immagini, andiamo a modificare l'attributo `src` sostituendolo con il valore del `data-src`, in modo che l'immagine venga finalmente caricata.

Ecco un esempio dentro l'`iframe`:

[Apri l’esempio nella fonte originale](https://it.javascript.info/onscroll).

Scrollare per vedere le immagini "a richiesta".

Requisiti:
- Quando la pagina viene caricata, le immagini che sono sullo schermo dovrebbero caricarsi immediatamente, prima di qualunque scroll.
- Alcune immagini potrebbero essere normali, prive dell'attributo `data-src`. Queste immagini non dovrebbero essere influenzate dal nostro codice.
- Una volta che l'immagine viene caricata, non dovrebbe più caricarsi, a prescindere che se si stia scrollando oltre o che l'elemento che la contenga torni nuovamente ad essere visibile sullo schermo.

P.S. Se potete, create una soluzione avanzata che effettui un "preload" delle immagini che sono poco sotto la posizione attuale.

P.P.S. Si deve gestire solamente lo scroll verticale, e non quello orizzontale.

::::: details Soluzione

Il gestore `onscroll` dovrebbe controllare quali immagini sono visibili e mostrarle.

Vogliamo anche eseguirla al caricamento della pagina, per rilevare immediatamente le immagini visibili e caricarle.

Il codice dovrebbe essere eseguito al caricamento del documento, in modo che abbia accesso al suo contenuto.

Oppure, per fare ciò, si potrebbe mettere alla del `<body>`:

```js
// ...il contenuto della pagina sta sopra...

function isVisible(elem) {

  let coords = elem.getBoundingClientRect();

  let windowHeight = document.documentElement.clientHeight;

  // il bordo superiore dell'elemento risulta visibile?
  let topVisible = coords.top > 0 && coords.top < windowHeight;

  // il bordo inferiore risulta visibile?
  let bottomVisible = coords.bottom < windowHeight && coords.bottom > 0;

  return topVisible || bottomVisible;
}
```

The `showVisible()` function uses the visibility check, implemented by `isVisible()`, to load visible images:

```js
function showVisible() {
  for (let img of document.querySelectorAll('img')) {
    let realSrc = img.dataset.src;
    if (!realSrc) continue;

    if (isVisible(img)) {
      img.src = realSrc;
      img.dataset.src = '';
    }
  }
}


showVisible();
window.onscroll = showVisible;

```

P.S. La soluzione ha anche una variante di `isVisible` che "precarica" le immagini che sono distano solo una pagina di scroll sopra o sotto lo scroll corrente del documento.

:::::

