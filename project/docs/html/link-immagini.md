# 04 · Link e immagini

**Obiettivo:** collegare pagine e inserire immagini con un'alternativa testuale utile.

## Tre tipi di destinazione

```html
<!-- URL assoluto: un sito esterno -->
<a href="https://developer.mozilla.org/">Documentazione MDN</a>

<!-- Percorso relativo: un file nella stessa cartella -->
<a href="contatti.html">I miei contatti</a>

<!-- Ancora: un elemento nella stessa pagina -->
<a href="#interessi">Vai ai miei interessi</a>
<h2 id="interessi">I miei interessi</h2>
```

Scrivi testi che descrivano la destinazione. «Leggi la documentazione HTML» è più utile di «clicca qui».

Se decidi di aprire una nuova scheda, dichiaralo nel testo:

```html
<a href="https://developer.mozilla.org/" target="_blank" rel="noopener noreferrer">
  Documentazione MDN (nuova scheda)
</a>
```

`noopener` impedisce alla pagina aperta di accedere alla finestra di origine; `noreferrer` evita l'invio dell'intestazione di provenienza. Per i nostri esempi basta aprire il link nella scheda corrente.

## Percorsi di file

Con questa cartella:

```text
esercizi/
├── index.html
├── contatti.html
└── immagini/
    └── sentiero.jpg
```

da `index.html` puoi scrivere `src="immagini/sentiero.jpg"`. Il percorso è relativo alla posizione del documento. Anche maiuscole e minuscole contano su molti server.

## Immagini e testo alternativo

```html
<img
  src="immagini/sentiero.jpg"
  alt="Un sentiero sterrato attraversa un bosco di pini"
  width="800"
  height="600"
>
```

`src` indica il file e `alt` offre un'alternativa quando l'immagine non si vede o viene letta da una tecnologia assistiva. `width` e `height`, corrispondenti alle dimensioni reali, aiutano il browser a riservare lo spazio.

Un'immagine solo decorativa usa `alt=""`. Se è l'unico contenuto di un link, l'alternativa deve spiegare la destinazione o la funzione. Scegli il testo in base al ruolo, senza iniziare sempre con «immagine di».

## Didascalie

```html
<figure>
  <img src="immagini/sentiero.jpg" alt="Sentiero nel bosco di pini" width="800" height="600">
  <figcaption>Una passeggiata di ottobre.</figcaption>
</figure>
```

## Esercizio

1. Crea `contatti.html` con la struttura della prima lezione.
2. Collega le due pagine in entrambe le direzioni.
3. Aggiungi un link a una sezione della pagina principale.
4. Se hai una tua immagine, inseriscila con un `alt` coerente.

::: details Controllo e soluzione dei link
In `index.html`: `<a href="contatti.html">Contatti</a>`.
In `contatti.html`: `<a href="index.html">Torna alla pagina principale</a>`.
Per l'ancora: `<a href="#interessi">Interessi</a>` e `<h2 id="interessi">I miei interessi</h2>`.
Clicca ciascun collegamento: deve portare alla destinazione prevista.
:::

Riferimento: [WAI · Come scegliere il testo alternativo](https://www.w3.org/WAI/tutorials/images/decision-tree/).
