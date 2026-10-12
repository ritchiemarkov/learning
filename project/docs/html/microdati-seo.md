# 23 · Microdati e informazioni per i motori di ricerca

**Obiettivo:** distinguere semantica del documento, vocabolari strutturati e convenzioni esterne.

## Microdati HTML

```html
<article itemscope itemtype="https://schema.org/Course">
  <h2 itemprop="name">Laboratorio HTML</h2>
  <p itemprop="description">Struttura, form e accessibilità con esercizi pratici.</p>
  <a itemprop="url" href="https://example.org/corsi/html">Pagina del corso</a>
</article>
```

`itemscope` crea un item; `itemtype` ne indica il tipo secondo un vocabolario; `itemprop` assegna proprietà. Il valore di una proprietà dipende dall'elemento: testo, URL di un link, data di `time`, contenuto di `meta` e così via. Le regole HTML descrivono il contenitore dei dati, mentre Schema.org definisce tipi e proprietà del vocabolario.

`itemid` fornisce un identificatore globale quando il vocabolario lo ammette. `itemref` permette di considerare proprietà in elementi esterni all'item tramite una lista di ID. Puoi annidare item per oggetti composti; evita riferimenti incomprensibili e duplicazioni contraddittorie.

## JSON-LD e altre convenzioni

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Course",
  "name": "Laboratorio HTML",
  "description": "Struttura, form e accessibilità con esercizi pratici."
}
</script>
```

Google descrive JSON-LD, microdati e RDFa fra i formati per dati strutturati, con una preferenza per JSON-LD nelle sue indicazioni. Non sono tecniche per inventare contenuti assenti dalla pagina: i dati devono descrivere ciò che l'utente può trovare. Questo frammento è un esempio di sintassi, non una configurazione completa che garantisce risultati avanzati.

Open Graph usa metadati per anteprime social; i nomi `og:*` e l'attributo `property` appartengono a quella convenzione esterna. Il riferimento HTML non enumera tutti i vocabolari del Web. Allo stesso modo `rel="canonical"`, le versioni linguistiche e la descrizione della pagina comunicano informazioni, ma non decidono da soli come un motore indicizza e presenta il sito.

## La base resta un documento utile

Un `title` specifico, link navigabili con `href`, contenuti comprensibili e alternative delle immagini servono sia ai lettori sia agli strumenti. Un `meta robots` non protegge una pagina privata. Non nascondere testo ai visitatori per riempire metadati: organizza il contenuto visibile.

Puoi controllare sintassi e risultati con il Rich Results Test per i tipi supportati e con strumenti dedicati al vocabolario. Un risultato valido non promette che il motore mostri una particolare presentazione.

## Esercizio e verifica

Descrivi lo stesso corso in microdati e JSON-LD. Individua cosa appartiene a HTML e cosa a Schema.org.

::: details Soluzione
Gli attributi `itemscope`, `itemtype` e `itemprop`, e l'elemento `script` appartengono al markup HTML. `Course`, `name` e `description` dipendono dal vocabolario. I due esempi devono restituire le stesse informazioni del testo visibile. Non considerarli una certificazione SEO.
:::

Fonti: [WHATWG · Microdati](https://html.spec.whatwg.org/multipage/microdata.html), [Google Search Central · Dati strutturati](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data), [Open Graph](https://ogp.me/).
