# 18 · Attributi globali e collegamenti con le API

**Obiettivo:** capire gli attributi riutilizzabili su elementi diversi e i loro limiti.

## Identità, lingua e dati

`id` deve identificare un elemento univocamente nel documento; `class` è una lista di token condivisibili. `title` aggiunge informazioni consultive, ma un tooltip non sostituisce una label o istruzioni visibili. `style` contiene dichiarazioni CSS. `lang`, `dir` e `translate` descrivono lingua, direzione e trattamento nella traduzione.

```html
<article id="corso-html" class="corso disponibile" data-corso-id="html-01">
  <h2>Laboratorio HTML</h2>
  <p lang="en">Learn by building.</p>
</article>
```

`data-*` è una famiglia aperta per dati dell'applicazione. In JavaScript `data-corso-id` si legge come `dataset.corsoId`; il valore è una stringa. Non usarla al posto della semantica né per conservare segreti.

## Modificabilità e suggerimenti

`contenteditable` può rendere una regione modificabile; `plaintext-only` limita il testo incollato dove supportato. Non la trasforma in un campo che viene inviato automaticamente con il form. `spellcheck`, `autocapitalize`, `autocorrect` e `writingsuggestions` influenzano assistenza e inserimento del testo. La risposta dipende da browser, sistema e tipo di controllo. Non sono vincoli di validazione.

```html
<label for="codice">Codice del corso</label>
<input id="codice" name="codice" type="text" autocapitalize="characters"
       spellcheck="false" enterkeyhint="next">
```

`inputmode` suggerisce il tipo di tastiera virtuale; `enterkeyhint` la funzione del tasto di conferma. L'utente può comunque inserire altri caratteri.

## Visibilità e interazione

`hidden` nasconde contenuto non pertinente; `hidden="until-found"` consente meccanismi di ricerca/rivelazione nei browser che lo supportano. `inert` rende un sottoalbero non interattivo e lo esclude dai normali percorsi di focus e accessibilità, senza nasconderlo necessariamente alla vista. Non usarli per simulare autorizzazioni.

`tabindex`, `autofocus` e `accesskey` riguardano il focus: consulta la [lezione dedicata](/html/accessibilita-focus). `draggable="true"` rende un elemento trascinabile, ma servono eventi JavaScript e un'alternativa da tastiera per una funzione completa. `popover` richiede un'azione per mostrare il contenuto.

## Altre famiglie

`itemscope`, `itemtype`, `itemprop`, `itemid`, `itemref` costruiscono [microdati](/html/microdati-seo). `slot`, `is`, `part` ed `exportparts` riguardano componenti e Shadow DOM: questi ultimi provengono dalle specifiche correlate, non tutti dall'indice HTML. `nonce` collabora con la Content Security Policy configurata sul server. `role` e `aria-*` sono definiti da ARIA e soggetti ai vincoli del singolo elemento.

Gli attributi `on*` contengono codice per eventi. Li cataloghiamo nel [riferimento](/html/riferimento-attributi), ma negli esercizi nuovi preferiamo `addEventListener` in un file JavaScript. La presenza di `onclick` non rende accessibile un `div` come pulsante. Le proprietà DOM possono riflettere attributi con conversioni: `checked` iniziale e stato corrente del controllo non sono sempre la stessa cosa.

## Esercizio e verifica

Aggiungi un identificatore dati e una frase inglese all'articolo. Rendi non modificabile un campo, senza usare `hidden`.

::: details Soluzione
Usa `data-corso-id`, `lang="en"` sulla frase e, per un campo testuale da inviare, `readonly`. `disabled` sarebbe una scelta diversa perché normalmente esclude il campo dall'invio. `hidden` non controlla la modificabilità.
:::

Fonti: [MDN · Attributi globali](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes), [MDN · hidden](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/hidden), [MDN · inert](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/inert).
