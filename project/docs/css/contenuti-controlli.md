# 14 · Immagini, form, tabelle e liste

**Obiettivo:** applicare CSS alle strutture HTML conservando la loro funzione.

## Immagini e contenuti sostituiti

```css
img, video { max-inline-size: 100%; block-size: auto; }
.copertina { inline-size: 100%; aspect-ratio: 16 / 9; object-fit: cover; }
```

`object-fit` governa come il contenuto sostituito entra nella propria scatola; `cover` può ritagliare, `contain` conservare tutta l'immagine. `object-position` sceglie il punto del ritaglio. Il rapporto d'aspetto mantiene una forma ma non sostituisce dimensioni HTML, alternative testuali o scelta dei file responsive.

## Form leggibili

```css
button, input, select, textarea { font: inherit; }
label { display: block; margin-block-end: 0.25rem; }
input:not([type="radio"]):not([type="checkbox"]), select, textarea {
  max-inline-size: 100%;
  padding: 0.6rem;
}
fieldset { border: 1px solid #b9ccc3; }
```

Non rimuovere tutte le apparenze native per uniformare i controlli senza implementare e verificare stati equivalenti. `accent-color` può personalizzare alcuni controlli mantenendone il funzionamento. Label, istruzioni ed errori appartengono all'HTML; il CSS ne cura la presentazione.

## Tabelle e liste

```css
table { border-collapse: collapse; inline-size: 100%; }
th, td { padding: 0.75rem; border-block-end: 1px solid #b9ccc3; text-align: start; }
.tabella-scroll { overflow: auto; }
ul, ol { padding-inline-start: 1.5rem; }
li + li { margin-block-start: 0.5rem; }
```

Le tabelle restano tabelle di dati, con caption e intestazioni associate. `table-layout` e larghezze influenzano la distribuzione; prova testi lunghi. Un contenitore scorrevole può essere preferibile a comprimere i numeri fino a renderli illeggibili.

Le liste hanno marker personalizzabili con `list-style` e `::marker`. Quando rimuovi marker da una navigazione, conserva una semantica e una presentazione comprensibili, verificando anche le tecnologie assistive. Contatori e marker avanzati sono nella [lezione 29](/css/liste-contatori).

## Esercizio

Applica queste regole al [laboratorio HTML](/esempi/laboratorio-html.html). Aggiungi un'immagine reale e prova un nome di corso molto lungo nella tabella.

::: details Soluzione
Collega un CSS esterno al documento, conserva caption e label e avvolgi solo la tabella in `.tabella-scroll` se serve. Per l'immagine usa max-inline-size e height automatica; usa object-fit soltanto quando il ritaglio è intenzionale. Tutti i controlli devono continuare a funzionare senza mouse.
:::

Fonti: [MDN · Object fit](https://developer.mozilla.org/en-US/docs/Web/CSS/object-fit), [MDN · Styling forms](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Styling_web_forms), [web.dev · Liste](https://web.dev/learn/css/lists).
