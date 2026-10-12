# Fonti, traduzioni e licenza

Il corso JavaScript ripubblica e adatta **The Modern JavaScript Tutorial**, creato da **Ilya Kantor**, con il lavoro dei contributori del progetto e della traduzione italiana. Learning è un sito di studio indipendente e non implica approvazione o collaborazione ufficiale da parte dell'autore.

## Fonti

- [JavaScript.info: versione inglese](https://javascript.info/).
- [JavaScript.info: edizione italiana](https://it.javascript.info/).
- [Sorgenti inglesi](https://github.com/javascript-tutorial/en.javascript.info/tree/20208769e528337949e946f526534d61d38bac47).
- [Sorgenti italiani](https://github.com/javascript-tutorial/it.javascript.info/tree/12f2526c8c0dd41320d1d85e477d6074abdb7005).

L'importazione include i **175 articoli** presenti nello snapshot inglese e **252 esercizi** con soluzioni: 250 dal repository italiano e due tradotti dal repository inglese. I collegamenti alla fonte compaiono anche nei singoli articoli.

## Che cosa abbiamo modificato

- Riutilizzato 171 articoli dall'edizione italiana, con adattamento del formato a VitePress.
- Tradotto e adattato quattro capitoli: [Unicode](/javascript/tutorial/unicode), [WeakRef e FinalizationRegistry](/javascript/tutorial/weakref-finalizationregistry), [IndexedDB](/javascript/tutorial/indexeddb) e [Shadow DOM ed eventi](/javascript/tutorial/shadow-dom-events).
- Tradotto anche due esercizi aggiuntivi su event loop e `Promise.all`.
- Convertito riquadri, evidenziazioni, collegamenti, figure e soluzioni espandibili.
- Sostituito le dimostrazioni che richiedono il renderer originale con collegamenti alla fonte.
- Aggiunto un nostro ordine di studio, separando la base frontend dagli approfondimenti.

Le quattro traduzioni sono adattamenti editoriali: alcuni passaggi sono riformulati e alcuni esempi sono aggiornati. IndexedDB chiarisce la clonazione strutturata e usa l'API attuale di `idb`; WeakRef chiarisce che la raccolta e la finalizzazione non hanno tempi garantiti; Unicode distingue punti di codice e unità UTF-16.

Gli altri articoli riflettono lo snapshot italiano e possono contenere riferimenti a strumenti o pratiche meno recenti. L'importazione non equivale a una revisione tecnica integrale. Per ciascuna lezione puoi confrontare la fonte inglese attuale con quella italiana.

## Condizioni di riutilizzo

© Ilya Kantor e contributori. Il sito delle lezioni è gratuito e senza pubblicità.

I repository distribuiscono il materiale con una licenza basata su **Creative Commons Attribution–NonCommercial**, con il testo specifico pubblicato dall'autore. I [termini del sito](https://javascript.info/terms) descrivono anche la condivisione del tutorial con attribuzione e uso non commerciale. Riportiamo integralmente entrambi i testi di licenza, che restano i riferimenti per i rispettivi materiali:

- [Licenza dello snapshot inglese](/javascript-info/LICENSE-en.txt).
- [Licenza dello snapshot italiano](/javascript-info/LICENSE-it.txt).

I nostri adattamenti dei capitoli seguono le condizioni di riutilizzo delle fonti; l'attribuzione e i collegamenti alle licenze devono essere mantenuti. Le pagine di roadmap e il laboratorio Learning sono identificati come contenuti aggiunti da noi.

## Provenienza e aggiornamenti

Nel repository Learning, `project/sources/javascript-info/manifest.json` registra fonte, traduzione, impronta SHA-256 e numero di esercizi di ciascun articolo. Le quattro traduzioni aggiunte sono in `project/sources/javascript-info/translations`.

L'importazione è uno snapshot: non scarichiamo contenuti durante la build o mentre studi. Gli aggiornamenti delle fonti richiedono una nuova importazione e la verifica della build.
