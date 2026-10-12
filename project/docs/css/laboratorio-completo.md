# 35 · Laboratorio completo e soluzioni

**Obiettivo:** costruire una pagina robusta e dimostrare le scelte con prove osservabili.

## Un progetto che applica il corso

Il progetto è il sito dei laboratori HTML, con schede, calendario, iscrizione di prova e domande frequenti. Parti dal documento HTML e costruisci lo stile prima di aprire la soluzione.

| Area | Prova richiesta |
| --- | --- |
| Cascata | Spiega un conflitto usando origine, layer e selettore |
| Box e layout | Schede senza overflow a 320px e con testi lunghi |
| Tipografia | Zoom, font alternativo e spaziatura non tagliano contenuti |
| Responsive | Colonne e controlli cambiano quando lo spazio lo richiede |
| Focus | Percorso completo con Tab, outline visibile e attivazione nativa |
| Colori | Coppie testo/sfondo verificate, stato non comunicato solo dal colore |
| Preferenze | Reduced motion e contrasto forzato preservano funzione e riconoscibilità |
| Stampa | Programma, date e contatti restano leggibili |
| Compatibilità | Una base funziona con miglioramenti avanzati disattivati |
| Debugging | Documenti la causa e la correzione di un problema reale |

Non aggiungere ogni filtro o animazione al sito per completare il corso. Gli effetti non richiesti dal progetto vanno nella cartella esperimenti, con gli esercizi delle singole lezioni. Le proprietà devono risolvere un bisogno.

## Esercizio del progetto

Usa classi di componente, un ordine di layer e token riutilizzabili. Definisci una griglia adattabile, spazi logici, controlli con font coerente e un foglio print. Le informazioni del form sono inventate e non vengono registrate.

::: details Soluzione eseguibile
Apri la [pagina completa](/esempi/laboratorio-css.html) e il [foglio CSS](/esempi/laboratorio-css.css). Sono file autonomi: puoi copiarli nella stessa cartella e aprire la pagina localmente. Contengono layout, token, layer, stati, tabella, form e stampa. Il confronto con il [documento senza CSS](/esempi/laboratorio-html.html) mostra ciò che aggiunge la presentazione.

Le funzioni grafiche avanzate restano esperimenti separati: una soluzione completa del progetto non deve usare tutto il catalogo CSS. Le lezioni 16–34 forniscono esempi e criteri per gli approfondimenti.
:::

## Cinque problemi da correggere

1. Un h1 lungo viene tagliato da height 4rem.
2. Tre colonne fisse escono dallo schermo piccolo.
3. Un input ha font minuscolo e nessun focus visibile.
4. Un menu si vede soltanto durante hover.
5. Un'ombra distingue una scheda ma sparisce in contrasto forzato.

::: details Soluzioni ragionate
Lascia crescere il titolo; usa griglia intrinseca o un breakpoint adatto; applica font inherit e un focus visibile; rendi la funzione disponibile anche con tastiera/touch e comportamento appropriato; conserva un bordo riconoscibile. Poi ripeti le prove con contenuti più lunghi. Evita overflow hidden globale e z-index enormi come rimedi generici.
:::

## Il passo successivo

Quando completi il progetto delle basi, puoi iniziare [JavaScript](/javascript/). Torna agli approfondimenti mentre aggiungi comportamento al sito. La [mappa di copertura](/css/copertura) distingue argomenti presenti, prove pratiche e ciò che rimane nel riferimento ufficiale.

Fonti per le verifiche: [Chrome DevTools · CSS](https://developer.chrome.com/docs/devtools/css), [WAI · Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html).
