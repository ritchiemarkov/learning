# 13 · Stati, focus e puntatori

**Obiettivo:** rendere visibili le interazioni senza dipendere soltanto dal mouse.

## Selezionare uno stato

```css
a:hover { text-decoration-thickness: 0.15em; }
button:active { background-color: #174f3e; }
input:disabled { opacity: 0.65; }
input:checked { accent-color: #17634d; }
:focus-visible { outline: 3px solid #245b8a; outline-offset: 3px; }
```

`:hover` riguarda il puntamento, `:active` l'attivazione, `:focus` il focus corrente. `:focus-visible` usa il criterio del browser per quando mostrarne un indicatore; non significa semplicemente «tastiera» in ogni caso. `:focus-within` seleziona un contenitore quando lui o un discendente ha focus.

Un indicatore non deve essere tagliato dall'overflow o coperto da una barra fissa. Non togliere `outline` per motivi estetici senza sostituirlo. Il bordo del componente e il focus hanno finalità diverse.

## Validazione e selezione

Pseudoclassi come `:required`, `:optional`, `:valid`, `:invalid`, `:in-range` e `:out-of-range` riflettono stati dei controlli pertinenti. Un campo obbligatorio vuoto può essere invalid già all'apertura: mostrare errori troppo presto può confondere. `:user-invalid` dove supportato aiuta a distinguere l'interazione, ma un colore rosso non sostituisce un messaggio associato al campo.

## Cursore e pointer-events

`cursor` suggerisce quale interazione sia disponibile; non la implementa. `pointer-events: none` non equivale a `disabled`: può lasciare focus e attivazione da tastiera e cambia il bersaglio del puntatore. Usa il controllo nativo appropriato e il suo stato HTML.

Su dispositivi touch hover e precisione differiscono. Mantieni le azioni riconoscibili e raggiungibili, lasciando spazio fra i controlli. Non mostrare un comando importante solo durante hover.

## Esercizio

Crea due pulsanti e un input con label. Senza mouse, raggiungi ogni elemento e rendi evidente quale ha focus.

::: details Soluzione
Usa `:focus-visible` dell'esempio, conservando gli stili nativi per i casi in cui serve. Prova Tab e Shift+Tab, Invio/Spazio sui pulsanti. Se un pulsante è indisponibile, usa `disabled` nell'HTML e spiega il motivo quando necessario; non limitarti a cambiare cursore o opacità.
:::

Fonti: [Google/web.dev · Focus](https://web.dev/learn/css/focus), [Google/web.dev · Pseudoclassi](https://web.dev/learn/css/pseudo-classes), [Google/web.dev · Cursori e puntatori](https://web.dev/learn/css/cursors-and-pointers).
