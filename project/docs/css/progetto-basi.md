# 15 · Progetto delle basi CSS

**Obiettivo:** rendere responsive il sito di laboratori costruito con HTML.

## Il risultato da ottenere

Parti dal [laboratorio HTML](/esempi/laboratorio-html.html). Crea un foglio esterno e una classe contenitore per header, main e footer. Il progetto deve avere testo leggibile, schede, tabella e form con focus visibile. Non serve un framework CSS.

| Requisito | Criterio di verifica |
| --- | --- |
| Cascata comprensibile | Sai spiegare in DevTools la regola che colora un titolo |
| Box model | Padding e bordo non producono overflow inatteso |
| Tipografia | Testo ingrandito e URL lunghi restano leggibili |
| Layout | Le schede passano a più colonne soltanto quando trovano spazio |
| Immagini | Nessuna deformazione o larghezza superiore al contenitore |
| Form | Label leggibili, controlli utilizzabili, errori anche testuali |
| Focus | Tutti i controlli si possono raggiungere e riconoscere |
| Responsive | Niente contenuti tagliati a 320px e alle larghezze intermedie |

## Esercizio

Realizza il progetto prima di guardare la soluzione. Usa una scala di spazi, limita la larghezza della prosa e organizza il gruppo di schede con grid. Mantieni l'ordine DOM.

::: details Una possibile soluzione di base
```css
*, *::before, *::after { box-sizing: border-box; }
body { margin: 0; font: 1rem/1.6 system-ui, sans-serif; color: #17382d; background: #f4f8f5; }
.contenitore { width: min(100% - 2rem, 70rem); margin-inline: auto; }
header, main, footer { padding-block: 2rem; }
h1, h2, h3 { line-height: 1.2; }
.schede { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 16rem), 1fr)); gap: 1rem; }
.scheda { background: white; border: 1px solid #b9ccc3; border-radius: 0.75rem; padding: 1.5rem; }
img { max-inline-size: 100%; block-size: auto; }
a { color: #155b8a; text-underline-offset: 0.2em; }
button, input, select, textarea { font: inherit; }
:focus-visible { outline: 3px solid #245b8a; outline-offset: 3px; }
```
Le classi vanno aggiunte agli elementi HTML pertinenti. Completa regole per tabella e form usando la lezione 14. La soluzione completa è disponibile nel [laboratorio CSS](/css/laboratorio-completo).
:::

## Verifica senza scorciatoie

Prima controlla il file caricato in Network, poi selettori e valori. Non correggere ogni conflitto con important né ogni contenuto fuori posto con position absolute. Se un contenuto è tagliato, controlla dimensioni minime, overflow, parole indivisibili e altezze fisse.

Prova la pagina con Tab, zoom e testo più lungo. Una pagina che funziona solo con il testo dell'esempio non ha ancora superato l'esercizio. Salva le modifiche osservate in DevTools nel file sorgente e documenta una correzione che hai compreso.

Puoi iniziare [JavaScript](/javascript/) quando sai completare questi requisiti. Gli approfondimenti CSS rimangono disponibili durante i progetti successivi: non è necessario conoscere ogni effetto grafico prima di aggiungere un evento.

Fonte per i criteri del percorso: [MDN · CSS layout](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout).
