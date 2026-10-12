# 20 · Sfondi, gradienti, bordi e ombre

**Obiettivo:** comporre superfici senza perdere contrasto o introdurre significato soltanto decorativo.

## Gradienti e livelli

```css
.copertina {
  background-color: #17382d;
  background-image: linear-gradient(120deg, #17382d, #21715a);
  color: white;
}
.pannello {
  background-image: radial-gradient(circle at top right, #dcece2, transparent 65%),
                    linear-gradient(white, #f4f8f5);
}
```

Un gradiente è un'immagine CSS. Linear segue una direzione, radial si espande da un centro, conic varia intorno a un centro; esistono versioni repeating. Posizioni e stop controllano le transizioni fra colori, anche con bordi netti. Lo spazio di interpolazione del colore può modificare il risultato nelle forme moderne.

Negli sfondi multipli il primo livello viene dipinto davanti agli altri. Le liste di position, size, repeat e altre componenti devono essere interpretate secondo le regole di background. `background-origin` e `background-clip` distinguono l'area di posizionamento da quella di pittura. `background-attachment` cambia il riferimento allo scorrimento e richiede prove su dispositivi diversi.

## Ombre e bordi

```css
.scheda {
  border: 1px solid #b9ccc3;
  border-radius: 0.75rem;
  box-shadow: 0 0.5rem 1.5rem rgb(23 56 45 / 0.08);
}
```

`box-shadow` usa offset, blur, spread, colore e opzionalmente inset. Non occupa spazio nel layout; molte ombre grandi possono aumentare il costo di pittura. `text-shadow` riguarda il testo. `filter: drop-shadow()` segue la sagoma dell'immagine filtrata, con comportamento diverso dalla scatola.

Un border richiede stile e dimensione. `border-image` usa una sorgente e regole di slicing per comporre un bordo; non è un sostituto universale di border-radius. Mantieni un bordo o contrasto sufficiente anche quando un'ombra non viene mostrata, per esempio in alcuni contesti di stampa o contrasto forzato.

## Colori moderni

`oklab()`, `oklch()`, `color()` e `color-mix()` offrono spazi e trasformazioni aggiuntive. Un colore fuori gamut può essere adattato dal dispositivo. La componente lightness non dimostra da sola il contrasto accessibile: verifica il risultato con il testo e lo sfondo effettivi.

## Esercizio

Crea una scheda con sfondo a due livelli e un bordo visibile anche senza ombra. Cambia il titolo da breve a due righe.

::: details Soluzione
Combina `.pannello` e `.scheda` degli esempi, evitando dimensioni fisse. Il testo rimane sopra gli sfondi e deve avere contrasto sufficiente in ogni punto in cui può comparire. Rimuovi box-shadow in DevTools: il bordo deve continuare a distinguere la scheda.
:::

Fonti: [web.dev · Gradienti](https://web.dev/learn/css/gradients), [web.dev · Ombre](https://web.dev/learn/css/shadows), [MDN · Background clip](https://developer.mozilla.org/en-US/docs/Web/CSS/background-clip).
