# 05 · HTML semantico

**Obiettivo:** scegliere gli elementi in base alla funzione dei contenuti.

## Una pagina riconoscibile

```html
<body>
  <header>
    <p>Il quaderno di Alex</p>
    <nav aria-label="Principale">
      <a href="#chi-sono">Chi sono</a>
      <a href="#progetti">Progetti</a>
    </nav>
  </header>

  <main>
    <h1>Imparo a costruire sul web</h1>
    <section id="chi-sono">
      <h2>Chi sono</h2>
      <p>Sto studiando HTML, un esempio alla volta.</p>
    </section>
    <section id="progetti">
      <h2>I miei progetti</h2>
      <article>
        <h3>La prima pagina</h3>
        <p>Una piccola presentazione personale.</p>
      </article>
    </section>
  </main>

  <footer>
    <p>Creato per esercitarmi con HTML.</p>
  </footer>
</body>
```

## Che elemento scelgo?

| Elemento | Quando usarlo |
| --- | --- |
| `<header>` | Introduzione alla pagina o a una sezione |
| `<nav>` | Un gruppo importante di collegamenti di navigazione |
| `<main>` | Il contenuto principale della pagina; per i nostri documenti ne usiamo uno |
| `<section>` | Un gruppo tematico di contenuti, di norma con un titolo |
| `<article>` | Contenuto autonomo, come un post o una scheda che ha senso da sola |
| `<aside>` | Informazioni collegate ma secondarie |
| `<footer>` | Informazioni di chiusura della pagina o di una sezione |
| `<div>` | Un contenitore generico quando non serve un significato specifico |

Non serve riempire ogni pagina con tutti questi elementi. Parti dai contenuti e scegli ciò che li descrive.

## Accessibilità come parte della struttura

Titoli, regioni e link descrittivi aiutano a orientarsi. Gli elementi nativi portano anche comportamenti utili: un `<button>` risponde alla tastiera, mentre una `<div>` da sola non è un pulsante.

Regola pratica: **link per navigare, pulsanti per compiere azioni**. Preferisci gli elementi HTML adatti prima di aggiungere attributi ARIA.

## Esercizio

Riorganizza la tua pagina personale con un'intestazione, una navigazione, un contenuto principale con due sezioni e un piè di pagina. Poi premi `Tab` più volte: riesci a raggiungere ogni link? Premi `Invio` su un link: si apre la destinazione prevista?

::: details Come verificare
Confronta la struttura con l'esempio. Controlla che ogni `href="#..."` abbia un `id` corrispondente e che le sezioni abbiano un titolo. Non scegliere `<article>` solo per avere un riquadro: il riquadro sarà una scelta CSS.
:::
