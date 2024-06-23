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
filename: main.py - draw_player()
---

    collide = get(mouse_x, player_y).hex

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

def setup(): size(400, 400) text_size(40)  # Controls the size of the emoji text_align(CENTER, TOP)  # Position around the centre

--- /code ---

--- code ---
---
language: python
filename: main.py - draw_player()
---

def draw_player(): if collide == safe.hex:  # On background text('🎈', mouse_x, player_y) else:  # Collided text('💥', mouse_x, player_y)

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
    print(red(collide), green(collide), blue(collide))
```

Puoi anche stampare un cerchio attorno al punto che stai controllando e regolare il punto che controlli se necessario:

```python
    no_fill()
    ellipse(mouse_x, player_y, 10, 10)  # Draw collision point
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
def draw_player():

    player_y = int(height * 0.8)
    # Useful for debugging
    # Draw circles around the pixels to check for collisions

    no_fill()
    ellipse(mouse_x, player_y, 10, 10)  # Draw collision point
    ellipse(mouse_x, player_y + 40, 10, 10)
    ellipse(mouse_x - 12, player_y + 20, 10, 10)
    ellipse(mouse_x + 12, player_y + 20, 10, 10)

    collide = get(mouse_x, player_y).hex
    collide2 = get(mouse_x - 12, player_y + 20).hex
    collide3 = get(mouse_x + 12, player_y + 20).hex
    collide4 = get(mouse_x, player_y + 40).hex

    if mouse_x < width:  # Off the left of the screen
        collide2 = safe.hex

    if mouse_x > width:  # Off the right of the screen
        collide3 = safe.hex

    if collide == safe.hex and collide2 == safe.hex and collide3 == safe.hex and collide4 == safe.hex:
        text('🎈', mouse_x, player_y)
    else:
        text('💥', mouse_x, player_y)
```

--- /collapse ---

Potresti anche usare un loop e controllare molti pixel diversi. Ecco come funziona il rilevamento delle collisioni nei giochi.

--- /task ---

--- save ---
