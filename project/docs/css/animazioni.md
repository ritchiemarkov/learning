# 25 · Keyframes e animazioni legate allo scroll

**Obiettivo:** descrivere una sequenza e capire quando deve cessare o non partire.

## Keyframes e impostazioni

```css
@keyframes comparsa {
  from { opacity: 0; transform: translateY(0.5rem); }
  to { opacity: 1; transform: none; }
}
@media (prefers-reduced-motion: no-preference) {
  .avviso { animation: comparsa 180ms ease-out both; }
}
```

Un'animazione usa fotogrammi chiave invece di richiedere un cambio fra due stati esterni. Name, duration, timing-function, delay, iteration-count, direction, fill-mode e play-state definiscono il comportamento. La shorthand può ripristinare impostazioni omesse: controlla le proprietà risultanti.

`both` applica gli effetti di fill previsti prima e dopo l'esecuzione; non riscrive permanentemente il markup. Animazioni concorrenti su una stessa proprietà possono competere secondo composizione e cascata. L'esempio è facoltativo: il contenuto deve essere visibile anche se non c'è supporto o movimento consentito.

## Tempo e timeline di scroll

```css
@keyframes crescita { from { scale: 0 1; } to { scale: 1 1; } }
@supports (animation-timeline: scroll()) {
  @media (prefers-reduced-motion: no-preference) {
    .progresso-lettura {
      transform-origin: left;
      animation: crescita auto linear both;
      animation-timeline: scroll(root);
    }
  }
}
```

È un frammento per un indicatore decorativo da costruire separatamente. Scroll timeline segue l'avanzamento dello scorrimento; view timeline può seguire il passaggio di un elemento nel viewport pertinente. `animation-range`, timeline nominate e scope permettono altri controlli, con supporto da verificare per ciascuna funzione. La shorthand animation può resettare la timeline: assegnala dopo.

## Controllo dell'utente

Evita loop continui senza finalità. Un contenuto in movimento persistente può richiedere pausa, arresto o possibilità di nasconderlo. Non usare lampi o grandi movimenti per comunicare uno stato che si può rappresentare con testo. Reduced motion è una preferenza da rispettare, non un motivo per eliminare la funzione.

## Esercizio

Applica un'entrata breve a un avviso non essenziale. Poi disattiva il movimento nel sistema e verifica che il testo compaia immediatamente.

::: details Soluzione
Usa la query iniziale senza porre opacity zero nella base. Quando la query non corrisponde, `.avviso` mantiene il suo normale aspetto. La presenza dell'animazione non deve cambiare il messaggio accessibile né ritardare l'attivazione di un controllo.
:::

Fonti: [web.dev · Animazioni](https://web.dev/learn/css/animations), [MDN · Scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_scroll-driven_animations), [MDN · Keyframes](https://developer.mozilla.org/en-US/docs/Web/CSS/@keyframes).
