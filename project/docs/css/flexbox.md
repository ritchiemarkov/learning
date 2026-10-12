# 09 · Flexbox

**Obiettivo:** disporre un gruppo lungo un asse e consentirgli di adattarsi allo spazio.

## Container e item

```html
<nav class="azioni" aria-label="Corsi">
  <a href="html.html">HTML</a><a href="css.html">CSS</a><a href="js.html">JavaScript</a>
</nav>
```
```css
.azioni { display: flex; flex-wrap: wrap; gap: 0.75rem; align-items: center; }
```

I figli diretti diventano flex item. L'asse principale dipende da `flex-direction`: row segue l'asse inline, column il block. Non dire «justify è orizzontale» come regola universale: la direzione cambia gli assi.

`justify-content` distribuisce lo spazio sull'asse principale; `align-items` allinea sull'asse trasversale. `align-content` riguarda la distribuzione di più righe quando esiste spazio e il contenitore permette wrap. `align-self` modifica un item.

## Crescita, restringimento e base

```css
.schede { display: flex; flex-wrap: wrap; gap: 1rem; }
.schede > article { flex: 1 1 16rem; min-inline-size: 0; }
```

`flex` combina grow, shrink e basis. Qui ogni scheda parte da una base di 16rem, può crescere e restringersi secondo le regole di flex. Le dimensioni minime del contenuto possono limitare il risultato: `min-inline-size: 0` permette un restringimento pertinente, poi il testo va reso spezzabile.

Un margine auto su un item assorbe spazio disponibile e può separare un gruppo di azioni. `gap` imposta una distanza fra gli item, senza aggiungere spazi ai bordi esterni. I margini del contenitore e il suo padding rimangono una decisione separata.

## Ordine visivo e ordine reale

`order` e direzioni reverse possono riordinare visivamente gli item, mentre lettura e tastiera mantengono riferimenti al DOM. Non usare questa differenza per correggere un documento con ordine sbagliato. Un layout responsive deve conservare un percorso comprensibile.

Flexbox lavora principalmente lungo un asse. Se più righe devono condividere colonne allineate, grid può descrivere meglio il requisito: ogni riga flex ha una propria distribuzione dello spazio.

## Esercizio

Disponi tre schede su una riga quando c'è spazio e su più righe quando non c'è. L'ultima scheda deve poter occupare spazio residuo senza una larghezza fissa.

::: details Soluzione
Usa `.schede` e la regola `flex: 1 1 16rem` dell'esempio. Aggiungi contenuti di lunghezze diverse e un URL lungo; verifica wrap, `gap`, minimo e assenza di tagli. Se vuoi colonne identiche fra righe, passa alla lezione grid.
:::

Fonti: [Google/web.dev · Flexbox](https://web.dev/learn/css/flexbox), [MDN · Concetti di Flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout/Basic_concepts_of_flexbox).
