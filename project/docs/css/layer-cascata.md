# 17 · Layer e controllo della cascata

**Obiettivo:** organizzare le priorità senza aumentare continuamente la specificità.

## Dichiarare un ordine

```css
@layer base, componenti, utilita;
@layer base { h2 { color: #17382d; } }
@layer componenti { .scheda h2 { color: #17634d; } }
@layer utilita { .evidenza { color: #245b8a; } }
```

Fra dichiarazioni normali dell'autore, il layer successivo prevale sul precedente prima di confrontare la specificità. Un titolo con classe evidenza diventa blu anche se il selettore nel layer componenti ha più tipi. Le dichiarazioni normali fuori dai layer hanno una priorità superiore a quelle dentro i layer della stessa origine.

Con `!important` l'ordine dei layer si inverte: i primi layer importanti prevalgono e le dichiarazioni importanti nei layer precedono quelle importanti senza layer. Anche l'ordine fra origini cambia per le dichiarazioni importanti. Questa è una ragione per progettare i layer senza usarli come semplice «ultima regola vince».

## Origini e valori globali

La cascata comprende autore, utente, user agent, animazioni e transizioni secondo priorità precise. Un'impostazione importante dell'utente può prevalere su una importante dell'autore; le transizioni attive hanno un trattamento particolarmente alto. Gli stili inline mantengono regole proprie. Consulta la tabella normativa prima di attribuire tutto alla specificità.

`revert` torna attraverso l'origine pertinente; `revert-layer` ripristina il risultato al di fuori del layer corrente secondo le regole previste. `initial` e `unset` non significano «ripristina lo stile del browser» in ogni caso.

## Stili esterni e manutenzione

```css
@layer libreria, applicazione;
@import url("libreria.css") layer(libreria);
@layer applicazione { .pulsante { border-radius: 0.5rem; } }
```

L'import deve rispettare la posizione prevista nella grammatica del foglio. Importare una libreria in un layer separa la sua priorità; il file deve esistere e la catena di richieste va misurata. In un progetto reale un processo di build può organizzare risorse senza creare ulteriori import di rete.

Un reset va limitato a scelte comprese. Azzerare tutto con `all: unset` può rimuovere indicatori e presentazione utile dei controlli. Scrivi componenti con selettori semplici e proprietà ereditabili ragionate.

## Esercizio

Metti un selettore con ID nel layer base e una classe nel layer utilita, entrambi normali, per il colore dello stesso elemento.

::: details Soluzione
Con l'ordine dichiarato sopra vince la classe del layer utilita, perché il confronto dei layer precede la specificità. Aggiungendo una dichiarazione normale senza layer, questa può prevalere. Conferma in DevTools il layer della dichiarazione, non solo il selettore.
:::

Fonti: [MDN · layer](https://developer.mozilla.org/en-US/docs/Web/CSS/@layer), [MDN · Cascata](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_cascade/Cascade), [W3C · Cascade](https://www.w3.org/TR/css-cascade-5/).
