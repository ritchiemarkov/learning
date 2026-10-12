# Riferimento: attributi e gestori di eventi

Lo snapshot contiene **144 nomi di attributi**, descritti in **180 righe di contesto**, più **89 attributi gestori di eventi**. Un nome come `type` cambia significato fra elementi: non basta memorizzare il nome.

Le colonne di valori sono un indice della grammatica ufficiale, non tutte le sue condizioni. Le parole tecniche e i valori sono conservati dalla fonte; apri la definizione per default, errori, intervalli ed eccezioni. Gli asterischi rinviano alle condizioni della specifica. [Copertura e confini](/html/copertura).

## Attributi globali nell’indice HTML

| Nome e definizione | Dove | Significato | Valori / grammatica | Lezione |
| --- | --- | --- | --- | --- |
| [`accesskey`](https://html.spec.whatwg.org/multipage/interaction.html#the-accesskey-attribute) | HTML elements | Suggerimento per una scorciatoia di attivazione o focus | Ordered set of unique space-separated tokens , none of which are identical to another, each consisting of one code point in length | [Studia](/html/accessibilita-focus) |
| [`autocapitalize`](https://html.spec.whatwg.org/multipage/interaction.html#attr-autocapitalize) | HTML elements | Suggerimento di capitalizzazione del testo | " on "; " off "; " none "; " sentences "; " words "; " characters " | [Studia](/html/attributi-globali) |
| [`autocorrect`](https://html.spec.whatwg.org/multipage/interaction.html#attr-autocorrect) | HTML elements | Suggerimento di correzione automatica | " on "; " off "; the empty string | [Studia](/html/attributi-globali) |
| [`autofocus`](https://html.spec.whatwg.org/multipage/interaction.html#attr-fe-autofocus) | HTML elements | Focus automatico all’apertura o caricamento | Boolean attribute | [Studia](/html/accessibilita-focus) |
| [`class`](https://html.spec.whatwg.org/multipage/dom.html#classes) | HTML elements | Lista di classi per selezione e stile | Set of space-separated tokens | [Studia](/html/attributi-globali) |
| [`contenteditable`](https://html.spec.whatwg.org/multipage/interaction.html#attr-contenteditable) | HTML elements | Modificabilità della regione testuale | " true "; " false "; " plaintext-only "; the empty string | [Studia](/html/attributi-globali) |
| [`dir`](https://html.spec.whatwg.org/multipage/dom.html#attr-dir) | HTML elements | Direzione di base del testo | " ltr "; " rtl "; " auto " | [Studia](/html/internazionalizzazione) |
| [`draggable`](https://html.spec.whatwg.org/multipage/dnd.html#attr-draggable) | HTML elements | Abilitazione del trascinamento, non comportamento completo | " true "; " false " | [Studia](/html/attributi-globali) |
| [`enterkeyhint`](https://html.spec.whatwg.org/multipage/interaction.html#attr-enterkeyhint) | HTML elements | Azione suggerita del tasto Invio virtuale | " enter "; " done "; " go "; " next "; " previous "; " search "; " send " | [Studia](/html/attributi-globali) |
| [`headingoffset`](https://html.spec.whatwg.org/multipage/interaction.html#attr-tabindex) | HTML elements | Incremento del livello calcolato dei titoli | Valid non-negative integer between 0 and 8 | [Studia](/html/compatibilita) |
| [`headingreset`](https://html.spec.whatwg.org/multipage/interaction.html#attr-tabindex) | HTML elements | Interruzione dell’accumulo degli offset dei titoli | Boolean attribute | [Studia](/html/compatibilita) |
| [`hidden`](https://html.spec.whatwg.org/multipage/interaction.html#attr-hidden) | HTML elements | Contenuto nascosto, anche rivelabile con until-found | " until-found "; " hidden "; the empty string | [Studia](/html/attributi-globali) |
| [`id`](https://html.spec.whatwg.org/multipage/dom.html#the-id-attribute) | HTML elements | Identificatore univoco dell’elemento | Text * | [Studia](/html/attributi-globali) |
| [`inert`](https://html.spec.whatwg.org/multipage/interaction.html#the-inert-attribute) | HTML elements | Sottoalbero non interattivo e fuori dai normali percorsi accessibili | Boolean attribute | [Studia](/html/accessibilita-focus) |
| [`inputmode`](https://html.spec.whatwg.org/multipage/interaction.html#attr-inputmode) | HTML elements | Tipo di tastiera virtuale suggerito | " none "; " text "; " tel "; " email "; " url "; " numeric "; " decimal "; " search " | [Studia](/html/attributi-globali) |
| [`is`](https://html.spec.whatwg.org/multipage/custom-elements.html#attr-is) | HTML elements | Nome di un elemento built-in personalizzato | Valid custom element name of a defined customized built-in element | [Studia](/html/script-template) |
| [`itemid`](https://html.spec.whatwg.org/multipage/microdata.html#attr-itemid) | HTML elements | Identificatore globale dell’item | Valid URL potentially surrounded by spaces | [Studia](/html/microdati-seo) |
| [`itemprop`](https://html.spec.whatwg.org/multipage/microdata.html#names:-the-itemprop-attribute) | HTML elements | Proprietà del vocabolario dei microdati | Unordered set of unique space-separated tokens consisting of valid absolute URLs , defined property names , or text* | [Studia](/html/microdati-seo) |
| [`itemref`](https://html.spec.whatwg.org/multipage/microdata.html#attr-itemref) | HTML elements | ID esterni con proprietà dell’item | Unordered set of unique space-separated tokens consisting of IDs* | [Studia](/html/microdati-seo) |
| [`itemscope`](https://html.spec.whatwg.org/multipage/microdata.html#attr-itemscope) | HTML elements | Creazione di un item di microdati | Boolean attribute | [Studia](/html/microdati-seo) |
| [`itemtype`](https://html.spec.whatwg.org/multipage/microdata.html#attr-itemtype) | HTML elements | URL dei tipi del vocabolario dell’item | Unordered set of unique space-separated tokens consisting of valid absolute URLs * | [Studia](/html/microdati-seo) |
| [`lang`](https://html.spec.whatwg.org/multipage/dom.html#attr-lang) | HTML elements | Lingua del contenuto secondo BCP 47 | Valid BCP 47 language tag or the empty string | [Studia](/html/internazionalizzazione) |
| [`nonce`](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#attr-nonce) | HTML elements | Token che collabora con la Content Security Policy | Text | [Studia](/html/sicurezza-prestazioni) |
| [`popover`](https://html.spec.whatwg.org/multipage/popover.html#attr-popover) | HTML elements | Tipo di popover del contenuto | " auto "; " manual "; " hint "; the empty string | [Studia](/html/interazioni-native) |
| [`slot`](https://html.spec.whatwg.org/multipage/dom.html#the-id-attribute) | HTML elements | Slot nominato cui assegnare il nodo | Text | [Studia](/html/script-template) |
| [`spellcheck`](https://html.spec.whatwg.org/multipage/interaction.html#attr-spellcheck) | HTML elements | Suggerimento di controllo ortografico | " true "; " false "; the empty string | [Studia](/html/attributi-globali) |
| [`style`](https://html.spec.whatwg.org/multipage/dom.html#attr-style) | HTML elements | Dichiarazioni CSS inline | CSS declarations* | [Studia](/html/attributi-globali) |
| [`tabindex`](https://html.spec.whatwg.org/multipage/interaction.html#attr-tabindex) | HTML elements | Partecipazione al focus programmatico e sequenziale | Valid integer | [Studia](/html/accessibilita-focus) |
| [`title`](https://html.spec.whatwg.org/multipage/dom.html#attr-title) | HTML elements | Informazioni consultive, non sostituto di nome o label | Text | [Studia](/html/attributi-globali) |
| [`translate`](https://html.spec.whatwg.org/multipage/dom.html#attr-translate) | HTML elements | Suggerimento sul trattamento nella traduzione | " yes "; " no "; the empty string | [Studia](/html/internazionalizzazione) |
| [`writingsuggestions`](https://html.spec.whatwg.org/multipage/interaction.html#attr-writingsuggestions) | HTML elements | Suggerimento di assistenza alla scrittura | " true "; " false "; the empty string | [Studia](/html/attributi-globali) |

## Attributi nei contesti specifici

| Nome e definizione | Dove | Significato | Valori / grammatica | Lezione |
| --- | --- | --- | --- | --- |
| [`abbr`](https://html.spec.whatwg.org/multipage/tables.html#attr-th-abbr) | th | Etichetta alternativa breve di un’intestazione | Text * | [Studia](/html/tabelle) |
| [`accept`](https://html.spec.whatwg.org/multipage/input.html#attr-input-accept) | input | Suggerimento per i tipi di file selezionabili | Set of comma-separated tokens * consisting of valid MIME type strings with no parameters or audio/* , video/* , or image/* | [Studia](/html/invio-validazione) |
| [`accept-charset`](https://html.spec.whatwg.org/multipage/forms.html#attr-form-accept-charset) | form | Codifica dei dati del form: UTF-8 | ASCII case-insensitive match for " UTF-8 " | [Studia](/html/invio-validazione) |
| [`action`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fs-action) | form | Destinazione dell’invio del form | Valid non-empty URL potentially surrounded by spaces | [Studia](/html/invio-validazione) |
| [`allow`](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#attr-iframe-allow) | iframe | Permissions Policy del frame | Serialized permissions policy | [Studia](/html/contenuti-incorporati) |
| [`allowfullscreen`](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#attr-iframe-allowfullscreen) | iframe | Abilitazione fullscreen del frame | Boolean attribute | [Studia](/html/contenuti-incorporati) |
| [`alpha`](https://html.spec.whatwg.org/multipage/input.html#attr-input-alpha) | input | Componente alpha del controllo colore | Boolean attribute | [Studia](/html/compatibilita) |
| [`alt`](https://html.spec.whatwg.org/multipage/image-maps.html#attr-area-alt) | area ; img ; input | Alternativa testuale dell’immagine o del controllo grafico | Text * | [Studia](/html/immagini-responsive) |
| [`as`](https://html.spec.whatwg.org/multipage/semantics.html#attr-link-as) | link | Destinazione della richiesta anticipata da link | Preload destination , for rel =" preload "; module preload destination , for rel =" modulepreload " | [Studia](/html/sicurezza-prestazioni) |
| [`async`](https://html.spec.whatwg.org/multipage/scripting.html#attr-script-async) | script | Esecuzione dello script quando disponibile | Boolean attribute | [Studia](/html/script-template) |
| [`autocomplete`](https://html.spec.whatwg.org/multipage/forms.html#attr-form-autocomplete) | form | Autocompletamento del form o del controllo | " on "; " off " | [Studia](/html/invio-validazione) |
| [`autocomplete`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fe-autocomplete) | input ; select ; textarea | Autocompletamento del form o del controllo | Autofill field name and related tokens* | [Studia](/html/invio-validazione) |
| [`autoplay`](https://html.spec.whatwg.org/multipage/media.html#attr-media-autoplay) | audio ; video | Suggerimento di riproduzione automatica, soggetto a policy | Boolean attribute | [Studia](/html/audio-video) |
| [`blocking`](https://html.spec.whatwg.org/multipage/semantics.html#attr-link-blocking) | link ; script ; style | Comportamento di blocco del rendering dove previsto | Unordered set of unique space-separated tokens * | [Studia](/html/sicurezza-prestazioni) |
| [`charset`](https://html.spec.whatwg.org/multipage/semantics.html#attr-meta-charset) | meta | Dichiarazione della codifica UTF-8 | " utf-8 " | [Studia](/html/metadati) |
| [`checked`](https://html.spec.whatwg.org/multipage/input.html#attr-input-checked) | input | Selezione iniziale di checkbox o radio | Boolean attribute | [Studia](/html/controlli-form) |
| [`cite`](https://html.spec.whatwg.org/multipage/grouping-content.html#attr-blockquote-cite) | blockquote ; del ; ins ; q | URL della fonte di una citazione o modifica | Valid URL potentially surrounded by spaces | [Studia](/html/testo-avanzato) |
| [`closedby`](https://html.spec.whatwg.org/multipage/interactive-elements.html#attr-dialog-closedby) | dialog | Azioni dell’utente che possono chiudere un dialogo | " any "; " closerequest "; " none "; | [Studia](/html/interazioni-native) |
| [`color`](https://html.spec.whatwg.org/multipage/semantics.html#attr-link-color) | link | Colore per specifici tipi di icona link | CSS &lt;color&gt; | [Studia](/html/metadati) |
| [`colorspace`](https://html.spec.whatwg.org/multipage/input.html#attr-input-colorspace) | input | Spazio colore del valore serializzato | " limited-srgb "; " display-p3 " | [Studia](/html/compatibilita) |
| [`cols`](https://html.spec.whatwg.org/multipage/form-elements.html#attr-textarea-cols) | textarea | Larghezza indicativa del controllo textarea in caratteri | Valid non-negative integer greater than zero | [Studia](/html/controlli-form) |
| [`colspan`](https://html.spec.whatwg.org/multipage/tables.html#attr-tdth-colspan) | td ; th | Numero di colonne occupate da una cella | Valid non-negative integer greater than zero | [Studia](/html/tabelle) |
| [`command`](https://html.spec.whatwg.org/multipage/form-elements.html#attr-button-command) | button | Azione invocata sul bersaglio del pulsante | " toggle-popover "; " show-popover "; " hide-popover "; " close "; " request-close "; " show-modal "; a custom command keyword | [Studia](/html/interazioni-native) |
| [`commandfor`](https://html.spec.whatwg.org/multipage/form-elements.html#attr-button-commandfor) | button | ID del bersaglio del comando | ID * | [Studia](/html/interazioni-native) |
| [`content`](https://html.spec.whatwg.org/multipage/semantics.html#attr-meta-content) | meta | Valore del metadato | Text * | [Studia](/html/metadati) |
| [`controls`](https://html.spec.whatwg.org/multipage/media.html#attr-media-controls) | audio ; video img ; | Controlli dell’utente per media; contesti recenti da verificare | Boolean attribute | [Studia](/html/audio-video) |
| [`coords`](https://html.spec.whatwg.org/multipage/image-maps.html#attr-area-coords) | area | Coordinate della regione di una mappa | Valid list of floating-point numbers * | [Studia](/html/immagini-responsive) |
| [`crossorigin`](https://html.spec.whatwg.org/multipage/media.html#attr-media-crossorigin) | audio ; img ; link ; script ; video | Modalità CORS della richiesta | " anonymous "; " use-credentials "; the empty string | [Studia](/html/sicurezza-prestazioni) |
| [`data`](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#attr-object-data) | object | URL della risorsa di object | Valid non-empty URL potentially surrounded by spaces | [Studia](/html/contenuti-incorporati) |
| [`datetime`](https://html.spec.whatwg.org/multipage/edits.html#attr-mod-datetime) | del ; ins | Data/tempo macchina o data di una modifica | Valid date string with optional time | [Studia](/html/testo-avanzato) |
| [`datetime`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#attr-time-datetime) | time | Data/tempo macchina o data di una modifica | Valid month string , valid date string , valid yearless date string , valid time string , valid local date and time string , valid time-zone offset string , valid global date and time string , valid week string , valid non-negative integer , or valid duration string | [Studia](/html/testo-avanzato) |
| [`decoding`](https://html.spec.whatwg.org/multipage/embedded-content.html#attr-img-decoding) | img | Suggerimento per la decodifica dell’immagine | " sync "; " async "; " auto " | [Studia](/html/immagini-responsive) |
| [`default`](https://html.spec.whatwg.org/multipage/media.html#attr-track-default) | track | Traccia testuale suggerita come iniziale | Boolean attribute | [Studia](/html/audio-video) |
| [`defer`](https://html.spec.whatwg.org/multipage/scripting.html#attr-script-defer) | script | Esecuzione differita dello script classico esterno | Boolean attribute | [Studia](/html/script-template) |
| [`dir`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-bdo-element) | bdo | Direzione di base del testo | " ltr "; " rtl " | [Studia](/html/internazionalizzazione) |
| [`dirname`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fe-dirname) | input ; textarea | Nome della voce aggiuntiva che invia la direzione del testo | Text * | [Studia](/html/internazionalizzazione) |
| [`disabled`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fe-disabled) | button ; input ; optgroup ; option ; select ; textarea ; form-associated custom elements | Disabilitazione del controllo, gruppo o risorsa dove applicabile | Boolean attribute | [Studia](/html/invio-validazione) |
| [`disabled`](https://html.spec.whatwg.org/multipage/form-elements.html#attr-fieldset-disabled) | fieldset | Disabilitazione del controllo, gruppo o risorsa dove applicabile | Boolean attribute | [Studia](/html/invio-validazione) |
| [`disabled`](https://html.spec.whatwg.org/multipage/semantics.html#attr-link-disabled) | link | Disabilitazione del controllo, gruppo o risorsa dove applicabile | Boolean attribute | [Studia](/html/invio-validazione) |
| [`download`](https://html.spec.whatwg.org/multipage/links.html#attr-hyperlink-download) | a ; area | Suggerimento di download e nome del file | Text | [Studia](/html/navigazione) |
| [`enctype`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fs-enctype) | form | Codifica dei dati inviati dal form | " application/x-www-form-urlencoded "; " multipart/form-data "; " text/plain " | [Studia](/html/invio-validazione) |
| [`fetchpriority`](https://html.spec.whatwg.org/multipage/embedded-content.html#attr-img-fetchpriority) | img ; link ; script | Priorità suggerita della richiesta | " auto "; " high "; " low " | [Studia](/html/sicurezza-prestazioni) |
| [`for`](https://html.spec.whatwg.org/multipage/forms.html#attr-label-for) | label | ID del controllo etichettato o lista di dipendenze di output | ID * | [Studia](/html/controlli-form) |
| [`for`](https://html.spec.whatwg.org/multipage/form-elements.html#attr-output-for) | output | ID del controllo etichettato o lista di dipendenze di output | Unordered set of unique space-separated tokens consisting of IDs* | [Studia](/html/controlli-form) |
| [`for`](https://html.spec.whatwg.org/multipage/scripting.html#attr-template-for) | template | ID del controllo etichettato o lista di dipendenze di output | Text | [Studia](/html/controlli-form) |
| [`form`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fae-form) | button ; fieldset ; input ; object ; output ; select ; textarea ; form-associated custom elements | ID del form proprietario del controllo | ID * | [Studia](/html/invio-validazione) |
| [`formaction`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fs-formaction) | button ; input | Sovrascrittura della destinazione da parte del submitter | Valid non-empty URL potentially surrounded by spaces | [Studia](/html/invio-validazione) |
| [`formenctype`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fs-formenctype) | button ; input | Sovrascrittura della codifica da parte del submitter | " application/x-www-form-urlencoded "; " multipart/form-data "; " text/plain " | [Studia](/html/invio-validazione) |
| [`formmethod`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fs-formmethod) | button ; input | Sovrascrittura del metodo da parte del submitter | " get "; " post "; " dialog " | [Studia](/html/invio-validazione) |
| [`formnovalidate`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fs-formnovalidate) | button ; input | Invio dal submitter senza validazione interattiva | Boolean attribute | [Studia](/html/invio-validazione) |
| [`formtarget`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fs-formtarget) | button ; input | Sovrascrittura del contesto di risposta dal submitter | Valid navigable target name or keyword | [Studia](/html/invio-validazione) |
| [`headers`](https://html.spec.whatwg.org/multipage/tables.html#attr-tdth-headers) | td ; th | ID delle intestazioni associate alla cella | Unordered set of unique space-separated tokens consisting of IDs* | [Studia](/html/tabelle) |
| [`height`](https://html.spec.whatwg.org/multipage/canvas.html#attr-canvas-height) | canvas ; embed ; iframe ; img ; input ; object ; source (in picture ); video | Dimensione verticale, con regole proprie dell’elemento | Valid non-negative integer | [Studia](/html/contenuti-incorporati) |
| [`high`](https://html.spec.whatwg.org/multipage/form-elements.html#attr-meter-high) | meter | Soglia alta della misura meter | Valid floating-point number * | [Studia](/html/controlli-form) |
| [`href`](https://html.spec.whatwg.org/multipage/links.html#attr-hyperlink-href) | a ; area | URL della destinazione o risorsa collegata | Valid URL potentially surrounded by spaces | [Studia](/html/navigazione) |
| [`href`](https://html.spec.whatwg.org/multipage/semantics.html#attr-link-href) | link | URL della destinazione o risorsa collegata | Valid non-empty URL potentially surrounded by spaces | [Studia](/html/navigazione) |
| [`href`](https://html.spec.whatwg.org/multipage/semantics.html#attr-base-href) | base | URL della destinazione o risorsa collegata | Valid URL potentially surrounded by spaces | [Studia](/html/navigazione) |
| [`hreflang`](https://html.spec.whatwg.org/multipage/links.html#attr-hyperlink-hreflang) | a ; link | Lingua dichiarata della destinazione | Valid BCP 47 language tag | [Studia](/html/navigazione) |
| [`http-equiv`](https://html.spec.whatwg.org/multipage/semantics.html#attr-meta-http-equiv) | meta | Direttiva pragma prevista per meta | " content-type "; " default-style "; " refresh "; " x-ua-compatible "; " content-security-policy " | [Studia](/html/metadati) |
| [`imagesizes`](https://html.spec.whatwg.org/multipage/semantics.html#attr-link-imagesizes) | link | Dimensione prevista dell’immagine anticipata da link | Valid source size list | [Studia](/html/immagini-responsive) |
| [`imagesrcset`](https://html.spec.whatwg.org/multipage/semantics.html#attr-link-imagesrcset) | link | Candidati responsive dell’immagine anticipata da link | Comma-separated list of image candidate strings | [Studia](/html/immagini-responsive) |
| [`integrity`](https://html.spec.whatwg.org/multipage/semantics.html#attr-link-integrity) | link ; script | Metadato crittografico di integrità della risorsa | Text | [Studia](/html/sicurezza-prestazioni) |
| [`ismap`](https://html.spec.whatwg.org/multipage/embedded-content.html#attr-img-ismap) | img | Mappa dell’immagine gestita dal server | Boolean attribute | [Studia](/html/immagini-responsive) |
| [`kind`](https://html.spec.whatwg.org/multipage/media.html#attr-track-kind) | track | Tipo di traccia temporizzata | " subtitles "; " captions "; " descriptions "; " chapters "; " metadata " | [Studia](/html/audio-video) |
| [`label`](https://html.spec.whatwg.org/multipage/form-elements.html#attr-optgroup-label) | optgroup ; option ; track | Etichetta dell’opzione o gruppo; nome della traccia media | Text | [Studia](/html/controlli-form) |
| [`list`](https://html.spec.whatwg.org/multipage/input.html#attr-input-list) | input | ID del datalist di suggerimenti | ID * | [Studia](/html/controlli-form) |
| [`loading`](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#attr-iframe-loading) | iframe ; img ; audio ; video | Strategia di caricamento nei contesti previsti | " lazy "; " eager " | [Studia](/html/sicurezza-prestazioni) |
| [`loop`](https://html.spec.whatwg.org/multipage/media.html#attr-media-loop) | audio ; video | Ripetizione del media | Boolean attribute | [Studia](/html/audio-video) |
| [`low`](https://html.spec.whatwg.org/multipage/form-elements.html#attr-meter-low) | meter | Soglia bassa della misura meter | Valid floating-point number * | [Studia](/html/controlli-form) |
| [`max`](https://html.spec.whatwg.org/multipage/input.html#attr-input-max) | input | Massimo valore ammesso o massimo della misura | Varies* | [Studia](/html/invio-validazione) |
| [`max`](https://html.spec.whatwg.org/multipage/form-elements.html#attr-meter-max) | meter ; progress | Massimo valore ammesso o massimo della misura | Valid floating-point number * | [Studia](/html/invio-validazione) |
| [`maxlength`](https://html.spec.whatwg.org/multipage/input.html#attr-input-maxlength) | input ; textarea | Lunghezza massima del testo dove applicabile | Valid non-negative integer | [Studia](/html/invio-validazione) |
| [`media`](https://html.spec.whatwg.org/multipage/semantics.html#attr-link-media) | link ; meta ; source ; style | Condizione media di applicazione o scelta della risorsa | Valid media query list | [Studia](/html/metadati) |
| [`method`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fs-method) | form | Metodo di invio o chiusura del dialogo | " get "; " post "; " dialog " | [Studia](/html/invio-validazione) |
| [`min`](https://html.spec.whatwg.org/multipage/input.html#attr-input-min) | input | Minimo valore ammesso o minimo della misura | Varies* | [Studia](/html/invio-validazione) |
| [`min`](https://html.spec.whatwg.org/multipage/form-elements.html#attr-meter-min) | meter | Minimo valore ammesso o minimo della misura | Valid floating-point number * | [Studia](/html/invio-validazione) |
| [`minlength`](https://html.spec.whatwg.org/multipage/input.html#attr-input-minlength) | input ; textarea | Lunghezza minima del testo dove applicabile | Valid non-negative integer | [Studia](/html/invio-validazione) |
| [`multiple`](https://html.spec.whatwg.org/multipage/input.html#attr-input-multiple) | input ; select | Valori o selezioni multiple dove previste | Boolean attribute | [Studia](/html/controlli-form) |
| [`muted`](https://html.spec.whatwg.org/multipage/media.html#attr-media-muted) | audio ; video | Stato iniziale di silenziamento del media | Boolean attribute | [Studia](/html/audio-video) |
| [`name`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fe-name) | button ; fieldset ; input ; output ; select ; textarea ; form-associated custom elements | Nome del controllo, form, destinazione o gruppo secondo contesto | Text * | [Studia](/html/invio-validazione) |
| [`name`](https://html.spec.whatwg.org/multipage/interactive-elements.html#attr-details-name) | details | Nome del controllo, form, destinazione o gruppo secondo contesto | Text * | [Studia](/html/invio-validazione) |
| [`name`](https://html.spec.whatwg.org/multipage/forms.html#attr-form-name) | form | Nome del controllo, form, destinazione o gruppo secondo contesto | Text * | [Studia](/html/invio-validazione) |
| [`name`](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#attr-iframe-name) | iframe ; object | Nome del controllo, form, destinazione o gruppo secondo contesto | Valid navigable target name or keyword | [Studia](/html/invio-validazione) |
| [`name`](https://html.spec.whatwg.org/multipage/image-maps.html#attr-map-name) | map | Nome del controllo, form, destinazione o gruppo secondo contesto | Text * | [Studia](/html/invio-validazione) |
| [`name`](https://html.spec.whatwg.org/multipage/semantics.html#attr-meta-name) | meta | Nome del controllo, form, destinazione o gruppo secondo contesto | Text * | [Studia](/html/invio-validazione) |
| [`name`](https://html.spec.whatwg.org/multipage/scripting.html#attr-slot-name) | slot | Nome del controllo, form, destinazione o gruppo secondo contesto | Text | [Studia](/html/invio-validazione) |
| [`nomodule`](https://html.spec.whatwg.org/multipage/scripting.html#attr-script-nomodule) | script | Percorso script per browser senza supporto ai moduli | Boolean attribute | [Studia](/html/script-template) |
| [`novalidate`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fs-novalidate) | form | Form senza validazione interattiva all’invio | Boolean attribute | [Studia](/html/invio-validazione) |
| [`open`](https://html.spec.whatwg.org/multipage/interactive-elements.html#attr-details-open) | details | Stato aperto di details o dialog | Boolean attribute | [Studia](/html/interazioni-native) |
| [`open`](https://html.spec.whatwg.org/multipage/interactive-elements.html#attr-dialog-open) | dialog | Stato aperto di details o dialog | Boolean attribute | [Studia](/html/interazioni-native) |
| [`optimum`](https://html.spec.whatwg.org/multipage/form-elements.html#attr-meter-optimum) | meter | Valore ottimale della misura meter | Valid floating-point number * | [Studia](/html/controlli-form) |
| [`pattern`](https://html.spec.whatwg.org/multipage/input.html#attr-input-pattern) | input | Vincolo sull’intero valore testuale dove applicabile | Regular expression matching the JavaScript Pattern production | [Studia](/html/invio-validazione) |
| [`ping`](https://html.spec.whatwg.org/multipage/links.html#ping) | a ; area | URL notificati al seguito di un collegamento | Set of space-separated tokens consisting of valid non-empty URLs | [Studia](/html/navigazione) |
| [`placeholder`](https://html.spec.whatwg.org/multipage/input.html#attr-input-placeholder) | input ; textarea | Suggerimento di inserimento, non etichetta | Text * | [Studia](/html/controlli-form) |
| [`playsinline`](https://html.spec.whatwg.org/multipage/media.html#attr-video-playsinline) | video | Suggerimento di riproduzione video nel contesto della pagina | Boolean attribute | [Studia](/html/audio-video) |
| [`popovertarget`](https://html.spec.whatwg.org/multipage/popover.html#attr-popovertarget) | button ; input | ID del popover bersaglio | ID * | [Studia](/html/interazioni-native) |
| [`popovertargetaction`](https://html.spec.whatwg.org/multipage/popover.html#attr-popovertargetaction) | button ; input | Azione di apertura, chiusura o alternanza del popover | " toggle "; " show "; " hide " | [Studia](/html/interazioni-native) |
| [`poster`](https://html.spec.whatwg.org/multipage/media.html#attr-video-poster) | video | Immagine di anteprima del video | Valid non-empty URL potentially surrounded by spaces | [Studia](/html/audio-video) |
| [`preload`](https://html.spec.whatwg.org/multipage/media.html#attr-media-preload) | audio ; video | Quantità di precaricamento suggerita per il media | " none "; " metadata "; " auto "; the empty string | [Studia](/html/audio-video) |
| [`readonly`](https://html.spec.whatwg.org/multipage/input.html#attr-input-readonly) | input ; textarea | Controllo non modificabile ma normalmente inviabile | Boolean attribute | [Studia](/html/invio-validazione) |
| [`readonly`](https://html.spec.whatwg.org/multipage/custom-elements.html#attr-face-readonly) | form-associated custom elements | Controllo non modificabile ma normalmente inviabile | Boolean attribute | [Studia](/html/invio-validazione) |
| [`referrerpolicy`](https://html.spec.whatwg.org/multipage/links.html#attr-hyperlink-referrerpolicy) | a ; area ; iframe ; img ; link ; script | Policy delle informazioni di referrer della richiesta | Referrer policy | [Studia](/html/sicurezza-prestazioni) |
| [`rel`](https://html.spec.whatwg.org/multipage/links.html#attr-hyperlink-rel) | a ; area | Lista di relazioni o tipi di collegamento | Unordered set of unique space-separated tokens * | [Studia](/html/metadati) |
| [`rel`](https://html.spec.whatwg.org/multipage/semantics.html#attr-link-rel) | link | Lista di relazioni o tipi di collegamento | Unordered set of unique space-separated tokens * | [Studia](/html/metadati) |
| [`required`](https://html.spec.whatwg.org/multipage/input.html#attr-input-required) | input ; select ; textarea | Valore obbligatorio dove applicabile | Boolean attribute | [Studia](/html/invio-validazione) |
| [`reversed`](https://html.spec.whatwg.org/multipage/grouping-content.html#attr-ol-reversed) | ol | Numerazione discendente della lista ordinata | Boolean attribute | [Studia](/html/navigazione) |
| [`rows`](https://html.spec.whatwg.org/multipage/form-elements.html#attr-textarea-rows) | textarea | Altezza indicativa della textarea in righe | Valid non-negative integer greater than zero | [Studia](/html/controlli-form) |
| [`rowspan`](https://html.spec.whatwg.org/multipage/tables.html#attr-tdth-rowspan) | td ; th | Numero di righe occupate da una cella | Valid non-negative integer | [Studia](/html/tabelle) |
| [`sandbox`](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#attr-iframe-sandbox) | iframe | Restrizioni e capacità concesse al documento incorporato | Unordered set of unique space-separated tokens , ASCII case-insensitive , consisting of " allow-downloads " " allow-forms " " allow-modals " " allow-orientation-lock " " allow-pointer-lock " " allow-popups " " allow-popups-to-escape-sandbox " " allow-presentation " " allow-same-origin " " allow-scripts " " allow-top-navigation " " allow-top-navigation-by-user-activation " " allow-top-navigation-to-custom-protocols " | [Studia](/html/contenuti-incorporati) |
| [`scope`](https://html.spec.whatwg.org/multipage/tables.html#attr-th-scope) | th | Gruppo di celle cui si riferisce un’intestazione | " row "; " col "; " rowgroup "; " colgroup " | [Studia](/html/tabelle) |
| [`selected`](https://html.spec.whatwg.org/multipage/form-elements.html#attr-option-selected) | option | Selezione iniziale dell’opzione | Boolean attribute | [Studia](/html/controlli-form) |
| [`shadowrootclonable`](https://html.spec.whatwg.org/multipage/scripting.html#attr-template-shadowrootclonable) | template | Clonabilità dello Shadow DOM dichiarativo | Boolean attribute | [Studia](/html/script-template) |
| [`shadowrootcustomelementregistry`](https://html.spec.whatwg.org/multipage/scripting.html#attr-template-shadowrootcustomelementregistry) | template | Registro di custom elements dello Shadow DOM dichiarativo | Boolean attribute | [Studia](/html/script-template) |
| [`shadowrootdelegatesfocus`](https://html.spec.whatwg.org/multipage/scripting.html#attr-template-shadowrootdelegatesfocus) | template | Delega del focus nello Shadow DOM dichiarativo | Boolean attribute | [Studia](/html/script-template) |
| [`shadowrootmode`](https://html.spec.whatwg.org/multipage/scripting.html#attr-template-shadowrootmode) | template | Modalità open/closed della radice shadow dichiarativa | " open "; " closed " | [Studia](/html/script-template) |
| [`shadowrootserializable`](https://html.spec.whatwg.org/multipage/scripting.html#attr-template-shadowrootserializable) | template | Serializzabilità dello Shadow DOM dichiarativo | Boolean attribute | [Studia](/html/script-template) |
| [`shadowrootslotassignment`](https://html.spec.whatwg.org/multipage/scripting.html#attr-template-shadowrootslotassignment) | template | Modalità di assegnazione degli slot dichiarativi | " named "; " manual " | [Studia](/html/script-template) |
| [`shape`](https://html.spec.whatwg.org/multipage/image-maps.html#attr-area-shape) | area | Geometria della regione area | " circle "; " default "; " poly "; " rect " | [Studia](/html/immagini-responsive) |
| [`size`](https://html.spec.whatwg.org/multipage/input.html#attr-input-size) | input ; select | Dimensione indicativa del controllo, secondo il tipo | Valid non-negative integer greater than zero | [Studia](/html/controlli-form) |
| [`sizes`](https://html.spec.whatwg.org/multipage/semantics.html#attr-link-sizes) | link | Spazio previsto dell’immagine o dimensioni dell’icona secondo contesto | Unordered set of unique space-separated tokens , ASCII case-insensitive , consisting of sizes* | [Studia](/html/immagini-responsive) |
| [`sizes`](https://html.spec.whatwg.org/multipage/embedded-content.html#attr-img-sizes) | img ; source | Spazio previsto dell’immagine o dimensioni dell’icona secondo contesto | Valid source size list | [Studia](/html/immagini-responsive) |
| [`span`](https://html.spec.whatwg.org/multipage/tables.html#attr-col-span) | col ; colgroup | Numero di colonne del col/colgroup | Valid non-negative integer greater than zero | [Studia](/html/tabelle) |
| [`src`](https://html.spec.whatwg.org/multipage/media.html#attr-media-src) | audio ; embed ; iframe ; img ; input ; script ; source (in video or audio ); track ; video | URL della sorgente, secondo l’elemento | Valid non-empty URL potentially surrounded by spaces | [Studia](/html/contenuti-incorporati) |
| [`srcdoc`](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#attr-iframe-srcdoc) | iframe | Documento HTML inline del frame | The source of an iframe srcdoc document * | [Studia](/html/contenuti-incorporati) |
| [`srclang`](https://html.spec.whatwg.org/multipage/media.html#attr-track-srclang) | track | Lingua della traccia temporizzata | Valid BCP 47 language tag | [Studia](/html/audio-video) |
| [`srcset`](https://html.spec.whatwg.org/multipage/embedded-content.html#attr-img-srcset) | img ; source | Lista di sorgenti immagine candidate | Comma-separated list of image candidate strings | [Studia](/html/immagini-responsive) |
| [`start`](https://html.spec.whatwg.org/multipage/grouping-content.html#attr-ol-start) | ol | Numero iniziale della lista ordinata | Valid integer | [Studia](/html/navigazione) |
| [`step`](https://html.spec.whatwg.org/multipage/input.html#attr-input-step) | input | Passo dei valori numerici o temporali dove applicabile | Valid floating-point number greater than zero, or " any " | [Studia](/html/invio-validazione) |
| [`target`](https://html.spec.whatwg.org/multipage/links.html#attr-hyperlink-target) | a ; area | Contesto di navigazione destinazione | Valid navigable target name or keyword | [Studia](/html/navigazione) |
| [`target`](https://html.spec.whatwg.org/multipage/semantics.html#attr-base-target) | base | Contesto di navigazione destinazione | Valid navigable target name or keyword | [Studia](/html/navigazione) |
| [`target`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fs-target) | form | Contesto di navigazione destinazione | Valid navigable target name or keyword | [Studia](/html/navigazione) |
| [`title`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#attr-abbr-title) | abbr ; dfn | Informazioni consultive, non sostituto di nome o label | Text | [Studia](/html/attributi-globali) |
| [`title`](https://html.spec.whatwg.org/multipage/input.html#attr-input-title) | input | Informazioni consultive, non sostituto di nome o label | Text | [Studia](/html/attributi-globali) |
| [`title`](https://html.spec.whatwg.org/multipage/semantics.html#attr-link-title) | link | Informazioni consultive, non sostituto di nome o label | Text | [Studia](/html/attributi-globali) |
| [`title`](https://html.spec.whatwg.org/multipage/semantics.html#attr-link-title) | link ; style | Informazioni consultive, non sostituto di nome o label | Text | [Studia](/html/attributi-globali) |
| [`type`](https://html.spec.whatwg.org/multipage/links.html#attr-hyperlink-type) | a ; link | Tipo del controllo, script, risorsa o lista secondo contesto | Valid MIME type string | [Studia](/html/controlli-form) |
| [`type`](https://html.spec.whatwg.org/multipage/form-elements.html#attr-button-type) | button | Tipo del controllo, script, risorsa o lista secondo contesto | " submit "; " reset "; " button " | [Studia](/html/controlli-form) |
| [`type`](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#attr-embed-type) | embed ; object ; source | Tipo del controllo, script, risorsa o lista secondo contesto | Valid MIME type string | [Studia](/html/controlli-form) |
| [`type`](https://html.spec.whatwg.org/multipage/input.html#attr-input-type) | input | Tipo del controllo, script, risorsa o lista secondo contesto | input type keyword | [Studia](/html/controlli-form) |
| [`type`](https://html.spec.whatwg.org/multipage/grouping-content.html#attr-ol-type) | ol | Tipo del controllo, script, risorsa o lista secondo contesto | " 1 "; " a "; " A "; " i "; " I " | [Studia](/html/controlli-form) |
| [`type`](https://html.spec.whatwg.org/multipage/scripting.html#attr-script-type) | script | Tipo del controllo, script, risorsa o lista secondo contesto | " module "; " importmap "; " speculationrules "; a valid MIME type string that is not a JavaScript MIME type essence match | [Studia](/html/controlli-form) |
| [`usemap`](https://html.spec.whatwg.org/multipage/image-maps.html#attr-hyperlink-usemap) | img | Riferimento alla mappa dell’immagine | Valid hash-name reference * | [Studia](/html/immagini-responsive) |
| [`value`](https://html.spec.whatwg.org/multipage/form-elements.html#attr-button-value) | button ; option | Valore iniziale, dato macchina o misura secondo contesto | Text | [Studia](/html/controlli-form) |
| [`value`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#attr-data-value) | data | Valore iniziale, dato macchina o misura secondo contesto | Text * | [Studia](/html/controlli-form) |
| [`value`](https://html.spec.whatwg.org/multipage/input.html#attr-input-value) | input | Valore iniziale, dato macchina o misura secondo contesto | Varies* | [Studia](/html/controlli-form) |
| [`value`](https://html.spec.whatwg.org/multipage/grouping-content.html#attr-li-value) | li | Valore iniziale, dato macchina o misura secondo contesto | Valid integer | [Studia](/html/controlli-form) |
| [`value`](https://html.spec.whatwg.org/multipage/form-elements.html#attr-meter-value) | meter ; progress | Valore iniziale, dato macchina o misura secondo contesto | Valid floating-point number | [Studia](/html/controlli-form) |
| [`width`](https://html.spec.whatwg.org/multipage/canvas.html#attr-canvas-width) | canvas ; embed ; iframe ; img ; input ; object ; source (in picture ); video | Dimensione orizzontale, con regole proprie dell’elemento | Valid non-negative integer | [Studia](/html/contenuti-incorporati) |
| [`wrap`](https://html.spec.whatwg.org/multipage/form-elements.html#attr-textarea-wrap) | textarea | Trattamento delle interruzioni di riga della textarea | " soft "; " hard " | [Studia](/html/controlli-form) |

## Famiglie aperte e specifiche collegate

| Famiglia | Significato | Percorso |
| --- | --- | --- |
| `data-*` | Dati personalizzati dell’applicazione; non segreti né semantica nativa | [Attributi globali](/html/attributi-globali) |
| `role`, `aria-*` | Ruoli, stati e relazioni definiti da ARIA; rispettare i vincoli dell’elemento | [Accessibilità](/html/accessibilita-focus), [ARIA in HTML](https://www.w3.org/TR/html-aria/) |
| `part`, `exportparts` | Agganci di stile dello Shadow DOM, da specifiche collegate | [Componenti](/html/script-template) |

Queste famiglie non sono sommate artificialmente ai 144 nomi dell’indice. Attributi sperimentali o vendor-specific assenti dalla fonte non sono classificati come standard per aumentare il conteggio.

## Tutti i gestori di eventi dello snapshot

Ogni attributo esegue un handler per l’evento indicato dal nome senza prefisso `on`; il link specifica bersaglio e comportamento. Gli handler su `body` possono riferirsi a `Window`. Per nuovi programmi preferiamo `addEventListener`: vedi [eventi JavaScript](/javascript/tutorial/introduction-browser-events) e [event loop](/javascript/tutorial/event-loop). Il catalogo non costituisce un corso completo di tutte le API coinvolte.

| Attributo e definizione | Applicazione nell’indice | Evento |
| --- | --- | --- |
| [`onafterprint`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-window-onafterprint) | body | `afterprint` |
| [`onauxclick`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-onauxclick) | HTML elements | `auxclick` |
| [`onbeforeinput`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-onbeforeinput) | HTML elements | `beforeinput` |
| [`onbeforematch`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-onbeforematch) | HTML elements | `beforematch` |
| [`onbeforeprint`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-window-onbeforeprint) | body | `beforeprint` |
| [`onbeforeunload`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-window-onbeforeunload) | body | `beforeunload` |
| [`onbeforetoggle`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-onbeforetoggle) | HTML elements | `beforetoggle` |
| [`onblur`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-onblur) | HTML elements | `blur` |
| [`oncancel`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-oncancel) | HTML elements | `cancel` |
| [`oncanplay`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-oncanplay) | HTML elements | `canplay` |
| [`oncanplaythrough`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-oncanplaythrough) | HTML elements | `canplaythrough` |
| [`onchange`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-onchange) | HTML elements | `change` |
| [`onclick`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-onclick) | HTML elements | `click` |
| [`onclose`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-onclose) | HTML elements | `close` |
| [`oncommand`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-oncommand) | HTML elements | `command` |
| [`oncontextlost`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-oncontextlost) | HTML elements | `contextlost` |
| [`oncontextmenu`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-oncontextmenu) | HTML elements | `contextmenu` |
| [`oncontextrestored`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-oncontextrestored) | HTML elements | `contextrestored` |
| [`oncopy`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-oncopy) | HTML elements | `copy` |
| [`oncuechange`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-oncuechange) | HTML elements | `cuechange` |
| [`oncut`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-oncut) | HTML elements | `cut` |
| [`ondblclick`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-ondblclick) | HTML elements | `dblclick` |
| [`ondrag`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-ondrag) | HTML elements | `drag` |
| [`ondragend`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-ondragend) | HTML elements | `dragend` |
| [`ondragenter`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-ondragenter) | HTML elements | `dragenter` |
| [`ondragleave`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-ondragleave) | HTML elements | `dragleave` |
| [`ondragover`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-ondragover) | HTML elements | `dragover` |
| [`ondragstart`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-ondragstart) | HTML elements | `dragstart` |
| [`ondrop`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-ondrop) | HTML elements | `drop` |
| [`ondurationchange`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-ondurationchange) | HTML elements | `durationchange` |
| [`onemptied`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-onemptied) | HTML elements | `emptied` |
| [`onended`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-onended) | HTML elements | `ended` |
| [`onerror`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-onerror) | HTML elements | `error` |
| [`onfocus`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-onfocus) | HTML elements | `focus` |
| [`onformdata`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-onformdata) | HTML elements | `formdata` |
| [`onhashchange`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-window-onhashchange) | body | `hashchange` |
| [`oninput`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-oninput) | HTML elements | `input` |
| [`oninvalid`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-oninvalid) | HTML elements | `invalid` |
| [`onkeydown`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-onkeydown) | HTML elements | `keydown` |
| [`onkeypress`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-onkeypress) | HTML elements | `keypress` |
| [`onkeyup`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-onkeyup) | HTML elements | `keyup` |
| [`onlanguagechange`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-window-onlanguagechange) | body | `languagechange` |
| [`onload`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-onload) | HTML elements | `load` |
| [`onloadeddata`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-onloadeddata) | HTML elements | `loadeddata` |
| [`onloadedmetadata`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-onloadedmetadata) | HTML elements | `loadedmetadata` |
| [`onloadstart`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-onloadstart) | HTML elements | `loadstart` |
| [`onmessage`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-window-onmessage) | body | `message` |
| [`onmessageerror`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-window-onmessageerror) | body | `messageerror` |
| [`onmousedown`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-onmousedown) | HTML elements | `mousedown` |
| [`onmouseenter`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-onmouseenter) | HTML elements | `mouseenter` |
| [`onmouseleave`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-onmouseleave) | HTML elements | `mouseleave` |
| [`onmousemove`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-onmousemove) | HTML elements | `mousemove` |
| [`onmouseout`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-onmouseout) | HTML elements | `mouseout` |
| [`onmouseover`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-onmouseover) | HTML elements | `mouseover` |
| [`onmouseup`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-onmouseup) | HTML elements | `mouseup` |
| [`onoffline`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-window-onoffline) | body | `offline` |
| [`ononline`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-window-ononline) | body | `online` |
| [`onpagehide`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-window-onpagehide) | body | `pagehide` |
| [`onpagereveal`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-window-onpagereveal) | body | `pagereveal` |
| [`onpageshow`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-window-onpageshow) | body | `pageshow` |
| [`onpageswap`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-window-onpageswap) | body | `pageswap` |
| [`onpaste`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-onpaste) | HTML elements | `paste` |
| [`onpause`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-onpause) | HTML elements | `pause` |
| [`onplay`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-onplay) | HTML elements | `play` |
| [`onplaying`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-onplaying) | HTML elements | `playing` |
| [`onpopstate`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-window-onpopstate) | body | `popstate` |
| [`onprogress`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-onprogress) | HTML elements | `progress` |
| [`onratechange`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-onratechange) | HTML elements | `ratechange` |
| [`onreset`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-onreset) | HTML elements | `reset` |
| [`onresize`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-onresize) | HTML elements | `resize` |
| [`onrejectionhandled`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-window-onrejectionhandled) | body | `rejectionhandled` |
| [`onscroll`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-onscroll) | HTML elements | `scroll` |
| [`onscrollend`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-onscrollend) | HTML elements | `scrollend` |
| [`onsecuritypolicyviolation`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-onsecuritypolicyviolation) | HTML elements | `securitypolicyviolation` |
| [`onseeked`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-onseeked) | HTML elements | `seeked` |
| [`onseeking`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-onseeking) | HTML elements | `seeking` |
| [`onselect`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-onselect) | HTML elements | `select` |
| [`onslotchange`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-onslotchange) | HTML elements | `slotchange` |
| [`onstalled`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-onstalled) | HTML elements | `stalled` |
| [`onstorage`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-window-onstorage) | body | `storage` |
| [`onsubmit`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-onsubmit) | HTML elements | `submit` |
| [`onsuspend`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-onsuspend) | HTML elements | `suspend` |
| [`ontimeupdate`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-ontimeupdate) | HTML elements | `timeupdate` |
| [`ontoggle`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-ontoggle) | HTML elements | `toggle` |
| [`onunhandledrejection`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-window-onunhandledrejection) | body | `unhandledrejection` |
| [`onunload`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-window-onunload) | body | `unload` |
| [`onvolumechange`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-onvolumechange) | HTML elements | `volumechange` |
| [`onwaiting`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-onwaiting) | HTML elements | `waiting` |
| [`onwheel`](https://html.spec.whatwg.org/multipage/webappapis.html#handler-onwheel) | HTML elements | `wheel` |

Fonte: [WHATWG · Indice degli attributi](https://html.spec.whatwg.org/multipage/indices.html#attributes-3). I significati italiani sono curati per Learning; la specifica contiene i vincoli completi.
