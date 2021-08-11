## Create your window

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

The first step is to define your window and create a backdrop for your animation. 

--- task ---
Under the ```setup()``` function in the starter project, enter the size of your animation window by setting the `size` of your canvas.

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
line_highlights: 7
---
def setup():
    size(400, 400)


--- /code ---

--- /collapse ---

--- /task ---

Next, we need to set the background colour. 

--- save ---