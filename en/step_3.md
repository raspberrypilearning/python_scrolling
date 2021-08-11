## Make a backdrop with randomness

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Now that our window is ready, we need to set a background.
</div>
<div>
Image, gif or video showing what they will achieve by the end of the step.
</div>
</div>

--- task ---

**Choose:** Think about the colours you will use for your face and change the `background` colour values to set your screen to a complementary colour:

[[[generic-theory-simple-colours]]]

--- collapse ---

---
title: Setting the background colour when your program starts
---

--- code ---
---
language: python
filename: main.py - setup()
line_numbers: true
line_number_start: 20
line_highlights: 21,22,23
---
def draw():    
    global BLACK
    BLACK = (0,0,0)
    background(BLACK) # Use any colour you like, but remember to set it up as a variable above! 

--- /code ---

--- /collapse ---

--- /task ---

Now you can create an overlay of simple shapes using randomness. In the example, we make a field of stars for our spaceship to fly over using tiny ellipses spread randomly around the window. 

--- task ---
**Choose:** Define the colour for your background shapes by adding a new colour variable to the `draw()` function. We used white, as shown here:

--- code ---
---
language: python
filename: main.py - setup()
line_numbers: true
line_number_start: 20
line_highlights: 21,23
---
def draw():    
    global BLACK, WHITE
    BLACK = (0,0,0)
    WHITE = (255,255,255)
--- /code ---

--- /task ---

--- task ---
**Create:** Find the line in your script that says `#draw_star() function goes here`. Underneath that line type:

--- code ---
---
language: python
filename: main.py - setup()
line_numbers: true
line_number_start: 10
line_highlights: 
---
#draw_star() function goes here
def draw_star(x, y):
  no_stroke()
  fill(WHITE)
  ellipse(x, y, 5, 5)

--- /task ---

--- task ---

**Debug:** You might find some bugs in your project that you need to fix. Here are some common bugs.

--- collapse ---
---
title: put a title here
---

Each debug in a collapse or ingredient

--- /collapse ---

--- /task ---

--- save ---

