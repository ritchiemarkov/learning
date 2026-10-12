---
title: "Date e time"
description: "JavaScript.info in italiano: Date e time"
sourceTutorial: true
prev: {"text": "Assegnamento di destrutturazione", "link": "/javascript/tutorial/destructuring-assignment"}
next: {"text": "Metodi JSON, toJSON", "link": "/javascript/tutorial/json"}
---

# Date e time

> **JavaScript.info · Ilya Kantor e contributori.** [Originale inglese](https://javascript.info/date) · [Edizione italiana](https://it.javascript.info/date) · [Fonti e licenza](/javascript/fonti).

Ora analizziamo un nuovo oggetto integrato: [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date). Esso memorizza la data e l'ora e fornisce dei metodi utili per il trattamento di queste.

Ad esempio, possiamo utilizzarlo per memorizzare modifiche su orari, o per misurare il tempo, o solamente per ottenere l'informazione della data corrente.

## Creazione

Per creare un nuovo oggetto `Date`, chiamiamo `new Date()` con uno dei seguenti argomenti:

`new Date()`
: Senza argomenti -- crea un oggetto `Date` con la data e l'ora corrente:

    ```js
    let now = new Date();
    alert( now ); // mostra l'attuale data/tempo
    ```

`new Date(milliseconds)`
: Crea un oggetto `Date` con l'ora impostata al numero di millisecondi trascorsi dal 1 Gennaio 1970 UTC+0.

    ```js
    // 0 significa 01.01.1970 UTC+0
    let Jan01_1970 = new Date(0);
    alert( Jan01_1970 );

    // ora vengono aggiunte 24 ore, si ha 02.01.1970 UTC+0
    let Jan02_1970 = new Date(24 * 3600 * 1000);
    alert( Jan02_1970 );
    ```

    Il numero di millisecondi passati da questa data vengono detti *timestamp*.

    E' un modo semplice di rappresentare una data. Possiamo sempre creare una data a partire da un timestamp utilizzando `new Date(timestamp)`, o possiamo convertire un oggetto `Date` esistente utilizzando il metodo `date.getTime()` (vedi sotto).

    Le date prima del 01.01.1970 hanno timestamps negativi, ad esempio:
    ```js
    // 31 Dec 1969
    let Dec31_1969 = new Date(-24 * 3600 * 1000);
    alert( Dec31_1969 );
    ```

`new Date(datestring)`
: Se viene fornito un solo argomento, ed è una stringa, allora viene analizzato tramite l'algoritmo `Date.parse` (che vedremo tra poco).


    ```js
    let date = new Date("2017-01-26");
    alert(date);
    // Il tempo non è specificato, quindi si da per scontato che sia mezzanotte GMT e viene
    // corretto a seconda della timezone dove il codice viene eseguito
    // Quindi il risultato potrebbe essere
    // Thu Jan 26 2017 11:00:00 GMT+1100 (Australian Eastern Daylight Time)
    // o
    // Wed Jan 25 2017 16:00:00 GMT-0800 (Pacific Standard Time)
    ```

`new Date(year, month, date, hours, minutes, seconds, ms)`
: Crea la data con le informazioni fornite. Solo i primi due argomenti sono obbligatori.

    Nota:

    - Il campo `year` deve essere composto da 4 cifre: `2013` va bene, `98` non è corretto.
    - Il numero `month` inizia da `0` (Gennaio), fino a `11` (Dicembre).
    - Il parametro `date` rappresenta il giorno del mese, se non viene fornito il valore di default è `1`.
    - Se non vengono forniti `hours/minutes/seconds/ms`, il valore di default è `0`.

    Ad esempio:

    ```js
    new Date(2011, 0, 1, 0, 0, 0, 0); // 1 Gennaio 2011, 00:00:00
    new Date(2011, 0, 1); //  // lo stesso, le ore ecc sono 0 di default
    ```

    La precisione minima è 1 ms (1/1000 sec):

    ```js
    let date = new Date(2011, 0, 1, 2, 3, 4, 567);
    alert( date ); // 1.01.2011, 02:03:04.567
    ```

## Accedere ai componenti di date

Ci sono diversi metodi per poter accedere a 'year', 'month' e agli altri parametri dell'oggetto `Date`. Per ricordarli meglio li divideremo in categorie.

[getFullYear()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getFullYear)
: Fornisce il valore di 'year' (anno), (4 cifre).

[getMonth()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getMonth)
: Fornisce il valore di 'month' (mese), **da 0 a 11**.

[getDate()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getDate)
: Fornisce il giorno del mese, da 1 a 31, il nome del metodo potrebbe confondere.

[getHours()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getHours), [getMinutes()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getMinutes), [getSeconds()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getSeconds), [getMilliseconds()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getMilliseconds)
: Fornisce il valore del corrispettivo parametro.


::: warning Not `getYear()`, but `getFullYear()`
Molti motori JavaScript implementano una versione non standard del metodo `getYear()`, che in alcuni casi ritorna un valore a 2 cifre. Per questo è un metodo deprecato ed è sconsigliato utilizzarlo. In sostituzione esiste un metodo più completo, `getFullYear()`.
:::

In più potremmo anche prelevare il giorno della settimana:

[getDay()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getDay)
: Restituisce il giorno della settimana, da `0` (Domenica) a `6` (Sabato). Il primo giorno è sempre Domenica; in alcuni stati non è cosi, ma non può essere modificato.

**Tutti i metodi sopra ritornano componenti relativi all'orario locale.**

Esistono anche le controparti UTC, che ritornano giorno, mese, anno e molto altro per la zona temporale UTC+0: [getUTCFullYear()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getUTCFullYear), [getUTCMonth()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getUTCMonth), [getUTCDay()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getUTCDay). E' sufficiente inserire `"UTC"` appena dopo `"get"`.

Se il vostro orario locale è scostato dal UTC, allora il codice sotto potrebbe mostrare orari differenti:

```js
// data corrente 
let date = new Date();

// l'ora nella tua time zone corrente
alert( date.getHours() );

// L'ora in UTC+0 time zone (l'orario di Londra senza l'ora legale)
alert( date.getUTCHours() );
```


Oltre ai metodi forniti, ce ne sono altri due speciali, che non possiedono la variante UTC:

[getTime()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getTime)
: Ritorna il timestamp della data -- il numero di millisecondi trascorsi dal 1 Gennaio 1970 in UTC+0.

[getTimezoneOffset()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getTimezoneOffset)
: Ritorna la differenza tra UTC e l'orario locale, in minuti:

    ```js
    // se sei in una timezone UTC-1, ritorna 60
    // se sei in una timezone UTC+3, ritorna -180
    alert( new Date().getTimezoneOffset() );

    ```

## Impostare i componenti di date 

I seguenti metodi consentono di impostare i componenti data/tempo:

- [`setFullYear(year, [month], [date])`](mdn:js/Date/setFullYear)
- [`setMonth(month, [date])`](mdn:js/Date/setMonth)
- [`setDate(date)`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setDate)
- [`setHours(hour, [min], [sec], [ms])`](mdn:js/Date/setHours)
- [`setMinutes(min, [sec], [ms])`](mdn:js/Date/setMinutes)
- [`setSeconds(sec, [ms])`](mdn:js/Date/setSeconds)
- [`setMilliseconds(ms)`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setMilliseconds)
- [`setTime(milliseconds)`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setTime) (imposta la data in millisecondi dal 01.01.1970 UTC)

Ognuno dei metodi sopra, ad eccezione di `setTime()` possiedono la variante UTC, ad esempio: `setUTCHours()`.

Come possiamo vedere, alcuni metodi possono impostare più componenti in una volta sola, ad esempio `setHours`. I componenti che non vengono menzionati non verranno modificati.

Ad esempio:

```js
let today = new Date();

today.setHours(0);
alert(today); // ancora oggi, ma l'ora è cambiata a 0

today.setHours(0, 0, 0, 0);
alert(today); // ancora oggi, ma ora è 00:00:00 preciso.
```

## Autocorrezione

L' *autocorrezione* è un caratteristica molto utile degli oggetti `Date`. Potremmo inserire valori fuori dagli intervalli, e questi verranno automaticamente aggiustati.

Ad esempio:

```js
let date = new Date(2013, 0, 32); // 32 Gen 2013 ?!?
alert(date); // ...è il primo Feb 2013!
```

I componenti fuori dall'intervallo vengono distribuiti automaticamente.

Ipotizziamo di voler incrementare la data "28 Feb 2016" di 2 giorni. Potrebbe essere "2 Mar" o "1 Mar" nel caso di anno bisestile. Non abbiamo bisogno di pensarci. Semplicemente aggiungiamo 2 giorni. L'oggetto `Date` farà il resto:

```js
let date = new Date(2016, 1, 28);

date.setDate(date.getDate() + 2);


alert( date ); // 1 Mar 2016
```

Questa caratteristica viene utilizzata spesso per ottenere la data dopo un certo periodo di tempo. Ad esempio, proviamo ad ottenere la data di "70 secondi da adesso":

```js
let date = new Date();
date.setSeconds(date.getSeconds() + 70);

alert( date ); // mostra la data corretta
```

Possiamo anche impostare zero o un valore negativo. Ad esempio:

```js
let date = new Date(2016, 0, 2); // 2 Gen 2016

date.setDate(1); // imposta il primo giorno del mese
alert( date );

date.setDate(0); // il primo giorno del mese è 1, quindi viene impostato l'ultimo giorno del mese precedente
alert( date ); // 31 Dec 2015
```

## Da date a number, differenza di date 

Quando un oggetto `Date` viene convertito a numero, diventa un the timestamp come `date.getTime()`:

```js
let date = new Date();
alert(+date); // il numero di millisecondi, uguale a date.getTime()
```

Un importante effetto collaterale: le date possono essere sottratte; il risultato è la loro differenza in millisecondi.

Questa caratteristica può essere utilizzata per effettuare misurazioni:

```js
let start = new Date(); // inizia a misurare il tempo

// esegui le tue operazioni
for (let i = 0; i < 100000; i++) {
  let doSomething = i * i * i;
}

let end = new Date(); // misura il tempo

alert( `The loop took ${end - start} ms` );
```

## Date.now()

Se vogliamo solo misurare una differenza, non abbiamo bisogno di un oggetto `Date`.

Esiste uno speciale metodo `Date.now()` che ritorna il timestamp corrente.

E' equivalente a `new Date().getTime()`, ma evita di creare un oggetto `Date`. Quindi risulta più veloce e non produce spazzatura in memoria.

Viene spesso utilizzato per comodità o quando le prestazioni diventano fondamentali, come nei giochi o altre particolari applicazioni.

Quindi è meglio fare:

```js

let start = Date.now(); // il conto dei millisecondi dal 1 Gen 1970


// esegui le tue operazioni
for (let i = 0; i < 100000; i++) {
  let doSomething = i * i * i;
}


let end = Date.now(); // done


alert( `The loop took ${end - start} ms` ); // sottrai numeri, non date
```

## Benchmarking

Se volessimo un benchmark affidabile del consumo di CPU di una funzione, dovremmo prestare attenzione.

Ad esempio, proviamo a misurare due funzioni che calcolano la differenza tra due date: quale sarebbe più veloce?

Queste misurazioni di performance vengono spesso chiamate "benchmarks".

```js
// abbiamo date1 e date2, quale funzione ritorna più velocemente la loro differenza in ms?
function diffSubtract(date1, date2) {
  return date2 - date1;
}

// o
function diffGetTime(date1, date2) {
  return date2.getTime() - date1.getTime();
}
```

Queste due fanno esattamente la stessa cosa, ma una di lore usa esplicitamente `date.getTime()` per ottenere la data in millisecondi, mentre l'altra si appoggia alla conversione data-numero. Il risultato non cambia.

Quindi, quale delle due è più veloce?

Una prima idea potrebbe essere quella di eseguirle varie volte e misurare la differenza. Nel nostro caso, le funzioni sono molto semplici, quindi dovremmo eseguirle 100000 volte.

Proviamo a misurare:

```js
function diffSubtract(date1, date2) {
  return date2 - date1;
}

function diffGetTime(date1, date2) {
  return date2.getTime() - date1.getTime();
}

function bench(f) {
  let date1 = new Date(0);
  let date2 = new Date();

  let start = Date.now();
  for (let i = 0; i < 100000; i++) f(date1, date2);
  return Date.now() - start;
}

alert( 'Time of diffSubtract: ' + bench(diffSubtract) + 'ms' );
alert( 'Time of diffGetTime: ' + bench(diffGetTime) + 'ms' );
```

Wow! L'utilizzo di `getTime()` è molto più veloce! Questo accade perché non c'è alcuna conversione di tipo, il che significa un'operazione più semplice da ottimizzare.

Okay, abbiamo qualcosa. Ma non è sufficiente.

Immaginiamo che al momento dell'esecuzione di `bench(diffSubtract)` le risorse della CPU siano occupate, e che allo stesso tempo `bench(diffGetTime)` sia già stato elaborato.

Uno scenario realistico per i processori moderni.

Quindi, il primo benchmark potrebbe richiedere meno risorse CPU del secondo. E ciò potrebbe portare a conclusioni errate.

**Per eseguire benchmark più affidabili, l'intero pacchetto di benchmark dovrebbe essere eseguito più volte.**

Qui un esempio:

```js
function diffSubtract(date1, date2) {
  return date2 - date1;
}

function diffGetTime(date1, date2) {
  return date2.getTime() - date1.getTime();
}

function bench(f) {
  let date1 = new Date(0);
  let date2 = new Date();

  let start = Date.now();
  for (let i = 0; i < 100000; i++) f(date1, date2);
  return Date.now() - start;
}

let time1 = 0;
let time2 = 0;


// esegue alternativamente bench(diffSubtract) e bench(diffGetTime) per 10 volte
for (let i = 0; i < 10; i++) {
  time1 += bench(diffSubtract);
  time2 += bench(diffGetTime);
}


alert( 'Total time for diffSubtract: ' + time1 );
alert( 'Total time for diffGetTime: ' + time2 );
```

I motori JavaScript moderni iniziano ad applicare ottimizzazioni solamente a "pezzi" di codice eseguiti molte volte (non è necessario ottimizzare un codice eseguito di rado). Quindi, nell'esempio sopra, la prima esecuzione non è ben ottimizzata. Vorremmo quindi poter forzare l'ottimizzazione:

```js
// aggiunto per "riscaldare" prima del loop principale
bench(diffSubtract);
bench(diffGetTime);

// ora benchmark
for (let i = 0; i < 10; i++) {
  time1 += bench(diffSubtract);
  time2 += bench(diffGetTime);
}
```


::: warning Prestate attenzione ai microbenchmarking
I moderni motori JavaScript applicano molte ottimizzazioni. Potrebbero quindi "truccare" i risultati di un "test artificiale" a differenza del "normale utilizzo", specialmente se stiamo eseguendo bemchmark molto piccoli. 
Quindi se l'intenzione è quella di studiare le prestazioni, vale la pena studiare come funziona il motore JavaScript. Probabilmente non avrete più bisogno dei microbenchmark.

Un buona libreria di articoli può essere trovata qui: <http://mrale.ph>.
:::

## Date.parse da una stringa

Il metodo [Date.parse(str)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/parse) può leggere una data da una stringa.

Il formato della stringa dovrebbe essere: `YYYY-MM-DDTHH:mm:ss.sssZ`, dove:

- `YYYY-MM-DD` -- è la data: anno-mese-giorno.
- Il carattere `"T"` viene utilizzato come delimitatore.
- `HH:mm:ss.sss` -- è l'orario: ore, minuti, secondi e millisecondi.
- La parte opzionale `'Z'` indica il fuso orario nel formato `+-hh:mm`. La singola lettera `Z` rappresenta UTC+0.

Sono disponibili anche varianti più brevi, come `YYYY-MM-DD` o `YYYY-MM` o anche `YYYY`.

La chiamata a `Date.parse(str)` analizza la stringa e ritorna il timestamp (numero di millisecondi trascorsi dal 1 Gennaio 1970). Se il formato non è valido, viene ritornato `NaN`.

Ad esempio:

```js
let ms = Date.parse('2012-01-26T13:51:50.417-07:00');

alert(ms); // 1327611110417  (timestamp)
```

Possiamo utilizzare questo metodo insieme a `new Date` per creare un oggetto dal timestamp:

```js
let date = new Date( Date.parse('2012-01-26T13:51:50.417-07:00') );

alert(date);  
```

## Riepilogo

- Le date e gli orari in JavaScript sono rappresentate dall'oggetto [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date). Non possiamo creare "solo una data" o "solo un orario": l'oggetto `Date` li gestisce entrambi.
- Il conteggio dei mesi parte da zero (Gennaio viene identificato dallo zero).
- Il conteggio dei giorni della settimana in `getDay()` inizia da zero (la Domenica).
- `Date` si auto-corregge quando inseriamo valori fuori dai limiti. Questa caratteristica è fondamentale per sommare/sottrarre giorni/mesi/ore.
- Le date possono essere sottratte, fornendo la loro differenza in millisecondi. Questo è possibile perché `Date` diventa un timestamp quando lo convertiamo al tipo numerico.
- Si utilizza `Date.now()` per ottenere più rapidamente il corrente timestamp.

Da notare che a differenza di molti altri sistemi, in JavaScript il timestamp viene espresso in millisecondi, non in secondi.

Inoltre, talvolta potremmo aver bisogno di misurazioni più precise. JavaScript non permette di gestire i microsecondi (1 milionesimo di secondo), ma molti altri ambienti forniscono questa possibilità. Ad esempio, i browser possiedono [performance.now()](https://developer.mozilla.org/en-US/docs/Web/API/Performance/now) che fornisce il numero di millisecondi a partire dall'inizio del caricamento della pagina con precisione al microsecondo (3 cifre dopo la virgola):

```js
alert(`Loading started ${performance.now()}ms ago`);
// Qualcosa come: "Loading started 34731.26000000001ms ago"
// .26 è microsecondi (260 microsecondi)
// dopo il punto decimale i numeri che seguono il terzo sono errori di precisione, solo i primi tre sono corretti
```

Node.js possiede un modulo `microtime` e altri metodi. Tecnicamente, la maggior parte degli ambienti forniscono un modo per gestire precisioni più elevate, questo non è pero previsto dall'oggetto `Date`.

## Esercizi

### 1 · Creare un oggetto date

Create un oggetto `Date` per la data: Febbraio 20, 2012, 3:12am. Con ora locale.

Mostratela con `alert`.

::::: details Soluzione

Il costruttore `new Date` utilizza l'ora locale di default. Quindi l'unica cosa da ricordare è che il conteggio dei mesi comincia da zero.

Quindi Febbraio è il numero 1.

Qui c'è un esempio con i numeri come componenti della data:

```js
//new Date(anno, mese, data, ora, minuti, secondi, millisecondi)
let d1 = new Date(2012, 1, 20, 3, 12);
alert( d1 );
```
Potremmo anche creare una data da una stringa, così:

```js
//new Date(datastring)
let d2 = new Date("February 20, 2012 03:12:00");
alert( d2 );
```

:::::

### 2 · Mostrare il giorno della settimana

Scrivete una funzione `getWeekDay(date)` per mostrare il giorno della settimana nel formato breve: 'LUN', 'MAR', 'MER', 'GIO', 'VEN', 'SAB', 'DOM'.

Ad esempio:

```js
let date = new Date(2012, 0, 3);  // 3 Gen 2012
alert( getWeekDay(date) );        // dovrebbe mostrare "MAR"
```

::::: details Soluzione

Il metodo `date.getDay()` ritorna il numero del giorno della settimana, cominciando da Domenica.

Creiamo quindi un array con i giorni della settimana, che utilizzeremo per assegnare il numero della settimana al giorno corretto:

```js
function getWeekDay(date) {
  let days = ['DOM', 'LUN', 'MAR', 'MER', 'GIO', 'VEN', 'SAB'];

  return days[date.getDay()];
}

let date = new Date(2014, 0, 3); // 3 Gen 2014
alert( getWeekDay(date) ); // FR
```

:::::

### 3 · Giorno della settimana Europeo

Nel continente europeo i giorni della settimana iniziano con Lunedì (numero 1); segue Martedì (numero 2) e così via fino a Domenica (numero 7). Scrivete una funzione `getLocalDay(date)` che ritorna il giorno della settimana nel formato europeo.

```js
let date = new Date(2012, 0, 3);  // 3 Gen 2012
alert( getLocalDay(date) );       // martedì, dovrebbe mostrare 2
```

::::: details Soluzione



:::::

### 4 · Quale giorno del mese era qualche giorno fa?

Create una funzione `getDateAgo(date, days)` che ritorna il giorno del mese di `days` giorni fa, a partire da `date`.

Ad esempio, se oggi è il 20, allora da `getDateAgo(new Date(), 1)` dovrebbe risultare il 19, e `getDateAgo(new Date(), 2)` dovrebbe ritornare 18.

Dovrebbe funzionare in maniera affidabile anche con `days=365` (o maggiori):

```js
let date = new Date(2015, 0, 2);

alert( getDateAgo(date, 1) ); // 1, (1 Gen 2015)
alert( getDateAgo(date, 2) ); // 31, (31 Dec 2014)
alert( getDateAgo(date, 365) ); // 2, (2 Gen 2014)
```

P.S. La funzione non deve modificare l'oggetto `date`.

::::: details Soluzione

L'idea è semplice: sottrarre il numero di giorni da `date`:

```js
function getDateAgo(date, days) {
  date.setDate(date.getDate() - days);
  return date.getDate();
}
```

...Ma la funzione non dovrebbe modificare l'oggetto `date`. Questo è un aspetto importante, poiché chi ci fornisce l'oggetto non si aspetta cambiamenti.

Per implementarlo correttamente dovremmo clonare l'oggetto, come nel codice seguente:

```js
function getDateAgo(date, days) {
  let dateCopy = new Date(date);

  dateCopy.setDate(date.getDate() - days);
  return dateCopy.getDate();
}

let date = new Date(2015, 0, 2);

alert( getDateAgo(date, 1) ); // 1, (1 Gen 2015)
alert( getDateAgo(date, 2) ); // 31, (31 Dec 2014)
alert( getDateAgo(date, 365) ); // 2, (2 Gen 2014)
```

:::::

### 5 · Ultimo giorno del mese?

Scrivi una funzione `getLastDayOfMonth(year, month)` che ritorna l'ultimo giorno del mese. Potrebbe essere il 30, il 31 o anche 28/29.

Parametri:

- `year` -- anno nel formato 4 cifre, ad esempio 2012.
- `month` -- mese, da 0 a 11.

Ad esempio, `getLastDayOfMonth(2012, 1) = 29` (anno bisestile, Febbraio).

::::: details Soluzione

Creiamo un oggetto `date` con il mese successivo, e come giorno passiamo zero:
```js
function getLastDayOfMonth(year, month) {
  let date = new Date(year, month + 1, 0);
  return date.getDate();
}

alert( getLastDayOfMonth(2012, 0) ); // 31
alert( getLastDayOfMonth(2012, 1) ); // 29
alert( getLastDayOfMonth(2013, 1) ); // 28
```

Formalmente, le date cominciano da 1, ma tecnicamente possiamo passare qualsiasi numero, l'oggetto si aggiusterà automaticamente. Quindi quando gli passiamo 0, allora significherà "il giorno precedente al primo giorno del mese"; in altre parole: "l'ultimo giorno del mese precedente".

:::::

### 6 · Quanti giorni sono passati oggi?

Scrivete una funzione `getSecondsToday()` che ritorna il numero di secondi trascorsi oggi.

Ad esempio, se ora sono le `10:00 am`, senza contare gli spostamenti dovuti all'ora legale, allora:

```js
getSecondsToday() == 36000 // (3600 * 10)
```

La funzione dovrebbe funzionare qualsiasi giorno. In altre parole, non deve esserci alcuna forzatura sul valore del giorno.

::::: details Soluzione

Per ottenere il numero di secondi, possiamo generare una data usando il giorno corrente e il tempo 00:00:00; la differenza rappresenta il tempo trascorso.

La differenza è il numero di millisecondi trascorsi dall'inizio del giorno, che dovremmo poi dividere per 100 per ottenere i secondi:

```js
function getSecondsToday() {
  let now = new Date();

  // crea un oggetto utilizzando il giorno/mese/anno corrente
  let today = new Date(now.getFullYear(), now.getMonth(), now.getDate());

  let diff = now - today; // differenza in ms
  return Math.round(diff / 1000); // converti in secondi
}

alert( getSecondsToday() );
```

Una soluzione alternativa potrebbe essere quella di ottenere ore/minuti/secondi e convertirli tutti in secondi:

```js
function getSecondsToday() {
  let d = new Date();
  return d.getHours() * 3600 + d.getMinutes() * 60 + d.getSeconds();
}

alert( getSecondsToday() );
```

:::::

### 7 · Quanti secondi mancano a domani?

Create una funzione `getSecondsToTomorrow()` che ritorni il numero di secondi mancanti al giorno successivo.

Ad esempio, se ora sono le `23:00`, allora:

```js
getSecondsToTomorrow() == 3600
```

P.S. Anche in questo caso la funzione non dovrebbe forzare il valore del giorno.

::::: details Soluzione

Per ottenere il numero di millisecondi mancanti al giorno successivo, possiamo sottrarre da "domani alle 00:00:00" la data attuale.

Prima generiamo l'oggetto "domani":

```js
function getSecondsToTomorrow() {
  let now = new Date();

  // data di domani
  let tomorrow = new Date(now.getFullYear(), now.getMonth(), now.getDate()+1);

  let diff = tomorrow - now; // differenza in ms
  return Math.round(diff / 1000); // converti in seconds
}
```

Soluzione alternativa:

```js
function getSecondsToTomorrow() {
  let now = new Date();
  let hour = now.getHours();
  let minutes = now.getMinutes();
  let seconds = now.getSeconds();
  let totalSecondsToday = (hour * 60 + minutes) * 60 + seconds;
  let totalSecondsInADay = 86400;

  return totalSecondsInADay - totalSecondsToday;
}
```

Da notare che molti stati potrebbero sottostare a DST, quindi alcuni giorni potrebbero durare 23 ore mentre altri 25. Vorremmo trattare queste situazioni separatamente.

:::::

### 8 · Formattare la data

Scrivete una funzione `formatDate(date)` che dovrebbe formattare `date` come segue:

- Se da `date` è passato meno di un secondo, allora ritorna `"right now"`.
- Altrimenti, se da `date` è passato meno di un minuto, allora ritorna `"n sec. ago"`.
- Altrimenti, se è passata meno di un'ora, ritorna `"m min. ago"`.
- Altrimenti, l'intera data nel formato `"DD.MM.YY HH:mm"`. Ovvero: `"day.month.year hours:minutes"`, tutto nel formato due cifre, ad esempio `31.12.16 10:00`.

Un esempio:

```js
alert( formatDate(new Date(new Date - 1)) ); // "right now"

alert( formatDate(new Date(new Date - 30 * 1000)) ); // "30 sec. ago"

alert( formatDate(new Date(new Date - 5 * 60 * 1000)) ); // "5 min. ago"

// la data di ieri, come: 31.12.16 20:00
alert( formatDate(new Date(new Date - 86400 * 1000)) );
```

::::: details Soluzione

Per ottenere il tempo passato da `date` fino ad ora -- sottraiamo le date.

```js
function formatDate(date) {
  let diff = new Date() - date; // la differenza in millisecondi

  if (diff < 1000) { // less than 1 second
    return 'right now';
  }

  let sec = Math.floor(diff / 1000); // converti diff in secondi

  if (sec < 60) {
    return sec + ' sec. ago';
  }

  let min = Math.floor(diff / 60000); // converti diff in minuti
  if (min < 60) {
    return min + ' min. ago';
  }

  // formatta la data
  // aggiungi gli zero a day/month/hours/minutes
  let d = date;
  d = [
    '0' + d.getDate(),
    '0' + (d.getMonth() + 1),
    '' + d.getFullYear(),
    '0' + d.getHours(),
    '0' + d.getMinutes()
  ].map(component => component.slice(-2)); // prendi gli ultimi 2 numeri da ogni componente

  // unisci i componenti in una data
  return d.slice(0, 3).join('.') + ' ' + d.slice(3).join(':');
}

alert( formatDate(new Date(new Date - 1)) ); // "right now"

alert( formatDate(new Date(new Date - 30 * 1000)) ); // "30 sec. ago"

alert( formatDate(new Date(new Date - 5 * 60 * 1000)) ); // "5 min. ago"

// la data di ieri come: 31.12.2016 20:00
alert( formatDate(new Date(new Date - 86400 * 1000)) );
```

Soluzione alternativa:

```js
function formatDate(date) {
  let dayOfMonth = date.getDate();
  let month = date.getMonth() + 1;
  let year = date.getFullYear();
  let hour = date.getHours();
  let minutes = date.getMinutes();
  let diffMs = new Date() - date;
  let diffSec = Math.round(diffMs / 1000);
  let diffMin = diffSec / 60;
  let diffHour = diffMin / 60;

  // formatta
  year = year.toString().slice(-2);
  month = month < 10 ? '0' + month : month;
  dayOfMonth = dayOfMonth < 10 ? '0' + dayOfMonth : dayOfMonth;
  hour = hour < 10 ? '0' + hour : hour;
  minutes = minutes < 10 ? '0' + minutes : minutes;

  if (diffSec < 1) {
    return 'right now';  
  } else if (diffMin < 1) {
    return `${diffSec} sec. ago`
  } else if (diffHour < 1) {
    return `${diffMin} min. ago`
  } else {
    return `${dayOfMonth}.${month}.${year} ${hour}:${minutes}`
  }
}
```

:::::

