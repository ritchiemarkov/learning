# Learning

Un percorso pratico in italiano: **HTML → CSS → JavaScript → Rust**.
Il sito è realizzato con VitePress nella cartella `project`.

Sito: [learning-web-rust.pages.dev](https://learning-web-rust.pages.dev).
Inizia da [La prima pagina HTML](https://learning-web-rust.pages.dev/html/prima-pagina).

## Contenuti

Sono disponibili sette lezioni HTML con esercizi, soluzioni e due esempi HTML apribili nel browser. CSS, JavaScript e Rust hanno una roadmap: le lezioni verranno aggiunte durante il percorso.

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
    ├── css/            # Prossima tappa
    ├── javascript/     # Prossima tappa
    ├── rust/           # Prossima tappa
    └── public/esempi/  # Documenti HTML autonomi
```

## Dipendenze

VitePress è fissato alla versione stabile 1.6.4. L'override di Vite a 6.4.4 evita le vulnerabilità segnalate da `npm audit` nella versione transitiva di Vite 5. La build va verificata quando si aggiornano queste dipendenze.

## Riferimenti

- [VitePress: guida](https://vitepress.dev/guide/getting-started)
- [MDN: strutturare contenuti con HTML](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content)
- [Cloudflare Pages: configurazione della build](https://developers.cloudflare.com/pages/configuration/build-configuration/)
