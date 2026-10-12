# Learning

Un percorso pratico in italiano per costruire una base **frontend e backend**: HTML → CSS → JavaScript → TypeScript → HTTP e Node.js → SQL e PostgreSQL → applicazione completa → un framework frontend → Rust.
Il sito è realizzato con VitePress nella cartella `project`.

Sito: [learning-web-rust.pages.dev](https://learning-web-rust.pages.dev).
Inizia da [La prima pagina HTML](https://learning-web-rust.pages.dev/html/prima-pagina).

## Contenuti

Sono disponibili [26 lezioni HTML](https://learning-web-rust.pages.dev/html/), [35 lezioni CSS](https://learning-web-rust.pages.dev/css/) e [175 articoli JavaScript.info in italiano](https://learning-web-rust.pages.dev/javascript/indice), con 252 esercizi e le soluzioni disponibili. La [roadmap](https://learning-web-rust.pages.dev/percorso) definisce obiettivi, progetti e punti di controllo per le tappe successive.

I contenuti JavaScript sono di Ilya Kantor e dei contributori del tutorial e dell'edizione italiana. Attribuzione, modifiche e licenze sono in [`project/docs/javascript/fonti.md`](project/docs/javascript/fonti.md). I contenuti importati sono destinati all'uso non commerciale secondo le condizioni delle fonti.

## Audit e copertura HTML/CSS

HTML include un inventario WHATWG del 12 ottobre 2026: 113 elementi nominati, 144 nomi di attributi / 180 contesti e 89 attributi gestori di eventi. La copertura al 100% riguarda il catalogo dello snapshot, non tutte le API o la padronanza del lettore. CSS mappa i 37 moduli didattici di Google Learn CSS, con lezioni aggiuntive; non pretende di riscrivere ogni proprietà CSS. Le pagine Copertura e Fonti documentano metodi e limiti.

Per verificare gli inventari, la struttura delle lezioni e la mappa del programma:

```bash
python3 project/scripts/check-curriculum.py
```

Il controllo gira anche nella CI. Per rigenerare i riferimenti HTML dallo snapshot e dalle descrizioni curate:

```bash
python3 project/scripts/build-html-reference.py
```

Le soluzioni autonome sono in `project/docs/public/esempi/laboratorio-html.html`, `laboratorio-css.html` e `laboratorio-css.css`.

## Importazione di JavaScript.info

Lo snapshot usa i repository ufficiali inglese e italiano, con quattro traduzioni/adattamenti aggiunti in `project/sources/javascript-info/translations`. Le revisioni delle fonti sono documentate nella pagina Fonti e licenza. Non è stata eseguita una revisione tecnica completa di tutti gli articoli italiani.

Per rigenerare i capitoli da checkout locali delle medesime revisioni:

```bash
python project/scripts/import-javascript-info.py \
  --italian /percorso/it.javascript.info \
  --english /percorso/en.javascript.info
npm run docs:build --prefix project
```

Il manifest registra le fonti dei capitoli e l'impronta dei testi. I blocchi di codice rimangono esempi da copiare; le demo che richiedono il renderer di JavaScript.info rimandano alla fonte originale.

## Sviluppo locale

Usa Node.js 22 o superiore (Node.js 24 è la versione usata dalla CI).

```bash
cd project
npm ci
npm run docs:dev
```

Apri l'indirizzo indicato nel terminale. Modifica i file Markdown in `project/docs`: il browser si aggiorna automaticamente.

## Build e anteprima

```bash
cd project
npm run docs:build
npm run docs:preview
```

L'output pubblicabile è `project/docs/.vitepress/dist`. La build verifica anche i collegamenti interni della documentazione.

## GitHub e Cloudflare Pages

Repository: <https://github.com/ritchiemarkov/learning>.

Configurazione del progetto Cloudflare Pages `learning-web-rust`:

| Impostazione | Valore |
| --- | --- |
| Repository | `ritchiemarkov/learning` |
| Branch di produzione | `main` |
| Root directory | `project` |
| Build command | `npm run docs:build` |
| Build output directory | `docs/.vitepress/dist` |
| Variabile di build | `NODE_VERSION=24` |

L'integrazione Git di Pages pubblica gli aggiornamenti di `main`. Il workflow GitHub Actions verifica la build sui push e sulle pull request; il deploy è gestito da Cloudflare, senza token Cloudflare nel repository.

Per un deploy manuale, dopo l'autenticazione personale:

```bash
cd project
npx wrangler login
npm run deploy
```

Il file `wrangler.jsonc` descrive il progetto Pages e la directory da pubblicare.

## Struttura

```text
project/
├── package.json
├── package-lock.json
├── wrangler.jsonc
└── docs/
    ├── .vitepress/     # Configurazione e tema
    ├── index.md        # Home
    ├── percorso.md     # Metodo e roadmap
    ├── html/           # Lezioni ed esercizi
    ├── css/            # 15 basi, 20 approfondimenti e soluzioni
    ├── javascript/     # Tutorial JavaScript.info completo
    ├── typescript/     # Tipi dopo JavaScript
    ├── backend/        # HTTP, API e Node.js
    ├── database/       # SQL e PostgreSQL
    ├── fullstack/      # Integrazione, sicurezza, test e deploy
    ├── frontend/       # Framework dopo le basi
    ├── rust/           # Prossima tappa
    └── public/esempi/  # Documenti HTML autonomi
```

## Dipendenze

VitePress è fissato alla versione stabile 1.6.4. L'override di Vite a 6.4.4 evita le vulnerabilità segnalate da `npm audit` nella versione transitiva di Vite 5. La build va verificata quando si aggiornano queste dipendenze.

## Riferimenti

- [VitePress: guida](https://vitepress.dev/guide/getting-started)
- [MDN: strutturare contenuti con HTML](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content)
- [Cloudflare Pages: configurazione della build](https://developers.cloudflare.com/pages/configuration/build-configuration/)
