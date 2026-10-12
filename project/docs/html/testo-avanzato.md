# 10 · Tutta la semantica del testo

**Obiettivo:** scegliere un elemento per ciò che significa, indipendentemente dalla sua forma visiva.

## Enfasi, precisione e annotazioni

| Elementi | Significato e scelta |
| --- | --- |
| `strong`, `em` | Importanza e accento della frase; non semplicemente grassetto e corsivo |
| `b`, `i`, `u` | Richiamo di attenzione, voce alternativa, annotazione non testuale; non sono tutti obsoleti |
| `mark` | Passaggio rilevante nel contesto, per esempio una corrispondenza di ricerca |
| `small` | Note laterali e clausole; non qualunque testo da rimpicciolire |
| `s` | Informazione non più corretta o rilevante |
| `del`, `ins` | Rimozioni e inserimenti editoriali; `cite` e `datetime` possono documentarli |
| `sub`, `sup` | Pedici e apici quando la notazione li richiede |
| `span` | Contenitore di frase quando non esiste un significato più specifico |

```html
<p><s>Quota: 30 €</s> <strong>Quota attuale: 20 €</strong></p>
<p>La formula dell'acqua è H<sub>2</sub>O.</p>
<p><small>Materiali didattici inclusi.</small></p>
```

## Citazioni, termini e codice

`blockquote` contiene una citazione estesa, `q` una breve. L'attributo `cite` collega la fonte ma non la mostra automaticamente. L'elemento `cite` marca il titolo di un'opera, non il nome di una persona. Mostra anche un link visibile alla fonte quando serve al lettore.

`abbr` identifica un'abbreviazione; espandila nel testo al primo uso. Il tooltip di `title` non è un'alternativa accessibile a una spiegazione visibile. `dfn` marca il termine nel punto in cui viene definito. `dl`, `dt`, `dd` organizzano associazioni termine–descrizione, anche con più termini per descrizione.

`code` significa codice; `pre` conserva la formattazione; `kbd` indica input, `samp` output di un programma, `var` una variabile. Escapa `<` e `&` negli esempi HTML.

```html
<dl>
  <dt><dfn>Elemento void</dfn></dt>
  <dd>Elemento che non può contenere figli, come <code>img</code>.</dd>
</dl>
<pre><code>&lt;p&gt;Ciao&lt;/p&gt;</code></pre>
<p>Premi <kbd>Invio</kbd>: compare <samp>Operazione completata</samp>.</p>
```

## Date e valori

`time` collega una data leggibile a una rappresentazione elaborabile. `data` associa altri contenuti a un valore macchina. Il valore non produce da solo calcoli o conversioni.

```html
<p>Prossimo incontro: <time datetime="2026-11-02T18:00+01:00">2 novembre alle 18</time>.</p>
<p>Corso: <data value="HTML-BASE-01">HTML per iniziare</data>.</p>
```

`br` interrompe una riga quando la divisione ha significato, come in una poesia. `wbr` indica un possibile punto di interruzione di una parola lunga. `hr` separa temi. La punteggiatura e lo spazio fra parole rimangono necessari: gli elementi non li aggiungono tutti automaticamente. Per `bdi`, `bdo`, `ruby`, `rt` e `rp` vedi [Lingue e direzione](/html/internazionalizzazione).

## Esercizio e verifica

Scrivi una scheda con un termine definito, una data macchina, un prezzo superato e un comando. Spiega la differenza fra `s` e `del`.

::: details Soluzione
Usa il glossario dell'esempio, `time datetime="2026-11-02"`, `s` per il prezzo vecchio e `code` per il comando. `del` sarebbe appropriato per una modifica editoriale del testo, non per la semplice scadenza di un'offerta.
:::

Fonti: [Google/web.dev · Altri elementi di testo](https://web.dev/learn/html/inline-text), [MDN · time](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/time), [WHATWG · Semantica del testo](https://html.spec.whatwg.org/multipage/text-level-semantics.html).
