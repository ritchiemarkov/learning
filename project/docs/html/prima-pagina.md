# 01 · La prima pagina

**Obiettivo:** creare un file HTML e aprirlo nel browser. Tempo indicativo: 20 minuti.

## Crea il file

Nella tua cartella `esercizi`, crea un file chiamato `index.html`. Assicurati che non sia stato salvato come `index.html.txt`. Incolla questo codice:

```html
<!doctype html>
<html lang="it">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>La mia prima pagina</title>
  </head>
  <body>
    <h1>Ciao, mondo!</h1>
    <p>Sto imparando a creare pagine web.</p>
  </body>
</html>
```

Salva il file e aprilo con il browser, per esempio con un doppio clic. Dovresti vedere un titolo grande e un paragrafo. Puoi anche [aprire l'esempio completo](/esempi/prima-pagina.html).

## Leggiamo il documento

| Parte | A cosa serve |
| --- | --- |
| `<!doctype html>` | Chiede al browser di usare la modalità standard per HTML |
| `<html lang="it">` | Racchiude il documento e indica la lingua italiana |
| `<head>` | Contiene metadati, come il titolo della scheda |
| `<meta charset="utf-8">` | Specifica la codifica dei caratteri, comprese le lettere accentate |
| `<meta name="viewport" ...>` | Imposta il viewport in base alla larghezza del dispositivo |
| `<title>` | Imposta il nome della scheda del browser |
| `<body>` | Contiene ciò che la pagina mostra |

`<title>` e `<h1>` hanno ruoli diversi: il primo compare nella scheda, il secondo nel contenuto.

## Prova subito

1. Cambia `Ciao, mondo!` con il tuo nome.
2. Aggiungi un secondo paragrafo con un tuo interesse.
3. Cambia il titolo della scheda in `Il mio quaderno`.
4. Salva e ricarica la pagina nel browser.

::: details Una possibile soluzione
```html
<!doctype html>
<html lang="it">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Il mio quaderno</title>
  </head>
  <body>
    <h1>Ciao, sono Alex</h1>
    <p>Sto imparando a creare pagine web.</p>
    <p>Mi piace fotografare la natura.</p>
  </body>
</html>
```
:::

## Controlla se hai capito

Quale parte contiene i contenuti visibili? Dove imposti la lingua? Perché cambiando `<title>` non cambia il titolo grande della pagina?

::: details Risposte
I contenuti visibili sono nel `<body>`. La lingua si indica con `lang` sull'elemento `<html>`. Il titolo grande è un `<h1>` e il titolo della scheda è un `<title>`: sono due elementi distinti.
:::

Se la pagina non cambia, controlla di aver salvato il file e ricaricato la scheda giusta.
