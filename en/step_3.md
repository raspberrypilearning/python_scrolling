## Create obstacles

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Create the obstacles that you will have to avoid to keep playing the game.
</div>
<div>
Image, gif or video showing what they will achieve by the end of the step.
</div>
</div>

Your obstacles will be made from shapes in processing. Can you make them out of a combination of shapes or just one shape? How does the obstacle fit with your theme?

--- task ---

**Choose:** what colours you will use for your obstacles. Add new colour variables to the `setup()` function.

[[[generic-theory-simple-colours]]]

--- /task ---

What shape(s) will your obstacles be?

--- task ---

Create a function that will draw your obstacles

--- collapse ---
---
title: Create a filled in shape
---

To fill a shape use the `fill()` function with a colour. Remember you can use `no_fill()` to turn your fill off.

```python
fill(100, 200, 50)
ellipse(160, 220, 50, 50)
```

--- /collapse ---

[[[processing-python-ellipse]]]

[[[processing-python-rect]]]

[[[processing-python-triangle]]]

**Tip:** You can use several simple shapes in the same function to create a more complex obstacle (like the trees in the example Skiing project).

<mark>A small gallery of complex shapes from simple primitives</mark>

--- /task ---

Placing enough obstacles for the game would be time consuming and take too much code. You can use a `for` loop and `randint()` to choose their positions for you. However, `randint()` will start from a new number in every frame, so your obstacles will jump all over the place! If you use the `seed()` function first, you can avoid this.

[[[using-seed-in-python]]]

<mark>We are here</mark>

--- task ---



--- /task ---

The next step is to create a starfield using our single star. To do this, we're using a randomisation method  in python called 'seeded randomisation', using the `seed()` method. 



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

--- /task ---

--- task ---


**Debug:** You might find some bugs in your project that you need to fix. Here are some common bugs.

--- collapse ---
---
title: I am having trouble with the colour of my shapes
---

Make sure that, if you have variables for colour, they are defined as global variables.

--- code ---
---
language: python
filename: main.py - setup()
line_numbers: true
line_number_start: 20
line_highlights: 21
---

def setup():    
    global BLACK, WHITE
    BLACK = (0,0,0)
    WHITE = (255,255,255)

--- /code ---

--- /collapse ---


--- /task ---

--- /task ---

--- save --- 

