## Choose your theme

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
In this step you will create the theme of your game.

</div>
<div>
![Image of turtle size 100x100 against a blue background with screen size 400x400](images/theme-turtle.png){:width="300px"}
</div>
</div>

--- task ---

Open the [starter project](https://trinket.io/python/cda05e5911){:target="_blank"}. Trinket will open in another browser tab.

--- /task ---

What is the theme of your game? You could choose anything you want. Here are some ideas:
- a sport, or hobby
- a movie, show or game
- science, or nature
- anything else!

--- task ---

**Choose:** Set the size of your canvas.

--- collapse ---

---
title: Setting the screen size when your program starts
---

--- code ---
---
language: python
filename: main.py - setup()
line_numbers: true
line_number_start: 6
line_highlights: 7
---
def setup():
    size(400, 400)

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

Set the background colour based on the theme you want for your game. 

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
line_number_start: 9
line_highlights: 9
---
    background(255, 255, 255) # Try different numbers to change the colour 

--- /code ---

--- /collapse ---

--- /task ---

Now think about the character that is playing the game and avoiding the obstacles. Is it an object? person? animal?

--- task ---

Add an image for your character.

You can use the characters provided or use your own image.

[[[processing-add-image]]]

--- /task ---

Control the character's movement using the mouse pointer

--- task ---

Add code for the character to follow the mouse pointer. You can do this by getting the coordinates of the mouse pointer and using them as the coordinates for your character image when you draw it.

--- collapse ---

---
title: Getting the coordinates of the mouse pointer
---

You can get the coordinates of the mouse pointer from built-in variables —`mouse_x` and `mouse_y` — that the p5 library gives you. 

```python

image(skater, mouse_x, mouse_y, 30, 30) #the image of a skater sized 30x30 will go to the mouse pointer coordinates

```

--- /collapse ---

--- /task ---

--- save ---