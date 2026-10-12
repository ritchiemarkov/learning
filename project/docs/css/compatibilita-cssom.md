# 34 · Compatibilità, supports e CSSOM

**Obiettivo:** aggiungere miglioramenti senza rendere il risultato dipendente da una singola funzione recente.

## Base e miglioramento

```css
.schede { display: flex; flex-wrap: wrap; gap: 1rem; }
.schede > article { flex: 1 1 16rem; }
@supports (display: grid) {
  .schede { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 16rem), 1fr)); }
}
```

Supports valuta se il browser riconosce la condizione dichiarata. Non garantisce assenza di bug, interoperabilità o accessibilità. Puoi interrogare selettori con la forma prevista da selector e combinare condizioni con and/or/not. Le media query interrogano l'ambiente; le support query la funzione: non sono la stessa scelta.

Una dichiarazione non riconosciuta viene normalmente ignorata, quindi valori successivi possono migliorare una base valida. Attenzione a custom properties e valori invalidi al tempo di calcolo: non ogni fallback segue lo stesso comportamento.

## Leggere la documentazione

Per ogni funzione nuova verifica proprietà o valore esatto, tabella di compatibilità, stato dello standard e vincoli. «Baseline» non significa che ogni dispositivo storico la supporti; «experimental» non significa che devi usarla per avere un corso completo. I prefissi vendor appartengono a supporti specifici: un processo come Autoprefixer dipende dai browser target, non sostituisce le verifiche.

CSS si sviluppa in molti moduli. Il [CSS Snapshot W3C](https://www.w3.org/TR/css/) distingue livelli di stabilità e inventari; non esiste un singolo «CSS3 completo» congelato che esaurisca ogni futura proprietà.

## Il ponte con JavaScript

```js
const scheda = document.querySelector('.scheda');
scheda.style.setProperty('--accento', '#245b8a');
const colore = getComputedStyle(scheda).color;
const supportaGrid = CSS.supports('display', 'grid');
```

Element.style riguarda dichiarazioni inline, non tutto il CSS applicato. GetComputedStyle restituisce valori risolti secondo la proprietà; la rappresentazione non coincide necessariamente con il testo scritto nel foglio. Leggere layout subito dopo molte scritture può imporre lavoro di aggiornamento: in JS organizzeremo letture e scritture quando la misura lo richiede.

CSSOM comprende fogli, regole e API correlate, con limitazioni di accesso per risorse cross-origin. Non tentare di aggirare queste limitazioni usando il foglio come archivio di dati.

## Esercizio

Progetta una scheda che resti leggibile senza container query e subgrid. Documenta un miglioramento e il suo fallback.

::: details Soluzione
Base a colonna con flex e altezza libera; container query affianca contenuti quando lo spazio lo consente e subgrid allinea track dove previsto. Disabilita le regole avanzate in DevTools: dati, focus e azioni devono rimanere completi. Non basta che CSS.supports restituisca true.
:::

Fonti: [MDN · Supports](https://developer.mozilla.org/en-US/docs/Web/CSS/@supports), [MDN · CSSOM](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Object_Model), [W3C · CSS Snapshot](https://www.w3.org/TR/css/).
