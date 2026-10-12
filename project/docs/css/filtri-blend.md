# 27 · Filtri, blend e isolamento

**Obiettivo:** capire quali pixel vengono modificati e preservare una base leggibile.

## Filtrare il contenuto

```css
.immagine { filter: saturate(0.8) contrast(1.05); }
.icona { filter: drop-shadow(0 0.2rem 0.3rem rgb(0 0 0 / 0.2)); }
```

Filter può applicare blur, brightness, contrast, grayscale, hue-rotate, invert, opacity, saturate, sepia, drop-shadow e riferimenti a filtri nei contesti previsti. Le funzioni si compongono in ordine: invertire la sequenza può cambiare il risultato. Il filtro non modifica il file originale.

`drop-shadow()` segue la sagoma del contenuto trasparente, mentre box-shadow riguarda la scatola. Un blur ampio può aumentare la pittura necessaria. Non filtrare testo essenziale rendendolo difficile da leggere.

## Lo sfondo dietro un elemento

```css
.pannello { background: rgb(255 255 255 / 0.92); }
@supports (backdrop-filter: blur(8px)) {
  .pannello { background: rgb(255 255 255 / 0.8); backdrop-filter: blur(8px); }
}
```

Backdrop-filter agisce sulla regione dietro il pannello secondo i confini previsti; normalmente serve una superficie almeno parzialmente trasparente per vederne l'effetto. Mantieni uno sfondo abbastanza solido come fallback. Il contrasto deve essere verificato con lo sfondo reale, non con una sola immagine favorevole.

## Mescolare colori

`background-blend-mode` mescola i livelli dello sfondo. `mix-blend-mode` mescola la rappresentazione dell'elemento con il contesto. Valori come multiply, screen, overlay, difference e altri seguono formule differenti e possono produrre risultati inattesi su nuovi sfondi.

```css
.composizione { isolation: isolate; background: #dcece2; }
.composizione .decorazione { mix-blend-mode: multiply; }
```

Isolation aiuta a controllare il confine di composizione e crea uno stacking context. Non rende il colore di un testo universalmente contrastato. Evita di affidare uno stato esclusivamente a un effetto che dipende dai pixel sottostanti.

## Esercizio

Crea un pannello con backdrop-filter ma leggibile anche quando il filtro viene disabilitato. Poi cambia lo sfondo da chiaro a scuro.

::: details Soluzione
Usa la base opaca e la query sopra. Verifica il colore del testo e aumenta l'opacità della superficie se necessario. Misura l'effetto con DevTools e rimuovilo se introduce costi o peggiora la lettura senza un beneficio concreto.
:::

Fonti: [web.dev · Filtri](https://web.dev/learn/css/filters), [web.dev · Blend](https://web.dev/learn/css/blend-modes), [MDN · Backdrop filter](https://developer.mozilla.org/en-US/docs/Web/CSS/backdrop-filter).
