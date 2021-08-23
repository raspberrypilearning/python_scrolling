## Create obstacles

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Create the obstacles that you will have to avoid to keep playing the game
</div>
<div>
Image, gif or video showing what they will achieve by the end of the step.
</div>
</div>

Your obstacles will be made from shapes in processing. Can you make them out of a combination of shapes or just one shape? How does the obstacle fit with your theme?

--- task ---

**Choose:** what colours you will use for your obstacles. Add new colour variables to the `draw()` function.

<mark>collapse needed? Example needed?</mark>

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

What shape(s) will your obstacles be?

--- task ---

Create a function that will draw your obstacles

<mark>Again, to decide if code is needed here or even a collapse/ingredient</mark>

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

