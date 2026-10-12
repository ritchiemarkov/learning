# 13 · Immagini responsive e mappe

**Obiettivo:** offrire immagini appropriate allo schermo senza perdere il loro significato.

## Risoluzioni diverse, stesso contenuto

```html
<img src="aula-800.jpg"
     srcset="aula-400.jpg 400w, aula-800.jpg 800w, aula-1600.jpg 1600w"
     sizes="(max-width: 600px) 100vw, 800px"
     width="800" height="450"
     alt="Partecipanti al laboratorio intorno a un tavolo">
```

`srcset` elenca candidati. Il descrittore `w` è la larghezza reale del file, non quella desiderata sullo schermo. `sizes` descrive lo spazio previsto dal layout. Il browser sceglie usando queste informazioni, densità dello schermo e altre condizioni; non è garantito che scarichi sempre il candidato più piccolo. I file indicati vanno creati davvero.

Per uno spazio fisso puoi usare descrittori `1x`, `2x`. Non mescolare `w` e `x` nello stesso elenco. `width` e `height` permettono di conoscere il rapporto d'aspetto prima del download; CSS può poi adattare la dimensione visualizzata.

## Cambiare composizione o formato

```html
<picture>
  <source media="(max-width: 600px)" srcset="aula-ritaglio.jpg">
  <source type="image/avif" srcset="aula.avif">
  <img src="aula.jpg" width="800" height="450"
       alt="Il gruppo lavora a un progetto HTML">
</picture>
```

`picture` consente *art direction* e selezione del formato. I `source` precedono l'`img`; il primo candidato applicabile governa la scelta. L'`img` resta necessario e contiene il testo alternativo. Le varianti devono mantenere il senso della descrizione.

## Testo alternativo e caricamento

Un'immagine informativa richiede un'alternativa pertinente al contesto. Una puramente decorativa usa `alt=""`. Se è l'unico contenuto di un link, descrivi la destinazione o l'azione. Un grafico complesso richiede anche una spiegazione o una tabella dei dati: un lungo `alt` non risolve tutto. `figure` e `figcaption` associano una didascalia, senza sostituire automaticamente l'alternativa.

`loading="lazy"` è utile per immagini fuori dalla vista iniziale. Un'immagine principale visibile subito normalmente non va ritardata. `decoding` e `fetchpriority` sono suggerimenti; non aumentano la qualità del file. `crossorigin` e `referrerpolicy` regolano richieste e uso della risorsa, non il suo aspetto. Le funzioni recenti, come `controls` su immagini nello snapshot dello standard, richiedono una verifica dedicata prima dell'uso.

## Mappe cliccabili

```html
<img src="pianta.png" usemap="#aule" width="400" height="200" alt="Pianta delle aule">
<map name="aule">
  <area shape="rect" coords="0,0,200,200" href="aula-a.html" alt="Aula A">
  <area shape="rect" coords="200,0,400,200" href="aula-b.html" alt="Aula B">
</map>
```

`map` e `area` collegano regioni dell'immagine a destinazioni. `coords` dipende dalla geometria e dal sistema di coordinate: verifica ridimensionamento, tastiera e alternative testuali. `ismap` è una mappa gestita dal server con coordinate nella richiesta, distinta da `usemap`.

## Esercizio e verifica

Crea due versioni della stessa immagine e un `srcset` con descrittori reali. Poi trasforma un'immagine decorativa in contenuto informativo.

::: details Soluzione
Assegna a ciascun candidato il suo numero di pixel, descrivi in `sizes` la larghezza del layout e sostituisci `alt=""` con una descrizione del messaggio comunicato. In Network verifica la risorsa scelta, usando una nuova sessione o disabilitando la cache.
:::

Fonti: [Google/web.dev · Immagini](https://web.dev/learn/html/images), [MDN · Immagini responsive](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Responsive_images), [WAI · Scelta di alt](https://www.w3.org/WAI/tutorials/images/decision-tree/).
