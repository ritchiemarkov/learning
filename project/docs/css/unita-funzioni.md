# 05 · Unità, valori e funzioni di base

**Obiettivo:** scegliere dimensioni che seguano contenuto, preferenze e spazio disponibile.

## Le unità hanno riferimenti diversi

| Unità | Riferimento |
| --- | --- |
| `px` | Pixel CSS, non necessariamente un pixel fisico dello schermo |
| `rem` | Dimensione del font della radice |
| `em` | Font dell'elemento; su font-size dipende dal font del genitore |
| `ch` | Misura associata al glifo zero del font, non numero esatto di caratteri |
| `%` | Riferimento definito dalla singola proprietà |
| `vw`, `vh` | Dimensioni del viewport con le regole delle unità viewport |
| `svh`, `lvh`, `dvh` | Viewport piccolo, grande e dinamico, utili su mobile |
| `fr` | Quota dello spazio disponibile nei track di grid |

Usa `rem` per una scala leggibile e non impostare la radice a una dimensione che ignori le preferenze dell'utente. Le unità assolute come `cm`, `mm`, `in`, `pt` e `pc` hanno usi soprattutto di stampa, non promettono la stessa misura fisica su ogni schermo.

## Combinare limiti

```css
.contenitore { width: min(100% - 2rem, 70rem); margin-inline: auto; }
h1 { font-size: clamp(2rem, 1.4rem + 2vw, 3.5rem); }
.colonna { width: calc(100% - 3rem); }
```

`calc()` combina valori compatibili; gli spazi intorno a `+` e `-` sono importanti nella sintassi. `min()` sceglie il minore, `max()` il maggiore, `clamp()` applica minimo, valore preferito e massimo. Una dimensione fluida deve comunque restare leggibile con zoom e preferenze del font.

## Valori e shorthand

Uno zero di lunghezza può spesso essere scritto `0`; un numero non nullo richiede un'unità quando la grammatica vuole una lunghezza. `line-height: 1.6` è un numero intenzionalmente senza unità. `auto` non significa sempre zero: ogni proprietà lo interpreta secondo la propria definizione.

Le shorthand impostano più proprietà, spesso riportando a valori iniziali quelle omesse. `margin: 1rem 2rem` significa margine verticale di 1rem e orizzontale di 2rem. Con quattro valori l'ordine fisico è alto, destra, basso, sinistra. Le [proprietà logiche](/css/spazi-logici) offrono un modo legato alla scrittura.

## Esercizio

Crea una colonna larga al massimo 65ch con 1rem di spazio libero per lato e un titolo fluido limitato fra 2rem e 3rem.

::: details Soluzione
```css
main { width: min(100% - 2rem, 65ch); margin-inline: auto; }
h1 { font-size: clamp(2rem, 1.5rem + 2vw, 3rem); }
```
Riduci la finestra e aumenta il testo: la colonna deve restringersi senza tagliare contenuti. `65ch` è un obiettivo indicativo di misura, non 65 lettere esatte su ogni riga.
:::

Fonti: [Google/web.dev · Unità](https://web.dev/learn/css/sizing), [Google/web.dev · Funzioni](https://web.dev/learn/css/functions), [MDN · Valori e unità](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Values_and_Units).
