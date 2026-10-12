---
title: "Dimensioni dell'elemento e barra di scorrimento"
description: "JavaScript.info in italiano: Dimensioni dell'elemento e barra di scorrimento"
sourceTutorial: true
prev: {"text": "Stili e classi", "link": "/javascript/tutorial/styles-and-classes"}
next: {"text": "Dimensioni e scorrimento della finestra del browser", "link": "/javascript/tutorial/size-and-scroll-window"}
---

# Dimensioni dell'elemento e barra di scorrimento

> **JavaScript.info · Ilya Kantor e contributori.** [Originale inglese](https://javascript.info/size-and-scroll) · [Edizione italiana](https://it.javascript.info/size-and-scroll) · [Fonti e licenza](/javascript/fonti).

Ci sono molte proprietà JavaScript che ci consentono di leggere informazioni circa la larghezza, l'altezza e altre proprietà geometriche di un elemento.

Spesso ne abbiamo bisogno quando spostiamo o posizioniamo gli elementi in JavaScript.

## Esempio dimostrativo

Useremo l'elemento indicato sotto quale esempio di tali proprietà:

```html
<div id="example">
  ...Text...
</div>
<style>
  #example {
    width: 300px;
    height: 200px;
    border: 25px solid #E8C48F;
    padding: 20px;              
    overflow: auto;             
  }
</style>
```

Questo elemento possiede bordi, padding e barra di scorrimento: l'intero insieme delle proprietà. Non ci sono margini, in quanto questi non fanno parte dell'elemento stesso, e non ci sono proprietà speciali.

L'elemento si presenta così:

![](/javascript-info/2-ui/1-document/09-size-and-scroll/metric-css.svg)

Potete [visualizzare il documento nella sandbox](https://javascript.info/size-and-scroll).


::: tip Prestate attenzione alla barra di scorrimento
L'immagine sopra rappresenta il caso più complesso, quello in cui l'elemento possiede una barra di scorrimento. Alcuni browser (non tutti) ricavano lo spazio per la barra prendendolo dall'area del contenuto (indicata sopra come "content width").

Senza la barra di scorrimento, pertanto, l'area del contenuto sarebbe `300px`, ma se la barra di scorrimento è larga `16px` (la larghezza è variabile in base al dispositivo ed al browser) allora rimane soltanto `300 - 16 = 284px`, ed è questa la misura che dovremmo tenere in considerazione. Ecco perché gli esempi di questo capitolo presumono che ci sia una barra di scorrimento. Senza questa, alcuni calcoli sarebbero più semplici.
:::


::: tip L'area del `padding-bottom` può essere occupata dal testo
Di solito gli spazi definiti dai padding sono rappresentati vuoti nelle immagini, ma se nell'elemento c'è molto testo ed eccede l'area del contenuto, in quel caso è normale che il browser mostri il testo eccedente nel `padding-bottom`.
:::

## Proprietà geometriche

Ecco un'immagine riassuntiva delle proprietà geometriche:

![](/javascript-info/2-ui/1-document/09-size-and-scroll/metric-all.svg)

I valori di tali proprietà sono tecnicamente numerici, ma questi numeri sottintendono l'unità di misura pixel, stiamo parlando quindi delle dimensioni espresse in pixel.

Cominciamo ad esplorare le proprietà partendo dall'esterno dell'elemento.

## offsetParent, offsetLeft/Top

Queste proprietà sono raramente necessarie, ma sono comunque le proprietà geometriche "più esterne" e pertanto cominceremo da esse.

La proprietà `offsetParent` contiene un riferimento all'antenato più vicino, usato dal browser per il calcolo delle coordinate durante il rendering.

L'antenato più vicino è uno dei seguenti:

1. l'elemento contenitore più prossimo posizionato tramite CSS (la cui proprietà `position` sia `absolute`, `relative`, `fixed` o `sticky`),  oppure
2. `<td>`, `<th>`, `<table>`,  oppure
3. `<body>`.

Le proprietà `offsetLeft/offsetTop` forniscono le coordinate x/y relative all'angolo in alto a sinistra di `offsetParent`.

Nell'esempio di seguito il `<div>` interno ha `<main>` come `offsetParent` e `offsetLeft/offsetTop` lo spostano dall'angolo in alto a sinistra di questo (`180`):

```html
<main style="position: relative" id="main">
  <article>
    <div id="example" style="position: absolute; left: 180px; top: 180px">...</div>
  </article>
</main>
<script>
  alert(example.offsetParent.id); // main
  alert(example.offsetLeft); // 180 (nota: un numero, non una stringa "180px")
  alert(example.offsetTop); // 180
</script>
```

![](/javascript-info/2-ui/1-document/09-size-and-scroll/metric-offset-parent.svg)

Ci sono alcune circostanze in cui `offsetParent` è `null`:

1. Per gli elementi nascosti (`display:none` oppure non inseriti nel documento).
2. Per `<body>` e `<html>`.
3. Per gli elementi con `position:fixed`.

## offsetWidth/Height

Adesso occupiamoci dell'elemento stesso.

Queste due proprietà sono le più semplici. Forniscono la larghezza e l'altezza "esterne" dell'elemento, o, in altre parole, le sue dimensioni bordi compresi.

![](/javascript-info/2-ui/1-document/09-size-and-scroll/metric-offset-width-height.svg)

In riferimento al nostro esempio:

- `offsetWidth = 390` -- la larghezza esterna, risultante dalla larghezza interna (la proprietà CSS `width` pari a `300px`) più i padding (`2 * 20px`) ed i bordi (`2 * 25px`).
- `offsetHeight = 290` -- l'altezza esterna.


:::: tip Le proprietà geometriche valgono zero/null per gli elementi nascosti
Le proprietà geometriche sono calcolate solo per gli elementi visibili.

Se un elemento (o uno dei suoi antenati) ha `display:none` o non è nel documento, allora tutte le proprietà geometriche valgono zero (o `null` per `offsetParent`).

Per esempio, `offsetParent` vale `null`, e `offsetWidth`, `offsetHeight` sono `0` quando abbiamo creato un elemento, ma non lo abbiamo ancora inserito nel documento, o esso (o un suo antenato) ha `display:none`.

Possiamo servirci di questa particolarità per verificare se un elemento è nascosto, in questo modo:

```js
function isHidden(elem) {
  return !elem.offsetWidth && !elem.offsetHeight;
}
```

Si noti che questa funzione `isHidden` restituisce `true` anche per gli elementi che sono presenti sullo schermo, ma hanno dimensioni pari a zero (come un `<div>` vuoto).
::::

## clientTop/Left

I bordi fanno parte dell'elemento.

Per misurarli abbiamo a disposizione le proprietà `clientTop` e `clientLeft`.

Nel nostro esempio:

- `clientLeft = 25` -- larghezza bordo sinistro
- `clientTop = 25` -- larghezza bordo superiore

![](/javascript-info/2-ui/1-document/09-size-and-scroll/metric-client-left-top.svg)

...ma per essere precisi, queste proprietà non indicano la dimensione del bordo, piuttosto le coordinate relative del lato interno rispetto al lato esterno.

Qual è la differenza?

La differenza è percepibile quando il testo del documento è da destra verso sinistra (se il sistema operativo è in lingua araba o ebraica). In quel caso la barra di scorrimento non è a destra, ma a sinistra, e quindi `clientLeft` include anche la larghezza della barra.

In questa ipotesi `clientLeft` non sarebbe `25`, ma, considerata la larghezza della barra di scorrimento, sarebbe `25 + 16 = 41`.

A seguire l'esempio in ebraico:

![](/javascript-info/2-ui/1-document/09-size-and-scroll/metric-client-left-top-rtl.svg)

## clientWidth/Height

Queste proprietà forniscono la dimensione dell'area dentro i bordi dell'elemento.

Includono l'area del contenuto ed i padding ma non la barra di scorrimento:

![](/javascript-info/2-ui/1-document/09-size-and-scroll/metric-client-width-height.svg)

Nell'immagine sopra soffermiamo prima l'attenzione su `clientHeight`.

Non c'è una barra di scorrimento orizzontale, pertanto equivale esattamente alla somma di quanto è compreso tra i bordi: la misura dell'altezza espressa nei CSS `200px` più il padding superiore e quello inferiore (`2 * 20px`) per un totale di `240px`.

Esaminiamo ora `clientWidth`, in questo caso l'area del contenuto non coincide con i `300px` espressi nei CSS, ma è `284px`, perché la barra di scorrimento occupa `16px`. La somma è quindi `284px` più i padding sinistro e destro, per un totale di `324px`.

**Se non ci sono padding, allora `clientWidth/Height` coincidono esattamente con l'area del contenuto (content width) all'interno dei bordi e delle barre di scorrimento (se presenti).**

![](/javascript-info/2-ui/1-document/09-size-and-scroll/metric-client-width-nopadding.svg)

In assenza di padding, dunque, possiamo usare `clientWidth/clientHeight` per ricavare la dimensione dell'area del contenuto.

## scrollWidth/Height

Queste proprietà sono come `clientWidth/clientHeight`, ma includono anche le parti (non visibili) fuori dall'area di scorrimento:

![](/javascript-info/2-ui/1-document/09-size-and-scroll/metric-scroll-width-height.svg)

Nell'immagine sopra:

- `scrollHeight = 723` -- è l'intera altezza del contenuto, include le parti fuori dall'area visibile di scorrimento.
- `scrollWidth = 324` -- è l'intera larghezza, dal momento che non c'è barra di scorrimento orizzontale equivale a `clientWidth`.

Possiamo servirci di queste proprietà per espandere l'elemento fino alla sua larghezza/altezza completa.

In questo modo:

```js
// espande l'elemento fino alla sua altezza completa
element.style.height = `${element.scrollHeight}px`;
```


> [Esempio interattivo nell’articolo originale](https://it.javascript.info/size-and-scroll).


## scrollLeft/scrollTop

Le proprietà `scrollLeft/scrollTop` sono la larghezza/altezza delle parti di un elemento nascoste e fuori dall'area visibile di scorrimento.

Nell'immagine sotto possiamo osservare la rappresentazione di `scrollHeight` e `scrollTop` per un blocco soggetto a scorrimento verticale.

![](/javascript-info/2-ui/1-document/09-size-and-scroll/metric-scroll-top.svg)

In altre parole, con `scrollTop` si intende "quanto l'elemento è stato fatto scorrere verso l'alto".


:::: tip `scrollLeft/scrollTop` possono essere modificate
La maggior parte delle proprietà geometriche trattate sono in sola lettura, ma `scrollLeft/scrollTop` possono essere modificate, e il browser farà scorrere il contenuto.


> [Esempio interattivo nell’articolo originale](https://it.javascript.info/size-and-scroll).


Impostare `scrollTop` a `0` o su un grande valore, come `1e9`, farà sì che l'elemento scorrerà rispettivamente verso l'estremità superiore o inferiore.
::::

## Non ricavare la larghezza o l'altezza dai CSS

Abbiamo appena trattato le proprietà geometriche degli elementi DOM che usiamo per ricavare larghezza, altezza e per calcolare le distanze.

Ma come abbiamo imparato dal capitolo [Stili e classi](/javascript/tutorial/styles-and-classes), possiamo ottenere la larghezza e l'altezza CSS tramite `getComputedStyle`.

Dunque, perché non leggere la larghezza di un elemento con `getComputedStyle` in questo modo?

```js
let elem = document.body;

alert( getComputedStyle(elem).width ); // mostra la larghezza CSS per elem
```

Perché invece dovremmo usare le proprietà geometriche? Ci sono due ragioni:

1. La prima, le proprietà CSS `width/height` dipendono da un'altra proprietà: `box-sizing` che definisce "cosa siano" la larghezza e l'altezza CSS. Una modifica in `box-sizing` per scopi riguardanti i CSS possono rompere un JavaScript che fa affidamento su questa.
2. La seconda, le proprietà CSS `width/height` possono valere `auto`, ad esempio per un elemento inline:

    ```html
    <span id="elem">Hello!</span>

    <script>
    
      alert( getComputedStyle(elem).width ); // auto
    
    </script>
    ```

    Dal punto di vista dei CSS, `width:auto` è perfettamente normale, ma in JavaScript abbiamo bisogno di un'esatta dimensione in `px` da usare nei calcoli. In questo caso, quindi, la larghezza CSS è inutile.

Ma c'è un'altra ragione: la barra di scorrimento. Talvolta un codice che funziona bene senza barra di scorrimento, con questa diventa difettoso, perché la barra di scorrimento su alcuni browser ricava il suo spazio dall'area del contenuto. La larghezza effettiva per il contenuto, dunque, è *minore* della larghezza CSS e `clientWidth/clientHeight` ne tengono conto.

...Ma con `getComputedStyle(elem).width` la situazione è differente. Alcuni browser (es. Chrome) restituiscono la larghezza interna effettiva, meno la barra di scorrimento, mentre altri (es. Firefox) la larghezza CSS (ignorando la barra di scorrimento). Queste inconsistenze cross-browser costituiscono il motivo per il quale non usare `getComputedStyle` ma piuttosto fare affidamento sulle proprietà geometriche.


> [Esempio interattivo nell’articolo originale](https://it.javascript.info/size-and-scroll).

Si noti che la discrepanza descritta riguarda solo la lettura di `getComputedStyle(...).width` tramite JavaScript, dal punto di vista visuale non ci sono differenze.

## Riepilogo

Gli elementi hanno le seguenti proprietà geometriche:

- `offsetParent` -- è l'antenato più vicino posizionato (cioè con proprietà `position` diversa da `static`), oppure `td`, `th`, `table`, `body`.
- `offsetLeft/offsetTop` -- le coordinate relative all'angolo in alto a sinistra di `offsetParent`.
- `offsetWidth/offsetHeight` -- la larghezza/altezza "esterne" di un elemento bordi inclusi.
- `clientLeft/clientTop` -- le distanze dell'angolo esterno superiore sinistro dall'angolo interno (contenuto + padding) superiore sinistro. Per le lingue da sinistra verso destra corrispondono sempre alla larghezza dei bordi superiore e sinistro. Per le lingue da destra verso sinistra la barra di scorrimento verticale è a sinistra, quindi `clientLeft` include anche la larghezza della barra.
- `clientWidth/clientHeight` -- la larghezza/altezza del contenuto, padding inclusi ma senza la barra di scorrimento.
- `scrollWidth/scrollHeight` -- la larghezza/altezza del contenuto, proprio come `clientWidth/clientHeight`, ma comprende anche la parte di un elemento nascosta e fuori dall'area visibile di scorrimento.
- `scrollLeft/scrollTop` -- la larghezza/altezza della parte superiore di un elemento fuori dall'area visibile di scorrimento, partendo dal suo angolo in alto a sinistra.

Tutte le proprietà sono in sola lettura tranne `scrollLeft/scrollTop` che, se modificate, fanno scorrere il contenuto nel browser.

## Esercizi

### 1 · Qual è la misura dello scorrimento verso il basso?

La proprietà `elem.scrollTop` è la misura della parte superiore di un elemento fuori dall'area di scorrimento. Come ottenere la misura della parte inferiore (chiamiamola `scrollBottom`)?

Scrivete il codice che funzioni per un elemento arbitrario `elem`.

P.S. Verificate il vostro codice: se non c'è scorrimento o è stato effettuato tutto lo scorrimento verso il basso, allora dovrebbe restituire `0`.

::::: details Soluzione

La soluzione è:

```js
let scrollBottom = elem.scrollHeight - elem.scrollTop - elem.clientHeight;
```

In altre parole: (altezza totale) meno (misura dello scorrimento dall'alto) meno (altezza dell'area di scorrimento visibile). Il risultato è esattamente la misura della parte inferiore che resta da scorrere.

:::::

### 2 · Qual è la larghezza della barra di scorrimento?

Scrivete il codice che restituisca la larghezza di una barra di scorrimento standard.

Per Windows solitamente varia tra `12px` e `20px`. Se il browser non le riserva alcuno spazio (capita che la barra di scorrimento appaia semi-opaca sopra il testo), allora può essere `0px`.

P.S. Il codice dovrebbe funzionare per ogni documento HTML indipendentemente dal contenuto.

::::: details Soluzione

Per ricavare la larghezza della barra di scorrimento, possiamo creare un elemento con scorrimento ma senza bordi e padding.

In quel caso la sottrazione tra la larghezza totale `offsetWidth` e la larghezza dell'area interna del contenuto `clientWidth` equivarrà esattamente alla larghezza della barra di scorrimento:

```js
// creiamo un div con scorrimento
let div = document.createElement('div');

div.style.overflowY = 'scroll';
div.style.width = '50px';
div.style.height = '50px';

// dobbiamo inserirlo nel flusso del documento, altrimenti le dimensioni saranno pari a 0
document.body.append(div);
let scrollWidth = div.offsetWidth - div.clientWidth;

div.remove();

alert(scrollWidth);
```

:::::

### 3 · Posiziona la palla al centro del campo

Ecco come si presenta il documento di partenza:

[Apri l’esempio nella fonte originale](https://it.javascript.info/size-and-scroll).

Quali sono le coordinate del centro del campo?

Calcolale e usale per posizionare la palla al centro del campo verde:

[Apri l’esempio nella fonte originale](https://it.javascript.info/size-and-scroll).

- L'elemento dovrebbe essere spostato con JavaScript, non con i CSS.
- Il codice dovrebbe funzionare anche con una dimensione della palla differente (`10`, `20`, `30` pixel) e qualunque dimensione del campo: non dovrebbe essere legato a valori noti.

P.S. Certamente, il posizionamento al centro potrebbe essere ottenuto con i CSS, ma qui vi chiediamo di farlo proprio con JavaScript. Più avanti incontreremo altri casi e situazioni più complesse in cui JavaScript è l'unica alternativa. Ora ci stiamo solo "scaldando".

::::: details Soluzione

La palla ha `position:absolute`. Ciò significa che le coordinate `left/top` sono relative all'elemento posizionato più prossimo, cioè `#field` (perché ha `position:relative`).

Le coordinate sono a partire dall'angolo interno superiore sinistro del campo:

![](/javascript-info/2-ui/1-document/09-size-and-scroll/4-put-ball-in-center/field.svg)

Le dimensioni interne del campo si calcolano con `clientWidth/clientHeight`. I valori delle coordinate del centro del campo, quindi, si ottengono con `(clientWidth/2, clientHeight/2)`.

...Ma se impostiamo tali valori per `ball.style.left/top`, allora si troverebbe al centro non la palla ma il suo bordo superiore sinistro:

```js
ball.style.left = Math.round(field.clientWidth / 2) + 'px';
ball.style.top = Math.round(field.clientHeight / 2) + 'px';
```

Ecco cosa otterremmo:

[Apri l’esempio nella fonte originale](https://it.javascript.info/size-and-scroll).

Per allineare il centro della palla con il centro del campo, dovremmo spostare la palla alla metà della sua larghezza a sinistra ed alla metà della sua altezza verso l'alto:

```js
ball.style.left = Math.round(field.clientWidth / 2 - ball.offsetWidth / 2) + 'px';
ball.style.top = Math.round(field.clientHeight / 2 - ball.offsetHeight / 2) + 'px';
```

Adesso la palla è finalmente centrata.


:::: warning Attenzione: c'è una difficoltà imprevista!

Il codice non funzionerà in modo affidabile finché `<img>` non avrà larghezza ed altezza definite:

```html
<img src="ball.png" id="ball">
```
::::

Quando il browser non conosce le dimensioni di un'immagine (dagli attributi del tag o dai CSS), allora assume che siano pari a `0` finché l'immagine non completa il caricamento.

Pertanto il valore di `ball.offsetWidth` sarà `0` fino al momento in cui l'immagine non viene caricata. Questo causerà coordinate errate nel codice sopra.

Dopo il primo caricamento, il browser solitamente mette in cache l'immagine, e ne ricorderà subito le dimensioni se la dovesse ricaricare. Al primo caricamento, tuttavia, il valore di `ball.offsetWidth` è `0`.

Dovremmo correggere aggiungendo `width/height` a `<img>`:

```html
<img src="ball.png" width="40" height="40" id="ball">
```

...o fornire le dimensioni nei CSS:

```css
#ball {
  width: 40px;
  height: 40px;
}
```

:::::

### 4 · Indica le differenze tra la proprietà width CSS e clientWidth

Quali sono le differenze tra `getComputedStyle(elem).width` e `elem.clientWidth`?

Indica almeno 3 differenze. Più sono meglio è.

::::: details Soluzione

Differenze:

1. `clientWidth` è un valore numerico, `getComputedStyle(elem).width` invece restituisce una stringa con `px` alla fine.
2. `getComputedStyle` può restituire una larghezza non numerica come `"auto"` per un elemento inline.
3. `clientWidth` è l'area del contenuto interna di un elemento più il padding, mentre la proprietà width dei CSS (con il valore predefinito di `box-sizing`) è l'area del contenuto interna *senza il padding*.
4. Se c'è una barra di scorrimento ed il browser le riserva uno spazio, alcuni browser sottraggono quello spazio alla larghezza impostata tramite CSS (perché non è più disponibile per i contenuti), e altri invece no. La proprietà `clientWidth` è sempre la stessa: se la barra di scorrimento ha uno spazio riservato viene sottratto all'area del contenuto.

:::::

