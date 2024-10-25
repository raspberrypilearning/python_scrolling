## Create obstacles

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Create the obstacles that you will have to avoid to keep playing the game.
</div>
<div>

![Example skiing project with tree obstacles](images/obstacles.png){:width="300px"}

</div>
</div>

--- task ---

Define a `draw_obstacles` function to draw a cactus emoji 🌵.

--- code ---
---
language: python
line_numbers: true
line_number_start: 12
line_highlights: 13-14
---
 
# Draw obstacles function goes here
def draw_obstacles():
    text('🌵', 200, 200)
  
--- /code ---

Call the `draw_obstacles` function so that the cactus is drawn on the screen. 

--- code ---
---
language: python
line_numbers: true
line_number_start: 22
line_highlights: 27
---

def draw():   
    # Put code to run every frame here
    global safe
    safe = Color(200, 100, 0) 
    background(safe)
    draw_obstacles()
    draw_player()
  
--- /code ---

--- /task ---


--- task ---
**Test:** Run your code and you should see a cactus as well as your player. 
--- /task ---

--- task --- 

Add two variables to keep track of the obstacle's x and y coordinates. Update the code to draw the emoji so that it uses these variables.  

--- code ---
---
language: python
line_numbers: true
line_number_start: 13
line_highlights: 14-16
---

def draw_obstacles():
    obstacle_x = 200
    obstacle_y = 200 
    text('🌵', obstacle_x, obstacle_y) 

--- /code ---
</div>
--- /task ---

--- task ---

Now, add `frame_count` to the obstacle's y (vertical) position. 

--- code ---
---
language: python
line_numbers: true
line_number_start: 13
line_highlights: 15
---

def draw_obstacles():
    obstacle_x = 200
    obstacle_y = 200 + frame_count
    text('🌵', obstacle_x, obstacle_y) 

--- /code ---
--- /task ---

--- task --- 
**Test:** Run your code and the cactus emoji should move down the screen until it reaches the bottom.  

--- /task ---
