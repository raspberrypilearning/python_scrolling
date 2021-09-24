## Speed up!

Most endless runner games increase the difficulty of the game as the player progresses, and give them a score. 

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

**Choose:** This code limits the level to 5, so it doesn't get too hard to play. There's no reason your game has to use 5, but you should choose a limt. Humans can only move so fast!

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

--- /task ---

The two main options for increasing difficulty are to make the game move faster, and to increase the number of obstacles.

--- task ---

The speed of the game is controlled by how fast obstacles seem to be moving towards the player. This code speeds this up by adding `frame_count * level` to the y-coordinate during obstacle generation.

--- code ---
---
language: python
filename: main.py — draw_obstacles()
line_numbers: false
---
  for i in range(6):
    ob_x = randint(0, height)
    ob_y = randint(0, height) + (frame_count * level)
    ob_y %= height # wrap around
    text('🌵', ob_x, ob_y)
--- /code ---

--- /task ---

--- task ---

Adding extra obstacles is just a matter of increasing the number of times the `for` loop that creates them runs. You can do this by increasing the number you pass to the `range()` function by `level`.

**Tip:** Of course, you can always use `level * 2`, or even larger multiples, if you want to make your game harder.

--- /task ---

### Keep score

The longer a player lasts without colliding with an obstacle, the better they're playing your game. Adding a score will let them see how well they're doing.

--- task ---

Create a `global` `score` variable to track the player's score. Set it to `10` so players start a new game without any points.

--- code ---
---
language: python
filename: main.py
line_numbers: false
---
score = 0
--- /code ---

--- /task ---

--- task ---

You can increase your player's score for every frame where they have not collided with an obstacle by increasing their score when you check for collision in `draw_player()`.

**Choose:** You can decide how many points each frame is worth, but increasing the player's score by `level` rewards players who can survive at higher difficulty levels.

--- code ---
---
language: python
filename: main.py — draw_player()
---
global score

  if collide == safe:
    text('🎈', mouse_x, player_y)
    score += level
  else:
    text('💥', mouse_x, player_y)
--- /code ---

--- /task ---

--- task ---

Players should be able to see their score. Because it increases so quickly, using `print()` wouldn't work very well. Using p5's `text()` function to display it as text on the game screen instead.

<mark>Python string concat ingredient — inc casting </mark>

<mark>Processing text function ingredient</mark>

--- /task ---

### Game over!

When a player has collided with an obstacle, the game should stop moving and their score should stop increasing.

--- task ---

You can use the `level` variable to signal 'Game over' by setting it to 0 — a value it will never reach any other way. Do this in the `else` step of your colision detection code.

--- /task ---

--- task ---

Create an `if` statement in `draw()` that tests whether `level > 0` before calling any of the functions — like `background()`, `draw_obstacles()`, and `draw_player()` — that update the game. Because these functions are not called, the entire game seems to end, even though your program is still running.

--- /task ---