# 26 · View Transitions e aggiornamenti di pagina

**Obiettivo:** capire il ponte fra CSS, navigazione e aggiornamenti JavaScript.

## Una transizione fra viste

Le View Transitions possono catturare rappresentazioni della vista precedente e successiva e comporre un passaggio. Non sono semplicemente transition su un elemento DOM: hanno un albero di pseudoelementi dedicato e regole per i gruppi e le immagini vecchia/nuova.

```js
function mostraVista(aggiorna) {
  const riduci = matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!document.startViewTransition || riduci) {
    aggiorna();
    return;
  }
  document.startViewTransition(aggiorna);
}
```

`aggiorna` è una funzione da implementare nella propria applicazione. Il fallback aggiorna il contenuto comunque. Nel corso JavaScript studieremo DOM e asincronia prima di integrare questo meccanismo in una vera applicazione.

## Personalizzare il passaggio

```css
::view-transition-old(root), ::view-transition-new(root) {
  animation-duration: 150ms;
}
.copertina-principale { view-transition-name: copertina; }
@media (prefers-reduced-motion: reduce) {
  ::view-transition-group(*) { animation-duration: 0s; }
}
```

Un nome condiviso permette di riconoscere un elemento fra viste. Non duplicare lo stesso nome su più elementi partecipanti simultaneamente. Pseudoelementi e fasi vanno verificati con il browser: un errore o una transizione saltata non deve impedire il cambio di vista.

Le transizioni nello stesso documento e quelle fra documenti hanno meccanismi e vincoli diversi. `@view-transition` riguarda l'opt-in per navigazioni supportate fra documenti della stessa origine, con condizioni di compatibilità specifiche. Un router non riceve automaticamente una corretta gestione del focus perché hai aggiunto un effetto visivo.

## Responsabilità dell'applicazione

L'aggiornamento deve mantenere URL, cronologia, titolo e focus coerenti. Snapshot di video, iframe o contenuti complessi possono avere limiti. Prova navigazioni rapide e interruzioni; evita di attendere la fine di un'animazione per consentire una nuova azione.

## Esercizio

In un esperimento JS cambia il testo di una regione con o senza API disponibile. Il risultato deve essere uguale al termine dell'operazione.

::: details Soluzione
Passa a `mostraVista` una funzione che aggiorna il testo con `textContent`. Se l'API manca o reduced motion è attivo, l'aggiornamento avviene direttamente. Non usare la transizione come sostituto di un messaggio di stato o della gestione del focus.
:::

Fonti: [web.dev · View transitions per SPA](https://web.dev/learn/css/view-transitions-spas), [MDN · View Transition API](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API).
