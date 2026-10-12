# 31 · Preferenze, accessibilità e stampa

**Obiettivo:** adattare la presentazione senza annullare le scelte dell'utente.

## Colore e contrasto

```css
:root { color-scheme: light; }
@media (prefers-color-scheme: dark) {
  :root { color-scheme: dark; }
  body { color: #edf5ef; background: #17241e; }
}
@media (forced-colors: active) {
  .scheda { border: 1px solid CanvasText; }
  :focus-visible { outline-color: Highlight; }
}
```

Color-scheme informa il browser sugli schemi supportati, influenzando anche controlli e superfici native. Non crea automaticamente tutti gli stili di un tema. In forced colors il sistema può sostituire colori: conserva bordi, nomi e stati senza affidarti alle ombre. Evita `forced-color-adjust: none` su tutto il sito.

Prefers-contrast, reduced-motion e altre caratteristiche hanno scopi distinti. Mantieni una base solida e verifica ogni query nei browser previsti. Una preferenza non è una classificazione dell'utente.

## Reflow e spaziatura

Una pagina deve permettere zoom, testo più grande e variazioni di spaziatura senza perdere contenuti o funzioni. Evita altezze fisse per prosa e label. Reflow riguarda anche finestre strette: parti come tabelle di dati possono richiedere un trattamento specifico, non giustificare overflow di tutta la pagina.

Per testo normale il criterio WCAG sul contrasto minimo usa normalmente 4,5:1, con eccezioni e una soglia diversa per testo grande. Anche focus e componenti richiedono criteri pertinenti: non trasformare un unico numero in una certificazione dell'interfaccia.

## Stampa e frammentazione

```css
@media print {
  nav, .azioni { display: none; }
  body { color: black; background: white; }
  .scheda { box-shadow: none; break-inside: avoid; }
  a { color: black; text-decoration: underline; }
}
@page { margin: 18mm; }
```

Media print modifica il foglio per la stampa; `@page` descrive aspetti delle pagine. Break-before/after/inside, orphans e widows riguardano frammentazione secondo supporto e contesto. Evitare una divisione non è sempre possibile se il contenuto è più grande della pagina. Non nascondere istruzioni indispensabili solo perché si trovano vicino a un'azione.

## Esercizio

Prova il progetto in dark mode, contrasto forzato, testo ingrandito e anteprima di stampa. Annota una correzione per ciascun problema trovato.

::: details Soluzione e criteri
Mantieni coppie testo/superficie coerenti, bordi in forced colors, altezza libera per i testi e un foglio print che conserva programma e contatti. La stampa non deve essere una schermata piena di pulsanti inutili; la navigazione a schermo deve restare completa. Riduci il movimento con la query delle lezioni 24–26.
:::

Fonti: [MDN · Forced colors](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/forced-colors), [MDN · Paged media](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_paged_media), [WAI · Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html), [WAI · Contrasto](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html).
