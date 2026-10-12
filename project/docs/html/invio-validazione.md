# 17 · Form: invio, vincoli e dati

**Obiettivo:** prevedere quali dati vengono inviati e distinguere validazione e sicurezza.

## Destinazione e codifica

```html
<form id="iscrizione" action="/iscrizioni" method="post" enctype="multipart/form-data">
  <label for="email">Email</label>
  <input id="email" name="email" type="email" autocomplete="email" required>
  <label for="allegato">Allegato PDF</label>
  <input id="allegato" name="allegato" type="file" accept="application/pdf">
  <button type="submit">Invia iscrizione</button>
</form>
```

L'endpoint è didattico: per ricevere dati occorre implementarlo. `get` mette i dati nella query e si usa per operazioni come ricerca; `post` li invia nel corpo. POST da solo non cifra niente: serve HTTPS. `method="dialog"` chiude un dialogo senza il normale invio HTTP.

La codifica predefinita è `application/x-www-form-urlencoded`; `multipart/form-data` serve all'invio dei file; `text/plain` ha usi limitati e non è il formato da scegliere per un normale backend. `accept-charset` moderno ammette UTF-8. `target` sceglie il contesto della risposta.

## Quali controlli contribuiscono?

I dati usano `name`, non `id`. Controlli disabilitati, checkbox non selezionate e radio non selezionati normalmente non contribuiscono. Un controllo `readonly` può contribuire. Se due controlli condividono un nome, la richiesta può avere più valori per quella chiave. Solo il pulsante di invio effettivamente usato contribuisce con il proprio nome e valore.

Un controllo esterno può appartenere al form tramite `form="iscrizione"`. `fieldset disabled` disabilita un gruppo con l'eccezione prevista per il primo `legend`. Un pulsante può sovrascrivere la destinazione e il metodo con `formaction`, `formmethod`, `formenctype`, `formtarget`, `formnovalidate`.

## Vincoli applicabili

| Attributo | Che cosa controllare |
| --- | --- |
| `required` | Presenza del valore; effetto dipendente dal controllo |
| `minlength`, `maxlength` | Lunghezza per tipi testuali applicabili |
| `min`, `max`, `step` | Intervalli e passi per numeri/date/ore applicabili |
| `pattern` | Intero valore testuale secondo l'espressione prevista; mostra istruzioni visibili |
| `multiple` | Più valori/file dove supportato |
| `readonly`, `disabled` | Modificabilità e partecipazione all'invio differenti |
| `novalidate` | Disabilita la validazione interattiva del form all'invio |

Un campo facoltativo vuoto non diventa obbligatorio soltanto perché ha `pattern`. `placeholder` non è una label; `size` non è un limite di caratteri. `accept` non verifica il contenuto del file. `autocomplete` può indicare dati come `given-name`, `email`, `new-password` e gruppi: scegli token pertinenti. `inputmode` e `enterkeyhint` suggeriscono la tastiera; non validano.

JavaScript può usare `checkValidity()`, `reportValidity()` e `setCustomValidity()` e leggere `validity`; il corso JS approfondisce questi metodi. Evita messaggi che indicano soltanto «errore»: mostra cosa correggere. Il server deve verificare formato, dimensioni, autorizzazioni e regole del dominio, anche per campi hidden.

## Esercizio e verifica

Prevedi la richiesta: email compilata, checkbox non selezionata, campo disabled con nome, campo readonly con nome. Poi controllala nella scheda Network contro un endpoint di esercizio locale.

::: details Soluzione
Email e readonly contribuiscono; checkbox non selezionata e disabled no. Non provare dati personali sul sito didattico. Nel primo esempio l'upload richiede POST multipart e un server che lo gestisca; la pagina statica non lo salva.
:::

Fonti: [Google/web.dev · Form](https://web.dev/learn/html/forms), [MDN · Validazione](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation), [WHATWG · Invio](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html).
