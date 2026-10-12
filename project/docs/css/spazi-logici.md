# 12 · Spazi e proprietà logiche

**Obiettivo:** distribuire lo spazio seguendo il layout e la direzione di scrittura.

## Tre tipi di distanza

Il padding separa contenuto e bordo; il margine separa la scatola da ciò che la circonda; gap separa item di flex/grid o colonne nei contesti previsti. Non sono intercambiabili. Un gap non aggiunge spazio all'esterno del gruppo e i margini possono collassare nel flusso normale.

```css
.schede { display: grid; gap: 1rem; }
.scheda { padding: 1.5rem; }
.titolo { margin-block: 0 0.75rem; }
```

Una piccola scala di spazi evita valori scollegati. In seguito la esprimeremo con custom properties. Il numero più grande non deve nascondere un errore di annidamento o una box dimensionata male.

## Assi inline e block

In una normale scrittura orizzontale, inline segue le righe e block la progressione delle righe. In una scrittura verticale gli assi cambiano. Start ed end tengono conto anche della direzione: non sono sempre sinistra e destra.

```css
.nota {
  border-inline-start: 0.25rem solid #17634d;
  padding-inline-start: 1rem;
  margin-block: 1.5rem;
}
.contenitore { max-inline-size: 70rem; margin-inline: auto; }
```

Con `dir="rtl"` il bordo della nota si sposta sul lato iniziale appropriato. `inline-size` e `block-size` sono alternative logiche a width e height; `inset-inline-*` e `inset-block-*` riguardano elementi posizionati. Non mescolare proprietà fisiche e logiche che si sovrascrivono senza capire quale vince.

## Spazio disponibile e margini auto

Un contenitore a blocchi con una larghezza inferiore al containing block può essere centrato con margini inline auto. In flex un margine auto può assorbire spazio sul suo asse. In un normale elemento inline lo stesso codice non produce necessariamente il medesimo risultato.

La proprietà `writing-mode` cambia il modo di scrittura; `direction`/`dir` la direzione pertinente. Non usare rtl solo per ottenere un allineamento grafico.

## Esercizio

Scrivi una nota con bordo iniziale e spazio interno, poi cambia la pagina da ltr a rtl. Il bordo deve seguire la lingua, mentre la distanza fra schede rimane coerente.

::: details Soluzione
Usa il blocco `.nota` sopra e `gap` sul container. Cambia `dir` nell'HTML, non aggiungere una regola che inverta manualmente tutti i margini. Prova anche che testi, numeri e link mantengano l'ordine corretto.
:::

Fonti: [Google/web.dev · Proprietà logiche](https://web.dev/learn/css/logical-properties), [Google/web.dev · Spazi](https://web.dev/learn/css/spacing), [MDN · Logical properties](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_logical_properties_and_values).
