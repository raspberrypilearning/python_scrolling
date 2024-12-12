## Collisions

Recall that in the first step you created a 'safe' colour.

--- task ---
Create a variable to store the colour the player emoji is currently touching. 

--- code ---
---
language: python
line_numbers: true
line_number_start: 8
line_highlights: 9
---
 
def draw_player():
    player_on = get(mouse_x, 320).hex
    text('🤠', mouse_x, 320)
  
--- /code ---

--- /task ---

--- task ---

If the player is touching the safe colour, draw the player emoji. If it is not, draw an explosion emoji to show they have crashed. 

--- code ---
---
language: python
line_numbers: true
line_number_start: 8
line_highlights: 10, 12-13
---
 
def draw_player():
    player_on = get(mouse_x, 320).hex
    if player_on == safe.hex: 
        text('🤠', mouse_x, 320)
    else:  
        text('💥', mouse_x, 320)
  
--- /code ---
--- /task ---


--- task --- 
**Test:** Run your code and move the player. You should see the explosion emoji if your player touches an obstacle.

Make sure that in `draw()`, the line of code to `draw_obstacles()` is before `draw_player()`. If you check for collisions before drawing the obstacles in a frame, then there won’t be any obstacles to collide with!

--- /task ---