# 10 · Grid

**Obiettivo:** organizzare righe e colonne con dimensioni adattabili.

## Definire i track

```css
.schede {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 1rem;
}
```

I figli diretti diventano grid item. Le colonne e le righe sono *track*, delimitati da linee. `fr` divide spazio residuo; `minmax(0, 1fr)` evita il minimo automatico di un semplice `1fr` quando è appropriato al contenuto. Non impedisce da solo a un'immagine non ridimensionata o a una parola lunga di fuoriuscire.

```css
.schede { grid-template-columns: repeat(auto-fit, minmax(min(100%, 16rem), 1fr)); }
.schede img { max-inline-size: 100%; block-size: auto; }
```

Questo pattern crea colonne finché trovano spazio. `auto-fit` può far collassare track vuoti; `auto-fill` conserva track vuoti secondo le regole della ripetizione. Sono scelte differenti, non sinonimi.

## Posizionamento e aree

```css
.pagina {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 16rem;
  grid-template-areas: "contenuto laterale";
  gap: 2rem;
}
main { grid-area: contenuto; }
aside { grid-area: laterale; }
```

Un'area nominata deve formare un rettangolo nella sua definizione. In alternativa `grid-column: 1 / 3` estende dalle linee 1 a 3; `span 2` occupa due track. Gli item non assegnati vengono collocati con auto-placement. I track impliciti si controllano con `grid-auto-rows` e `grid-auto-columns`.

`justify-items` e `align-items` allineano dentro le aree; `justify-content` e `align-content` distribuiscono la griglia quando resta spazio nel container. L'ordine visivo non deve contraddire quello di lettura o focus. `dense` può riempire buchi alterando la disposizione visiva: valuta attentamente i contenuti interattivi.

## Grid insieme a flex

Una griglia di schede può usare grid fra le schede e flex dentro ciascuna scheda. Non è necessario scegliere un solo sistema per tutta la pagina. Nella [lezione 22](/css/layout-avanzato) aggiungeremo linee nominate, subgrid e controlli dei minimi.

## Esercizio

Crea una griglia che funzioni anche a 320px di larghezza, senza imporre tre colonne sul telefono.

::: details Soluzione
Usa il pattern `auto-fit` con `minmax(min(100%, 16rem), 1fr)`. Verifica contenuti molto lunghi e zoom. Per una struttura main/aside aggiungi una media query che passi a una colonna, senza cambiare l'ordine del DOM.
:::

Fonti: [Google/web.dev · Grid](https://web.dev/learn/css/grid), [MDN · Concetti di Grid](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout/Basic_concepts_of_grid_layout).
