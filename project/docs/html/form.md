# 06 · Form accessibili

**Obiettivo:** creare controlli con etichette e capire che cosa succede quando invii un form.

## Un form di esercizio

Metti questo frammento nel `<body>` di un documento completo:

```html
<form action="" method="get">
  <p>
    <label for="nome">Nome (obbligatorio)</label>
    <input id="nome" name="nome" type="text" autocomplete="given-name" required>
  </p>
  <p>
    <label for="email">Email (obbligatoria)</label>
    <input id="email" name="email" type="email" autocomplete="email" required>
  </p>
  <p>
    <label for="messaggio">Che cosa vuoi imparare?</label>
    <textarea id="messaggio" name="messaggio" rows="4"></textarea>
  </p>
  <button type="submit">Prova l'invio</button>
</form>
```

::: warning Usiamo dati inventati
Questo è un esempio didattico, senza un servizio che riceve o salva messaggi. Con `method="get"` i dati compaiono nell'URL; `action=""` invia alla pagina corrente. Su un file aperto dal disco il comportamento può variare. Per un form reale servono una destinazione e un backend: non raccogliere dati riservati con questo esempio.
:::

## Le parti importanti

| Attributo | Funzione |
| --- | --- |
| `for` su `<label>` | Collega l'etichetta all'`id` del controllo |
| `id` | Identifica il controllo nella pagina |
| `name` | È la chiave con cui il valore viene inviato |
| `type` | Sceglie il tipo di controllo, come `email` o `text` |
| `required` | Chiede un valore prima dell'invio |
| `autocomplete` | Suggerisce al browser il tipo di dato per l'autocompletamento |

Un `placeholder` può suggerire un formato ma non sostituisce un'etichetta visibile. Gli attributi booleani, come `required`, sono attivi quando sono presenti: `required="false"` non li disattiva.

## Validazione nel browser

Prova a inviare con i campi obbligatori vuoti e poi con un indirizzo email senza `@`. Il browser segnala i problemi. Non verifica però che l'indirizzo esista.

La validazione nel browser aiuta chi compila il form. Un'applicazione reale deve validare di nuovo i dati sul server, perché i controlli del browser possono essere aggirati.

## Raggruppare opzioni

```html
<fieldset>
  <legend>Da dove vuoi partire?</legend>
  <label><input type="radio" name="argomento" value="html" checked> HTML</label>
  <label><input type="radio" name="argomento" value="css"> CSS</label>
</fieldset>
```

Le opzioni con lo stesso `name` formano un gruppo: puoi sceglierne una. `fieldset` e `legend` danno al gruppo un'etichetta comune.

## Esercizio

Aggiungi una scelta fra HTML e CSS e una casella «Voglio fare un esercizio ogni giorno». Prova tutto con la tastiera: `Tab` per spostarti, spazio per selezionare una casella, frecce per le opzioni radio.

::: details Una possibile soluzione
Inserisci il `fieldset` dell'esempio prima del pulsante, poi aggiungi:
```html
<p>
  <label>
    <input type="checkbox" name="pratica" value="giornaliera">
    Voglio fare un esercizio ogni giorno
  </label>
</p>
```
Una casella non selezionata non invia il proprio valore. Le opzioni radio inviano il valore di quella selezionata.
:::
