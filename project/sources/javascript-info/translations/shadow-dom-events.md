# Shadow DOM ed eventi

Lo shadow tree serve a incapsulare i dettagli interni di un componente.

Immagina un clic nello Shadow DOM di un componente `<user-card>`. Gli script del documento principale non dovrebbero dover conoscere la sua struttura interna, specialmente quando il componente proviene da una libreria esterna.

Il browser quindi **ridefinisce il destinatario dell'evento**, un comportamento chiamato *retargeting*.

**Un evento nato nello Shadow DOM presenta l'elemento host come `target` quando viene osservato dall'esterno del componente.**

Ecco un esempio:

```html
<user-card></user-card>

<script>
customElements.define('user-card', class extends HTMLElement {
  connectedCallback() {
    this.attachShadow({mode: 'open'});
    this.shadowRoot.innerHTML = `<p>
      <button>Click me</button>
    </p>`;
    this.shadowRoot.firstElementChild.onclick =
      e => alert("Inner target: " + e.target.tagName);
  }
});

document.onclick =
  e => alert("Outer target: " + e.target.tagName);
</script>
```

Facendo clic sul pulsante vedremo:

1. `Inner target: BUTTON`: il gestore interno riceve l'elemento nello Shadow DOM.
2. `Outer target: USER-CARD`: il gestore del documento vede l'host.

Il documento esterno può così gestire un evento sul componente senza conoscerne i dettagli interni.

**Il retargeting non si verifica quando l'evento nasce su un elemento inserito in uno slot che appartiene fisicamente al light DOM.**

Se clicchiamo sullo `<span slot="username">` di questo esempio, entrambi i gestori vedono proprio lo `span`:

```html
<user-card id="userCard">
  <span slot="username">John Smith</span>
</user-card>

<script>
customElements.define('user-card', class extends HTMLElement {
  connectedCallback() {
    this.attachShadow({mode: 'open'});
    this.shadowRoot.innerHTML = `<div>
      <b>Name:</b> <slot name="username"></slot>
    </div>`;

    this.shadowRoot.firstElementChild.onclick =
      e => alert("Inner target: " + e.target.tagName);
  }
});

userCard.onclick = e => alert(`Outer target: ${e.target.tagName}`);
</script>
```

Un clic su `John Smith` mantiene come destinatario lo `span`, perché fa parte del light DOM. Un clic su `<b>Name:</b>`, invece, nasce nello Shadow DOM: all'esterno il suo `target` diventa `<user-card>`.

## Propagazione ed event.composedPath()

La propagazione degli eventi considera il DOM appiattito, risultante dalla composizione degli slot. Un evento su un elemento assegnato a uno slot passa per lo slot e poi per i suoi antenati.

`event.composedPath()` restituisce il percorso dell'evento, includendo gli elementi dello Shadow DOM aperto. Nell'esempio precedente la composizione è rappresentabile così:

```html
<user-card id="userCard">
  #shadow-root
    <div>
      <b>Name:</b>
      <slot name="username">
        <span slot="username">John Smith</span>
      </slot>
    </div>
</user-card>
```

Per un clic sullo `span`, `event.composedPath()` restituisce un array con `span`, `slot`, `div`, `shadow-root`, `user-card`, `body`, `html`, `document` e `window`.

```warn header="I dettagli degli alberi chiusi rimangono nascosti all'esterno"
Se lo shadow tree è stato creato con `{mode: 'closed'}`, un gestore esterno non vede i nodi interni nel percorso composto: vede l'host `user-card` e gli elementi successivi. Questo segue lo stesso principio di incapsulamento degli altri strumenti dello Shadow DOM.
```

## event.composed

La proprietà `composed` stabilisce se un evento può attraversare il confine dello Shadow DOM. Con `true` può attraversarlo; con `false` rimane entro quell'albero. La propagazione tramite bubbling dipende anche dalla proprietà `bubbles`.

Molti eventi della [specifica UI Events](https://www.w3.org/TR/uievents) hanno `composed: true`:

- `blur`, `focus`, `focusin`, `focusout`;
- `click`, `dblclick`;
- `mousedown`, `mouseup`, `mousemove`, `mouseout`, `mouseover`;
- `wheel`;
- `beforeinput`, `input`, `keydown`, `keyup`.

Anche gli eventi touch e pointer hanno normalmente `composed: true` secondo le relative specifiche.

Alcuni eventi hanno invece `composed: false`, fra cui:

- `mouseenter`, `mouseleave`, che non fanno neanche bubbling;
- `load`, `unload`, `abort`, `error`;
- `select`;
- `slotchange`.

Questi si osservano negli elementi appartenenti allo stesso albero del loro destinatario.

## Eventi personalizzati

Quando vogliamo far risalire un evento personalizzato fuori dal componente, impostiamo sia `bubbles` sia `composed` a `true`.

Creiamo un `div` interno allo Shadow DOM di `div#outer` e inviamo due eventi. Solo quello con `composed: true` arriva al documento:

```html
<div id="outer"></div>

<script>
outer.attachShadow({mode: 'open'});

let inner = document.createElement('div');
outer.shadowRoot.append(inner);

/*
div(id=outer)
  #shadow-dom
    div(id=inner)
*/

document.addEventListener('test', event => alert(event.detail));

inner.dispatchEvent(new CustomEvent('test', {
  bubbles: true,
  composed: true,
  detail: "composed"
}));

inner.dispatchEvent(new CustomEvent('test', {
  bubbles: true,
  composed: false,
  detail: "not composed"
}));
</script>
```

## Riepilogo

Un evento attraversa il confine dello Shadow DOM se `composed` è `true`. La maggior parte degli eventi di interazione ha questo valore, come descritto nelle specifiche:

- [UI Events](https://www.w3.org/TR/uievents);
- [Touch Events](https://w3c.github.io/touch-events);
- [Pointer Events](https://www.w3.org/TR/pointerevents).

Gli eventi con `composed: false` restano nel loro albero. Quando creiamo un `CustomEvent`, dobbiamo scegliere esplicitamente il comportamento desiderato.

Con componenti annidati, un evento composto può attraversare più confini Shadow DOM. Se vogliamo informare soltanto il componente esterno immediato, possiamo inviare l'evento dall'host con `composed: false`: parte fuori dal nostro shadow tree, ma non attraversa il confine dell'albero che lo contiene.
