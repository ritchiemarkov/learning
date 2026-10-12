# 21 · Lingue, Unicode e direzione del testo

**Obiettivo:** scrivere documenti che mantengano significato con lingue e alfabeti diversi.

## Lingua e codifica sono distinte

```html
<!doctype html>
<html lang="it">
<head><meta charset="utf-8"><title>Laboratorio multilingue</title></head>
<body>
  <p>Il motto è <span lang="en">Learn by doing</span>.</p>
</body>
</html>
```

UTF-8 definisce la codifica dei caratteri, `lang` la lingua del contenuto. La lingua aiuta pronuncia delle tecnologie assistive, correzione ortografica e altri strumenti. Usa tag BCP 47 pertinenti, come `it` o `en-GB`; una bandiera non è una lingua. Un cambio di lingua in un frammento può avere il proprio `lang`.

La dichiarazione non traduce il testo. `translate="no"` suggerisce di conservare un nome o codice. Anche attributi con testo traducibile possono essere interessati dalle regole di traduzione. Non usare un vecchio `meta http-equiv="content-language"` al posto di `lang`.

## Direzione e isolamento

```html
<p lang="ar" dir="rtl">مرحبا بكم</p>
<p>Utente: <bdi>ليلى</bdi> — 12 messaggi</p>
<p dir="auto">Testo inserito da un partecipante</p>
```

`dir="ltr"`, `rtl` e `auto` descrivono direzione di base. Lingua e direzione sono proprietà diverse: non tutte le lingue richiedono rtl. `bdi` isola un frammento dalla direzione del contesto, utile per nomi di origine sconosciuta. `bdo dir` forza l'ordine direzionale e si usa solo quando questa forzatura è intenzionale. Preferisci markup esplicito a caratteri di controllo invisibili difficili da revisionare.

Nei form, `dirname` su controlli applicabili può inviare una voce aggiuntiva con la direzione del testo. L'allineamento visivo non sostituisce `dir`; le proprietà CSS logiche proseguono nella tappa CSS.

## Annotazioni ruby

```html
<p lang="ja">
  <ruby>漢<rp>(</rp><rt>かん</rt><rp>)</rp></ruby>
</p>
```

`ruby` associa annotazioni al testo di base; `rt` contiene l'annotazione e `rp` le parentesi di fallback. Il testo di base non richiede gli elementi obsoleti `rb` e `rtc`. La struttura deve seguire il modello previsto per le annotazioni.

## Date, numeri e moduli

La forma leggibile può dipendere dalla cultura del lettore; i valori macchina rimangono normalizzati. Usa `time datetime="2026-11-02"` e spiega nel testo la data. Un input `datetime-local` non trasmette un fuso orario: non dedurlo soltanto dalla lingua. Non dare per universali strutture di nomi, telefoni o indirizzi; chiedi solo i campi necessari.

## Esercizio e verifica

Inserisci una frase inglese e un nome in alfabeto arabo in una pagina italiana. Esamina punteggiatura e direzione intorno al nome.

::: details Soluzione
Usa `lang="it"` sulla radice, `lang="en"` sulla frase e `bdi` intorno al nome. Quando la direzione dell'intero input è sconosciuta puoi usare `dir="auto"`. La pagina deve conservare il corretto ordine del testo anche nel DOM e nelle alternative accessibili.
:::

Fonti: [W3C · Dichiarare la lingua](https://www.w3.org/International/questions/qa-html-language-declarations), [W3C · Testo bidirezionale](https://www.w3.org/International/articles/inline-bidi-markup/), [MDN · ruby](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ruby).
