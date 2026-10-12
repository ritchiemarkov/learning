# 15 · Iframe, oggetti, canvas, SVG e MathML

**Obiettivo:** riconoscere cosa viene incorporato e quali responsabilità rimangono alla pagina ospite.

## Un documento dentro un documento

```html
<iframe src="anteprima.html" title="Anteprima del programma del laboratorio"
        width="640" height="360" loading="lazy"
        sandbox referrerpolicy="no-referrer"></iframe>
<p><a href="anteprima.html">Apri il programma come pagina separata</a></p>
```

`iframe` crea un altro contesto di navigazione. `title` descrive il frame; non è il titolo del documento incorporato. `name` può renderlo una destinazione per link e form. `srcdoc` contiene markup inline e richiede escaping corretto; non usarlo per inserire testo utente non controllato.

`sandbox` senza token applica restrizioni. Aggiungi solo capacità motivate, come `allow-scripts` o `allow-forms`. Concedere insieme script e stessa origine a contenuti della stessa origine può compromettere il valore del sandbox. `allow` configura la Permissions Policy; `allowfullscreen` riguarda fullscreen. Il sito remoto può comunque rifiutare di essere incorporato. `loading` e `referrerpolicy` non aggirano questi vincoli.

## Object ed embed

```html
<object data="programma.pdf" type="application/pdf" width="640" height="480">
  <p><a href="programma.pdf">Scarica il programma PDF</a></p>
</object>
```

`object` può avere contenuto di fallback; `embed` è void e non ha lo stesso fallback interno. Il supporto dipende da formato e browser. Conserva un collegamento diretto accessibile. Le vecchie tecnologie a plugin non sono una scelta per un progetto nuovo e `param` è obsoleto. La presenza di un PDF non ne garantisce l'accessibilità.

## Tre tipi di grafica

`canvas` definisce una superficie bitmap, normalmente disegnata da JavaScript. Le dimensioni HTML della superficie e quelle CSS visualizzate sono distinte; solo ingrandire via CSS può deformare l'immagine. Il contenuto alternativo e controlli equivalenti sono responsabilità dell'autore: i pixel non diventano automaticamente testo accessibile.

```html
<canvas width="400" height="200">
  <p>Posti disponibili: HTML 12, CSS 8.</p>
</canvas>
```

`svg` e `math` sono radici di linguaggi esterni integrati in HTML, non altri due elementi definiti dal vocabolario HTML. SVG descrive grafica vettoriale; MathML formule. Per una grafica informativa puoi dare un nome accessibile, per una decorativa usare una presentazione appropriata al contesto.

```html
<svg viewBox="0 0 100 100" role="img" aria-labelledby="titolo-grafico">
  <title id="titolo-grafico">Cerchio verde</title>
  <circle cx="50" cy="50" r="40" fill="green" />
</svg>
<math><msup><mi>x</mi><mn>2</mn></msup></math>
```

Le proprietà e gli elementi interni di SVG/MathML hanno specifiche proprie. Qui studiamo l'integrazione; disegno, API canvas e interazioni proseguono con CSS e JavaScript.

## Esercizio e verifica

Incorpora un documento locale con sandbox e un titolo significativo. Aggiungi un link esterno al frame; prova a navigare quando l'incorporamento non funziona.

::: details Soluzione
Usa il primo esempio e crea `anteprima.html`. Non concedere permessi al frame se il documento è solo testo. Il collegamento esterno resta utilizzabile; verifica anche la raggiungibilità dalla tastiera.
:::

Fonti: [MDN · iframe](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe), [MDN · canvas](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas), [WHATWG · Contenuti incorporati](https://html.spec.whatwg.org/multipage/embedded-content.html).
