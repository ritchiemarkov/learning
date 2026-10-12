# 16 · Tutti i controlli e i 22 tipi di input

**Obiettivo:** scegliere il controllo che rappresenta il dato, comprese le alternative a `input`.

## I tipi di input dello snapshot

| Tipo | Uso e attenzione |
| --- | --- |
| `text` | Testo su una riga; default se il tipo manca o non è riconosciuto |
| `search` | Query di ricerca |
| `email` | Indirizzo email; il formato non prova l'esistenza dell'indirizzo |
| `url` | URL; la validità sintattica non prova che il sito sia affidabile |
| `tel` | Telefono; non impone un formato telefonico universale |
| `password` | Nasconde visivamente il testo; non cifra il trasporto |
| `number` | Quantità numerica; evita per codici postali e identificatori |
| `range` | Quantità su un intervallo quando serve una regolazione |
| `date` | Data, valore macchina `YYYY-MM-DD` |
| `month` | Anno e mese, `YYYY-MM` |
| `week` | Settimana ISO, per esempio `2026-W45` |
| `time` | Ora senza fuso |
| `datetime-local` | Data e ora senza fuso: il server deve conoscere il contesto |
| `color` | Colore; `alpha` e `colorspace` sono estensioni da verificare |
| `checkbox` | Scelta indipendente; se non selezionata non invia una voce |
| `radio` | Una scelta in un gruppo con lo stesso `name` |
| `file` | File locale scelto dall'utente; `accept` è un suggerimento |
| `hidden` | Dato inviato senza controllo visibile; può essere manipolato |
| `submit` | Invio del form, con etichetta in `value` |
| `image` | Invio con immagine; richiede `alt`, invia coordinate |
| `reset` | Ripristino dei valori iniziali; può far perdere lavoro |
| `button` | Pulsante senza azione predefinita |

Non tutti gli attributi sono applicabili a tutti i tipi. Il widget e il formato mostrato variano per browser e lingua; il valore inviato segue la grammatica prevista. Il tipo storico `datetime` non appartiene all'inventario moderno.

## Scelte, suggerimenti e testo

```html
<label for="corso">Corso</label>
<select id="corso" name="corso" required>
  <option value="">Scegli un corso</option>
  <optgroup label="Frontend">
    <option value="html">HTML</option>
    <option value="css">CSS</option>
  </optgroup>
</select>
<label for="citta">Città</label>
<input id="citta" name="citta" list="citta-note">
<datalist id="citta-note"><option value="Roma"><option value="Milano"></datalist>
<label for="note">Note</label>
<textarea id="note" name="note" rows="4" cols="40" maxlength="500"></textarea>
```

`select`, `option` e `optgroup` offrono scelte. `selected` marca la scelta iniziale, `disabled` un'opzione indisponibile, `multiple` abilita più scelte e `size` influenza le righe visualizzate. `datalist` suggerisce valori ma non impedisce altri input; verifica il suo funzionamento con tecnologie assistive. Il contenuto di `textarea` è il valore iniziale, non un attributo `value`; `wrap` influisce sul trattamento delle righe.

La variante di select personalizzabile e `selectedcontent` sono trattati fra le [funzioni recenti](/html/compatibilita). Non assumere che tutti i browser accettino lo stesso nuovo modello di contenuto.

## Risultati e misure

```html
<label for="posti">Occupazione</label>
<meter id="posti" min="0" max="20" low="5" high="15" optimum="10" value="12">12 su 20</meter>
<label for="invio">Caricamento</label>
<progress id="invio" max="100" value="40">40%</progress>
<output name="totale" for="quantita prezzo">60 €</output>
```

`meter` è una misura in un intervallo; `progress` l'avanzamento di un processo, indeterminato quando manca `value`. `output` rappresenta un risultato, ma non lo calcola automaticamente. Il suo `for` può riferirsi a più ID, diversamente da quello di `label`. Il risultato non è un normale campo inviato come `input`.

## Esercizio e verifica

Scegli controlli per email, CAP, numero di partecipanti e data dell'incontro. Dai un'etichetta a ciascuno.

::: details Soluzione
Email: `email`; CAP: `text` con `inputmode="numeric"` (preserva zeri iniziali); partecipanti: `number` con `min="1" step="1"`; data: `date`. Usa `label for` e ID unici. Nessun controllo sostituisce la verifica sul server.
:::

Fonti: [MDN · input](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input), [MDN · select](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select), [WHATWG · Controlli](https://html.spec.whatwg.org/multipage/form-elements.html).
