# 24 · Sicurezza e caricamento delle risorse

**Obiettivo:** riconoscere le conseguenze di un attributo che carica contenuti o modifica l'interazione.

## Il confine fra testo e markup

HTML può caricare risorse ed eseguire script. Se un'applicazione inserisce input non attendibile come HTML, un testo apparentemente innocuo può diventare markup attivo. L'escaping deve essere adatto al contesto: testo, attributo, URL e script hanno regole diverse. La sanitizzazione di HTML consentito è un problema distinto.

```html
<p>Il messaggio letterale è: &lt;script&gt;alert(1)&lt;/script&gt;</p>
```

Quando useremo JavaScript, `textContent` sarà appropriato per semplice testo; `innerHTML` richiederà una ragione e controlli adeguati. In un backend evita di costruire HTML tramite concatenazione di input arbitrario; usa escaping previsto dal sistema di template.

## Origini, integrità e policy

`crossorigin` controlla modalità delle richieste nei contesti previsti, insieme al CORS del server. `referrerpolicy` influenza le informazioni del referrer inviate. `sandbox` e `allow` limitano capacità degli iframe secondo regole differenti. Nessun attributo rende affidabile una destinazione sconosciuta.

`integrity` verifica che una risorsa corrisponda all'hash dichiarato; cambia quando cambia il file. Per risorse cross-origin devono essere coerenti anche le impostazioni CORS. Non inserire hash inventati: una verifica fallita impedisce il caricamento.

La Content Security Policy limita sorgenti e altre capacità. Un `nonce` va generato dal server per la risposta e deve corrispondere alla policy; una stringa fissa copiata in tutte le pagine non offre lo stesso modello. La CSP tramite header offre opzioni che una `meta http-equiv` non può rappresentare interamente. Sicurezza della sessione, cookie e autorizzazioni proseguono nel backend.

## Caricamento con priorità ragionata

```html
<link rel="preconnect" href="https://fonts.example.org" crossorigin>
<link rel="preload" href="/copertina.jpg" as="image">
<img src="/copertina.jpg" width="1200" height="675" fetchpriority="high"
     alt="Il laboratorio durante un'esercitazione">
```

Questi sono esempi di markup: usa solo risorse reali necessarie al progetto. `preconnect` prepara una connessione, `preload` anticipa una risorsa, `modulepreload` riguarda moduli. `as`, `type`, `media`, `imagesrcset`, `imagesizes` e `crossorigin` devono corrispondere alla richiesta effettiva. Precaricare tutto può sprecare banda e ritardare ciò che conta.

`loading="lazy"` serve a rimandare alcune risorse fuori vista, non l'immagine principale. `fetchpriority` e `decoding` sono suggerimenti. `blocking` riguarda aspetti del blocco del rendering nei contesti previsti; l'ordine dei classici script e dei moduli rimane distinto. Misura in Network e Performance, con cache e dispositivi diversi, prima di aggiungere ottimizzazioni.

## Esercizio e verifica

In una pagina con copertina iniziale e immagini più in basso, assegna priorità senza ritardare la copertina. Spiega perché POST e un campo hidden non proteggono dati.

::: details Soluzione
Copertina con dimensioni esplicite e caricamento normale, eventuale `fetchpriority="high"` se la misura lo giustifica; immagini successive con lazy loading. POST non cifra il trasporto e hidden può essere modificato: servono HTTPS e verifiche del server.
:::

Fonti: [MDN · XSS](https://developer.mozilla.org/en-US/docs/Web/Security/Attacks/XSS), [MDN · Subresource Integrity](https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Subresource_Integrity), [MDN · link](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link), [WHATWG · Link types](https://html.spec.whatwg.org/multipage/links.html#linkTypes).
