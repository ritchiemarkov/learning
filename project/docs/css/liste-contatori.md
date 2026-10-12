# 29 · Liste, marker e contatori

**Obiettivo:** personalizzare la presentazione di una sequenza senza spostarne il significato fuori da HTML.

## Marker nativi

```css
ol { list-style-type: decimal; padding-inline-start: 1.75rem; }
li::marker { color: #17634d; font-weight: 700; }
```

`list-style-type` sceglie il tipo di marker; `list-style-position` ne cambia la relazione con il contenuto; `list-style-image` può usare una risorsa con fallback. `::marker` ammette un insieme specifico di proprietà: non è una normale scatola con tutte le capacità di before.

Le liste HTML mantengono ordine e raggruppamento. Se una sequenza ha un numero iniziale o una voce con valore particolare, gli attributi HTML `start`, `reversed` e `value` possono comunicare quella struttura, indipendentemente dall'effetto CSS.

## Contatori personalizzati

```css
.capitoli { counter-reset: capitolo; }
.capitoli h2 { counter-increment: capitolo; }
.capitoli h2::before { content: counter(capitolo) ". "; }
```

Counter-reset crea o reimposta il contatore nel contesto previsto; counter-increment lo modifica; counter-set assegna un valore. `counter()` legge un livello, `counters()` può rappresentare livelli annidati. Gli scope dei contatori dipendono dall'albero e dalle regole della specifica, non da variabili JavaScript globali.

`@counter-style` permette sistemi, simboli, suffissi e fallback personalizzati. È utile per convenzioni di numerazione, ma non richiede di ridefinire una lista decimale semplice.

## Contenuto generato e accessibilità

Non affidare una procedura essenziale solo a numeri inseriti con `content`: presentazione e annunci possono variare. Se il numero è parte del significato, usa una lista ordinata o testo nel documento. Anche rimuovere tutti i marker da liste deve essere verificato nel contesto delle tecnologie assistive.

Una lista di navigazione può avere disposizione flex senza perdere il proprio raggruppamento HTML. Non assegnare ruoli di menu interattivo soltanto perché visivamente appare un menu: quello comporta regole di tastiera e comportamento aggiuntive.

## Esercizio

Personalizza una lista di tre passi con marker verdi e una lista annidata. Poi disattiva CSS.

::: details Soluzione
Usa ol e li nell'HTML e `li::marker` per il colore. La sequenza rimane numerata e leggibile anche senza CSS. Se usi counters per titoli, considera quei numeri un ausilio visivo e conserva nel documento una struttura di heading comprensibile.
:::

Fonti: [web.dev · Liste](https://web.dev/learn/css/lists), [web.dev · Contatori](https://web.dev/learn/css/counters), [MDN · Counter style](https://developer.mozilla.org/en-US/docs/Web/CSS/@counter-style).
