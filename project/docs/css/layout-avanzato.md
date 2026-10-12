# 22 · Grid, subgrid e allineamento avanzato

**Obiettivo:** condividere allineamenti fra componenti e riconoscere dimensioni minime implicite.

## Linee e aree nominate

```css
.pagina {
  display: grid;
  grid-template-columns: [inizio] minmax(0, 1fr) [laterale] 18rem [fine];
  gap: 2rem;
}
.testata { grid-column: inizio / fine; }
```

I nomi rendono più chiaro il posizionamento. Track espliciti e impliciti possono avere dimensioni diverse; `grid-auto-flow` governa l'auto-placement, non la semantica del documento. Usa il pannello Grid di DevTools per osservare linee e aree, invece di indovinare coordinate.

## Subgrid

```css
.schede { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 1rem; }
.scheda {
  display: grid;
  grid-row: span 3;
  grid-template-rows: subgrid;
}
```

Un item può adottare i track del genitore nell'asse indicato, consentendo di allineare titolo, contenuto e azione di schede con testi diversi. Il markup deve corrispondere ai track e l'item deve occupare lo spazio previsto. Subgrid non trasforma automaticamente qualsiasi discendente in item della griglia del nonno.

## Minimi e distribuzione

Una colonna `1fr` può avere un minimo automatico che dipende dal contenuto; `minmax(0, 1fr)` e `min-inline-size: 0` hanno scopi correlati ma diversi. Una risorsa sostituita deve comunque adattarsi alla propria scatola. Le lunghe parole richiedono regole di wrapping.

In flex, grow distribuisce spazio positivo e shrink partecipa a quello negativo con pesi e basi. `justify-content` non crea spazio se gli item lo hanno già consumato con crescita o margini auto. In grid e flex, baseline, stretch e allineamento possono agire diversamente secondo asse e dimensioni definite.

`order`, dense e posizionamenti manuali non devono produrre una sequenza visiva incompatibile con focus e lettura. Il layout masonry e altre proposte in evoluzione richiedono verifica separata: non sono un prerequisito per una griglia di schede solida.

## Esercizio

Crea tre schede con titoli di una, due e tre righe. Allinea le azioni finali e verifica una variante con una sola colonna.

::: details Soluzione
Puoi usare un subgrid di tre righe con h2, descrizione e azione come figli diretti. Per la base compatibile usa una scheda flex column e `margin-block-start: auto` sull'azione. Quest'ultima allinea il fondo delle schede, ma non condivide tutti i track interni come subgrid: confronta il risultato.
:::

Fonti: [MDN · Subgrid](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout/Subgrid), [MDN · Box alignment](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_box_alignment), [web.dev · Grid](https://web.dev/learn/css/grid).
