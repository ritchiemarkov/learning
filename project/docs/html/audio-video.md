# 14 · Audio, video e sottotitoli

**Obiettivo:** pubblicare media con controlli e alternative utilizzabili.

## Video con più sorgenti

```html
<video controls preload="metadata" width="640" height="360"
       poster="anteprima.jpg" playsinline>
  <source src="laboratorio.webm" type="video/webm">
  <source src="laboratorio.mp4" type="video/mp4">
  <track kind="captions" src="laboratorio-it.vtt" srclang="it"
         label="Italiano" default>
  <p>Il browser non supporta video HTML.</p>
</video>
<p><a href="trascrizione.html">Leggi la trascrizione del laboratorio</a></p>
```

`video` e `audio` possono avere un `src` oppure una sequenza di `source`. Il browser cerca una sorgente supportata: il MIME e i codec contano. Il testo dentro il media è un fallback per browser che non supportano l'elemento; non sostituisce una trascrizione visibile né appare necessariamente quando un file è irraggiungibile.

`controls` richiede i controlli nativi. `poster` è l'anteprima del video; `width` e `height` ne descrivono le dimensioni. `playsinline` suggerisce riproduzione nel contesto della pagina su dispositivi mobili. Tutti i file citati nell'esempio devono essere disponibili.

## Tracce WebVTT

`track` è void e punta a un file di testo temporizzato. `kind="captions"` include dialoghi e suoni rilevanti; `subtitles` traduce o trascrive dialoghi per chi sente; `descriptions`, `chapters` e `metadata` hanno finalità differenti. `srclang` identifica la lingua e `label` il nome mostrato. `default` suggerisce la traccia iniziale, ma le preferenze dell'utente possono prevalere.

```text
WEBVTT

00:00:00.000 --> 00:00:03.000
Benvenuti al laboratorio HTML.

00:00:03.000 --> 00:00:05.000
[Suono di apertura della porta]
```

I sottotitoli devono essere sincronizzati e corretti. Una trascrizione aiuta anche chi non può riprodurre il video. Se informazioni essenziali sono soltanto visive, considera audiodescrizione o un'alternativa equivalente.

## Caricamento e riproduzione

`preload` ammette `none`, `metadata`, `auto`: è un suggerimento, non un limite di banda garantito. `autoplay`, `loop` e `muted` sono booleani. I browser possono bloccare l'autoplay; avviare audio senza richiesta è spesso una cattiva esperienza. Lascia all'utente il controllo della riproduzione.

`crossorigin` può essere necessario per tracce e usi del media da altri domini, insieme agli header CORS corretti sul server. La presenza dell'attributo non modifica da sola i permessi del server. Anche gli attributi di caricamento più recenti vanno confrontati con la compatibilità del browser.

## Esercizio e verifica

Prepara un breve audio locale con controlli e una trascrizione separata. Non usare autoplay. Controlla play, pausa e volume con tastiera, poi prova una sorgente inesistente.

::: details Soluzione
```html
<audio controls preload="none" src="introduzione.mp3"></audio>
<p><a href="introduzione-testo.html">Trascrizione dell'introduzione</a></p>
```
Il collegamento alla trascrizione rimane disponibile anche quando il file audio non si carica. Per il video aggiungi una traccia captions valida e controllane tempi e lingua.
:::

Fonti: [Google/web.dev · Audio e video](https://web.dev/learn/html/audio-video), [MDN · track](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/track), [WAI · Media](https://www.w3.org/WAI/media/av/).
