---
title: "WeakRef e FinalizationRegistry"
description: "JavaScript.info in italiano: WeakRef e FinalizationRegistry"
sourceTutorial: true
prev: {"text": "Unicode e rappresentazione delle stringhe", "link": "/javascript/tutorial/unicode"}
next: {"text": "Il Browser come ambiente, specifiche", "link": "/javascript/tutorial/browser-environment"}
---

# WeakRef e FinalizationRegistry

> **JavaScript.info · Ilya Kantor e contributori.** [Originale inglese](https://javascript.info/weakref-finalizationregistry) · [Edizione italiana](https://it.javascript.info/weakref-finalizationregistry) · [Fonti e licenza](/javascript/fonti).

::: warning Un argomento avanzato e poco frequente
Queste funzionalità servono in situazioni molto specifiche. Se stai iniziando JavaScript, puoi saltare il capitolo e tornarci dopo. Il comportamento del garbage collector non è deterministico: non basare la correttezza del programma sulla sua tempistica.
:::

Nel capitolo [Garbage collection ("Spazzatura")](/javascript/tutorial/garbage-collection) abbiamo studiato la raggiungibilità: il motore mantiene in memoria gli oggetti ancora accessibili o in uso.

```js
// user mantiene un riferimento forte all'oggetto.
let user = { name: "John" };
user = null;
// Senza altri riferimenti forti, l'oggetto può essere raccolto.
```

Se c'è un secondo riferimento forte, l'oggetto rimane raggiungibile:

```js
let user = { name: "John" };
let admin = user;
user = null;
// L'oggetto è ancora raggiungibile attraverso admin.
```

La raccolta diventa possibile quando anche quel riferimento viene meno.

## Riferimenti forti e deboli

Un **riferimento forte** mantiene raggiungibile l'oggetto a cui punta. I normali riferimenti agli oggetti JavaScript sono forti.

Un **riferimento debole** permette invece al garbage collector di raccogliere il destinatario quando non restano riferimenti forti. Non ne prolunga da solo la vita.

## WeakRef

`WeakRef` contiene un riferimento debole a un oggetto, chiamato *target* o *referent*. Non ne impedisce la raccolta.

```js
let user = { name: "John" };
let admin = new WeakRef(user);
```

![](/javascript-info/1-js/99-js-misc/07-weakref-finalizationregistry/weakref-finalizationregistry-01.svg)

Ora `user` è un riferimento forte e `admin` contiene un riferimento debole. Se smettiamo di usare `user`, il garbage collector può recuperare l'oggetto:

```js
user = null;
```

Finché l'oggetto non viene effettivamente raccolto, il riferimento debole può ancora restituirlo. Non possiamo sapere in anticipo quando ciò avverrà.

![](/javascript-info/1-js/99-js-misc/07-weakref-finalizationregistry/weakref-finalizationregistry-02.svg)

Per leggere il destinatario usiamo `deref()`. Restituisce l'oggetto se è ancora disponibile, altrimenti `undefined`:

```js
let ref = admin.deref();
if (ref) {
  // L'oggetto è disponibile: possiamo usarlo.
} else {
  // Il destinatario non è più disponibile.
}
```

Mantieni il risultato in una variabile mentre lo usi. Una volta ottenuto, quel normale riferimento mantiene l'oggetto raggiungibile durante il suo utilizzo.

## Quando può servire

Una possibile applicazione è una cache di oggetti grandi, per esempio immagini rappresentate da `Blob` o `ArrayBuffer`. Vorremmo associare a ogni immagine un nome, ma lasciare che il browser recuperi memoria se nessun'altra parte del programma la usa.

- Una normale `Map` mantiene fortemente sia le chiavi sia i valori.
- Una `WeakMap` ha chiavi deboli e non accetta normali stringhe come chiavi: non risolve una cache basata su nomi con valori deboli.
- Una `Map` con stringhe come chiavi e `WeakRef` come valori può invece contenere riferimenti deboli alle immagini.

Se l'immagine è disponibile la riutilizziamo; altrimenti la ricarichiamo o la ricreiamo. Questo è utile solo quando perdere un valore della cache è accettabile.

## Esempio 1: una cache con WeakRef

```js
function fetchImg(imgName) {
  // Funzione di esempio: restituisce un oggetto immagine.
  // La logica concreta di caricamento dipende dall'applicazione.
}

function weakRefCache(fetchImg) {
  const imgCache = new Map();

  return (imgName) => {
    const cachedImg = imgCache.get(imgName)?.deref();
    if (cachedImg) return cachedImg;

    const newImg = fetchImg(imgName);
    imgCache.set(imgName, new WeakRef(newImg));
    return newImg;
  };
}

const getCachedImg = weakRefCache(fetchImg);
```

Il frammento è uno schema: per eseguirlo devi completare `fetchImg` e farle restituire un oggetto. Se il caricamento è asincrono, devi anche adattare la funzione per gestire la Promise.

1. `weakRefCache` riceve la funzione che produce l'immagine.
2. Crea una `Map` dei risultati già ottenuti.
3. Restituisce una funzione che cerca un'immagine per nome.
4. Legge l'eventuale `WeakRef` e chiama `deref()`.
5. Se il destinatario esiste, lo restituisce.
6. Altrimenti produce un nuovo oggetto.
7. Conserva un riferimento debole a quell'oggetto per un eventuale riuso.

![](/javascript-info/1-js/99-js-misc/07-weakref-finalizationregistry/weakref-finalizationregistry-03.svg)

La cache non mantiene vive da sola tutte le immagini, ma ha un limite: i nomi e gli oggetti `WeakRef` rimangono nella `Map` anche quando i loro destinatari sono stati raccolti.

![](/javascript-info/1-js/99-js-misc/07-weakref-finalizationregistry/weakref-finalizationregistry-04.svg)

Possiamo rimuovere periodicamente le voci senza destinatario oppure usare `FinalizationRegistry` come aiuto alla pulizia. Anche in quel caso la tempistica non è garantita.

## Esempio 2: osservare un elemento DOM

Immagina un logger esterno che aggiunge messaggi a una finestra della pagina. Quando quella finestra viene rimossa, il logger dovrebbe smettere di scriverci.

Nell'[esempio interattivo originale](https://javascript.info/weakref-finalizationregistry), il pulsante «Start sending messages» avvia i messaggi e «Close» rimuove la finestra.

Il codice segue questi passaggi:

1. Trova il pulsante di avvio e quello di chiusura.
2. Crea una `WeakRef` all'elemento che contiene i messaggi.
3. Collega gli eventi dei pulsanti.
4. Usa `setInterval` per generare un messaggio ogni secondo.
5. A ogni intervallo chiama `deref()`.
6. Se l'elemento esiste, lo usa; altrimenti interrompe il timer.

**Rimuovere un elemento dal DOM non significa raccoglierlo immediatamente dalla memoria.** Può rimanere raggiungibile da altri riferimenti; inoltre il garbage collector sceglie autonomamente quando intervenire. Questo esempio osserva la raccolta, non garantisce una notifica immediata della rimozione.

Gli strumenti del browser possono aiutare a osservare la memoria durante il debugging. Nel tutorial originale viene mostrato il pulsante per richiedere una raccolta in Chrome:

![](/javascript-info/1-js/99-js-misc/07-weakref-finalizationregistry/google-chrome-developer-tools.png)

La logica che deve reagire immediatamente a una chiusura dovrebbe farlo tramite un evento esplicito o un controllo della connessione al DOM, anziché attendere il garbage collector.

## FinalizationRegistry

Una **cleanup callback**, o finalizzatore, è una funzione che il runtime può richiamare dopo la raccolta di un oggetto registrato. Un **registro** conserva l'associazione fra l'oggetto osservato e il valore da passare alla callback.

```js
function cleanupCallback(heldValue) {
  // Operazioni di pulizia che non sono essenziali alla correttezza.
}

const registry = new FinalizationRegistry(cleanupCallback);
```

- `cleanupCallback` è la funzione di pulizia.
- `heldValue` è il valore da passarle. Se è un oggetto, il registro lo conserva fortemente.
- `registry` è il registro creato.

I metodi principali sono:

- `register(target, heldValue, unregisterToken)`: registra un destinatario; il token è opzionale.
- `unregister(unregisterToken)`: annulla le registrazioni associate a quel token.

Il token è spesso l'oggetto stesso. Il registro non deve conservare fortemente `target`, altrimenti ne impedirebbe la raccolta. Non usare un `heldValue` che mantenga fortemente raggiungibile il destinatario.

```js
let user = { name: "John" };

const registry = new FinalizationRegistry((heldValue) => {
  console.log(`${heldValue} has been collected by the garbage collector.`);
});

registry.register(user, user.name);
user = null;
```

Se l'oggetto viene raccolto e la callback viene eseguita, la console potrà mostrare:

```text
John has been collected by the garbage collector.
```

La callback potrebbe essere eseguita molto più tardi o non essere eseguita affatto. Per esempio, la scheda può chiudersi prima della pulizia, oppure il registro stesso può diventare irraggiungibile.

## Una cache con FinalizationRegistry

Torniamo alla cache debole: i destinatari possono essere raccolti, ma le chiavi rimangono. Un registro può aiutarci a eliminare le voci inutili:

```js
function weakRefCache(fetchImg) {
  const imgCache = new Map();

  const registry = new FinalizationRegistry((imgName) => {
    const cachedRef = imgCache.get(imgName);
    if (cachedRef && !cachedRef.deref()) imgCache.delete(imgName);
  });

  return (imgName) => {
    const cachedImg = imgCache.get(imgName)?.deref();
    if (cachedImg) return cachedImg;

    const newImg = fetchImg(imgName);
    imgCache.set(imgName, new WeakRef(newImg));
    registry.register(newImg, imgName);
    return newImg;
  };
}

const getCachedImg = weakRefCache(fetchImg);
```

Il registro associa a ogni nuova immagine il suo nome. Quando la callback arriva, controlla la voce corrente prima di eliminarla: nel frattempo il programma potrebbe aver caricato una nuova immagine con lo stesso nome.

![](/javascript-info/1-js/99-js-misc/07-weakref-finalizationregistry/weakref-finalizationregistry-05.svg)

La raccolta e l'esecuzione della callback non coincidono necessariamente. Fra i due momenti il programma continua a lavorare: una chiave potrebbe essere riutilizzata e un valore potrebbe risultare già assente anche se la pulizia non è ancora avvenuta.

Questo schema permette una pulizia opportunistica. Non garantisce che la `Map` contenga sempre soltanto voci vive e non sostituisce una politica esplicita di limite e scadenza della cache.

## Un esempio pratico: un collage di fotografie

Pensa a un servizio che mostra miniature delle fotografie sincronizzate e permette di creare un collage usando le immagini originali. Il tutorial usa questa situazione per illustrare insieme `WeakRef` e `FinalizationRegistry`.

![](/javascript-info/1-js/99-js-misc/07-weakref-finalizationregistry/weakref-finalizationregistry-demo-01.png)

Per caricare rapidamente la pagina usiamo miniature compresse, qui da 240×240 pixel. Le versioni a grandezza piena servono solo quando l'utente crea il collage.

![](/javascript-info/1-js/99-js-misc/07-weakref-finalizationregistry/weakref-finalizationregistry-demo-02.png)

Selezioniamo quattro foto e premiamo «Create collage». Per ciascuna foto la cache cerca l'originale: se manca, lo scarica e memorizza un riferimento debole.

![](/javascript-info/1-js/99-js-misc/07-weakref-finalizationregistry/weakref-finalizationregistry-demo-03.gif)

La console indica con `FETCHED_IMAGE` le immagini appena scaricate. Al primo tentativo, la cache è vuota e devono essere caricate tutte.

Quando il garbage collector raccoglie un'immagine non più raggiungibile, il finalizzatore può eliminare la relativa voce. Il messaggio `CLEANED_IMAGE` mostra quella pulizia:

![](/javascript-info/1-js/99-js-misc/07-weakref-finalizationregistry/weakref-finalizationregistry-demo-04.jpg)

Ora sostituiamo una foto e creiamo un altro collage:

![](/javascript-info/1-js/99-js-misc/07-weakref-finalizationregistry/weakref-finalizationregistry-demo-05.gif)

Se un'immagine precedente è ancora disponibile, viene riutilizzata. La console mostra `CACHED_IMAGE`, indicando che una richiesta di rete è stata evitata:

![](/javascript-info/1-js/99-js-misc/07-weakref-finalizationregistry/weakref-finalizationregistry-demo-06.jpg)

Ripetendo l'operazione, nella dimostrazione tre delle quattro immagini provengono dalla cache e solo una deve essere scaricata:

![](/javascript-info/1-js/99-js-misc/07-weakref-finalizationregistry/weakref-finalizationregistry-demo-07.gif)

![](/javascript-info/1-js/99-js-misc/07-weakref-finalizationregistry/weakref-finalizationregistry-demo-08.jpg)

In quel particolare passaggio si evitano tre richieste su quattro. **Questo risultato non è garantito:** dipende da quali immagini sono rimaste raggiungibili e da quando il garbage collector ha lavorato.

Una normale cache con dimensione massima e scadenza esplicita è spesso più semplice e prevedibile. Il tutorial mostra qui un'alternativa per capire le funzionalità del linguaggio, non una raccomandazione generale per tutte le applicazioni.

[Apri la dimostrazione originale](https://javascript.info/weakref-finalizationregistry).

## Riepilogo

`WeakRef` permette di osservare un oggetto senza mantenerlo vivo. `deref()` può restituire il destinatario oppure `undefined`.

`FinalizationRegistry` registra callback di pulizia che il runtime può eseguire dopo la raccolta. L'esecuzione non è garantita e non deve essere necessaria al corretto funzionamento del programma.

Per ulteriori dettagli consulta la [documentazione MDN di FinalizationRegistry](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/FinalizationRegistry). Questo adattamento chiarisce i limiti del garbage collector e aggiorna alcune formulazioni della fonte.
