# 24 · Trasformazioni e transizioni

**Obiettivo:** rendere comprensibile un cambio di stato senza rallentare l'interazione.

## Due stati, un passaggio

```css
.pulsante { background-color: #17634d; color: white; }
@media (prefers-reduced-motion: no-preference) {
  .pulsante { transition: background-color 150ms ease-out, transform 150ms ease-out; }
  .pulsante:active { transform: translateY(1px); }
}
.pulsante:hover { background-color: #174f3e; }
```

Una transition interpola un cambiamento di proprietà. Definisci proprietà, durata, curva e ritardo. Metterla nello stato base permette di gestire sia ingresso sia uscita. Evita `transition: all`: include cambiamenti futuri che potrebbero non dover essere animati.

Il movimento deve avere uno scopo, come feedback breve, e la funzione deve restare completa senza di esso. Un ritardo lungo o una transizione su ogni click può rendere la pagina meno pronta.

## Transform non cambia il layout normale

`translate`, `rotate`, `scale`, `skew` e `matrix` trasformano la rappresentazione; l'ordine delle funzioni conta. `transform-origin` stabilisce il punto di riferimento. Le proprietà individuali translate/rotate/scale hanno un ordine di composizione definito e non sono una sostituzione testuale arbitraria della lista transform.

Trasformare un elemento non ridistribuisce necessariamente lo spazio come modificare width. Può creare un containing block e uno stacking context: controlla elementi fixed e sovrapposizioni. Le trasformazioni 3D usano anche perspective, transform-style e backface-visibility; non sono necessarie per un pulsante.

## Prestazioni e tipi di valore

Transform e opacity spesso evitano alcuni costi di layout/pittura, ma la prestazione dipende dal contenuto, dai layer e dal dispositivo. Animare height o width può richiedere layout a ogni frame. Misura prima di aggiungere `will-change`, che non è un acceleratore gratuito.

Non tutte le proprietà interpolano allo stesso modo. Cambi discreti, display e entrata/uscita di elementi richiedono meccanismi moderni come `transition-behavior` e `@starting-style` dove supportati. Mantieni una base che compia comunque il cambio di stato.

## Esercizio

Fai cambiare sfondo a un pulsante e aggiungi un feedback di pressione che rispetti reduced motion.

::: details Soluzione
Usa l'esempio iniziale: il colore cambia sempre, la piccola trasformazione e la transizione sono dentro la query no-preference. Prova attivazioni rapide e uscita del puntatore. Il focus della lezione 13 deve restare visibile e indipendente dall'effetto.
:::

Fonti: [web.dev · Transizioni](https://web.dev/learn/css/transitions), [MDN · Transforms](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_transforms), [MDN · Reduced motion](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion).
