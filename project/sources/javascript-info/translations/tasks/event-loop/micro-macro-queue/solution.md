L'ordine è **1, 7, 3, 5, 2, 6, 4**.

1. `1` e `7` sono stampati durante l'esecuzione sincrona.
2. Terminato il codice corrente, vengono eseguite le microtask delle Promise: la prima stampa `3`, la seconda programma il timer per `4`, la terza stampa `5`.
3. I timer già programmati per `2` e `6` precedono il timer appena aggiunto per `4`.

La callback di una Promise non viene eseguita immediatamente dalla chiamata a `then`: entra nella coda delle microtask. Il timer creato dentro quella callback viene aggiunto solo quando la callback viene eseguita.
