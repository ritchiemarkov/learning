# 03 · Cascata, specificità ed ereditarietà

**Obiettivo:** spiegare perché una dichiarazione prevale su un'altra.

## La cascata sceglie una dichiarazione

Più regole possono corrispondere allo stesso elemento. La cascata considera applicabilità, origine e importanza, livelli di cascata e poi criteri come specificità, prossimità dello scope e ordine. L'ordine nel file non risolve ogni conflitto. Gli stili del browser, dell'utente e dell'autore hanno origini differenti; animazioni e transizioni partecipano con regole proprie.

Per cominciare confrontiamo dichiarazioni normali dell'autore, senza layer o scope:

```html
<p class="nota">Il risultato dipende dalla cascata.</p>
```
```css
.nota { color: #17634d; }
p { color: #245b8a; }
```

Vince la classe, anche se `p` viene dopo. A parità degli altri criteri e della specificità, prevale la dichiarazione successiva.

## Specificità in tre colonne

Confronta ID; poi classi, attributi e pseudoclassi; poi tipi e pseudoelementi. Non è un numero decimale: molte classi non «riportano» a un ID. Combinatori e selettore universale non aggiungono peso.

| Selettore | Peso ID / classi / tipi |
| --- | --- |
| `p` | 0 / 0 / 1 |
| `.nota` | 0 / 1 / 0 |
| `article .nota` | 0 / 1 / 1 |
| `#contenuto .nota` | 1 / 1 / 0 |

Stili inline e `!important` hanno un trattamento nella cascata che non si riduce alla sola tabella. Non usare `!important` come soluzione universale: spesso il problema è un selettore o un layer. I dettagli sono nella [lezione 17](/css/layer-cascata).

## Ereditarietà

Proprietà come `color` e `font-family` normalmente vengono ereditate; `margin` e `border` normalmente no. Una dichiarazione diretta applicabile sul figlio prevale su un valore che arriverebbe dal genitore, anche se il selettore del genitore aveva molta specificità.

```css
body { font-family: system-ui, sans-serif; color: #17382d; }
button, input, select, textarea { font: inherit; }
```

`inherit` prende il valore dal genitore; `initial` il valore iniziale della proprietà; `unset` sceglie inherit o initial secondo la proprietà. `revert` e `revert-layer` hanno funzioni di ritorno fra origini o layer, approfondite più avanti. Il valore iniziale non coincide necessariamente con lo stile predefinito del browser.

## Esercizio

Due regole `.nota` impostano colori diversi. Quale vince? Poi assegna un colore soltanto a `body` e uno direttamente a `p`.

::: details Soluzione
Fra due regole `.nota` normali nello stesso contesto vince l'ultima. Il colore dichiarato direttamente su `p` prevale su quello ereditabile da `body`. In Styles le dichiarazioni superate sono normalmente barrate; Computed mostra il risultato.
:::

Fonti: [web.dev · Specificità](https://web.dev/learn/css/specificity), [web.dev · Ereditarietà](https://web.dev/learn/css/inheritance), [MDN · Cascata](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_cascade/Cascade).
