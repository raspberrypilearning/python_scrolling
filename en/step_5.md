## Speed up!

Most endless runner games increase the difficulty of the game as the player progresses. 

### Add difficulty levels
Creating clear difficulty levels will make it easier for your player to understand what is happening.

--- task ---

Create a `global` `level` variable to track the level the player is currently on. Set it to `1` so players start a new game on the first level.

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
level = 1
--- /code ---

--- /task ---

--- task ---

This code uses the `height` and the `frame_count` to increase the `level` variable every time the player finishes a screen, then prints out the new level for the player.

--- code ---
---
language: python
filename: main.py — draw_obstacles()
line_numbers: false
---
def draw_obstacles():
  
  global level # use the global level
  
  if frame_count % height == height - 1 and level < 5:
    level += 1
    print('You reached level', level)
--- /code ---

**Tip:** This code uses `frame_count % height == height - 1` to increase the level just as the player reaches the end of the screen. Using `frame_count % height ==  0` would detect the start of a new screen, but it would also be true at the very start of the game.

--- /task ---

The two main options for increasing difficulty are to make the game move faster, and to increase the number of obstacles.

--- task ---

The speed of the game is controlled by how fast obstacles seem to be moving towards the player. This code speeds this up by using the level to set the y-coordinate during obstacle generation.

--- code ---
---
language: python
filename: main.py — draw_obstacles()
line_numbers: false
line_number_start: 1
line_highlights: 3
---
  for i in range(6):
    ob_x = randint(0, height)
    ob_y = randint(0, height) + (frame_count * level)
    ob_y %= height # wrap around
    text('🌵', ob_x, ob_y)
--- /code ---

--- /task ---

--- task ---

Adding extra obstacles is just a matter of increasing the number of times the `for` loop that creates them runs. You can do this by increasing the number you pass to the `range()` function.

--- code ---
---
language: python
filename: main.py — draw_obstacles()
line_numbers: false
line_number_start: 1
line_highlights: 1
---
  for i in range(6 + level):
--- /code ---

--- /task ---

### Give the player a score