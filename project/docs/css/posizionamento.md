# 21 · Posizionamento, stacking e top layer

**Obiettivo:** prevedere il riferimento delle coordinate e il livello di sovrapposizione.

## Position cambia il riferimento

`static` segue il flusso normale. `relative` conserva il proprio spazio e può spostare la pittura. `absolute` esce dal flusso e usa il containing block pertinente; un antenato posizionato spesso lo definisce, ma altre proprietà possono influenzarlo. `fixed` usa normalmente il viewport, con eccezioni legate ad alcuni antenati. `sticky` combina partecipazione al flusso e vincoli rispetto al contenitore di scorrimento.

```css
.scheda { position: relative; }
.etichetta { position: absolute; inset-block-start: 0.5rem; inset-inline-end: 0.5rem; }
.indice { position: sticky; inset-block-start: 1rem; align-self: start; }
```

Lo sticky richiede una soglia applicabile e spazio per muoversi. Un overflow su un antenato può cambiare il riferimento. Non usare absolute per costruire ogni riga di testo: il contenuto deve poter crescere.

## Z-index non è globale

Un **stacking context** raggruppa la sovrapposizione. Un figlio con z-index altissimo non supera liberamente uno stacking context fratello sopra il suo genitore. Position con z-index, trasformazioni, opacity e altre proprietà possono creare nuovi contesti con condizioni precise. Gli item flex/grid possono usare z-index anche senza essere posizionati.

`isolation: isolate` crea un confine utile; stacking context e layer compositato della GPU non sono la stessa misura. Aumentare i numeri all'infinito non corregge un confine di sovrapposizione sbagliato.

## Dialoghi, popover e ancore

Dialoghi modali e popover aperti possono vivere nel top layer, distinto dal normale stacking. `::backdrop` permette di presentare lo sfondo pertinente.

```css
dialog { max-inline-size: min(90vw, 35rem); border: 1px solid #b9ccc3; border-radius: 0.75rem; }
dialog::backdrop { background: rgb(0 0 0 / 0.45); }
```

L'apertura, la modalità e il focus dipendono anche da HTML e API: vedi [interazioni native HTML](/html/interazioni-native). CSS non rende modale un div.

L'anchor positioning può associare una posizione a un altro elemento tramite `anchor-name`, `position-anchor`, `anchor()` e `position-area`, con strategie di fallback come position-try. Verifica la singola funzione nei browser previsti: il top layer e l'ancoraggio risolvono problemi diversi.

```html
<button id="apri-aiuto" type="button" popovertarget="suggerimento">Aiuto</button>
<div id="suggerimento" popover>Leggi la prima lezione.</div>
```
```css
@supports (position-anchor: --aiuto) {
  #apri-aiuto { anchor-name: --aiuto; }
  #suggerimento {
    position: fixed;
    position-anchor: --aiuto;
    position-area: block-end;
    inset: auto;
    margin: 0;
  }
}
```

Senza il miglioramento, resta il popover nativo. Con il supporto pertinente si dispone rispetto al pulsante: prova anche il caso vicino al bordo del viewport e le strategie position-try prima di usarlo in una pagina reale.

## Esercizio

Un figlio con z-index 9999 resta sotto un pannello. Quale antenato controlli? Crea poi un badge nell'angolo di una scheda.

::: details Soluzione
Controlla gli stacking context di entrambi i rami, in particolare z-index, transform e opacity degli antenati. Per il badge usa la coppia relative/absolute dell'esempio, lasciando spazio al testo con padding se necessario. Non coprire il titolo o il focus di un controllo.
:::

Fonti: [web.dev · Z-index](https://web.dev/learn/css/z-index), [web.dev · Anchor positioning](https://web.dev/learn/css/anchor-positioning), [web.dev · Popover e dialog](https://web.dev/learn/css/popover-and-dialog), [MDN · Position](https://developer.mozilla.org/en-US/docs/Web/CSS/position).
