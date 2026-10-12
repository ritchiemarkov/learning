# 20 · Details, dialog e popover

**Obiettivo:** usare interazioni native e riconoscere quali comportamenti richiedono JavaScript.

## Details e summary

```html
<details>
  <summary>Quali strumenti servono?</summary>
  <p>Un editor e un browser.</p>
</details>
```

`summary` è l'etichetta del controllo di espansione e precede il contenuto. `open` è booleano: `open="false"` apre comunque il pannello. Più `details` con lo stesso `name` possono formare un gruppo esclusivo nei browser che supportano la funzione. Non nascondere informazioni essenziali solo per ridurre l'altezza della pagina e non trasformare il summary in una raccolta di altri controlli interattivi.

## Dialoghi modali e non modali

```html
<button id="apri" type="button">Mostra informazioni</button>
<dialog id="informazioni" aria-labelledby="titolo-dialogo">
  <h2 id="titolo-dialogo">Informazioni sul corso</h2>
  <p>Ogni laboratorio dura due ore.</p>
  <form method="dialog"><button type="submit">Chiudi</button></form>
</dialog>
<script type="module">
  const dialogo = document.querySelector('#informazioni');
  document.querySelector('#apri').addEventListener('click', () => dialogo.showModal());
</script>
```

`showModal()` apre nel top layer e rende inerte il resto della pagina; `show()` apre un dialogo non modale. Aggiungere soltanto `open` non crea la stessa modalità. Un form con `method="dialog"` può chiuderlo senza invio HTTP. Un dialogo richiede un nome, una chiusura comprensibile e una destinazione sensata per il focus. Prova Escape, navigazione interna e ritorno al pulsante iniziale.

Gli attributi recenti `closedby`, `command` e `commandfor` permettono ulteriori comportamenti dichiarativi. Per esempio `command="show-modal"` su un button che punta al dialogo può sostituire l'apertura via script dove supportato. La conformità allo standard non garantisce che ogni browser li implementi: conserva un fallback o verifica i browser del progetto. Comandi personalizzati non implementano da soli una funzione dell'applicazione.

## Popover

```html
<button type="button" popovertarget="aiuto">Mostra un suggerimento</button>
<div id="aiuto" popover>Puoi iniziare dalla lezione 01.</div>
```

Il popover entra nel top layer ma non rende modale il resto della pagina. `auto` offre comportamento automatico di apertura/chiusura; `manual` richiede gestione esplicita; `hint` appartiene alle estensioni recenti da verificare. `popovertargetaction` può essere `show`, `hide`, `toggle`. Un popover non è automaticamente un tooltip, un menu ARIA o una finestra modale.

Scegli secondo il bisogno: dettagli per un approfondimento nella pagina, dialogo per un'interazione separata, popover per contenuto temporaneo non modale. In ogni caso verifica posizione, tastiera e contenuto su schermi diversi.

## Esercizio e verifica

Crea una FAQ con details e un popover di aiuto. Aggiungi poi il dialogo dell'esempio in un file HTML locale.

::: details Soluzione e criteri
La FAQ deve aprirsi con tastiera e avere un summary comprensibile. Il popover deve apparire dal pulsante e chiudersi secondo il tipo scelto. Il dialogo deve aprirsi con `showModal()`, chiudersi e restituire il focus. Senza supporto o JavaScript, lascia disponibili in pagina le informazioni necessarie.
:::

Fonti: [MDN · dialog](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dialog), [MDN · popover](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/popover), [MDN · button](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button), [Google/web.dev · Details](https://web.dev/learn/html/details).
