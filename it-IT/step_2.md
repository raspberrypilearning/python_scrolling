## Prepara la scena

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Imposta il tema del tuo gioco e crea un personaggio che segue il puntatore del mouse.

</div>
<div>

![Immagine di una tartaruga vista dall'alto in uno sfondo blu.](images/theme-turtle.png){:width="300px"}

</div>
</div>

Qual è il tema del tuo gioco? Ecco alcune idee:
- Sport
- Hobbies
- Scienza
- Natura

--- task ---

Apri [Non scontrarti! progetto iniziale](https://editor.raspberrypi.org/it-IT/projects/dont-collide-starter){:target="_blank"} progetto. L'editor si aprirà in un'altra scheda del browser.

Se disponi di un account Raspberry Pi, puoi fare clic sul pulsante **Salva** per salvarne una copia nei tuoi **Progetti**.

--- /task ---

--- task ---

**Scegli:** Imposta la dimensione della tua cornice.

--- code ---
---
language: python
filename: main.py - setup()
line_numbers: true
line_number_start: 9
line_highlights: 10
---

def setup():
    size(400, 400)

--- /code ---

--- /task ---

--- task ---

Crea una variabile chiamata `safe` per memorizzare il colore di sfondo in base al tema che desideri per il tuo gioco.

Questo è il colore su cui è sicuro che il giocatore si trovi e utilizzerai di nuovo questa variabile in seguito.

--- code ---
---
language: python
filename: main.py - draw()
line_numbers: true
line_number_start: 13
line_highlights: 14, 15, 16
---

def draw():
    global safe
    safe = Color(200, 100, 0)  # Aggiungi il colore del tuo tema
    background(safe)

--- /code ---

[[[generic-theory-simple-colours]]]

--- /task ---

--- task ---

**Test:** Esegui il codice per vedere il colore di sfondo. Cambialo finché non sei soddisfatto del colore e delle dimensioni dello schermo.

--- /task ---

Ora scegli il personaggio che sta giocando ed evitando gli ostacoli. Un oggetto, una persona, un animale o qualcos'altro?

Il giocatore apparirà in una fissata posizione `y` e lo stesso sarà per la posizione `x` del puntatore del mouse, la quale è salvata nella `p5` variabile `mouse_x`.

--- task ---

È una buona idea organizzare il codice per stabilire quello che il personaggio può fare in una funzione.

Definisci una funzione `disegna_giocatore()` e crea una posizione `giocatore_y` per la posizione fissa `y` del giocatore:

--- code ---
---
language: python
filename: main.py - disegna_giocatore()
line_numbers: true
line_number_start: 12
line_highlights: 12-14
---

def disegna_giocatore():
    giocatore_y = int(height * 0.8)  # Posizionato verso la parte inferiore dello schermo

--- /code ---

Aggiungi codice per `draw()` per chiamare `disegna_giocatore()` ogni fotogramma.

--- code ---
---
language: python
filename: main.py - draw()
line_numbers: true
line_number_start: 15
line_highlights: 19
---

def draw():
    global safe
    safe = Color(200, 100, 0)  # Il colore che hai scelto
    background(safe)
    disegna_giocatore()
  
--- /code ---

--- /task ---

Successivamente aggiungerai il codice alla funzione `disegna_giocatore()` per disegnare la tua forma. Potrebbe anche essere necessario aggiungere il codice `setup()`.

--- task ---

**Scegli:** Che aspetto ha il tuo giocatore? Il tuo giocatore potrebbe essere:
+ Un'immagine fornita nel progetto iniziale
+ Un'emoji 🎈 o un testo
+ Disegnato utilizzando una serie di forme

--- collapse ---
---
title: Usare un'immagine di partenza
---

Le immagini incluse nel progetto iniziale verranno visualizzate nella `Galleria di immagini`.

![La Galleria di immagini mostra le immagini incluse.](images/starter-images.png)

Prendi nota del nome dell'immagine che desideri utilizzare.

Carica l'immagine nella funzione `setup()`

--- code ---
---
language: python
filename: main.py - setup()
line_numbers: true
line_number_start: 9
line_highlights: 11-12
---

def setup():
    size(400, 400)
    global giocatore
    giocatore = load_image('turtle.png')  # Carica la tua immagine

--- /code ---

Chiama `image()` e impostala come globale nella funzione `disegna_giocatore()`.

--- code ---
---
language: python
filename: main.py - disegna_giocatore()
line_numbers: true
line_number_start: 14
line_highlights: 16
---

def disegna_giocatore():
    giocatore_y = int(height * 0.8)  # Posizionato verso la parte inferiore dello schermo
    image(giocatore, mouse_x, giocatore_y, 30, 30)

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Usare come personaggi emoji
---

Puoi utilizzare i caratteri emoji nella funzione p5 `text()` per usare un emoji per rappresentare il tuo giocatore.

Ecco un esempio:

--- code ---
---
language: python
filename: main.py - setup()
line_numbers: true
line_number_start: 9
line_highlights: 11-13
---

def setup():
    size(400, 400)
    text_size(40)  # Controlla la dimensione dell'emoji
    text_align(CENTER, TOP)  # Posizionati circa al centro

--- /code ---

Chiama `text()` e impostala come globale nella funzione `disegna_giocatore()`.

--- code ---
---
language: python
filename: main.py - disegna_giocatore()
line_numbers: true
line_number_start: 14
line_highlights: 16-17
---

def disegna_giocatore():
    giocatore_y = int(height * 0.8)
    text('🎈', mouse_x, giocatore_y)

--- /code ---

--- /collapse ---

[[[processing-python-text]]]

[[[generic-theory-simple-colours]]]

[[[processing-python-ellipse]]]

[[[processing-python-rect]]]

[[[processing-python-triangle]]]

[[[processing-tint]]]

[[[processing-stroke]]]

**Suggerimento:** Puoi utilizzare diverse forme semplici nella stessa funzione per creare un giocatore più complesso.

--- collapse ---
---
title: Disegna un giocatore utilizzando più forme
---

![Una faccia composta da un cerchio verde come sfondo e due occhi disegnati da cerchi blu, con cerchi neri all'interno e un luccichio all'interno di quelli sono disegnati da un cerchio bianco.](images/face_player.png)

--- code ---
---
language: python
filename: main.py - disegna_giocatore()
---

def disegna_giocatore():
    giocatore_y = int(height * 0.8)
    noStroke()
    # Volto
    fill(0, 200, 100)
    ellipse(mouse_x, giocatore_y, 60, 60)

    # Occhi
    fill(0, 100, 200)
    ellipse(mouse_x - 10, giocatore_y - 10, 20, 20)
    ellipse(mouse_x + 10, giocatore_y - 10, 20, 20)
    fill(0)
    ellipse(mouse_x - 10, giocatore_y - 10, 10, 10)
    ellipse(mouse_x + 10, giocatore_y - 10, 10, 10)
    fill(255)
    ellipse(mouse_x - 12, giocatore_y - 12, 5, 5)
    ellipse(mouse_x + 12, giocatore_y - 12, 5, 5)

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

**Test:** Esegui il codice e muovi il mouse per controllare il giocatore.

Si muove come ti aspetti?

--- /task ---

**Debug:** Potresti trovare alcuni bug nel tuo progetto che devi correggere. Ecco alcuni bug comuni.

--- task ---

--- collapse ---
---
title: Non riesco a vedere il giocatore
---

Prova a passare allo schermo intero. Anche, controlla le coordinate `x` e `y` che hai usato per disegnare il giocatore — sii sicuro che le coordinate siano interne alla cornice che hai creato con `size()`.

--- /collapse ---

--- collapse ---
---
title: Un'immagine non si carica
---

Innanzitutto, controlla che l'immagine sia nella `Galleria immagini`. Quindi, controlla il nome del file con molta attenzione: ricorda che le lettere maiuscole sono diverse dalle lettere minuscole e la punteggiatura è importante.

--- /collapse ---

--- collapse ---
---
title: Un'immagine è della dimensione errata
---

Controlla gli input che controllano la larghezza e l'altezza dell'immagine:

```python
image(image_file, x_coord, y_coord, width, height)
```

--- /collapse ---

--- collapse ---
---
title: Un'emoji è della dimensione errata
---

Se la tua emoji è troppo grande o troppo piccola, modifica il valore in `text_size()`.

--- /collapse ---

--- /task ---

--- save ---
