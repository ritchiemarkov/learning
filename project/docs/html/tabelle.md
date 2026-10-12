# 12 · Tabelle per dati

**Obiettivo:** rendere comprensibili le relazioni fra righe, colonne e intestazioni.

## Una tabella completa

```html
<table>
  <caption>Posti disponibili nei laboratori</caption>
  <colgroup><col><col><col></colgroup>
  <thead>
    <tr><th scope="col">Corso</th><th scope="col">Posti</th><th scope="col">Durata</th></tr>
  </thead>
  <tbody>
    <tr><th scope="row">HTML</th><td>12</td><td>2 ore</td></tr>
    <tr><th scope="row">CSS</th><td>8</td><td>3 ore</td></tr>
  </tbody>
  <tfoot>
    <tr><th scope="row">Totale posti</th><td>20</td><td>—</td></tr>
  </tfoot>
</table>
```

`table` descrive dati tabulari; non serve a disporre la pagina in colonne. `caption` è il titolo associato alla tabella. `tr` contiene celle: `th` è un'intestazione, `td` un dato. Il testo in grassetto non trasforma un `td` in un'intestazione.

`thead`, `tbody` e `tfoot` raggruppano righe. Scrivili esplicitamente per capire il DOM, anche se il parser può inserire un `tbody`. Mantieni l'ordine caption, gruppi di colonne, intestazione, corpo e piede. `colgroup` e `col` descrivono colonne e offrono agganci CSS; non sostituiscono le intestazioni delle celle.

## Associare intestazioni

`scope="col"` lega un'intestazione alla colonna; `scope="row"` alla riga. `colgroup` e `rowgroup` possono descrivere gruppi nei casi appropriati. Per associazioni complesse usa ID delle intestazioni e `headers` sulle celle interessate.

```html
<!-- Frammento di una tabella con associazioni esplicite -->
<tr><th id="corso" scope="col">Corso</th><th id="posti" scope="col">Posti</th></tr>
<tr><th id="html" scope="row">HTML</th><td headers="html posti">12</td></tr>
```

`abbr` su `th` offre un'etichetta alternativa breve. `colspan` estende una cella su più colonne; `rowspan` su più righe. Le celle non devono sovrapporsi e il numero logico delle colonne deve rimanere coerente. `rowspan="0"` ha un significato speciale: si estende fino alla fine del gruppo di righe. Una tabella più semplice spesso è più leggibile di una con molti incroci.

## Presentazione e accessibilità

Bordi, allineamento, spazi e larghezze appartengono a CSS. Gli attributi storici `cellpadding`, `cellspacing` e `align` non sono la soluzione moderna. Su uno schermo stretto puoi rendere scorrevole il contenitore, mantenendo i collegamenti fra intestazioni e dati. Se i numeri raccontano una conclusione, scrivila anche in un paragrafo visibile.

Una tabella HTML statica ha già una semantica propria. Aggiungere `role="grid"` implica un'interazione e una gestione della tastiera che il semplice markup non implementa.

## Esercizio e verifica

Aggiungi un terzo corso con 6 posti e aggiorna il totale. Ogni dato deve essere interpretabile indicando riga e colonna.

::: details Soluzione
```html
<tr><th scope="row">JavaScript</th><td>6</td><td>4 ore</td></tr>
```
Inserisci la riga nel `tbody`, cambia il totale in 26 e verifica con un lettore di schermo l'associazione delle intestazioni. Il solo controllo visivo non basta.
:::

Fonti: [Google/web.dev · Tabelle](https://web.dev/learn/html/tables), [WAI · Tabelle accessibili](https://www.w3.org/WAI/tutorials/tables/), [WHATWG · Tabelle](https://html.spec.whatwg.org/multipage/tables.html).
