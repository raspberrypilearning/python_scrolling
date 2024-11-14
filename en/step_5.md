## Lots of obstacles

Now you will add code to make lots of obstacles to avoid. 

--- task ---

Add a loop and indent the code to draw an obstacle. The loop will run this code multiple times. 

--- code ---
---
language: python
line_numbers: true
line_number_start: 13
line_highlights: 15-19
---
 
def draw_obstacles():
    seed(1234)
    for i in range(8):
        obstacle_x = randint(0, screen_size)
        obstacle_y = randint(0, screen_size) + frame_count
        obstacle_y = obstacle_y % screen_size
        text('🌵', obstacle_x, obstacle_y)
  
--- /code ---

Make sure that the code for the seed is before the loop, otherwise all of your obstacles will be generated on top of each other!

--- /task ---

--- task ---
Change the number inside `range()` to control how many obstacles are created.

--- /task ---

--- task --- 
**Test:** Run your code and you should see several obstacles. 
--- /task ---