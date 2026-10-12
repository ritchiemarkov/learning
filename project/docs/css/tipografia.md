# 07 · Testo e tipografia leggibile

**Obiettivo:** far crescere il testo senza romperne leggibilità e struttura.

## Una base semplice

```css
body {
  font-family: system-ui, sans-serif;
  font-size: 1rem;
  line-height: 1.6;
}
main { max-inline-size: 70ch; margin-inline: auto; }
h1, h2, h3 { line-height: 1.2; }
p { margin-block: 0 1rem; }
```

Una lista di font offre alternative se un carattere manca. Le famiglie generiche come sans-serif e serif dipendono dal dispositivo. I nomi composti possono richiedere virgolette. Non è necessario scaricare un font per iniziare.

`font-size` influenza dimensione del testo, `font-weight` il peso e `font-style` la variante. `line-height` senza unità segue bene i discendenti con font diversi. Un'altezza di contenitore fissa non deve sostituire una line-height coerente.

## Misura, allineamento e decorazione

La larghezza della colonna è parte della tipografia. Una riga troppo lunga rende difficile tornare all'inizio della successiva. `text-align: start` segue la direzione di scrittura; l'allineamento giustificato può generare spazi irregolari. Usa `letter-spacing` e `word-spacing` con criterio, senza impedire al lettore di aumentare la spaziatura.

`text-decoration` mantiene riconoscibili i link; `text-underline-offset` può distanziare la sottolineatura dal testo. `text-transform` cambia la presentazione, non la stringa originale. Non usare dimensioni visive per scegliere livelli h1–h6: quella scelta appartiene alla struttura HTML.

## Testo lungo e spazi

```css
.indirizzo { overflow-wrap: anywhere; }
pre { overflow: auto; }
```

`white-space` controlla spazi e ritorni; `overflow-wrap` permette interruzioni di emergenza. `word-break` ha effetti differenti e può compromettere la lettura se usato indiscriminatamente. `hyphens: auto` dipende da lingua e supporto: imposta `lang` correttamente. Codice e prosa possono richiedere trattamenti diversi.

Per un testo troncato `text-overflow: ellipsis` richiede altre condizioni di overflow e spazio. Non è un modo per eliminare informazioni che servono all'utente. Font web, numeri tabulari e proprietà avanzate proseguono nella [lezione 19](/css/tipografia-avanzata).

## Esercizio

Rendi leggibile una pagina di tre paragrafi e un URL molto lungo. Aumenta il testo e la spaziatura dal browser.

::: details Soluzione
Usa la base iniziale, evita height fisse e assegna `overflow-wrap: anywhere` al contenitore degli URL. Il testo deve andare a capo e i paragrafi crescere. I controlli con `font: inherit` devono restare leggibili come il resto della pagina.
:::

Fonti: [Google/web.dev · Tipografia](https://web.dev/learn/css/typography), [MDN · Fondamenti del testo](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Text_styling/Fundamentals).
