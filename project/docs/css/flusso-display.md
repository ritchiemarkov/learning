# 08 · Flusso, display e overflow

**Obiettivo:** capire il layout normale prima di sostituirlo con un altro sistema.

## Il comportamento di partenza

Nel normale flusso, scatole a blocchi si susseguono lungo l'asse block e contenuti inline formano righe lungo l'asse inline. Un elemento HTML non è immutabilmente «block» o «inline»: il browser applica stili predefiniti, che CSS può cambiare senza modificarne il significato.

```css
.etichetta { display: inline-block; padding: 0.25rem 0.5rem; }
.scheda { display: block; }
.azioni { display: flex; }
```

`display` riguarda sia la partecipazione della scatola al layout esterno sia il layout dei figli. `inline-block` resta nella riga ma consente una scatola dimensionabile. `flex` e `grid` cambiano il layout dei figli diretti, non di ogni discendente automaticamente.

## Nascondere ha conseguenze

`display: none` elimina normalmente la scatola e il contenuto dai percorsi di accessibilità. `visibility: hidden` conserva spazio ma nasconde il contenuto. `opacity: 0` rende invisibile e può lasciare elementi interattivi focalizzabili: non è una soluzione equivalente. `display: contents` rimuove la scatola dell'elemento e richiede attenzione a semantica e compatibilità.

## Contenuto che supera lo spazio

```css
.codice { max-block-size: 20rem; overflow: auto; }
.scheda { overflow-wrap: anywhere; }
```

`overflow: auto` crea scorrimento quando necessario; `scroll` richiede il meccanismo di scorrimento; `hidden` può nascondere contenuto e creare un contenitore di scorrimento con regole proprie; `clip` ha differenze importanti. Nascondere l'overflow di tutta la pagina può mascherare il problema e tagliare focus, contenuti o menu.

## Float e colonne

Un float può far scorrere testo intorno a un'immagine, ma non è il punto di partenza per un'intera applicazione. `display: flow-root` crea un nuovo contesto che può contenere i float.

```css
.articolo { display: flow-root; }
.articolo img { float: inline-start; max-inline-size: 12rem; margin-inline-end: 1rem; }
.glossario { columns: 16rem 2; column-gap: 2rem; }
```

Le colonne multicol dividono un flusso; grid organizza item in una griglia. L'ordine di lettura rimane quello del documento: prova come la colonna cambia con altezza e larghezza. La frammentazione e `break-inside` sono approfondite nella [lezione di stampa](/css/preferenze-stampa).

## Esercizio

Un paragrafo scompare quando ha un testo lungo dentro una scatola alta 4rem con `overflow: hidden`. Correggi il layout senza togliere il testo.

::: details Soluzione
Rimuovi l'altezza fissa quando il paragrafo può crescere. Se il requisito è un pannello scorrevole, usa un limite ragionato e `overflow: auto`, verificando accesso da tastiera e focus. `overflow-wrap: anywhere` risolve parole indivisibili, non un'altezza troppo piccola.
:::

Fonti: [web.dev · Layout](https://web.dev/learn/css/layout), [web.dev · Overflow](https://web.dev/learn/css/overflow), [MDN · Display](https://developer.mozilla.org/en-US/docs/Web/CSS/display).
