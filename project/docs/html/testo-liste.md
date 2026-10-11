# 03 · Testo e liste

**Obiettivo:** organizzare un testo usando titoli, paragrafi ed elenchi.

## Titoli con una gerarchia

Da `<h1>` a `<h6>`, i titoli descrivono livelli di contenuto. Per i nostri documenti useremo un `<h1>` per il tema principale, `<h2>` per le sezioni e `<h3>` per le sottosezioni.

```html
<h1>Il mio quaderno</h1>
<h2>Web</h2>
<h3>HTML</h3>
<p>Oggi ho creato la mia prima pagina.</p>
<h2>Idee per i prossimi progetti</h2>
```

Scegli il livello per la struttura, senza saltare livelli per ottenere un carattere più piccolo. Lo stile lo cambieremo con CSS.

## Importanza ed enfasi

```html
<p><strong>Salva il file</strong> prima di ricaricare.</p>
<p>Voglio capire <em>perché</em> funziona.</p>
```

`<strong>` indica importanza. `<em>` indica enfasi nel significato della frase. Di solito il browser li presenta in grassetto e corsivo, ma il motivo per usarli è il significato.

## Liste non ordinate e ordinate

Usa `<ul>` se l'ordine non conta:

```html
<ul>
  <li>Un editor</li>
  <li>Un browser</li>
  <li>Una cartella per gli esercizi</li>
</ul>
```

Usa `<ol>` quando la sequenza conta:

```html
<ol>
  <li>Scrivi il codice.</li>
  <li>Salva il file.</li>
  <li>Ricarica il browser.</li>
</ol>
```

Gli elementi della lista sono `<li>` e vanno dentro la lista. Una lista annidata si mette dentro un `<li>`.

## Esercizio

Nel tuo `index.html`, aggiungi la sezione «I miei interessi» con una lista di tre interessi e la sezione «Come studio» con una lista ordinata di tre passaggi.

::: details Una possibile soluzione
```html
<h2>I miei interessi</h2>
<ul>
  <li>Fotografia</li>
  <li>Musica</li>
  <li>Programmazione</li>
</ul>
<h2>Come studio</h2>
<ol>
  <li>Leggo una lezione.</li>
  <li>Provo un esempio.</li>
  <li>Scrivo un esercizio da solo.</li>
</ol>
```
:::

Controlla: se cambi l'ordine degli interessi, il significato rimane lo stesso? E se cambi l'ordine dei passaggi?
