---
title: "Form: eventi e metodi di submit"
description: "JavaScript.info in italiano: Form: eventi e metodi di submit"
sourceTutorial: true
prev: {"text": "Eventi: change, input, cut, copy, paste", "link": "/javascript/tutorial/events-change-input"}
next: {"text": "Page: DOMContentLoaded, load, beforeunload, unload", "link": "/javascript/tutorial/onload-ondomcontentloaded"}
---

# Form: eventi e metodi di submit

> **JavaScript.info · Ilya Kantor e contributori.** [Originale inglese](https://javascript.info/forms-submit) · [Edizione italiana](https://it.javascript.info/forms-submit) · [Fonti e licenza](/javascript/fonti).

L'evento `submit` si scatena quando il form viene inviato, e solitamente viene usato per validare il form prima dell'invio al server o per annullare l'invio e elaborarlo con JavaScript.

Il metodo `form.submit()` ci permette di iniziare l'invio del form da JavaScript. Possiamo usarlo per creare ed inviare i nostri form al server dinamicamente.

Andiamo più nel dettaglio.

## Evento: submit

Ci sono due modi per inviare un form:

1. Il primo -- cliccare `<input type="submit">` o `<input type="image">`.
2. Il secondo -- premere `key:Enter` su un campo di input.

Entrambe le azioni portano all'evento `submit` del form. Il gestore può controllare i dati, ed in caso di errori, può mostrarli e chiamare `event.preventDefault()`, ed a quel punto il form non viene inviato al server.

Nel form seguente:
1. Andare nel campo di testo e premere `key:Enter`.
2. Cliccare `<input type="submit">`.

Entrambe le azioni mostrano un `alert` ed il form non viene inviato da nessuna parte a causa di `return false`:

```html
<form onsubmit="alert('submit!');return false">
  Primo: Entrare nel campo di testo <input type="text" value="text"><br>
  Secondo: Clicare "submit": <input type="submit" value="Submit">
</form>
```


:::: tip Relation between `submit` and `click`
Quando un form viene inviato usando `key:Enter` su un campo di input, un evento `click` viene scaturito sull'elemento `<input type="submit">`.

Ciò è piuttosto divertente, dal momento che non c'è stato nessun click.

Ecco la demo:
```html
<form onsubmit="return false">
 <input type="text" size="30" value="Porre il focus qui e premere Invio">
 <input type="submit" value="Submit" onclick="alert('click')">
</form>
```

::::

## Metodo: submit

Per eseguire l'invio (submit)  di un form sul server manualmente, possiamo chiamare `form.submit()`.

In questo caso l'evento di `submit` non viene generato. Si assume che il programmatore chiamando `form.submit()`, abbia previsto che nello script siano state considerate tutte le dovute elaborazioni.

Talvolta viene usato per creare ed inviare manualmente un form, come in questo esempio:

```js
let form = document.createElement('form');
form.action = 'https://google.com/search';
form.method = 'GET';

form.innerHTML = '<input name="q" value="test">';

// il form deve essere nel documento per poterlo inviare
document.body.append(form);

form.submit();
```

## Esercizi

### 1 · Modal form

Create una funzione `showPrompt(html, callback)` che mostra un form con un messaggio `html`, un campo di input ed i pulsanti `OK/CANCEL`.

- Un utente dovrebbe digitare qualcosa nel campo di testo e premere `key:Enter` o il pulsante OK, quindi verrà chiamata `callback(value)` con il valore che è stato inserito.
- Altrimenti, se l'utente preme `key:Esc` oppure CANCEL, viene chiamata `callback(null)`.

In entrambi i casi, questo termina l'elaborazione dell'input e rimuove il form.

Requisiti:

- Il form dovrebbe essere al centro della finestra.
- Il form è *modal*. In altre parole, non possono esserci interazioni con il resto della pagina fino a quando non viene chiusa.
- Quando viene mostrato il form, il focus dovrebbe essere dentro il campo `<input>` per l'utente.
- I tasti `key:Tab`/`key:Shift+Tab` dovrebbe cambiare il focus tra i campi del form, e non permettergli di lasciarlo per altri elementi della pagina.

Un esempio di come dovrebbe funzionare:

```js
showPrompt("Enter something<br>...smart :)", function(value) {
  alert(value);
});
```

Una demo nell'iframe:

[Apri l’esempio nella fonte originale](https://it.javascript.info/forms-submit).

P.S.: Il sorgente del documento ha HTML e CSS per il form, con posizionamento fixed, ma sta a te renderla modale.

::::: details Soluzione

Una finestra modale può essere implementata usando un `<div id="cover-div">` semitrasparente che copre l'intera finestra, in questa maniera:

```css
#cover-div {
  position: fixed;
  top: 0;
  left: 0;
  z-index: 9000;
  width: 100%;
  height: 100%;
  background-color: gray;
  opacity: 0.3;
}
```

Dato che il `<div>` copre ogni cosa, sarà questo elemento a catturare tutti i click, e non la pagina sottostante.

Inoltre può essere prevenuto lo scrolling della pagina impostando `body.style.overflowY='hidden'`.

Il form non dovrebbe essere dentro il `<div>`, ma subito dopo nel codice della pagina (quindi starà anche sopra), perché non vogliamo che sia soggetto alla trasparenza dovuta ad `opacity`.

:::::

