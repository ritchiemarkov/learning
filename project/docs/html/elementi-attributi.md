# 02 · Elementi e attributi

**Obiettivo:** leggere e scrivere la sintassi di base di HTML.

## Un elemento ha un significato

```html
<p>Questo è un paragrafo.</p>
```

`<p>` è il tag di apertura, `</p>` è il tag di chiusura. Insieme al contenuto formano un **elemento**. Il nome `p` dice al browser che il testo è un paragrafo.

## Gli attributi aggiungono informazioni

Gli attributi si scrivono nel tag di apertura:

```html
<a href="https://developer.mozilla.org/">Leggi MDN</a>
```

`href` è il nome dell'attributo; l'URL fra virgolette è il valore. In questo caso indica la destinazione del collegamento.

```html
<p id="presentazione" class="introduzione">Ciao!</p>
```

`id` identifica un elemento e deve essere unico nel documento. `class` raggruppa elementi: tornerà utile con CSS.

## Annidare correttamente

Puoi mettere un elemento dentro un altro, se il suo contenuto lo permette. Chiudi prima quello più interno:

```html
<p>Sto imparando <strong>HTML</strong>.</p>
```

Questo invece è un annidamento sbagliato:

```html
<p>Sto imparando <strong>HTML.</p></strong>
```

Il browser può tentare di correggere gli errori. Il fatto che qualcosa appaia sullo schermo non dimostra che il markup sia corretto.

## Elementi senza chiusura

Alcuni elementi, detti *void*, non possono contenere altri nodi e non hanno un tag di chiusura:

```html
<img src="foto.jpg" alt="Un sentiero tra gli alberi">
<input type="text" name="nome">
<br>
```

Usa `<br>` per un'interruzione significativa, come in un indirizzo o una poesia. La distanza fra paragrafi si gestisce con CSS.

## Caratteri speciali e commenti

```html
<p>Il tag &lt;p&gt; indica un paragrafo.</p>
<p>Pane &amp; marmellata</p>
<!-- Una nota per chi legge il sorgente -->
```

`&lt;` mostra `<`, `&gt;` mostra `>` e `&amp;` mostra `&`. I commenti non sono visibili nel contenuto, ma chiunque può leggerli dal sorgente della pagina: non inserirci informazioni riservate.

## Esercizio

Correggi questo frammento:

```html
<p>La mia <strong>prima pagina.</p></strong>
<img src="paesaggio.jpg"></img>
```

::: details Una possibile soluzione
```html
<p>La mia <strong>prima pagina.</strong></p>
<img src="paesaggio.jpg" alt="Colline verdi al tramonto">
```
Il testo alternativo deve descrivere la tua immagine reale. `<img>` non ha un tag di chiusura.
:::

Fonti: [WHATWG · Sintassi HTML](https://html.spec.whatwg.org/multipage/syntax.html).
