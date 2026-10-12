# 26 · Laboratorio completo e verifica

**Obiettivo:** trasformare il riferimento in capacità osservabili, senza inserire elementi solo per spuntare una lista.

## Il progetto: un piccolo sito di laboratori

Crea tre pagine collegate: presentazione dei corsi, calendario e iscrizione. Parti dal [progetto delle basi](/html/progetto), poi aggiungi contenuto reale e usa questa rubrica.

| Area | Risultato richiesto | Prova |
| --- | --- | --- |
| Documento | Doctype, UTF-8, lingua, title e viewport | Sorgente e scheda del browser |
| Sintassi | Categorie e annidamenti validi | Validatore e confronto sorgente/DOM |
| Semantica | Main, regioni, titoli e contatti pertinenti | Elenco dei titoli e landmark |
| Navigazione | Link fra pagine, frammenti, pagina corrente | Percorso completo senza mouse |
| Testo | Data macchina, glossario, annotazione significativa | Spiega ciascun elemento scelto |
| Immagini | Alternative, dimensioni e candidati responsive | Risorsa scelta e immagine assente |
| Tabelle | Caption e intestazioni di dati | Interpreta una cella con lettore di schermo |
| Media | Controlli, captions e trascrizione | Tastiera, traccia attiva, media irraggiungibile |
| Form | Label, gruppo, scelte, vincoli e name | Invio vuoto e previsione delle voci inviate |
| Interazioni | FAQ e dialogo/popover appropriati | Apertura, chiusura e focus |
| Internazionalizzazione | Cambio di lingua e isolamento di nomi | Ordine e pronuncia del testo |
| Componenti | Un template con fallback | Comprendi perché non viene mostrato direttamente |
| Dati strutturati | Informazioni coerenti col testo | Confronto markup–contenuto visibile |
| Caricamento | Priorità e lazy loading motivate | Network con cache disabilitata |
| Compatibilità | Browser previsti e fallback documentati | Prova con funzione non disponibile |

Non è necessario forzare canvas, mappe cliccabili o tutti i tipi di input nella pagina principale. Crea una cartella `esperimenti` per le funzioni che il progetto non richiede. Il catalogo completo serve a riconoscerle e consultarne i vincoli, non a rendere ogni documento il più lungo possibile.

## Una soluzione di partenza

La [pagina HTML autonoma](/esempi/laboratorio-html.html) è una soluzione parziale funzionante per struttura, navigazione, tabella, form, dettagli e popover. Puoi aprire il sorgente dal browser e copiarlo in un file locale. Le immagini e i media vanno aggiunti con file veri; un backend per iscrizioni non è incluso.

::: details Come completarla
Dividi la pagina in tre documenti e aggiorna i link relativi. Aggiungi un'immagine con due varianti reali, un breve video con una traccia WebVTT e la sua trascrizione. Inserisci un template normale nell'area esperimenti e il dialogo della lezione 20. Per il form mantieni dati inventati durante le prove e crea un endpoint locale nella tappa backend.
:::

## Controlli tecnici

Usa [Nu HTML Checker](https://validator.w3.org/nu/) per documenti completi. Correggi errori e interpreta gli avvisi: un validatore non verifica qualità di alt, lingua reale, regole del backend o tutta l'accessibilità.

DevTools permette di osservare DOM, nomi accessibili, richieste e file mancanti. Prova zoom, tastiera, larghezze diverse e almeno i browser pertinenti al pubblico del progetto. Registra una tabella «prova → risultato → correzione». Un controllo automatico di accessibilità è un aiuto, da integrare con prove manuali.

## Esercizio conclusivo con soluzione

Un form usa solo placeholder, un'immagine informativa ha `alt=""`, una tabella usa `td` per tutti i titoli e un link `href="#"` salva dati al click. Correggi le quattro scelte.

::: details Soluzione
Aggiungi label visibili collegate agli input; scrivi un'alternativa che comunichi lo scopo dell'immagine; usa `th` e le associazioni appropriate; per salvare usa un button e il flusso form/API corretto. Poi verifica tastiera, dati inviati e messaggi di errore. I dettagli di rete e salvataggio proseguono con JavaScript e backend.
:::

## Quando passare a CSS

Puoi passare a CSS quando completi il progetto delle basi e sai cercare una funzione nel riferimento. Gli approfondimenti HTML restano disponibili durante CSS e JavaScript. «Catalogo al 100%» non significa che hai completato tutte le prove della rubrica: sono due misure distinte, descritte nella [pagina di copertura](/html/copertura).

Fonti: [Nu HTML Checker](https://validator.w3.org/nu/), [WAI · Easy Checks](https://www.w3.org/WAI/test-evaluate/preliminary/).
