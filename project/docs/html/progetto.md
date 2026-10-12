# 07 · Progetto: la tua pagina personale

**Obiettivo:** costruire una pagina senza copiare un documento già completo. Dedica circa 45 minuti, anche divisi in più sessioni.

## Esercizio · La consegna

Crea `profilo.html` con:

1. Struttura completa: doctype, lingua italiana, codifica, viewport e titolo della scheda.
2. Un'intestazione con il nome del sito e una navigazione interna.
3. Un contenuto principale con un `<h1>` e le sezioni «Chi sono», «Interessi» e «Come studio».
4. Una lista non ordinata degli interessi e una lista ordinata dei passaggi di studio.
5. Un link alla documentazione MDN.
6. Un piè di pagina con una breve nota sul progetto.

Se hai una tua foto, puoi aggiungerla con un testo alternativo adatto. Come estensione, crea una seconda pagina con il form della lezione precedente, usando dati inventati.

## Prima di guardare la soluzione

Apri la pagina e controlla:

- [ ] La scheda ha un titolo utile e gli accenti si leggono correttamente.
- [ ] C'è una gerarchia chiara fra titolo principale e sezioni.
- [ ] Ogni collegamento interno raggiunge la sezione giusta.
- [ ] I collegamenti si possono raggiungere e attivare con la tastiera.
- [ ] Ogni immagine ha un attributo `alt` scelto in base al suo ruolo.
- [ ] Gli eventuali controlli del form hanno un'etichetta.

Puoi verificare il file con il [validatore HTML del W3C](https://validator.w3.org/nu/), usando «file upload» o «text input». Leggi il primo errore, correggilo e riprova. La validazione controlla il markup: l'accessibilità richiede anche verifiche come quelle sopra.

::: details Una possibile soluzione
```html
<!doctype html>
<html lang="it">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Alex · Il mio quaderno</title>
  </head>
  <body>
    <header>
      <p>Il mio quaderno</p>
      <nav aria-label="Principale">
        <a href="#chi-sono">Chi sono</a>
        <a href="#interessi">Interessi</a>
        <a href="#studio">Come studio</a>
      </nav>
    </header>
    <main>
      <h1>Ciao, sono Alex</h1>
      <section id="chi-sono">
        <h2>Chi sono</h2>
        <p>Sto imparando HTML per costruire la mia prima pagina web.</p>
      </section>
      <section id="interessi">
        <h2>Interessi</h2>
        <ul>
          <li>Fotografia</li>
          <li>Musica</li>
          <li>Programmazione</li>
        </ul>
      </section>
      <section id="studio">
        <h2>Come studio</h2>
        <ol>
          <li>Leggo una lezione.</li>
          <li>Scrivo un esempio.</li>
          <li>Provo a modificarlo.</li>
        </ol>
        <p>Approfondisco con la <a href="https://developer.mozilla.org/en-US/docs/Web/HTML">documentazione HTML di MDN</a>.</p>
      </section>
    </main>
    <footer>
      <p>Una pagina realizzata per imparare HTML.</p>
    </footer>
  </body>
</html>
```
:::

[Apri la soluzione nel browser](/esempi/profilo.html) per vedere come appare una pagina HTML senza CSS.

## Racconta ciò che hai costruito

Sai spiegare perché hai usato `<nav>`, perché «Come studio» usa una lista ordinata e quale differenza c'è fra `<title>` e `<h1>`? Se sì, abbiamo una buona base per [iniziare CSS](/css/).

Fonti: [Nu HTML Checker](https://validator.w3.org/nu/).
