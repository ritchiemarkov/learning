---
title: "Dynamic imports"
description: "JavaScript.info in italiano: Dynamic imports"
sourceTutorial: true
prev: {"text": "Export e Import", "link": "/javascript/tutorial/import-export"}
next: {"text": "Proxy e Reflect", "link": "/javascript/tutorial/proxy"}
---

# Dynamic imports

> **JavaScript.info · Ilya Kantor e contributori.** [Originale inglese](https://javascript.info/modules-dynamic-imports) · [Edizione italiana](https://it.javascript.info/modules-dynamic-imports) · [Fonti e licenza](/javascript/fonti).

Le istruzioni di export ed import che abbiamo visto nei capitolo precedente sono detti "statici". La sintassi è molto semplice e rigorosa.

Come prima cosa, non possiamo generare dinamicamente parametri di `import`.

Il percorso al modulo deve essere una stringa, non può essere una chiamata a funzione. Questo non funzionerebbe:

```js
import ... from getModuleName(); // Errore, sono ammesse solamente string
```

Secondo, non possiamo importare a run-time in base a determinate condizioni:

```js
if(...) {
  import ...; // Errore, non è possibile farlo!
}

{
  import ...; // Errore, non possiamo scrivere gli import all'interno di nessun blocco
}
```

Questo accade perché `import`/`export` mirano a fornire uno scheletro per la struttura del codice. Questa è una buona cosa, poiché la struttura del codice può essere analizzata, i moduli possono essere raccolti and impacchettati in un singolo file (grazie ad alcuni strumenti) e gli export inutilizzati possono essere rimossi ("tree-shaken"). Questo è possibile solamente perché la struttura degli imports/exports è semplice e preimpostata.

Ma come possiamo importare un modulo dinamicamente, a seconda delle necessità?

## L'espressione import()

L'espressione `import(module)` carica il modulo e ritorna una promise, che si risolve in un oggetto che contiene tutti gli export del modulo. Può essere quindi invocata in un qualsiasi punto del codice.

Possiamo utilizzarla dinamicamente ovunque, ad esempio:

```js
let modulePath = prompt("Which module to load?");

import(modulePath)
  .then(obj => <module object>)
  .catch(err => <loading error, e.g. if no such module>)
```

oppure, potremmo utilizzare `let module = await import(modulePath)` se ci troviamo all'interno di una funzione asincrona.

Ad esempio, se abbiamo il seguente modulo `say.js`:

```js
// 📁 say.js
export function hi() {
  alert(`Hello`);
}

export function bye() {
  alert(`Bye`);
}
```

...Allora il dyamic import può essere scritto così:

```js
let {hi, bye} = await import('./say.js');

hi();
bye();
```

Oppure, se `say.js` ha un default export:

```js
// 📁 say.js
export default function() {
  alert("Module loaded (export default)!");
}
```

...Quindi, per potervi accedere, possiamo utilizzare la proprietà `default` dell'oggetto:

```js
let obj = await import('./say.js');
let say = obj.default;
// o, in una riga: let {default: say} = await import('./say.js');

say();
```

Qui vediamo l'esempio completo:

[Apri l’esempio nella fonte originale](https://it.javascript.info/modules-dynamic-imports).


::: tip Da sapere
I dynamic import funzionano negli script regolari, non richiedono `script type="module"`.
:::


::: tip Da sapere
Anche se `import()` sembra una chiamata a funzione, in realtà è una speciale sintassi che utilizza le parentesi (in modo simile a `super()`).

Quindi non possiamo copiare `import` in una variabile o utilizzare `call/apply`. Non è una funzione.
:::
