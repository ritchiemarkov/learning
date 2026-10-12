# 25 · Compatibilità, funzioni recenti e HTML storico

**Obiettivo:** distinguere una regola dello standard, una funzione implementata e una vecchia funzionalità ancora tollerata.

## Tre domande diverse

1. **È conforme?** Leggi la specifica e il modello dell'elemento.
2. **È implementato nei browser del progetto?** Controlla la tabella di compatibilità e prova.
3. **È utilizzabile nel nostro contesto?** Verifica tastiera, tecnologie assistive, contenuto e fallback.

Il browser può visualizzare elementi obsoleti per compatibilità con vecchie pagine. Questo non li rende appropriati per un nuovo documento. Al contrario, una funzione nello standard può avere supporto ancora parziale. Baseline descrive disponibilità fra browser, non una certificazione completa di accessibilità o di qualità.

## Funzioni da verificare separatamente

| Funzione | Cosa studiare e quale base conservare |
| --- | --- |
| `search` | Semantica della regione di ricerca; conserva form ed etichette |
| Popover e valore `hint` | Tipi di chiusura e focus; mantieni informazioni essenziali accessibili |
| `command`, `commandfor`, `closedby` | Controllo dichiarativo del dialogo; fallback con script quando necessario |
| `details name` | Gruppi esclusivi; pannelli comprensibili anche se indipendenti |
| `selectedcontent` e select personalizzabili | Nuovo modello di contenuto e selezione; preserva un select funzionale |
| `headingoffset`, `headingreset` | Livelli calcolati dei titoli; verifica browser e tecnologie assistive |
| Attributi Shadow DOM recenti | Clonazione, serializzazione, registry, assegnazione degli slot |
| `alpha`, `colorspace` e funzioni media recenti | Differenze fra valore serializzato e controllo disponibile |

```html
<!-- Variante avanzata: verificare supporto e modello di contenuto -->
<select name="corso" aria-label="Corso">
  <button type="button"><selectedcontent></selectedcontent></button>
  <option value="html">HTML</option>
  <option value="css">CSS</option>
</select>
```

`selectedcontent` rappresenta il contenuto dell'opzione scelta nel nuovo select personalizzabile. La presentazione richiede anche CSS appropriato, per esempio il meccanismo `base-select` dove disponibile. Questo frammento è un approfondimento: il select classico con label visibile resta il punto di partenza. Funzioni documentate da un browser ma assenti dallo snapshot dell'indice WHATWG, come proposte di nuovi elementi per permessi, non entrano nel conteggio HTML standard.

## Riconoscere i vecchi elementi

| Elementi storici | Come affrontarli |
| --- | --- |
| `acronym` | Usa `abbr` |
| `bgsound` | Usa `audio` con controllo dell'utente |
| `dir`, `isindex` | Liste o form moderni secondo il significato |
| `frame`, `frameset`, `noframes` | Ripensa layout e navigazione; iframe solo quando serve un documento incorporato |
| `listing`, `xmp`, `plaintext` | `pre`/`code` con escaping o risposta `text/plain` |
| `strike` | `s` per informazione superata, `del` per revisione |
| `rb`, `rtc` | Modello moderno di ruby |
| `param`, `noembed`, `applet` | Risorse e fallback moderni; non ripristinare plugin storici |
| `basefont`, `big`, `blink`, `center`, `font`, `marquee`, `multicol`, `nobr`, `spacer`, `tt` | Semantica pertinente e CSS, evitando effetti distraenti |
| `keygen`, `menuitem`, `nextid` | Rivaluta la funzione e usa API o strutture moderne pertinenti |

Anche attributi come `align`, `bgcolor` e `cellpadding` appartengono al codice storico. La specifica distingue inoltre casi **obsoleti ma conformi**, ammessi con condizioni e avvisi: non confonderli con gli attributi conformi dell'inventario principale.

## Esercizio e verifica

Riscrivi `<center><font color="green">Titolo</font></center>` e spiega perché una pagina che «si vede bene» può essere non conforme.

::: details Soluzione
Se è un titolo usa `h1` o un livello pertinente e una classe CSS per colore/allineamento. Il parser può tollerare vecchio markup; il validatore verifica requisiti differenti dalla sola resa visiva.
:::

Fonti: [WHATWG · Obsoleto](https://html.spec.whatwg.org/multipage/obsolete.html), [MDN · selectedcontent](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/selectedcontent), [MDN · headingoffset](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/headingoffset), [web.dev · Baseline](https://web.dev/baseline).
