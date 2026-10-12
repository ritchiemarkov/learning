# 08 · Sintassi, categorie e DOM

**Obiettivo:** distinguere un documento valido da uno che il browser riesce soltanto a visualizzare.

## Dal file all'albero

Il server invia byte e un tipo MIME, normalmente `text/html`. Il browser decodifica i byte, riconosce i token e costruisce il DOM. Il DOM contiene elementi, attributi, testo e commenti: non è la fotografia esatta del file sorgente. Il parser può chiudere un paragrafo prima del previsto o inserire un `tbody`.

```html
<!-- Esempio volutamente errato -->
<p>Prima <div>Seconda</div> terza</p>
```

Un `p` ammette contenuto *phrasing*, non un `div`. Guarda prima «Visualizza sorgente», poi il pannello Elements: il browser ripara la struttura. Riparazione e conformità sono due cose diverse.

## Le categorie di contenuto

| Categoria | A cosa serve | Esempi |
| --- | --- | --- |
| Metadata | Descrivere documento e risorse | `meta`, `link`, `title` |
| Flow | Comporre il contenuto della pagina | `div`, `p`, `section` |
| Sectioning | Definire sezioni | `article`, `aside`, `nav`, `section` |
| Heading | Intitolare sezioni | `h1`–`h6` |
| Phrasing | Comporre testo e contenuti nella frase | `em`, `span`, `img` |
| Embedded | Integrare altre risorse | `iframe`, `video` |
| Interactive | Consentire interazione | `button`, `a` con `href` |

Un elemento può appartenere a più categorie. *Palpable* riguarda il contenuto percepibile; *script-supporting* comprende `script` e `template`. I controlli hanno inoltre categorie come *labelable* e *submittable*. «Block» e «inline» descrivono il layout CSS, non sostituiscono questi vincoli.

Un modello *transparent*, come quello di alcuni link, dipende dal contesto del genitore. Un link non può comunque contenere un altro link o altri controlli interattivi vietati dal suo modello. Un `button` non contiene un altro pulsante.

## Regole da riconoscere

Gli elementi void, come `img`, `input` e `br`, non hanno contenuto né tag di chiusura. In HTML la barra di `<img />` non crea un meccanismo di chiusura XML; `<div />` non chiude un `div`. Scrivi attributi fra virgolette e chiusure esplicite, anche quando alcune omissioni sono ammesse.

Gli attributi booleani dipendono dalla presenza: `disabled="false"` disabilita. Gli enumerati, come `contenteditable`, interpretano valori specifici. Numeri, date, liste di token e URL hanno grammatiche proprie. Per testo letterale usa `&lt;`, `&amp;`, `&quot;`; non inserire codice utente come markup.

`<!doctype html>` attiva il rendering standard. Un doctype storico o assente può attivare quirks mode. HTML servito come `application/xhtml+xml` usa il parser XML: nomi sensibili alle maiuscole, struttura ben formata e namespace; gli errori non ricevono le stesse riparazioni. SVG e MathML dentro HTML seguono regole di contenuto straniero.

## Esercizio e verifica

Correggi l'esempio iniziale, aggiungi un testo che mostri letteralmente `<button>` e spiega perché `required="false"` non disattiva un vincolo.

::: details Soluzione
```html
<p>Prima</p>
<div>Seconda</div>
<p>Terza: &lt;button&gt;</p>
```
Per disattivare `required` rimuovi l'attributo. Controlla il risultato con un validatore e confronta sorgente e DOM.
:::

Fonti: [MDN · Categorie](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories), [WHATWG · Sintassi](https://html.spec.whatwg.org/multipage/syntax.html), [WHATWG · Parsing](https://html.spec.whatwg.org/multipage/parsing.html).
