## Rilevamento delle collisioni

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
I giochi dei corridori senza fine spesso finiscono quando il giocatore si scontra con un ostacolo.
</div>
<div>

![Image of finished step.](images/collision.png){:width="300px"}

</div>
</div>

Ora puoi impostare il tuo giocatore in modo che reagisca alla collisione con un ostacolo.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">**Rilevamento collisioni**</span> determina quando due oggetti creati in una simulazione al computer —
che sia un gioco, un'animazione o qualcos'altro — si toccano. Esistono diversi modi per farlo, ad esempio: 
  - controllare se i colori che appaiono nella posizione di un oggetto sono i colori di quell'oggetto o uno diverso
  - tenere traccia della forma di ogni oggetto e controllare se quelle forme si sovrappongono
  - creare una serie di punti di confine, o linee, attorno a un oggetto e controllare se entrano in contatto con altri oggetti 'collidabili'
Quando tali collisioni vengono rilevate, il programma può reagire in qualche modo. In un videogioco, questo di solito serve per infliggere danni (se il giocatore si scontra con un nemico o un pericolo) o per fornire un vantaggio (se il giocatore collide con un potenziamento).
</p>

--- task ---

Nella tua funzione `disegna_giocatore()`, si crea una variabile chiamata `collisione` e si imposta per ottenere il valore del colore esadecimale (hex) nella posizione del giocatore.

--- code ---
---
language: python
filename: main.py - disegna_giocatore()
---

    collisione = get(mouse_x, giocatore_y).hex

--- /code ---

--- /task ---

--- task ---

Crea una condizione per verificare `if` la variabile `collisione` è uguale alla variabile `safe` — se lo è, il lettore tocca lo sfondo in modo sicuro e non si è scontrato con un ostacolo.

Sposta il codice per attirare il giocatore all'interno della tua condizione `if collisione == safe` e aggiungi il codice nell'istruzione `else` per far reagire il giocatore alla collisione.

**Scegli:** Come dovrebbe reagire il tuo giocatore? Potresti:
+ Usare un'emoji diversa per il giocatore
+ Potresti usare `tint()` per cambiare l'aspetto di un'immagine, non dimenticare di chiamare `no_tint()` dopo aver disegnato l'immagine

--- collapse ---
---
title: Usare come personaggi emoji
---

Puoi utilizzare i caratteri emoji nella funzione p5 `text()` per rappresentare i tuoi ostacoli.

Ecco un esempio:

--- code ---
---
language: python
filename: main.py - setup()
---

def setup():
    size(400, 400)
    text_size(40)  # Controlla la dimensione dell'emoji 
    text_align(CENTER, TOP)  # Posizionati circa al centro

--- /code ---

--- code ---
---
language: python
filename: main.py - disegna_giocatore()
---

def disegna_giocatore():
    if collisione == safe.hex:  # Sullo sfondo
        text('🎈', mouse_x, giocatore_y)
    else:  # Collisione
        text('💥', mouse_x, giocatore_y)

--- /code ---

--- /collapse ---

[[[processing-tint]]]

[[[generic-theory-simple-colours]]]

--- /task ---

--- task ---

**Test:** Controlla se viene rilevata una collisione e la reazione avviene ogni volta che si verifica una collisione.

--- /task ---

--- task ---

**Debug:** Potresti trovare alcuni bug nel tuo progetto che devi correggere. Ecco alcuni bug comuni.

--- collapse ---
---
title: Non esiste collisione quando il giocatore raggiunge un ostacolo
---

Se il tuo personaggio tocca l'ostacolo e non succede nulla, ci sono alcune cose che dovresti controllare:

 - Assicurati di chiamare `disegnare_ostacoli()` prima di `disegna_giocatore()`. Se controlli le collisioni prima di disegnare gli ostacoli in una cornice, non ci saranno ostacoli con cui scontrarti!
 - Assicurati di utilizzare esattamente lo stesso colore quando disegni l'oggetto e nell'istruzione `if` controllando la collisione. Puoi assicurartene utilizzando la stessa variabile `global` in entrambi i posti.
 - Stai disegnando il giocatore prima di controllare il colore alle coordinate del mouse? Se è così, otterrai i colori solo dal giocatore. Devi prima controllare il colore e **poi** disegnare il giocatore.
 - Hai del codice nella parte `else` per fare qualcosa di diverso quando viene rilevata una collisione, come applicare una tinta o usare un'emoji?
 - Hai correttamente indentato il codice per la tua istruzione `if` in modo che venga eseguita quando la condizione è soddisfatta?

Può essere utile stampare il colore del pixel di cui stai controllando la collisione:

```python
    print(red(collisione), green(collisione), blue(collisione))
```

Puoi anche stampare un cerchio attorno al punto che stai controllando e regolare il punto che controlli se necessario:

```python
    no_fill()
    ellipse(mouse_x, giocatore_y, 10, 10)  # Disegna il punto di collisione
```

--- /collapse ---

--- /task ---

--- task ---

**Opzionale:** Al momento, stai rilevando solo collisioni su un pixel sul tuo lettore. Potresti anche rilevare collisioni su altri pixel sul bordo del tuo giocatore, come i bordi inferiore o più a sinistra e a destra.

--- collapse ---
---
title: Rilevamento delle collisioni con più pixel
---

```python
def disegna_giocatore():

    giocatore_y = int(height * 0.8)
    # Utile per il debug
    # Disegna cerchi attorno ai pixel per verificare le collisioni

    no_fill()
    ellipse(mouse_x, giocatore_y, 10, 10)  # Disegna il punto di collisione
    ellipse(mouse_x, giocatore_y + 40, 10, 10)
    ellipse(mouse_x - 12, giocatore_y + 20, 10, 10)
    ellipse(mouse_x + 12, giocatore_y + 20, 10, 10)

    collisione = get(mouse_x, giocatore_y).hex
    collisione2 = get(mouse_x - 12, giocatore_y + 20).hex
    collisione3 = get(mouse_x + 12, giocatore_y + 20).hex
    collisione4 = get(mouse_x, giocatore_y + 40).hex

    if mouse_x < width:  # Alla sinistra dello schermo
        collisione2 = safe.hex

    if mouse_x > width:  # Alla destra dello schermo
        collisione3 = safe.hex

    if collisione == safe.hex and collisione2 == safe.hex and collisione3 == safe.hex and collisione4 == safe.hex:
        text('🎈', mouse_x, giocatore_y)
    else:
        text('💥', mouse_x, giocatore_y)
```

--- /collapse ---

Potresti anche usare un loop e controllare molti pixel diversi. Ecco come funziona il rilevamento delle collisioni nei giochi.

--- /task ---

--- save ---
