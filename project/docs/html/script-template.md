# 22 · Script, template e Web Components

**Obiettivo:** capire i punti di contatto fra markup e comportamento, senza saltare la tappa JavaScript.

## Caricare uno script

| Forma | Comportamento da distinguere |
| --- | --- |
| Script classico esterno senza async/defer | Può bloccare il parser durante caricamento ed esecuzione |
| Script classico con `defer` | Scarica in parallelo, esegue dopo il parsing e mantiene l'ordine dei deferred |
| Script classico con `async` | Esegue appena disponibile, senza un ordine di dipendenza garantito |
| `type="module"` | Modulo JavaScript, differito normalmente; importa altri moduli |
| Tipo dati, per esempio `application/ld+json` | Dati incorporati, non normale codice JS eseguito |

```html
<script src="/menu.js" defer></script>
<script type="module" src="/app.js"></script>
<noscript><p>Le informazioni del corso rimangono leggibili senza JavaScript.</p></noscript>
```

`defer` non modifica uno script classico inline come se fosse esterno. `nomodule` offre un percorso storico per browser senza moduli. `integrity`, `crossorigin`, `nonce`, `referrerpolicy` e `fetchpriority` hanno finalità di caricamento o sicurezza; le configurazioni devono essere coerenti con il server. `type="importmap"` descrive risoluzione dei nomi dei moduli e `speculationrules` regole di navigazione nei browser che le supportano: sono approfondimenti, non prerequisiti del primo script.

## Contenuto inerte riutilizzabile

```html
<template id="scheda">
  <article><h2>Nuovo corso</h2><p>Descrizione da aggiornare.</p></article>
</template>
```

Un template normale non mostra i figli come contenuto della pagina. JavaScript può clonare `template.content` e inserire il frammento nel DOM. Copiare un template contenente ID senza aggiornarli può produrre duplicati. Vedi la [lezione JS sul template](/javascript/tutorial/template-element).

## Slot e Shadow DOM

```html
<scheda-corso>
  <template shadowrootmode="open">
    <article><h2><slot name="titolo">Corso</slot></h2><slot></slot></article>
  </template>
  <span slot="titolo">HTML</span>
  <p>Un laboratorio pratico.</p>
</scheda-corso>
```

Il template con `shadowrootmode` può creare uno Shadow DOM dichiarativo dove supportato. `slot` definisce punti di inserimento e contenuto di fallback; l'attributo `slot` sui figli sceglie il punto nominato. I nodi assegnati rimangono nel light DOM e vengono presentati attraverso lo slot.

Un nome come `scheda-corso` può essere registrato come custom element autonomo tramite JavaScript. Il trattino fa parte delle regole del nome: il markup da solo non registra una classe. L'attributo `is` riguarda gli elementi built-in personalizzati, con supporto differente nei browser. Gli attributi `shadowrootclonable`, `shadowrootserializable`, `shadowrootdelegatesfocus`, `shadowrootcustomelementregistry` e `shadowrootslotassignment` hanno compiti avanzati e supporto da controllare.

`part` ed `exportparts` espongono agganci CSS di componenti. Shadow DOM non è un sistema di autorizzazioni o protezione di segreti. Focus, label e relazioni accessibili richiedono prove attraverso i confini del componente. [Custom elements](/javascript/tutorial/custom-elements), [Shadow DOM](/javascript/tutorial/shadow-dom) e [slot](/javascript/tutorial/slots-composition) hanno esercizi estesi nel corso JavaScript.

## Esercizio e verifica

Inserisci un template normale nella pagina e verifica che non appaia. Poi prova lo Shadow DOM dichiarativo con il contenuto di fallback e uno slot nominato.

::: details Soluzione e criteri
Nel primo caso controlla `template.content` in DevTools. Nel secondo il titolo è HTML e il paragrafo viene distribuito nello slot senza nome. Se il browser non supporta la funzione, il light DOM resta una base leggibile: verifica entrambe le condizioni prima di usarla in un progetto reale.
:::

Fonti: [MDN · script](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script), [MDN · template](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template), [Google/web.dev · Template e slot](https://web.dev/learn/html/template).
