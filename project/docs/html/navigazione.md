# 11 · Sezioni, liste e navigazione

**Obiettivo:** costruire un documento navigabile e dare un nome chiaro alle sue regioni.

## Una struttura che si può leggere

```html
<a href="#contenuto">Vai al contenuto</a>
<header><h1>Laboratori Learning</h1></header>
<nav aria-label="Principale">
  <ul>
    <li><a href="index.html" aria-current="page">Home</a></li>
    <li><a href="calendario.html">Calendario</a></li>
  </ul>
</nav>
<main id="contenuto">
  <section aria-labelledby="titolo-html">
    <h2 id="titolo-html">Laboratori HTML</h2>
    <article><h3>Form accessibili</h3><p>Un incontro pratico.</p></article>
  </section>
</main>
<footer><address>Contatti: <a href="mailto:info@example.org">info@example.org</a></address></footer>
```

`main` rappresenta il contenuto dominante; normalmente c'è un solo `main` visibile. `article` è una composizione autonoma, `section` raggruppa un tema e `aside` materiale laterale. Non avvolgere ogni contenitore in `section`: quando manca un significato specifico usa `div`. `header` e `footer` possono riferirsi alla pagina o alla sezione che li contiene. `address` raccoglie contatti pertinenti, non qualunque indirizzo postale.

`hgroup` raggruppa un titolo con sottotitoli o altri paragrafi correlati. Non crea una gerarchia magica: scegli `h1`–`h6` in base alla struttura. Non affidarti a un presunto outline automatico delle `section`. Gli attributi più recenti `headingoffset` e `headingreset` sono nel riferimento, ma richiedono verifica del supporto: la sequenza esplicita dei titoli resta la base del corso.

## Liste e ricerca

`ul` è una lista senza ordine significativo; `ol` ha ordine e può usare `start`, `reversed` e `type`. `li value` modifica un numero in una lista ordinata. `menu` rappresenta una lista di comandi con `li`: non è un componente menu a tendina completo. `dl` contiene associazioni e non usa `li`.

```html
<ol start="3"><li>Scrivi HTML</li><li value="7">Verifica il risultato</li></ol>
<search>
  <form action="/ricerca" method="get">
    <label for="q">Cerca un laboratorio</label>
    <input id="q" name="q" type="search">
    <button type="submit">Cerca</button>
  </form>
</search>
```

`search` identifica un'area di ricerca o filtro. L'endpoint dell'esempio va implementato nel backend.

## Link con intenzione chiara

Un link con `href` naviga; un `button` esegue un'azione. Un link senza `href` non offre la stessa navigazione e gestione del focus. Usa testo comprensibile fuori contesto, frammenti verso ID unici, `mailto:` o `tel:` quando appropriato. `download` è un suggerimento soggetto a restrizioni di origine e alle risposte del server.

`target="_blank"` può aprire un altro contesto. Avvisa se il cambiamento non è atteso; `rel="noopener"` rende esplicito l'isolamento, `noreferrer` sopprime anche il referrer. `hreflang` e `type` descrivono la destinazione, senza tradurla o imporre il suo MIME. `ping` può inviare notifiche di navigazione: conoscerlo non significa doverlo usare.

## Esercizio e verifica

Aggiungi una seconda navigazione per il piè di pagina e una lista numerata che parta da 5. Naviga con Tab e prova il link «Vai al contenuto».

::: details Soluzione
Usa `nav aria-label="Nel piè di pagina"`, distinto da «Principale», e `ol start="5"`. Il collegamento iniziale deve puntare all'ID del `main`, senza ID duplicati. Verifica il comportamento del focus nel browser utilizzato.
:::

Fonti: [Google/web.dev · Navigazione](https://web.dev/learn/html/navigation), [Google/web.dev · Liste](https://web.dev/learn/html/lists), [WAI · Struttura](https://www.w3.org/WAI/tutorials/page-structure/).
