# 19 · Accessibilità, nomi e focus

**Obiettivo:** rendere la pagina utilizzabile oltre il controllo visivo con il mouse.

## La semantica è la prima scelta

Elementi come link, pulsanti, form e titoli comunicano ruoli e relazioni al browser. Un pulsante nativo include interazione da tastiera; un `div` con un click non la acquisisce automaticamente. Mantieni una gerarchia comprensibile dei titoli, regioni riconoscibili, label visibili e link dal testo significativo.

Il *nome accessibile* identifica un controllo. Per un pulsante testuale viene normalmente dal contenuto. Per un campo usa `label`; per un'immagine considera `alt` e contesto. `aria-labelledby` può riferirsi a testo esistente; `aria-describedby` aggiunge una descrizione, non sostituisce il nome.

```html
<label for="email">Email (obbligatoria)</label>
<input id="email" name="email" type="email" required aria-describedby="aiuto-email">
<p id="aiuto-email">Riceverai soltanto le informazioni del laboratorio.</p>
```

Se un controllo ha già un testo visibile, un `aria-label` diverso può creare confusione per chi usa comandi vocali. ARIA non aggiunge il comportamento mancante; non sovrascrivere ruoli nativi senza una ragione e senza consultare i ruoli consentiti.

## Il percorso della tastiera

L'ordine del DOM deve sostenere l'ordine di lettura e focus. Prova Tab, Shift+Tab, Invio, Spazio e le frecce nei controlli che le usano. Il focus deve essere visibile: nella tappa CSS lo cureremo con `:focus-visible`.

| Attributo | Effetto e attenzione |
| --- | --- |
| Nessun `tabindex` | I controlli nativi seguono normalmente l'ordine del DOM |
| `tabindex="0"` | Inserisce un elemento nel percorso sequenziale; non gli dà il comportamento di un controllo |
| `tabindex="-1"` | Consente focus programmatico, normalmente fuori da Tab |
| `tabindex` positivo | Riordina il focus; rende difficile mantenere una sequenza coerente |
| `autofocus` | Può spostare subito il focus e far saltare contesto: usalo con criterio |
| `accesskey` | Scorciatoia dipendente dal sistema, con possibili conflitti |

`hidden`, `inert` e `aria-hidden` hanno effetti diversi. `aria-hidden` non blocca il focus: non applicarlo a controlli focalizzabili o ai loro antenati. Un dialogo modale deve gestire ingresso, permanenza e ritorno del focus; vedi la [lezione successiva](/html/interazioni-native).

## Errori e annunci

Mostra errori testuali associati ai campi e, quando necessario, uno stato come `aria-invalid="true"`. Non affidarti solo al colore. Contenuti aggiornati da JavaScript possono richiedere una live region, per esempio `role="status"`, ma annunci troppo frequenti diventano un disturbo. La scelta dipende dall'interazione reale.

## Esercizio e verifica

Percorri il progetto senza mouse. Annota il nome di ogni controllo, l'ordine del focus e dove ti trovi dopo l'apertura/chiusura di dettagli. Prova anche zoom e un lettore di schermo.

::: details Soluzione e criteri
Tutti i controlli devono essere raggiungibili e azionabili, il focus riconoscibile e i nomi pertinenti. Correggi prima markup e ordine DOM; non aggiungere numeri positivi a `tabindex` per inseguire un layout visivo. Un validatore o un audit automatico non certifica da solo l'accessibilità della pagina.
:::

Fonti: [Google/web.dev · Focus](https://web.dev/learn/html/focus), [WAI · Form](https://www.w3.org/WAI/tutorials/forms/), [WAI · Prima di usare ARIA](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/), [ARIA in HTML](https://www.w3.org/TR/html-aria/).
