## Random obstacles


Currently, the obstacle disappears off the bottom of the screen, because its `obstacle_y` position becomes larger than the screen size.

--- task ---

Use the modulo (%) operator to divide the y position by the screen size and give you the **remainder**. This makes the obstacle reappear at the top!

--- code ---
---
language: python
line_numbers: true
line_number_start: 13
line_highlights: 16
---
 
def draw_obstacles():
    obstacle_x = 200
    obstacle_y = 200 + frame_count
    obstacle_y = obstacle_y % screen_size
    text('🌵', obstacle_x, obstacle_y) 
  
--- /code ---

--- /task ---

--- task ---
**Test:** Run your code and you should see the obstacle reach the bottom of the screen and then restart from the top.
--- /task ---

--- task ---
Add a line of code for a random **seed**. A seed lets you generate the same random numbers in each frame.

--- code ---
---
language: python
line_numbers: true
line_number_start: 12
line_highlights: 14
---
 
# Draw obstacles function goes here
def draw_obstacles():
    seed(1234)
    obstacle_x = 200
    obstacle_y = 200 + frame_count

--- /code ---
--- /task ---

--- task ---
Update the code so that the x, y coordinates for the obstacle are generated randomly.

--- code ---
---
language: python
line_numbers: true
line_number_start: 12
line_highlights: 15-16
---
 
# Draw obstacles function goes here
def draw_obstacles():
    seed(1234)
    obstacle_x = randint(0, screen_size)
    obstacle_y = randint(0, screen_size) + frame_count

--- /code ---

--- /task ---

--- task ---
**Test:** Run your code and you should see the cactus appear at a random position. Change the `1234` value inside the seed to another number and it will appear somewhere else. 
--- /task ---
