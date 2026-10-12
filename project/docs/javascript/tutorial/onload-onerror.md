---
title: "Caricamento delle risorse: onload e onerror"
description: "JavaScript.info in italiano: Caricamento delle risorse: onload e onerror"
sourceTutorial: true
prev: {"text": "Scripts: async, defer", "link": "/javascript/tutorial/script-async-defer"}
next: {"text": "Mutation observer", "link": "/javascript/tutorial/mutation-observer"}
---

# Caricamento delle risorse: onload e onerror

> **JavaScript.info · Ilya Kantor e contributori.** [Originale inglese](https://javascript.info/onload-onerror) · [Edizione italiana](https://it.javascript.info/onload-onerror) · [Fonti e licenza](/javascript/fonti).

Il browser permette di tracciare il caricamento di risorse esterne: script, iframe, immagini e così via.

Esistono 2 eventi per tracciare il caricamento:

- `onload` -- caricato con successo,
- `onerror` -- si è verificato un errore.

## Caricamento di uno script

Diciamo che abbiamo necessità di caricare uno script di terze parti e chiamare una funzione che appartiene a questo script.

Possiamo caricarlo dinamicamente, in questo modo:

```js
let script = document.createElement('script');
script.src = "my.js";

document.head.append(script);
```

...Ma come possiamo eseguire la funzione dichiarata all'interno di quello script? Dobbiamo attendere la fine del caricamento dello script e successivamente chiamare la funzione. 


::: tip Da sapere
Per i nostri script dovremmo utilizzare i [moduli JavaScript](https://it.javascript.info/modules) in questo caso, ma non sono largamente adottati dalle librerie di terze parti.
:::

### script.onload

Il principale helper è l'evento `load`. Si innesca dopo che lo script è stato caricato ed eseguito. 

Per esempio:

```js
let script = document.createElement('script');

// si può caricare qualunque script, da qualunque dominio
script.src = "https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.3.0/lodash.js"
document.head.append(script);


script.onload = function() {
  // lo script crea una funzione helper "_"
  alert(_); // la funzione è disponibile
};

```

Quindi nell'evento `onload` possiamo utilizzare le variabili dello script, eseguire funzioni, ecc.


### script.onerror

Gli errori che si verificano durante il caricamento dello script possono essere tracciati tramite l'evento `error`.


script.onerror = function() {
  alert("Caricamento fallito " + this.src); // Error loading https://example.com/404.js
};

```

Notate bene che in questo punto non possiamo ottenere i dettagli dell'errore HTTP. Non sappiamo se è un errore 404 o 500 o qualcos'altro.


::: warning Attenzione
Gli eventi `onload`/`onerror` tracciano solo il caricamento stesso.

:::
Gli eventi `load` e `error` funzionano anche per le altre risorse, praticamente per qualunque risorsa che ha un `src` esterno.

Per esempio:

```js
let img = document.createElement('img');
img.src = "https://js.cx/clipart/train.gif"; // (*)

img.onload = function() {
  alert(`Immagine caricata, dimensione ${img.width}x${img.height}`);
};

img.onerror = function() {
  alert("Si è verificato un errore durante il caricamento dell'immagine");
};
```

Ci sono alcune note però:

- Per gli `<iframe>`, l'evento `iframe.onload` si aziona quando il caricamento dell' iframe è terminato, sia in caso di successo che in caso di errore. 

C'è una regola: gli script di un sito non possono accedere ai contenuti di un altro sito. Quindi, per esempio, uno script di  `https://facebook.com` non può leggere la casella di posta dell'utente di `https://gmail.com`.

Per essere più precisi, un'origine (tripletta dominio/porta/protocollo) non può accedere al contenuto di un'altra. Quindi se abbiamo un sottodominio, o anche solo un'altra porta, questo sarà un'origine differente e quindi non hanno accesso l'uno con l'altro.

Questa regola interessa anche le risorse di altri domini.

Se stiamo utilizzando uno script di un altro dominio e c'è un errore, non possiamo ottenere i dettagli di quell'errore.

Per esempio, prendiamo lo script `error.js`, che consiste in una singola chiamata ad una funzione (sbagliata):
```js
// 📁 error.js
noSuchFunction();
```

Ora caricatela dallo stesso sito su cui è situato lo script:

```html
<script>
window.onerror = function(message, url, line, col, errorObj) {
  alert(`${message}\n${url}, ${line}:${col}`);
};
</script>
<script src="/article/onload-onerror/crossorigin/error.js"></script>
```

Vedremo il report dell'errore, come questo:

```
Uncaught ReferenceError: noSuchFunction is not defined
https://javascript.info/article/onload-onerror/crossorigin/error.js, 1:1
```

Ora carichiamo lo stesso script da un altro dominio:

```html
<script>
window.onerror = function(message, url, line, col, errorObj) {
  alert(`${message}\n${url}, ${line}:${col}`);
};
</script>
<script src="https://cors.javascript.info/article/onload-onerror/crossorigin/error.js"></script>
```

Il report di errore è diverso rispetto a quello precedente, come questo:

```
Script error.
, 0:0
```

Ci sono molti servizi (e possiamo anche sviluppare il nostro) che stanno in ascolto sugli errori globali, utilizzando `window.onerror`, salvano gli errori e forniscono un interfaccia per accedere ed analizzarli. Fantastico, possiamo vedere i veri errori, scaturiti dai nostri utenti. Ma se uno script è caricato da un altro dominio non avremo nessuna informazioni sull'errore, come abbiamo appena visto.

Una policy cross-origin (CORS) simile viene applicata anche per altri tipi di risorse. 

**Per consentire l'accesso cross-origin il tag `<script>` deve avere l'attributo `crossorigin` e il server remoto deve fornire degli header speciali.**

Ci sono tre livelli di accesso cross-origin:

1. **Attributo `crossorigin` non presente** -- accesso vietato.
2. **`crossorigin="anonymous"`** -- accesso consentito se il server risponde con l'header `Access-Control-Allow-Origin` con il valore `*` o il nome della nostra origin (dominio). Il browser non manda dati e cookie sull'autenticazione al server remoto.
3. **`crossorigin="use-credentials"`** -- accesso consentito se il server manda indietro l'header `Access-Control-Allow-Origin` con la nostra origine (dominio) e `Access-Control-Allow-Credentials: true`. Il browser manda i dati e i cookie sull'autenticazione al server remoto.


::: tip Da sapere
Puoi approfondire l'accesso cross-origin nel capitolo [Fetch: Cross-Origin Requests](/javascript/tutorial/fetch-crossorigin). Descrive il metodo `fetch` per le richieste di rete, ma la policy è esattamente la stessa.

Ad esempio i "cookies" sono un argomento fuori dal nostro attuale ambito, ma puoi leggere informazioni a proposito nel capitolo [Cookies, document.cookie](/javascript/tutorial/cookie).
:::

Nel nostro caso non avevamo nessun attributo crossorigin, quindi l'accesso era vietato. Aggiungiamo l'attributo ora.

Possiamo scegliere tra `"anonymous"` (non vengono mandati cookie, è necessario un header lato server) e `"use-credentials"` (manda i cookie, sono necessari 2 header lato server).

Se non ci interessano i cookie allora `"anonymous"` è la scelta giusta:

```html
<script>
window.onerror = function(message, url, line, col, errorObj) {
  alert(`${message}\n${url}, ${line}:${col}`);
};
</script>
<script crossorigin="anonymous" src="https://cors.javascript.info/article/onload-onerror/crossorigin/error.js"></script>
```

Ora, supponendo che il server fornisca l'header `Access-Control-Allow-Origin`, riusciamo ad avere il report completo dell'errore.

## Riepilogo

Immagini `<img>`, fogli di stile esterni, script e altre risorse forniscono gli eventi `load` e `error` per tracciare i loro caricamento:

- `load` si aziona se il caricamento va a buon fine,
- `error` si azione se si verifica un errore durante il caricamento.

L'unica eccezione è `<iframe>`: per ragioni storiche scatta sempre l'evento `load`, per qualunque esito del caricamento, anche se la pagina non è stata trovata.

Possiamo monitorare il caricamento delle risorse anche tramite l'evento `readystatechange`, ma è poco utilizzato, perché gli eventi `load/error` sono più semplici.
```

## Esercizi

### 1 · Caricare immagini con una callback

Normalmente, le immagini vengono caricate quando sono create. Quindi quando aggiungiamo `<img>` alla pagina, l'utente non vede l'immagine immediatamente. Il Browser deve prima caricarla.

Per visualizzare un'immagine immediatamente dobbiamo crearla "in anticipo", come in questo caso:

```js
let img = document.createElement('img');
img.src = 'my.jpg';
```

Il browser inizia a caricare l'immagine e la salva nella cache. In seguito, quando la stessa immagine comparirà nel document, si visualizzerà immediatamente.

**Crea una funzione `preloadImages(sources, callback)` che carica tutte le immagini da un array `sources` e, quando pronte, esegue `callback`.**

Per esempio, questo pezzo di codice visualizzerà un `alert` dopo che le immagini sono caricate:

```js
function loaded() {
  alert("Images loaded")
}

preloadImages(["1.jpg", "2.jpg", "3.jpg"], loaded);
```

In caso di errore la funzione dovrebbe comunque considerare l'immagine "caricata"

In altre parole, la funzione di `callback` è eseguita quando tutte le immagini sono caricate o sono andate in errore.

La funzione, ad esempio, è utile quando dobbiamo mostrare una galleria scrollabile di immagini e vogliamo essere sicuri che tutte le immagini siano caricate.

Nel documento sorgente puoi trovare i link alle immagini di test ed anche il codice per verificare se le immagini sono state caricate o meno. L'output dovrebbe essere `300`.

::::: details Soluzione

L'algoritmo:
1. Fare un `img` per ogni sorgente.
2. Aggiungere `onload/onerror` ad ogni immagine.
3. Incrementa il contatore quando si aziona `onload` o `onerror`.
4. Quando il valore del contatore è uguale al numero delle sorgenti abbiamo finito: `callback()`.

:::::

