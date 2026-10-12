import { defineConfig } from 'vitepress'
import javascriptSidebar from './javascript-sidebar.json'

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
  description: 'Una base frontend e backend: HTML, CSS, JavaScript, TypeScript, Node.js, SQL e poi Rust. Lezioni pratiche in italiano.',
  cleanUrls: true,
  lastUpdated: true,
  markdown: {
    config(md) {
      // Gli esempi importati sono documentazione: l'HTML grezzo non diventa un componente Vue.
      const originalBlock = md.renderer.rules.html_block!
      const originalInline = md.renderer.rules.html_inline!
      md.renderer.rules.html_block = (tokens, idx, options, env, self) => {
        if (env.relativePath?.startsWith('javascript/tutorial/') && !tokens[idx].meta?.isPermalinkSymbol) {
          if (tokens[idx].content.trimStart().startsWith('<!--')) return ''
          return '<pre v-pre><code>' + md.utils.escapeHtml(tokens[idx].content) + '</code></pre>'
        }
        return originalBlock(tokens, idx, options, env, self)
      }
      md.renderer.rules.html_inline = (tokens, idx, options, env, self) => {
        if (env.relativePath?.startsWith('javascript/tutorial/') && !tokens[idx].meta?.isPermalinkSymbol) {
          const content = tokens[idx].content
          if (/^<\/?(?:u|sup|sub|br|em|strong|code)\s*\/?\s*>$/i.test(content)) return content
          return md.utils.escapeHtml(content)
        }
        return originalInline(tokens, idx, options, env, self)
      }
    },
  },
  head: [['link', { rel: 'icon', href: '/favicon.svg' }], ['meta', { name: 'theme-color', content: '#21715a' }]],
  themeConfig: {
    logo: '/favicon.svg',
    nav: [{ text: 'Percorso', link: '/percorso' }, { text: 'HTML', link: '/html/' }, { text: 'JavaScript', link: '/javascript/' }, { text: 'Laboratorio', link: '/html/progetto' }],
    sidebar: {
      '/javascript/': javascriptSidebar,
      '/': [
      { text: 'Il percorso', items: [{ text: 'Roadmap frontend e backend', link: '/percorso' }] },
      { text: 'HTML · Inizia qui', items: html },
      { text: 'Le basi frontend', collapsed: true, items: [
        { text: 'CSS · Lo stile', link: '/css/' },
        { text: 'JavaScript · Le interazioni', link: '/javascript/' },
        { text: 'TypeScript · I tipi', link: '/typescript/' },
      ] },
      { text: 'Backend e applicazione completa', collapsed: true, items: [
        { text: 'HTTP, API e Node.js', link: '/backend/' },
        { text: 'SQL e PostgreSQL', link: '/database/' },
        { text: 'Il progetto full stack', link: '/fullstack/' },
      ] },
      { text: 'Dopo le basi', collapsed: true, items: [
        { text: 'Un framework frontend', link: '/frontend/' },
        { text: 'Rust · Il prossimo linguaggio', link: '/rust/' },
      ] },
      ],
    },
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
    footer: { message: 'Leggi. Prova. Cambia qualcosa. Ripeti.', copyright: 'Learning · Frontend, backend e poi Rust' },
  },
})
