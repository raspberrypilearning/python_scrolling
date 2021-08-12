## Obstacle scrolling

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
By the end of this step, you will create a sprite that will move in your window, using x and y coordinates.
</div>
<div>
Image, gif or video showing what they will achieve by the end of the step. ![image of finished project](images/image.png){:width="300px"}
</div>
</div>

--- task ---
**Think** about what shape you would like your moving sprite to be. You will need to draw it using simple shapes.

You could make a cloud from ellipses, trees from triangles and rectangles, or anything you like! 

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;"> 
<span style="color: #0faeb0">**Sprites**</span> are computer graphics which can be moved on screen and thought about as a single unit or thing. You are writing a **function** that draws a single shape (a sprite) and then lets you make it do something interesting in another **function** </p>

--- task ---
**Create** your sprites by creating simple shapes. This example links three ellipses to create a cloud 

--- code ---
---
language: python
filename: main.py - draw()
line_numbers: true
line_number_start: 10
line_highlights: 
---
def cloud(x, y, size, colour):
  fill(128, 128, 128)
  ellipse(x, y, size, size)
  ellipse(x + (size * 0.75), y, size * 1.5, size * 1.5)
  ellipse(x + (size * 1.5), y, size, size)
--- /code ---

[[[processing-python-ellipse]]]


[[[processing-python-rect]]]


[[[processing-python-triangle]]]
--- /task ---

--- task ---
Add your new function to the `draw()` function by calling it using the name you created and giving it some coordinates. 

Using the example function `cloud()` (shown above) would look like this:

--- code ---
---
language: python
filename: main.py - draw()
line_numbers: true
line_number_start: 11
line_highlights: 12
---
def draw():
  cloud(200, 200) # will draw a cloud sprite in the centre of the window
--- /code ---
--- /task ---

--- task ---
**Test:** Run your code and change it to get your sprite to the size and shape that you want.

--- /task ---

--- task ---

Choose a stroke colour for the outline and a fill colour for the main part of the shape.

If you don't want an outline then use `no_stroke()`.

--- code ---
---
language: python
filename: main.py - draw()
line_numbers: true
line_number_start: 10
line_highlights: 11
---
def cloud(x, y, size, colour):
  stroke(0) #you can also use no_stroke()
  fill(128, 128, 128) # grey
  ellipse(x, y, size, size)
  ellipse(x + (size * 0.75), y, size * 1.5, size * 1.5)
  ellipse(x + (size * 1.5), y, size, size)
--- /code ---

[[[generic-theory-simple-colours]]]

--- /task ---

--- task ---
**Test:** Run your code and change the colour until you are happy with it.

--- /task ---

--- task ---

**Debug:** You might find some bugs in your project that you need to fix. Here are some common bugs.

--- collapse ---

---
title: I've updated my size and colour but the output area stays the same
---

After changing the code, you will need to `run` your project to see the changes in the output area. 

--- /collapse ---

--- collapse ---

---
title: I've tried different numbers but the color doesn't change 
---

The maximum amount of red, green or blue is `255`. Make sure all your `background` colour values are between `0` and `255`.  

--- /collapse ---

--- /task ---


Now that you have sprites that look the way you want, the next step is to make them move. 

--- save ---