---
title: "Alternanza (OR) |"
description: "JavaScript.info in italiano: Alternanza (OR) |"
sourceTutorial: true
prev: {"text": "Riferimenti all'indietro (backreference) nei pattern: \\N e \\kname", "link": "/javascript/tutorial/regexp-backreferences"}
next: {"text": "Lookahead e lookbehind", "link": "/javascript/tutorial/regexp-lookahead-lookbehind"}
---

# Alternanza (OR) |

> **JavaScript.info · Ilya Kantor e contributori.** [Originale inglese](https://javascript.info/regexp-alternation) · [Edizione italiana](https://it.javascript.info/regexp-alternation) · [Fonti e licenza](/javascript/fonti).

Alternanza è un termine usato nelle espressioni regolari che, in realtà, consiste in un semplice "OR".

È indicata con un carattere di linea verticale `|`.

Supponiamo di aver bisogno di trovare il nome di un linguaggio di programmazione: HTML, PHP, Java o JavaScript.

Ecco la regexp corrispondente: `html|php|java(script)?`.

Ed ora un esempio d'uso:

```js
let regexp = /html|php|css|java(script)?/gi;

let str = "First HTML appeared, then CSS, then JavaScript";

alert( str.match(regexp) ); // 'HTML', 'CSS', 'JavaScript'
```

Abbiamo già incontrato una funzionalità simile: le parentesi quadre. Essi permettono di scegliere tra più caratteri, ad esempio `gr[ae]y` trova corrispondenza con `gray` o `grey`.

Le parentesi quadre consentono solo caratteri o classi di caratteri. L'alternanza consente qualsiasi espressione. Una regexp `A|B|C` significa una delle espressioni `A`, `B` o `C`.

Per esempio:

- `gr(a|e)y` ha lo stesso identico significato di `gr[ae]y`.
- `gra|ey` significa `gra` o `ey`.

Per applicare l'alternanza ad una determinata parte di un pattern, dobbiamo racchiuderla tra parentesi:
- `I love HTML|CSS` trova `I love HTML` o `CSS`.
- `I love (HTML|CSS)` corrisponde a `I love HTML` o `I love CSS`.

## Esempio: regexp per un orario

Negli articoli precedenti abbiamo effettuato un'esercitazione per realizzare una regexp e trovare un orario nel formato `hh:mm`, ad esempio `12:00`. Un semplice `\d\d:\d\d`, tuttavia, è troppo impreciso. Accetta un orario come `25:99` (poiché 99 minuti trova corrispondenza nel pattern, ma non è un orario valido).

Come possiamo migliorare questo pattern?

Possiamo cercare una corrispondenza più accurata. Per prima cosa, le ore:

- Se la prima cifra è `0` o `1`, allora la cifra successiva può essere una qualsiasi: `[01]\d`.
- Diversamente, se la prima cifra è `2`, la successiva deve essere `[0-3]`.
- Non può esserci un altro carattere come prima cifra.

Possiamo scrivere entrambe le varianti in una regexp usando l'alternanza: `[01]\d|2[0-3]`.

I minuti a seguire, essi devono essere compresi in un intervallo tra `00` e `59`. In un'espressione regolare ciò può essere reso come `[0-5]\d`: la prima cifra `0-5`, quindi un numero qualsiasi.

Unendo le ore con i minuti otteniamo il pattern seguente: `[01]\d|2[0-3]:[0-5]\d`.

Abbiamo quasi finito, ma c'è ancora un problema. L'alternanza `|` al momento sembra avvenire tra `[01]\d` e `2[0-3]:[0-5]\d`.

In altre parole: i minuti sono aggiunti al secondo termine dell'alternanza, ecco una rappresentazione più chiara:

```
[01]\d  |  2[0-3]:[0-5]\d
```

Questo pattern cerca `[01]\d` o `2[0-3]:[0-5]\d`.

Non è quello che vogliamo, l'alternanza dovrebbe riguardare solo le ore e consentire `[01]\d` o `2[0-3]`. Correggiamo racchiudendo le ore tra parentesi: `([01]\d|2[0-3]):[0-5]\d`.

Ed ecco la soluzione definitiva:

```js
let regexp = /([01]\d|2[0-3]):[0-5]\d/g;

alert("00:00 10:10 23:59 25:99 1:2".match(regexp)); // 00:00,10:10,23:59
```

## Esercizi

### 1 · Trovate il nome dei linguaggi di programmazione

Ci sono molti linguaggi di programmazione, Per esempio Java, JavaScript, PHP, C, C++.

Create una regexp che li trovi nella stringa `Java JavaScript PHP C++ C`:

```js
let regexp = /your regexp/g;

alert("Java JavaScript PHP C++ C".match(regexp)); // Java JavaScript PHP C++ C
```

::::: details Soluzione

La prima idea potrebbe essere elencare i linguaggi separati da `|`.

Ma non funziona bene:

```js
let regexp = /Java|JavaScript|PHP|C|C\+\+/g;

let str = "Java, JavaScript, PHP, C, C++";

alert( str.match(regexp) ); // Java,Java,PHP,C,C
```

L'interprete dell'espressione regolare cerca le alternanze una per una. In altre parole: per prima cosa cerca `Java`, se non la trova cerca `JavaScript` e così via.

Il risultato è che `JavaScript` non trova mai corrispondenza proprio perché `Java` viene controllato per prima.

Lo stesso accade con `C` e `C++`.

Ci sono due soluzioni per questo problema:

1. Cambiare l'ordine di verifica mettendo per primo il termine più lungo: `JavaScript|Java|C\+\+|C|PHP`.
2. Unire le varianti che cominciano allo stesso modo: `Java(Script)?|C(\+\+)?|PHP`.

In azione:

```js
let regexp = /Java(Script)?|C(\+\+)?|PHP/g;

let str = "Java, JavaScript, PHP, C, C++";

alert( str.match(regexp) ); // Java,JavaScript,PHP,C,C++
```

:::::

### 2 · Trovate le coppie di bbtag

Un "bb-tag" si presenta così `[tag]...[/tag]`, in cui `tag` è uno tra: `b`, `url` o `quote`.

Ad esempio:
```
[b]text[/b]
[url]http://google.com[/url]
```

I BB-tags possono essere annidati. Un tag, tuttavia, non può essere contenuto all'interno di uno dello stesso tipo, ad esempio:

```
Normale:
[url] [b]http://google.com[/b] [/url]
[quote] [b]text[/b] [/quote]

Non deve verificarsi:
[b][b]text[/b][/b]
```

I tag possono contenere interruzioni di linea, questo è del tutto normale:

```
[quote]
  [b]text[/b]
[/quote]
```

Create una regexp per trovare tutti i BB-tags con il loro contenuto.

Per esempio:

```js
let regexp = /your regexp/flags;

let str = "..[url]http://google.com[/url]..";
alert( str.match(regexp) ); // [url]http://google.com[/url]
```

In caso di tag annidati ci occorre il tag esterno (se lo desideriamo possiamo continuare la ricerca nel contenuto appena ricavato):

```js
let regexp = /your regexp/flags;

let str = "..[url][b]http://google.com[/b][/url]..";
alert( str.match(regexp) ); // [url][b]http://google.com[/b][/url]
```

::::: details Soluzione

Il tag di apertura è `\[(b|url|quote)\]`.

Successivamente per trovare tutto fino al tag di chiusura usiamo il pattern `.*?` con il flag `s` per cercare la corrispondenza con ogni carattere inclusa una nuova riga. Per concludere aggiungiamo un riferimento all'indietro per il tag di chiusura.

L'intero pattern risultante è: `\[(b|url|quote)\].*?\[/\1\]`.

In azione:

```js
let regexp = /\[(b|url|quote)].*?\[\/\1]/gs;

let str = `
  [b]hello![/b]
  [quote]
    [url]http://google.com[/url]
  [/quote]
`;

alert( str.match(regexp) ); // [b]hello![/b],[quote][url]http://google.com[/url][/quote]
```

Si noti che oltre l'escape di `[` e `]`, abbiamo dovuto fare l'escape dello slash del tag di chiusura `[\/\1]`, poiché normalmente lo slash termina il pattern.

:::::

### 3 · Trovate le stringhe tra doppi apici

Create una regexp per trovare le stringhe tra doppi apici `"..."`.

Le stringhe dovrebbero supportare l'escape allo stesso modo delle stringhe JavaScript. Per esempio, i doppi apici possono essere inseriti come `\"` una nuova linea come `\n`, e lo stesso slash come `\\`.

```js
let str = "Just like \"here\".";
```

Si noti che, in particolare, un doppio apice con escape `\"` non termina una stringa.

Noi dovremmo cercare, pertanto, da un doppio apice fino all'altro ignorando quelli con escape tra i due.

Questo è la parte fondamentale dell'esercitazione, altrimenti diventerebbe banale.

Ecco degli esempi di stringhe che corrispondono:
```js
.. "test me" ..  
.. "Say \"Hello\"!" ... (contiene doppi apici con escape)
.. "\\" ..  (contiene un doppio slash)
.. "\\ \"" ..  (contiene un doppio slash e un doppio apice con escape)
```

In JavaScript abbiamo bisogno di raddoppiare lo slash per passarli correttamente all'interno della stringa, in questo modo:

```js
let str = ' .. "test me" .. "Say \\"Hello\\"!" .. "\\\\ \\"" .. ';

// la stringa in memoria
alert(str); //  .. "test me" .. "Say \"Hello\"!" .. "\\ \"" ..
```

::::: details Soluzione

La soluzione: `/"(\\.|[^"\\])*"/g`.

Passo dopo passo:

- Innanzitutto cerchiamo un doppio apice di apertura `"`
- Quindi se abbiamo un backslash `\\` (dobbiamo raddoppiarlo nel pattern perché è un carattere speciale), qualsiasi carattere dopo di esso è consentito (il punto).
- Altrimenti consideriamo ogni carattere eccetto un doppio apice (che significherebbe la fine della stringa) ed un backslash (per evitare backslashe isolati, il backslash è usato soltanto in congiunzione con altri simboli dopo di esso): `[^"\\]`
- ...e così via fino al doppio apice di chiusura.

In azione:

```js
let regexp = /"(\\.|[^"\\])*"/g;
let str = ' .. "test me" .. "Say \\"Hello\\"!" .. "\\\\ \\"" .. ';

alert( str.match(regexp) ); // "test me","Say \"Hello\"!","\\ \""
```

:::::

### 4 · Trovate l'intero tag

Scrivete una regexp per trovare il tag `<style...>`. Essa dovrebbe trovare corrispondenza con l'intero tag: esso potrebbe non avere alcun attributo `<style>` o averne diversi `<style type="..." id="...">`.

La regexp, tuttavia, non dobrebbe accettare `<styler>`!

Per esempio:

```js
let regexp = /your regexp/g;

alert( '<style> <styler> <style test="...">'.match(regexp) ); // <style>, <style test="...">
```

::::: details Soluzione

L'inizio del pattern è ovvio: `<style`.

Ma successivamente non possiamo semplicemente scrivere `<style.*?>`, poiché altrimenti `<styler>` troverebbe corrispondenza.

Abbiamo bisogno di uno spazio dopo `<style` e dopo facoltativamente qualcos'altro o la `>` finale.

Tradotto nel linguaggio delle regexp: `<style(>|\s.*?>)`.

In azione:

```js
let regexp = /<style(>|\s.*?>)/g;

alert( '<style> <styler> <style test="...">'.match(regexp) ); // <style>, <style test="...">
```

:::::

