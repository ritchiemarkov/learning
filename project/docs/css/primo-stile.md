# 01 · Il primo foglio di stile

**Obiettivo:** collegare HTML e CSS e osservare una regola nel browser.

## Due file, un documento

Crea `index.html` e `stile.css` nella stessa cartella. Parti da un documento completo con lingua, titolo e viewport, come nella [prima lezione HTML](/html/prima-pagina). Nel suo `head` inserisci:

```html
<link rel="stylesheet" href="stile.css">
```

Nel `body` aggiungi un `h1` e un paragrafo. Nel file CSS scrivi:

```css
body {
  color: #17382d;
  background-color: #f4f8f5;
  font-family: system-ui, sans-serif;
}
h1 { color: #17634d; }
```

Un **selettore** sceglie gli elementi; il blocco fra graffe contiene **dichiarazioni**. Ogni dichiarazione ha una proprietà, due punti, un valore e un punto e virgola. CSS descrive la presentazione: il documento HTML conserva significato e ordine.

## Dove può vivere CSS

Un file esterno si riusa fra pagine. Un elemento `style` contiene un foglio incorporato. L'attributo `style` contiene dichiarazioni inline, senza selettore: è utile in alcuni casi dinamici ma rende più difficile gestire molte pagine. Il corso parte dal file esterno.

Un commento CSS usa `/* ... */`, non `<!-- ... -->`. Un valore non valido viene normalmente ignorato; un selettore non valido può rendere inutilizzabile la regola, secondo la grammatica della lista. Graffe o commenti non chiusi possono coinvolgere più testo del previsto. Non contare sulla riparazione per organizzare il codice.

```css
/* Una classe riutilizzabile */
.introduzione {
  max-width: 65ch;
  line-height: 1.6;
}
```

## Verificare che il file sia caricato

Apri DevTools e controlla Network: il percorso deve puntare al file giusto e non a una pagina di errore. Se il CSS non viene applicato, verifica prima il collegamento e poi selettore e valore. I percorsi in `url()` dentro CSS sono normalmente relativi al file CSS, non alla pagina HTML.

Nel pannello Styles seleziona il titolo: devi vedere la regola `h1`. Il pannello Computed mostra il valore risultante. Cambiare una dichiarazione in DevTools è un esperimento temporaneo; riporta la modifica nel file per conservarla.

## Esercizio

Dai al paragrafo la classe `introduzione`, applica l'esempio e cambia il colore del titolo. Disattiva il foglio: il testo deve restare comprensibile.

::: details Soluzione
```html
<p class="introduzione">Sto imparando HTML e CSS costruendo una pagina.</p>
```
```css
h1 { color: #245b8a; }
```
Il font, il colore e la larghezza cambiano; il significato del paragrafo rimane nell'HTML. Controlla che la regola compaia in Styles.
:::

Fonti: [MDN · Basi di CSS](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics), [W3C · CSS Syntax](https://www.w3.org/TR/css-syntax-3/).
