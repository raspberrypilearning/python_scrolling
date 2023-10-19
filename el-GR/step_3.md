## Δημιούργησε τα εμπόδια

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Δημιούργησε τα εμπόδια που θα πρέπει να αποφεύγεις για να συνεχίζεις να παίζεις το παιχνίδι.
</div>
<div>

![Παράδειγμα έργου σκι με εμπόδια δέντρων](images/obstacles.png){:width="300px"}

</div>
</div>

### Ξεκίνα με ένα εμπόδιο

Μπορείς να κάνεις τα εμπόδια με τους ίδιους τρόπους που έφτιαξες τον παίκτη σου. Ταιριάζουν τα εμπόδια με το θέμα σου;

Θα χρησιμοποιήσεις έναν βρόχο `for` για να δημιουργήσεις πολλά αντίγραφα, επομένως χρειάζεται να δημιουργήσεις ή να επιλέξεις μόνο ένα εμπόδιο.

--- task ---

Πρόσθεσε μια συνάρτηση `draw_obstacles()`:

--- code ---
---
language: python filename: main.py - draw_obstacles() line_numbers: false line_number_start:
line_highlights: 4
---

def draw_obstacles(): ob_x = width/2 ob_y = height/2 text('🌵', ob_x, ob_y) #Αντικατάστησέ το με το εμπόδιό σου

--- /code ---

Πρόσθεσε κώδικα στη συνάρτηση `draw()` για να καλεί τη συνάρτηση `draw_obstacles()` σε κάθε καρέ.

--- code ---
---
language: python filename: main.py - draw() line_numbers: false line_number_start:
filename: main.py - draw()
---

def draw(): safe = color(200, 100, 0) #Πρόσθεσε το χρώμα του θέματός σου background(safe)  
draw_obstacles() #Πριν σχεδιάσεις τον παίκτη draw_player()

--- /code ---

--- /task ---

--- task ---

**Επίλεξε:** Πώς θα είναι το εμπόδιό σου; Το εμπόδιο σου μπορεί να είναι:
+ Μια εικόνα που παρέχεται στο αρχικό έργο
+ Ένα emoji 🌵 ή ένα κείμενο
+ Σχεδιασμένο χρησιμοποιώντας μια σειρά σχημάτων

--- collapse ---
---
title: Χρησιμοποίησε την αρχική εικόνα
---

Κάνε κλικ στο εικονίδιο **View and Add Images**.

![Το εικονίδιο της εικόνας στην επάνω δεξιά γωνία της περιοχής κώδικα.](images/starter-images.png)

Οι εικόνες που περιλαμβάνονται στο αρχικό έργο θα εμφανίζονται στη λίστα `Image Library`.

Load the image into the `setup()` function

--- code ---
---
Φόρτωσε την εικόνα στη συνάρτηση `setup()`.
line_highlights: 12
---

def setup(): size(400, 400) global player player = load_image('skiing.png')  # Load your player image obstacle = load_image('rocket.png')  # Load your obstacle image

--- /code ---

Find the line `# Keep this to run your code`. Before that line, define a new `draw_obstacles()` function, call `obstacle` as a global variable and use it in the call to `image()`.

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
title: Χρησιμοποίησε χαρακτήρες emoji
---

image(obstacle, ob_x, ob_y, 30, 30) #Αλλαγή μεγέθους για να ταιριάζει με το θέμα σου

Here's an example:

--- code ---
---
language: python
filename: main.py - setup()
---

Μπορείς να χρησιμοποιήσεις χαρακτήρες emoji στη συνάρτηση p5 `text()` για να αναπαραστήσεις τα εμπόδιά σου.

--- /code ---

Find the line `# Keep this to run your code`. Before that line, define a new `draw_obstacles()` function.

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

**Tip:** You can use several simple shapes in the same function to create a more complex obstacle.

--- collapse ---
---
title: Σχεδίασε ένα εμπόδιο χρησιμοποιώντας πολλά σχήματα
---

![A tree drawn with green triangles for the body and a brown rectangle for the trunk](images/tree_obstacle.png)

--- code ---
---
language: python
filename: main.py - draw_obstacles()
---

def draw_obstacles(): ob_x = width/2 ob_y = height/2 # Draw a fir tree no_stroke() fill(0,255,0)  # Green for needles triangle(ob_x + 20, ob_y + 20, ob_x + 10, ob_y + 40, ob_x + 30, ob_y + 40) triangle(ob_x + 20, ob_y + 30, ob_x + 5, ob_y + 55, ob_x + 35, ob_y + 55) triangle(ob_x + 20, ob_y + 40, ob_x + 0, ob_y + 70, ob_x + 40, ob_y + 70) fill(150,100,100)  # Brown for trunk rect(ob_x + 15, ob_y + 70, 10, 10)

--- /code ---

--- /collapse ---

--- /task ---

### Κίνησε το εμπόδιό σου

--- task ---

Now add code to increase the `y` position of the obstacle each frame, and have it wrap around when it gets to the bottom to create the effect of another obstacle.

The p5 `frame_count` variable starts counting the frames when you click run.

`ob_y %= height` sets the `y` position to the remainder when divided by `height`. With a `height` of '400', this will turn `401` into `1` so when the obstacles goes off the bottom of the screen, it reappears at the top.

--- code ---
---
language: python
filename: main.py - draw_obstacles()
---

def draw_obstacles(): ob_x = width/2 ob_y = height/2 + frame_count  # Increases each frame ob_y %= height  # Wrap around text('🌵', ob_x, ob_y)  # Replace with your obstacle

--- /code ---

--- /task ---

### Πολλά εμπόδια

You could draw lots of copies of your obstacle at different starting locations but that's quite a lot of work. Let's use a shortcut.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;"> 
<span style="color: #0faeb0">**Procedural generation**</span> is used in the creation of game worlds, obstacles, and movie scenes to create randomness but with certain rules applied. A <span style="color: #0faeb0">seed</span> means you can generate the same results every time you use the same seed.</p>

--- task ---

This code uses a `for` loop with `randint()` to choose obstacle positions for you. Calling the random `seed()` function first means that you will always get the same random numbers. This means that the obstacles won't jump around every frame and you can change the seed until you get one that positions the obstacles fairly.

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

Useful information:

[[[using-seed-in-python]]]

[[[generic-python-for-loop-repeat]]]

--- /task ---

--- collapse ---
---
title: Προειδοποίηση για επιληψία
---

Testing your program has the potential to induce seizures for people with photosensitive epilepsy. If you have photosensitive epilepsy or feel you may be susceptible to a seizure, do not run your program. Instead, you can:
- Βεβαιώσου ότι έχεις προσθέσει τη γραμμή κώδικα `seed()` για να βεβαιωθείς ότι τα εμπόδιά σου δεν χοροπηδάνε
- Ζήτησε από κάποιον να το εκτελέσει για σένα
- Προχώρησε και ολοκλήρωσε το έργο, ζητώντας από κάποιον να εκτελέσει το έργο για σένα, ώστε να μπορείς να κάνεις εντοπισμό σφαλμάτων
- Άλλαξε τον ρυθμό καρέ πριν εκτελέσεις το πρόγραμμά σου προσθέτοντας `frame_rate(1)` στην αρχή της συνάρτησης `setup()` — μπορείς να το αφαιρέσεις αφού επιβεβαιώσεις ότι δεν υπάρχει σφάλμα

```python
run(frame_rate = 10)
```
You can alter the speed of the game by changing `10` to a higher or lower value.

--- /collapse ---

--- task ---

**Test:** Run your program and you should see multiple objects on the screen, wrapping around when they get to the bottom.

Change your code until you are happy with the obstacles you have. You can:

+ Να αλλάξεις το seed για να βάλεις εμπόδια σε διαφορετικές θέσεις εκκίνησης
+ Να αλλάξεις τον αριθμό των φορών στις επαναλήψεις βρόχου για να λάβεις διαφορετικό αριθμό εμποδίων
+ Να προσαρμόσεις το μέγεθος των εμποδίων

**Tip:** Make sure it is possible to avoid your obstacles but that there is no easy path through your game.

--- /task ---

--- task ---

**Debug:** You might find some bugs in your project that you need to fix. Here are some common bugs.

--- collapse ---
---
title: Μόνο ένα εμπόδιο έχει σχεδιαστεί
---

Check your function that draws multiple obstacles:
 + Βεβαιώσου ότι χρησιμοποιεί έναν βρόχο `for` για να καλέσει τη συνάρτηση σχεδίασης εμποδίων περισσότερες από μία φορές
 + Βεβαιώσου ότι χρησιμοποιεί `randint()` για να αλλάξει τις συντεταγμένες (x, y) που περνά στη συνάρτηση σχεδίασης εμποδίων
 + Έλεγξε ότι έχεις χρησιμοποιήσει `ob_x` και `ob_y` ως συντεταγμένες για το εμπόδιό σου

For example:

--- code ---
---
language: python
filename: main.py — draw_obstacles()
---

Έλεγξε τη συνάρτησή σου που σχεδιάζει πολλά εμπόδια:

    for i in range(6):  
        ob_x = randint(0, height)
        ob_y = randint(0, height) + frame_count
        ob_y %= height
        text('🌵', ob_x, ob_y)  # Replace with your obstacle

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Τα εμπόδια αλλάζουν θέση κάθε φορά που σχεδιάζεται ένα καρέ
---

def draw_obstacles():

--- /collapse ---

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;"> 
Programmers use lots of neat tricks like using the `%` operator to make objects wrap around the screen and the `seed()` function to generate the same random numbers. The more coding you do, the more neat tricks you will learn.</p>

--- save ---
