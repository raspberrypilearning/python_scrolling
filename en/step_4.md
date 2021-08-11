## Add moving sprites

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
**Create** your sprites by creating simple shapes. This example links three ellipses to create a cloud or 

--- code ---
---
language: python
filename: main.py - draw()
line_numbers: true
line_number_start: 10
line_highlights: 
---
def cloud(x, y, size, colour):
  no_stroke()
  fill(colour)
  ellipse(x, y, size, size)
  ellipse(x + (size * 0.75), y, size * 1.5, size * 1.5)
  ellipse(x + (size * 1.5), y, size, size)
--- /code ---

[[[processing-python-ellipse]]]


[[[processing-python-rect]]]


[[[processing-python-triangle]]]
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
line_number_start: 11
line_highlights: 13
---
def draw():
  stroke(0) # you can also use no_stroke() 
  fill(255, 255, 0) # bright yellow
  ellipse(width/2, height/2, 200, 200) # circle in the middle
--- /code ---


[[[generic-theory-simple-colours]]]

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