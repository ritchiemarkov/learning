# 28 · Forme, clipping, maschere e percorsi

**Obiettivo:** distinguere forma del flusso, ritaglio della pittura e trasparenza.

## Ritagliare non cambia il contenuto

```css
.ritratto { clip-path: circle(45% at 50% 50%); }
.decorazione { clip-path: polygon(0 0, 100% 0, 85% 100%, 0 100%); }
```

Clip-path definisce la regione visibile. La scatola di layout non diventa automaticamente circolare e il contenuto semantico non cambia. Prova focus e hit testing quando l'elemento è interattivo; non tagliare parti indispensabili di un controllo.

Funzioni di forma come circle, ellipse, inset e polygon descrivono geometrie; path e shape hanno grammatiche e supporto propri. Le coordinate percentuali dipendono dal riferimento previsto. Un ritaglio molto specifico può non funzionare con un'immagine diversa o un testo più lungo.

## Maschere

```css
.sfumatura {
  mask-image: linear-gradient(black 70%, transparent);
}
```

Mask può usare alpha o luminanza secondo sorgente e modalità. Consente bordi parzialmente trasparenti, diversamente da un ritaglio netto. Mask-size, position, repeat, mode e composite controllano parti differenti; sorgenti esterne possono essere soggette a condizioni di origine e caricamento. Non sfumare via il fondo di un paragrafo che l'utente deve leggere.

## Testo intorno a una forma

```css
.figura {
  float: inline-start;
  inline-size: 10rem;
  block-size: 10rem;
  shape-outside: circle(50%);
  shape-margin: 1rem;
}
```

Shape-outside modifica il modo in cui il flusso pertinente avvolge un float; non rende l'immagine circolare da sola. Se vuoi entrambe le cose, combina la forma del flusso con la pittura appropriata. Controlla che il contenitore gestisca il float.

Motion path usa proprietà come `offset-path`, `offset-distance` e `offset-rotate` per posizionare un elemento lungo un percorso. Il percorso e l'eventuale animazione sono due scelte separate; reduced motion e comprensibilità dell'interazione rimangono necessari.

## Esercizio

Ritaglia un'immagine decorativa in un cerchio e confronta il risultato con un testo che scorre attorno alla stessa forma.

::: details Soluzione
Clip-path cambia solo il ritaglio; per l'avvolgimento usa un float con shape-outside, dimensioni e shape-margin. Mantieni alt appropriato e verifica un fallback senza forme. Il contenuto della pagina deve restare disponibile senza questi effetti.
:::

Fonti: [web.dev · Percorsi e forme](https://web.dev/learn/css/paths-shapes-clipping-masking), [MDN · Masking](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_masking), [MDN · Shapes](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_shapes).
