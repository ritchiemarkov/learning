# 32 · Organizzazione, debugging e prestazioni

**Obiettivo:** correggere una causa osservata e mantenere il foglio modificabile.

## Un percorso di debugging

1. Controlla che il file giusto sia caricato e non provenga da una cache inattesa.
2. Seleziona l'elemento nel DOM reale.
3. In Styles verifica selettori, valori invalidi, regole superate, media query e layer.
4. In Computed cerca il valore risultante e la sua origine.
5. Per layout controlla box model, containing block, minimi e overlay grid/flex.

Non aggiungere una nuova regola finché non sai quale proprietà sta producendo l'effetto. Una dichiarazione barrata può essere corretta ma perdere nella cascata; una proprietà non barrata può avere un effetto diverso nel layout corrente.

## Organizzare componenti e varianti

```css
@layer base, componenti, utilita;
@layer componenti {
  .scheda { padding: var(--spazio, 1rem); border: 1px solid #b9ccc3; }
  .scheda--compatta { --spazio: 0.75rem; }
}
```

Nomi di componenti e varianti sono convenzioni, non nuove funzioni CSS. Un approccio come BEM, CSS Modules o utility può essere utile secondo il progetto; comprende prima cascata, ambito e costi di riuso. Un preprocessore non è un prerequisito del corso. Evita selettori profondi dipendenti da contenitori accidentali.

## Lavoro del browser

Stile, layout, pittura e composizione sono fasi distinte. Un cambio di dimensioni può influenzare molti elementi; un filtro grande può costare in pittura; una trasformazione può avere un trattamento diverso. Misura nel pannello Performance con contenuti e dispositivi pertinenti, non usare il numero di righe del CSS come misura della velocità.

```css
.sezione-lunga { content-visibility: auto; contain-intrinsic-size: auto 40rem; }
```

Questo è un esperimento per sezioni grandi, non un reset globale. Content-visibility e containment possono ridurre lavoro fuori vista ma modificano assunzioni di dimensionamento e rendering. Il valore intrinseco deve riflettere il contenuto abbastanza da non produrre salti indesiderati. Verifica ricerca nella pagina, ancore, accessibilità e scorrimento.

Will-change va usato per un problema misurato e limitato: mantenere molti layer può consumare memoria. Rimuovere CSS non usato e limitare font/risorse può essere più utile di un effetto hardware aggiunto a tutto.

## Esercizio

Una scheda eccede la colonna grid per un URL lungo. Spiega perché `overflow: hidden` sul body maschera il problema.

::: details Soluzione
Controlla minimi della colonna/item, dimensione della risorsa e wrapping. Puoi usare minmax zero, min-inline-size zero e overflow-wrap sul testo secondo il caso. Nascondere overflow del body taglia contenuti e focus senza correggere la dimensione che ha causato l'errore.
:::

Fonti: [Chrome DevTools · CSS](https://developer.chrome.com/docs/devtools/css), [MDN · Containment](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_containment), [MDN · Content visibility](https://developer.mozilla.org/en-US/docs/Web/CSS/content-visibility).
