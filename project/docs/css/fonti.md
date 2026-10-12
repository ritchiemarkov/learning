# Fonti CSS e metodo della ricerca

**Ricerca dettagliata: 12 ottobre 2026.** La sezione CSS iniziale era una pagina con obiettivi futuri, senza lezioni o esercizi. Ora il percorso contiene 35 lezioni, divise in 15 basi e 20 approfondimenti.

| Fonte ufficiale | Che cosa abbiamo confrontato |
| --- | --- |
| [Google/web.dev · Learn CSS](https://web.dev/learn/css) | Tutti i 37 moduli didattici, separando benvenuto, conclusione e quiz |
| [MDN · Styling basics](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics) | Sintassi, selezione, cascata, box, contenuti e debugging |
| [MDN · CSS layout](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout) | Flusso, flex, grid, responsive, posizionamento e prove di layout |
| [MDN · CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference) | Categorie di proprietà, selettori, at-rule, funzioni e compatibilità |
| [W3C · CSS Snapshot](https://www.w3.org/TR/css/) | Moduli e stabilità; distinzione fra inventario CSS e programma didattico |
| [Google/web.dev · Responsive design](https://web.dev/learn/design) | Viewport, media query, input e componenti adattabili |
| [Chrome DevTools · CSS](https://developer.chrome.com/docs/devtools/css) | Verifica delle regole applicate, valori risultanti e layout |
| [WAI · Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html) e [contrasto](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) | Prove su testo, finestre strette, colori e preferenze |

## Approfondimenti aggiunti al confronto Google

Abbiamo consultato le schede ufficiali su [layer](https://developer.mozilla.org/en-US/docs/Web/CSS/@layer), [scope](https://developer.mozilla.org/en-US/docs/Web/CSS/@scope), [property](https://developer.mozilla.org/en-US/docs/Web/CSS/@property), [subgrid](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout/Subgrid), [scroll snap](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_scroll_snap), [containment](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_containment), [supports](https://developer.mozilla.org/en-US/docs/Web/CSS/@supports) e [CSSOM](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Object_Model), insieme alle fonti precise riportate in ogni lezione.

Il percorso non è una traduzione integrale del corso Google o di MDN. Le spiegazioni e gli esempi sono scritti per Learning; le fonti servono al confronto tecnico e ai riferimenti. Non è una revisione riga per riga di tutte le specifiche CSS.

## Verifica e aggiornamenti

`project/sources/css/curriculum.json` registra il programma, la mappa dei moduli Google, data e impronta della pagina consultata. Il controllo offline del repository verifica che la mappa abbia tutti i 37 moduli, che le 35 lezioni esistano e che ciascuna abbia obiettivo, esercizio, soluzione e fonti. La build controlla i link interni.

Questa verifica misura presenza e organizzazione del materiale, non correttezza assoluta di ogni esempio né padronanza del lettore. Abbiamo una soluzione eseguibile e prove mirate per il progetto; funzionalità recenti richiedono verifiche di browser e accessibilità prima dell'uso reale.

Per i risultati della ricerca consulta la [copertura](/css/copertura); per studiare scegli il [percorso](/css/).
