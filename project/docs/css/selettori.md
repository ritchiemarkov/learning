# 02 · Selettori e combinatori

**Obiettivo:** selezionare il contenuto voluto senza dipendere da una struttura fragile.

## I selettori più comuni

| Selettore | Cosa seleziona |
| --- | --- |
| `p` | Elementi p |
| `.scheda` | Elementi con la classe scheda |
| `#contenuto` | Elemento con quell'ID |
| `*` | Tutti gli elementi nel contesto |
| `[required]` | Elementi con l'attributo required |
| `[type="email"]` | Attributo con quel valore |
| `.scheda p` | Paragrafi discendenti, anche a più livelli |
| `.scheda > p` | Paragrafi figli diretti |
| `h2 + p` | Paragrafo fratello immediatamente successivo a h2 |
| `h2 ~ p` | Paragrafi fratelli successivi a h2 |

```html
<article class="scheda">
  <h2>Corso HTML</h2>
  <p>Introduzione.</p>
  <div><p>Approfondimento.</p></div>
</article>
```
```css
.scheda > p { color: #17634d; }
.scheda h2 { margin-block-end: 0.5rem; }
```

La prima regola colora solo «Introduzione». Lo spazio e `>` non sono intercambiabili: il loro significato dipende dall'albero DOM.

## Liste e attributi

Una virgola unisce selettori indipendenti: `h1, h2` sceglie entrambi. `.scheda.evidenza` richiede entrambe le classi sullo stesso elemento; `.scheda .evidenza` cerca invece un discendente.

Gli operatori degli attributi includono `~=`, per un token di una lista, `^=` inizio, `$=` fine, `*=` sottostringa e `|=` valore o prefisso seguito da trattino. I flag `i` e `s` riguardano confronti di maiuscole nei contesti previsti. Un link che finisce con `.pdf` è solo un indizio sull'URL, non una verifica del MIME.

Le pseudoclassi, come `:hover`, selezionano stati; gli pseudoelementi, come `::before`, selezionano parti o contenuto generato. Li useremo nelle lezioni sugli stati e sui [selettori avanzati](/css/selettori-avanzati).

## Classi che descrivono un componente

Preferisci una classe stabile a selettori lunghi come `body main section div p`. Cambiare un contenitore non dovrebbe rompere una scheda. Gli ID sono utili per ancore e relazioni HTML; in CSS aumentano la specificità e rendono più costose le sovrascritture.

## Esercizio

Nel frammento aggiungi un secondo articolo. Colora tutti i suoi paragrafi, ma nel primo articolo solo il paragrafo figlio diretto.

::: details Soluzione
```html
<article class="scheda estesa"><h2>CSS</h2><div><p>Layout.</p></div></article>
```
```css
.scheda > p { color: #17634d; }
.scheda.estesa p { color: #245b8a; }
```
In DevTools controlla quale selettore corrisponde a ciascun paragrafo. Non aggiungere `!important` per correggere una selezione sbagliata.
:::

Fonti: [Google/web.dev · Selettori](https://web.dev/learn/css/selectors), [MDN · Selettori CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_selectors).
