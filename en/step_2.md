## Choose your theme

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
In this step you will create the theme of your game.

</div>
<div>
Image, gif or video showing what they will achieve by the end of the step. ![](images/image.png){:width="300px"}
</div>
</div>

--- task ---

Open the [starter project](https://trinket.io/python/575bd82b01){:target="_blank"}. Trinket will open in another browser tab.

--- /task ---

What is the theme of your game? You could choose anything you want. Here are some ideas:
- a sport
- a hobby
- a movie, show or game
- nature
- science
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

Now think about the character that is playing the game and avoiding the obstacles. Is it an object? Person? Animal?

--- task ---

Add an image for your character.

You can use the characters provided or use your own image.

[[[processing-add-image]]]

--- /task ---

Control the character's movement using the mouse pointer

--- task ---

Add code for the character to follow the mouse pointer

<mark>ingredient for mouse pointer (see explore projects)</mark>

--- /task ---



--- save ---
