# 19 · Font web e tipografia avanzata

**Obiettivo:** caricare caratteri senza rendere il contenuto dipendente da un download perfetto.

## Dichiarare un font

```css
@font-face {
  font-family: "Learning Sans";
  src: url("learning-sans.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
body { font-family: "Learning Sans", system-ui, sans-serif; }
```

Il file è un segnaposto da sostituire con un font disponibile e con licenza adatta. `@font-face` descrive una risorsa; non applica il font da sola. Pesi e stili vanno dichiarati coerentemente: una risorsa regular non contiene automaticamente tutte le varianti.

`font-display` governa periodi di attesa e sostituzione secondo il valore scelto; swap mantiene testo leggibile ma può cambiare le misure quando il font arriva. Valuta fallback con metriche compatibili e le opzioni di regolazione come size-adjust quando pertinenti. Precaricare ogni peso può sprecare banda.

## Font variabili e funzioni tipografiche

Un font variabile può esporre assi di peso, larghezza, dimensione ottica e altri parametri. Preferisci le proprietà standard come font-weight quando rappresentano il bisogno; `font-variation-settings` permette controlli più specifici e dipende dagli assi reali del font.

```css
.prezzo { font-variant-numeric: tabular-nums; }
.titolo { text-wrap: balance; }
.prosa { hyphens: auto; }
```

Numeri tabulari allineano cifre quando il font supporta la funzione. `text-wrap` può migliorare titoli o paragrafi con valori e compatibilità differenti; non è necessario per rendere leggibile un documento. La sillabazione dipende da lingua, dizionari e browser.

## Scritture e densità

`writing-mode`, orientamento e proprietà logiche aiutano documenti con scritture diverse. Non applicare letter-spacing aggressivo indiscriminatamente: alcuni sistemi di scrittura hanno legature e regole proprie. Font fallback diversi possono avere altezze e copertura Unicode differenti.

Prova zoom, spaziatura personalizzata, font assente e connessione lenta. `line-clamp` e ellissi possono essere utili per estratti, ma devono lasciare accessibile il contenuto necessario. La leggibilità non si verifica con un solo titolo corto.

## Esercizio

Simula il fallimento del font web e verifica che pagina e form rimangano utilizzabili. Allinea i prezzi di una tabella.

::: details Soluzione
Mantieni una famiglia generica nella font stack e non dimensionare i contenitori sulla misura di una sola risorsa. Usa `font-variant-numeric: tabular-nums` sui prezzi e verifica che il font supporti la funzione. Con Network disabilita il download del font e osserva eventuali salti di layout.
:::

Fonti: [MDN · font-face](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face), [web.dev · Tipografia](https://web.dev/learn/css/typography), [MDN · Font variabili](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_fonts/Variable_fonts_guide).
