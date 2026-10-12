# 33 · Funzioni, valori moderni e grammatica

**Obiettivo:** leggere una funzione CSS e verificare tipo e contesto del risultato.

## Famiglie differenti

| Famiglia | Esempi e scopo |
| --- | --- |
| Calcolo | calc, min, max, clamp, round, mod, rem |
| Geometria | sin, cos, tan, atan2, hypot e altre funzioni matematiche |
| Colori | rgb, hsl, oklch, color, color-mix e colori relativi |
| Immagini | url, gradienti, image-set |
| Forme e movimento | circle, polygon, path, shape, trasformazioni |
| Dati e valori riusabili | var e attr nei contesti supportati |

Una funzione non è utilizzabile con qualunque proprietà. Il risultato deve corrispondere alla grammatica e le unità devono essere compatibili. La funzione matematica `rem()` non è l'unità di lunghezza rem: condividono un nome ma hanno compiti diversi.

## Un valore leggibile

```css
.contenitore { inline-size: min(100% - 2rem, 70rem); }
.scheda { padding: clamp(1rem, 3cqi, 2rem); }
.tinta { background: color-mix(in srgb, #17634d 15%, white); }
```

Nell'esempio con cqi controlla il container di riferimento e il fallback. Color-mix descrive uno spazio di interpolazione e proporzioni; il risultato non garantisce contrasto. Una formula sofisticata deve ancora esprimere un requisito comprensibile.

## Attr e valori del contenuto

La forma classica di `attr()` è comune nel contenuto generato. Le forme tipizzate moderne possono usare attributi in altri contesti, ma hanno regole di tipo, fallback, sicurezza e supporto. Non assumere che un browser che supporta attr in content supporti tutta la grammatica moderna.

```css
.etichetta::after { content: " · " attr(data-versione); }
```

Il testo di data-versione deve essere un dettaglio aggiuntivo, non una label essenziale presente soltanto in CSS. Non usare attr come fonte arbitraria di URL se il modello non lo consente.

## Funzioni nuove non equivalgono a prerequisiti

Calc-size, interpolate-size e altri meccanismi di dimensionamento intrinseco hanno finalità specifiche e richiedono compatibilità dedicata. Proposte come funzioni CSS personalizzate possono evolvere: consultale nel riferimento, conservando una soluzione con CSS stabile. I valori globali inherit, initial, unset, revert e revert-layer restano parte della grammatica delle proprietà.

## Esercizio

Scrivi un padding con minimo e massimo, e spiega perché `color: calc(2rem + 1rem)` non è valido.

::: details Soluzione
`padding: clamp(1rem, 2vw, 2rem)` produce una lunghezza. La proprietà color richiede un colore, non una lunghezza: una formula aritmeticamente corretta non basta. In DevTools controlla l'invalidazione e conserva un fallback appropriato per funzioni nuove.
:::

Fonti: [web.dev · Funzioni](https://web.dev/learn/css/functions), [MDN · Math functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Using_math_functions), [MDN · Attr](https://developer.mozilla.org/en-US/docs/Web/CSS/attr).
