# 11 · Responsive design e media query

**Obiettivo:** lasciare che contenuto e spazio decidano il layout, invece di assumere una sola dimensione.

## Prima una base fluida

Mantieni il viewport HTML, immagini ridimensionabili, testi senza altezze fisse e contenitori con limiti massimi. Una media query è utile quando il layout ha bisogno di cambiare; non corregge un minimo di contenuto sbagliato.

```css
.pagina { display: grid; gap: 1.5rem; }
@media (min-width: 48rem) {
  .pagina { grid-template-columns: minmax(0, 1fr) 16rem; }
}
img { max-inline-size: 100%; block-size: auto; }
```

La base è a una colonna. Il breakpoint indica il punto in cui due colonne hanno spazio, non il nome di un dispositivo. Prova anche larghezze intermedie, testo tradotto e zoom.

## Che cosa può interrogare una query

Le media query valutano tipo di media e caratteristiche. `width`/`height`, orientamento e rapporto d'aspetto non sono l'intero inventario. `hover`, `pointer`, preferenze di movimento e colori aiutano a adattare interazioni; le [preferenze](/css/preferenze-stampa) meritano prove specifiche.

```css
@media (hover: hover) and (pointer: fine) {
  a:hover { text-decoration-thickness: 0.15em; }
}
```

L'hover è un miglioramento, non l'unico modo per usare una funzione. Non dedurre identità del dispositivo da una query: un sistema può avere più metodi di input.

## Dimensioni del viewport mobile

Le barre del browser cambiano lo spazio visibile. `svh`, `lvh` e `dvh` offrono riferimenti differenti; scegli in base al comportamento desiderato. Per un contenuto che deve crescere preferisci `min-block-size` a una height fissa. `100vw` può produrre overflow in presenza di scrollbar dove `width: 100%` segue meglio il contenitore.

Le immagini responsive HTML selezionano anche i file; CSS determina lo spazio visualizzato. Per componenti riutilizzabili che dipendono dalla propria colonna, usa le [container query](/css/container-query).

## Esercizio

Adatta la struttura main/aside della lezione grid a una colonna sotto il punto in cui il testo diventa troppo stretto.

::: details Soluzione
```css
.pagina { display: grid; grid-template-areas: "contenuto" "laterale"; gap: 1.5rem; }
@media (min-width: 48rem) {
  .pagina { grid-template-columns: minmax(0, 1fr) 16rem; grid-template-areas: "contenuto laterale"; }
}
```
Il breakpoint è una prima scelta da provare, non un valore obbligatorio. Verifica 320px, finestre larghe e testo ingrandito; la pagina non deve tagliare il contenuto.
:::

Fonti: [Google/web.dev · Responsive design](https://web.dev/learn/design), [Google/web.dev · Media query](https://web.dev/learn/design/media-queries), [MDN · Media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_media_queries).
