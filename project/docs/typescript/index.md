# TypeScript: dopo un progetto JavaScript

**Prerequisito:** completa la [lista di attività in JavaScript](/javascript/). Le lezioni di questa tappa sono da scrivere; questa pagina ne definisce obiettivi e progetto.

TypeScript aggiunge a JavaScript un controllo statico dei tipi. Ci aiuterà a descrivere i dati delle attività e a individuare errori prima di eseguire il programma. Le basi JavaScript rimangono necessarie.

## Cosa impareremo

1. Inferenza e annotazioni: quando serve scrivere un tipo.
2. Tipi primitivi, array, oggetti e funzioni.
3. `type`, `interface`, proprietà opzionali e union.
4. Narrowing: controllare quale valore abbiamo davvero.
5. `unknown` e validazione dei dati esterni; i limiti di `any` e delle asserzioni.
6. Tipi degli eventi e gestione degli elementi del DOM che potrebbero mancare.
7. Moduli, `tsconfig`, controllo rigoroso dei tipi e generics di base quando servono.

## Lo stesso progetto, con tipi

Trasformeremo la lista di attività esistente in TypeScript. Definiremo prima il modello di un'attività, poi le funzioni che la creano, modificano e salvano. Il comportamento dell'applicazione dovrà rimanere lo stesso.

## Quando saremo pronti per il backend

Saprai modellare un'attività, comprendere gli errori del compilatore e distinguere un tipo dichiarato da un dato controllato a runtime. Un valore proveniente da `JSON.parse` o da una API richiede verifica: un'asserzione di tipo non lo rende valido.

La prossima tappa sarà [HTTP, API e Node.js](/backend/). [Torna alla roadmap](/percorso).

Riferimento: [TypeScript per chi inizia](https://www.typescriptlang.org/docs/handbook/typescript-from-scratch.html).
