## Crea gli ostacoli

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Crea gli ostacoli che dovrai evitare per continuare a giocare.
</div>
<div>

![Esempio del progetto sciare con alberi come ostacoli](images/obstacles.png){:width="300px"}

</div>
</div>

### Inizia con un ostacolo

Puoi creare ostacoli nello stesso modo in cui hai creato il tuo giocatore. Come si adattano gli ostacoli al tuo tema?

Utilizzerai un ciclo `for` per creare molte copie, quindi dovrai solo creare o scegliere un ostacolo.

--- task ---

Definisci una funzione `disegna_ostacoli()`:

--- code ---
---
language: python filename: main.py - disegna_ostacoli() line_numbers: false line_number_start:
line_highlights: 4
---

def draw_obstacles(): ob_x = width/2 ob_y = height/2 text('🌵', ob_x, ob_y)  # Replace with your obstacle

--- /code ---

Aggiungi codice per `draw()` per chiamare `disegna_ostacoli()` in ogni fotogramma.

--- code ---
---
language: python filename: main.py - draw() line_numbers: false line_number_start:
line_highlights: 5
---

def draw(): global safe safe = Color(200, 100, 0)  # Add the colour of your theme background(safe) draw_obstacles()  # Before drawing the player draw_player()

--- /code ---

--- /task ---

--- task ---

**Scegli:** Che aspetto ha il tuo giocatore? Il tuo ostacolo potrebbe essere:
+ Un'immagine fornita nel progetto iniziale
+ Un'emoji🌵 o un testo
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
language: python filename: main.py - setup() line_numbers: true line_number_start: 9
line_highlights: 12
---

def setup(): size(400, 400) global player player = load_image('turtle.png')  # Load your player image obstacle = load_image('shark.png')  # Load your obstacle image

--- /code ---

Trova la riga `# Conserva questo per eseguire il codice`. Prima di quella riga, definisci una nuova funzione `disegna_ostacoli()`, che chiama `ostacolo` come una variabile global e la usa per chiamare `image()`.

--- code ---
---
language: python
filename: main.py - draw_obstacles()
---

def draw_obstacles(): ob_x = width/2 ob_y = height/2

    global obstacle
    
    image(obstacle, ob_x, ob_y, 30, 30)  # Resize to fit your theme

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Usare i caratteri emoji
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

Trova la riga `# Conserva questo per eseguire il codice`. Prima di quella riga, definisci una nuova funzione `disegna_ostacoli()`.

--- code ---
---
language: python
filename: main.py - draw_obstacles()
---

def draw_obstacles(): ob_x = width/2 ob_y = height/2 text('🌵', ob_x, ob_y)

--- /code ---

--- /collapse ---

[[[processing-python-text]]]

[[[generic-theory-simple-colours]]]

[[[processing-python-ellipse]]]

[[[processing-python-rect]]]

[[[processing-python-triangle]]]

[[[processing-tint]]]

[[[processing-stroke]]]

**Suggerimento:** Puoi utilizzare diverse forme semplici nella stessa funzione per creare un ostacolo più complesso.

--- collapse ---
---
title: Disegna un ostacolo utilizzando più forme
---

![Un albero disegnato con triangoli verdi per il corpo e un rettangolo marrone per il tronco](images/tree_obstacle.png)

--- code ---
---
language: python
filename: main.py - draw_obstacles()
---

def draw_obstacles(): ob_x = width/2 ob_y = height/2 # Draw a fir tree no_stroke() fill(0,255,0)  # Green for needles triangle(ob_x + 20, ob_y + 20, ob_x + 10, ob_y + 40, ob_x + 30, ob_y + 40) triangle(ob_x + 20, ob_y + 30, ob_x + 5, ob_y + 55, ob_x + 35, ob_y + 55) triangle(ob_x + 20, ob_y + 40, ob_x + 0, ob_y + 70, ob_x + 40, ob_y + 70) fill(150,100,100)  # Brown for trunk rect(ob_x + 15, ob_y + 70, 10, 10)

--- /code ---

--- /collapse ---

--- /task ---

### Fai spostare il tuo ostacolo

--- task ---

Ora aggiungi il codice per aumentare la posizione `y` dell'ostacolo in ogni fotogramma e fallo riapparire quando arriva in fondo per creare l'effetto di un altro ostacolo.

La variabile p5 `frame_count` inizia a contare i fotogrammi quando fai clic su Esegui.

`ob_y %= height` imposta la posizione `y` sul resto quando diviso per `height`. Con un'altezza di `height` di '400', questo trasformerà `401` in `1` quindi quando gli ostacoli escono dalla parte inferiore dello schermo, riappaiono in alto.

--- code ---
---
language: python
filename: main.py - draw_obstacles()
---

def draw_obstacles(): ob_x = width/2 ob_y = height/2 + frame_count  # Increases each frame ob_y %= height  # Wrap around text('🌵', ob_x, ob_y)  # Replace with your obstacle

--- /code ---

--- /task ---

### Molti ostacoli

Potresti disegnare molte copie del tuo ostacolo in diverse posizioni di partenza, ma sarebbe un bel po' di lavoro. Usiamo una scorciatoia.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;"> 
<span style="color: #0faeb0">**Generazione procedurale**</span> viene utilizzata nella creazione di mondi di gioco, ostacoli e scene di film per creare casualità ma con l'applicazione di determinate regole. Un <span style="color: #0faeb0">seme</span> significa che puoi generare gli stessi risultati ogni volta che usi lo stesso seme.</p>

--- task ---

Questo codice utilizza un ciclo `for` con `randint()` per scegliere le posizioni degli ostacoli per te. Chiamando prima la funzione `seed()` otterrai sempre gli stessi numeri casuali. Ciò significa che gli ostacoli non salteranno ad ogni fotogramma e potrai cambiare il seme finché non ne otterrai uno che posizioni gli ostacoli in modo equo.

--- code ---
---
language: python
filename: main.py - draw_obstacles()
---

def draw_obstacles(): seed(12345678)  # Any number is fine

    for i in range(6):  
        ob_x = randint(0, height)
        ob_y = randint(0, height) + frame_count
        ob_y %= height
        text('🌵', ob_x, ob_y)  # Replace with your obstacle

--- /code ---

Informazioni utili:

[[[using-seed-in-python]]]

[[[generic-python-for-loop-repeat]]]

--- /task ---

--- collapse ---
---
title: Avvertimento sull'epilessia
---

Testare il tuo programma può potenzialmente indurre convulsioni in persone affette da epilessia fotosensibile. Se soffri di epilessia fotosensibile o ritieni di poter essere suscettibile a convulsioni, non eseguire il programma. Altrimenti, puoi invece:
- Essere sicuro di aver aggiunto la riga di codice `seed()` perchè gli ostacoli non saltino
- Chiedere a qualcuno di eseguirlo per te
- Andare avanti e completare il progetto, chiedendo a qualcuno di eseguirlo per te alla fine in modo da poter eseguire il debug
- Rallentare il gioco utilizzando `frame_rate = 10` nella chiamata a `run()` in questo modo:

```python
run(frame_rate = 10)
```
Puoi alterare la velocità del gioco cambiando `10` con un valore più alto o più basso.

--- /collapse ---

--- task ---

**Test:** Esegui il tuo programma e dovresti vedere più oggetti sullo schermo, che riappaiono quando arrivano in fondo.

Cambia il tuo codice finché non sei soddisfatto degli ostacoli che hai. Puoi:

+ Cambiare il seme per ottenere ostacoli in diverse posizioni di partenza
+ Cambiare il numero di ripetizioni del loop per ottenere un numero diverso di ostacoli
+ Regolare la dimensione degli ostacoli

**Suggerimento:** Assicurati che sia possibile evitare gli ostacoli ma che non ci sia un percorso facile nel gioco.

--- /task ---

--- task ---

**Debug:** Potresti trovare alcuni bug nel tuo progetto che devi correggere. Ecco alcuni bug comuni.

--- collapse ---
---
title: Viene disegnato solo un ostacolo
---

Controlla la tua funzione che disegna più ostacoli:
 + Assicurati che utilizzi un ciclo `for` per chiamare la funzione di disegno degli ostacoli più di una volta
 + Assicurati che usi `randint()` per modificare le coordinate (x, y) che sta passando alla funzione di disegno degli ostacoli
 + Verifica di aver utilizzato `ob_x` e `ob_y` come coordinate per il tuo ostacolo

Ad esempio:

--- code ---
---
language: python
filename: main.py — draw_obstacles()
---

def draw_obstacles(): seed(12345678)

    for i in range(6):  
        ob_x = randint(0, height)
        ob_y = randint(0, height) + frame_count
        ob_y %= height
        text('🌵', ob_x, ob_y)  # Replace with your obstacle

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Gli ostacoli cambiano posizione ogni volta che viene disegnata una schermata
---

Assicurati di aver utilizzato `seed()` all'interno della funzione che disegna più ostacoli.

--- /collapse ---

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;"> 
I programmatori utilizzano molti trucchetti, come l'utilizzo dell'operatore `%` per far sì che gli oggetti compaiano sullo schermo e la funzione `seed()` per generare gli stessi numeri casuali. Più programmerai, più trucchi utili imparerai.</p>

--- save ---
