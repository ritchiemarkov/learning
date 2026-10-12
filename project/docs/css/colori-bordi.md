# 06 · Colori, sfondi e bordi

**Obiettivo:** dare gerarchia alla pagina mantenendo testo e controlli riconoscibili.

## Testo e superficie

```css
body { color: #17382d; background-color: #f4f8f5; }
.scheda {
  background-color: white;
  border: 1px solid #b9ccc3;
  border-radius: 0.75rem;
  padding: 1.5rem;
}
a { color: #155b8a; text-decoration: underline; }
```

`color` normalmente si eredita e influenza anche `currentColor`. Il background iniziale trasparente lascia vedere ciò che si trova dietro: non è lo stesso che ereditare il colore dello sfondo. `opacity` agisce sull'elemento come insieme, figli compresi; un colore con alpha modifica solo quel colore.

## Formati di colore

Puoi usare nomi, esadecimale, `rgb()` e `hsl()`. Le forme moderne separano le componenti con spazi e l'alpha con `/`, per esempio `rgb(23 99 77 / 0.15)`. Spazi come `oklch()` e `color(display-p3 ...)` sono approfonditi più avanti; conserva un fallback coerente se i browser del progetto lo richiedono.

Un colore non deve essere l'unica informazione: un errore richiede testo, uno stato selezionato un segnale riconoscibile e un link un aspetto comprensibile. Verifica contrasto con lo sfondo effettivo, inclusi immagini e trasparenze.

## Bordo, outline e immagine di sfondo

`border` combina larghezza, stile e colore. Senza stile applicabile il bordo non compare come previsto. `border-radius` arrotonda la scatola ma non è una strategia di layout. `outline` non prende normalmente spazio nel box model ed è utile per il focus: non rimuoverlo senza una sostituzione visibile.

```css
.copertina {
  background-color: #17382d;
  background-image: url("decorazione.svg");
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
}
```

Un'immagine di sfondo non ha `alt`: usala per decorazione, non per contenuti indispensabili. `cover` può ritagliare, `contain` mantiene l'intera immagine con eventuale spazio residuo. Le shorthand come `background` possono azzerare componenti già impostate. Gradienti, ombre e sfondi multipli sono nella [lezione 20](/css/sfondi-effetti).

## Esercizio

Crea una scheda chiara con bordo verde, titolo scuro e link sottolineato. Aggiungi un errore di form che si capisca anche senza colore.

::: details Soluzione
```html
<p class="errore">Email non valida: inserisci un indirizzo con il formato nome@example.org.</p>
```
```css
.errore { color: #9b2727; border-inline-start: 0.25rem solid; padding-inline-start: 0.75rem; }
```
Il testo spiega cosa correggere. Misura il contrasto della combinazione reale e controlla che non scompaia in modalità di contrasto forzato.
:::

Fonti: [web.dev · Colore](https://web.dev/learn/css/color), [web.dev · Bordi](https://web.dev/learn/css/borders), [web.dev · Sfondi](https://web.dev/learn/css/backgrounds).
