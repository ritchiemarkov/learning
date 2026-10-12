# 16 · Selettori avanzati, nesting e scope

**Obiettivo:** selezionare relazioni e stati mantenendo prevedibile la specificità.

## Funzioni di selezione

```css
:where(article, section) > h2 { margin-block-start: 0; }
.scheda:is(.disponibile, .nuova) { border-color: #17634d; }
.scheda:not(.esaurita) { background: white; }
.campo:has(input:focus-visible) { border-color: #245b8a; }
li:nth-child(2n) { background: #f4f8f5; }
```

`:is()` unisce alternative e prende la specificità dell'argomento più specifico; `:where()` mantiene peso zero per sé e i suoi argomenti. Anche `:not()` e `:has()` hanno regole di specificità legate agli argomenti. Un ID inserito in una lista può quindi influenzare il peso anche quando pensavi di usare soltanto una classe.

`:has()` seleziona in base a relazioni: non è limitato ai figli diretti. Restringi il contesto e verifica che una selezione dinamica ampia non produca lavoro inutile. `:nth-child(... of selettore)` conta nella lista filtrata dove supportato; `nth-of-type` ragiona sul tipo dell'elemento.

## Pseudoelementi

`::before` e `::after` richiedono normalmente `content` per generare contenuto. `::first-letter`, `::first-line`, `::selection`, `::marker` e `::placeholder` agiscono su parti differenti con proprietà applicabili diverse. Il contenuto generato non è il luogo per istruzioni essenziali o per sostituire una label.

```css
.nota::before { content: ""; display: inline-block; inline-size: 0.5em; block-size: 0.5em; background: currentColor; margin-inline-end: 0.5em; }
```

## Nesting nativo

```css
.scheda {
  padding: 1rem;
  & > h2 { margin-block-start: 0; }
  &:hover { border-color: #17634d; }
}
```

`&` si riferisce al selettore del contesto. Nesting CSS nativo non è semplicemente copia della sintassi di Sass: verifica regole, specificità e browser. Annidare molti livelli può rendere il foglio difficile da modificare anche se il codice è più corto.

`@scope (.scheda) { ... }` limita l'applicazione a un sottoalbero e permette confini. La prossimità dello scope può intervenire nella cascata dopo la specificità. Non è Shadow DOM e non garantisce isolamento di tutte le proprietà ereditate.

## Esercizio

Seleziona una scheda solo quando contiene un'immagine figlia diretta; dai ai suoi titoli uno stile base facile da sovrascrivere.

::: details Soluzione
```css
.scheda:has(> img) { padding-block-start: 0; }
:where(.scheda h2) { font-size: 1.5rem; }
```
`:where()` non aumenta il peso. Prova una successiva classe `.titolo` sullo stesso h2 e verifica la cascata. Fornisci una classe esplicita come fallback se il progetto include browser senza has.
:::

Fonti: [MDN · has](https://developer.mozilla.org/en-US/docs/Web/CSS/:has), [MDN · scope](https://developer.mozilla.org/en-US/docs/Web/CSS/@scope), [web.dev · Nesting](https://web.dev/learn/css/nesting), [MDN · Pseudoelementi](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-elements).
