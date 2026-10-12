# 18 · Custom properties e property

**Obiettivo:** riusare valori e lasciare che un componente definisca le proprie varianti.

## Valori nella cascata

```css
:root { --accento: #17634d; --spazio: 1rem; }
.scheda { border: 1px solid var(--accento); padding: var(--spazio); }
.scheda.evidenza { --accento: #245b8a; --spazio: 1.5rem; }
```

Le custom properties sono proprietà CSS: partecipano alla cascata e normalmente si ereditano. Il loro nome è sensibile alle maiuscole. Non vengono sostituite tutte una volta durante la build come alcune variabili di preprocessori: il valore può dipendere dall'elemento.

`var(--nome, fallback)` usa il fallback quando la proprietà è assente o ha un valore non utilizzabile come custom property secondo le regole previste. Il fallback non è una validazione universale della proprietà finale: se `--accento` contiene `12px`, esiste ma non è un colore e la dichiarazione che lo usa può diventare invalida al valore calcolato. Una precedente dichiarazione non viene semplicemente ripescata come se var non fosse mai stata scritta.

## Registrare tipo e comportamento

```css
@property --accento {
  syntax: "<color>";
  inherits: true;
  initial-value: #17634d;
}
```

`@property` registra una grammatica, ereditarietà e valore iniziale dove supportato. Consente anche interpolazione coerente di alcuni valori animati. I descrittori hanno requisiti: il valore iniziale deve essere appropriato alla sintassi e rispettare le condizioni della specifica.

## Token, temi e componenti

```css
:root { --superficie: white; --testo: #17382d; }
@media (prefers-color-scheme: dark) {
  :root { --superficie: #17241e; --testo: #edf5ef; }
}
.scheda { color: var(--testo); background: var(--superficie); }
```

Un tema deve considerare contrasto, bordi e controlli, non soltanto invertire due colori. Non mettere ogni numero in una variabile: dai nomi ai valori che rappresentano decisioni condivise o opzioni del componente.

In JavaScript `element.style.setProperty('--accento', valore)` può modificare un token. Leggere valori calcolati usa CSSOM e viene approfondito nella [lezione 34](/css/compatibilita-cssom).

## Esercizio

Crea due schede con lo stesso CSS e accenti diversi, senza duplicare le regole di bordo e padding.

::: details Soluzione
Usa la variante `.scheda.evidenza` iniziale. Le regole del componente leggono i token e la variante cambia solo i valori. Prova una custom property non definita e un valore del tipo sbagliato per capire la differenza fra fallback e invalidazione.
:::

Fonti: [web.dev · Custom properties](https://web.dev/learn/css/custom-properties), [MDN · property](https://developer.mozilla.org/en-US/docs/Web/CSS/@property), [MDN · var](https://developer.mozilla.org/en-US/docs/Web/CSS/var).
