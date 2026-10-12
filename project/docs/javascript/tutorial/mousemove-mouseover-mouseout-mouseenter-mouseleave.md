---
title: "Movimenti del mouse: mouseover/out, mouseenter/leave"
description: "JavaScript.info in italiano: Movimenti del mouse: mouseover/out, mouseenter/leave"
sourceTutorial: true
prev: {"text": "Eventi del mouse", "link": "/javascript/tutorial/mouse-events-basics"}
next: {"text": "Drag'n'Drop con gli eventi del mouse", "link": "/javascript/tutorial/mouse-drag-and-drop"}
---

# Movimenti del mouse: mouseover/out, mouseenter/leave

> **JavaScript.info · Ilya Kantor e contributori.** [Originale inglese](https://javascript.info/mousemove-mouseover-mouseout-mouseenter-mouseleave) · [Edizione italiana](https://it.javascript.info/mousemove-mouseover-mouseout-mouseenter-mouseleave) · [Fonti e licenza](/javascript/fonti).

Entriamo nel dettaglio degli eventi generati quando il mouse si sposta tra gli elementi.

## Eventi mouseover/mouseout, relatedTarget

L'evento `mouseover` viene generato quando il puntatore del mouse passa su un elemento, e `mouseout` -- quando lo abbandona.

![](/javascript-info/2-ui/3-event-details/3-mousemove-mouseover-mouseout-mouseenter-mouseleave/mouseover-mouseout.svg)

Sono eventi particolari, perché posseggono la proprietà `relatedTarget`. Questa proprietà è complementare rispetto a `target`. Quando il mouse passa da un elemento a un altro, uno di questi diventa il `target`, e l'altro - `relatedTarget`.

Per `mouseover`:

- `event.target` -- é l'elemento appena raggiunto dal mouse.
- `event.relatedTarget` -- è l'elemento appena abbandonato dal mouse (`relatedTarget` -> `target`).

Per `mouseout`, invece, è esattamente il contrario:

- `event.target` -- è l'elemento appena lasciato dal mouse.
- `event.relatedTarget` -- è il nuovo elemento sotto il puntatore (`target` -> `relatedTarget`).


> [Esempio interattivo nell’articolo originale](https://it.javascript.info/mousemove-mouseover-mouseout-mouseenter-mouseleave).



::: warning `relatedTarget` può essere `null`
La proprietà `relatedTarget` può essere `null`.

È normale e significa solo che il mouse non proviene da un altro elemento della UI, ma esternamente rispetto alla finestra. Oppure può significare che l'ha appena lasciata (per l'evento `mouseover`). 

Dobbiamo tenere a mente questa eventualità, quando coinvolgiamo `event.relatedTarget` nel nostro codice, perché in queste condizioni, nel tentativo di accedere ad `event.relatedTarget.tagName`, andremmo incontro ad un errore.
:::

## Saltare elementi

L'evento `mousemove` viene attivato dal movimento del mouse. Tuttavia, ciò non significa che ogni pixel porterà ad un evento.

Il browser controlla la posizione del mouse di tanto in tanto. E se in questo frangente noterà qualche cambiamento, allora genererà degli eventi.

Ne consegue che, se l'utente muovesse il mouse molto velocemente, potrebbero essere "saltati" alcuni elementi del DOM:

![](/javascript-info/2-ui/3-event-details/3-mousemove-mouseover-mouseout-mouseenter-mouseleave/mouseover-mouseout-over-elems.svg)

Se il mouse si muovesse molto velocemente, passando dagli elementi `#FROM` a `#TO` appena illustrati, gli elementi `<div>` intermedi (o alcuni di essi) potrebbero essere ignorati. L'evento `mouseout` potrebbe essere generato su `#FROM` ed il successivo `mouseover` immediatamente su `#TO`.

Questo è sicuramente ottimo in termini di prestazioni, dal momento che potrebbero esserci tanti elementi intermedi. Non vogliamo veramente elaborare l'entrata e uscita per ognuno di essi.

D'altra parte, dovremmo anche tenere a mente che il puntatore del mouse non "visita" tutti gli elementi lungo il suo cammino. Può appunto "saltare" elementi.

In particolare, è possibile che il puntatore arrivi direttamente al centro della pagina, provenendo dall'esterno della finestra. In questo caso `relatedTarget` sarebbe `null`, non venendo da "nessuna parte":

![](/javascript-info/2-ui/3-event-details/3-mousemove-mouseover-mouseout-mouseenter-mouseleave/mouseover-mouseout-from-outside.svg)


> [Esempio interattivo nell’articolo originale](https://it.javascript.info/mousemove-mouseover-mouseout-mouseenter-mouseleave).



::: tip Se viene generato `mouseover`, allora deve esserci `mouseout`
Come appena detto, per movimenti sufficientemente rapidi, gli elementi intermedi potrebbero essere ignorati, ma una cosa è certa: se il puntatore entra "ufficialmente" dentro un elemento (quindi è stato generato l'evento `mouseover`), allora dopo averlo lasciato otterremo sempre un `mouseout`.
:::

## Mouseout quando si abbandona il genitore per un elemento figlio

Un'importante caratteristica di `mouseout` è che -- viene generato quando il puntatore si muove da un elemento verso un suo discendente, ad esempio da `#parent` verso `#child` come nel seguente HTML:

```html
<div id="parent">
  <div id="child">...</div>
</div>
```

Se siamo su `#parent` e spostiamo il mouse del tutto dentro `#child`, otteniamo un `mouseout` on `#parent`!

![](/javascript-info/2-ui/3-event-details/3-mousemove-mouseover-mouseout-mouseenter-mouseleave/mouseover-to-child.svg)

A prima vista può sembrare strano, ma la spiegazione è molto semplice.

**Coerentemente con la logica del browser, il puntatore del mouse può stare sopra un *solo* elemento per volta -- il più annidato e con il valore di z-index più alto.**

Quindi, se il puntatore si sposta su un altro elemento (anche nel caso di un suo discendente), allora lascia il precedente.

È bene porre la nostra attenzione ad un importante dettaglio sull'elaborazione dell'evento.

L'evento `mouseover` su un discendente "sale verso l'alto" (bubbling). Quindi, se `#parent` avesse un gestore `mouseover`, questo verrebbe attivato:

![](/javascript-info/2-ui/3-event-details/3-mousemove-mouseover-mouseout-mouseenter-mouseleave/mouseover-bubble-nested.svg)


> [Esempio interattivo nell’articolo originale](https://it.javascript.info/mousemove-mouseover-mouseout-mouseenter-mouseleave).


Si nota bene che quando il puntatore si muove dall'elemento `#parent` al `#child`, vengono attivati due gestori sull'elemento genitore: `mouseout` e `mouseover`:

```js
parent.onmouseout = function(event) {
  /* event.target: elemento genitore */
};
parent.onmouseover = function(event) {
  /* event.target: elemento figlio (bubbled) */
};
```

**Se non analizzassimo `event.target` dentro i gestori, potremmo essere portati a pensare che il puntatore lasci l'elemento genitore per poi di nuovo rientrarci subito dopo.**

Ma non è così. Il puntatore è ancora sul genitore, solo che si è mosso più internamente, dentro l'elemento figlio.

Se vi fossero degli eventi generati dall'abbandono dell'elemento genitore, ad esempio un'animazione eseguita al `parent.onmouseout`, nella maggioranza dei casi non vorremmo che si attivassero se il puntatore entrasse in profondità nel `#parent` andando dentro il figlio (anzi, in generale vorremmo che si attivassero solo quando il puntatore va all'esterno dell'area del `#parent`).

Quindi, per evitare questo, possiamo controllare `relatedTarget` nel gestore, e se il mouse è ancora dentro l'elemento, ignoriamo del tutto l'evento.

In alternativa, possiamo usare altri eventi: `mouseenter` e `mouseleave`, che affronteremo proprio adesso, che non sono affetti da queste problematiche.

## Eventi mouseenter e mouseleave

Gli eventi `mouseenter/mouseleave` si comportano come `mouseover/mouseout`. Vengono attivati quando il puntatore del mouse entra/lascia l'elemento.

Ma hanno due importanti differenze:

1. Le transizioni dentro l'elemento, da e verso i discendenti, non vengono considerate.
2. Gli eventi `mouseenter/mouseleave` non "risalgono" in bubbling.

Sono eventi estremamente semplici.

Quando il puntatore entra su un elemento -- viene generato `mouseenter`. La posizione esatta del puntatore dentro l'elemento o dei suoi discendenti è del tutto irrilevante.

Quando il puntatore lascia un elemento -- viene generato `mouseleave`.


> [Esempio interattivo nell’articolo originale](https://it.javascript.info/mousemove-mouseover-mouseout-mouseenter-mouseleave).


## Event delegation

Gli eventi `mouseenter/leave` sono molto semplici e facili da usare. Ma, abbiamo detto, non seguono la logica del bubbling. Quindi, con questi eventi non potremo mai usare la event delegation.

Ora immaginiamo di voler gestire il movimento del mouse, sia in entrata che in uscita dalle celle di una tabella. E immaginiamo anche che questa tabella abbia centinaia di celle.

La soluzione più naturale sarebbe quella di -- impostare un gestore su `<table>` per elaborare lì gli eventi. Ma il problema è che `mouseenter/leave` non fanno bubbling. Quindi se questi eventi avvengono su `<td>`, solo un gestore su `<td>` potrà catturarli.

I gestori per `mouseenter/leave` sulla `<table>` verrebbero generati solo se il puntatore entrasse ed uscisse dalla tabella, e sarebbe impossibile ottenere informazioni sugli spostamenti al suo interno.

Quindi, saremmo costretti ad usare `mouseover/mouseout`.

Cominciamo con dei semplici gestori che evidenziano gli elementi sotto il mouse:

```js
// evidenziamo un elemento sotto il puntatore
table.onmouseover = function(event) {
  let target = event.target;
  target.style.background = 'pink';
};

table.onmouseout = function(event) {
  let target = event.target;
  target.style.background = '';
};
```


> [Esempio interattivo nell’articolo originale](https://it.javascript.info/mousemove-mouseover-mouseout-mouseenter-mouseleave).


Nel nostro caso vogliamo gestire i passaggi tra le celle della tabella `<td>`: cioè quando entra in una cella lasciandone un'altra. Gli altri passaggi, come quelli all'interno o fuori da ogni altra celle, non ci interessano e li filtriamo.

Ecco come possiamo fare:

- Memorizzare l'attuale `<td>` evidenziata in una variabile, che chiameremo `currentElem`.
- Al `mouseover` -- ignorarlo se siamo ancora dentro l'elemento `<td>` corrente.
- Al `mouseout` -- ignorarlo se non abbiamo lasciato il `<td>` corrente.

Ecco un esempio di codice che tiene conto di tutte le combinazioni:

[js src="mouseenter-mouseleave-delegation-2/script.js"]

Ancora una volta, le caratteristiche da tenere in considerazione sono:
1. Usare la event delegation per gestire l'entrata/uscita dai `<td>` dentro la tabella. Quindi usare `mouseover/out` piuttosto che `mouseenter/leave`, in quanto questi ultimi, non facendo bubbling,  non permetterebbero la event delegation.
2. Gli eventi aggiuntivi, come lo spostamento del mouse tra gli elementi discendenti di `<td>` vanno esclusi, in modo da eseguire `onEnter/Leave` solo quando il puntatore entra o abbandona del tutto il `<td>`.


> [Esempio interattivo nell’articolo originale](https://it.javascript.info/mousemove-mouseover-mouseout-mouseenter-mouseleave).


## Riepilogo

Abbiamo visto gli eventi `mouseover`, `mouseout`, `mousemove`, `mouseenter` e `mouseleave`.

Queste sono le cose da evidenziare:

- Un rapido movimento del mouse può fare ignorare gli elementi intermedi.
- Gli eventi `mouseover/out` e `mouseenter/leave` posseggono una proprietà aggiuntiva: `relatedTarget` sarà l'elemento dal quale stiamo uscendo, o nel quale stiamo entrando, ed è complementare a `target`.

Gli eventi `mouseover/out` vengono generati anche quando andiamo dall'elemento genitore all'elemento figlio. Il browser assume che il mouse può stare su un solo elemento alla volta -- quello più annidato.

Gli eventi `mouseenter/leave` sono differenti da questo punto di vista: vengono scaturiti solo quando il mouse entra o esce del tutto da un elemento. Inoltre non sono soggetti al bubbling.

## Esercizi

### 1 · Comportamento del tooltip migliorato

Scrivete del codice JavaScript che mostri un tooltip su un elemento con un attributo `data-tooltip`. Il valore di questo attributo dovrebbe rappresentare il testo del tooltip.

Questo compito è come quello di [task/behavior-tooltip](https://it.javascript.info/task/behavior-tooltip), con la differenza che qui gli elementi delle annotazioni possono essere annidati. Deve essere mostrato il tooltip più annidato.

Può essere mostrato solo un tooltip alla volta.

Per esempio:

```html
<div data-tooltip="Qui – l'interno della casa" id="house">
  <div data-tooltip="Qui – il tetto" id="roof"></div>
  ...
  <a href="https://en.wikipedia.org/wiki/The_Three_Little_Pigs" data-tooltip="Leggi…">Hover su di me</a>
</div>
```

Il risultato dell'iframe:

[Apri l’esempio nella fonte originale](https://it.javascript.info/mousemove-mouseover-mouseout-mouseenter-mouseleave).

::::: details Soluzione



:::::

### 2 · "Smart" tooltip

Scrivete una funzione che mostri un tooltip su un elemento solo se l'utente sposta il mouse *su di esso*, e non *attraverso di esso*.

In altre parole, se il visitatore sposta il mouse su questo elemento e si ferma lì -- mostra il tooltip. Se invece ha solo spostato il mouse passandoci sopra, non ce n'è bisogno, d'altronde chi mai vorrebbe altri elementi lampeggianti non desiderati?

Tecnicamente, possiamo misurare la velocità del mouse su un elemento, e se è abbastanza lento possiamo supporre che sta arrivando proprio "sull'elemento", mostrando il tooltip, se è troppo veloce -- lo ignoriamo.

Creare un oggetto universale `new HoverIntent(options)` utile allo scopo.

Le opzioni possibili `options`:
- `elem` -- elemento da tracciare.
- `over` -- una funzione da chiamare se il mouse arriva sull'elemento: ossia, se si muove lentamente o se si ferma sull'elemento.
- `out` -- una funzione da chiamare quando il mouse abbandona l'elemento (se è stato chiamato `over`).

Ecco un esempio dell'uso di questo oggetto per il tooltip:

```js
// un tooltip di esempio
let tooltip = document.createElement('div');
tooltip.className = "tooltip";
tooltip.innerHTML = "Tooltip";

// l'oggetto tiene traccia del mouse e chiama over/out
new HoverIntent({
  elem,
  over() {
    tooltip.style.left = elem.getBoundingClientRect().left + 'px';
    tooltip.style.top = elem.getBoundingClientRect().bottom + 5 + 'px';
    document.body.append(tooltip);
  },
  out() {
    tooltip.remove();
  }
});
```

La demo:

[Apri l’esempio nella fonte originale](https://it.javascript.info/mousemove-mouseover-mouseout-mouseenter-mouseleave).

Muovendo il mouse oltre la velocità di "clock" non succede nulla, facendolo lentamente o fermandocisi sopra, viene mostrato il tooltip.

Nota bene: il tooltip non "lampeggia" quando il cursore si muove tra i sottoelementi dell'orologio.

::::: details Soluzione

L'algoritmo è semplice:
1. Impostare dei gestori `onmouseover/out` sull'elemento. Qui si possono anche usare `onmouseenter/leave`, però sono meno universali, e non funzionerebbero se introducessimo l'uso della delegation.
2. Quando il puntatore è entrato dentro l'elemento, si comincia a misurare la velocità al `mousemove`.
3. Se la velocità è lenta, eseguire `over`.
4. Quando si esce fuori dall'elemento, ed è stato eseguito `over`, eseguire `out`.

Ma come misurare la velocità?

La prima strategia potrebbe essere: eseguire una funzione ogni `100ms` e misurare la distanza tra le vecchie e nuove coordinate. Se fosse piccola, anche la velocità lo sarebbe.

Sfortunatamente, non c'è modo di ricavare "le coordinate attuali del mouse" in JavaScript. Non esistono funzioni come `getCurrentMouseCoordinates()`.

L'unico modo è di mettersi in ascolto sugli eventi del mouse, come `mousemove`, e prendere le coordinate dall'oggetto evento.

Quindi impostiamo un gestore su `mousemove` per tenere traccia delle coordinate e memorizzarle, per poi confrontarle ogni `100ms`.

P.S.: Nota bene: i test della soluzione fanno uso di `dispatchEvent` per vedere se il tooltip funziona bene.

:::::

