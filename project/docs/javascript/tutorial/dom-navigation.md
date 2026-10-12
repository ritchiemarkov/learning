---
title: "Percorrere il DOM"
description: "JavaScript.info in italiano: Percorrere il DOM"
sourceTutorial: true
prev: {"text": "Alberatura DOM", "link": "/javascript/tutorial/dom-nodes"}
next: {"text": "Ricerca: getElement*, querySelector*", "link": "/javascript/tutorial/searching-elements-dom"}
---

# Percorrere il DOM

> **JavaScript.info · Ilya Kantor e contributori.** [Originale inglese](https://javascript.info/dom-navigation) · [Edizione italiana](https://it.javascript.info/dom-navigation) · [Fonti e licenza](/javascript/fonti).

Il DOM ci consente di fare qualsiasi cosa con gli elementi ed il loro contenuto, ma prima dobbiamo essere in grado di raggiungere l'oggetto DOM corrispondente.

Tutte le operazioni sul DOM iniziano con l'oggetto `document`. Questo è il principale "punto di ingresso" per il DOM, dal quale possiamo accedere a qualsiasi nodo.

Ecco un'immagine dei collegamenti che consentono di muoversi tra i nodi del DOM:

![](/javascript-info/2-ui/1-document/03-dom-navigation/dom-links.svg)

Esaminiamoli nel dettaglio.

## In cima: documentElement e body

I nodi in cima all'albero sono disponibili direttamente come proprietà di `document`:

`<html>` = `document.documentElement`
: Il nodo del DOM più in alto è `document.documentElement`, esso corrisponde al tag `<html>`.

`<body>` = `document.body`
: Un altro nodo DOM largamente utilizzato è l'elemento `<body>`, ossia `document.body`.

`<head>` = `document.head`
: Il tag `<head>` è disponibile come `document.head`.


:::: warning C'è un problema: `document.body` può essere `null`
Uno script non può accedere ad un elemento che non esiste al momento dell'esecuzione.

In particolare, se uno script si trova all'interno di `<head>`, `document.body` non è disponibile, perché il browser non lo ha ancora letto.

Quindi, nell'esempio sottostante, il primo `alert` mostra `null`:

```html
<html>

<head>
  <script>

    alert( "Da HEAD: " + document.body ); // null, <body> non esiste ancora

  </script>
</head>

<body>

  <script>
    alert( "Da BODY: " + document.body ); // HTMLBodyElement, ora <body> esiste
  </script>

</body>
</html>
```
::::


::: tip Nel mondo del DOM `null` significa "non esiste"
Nel DOM, il valore `null` significa "non esiste" o "nessun nodo trovato".
:::

## Nodi figli: childNodes, firstChild, lastChild

Ci sono due termini che useremo d'ora in poi:

- **Nodi figli** (children o child node) : elementi che sono figli diretti, ossia che sono annidati al primo livello del nodo specificato. Ad esempio, `<head>` e `<body>` sono figli dell'elemento `<html>`.
- **Discendenti** : Tutti gli elementi che sono annidati a qualsiasi livello nell'elemento specificato. Sono inclusi i figli, i figli dei figli, e così via.

Ad esempio, qui `<body>` ha come figli `<div>` e `<ul>` (ed alcuni nodi di testo vuoti):

```html
<html>
<body>
  <div>Inizio</div>

  <ul>
    <li>
      <b>Informazione</b>
    </li>
  </ul>
</body>
</html>
```

...E come discendenti di `<body>`, oltre a `<div>` e `<ul>`, abbiamo anche gli elementi annidati più in profondità, come `<li>` (figlio di  `<ul>`) e `<b>` (figlio di `<li>`). In pratica l'intero albero sotto a `<body>`.

**La collection `childNodes` raccoglie tutti i nodi figlio, inclusi quelli di testo**

L'esempio qui sotto mostra i figli di `document.body`:

```html
<html>
<body>
  <div>Inizio</div>

  <ul>
    <li>Informazione</li>
  </ul>

  <div>Fine</div>

  <script>

    for (let i = 0; i < document.body.childNodes.length; i++) {
      alert( document.body.childNodes[i] ); // Text, DIV, Text, UL, ..., SCRIPT
    }

  </script>
  ...altro...
</body>
</html>
```

Da notare un particolare interessante. Se eseguiamo l'esempio, l'ultimo elemento mostrato è `<script>`. Di fatto l'ultimo elemento sarebbe "...altro...", ma al momento dell'esecuzione dello script esso non è ancora stato letto, quindi non viene visto.

**Le proprietà `firstChild` e `lastChild` permettono un accesso più veloce al primo ed all'ultimo figlio.**

Sono delle semplici scorciatoie. Se sono presenti dei nodi figlio, allora le seguenti espressioni sono sempre vere :
```js
elem.childNodes[0] === elem.firstChild
elem.childNodes[elem.childNodes.length - 1] === elem.lastChild
```

Esiste anche la funzione speciale `elem.hasChildNodes()`, per verificare se sono presenti nodi figlio.

### DOM collections

Come possiamo vedere, `childNodes` sembra un array. Ma in realtà non è un array, ma piuttosto una *collection*: uno speciale oggetto iterabile, simile ad un array.

Questo comporta due importanti conseguenze:

1. Possiamo usare `for..of` per iterare:
  ```js
  for (let node of document.body.childNodes) {
    alert(node); // mostra tutti i nodi della collection
  }
  ```
  Questo perché è iterabile (ha la proprietà `Symbol.iterator` che contraddistingue gli iterabili).

2. I metodi degli array non funzionano, perché non è un array:
  ```js
  alert(document.body.childNodes.filter); // undefined (il metodo filter non c'è!)
  ```

Il primo punto è ottimo, il secondo è tollerabile. Infatti nel caso avessimo bisogno dei metodi degli array possiamo usare `Array.from` e creare un "vero" array a partire dalla collection:

  ```js
  alert( Array.from(document.body.childNodes).filter ); // function
  ```


::: warning Le DOM collections funzionano in sola lettura
Le DOM collections, ed in generale *tutte* le proprietà utili alla navigazione elencate in questo capitolo, funzionano in sola lettura.

Non possiamo sostituire un nodo figlio con qualcos'altro con l'assegnazione `childNodes[i] = ...`.

Modificare il DOM richiede l'utilizzo di altri metodi, che vedremo nel prossimo capitolo.
:::


::: warning Le DOM collections sono vive
Salvo poche eccezioni, tutte le DOM collections sono *vive*. In altre parole, riflettono lo stato corrente del DOM.

Se prendiamo come riferimento `elem.childNodes`, ed aggiungiamo o rimuoviamo nodi dal DOM, essi appariranno o scompariranno automaticamente dalla collection.
:::


:::: warning Non usare `for..in` per eseguire cicli sulle collections
Le collections sono iterabili usando `for..of`, ma a volte qualcuno prova ad usare `for..in`.

E' una pratica sconsigliata. I cicli `for..in` iterano su tutte le proprietà enumerabili, e le collections possiedono alcune proprietà "extra", che vengono usate raramente, e che in genere non vorremmo ci fossero restituite dal ciclo:

```html
<body>
<script>
  // mostra 0, 1, length, item, values ed altro.
  for (let prop in document.body.childNodes) alert(prop);
</script>
</body>
```

## I fratelli (*siblings*) ed il genitore (*parent*)

I fratelli sono nodi figli dello stesso genitore.

Ad esempio, qui `<head>` e `<body>` sono fratelli:

```html
<html>
  <head>...</head><body>...</body>
</html>
```

- `<body>` è chiamato fratello "successivo" o "a destra" di `<head>`,
- `<head>` è chiamato fratello "precedente" o "a sinistra" di `<body>`.

Il fratello successivo è nella proprietà `nextSibling`, quello precedente in `previousSibling`.

Il genitore è disponibile come `parentNode`.

Ad esempio

```js
// il genitore di <body> è <html>
alert( document.body.parentNode === document.documentElement ); // true

// dopo di <head> c'è <body>
alert( document.head.nextSibling ); // HTMLBodyElement

// prima di <body> c'è <head>
alert( document.body.previousSibling ); // HTMLHeadElement
```

## Navigazione solo tra elementi

Le proprietà di navigazione viste finora fanno riferimento a *tutti* i nodi. Ad esempio, in `childNodes` possiamo trovare: nodi elemento, nodi di testo, ed anche nodi commento se ce ne sono.

Ma per alcuni compiti non vogliamo nodi di testo o di commento. Vogliamo solo manipolare nodi che rappresentano i tags e che costituiscono la struttura della pagina.

Quindi vediamo altri collegamenti di navigazione che prendono in considerazione solo *nodi elemento*:

![](/javascript-info/2-ui/1-document/03-dom-navigation/dom-links-elements.svg)

I collegamenti sono simili a quelli visti prima, ma con l'aggiunta della parola `Element`:

- `children` -- solo i figli che sono nodi elemento.
- `firstElementChild`, `lastElementChild` -- il primo e l'ultimo elemento figlio.
- `previousElementSibling`, `nextElementSibling` -- gli elementi vicini.
- `parentElement` -- l'elemento genitore.


:::: tip Perché `parentElement`? Può un genitore *non* essere un elemento?
La proprietà `parentElement` restituisce l'elemento genitore, mentre `parentNode` restituisce "qualsiasi nodo" genitore. Queste proprietà in genere coincidono: entrambe restituiscono lo stesso genitore.

Con l'unica eccezione di `document.documentElement`:

```js
alert( document.documentElement.parentNode ); // document
alert( document.documentElement.parentElement ); // null
```

La ragione è che il nodo radice `document.documentElement` (`<html>`) ha `document` come genitore, ma document non è un nodo elemento, quindi `parentNode` lo restituisce, mentre `parentElement` no. 

Questo dettaglio può essere utile quando vogliamo risalire da un elemento arbitrario `elem` verso `<html>`, ma senza arrivare a `document`: 
```js
while(elem = elem.parentElement) { // su, fino a <html>
  alert( elem );
}
```
::::

Modifichiamo uno degli esempi sopra, sostituendo `childNodes` con` children`. Ora vengono mostrati solo gli elementi:

```html
<html>
<body>
  <div>Inizio</div>

  <ul>
    <li>Informazione</li>
  </ul>

  <div>Fine</div>

  <script>

    for (let elem of document.body.children) {
      alert(elem); // DIV, UL, DIV, SCRIPT
    }

  </script>
  ...
</body>
</html>
```

## Ulteriori collegamenti: tabelle
Finora abbiamo descritto le proprietà base per la navigazione.

Alcuni tipi di elemento DOM possono fornire proprietà aggiuntive, specifiche per il loro tipo.

Le tabelle ne sono un esempio, e rappresentano un caso particolarmente importante:

**L'elemento `<table>`** supporta (in aggiunta a quelle trattate sinora) le seguenti proprietà:
- `table.rows` -- la collection degli elementi `<tr>` della tabella.
- `table.caption/tHead/tFoot` -- riferimenti agli elementi `<caption>`, `<thead>`, `<tfoot>`.
- `table.tBodies` -- la collection degli elementi `<tbody>` (secondo lo standard possono essere molti, ma ce ne sarà sempre almeno uno. Anche se non è nell'HTML di origine, il browser lo inserirà automaticamente nel DOM).

**Gli elementi `<thead>`, `<tfoot>`, `<tbody>`** hanno la proprietà `rows`:
- `tbody.rows` -- la collection degli elementi `<tr>` contenuti.

**`<tr>`:**
- `tr.cells` -- la collection delle celle `<td>` e `<th>` contenute nel `<tr>` specificato.
- `tr.sectionRowIndex` -- la posizione (index) di un dato `<tr>` incluso in `<thead>/<tbody>/<tfoot>`.
- `tr.rowIndex` -- il numero di `<tr>` nella tabella nel suo insieme (include tutte le righe della tabella).

**`<td>` e `<th>`:**
- `td.cellIndex` -- il numero della celle all'interno del contenitore `<tr>`.

Un esempio di utilizzo:

```html
<table id="table">
  <tr>
    <td>uno</td><td>due</td>
  </tr>
  <tr>
    <td>tre</td><td>quattro</td>
  </tr>
</table>

<script>
  // estrai td con "two" (prima riga, seconda colonna)
  let td = table.rows[0].cells[1];
  td.style.backgroundColor = "red"; // evidenzialo
</script>
```

La specifica: [tabular data](https://html.spec.whatwg.org/multipage/tables.html).

Proprietà di navigazione aggiuntive, sono anche disponibili per i moduli HTML. Le esamineremo più avanti, quando inizieremo a lavorare con i moduli.

## Riepilogo

Dato un nodo DOM, possiamo spostarci tra i suoi vicini usando le proprietà di navigazione.

Ne esistono due tipi principali:

- Per tutti i nodi: `parentNode`, `childNodes`, `firstChild`, `lastChild`, `previousSibling`, `nextSibling`.
- Solo per i nodi elemento: `parentElement`, `children`, `firstElementChild`, `lastElementChild`, `previousElementSibling`, `nextElementSibling`.

Alcuni tipi di elemento DOM, es. le tabelle, 
Some types of DOM elements, e.g. tables, forniscono proprietà e collections aggiuntive per accedere al loro contenuto.
::::

## Esercizi

### 1 · Figli nel DOM

Guardiamo questa pagina:

```html
<html>
<body>
  <div>Utenti:</div>
  <ul>
    <li>John</li>
    <li>Pete</li>
  </ul>
</body>
</html>
```

Per ciascuno dei seguenti, fornire almeno un modo per accedervi:
- Il nodo DOM `<div>` ?
- Il nodo DOM `<ul>` ?
- Il secondo `<li>` (con Pete)?

::::: details Soluzione

E' possibile farlo in diversi modi, ad esempio:


Il nodo DOM `<div>`:

```js
document.body.firstElementChild
// oppure
document.body.children[0]
// oppure (il primo nodo è uno spazio, quindi prendiamo il secondo)
document.body.childNodes[1]
```

Il nodo DOM `<ul>`:

```js
document.body.lastElementChild
// oppure
document.body.children[1]
```

Il secondo `<li>` (con Pete):

```js
// prendi <ul>, e quindi il suo ultimo elemento figlio
document.body.lastElementChild.lastElementChild
```

:::::

### 2 · La questione dei fratelli

Se `elem` è un nodo arbitrario del DOM...

- E' vero che `elem.lastChild.nextSibling` è sempre `null`?
- E' vero che `elem.children[0].previousSibling` è sempre `null`?

::::: details Soluzione

1. Si, è vero. L'elemento `elem.lastChild` è sempre l'ultimo, non ha `nextSibling`.
2. No, è falso, perché `elem.children[0]` è il primo figlio tra i nodi di tipo *elemento*, ma potrebbero esserci nodi di tipo diverso. Ad esempio `previousSibling` potrebbe essere un nodo di testo.

Nota: in entrambi i casi, se non ci sono figli si verificherà un errore.

Se non ci sono figli, `elem.lastChild` è `null`, quindi non possiamo accedere a `elem.lastChild.nextSibling`. E la collection `elem.children` sarà vuota (come un array vuoto `[]`).

:::::

### 3 · Seleziona tutte le celle sulla diagonale

Scrivi il codice per evidenziare in rosso tutte celle sulla diagonale  della tabella.

Dovrai estrarre tutte i `<td>` in diagonale da `<table>` ed evidenziarli usando il codice:

```js
// td dovrebbe essere il riferimento alla cella della tabella
td.style.backgroundColor = 'red';
```

Il risultato dovrebbe essere:

[Apri l’esempio nella fonte originale](https://it.javascript.info/dom-navigation).

::::: details Soluzione

Useremo le proprietà `rows` e `cells` per accedere alle celle sulla diagonale della tabella.

:::::

