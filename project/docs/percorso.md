# Il nostro percorso

Impariamo costruendo. Ogni tappa aggiunge una capacità alla precedente: prima i contenuti, poi lo stile, poi il comportamento. Infine esploreremo Rust come linguaggio per scrivere programmi con un modello diverso di tipi e memoria.

| Tappa | Domanda | Cosa costruiremo | Stato |
| --- | --- | --- | --- |
| [HTML](/html/) | Che cosa significa questo contenuto? | Una pagina personale accessibile | Lezioni disponibili |
| [CSS](/css/) | Come si presenta su schermi diversi? | Lo stile della pagina personale | Prossima tappa |
| [JavaScript](/javascript/) | Come risponde alle azioni? | Una piccola lista di attività | Da affrontare dopo CSS |
| [Rust](/rust/) | Come modelliamo dati e operazioni? | Un programma da terminale | Dopo le basi di JavaScript |

## Un metodo semplice

1. Leggi una lezione: punta a capire l'idea centrale.
2. Copia l'esempio in un file e aprilo nel browser.
3. Modifica qualcosa e osserva cosa cambia.
4. Prova l'esercizio senza guardare la soluzione.
5. Spiega a parole tue cosa hai imparato.

Sessioni di 20–30 minuti sono un buon punto di partenza. Se un passaggio non è chiaro, fermiamoci lì: la velocità viene con la pratica.

## Cosa serve per HTML

Un editor di testo, un browser e una cartella `esercizi`. Puoi aprire i file `.html` direttamente nel browser. Node.js serve per avviare **questo sito VitePress**, ma non è necessario per gli esercizi HTML.

::: tip Il tuo primo passo
Apri [La prima pagina](/html/prima-pagina). Alla fine avrai già creato un documento HTML completo.
:::

## Come aggiorniamo le lezioni

I sorgenti sono file Markdown dentro `project/docs`. VitePress li trasforma nel sito. Per lavorare in locale, dalla cartella del repository:

```bash
cd project
npm ci
npm run docs:dev
```

Per preparare la versione pubblicabile:

```bash
npm run docs:build
npm run docs:preview
```

La guida al deploy è nel `README.md` del repository.
