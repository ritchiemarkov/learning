# 23 · Container query e componenti responsive

**Obiettivo:** adattare una scheda alla propria colonna, anche quando il viewport non cambia.

## Il contenitore interrogato

```html
<div class="slot-corso"><article class="scheda">Contenuto del corso</article></div>
```
```css
.slot-corso { container-type: inline-size; container-name: corso; }
.scheda { display: grid; gap: 1rem; }
@container corso (min-width: 30rem) {
  .scheda { grid-template-columns: 12rem minmax(0, 1fr); }
}
```

La query valuta un antenato container applicabile, non il viewport. La scheda può quindi cambiare in una colonna larga e restare compatta in una sidebar sulla stessa schermata. Container type applica forme di containment con effetti sul dimensionamento: non è soltanto un'etichetta.

L'elemento interrogato non si ridimensiona da solo in base alla propria query come un circuito ricorsivo arbitrario: le regole si applicano ai discendenti nel contesto previsto. Se la regola non funziona, controlla che esista un antenato idoneo e che il nome corrisponda.

## Unità e altre query

`cqi`, `cqb`, `cqw`, `cqh`, `cqmin` e `cqmax` esprimono misure relative ai container pertinenti, con regole di fallback quando mancano. Prova il riferimento effettivo prima di usarle per tutta la tipografia.

```css
@container corso (min-width: 30rem) {
  .scheda h2 { font-size: clamp(1.5rem, 5cqi, 2.5rem); }
}
```

Style query e scroll-state query interrogano aspetti differenti e hanno supporto specifico. Non assumere che supportare size query significhi supportarle tutte. Documenta la condizione esatta e una base funzionante senza la query.

## Pattern responsive

Un componente può combinare container query, griglia intrinseca e limiti min/max. Le media query restano appropriate per caratteristiche della pagina o preferenze dell'utente. Non duplicare tutte le regole in entrambi i sistemi.

Prova due copie della stessa scheda, una nella colonna principale e una laterale. Usa DevTools per vedere container e dimensioni; controlla testo lungo, immagini e focus dopo il cambio.

## Esercizio

Mostra titolo e immagine affiancati solo quando il contenitore supera 30rem. La versione stretta deve rimanere completa.

::: details Soluzione
Usa il wrapper e la query iniziale, mettendo immagine e contenuto come figli della scheda. La base resta una colonna; limita la larghezza dell'immagine. Ridimensiona il wrapper, non soltanto la finestra, per dimostrare che la condizione dipende dal componente.
:::

Fonti: [web.dev · Container query](https://web.dev/learn/css/container-queries), [MDN · Container queries](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_containment/Container_queries).
