# 30 · Scroll, overflow e scroll snap

**Obiettivo:** offrire scorrimento controllabile senza intrappolare o nascondere contenuti.

## Un contenitore di scorrimento

```css
.pannello { max-block-size: 24rem; overflow: auto; scrollbar-gutter: stable; }
.destinazione { scroll-margin-block-start: 5rem; }
html { scroll-padding-block-start: 5rem; }
```

Un limite di altezza crea un pannello soltanto se serve davvero. Scrollbar-gutter può riservare spazio per le scrollbar nei contesti previsti, riducendo spostamenti di layout. Scroll-margin e scroll-padding aiutano ancore e controlli a non finire sotto una testata fissa; non cambiano da soli la posizione dei normali margini.

`overflow-x` e `overflow-y` possono influenzarsi nei valori calcolati. `hidden` e `clip` differiscono per scorrimento programmatico e contesto; controlla la proprietà esatta. Un contenitore scorrevole deve essere raggiungibile e utilizzabile: alcuni browser gestiscono il focus diversamente, quindi verifica il caso reale.

## Snap facoltativo

```css
.galleria { display: flex; gap: 1rem; overflow-x: auto; scroll-snap-type: x proximity; }
.galleria > article { flex: 0 0 min(85%, 22rem); scroll-snap-align: start; }
```

Snap-type sceglie asse e rigidità, snap-align il punto di allineamento. Proximity è meno vincolante di mandatory; con contenuti grandi una scelta obbligatoria può rendere difficile fermarsi in punti necessari. Scroll-snap-stop e altri controlli richiedono prove su mouse, touch e tastiera.

Una galleria scorrevole non acquisisce automaticamente pulsanti, annunci o gestione del focus di un carousel completo. Mantieni accesso ai contenuti e indica che c'è altro materiale.

## Movimento e concatenazione

`scroll-behavior: smooth` influenza alcune navigazioni/scorrimenti, non ogni input di scroll. Applicalo solo se aiuta e rispetta reduced motion. `overscroll-behavior` controlla concatenazione e alcuni comportamenti ai limiti del contenitore: non bloccare le normali aspettative dell'utente senza un requisito.

## Esercizio

Crea tre schede scorrevoli e raggiungi la terza con tastiera e touch. Apri un link a un titolo sotto una testata fissa.

::: details Soluzione
Usa snap proximity e scroll-margin sulla destinazione. Verifica che focus e scroll rendano visibile la scheda raggiunta, senza tagliare l'outline. Se il browser non consente accesso al contenitore quando serve, valuta tabindex zero e un nome significativo sul contenitore, evitando di aggiungere inutili fermate.
:::

Fonti: [MDN · Scroll snap](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_scroll_snap), [web.dev · Overflow](https://web.dev/learn/css/overflow), [MDN · Scroll behavior](https://developer.mozilla.org/en-US/docs/Web/CSS/scroll-behavior).
