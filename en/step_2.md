## Define your window

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
In this step you will create the background for your game.
</div>
<div>
Image, gif or video showing what they will achieve by the end of the step. ![](images/image.png){:width="300px"}
</div>
</div>

--- task ---

Open the [starter project](https://trinket.io/python/ea490530aa){:target="_blank"}. Trinket will open in another browser tab.

[[[python-offline]]]

--- /task ---

The first step is to define your game window and create a backdrop for your game. 

--- task ---
Under the ```setup()``` function in the starter project, enter the size of your game window by setting the `size` of your canvas.

**Choose:** Experiment with the numbers and re-run your code to find a size that you are happy with.

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
line_highlights: 8
---
def setup():
    #setup your game here
    size(400, 400)

--- /code ---

--- /collapse ---

--- /task ---

Next, we need to set the background colour. 

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

--- task ---

--- /task ---

--- save ---