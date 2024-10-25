## Set the scene

--- task ---

Open the [starter project](https://editor.raspberrypi.org/en/projects/dont-collide-starter){:target="_blank"}. 

--- /task ---

--- task ---

Create a variable called `safe` to store the background colour.

In the game, the player is safe if they are touching the background colour. 

--- code ---
---
language: python
line_numbers: true
line_number_start: 20
line_highlights: 22-24
---
 
def draw():   
    # Put code to run every frame here
    global safe
    safe = Color(200, 100, 0) 
    background(safe) 
  
--- /code ---

--- /task ---

--- task ---
**Test:** Run your code and you should see a coloured square. 

The colour is three numbers - the amount of red, green and blue. Try changing the numbers to any whole number between 0 and 255 to get a different colour.
--- /task ---

--- task ---

Define a `draw_player` function. Inside, add an emoji and a pair of x, y coordinates to represent the player. 

--- code ---
---
language: python
line_numbers: true
line_number_start: 7
line_highlights: 8-9
---
# Draw player function goes here
def draw_player():
    text('🤠', 200, 320)
  
--- /code ---

--- /task ---

--- task ---

Call the `draw_player` function so that the player is drawn on the screen.

--- code ---
---
language: python
line_numbers: true
line_number_start: 21
line_highlights: 26
---

def draw():  
    # Put code to run every frame here 
    global safe
    safe = Color(200, 100, 0) 
    background(safe)
    draw_player()
  
--- /code ---

--- /task ---

--- task ---
**Test:** Run your code and you should see the emoji appear near the bottom of the screen. 

You can paste in a different emoji if you want to.

--- /task ---

--- task ---

To make the player follow the mouse as it moves from side to side, change the player's x position to `mouse_x`.

--- code ---
---
language: python
line_numbers: true
line_number_start: 7
line_highlights: 9
---
# Draw player function goes here
def draw_player():
    text('🤠', mouse_x, 320)
  
--- /code ---
--- /task ---

--- task ---
Run your code and check that the player moves left and right when you move the mouse. 


--- /task ---