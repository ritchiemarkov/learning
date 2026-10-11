import { defineConfig } from 'vitepress'

const html = [
  { text: 'Da dove iniziare', link: '/html/' },
  { text: '01 · La prima pagina', link: '/html/prima-pagina' },
  { text: '02 · Elementi e attributi', link: '/html/elementi-attributi' },
  { text: '03 · Testo e liste', link: '/html/testo-liste' },
  { text: '04 · Link e immagini', link: '/html/link-immagini' },
  { text: '05 · HTML semantico', link: '/html/semantica' },
  { text: '06 · Form accessibili', link: '/html/form' },
  { text: '07 · Il progetto finale', link: '/html/progetto' },
]

export default defineConfig({
  lang: 'it-IT',
  title: 'Learning',
  description: 'Un passo alla volta: HTML, CSS, JavaScript e poi Rust. Lezioni pratiche in italiano.',
  cleanUrls: true,
  lastUpdated: true,
  head: [['link', { rel: 'icon', href: '/favicon.svg' }], ['meta', { name: 'theme-color', content: '#21715a' }]],
  themeConfig: {
    logo: '/favicon.svg',
    nav: [{ text: 'Percorso', link: '/percorso' }, { text: 'HTML', link: '/html/' }, { text: 'Laboratorio', link: '/html/progetto' }],
    sidebar: [
      { text: 'Il percorso', items: [{ text: 'Come studiare', link: '/percorso' }] },
      { text: 'HTML · Inizia qui', items: html },
      { text: 'Le prossime tappe', collapsed: true, items: [
        { text: 'CSS · Lo stile', link: '/css/' },
        { text: 'JavaScript · Le interazioni', link: '/javascript/' },
        { text: 'Rust · La prossima sfida', link: '/rust/' },
      ] },
    ],
    search: { provider: 'local', options: { locales: { root: { translations: {
      button: { buttonText: 'Cerca', buttonAriaLabel: 'Cerca nelle lezioni' },
      modal: { displayDetails: 'Mostra dettagli', resetButtonTitle: 'Azzera ricerca', backButtonTitle: 'Chiudi ricerca', noResultsText: 'Nessun risultato per', footer: { selectText: 'seleziona', navigateText: 'naviga', closeText: 'chiudi' } },
    } } } } },
    outline: { label: 'In questa lezione', level: [2, 3] },
    docFooter: { prev: 'Lezione precedente', next: 'Prossima lezione' },
    lastUpdated: { text: 'Aggiornato il', formatOptions: { dateStyle: 'short' } },
    darkModeSwitchLabel: 'Aspetto',
    lightModeSwitchTitle: 'Passa al tema chiaro',
    darkModeSwitchTitle: 'Passa al tema scuro',
    sidebarMenuLabel: 'Lezioni',
    returnToTopLabel: 'Torna in alto',
    footer: { message: 'Leggi. Prova. Cambia qualcosa. Ripeti.', copyright: 'Learning · HTML → CSS → JavaScript → Rust' },
  },
})
