## Create obstacles

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Create the obstacles that you will have to avoid to keep playing the game
</div>
<div>
Image, gif or video showing what they will achieve by the end of the step.
</div>
</div>



--- task ---


--- /task ---

Now you can create an overlay of simple shapes using randomness. In the example, we make a field of stars for our spaceship to fly over using tiny ellipses spread randomly around the window. 

--- task ---

**Choose:** Define the colour for your background shapes by adding a new colour variable to the `draw()` function. We used white, as shown here:
python

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

Now, we will create the function that will draw a single shape. Once we've done that, we can place our single shape in lots of random places in the window. To make a 'star', we want to draw a single white ellipse, with no stroke, that is 5 pixels by 5 pixels. 
8

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

--- /code ---

--- /task ---

The next step is to create a starfield using our single star. To do this, we're using a randomisation method  in python called 'seeded randomisation', using the `seed()` method. 

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;"> 
The `seed()` method is used to create a repeatable random number or sequence. A random number generator needs a number to start with (called the <span style="color: #0faeb0">seed value</span>), to be able to generate a random number. Usually, when you call for a random number using `randint()`, python uses your **system time** as the seed value. By using `seed()` and specifying the seed value in your program, you will **always get the same random number**.</p>

--- task ---

**Create:** Write a function that will draw your shape multiple times in the window, in random co-ordinates.


--- code ---
---
language: python
filename: main.py - setup()
line_numbers: true
line_number_start: 
line_highlights: 
---

#starfield() function goes here
def starfield(drift):
  seed(141234161689789)

  star_count = randint(10,50)
  
  for star in range(star_count):
    star_x = randint(0,400)
    star_y = randint(0,400)

--- /code ---

--- collapse ---
---
title: put a title here
---

Each debug in a collapse or ingredient

--- /collapse ---

--- /task ---

--- save --- 

