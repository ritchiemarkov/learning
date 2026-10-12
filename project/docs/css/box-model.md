# 04 · Box model e dimensioni

**Obiettivo:** calcolare lo spazio occupato da contenuto, padding, bordo e margine.

## Quattro aree

Il contenuto è circondato dal padding, poi dal bordo, poi dal margine esterno. Lo sfondo si dipinge nelle aree previste da background, non nel margine. Outline e ombre non aumentano normalmente la dimensione di layout della scatola.

```css
.scheda {
  width: 240px;
  padding: 16px;
  border: 2px solid #b9ccc3;
  margin: 12px;
}
```

Con `box-sizing: content-box`, la larghezza del bordo esterno è 240 + 32 + 4 = **276px**, prima dei margini. Con `border-box` la width include contenuto, padding e bordo: diventa **240px**. Non include i margini.

```css
*, *::before, *::after { box-sizing: border-box; }
```

Questa base facilita molti layout. Non elimina i vincoli di contenuto minimo, gli effetti dei controlli nativi o i comportamenti di flex e grid.

## Dimensioni adattabili

```css
.contenitore {
  width: 100%;
  max-width: 70rem;
  margin-inline: auto;
  padding-inline: 1rem;
}
.scheda { min-height: 8rem; }
```

Un limite massimo evita righe eccessive su schermi ampi. Un'altezza minima permette al contenuto di crescere; un'altezza fissa può tagliare testi tradotti o ingranditi. I valori percentuali dipendono dalla proprietà e dal containing block: `height: 100%` non produce sempre l'altezza che immagini.

`min-content`, `max-content` e `fit-content` usano dimensioni intrinseche del contenuto. Un elemento flex/grid può avere un minimo automatico che impedisce il restringimento: in alcuni layout `min-width: 0` o `min-inline-size: 0` è la correzione pertinente, non nascondere ogni overflow.

## Collasso dei margini

Nel normale flusso a blocchi alcuni margini verticali si combinano invece di sommarsi. Non succede allo stesso modo fra item flex/grid. Usa gap per distanze fra item e padding per lo spazio interno. Un nuovo contesto come `display: flow-root` può essere utile per comprendere la separazione dei margini e contenere float; non applicarlo senza capire il layout.

## Esercizio

Una scatola ha width 300px, padding 20px e bordo 3px per lato. Calcola la larghezza con entrambi i box-sizing e prova un titolo molto lungo.

::: details Soluzione
Content-box: 300 + 40 + 6 = **346px**. Border-box: **300px**, salvo altri vincoli del layout. Per una scheda responsiva usa `max-width: 100%` e altezza libera. Guarda le misure nel box model di DevTools, non solo il risultato a occhio.
:::

Fonti: [Google/web.dev · Box model](https://web.dev/learn/css/box-model), [MDN · Box sizing](https://developer.mozilla.org/en-US/docs/Web/CSS/box-sizing).
