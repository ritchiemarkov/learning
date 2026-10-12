# 09 · Head, metadati e risorse

**Obiettivo:** descrivere la pagina al browser e collegare le sue risorse.

## Un head ragionato

```html
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Calendario dei laboratori · Learning</title>
  <meta name="description" content="Date, programmi e iscrizione ai laboratori HTML.">
  <meta name="theme-color" content="#21715a">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="/stile.css">
  <script type="module" src="/app.js"></script>
</head>
```

`head` raccoglie metadati; `title` identifica il documento nella scheda, nella cronologia e nei risultati di ricerca. Un titolo specifico aiuta a distinguere pagine dello stesso sito. `meta` è void: il suo significato dipende dagli attributi. Salva il file in UTF-8 e colloca la dichiarazione della codifica all'inizio del documento.

Il viewport rende possibile un layout mobile coerente. Non disabilitare lo zoom. La descrizione riassume il contenuto, ma il motore di ricerca può scegliere un'altra descrizione. `theme-color` suggerisce un colore all'interfaccia del browser.

## Altre forme di metadati

`meta name="author"` indica l'autore. `name="robots"` con `content="noindex"` comunica una preferenza di indicizzazione: non protegge dati privati. `http-equiv` rappresenta solo le direttive previste, non qualunque header HTTP. I redirect e refresh automatici possono interrompere la lettura; per un redirect stabile configura il server.

`link` esprime relazioni con risorse e documenti. `rel="canonical"` segnala un URL preferito; `alternate` può descrivere versioni linguistiche con `hreflang`. Usa URL coerenti con il sito reale. I diversi valori di `rel`, `type`, `media`, `sizes` e `as` dipendono dal tipo di relazione: consulta la scheda ufficiale.

`style` contiene CSS, mentre un foglio esterno favorisce il riuso. `script` carica codice o contiene dati, secondo il suo `type`; l'ordine di esecuzione è trattato nella [lezione sui template](/html/script-template). `noscript` offre contenuto quando lo scripting è disabilitato, con regole diverse dentro `head` e `body`.

## Il caso di base

```html
<base href="https://example.org/corso/">
```

`base` modifica la risoluzione degli URL relativi, anche dei link con frammento. Può essere utile in documenti generati, ma rende meno evidente dove puntano link, immagini e form. Se lo usi, mettilo prima delle risorse con URL relativi e verifica l'effetto; normalmente puoi ometterlo. I primi valori `href` e `target` applicabili governano il comportamento previsto dalla specifica.

## Esercizio e verifica

Crea l'head di una pagina «Iscrizione al laboratorio». Aggiungi titolo, descrizione, codifica, viewport e CSS. La scheda deve avere un titolo distinguibile; la pagina deve restare ingrandibile su telefono.

::: details Soluzione
```html
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Iscrizione al laboratorio HTML · Learning</title>
  <meta name="description" content="Scegli una data e iscriviti al laboratorio HTML.">
  <link rel="stylesheet" href="stile.css">
</head>
```
Controlla in Network che `stile.css` sia raggiungibile. Il file CSS va creato separatamente.
:::

Fonti: [Google/web.dev · Metadati](https://web.dev/learn/html/metadata), [MDN · link](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link), [WHATWG · Metadati](https://html.spec.whatwg.org/multipage/semantics.html).
