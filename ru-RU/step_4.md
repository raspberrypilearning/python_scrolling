## Collision detection

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Endless runner games often end when the player collides with an obstacle.
</div>
<div>

![Image of finished step.](images/collision.png){:width="300px"}

</div>
</div>

Now you can set up your player to react to an obstacle collision.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">**Collision detection**</span> is determining when two objects created inside a computer simulation — whether that's a game, and animation, or something else — are touching. There are several ways to do this, for example: 
  - checking if the colours appearing at the location of an object are the colours of that object, or a different one
  - keeping track of the shape of every object, and checking if those shapes overlap
  - creating a set of boundary points, or lines, around an object and checking if they come into contact with any other 'collidable' objects
When such a collision is detected, the program can react in some way. In a video game, this is usually to deal damage (if the player collides with an enemy or hazard) or to give a benefit (if the player collides with a powerup).
</p>

--- task ---

In your `draw_player()` function, create a variable called `collide` and set it to get the colour at the position of the player.

--- code ---
---
language: python
filename: main.py - draw_player()
---

collide = get(mouse_x, player_y)

--- /code ---

--- /task ---

--- task ---

Create a condition to check `if` the `collide` variable is the same as the `safe` variable — if it is, then your player is safely touching the background and has not collided with an obstacle.

Move your code to draw your player inside your `if collide == safe` condition and add code in the `else` statement to get the player to react to the collision.

**Choose:** How should your player react? You could:
+ Change the image to a `crashed` version
+ Use a different emoji for the player
+ You could use `tint()` to change the appearance of an image, don't forget to call `no_tint()` after drawing the image

--- collapse ---
---
title: Change the image
---

You can use a different image to represent your player when it collides with an obstacle.

Вот пример:

--- code ---
---
language: python
filename: main.py - draw_player()
---

def draw_player(): player_y = int(height * 0.8)

  collide = get(mouse_x, player_y)

  if collide == safe: #On background image(skiing, mouse_x, player_y, 30, 30) else: #Collided image(crashed, mouse_x, player_y, 30, 30)

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Use emoji characters
---

You can use emoji characters in the p5 `text()` function to represent your collided player.

Вот пример:

--- code ---
---
language: python
filename: main.py - setup()
---

def setup(): size(400, 400) text_size(40) #Controls the size of the emoji text_align(CENTER, TOP) #Position around the centre

--- /code ---

--- code ---
---
language: python
filename: main.py - draw_player()
---

def draw_player(): if collide == safe: #On background text('🎈', mouse_x, player_y) else: #Collided text('💥', mouse_x, player_y)

--- /code ---

--- /collapse ---

[[[processing-tint]]]

[[[generic-theory-simple-colours]]]

--- /task ---

--- task ---

**Test:** Check if a collision is detected and the reaction takes place each time a collision occurs.

--- /task ---

--- task ---

**Debug:** You might find some bugs in your project that you need to fix. Here are some common bugs.

--- collapse ---
---
title: There is no collision when the player reaches an obstacle
---

If your player character touches the obstacle and nothing happens, there are a few things you should check:

 - Make sure you call `draw_obstacles()` before `draw_players()`. If you check for collisions before drawing the obstacles in a frame, then there won't be any obstacles to collide with!
 - Make sure you are using the exact same colour when drawing the object and in the `if` statement checking for the collision. You can make sure of this by using the same `global` variable in both places.
 - Are you drawing the player character before checking the colour at the mouse coordinates? If so, you are only ever going to get the colours from the player. You need to check the colour first and **then** draw the player.
 - Do you have code in the `else` part to do something different when a collision is detected, such as applying a tint or using a different image?
 - Have you correctly indented the code for your `if` statement so it runs when the condition is met?

Printing the colour of the pixel you are checking for a collision can be useful:

```python
  print(red(collide), green(collide), blue(collide))
```

You can also print a circle around the point you are checking and adjust the point you check if you need to:

```python
  no_fill()
  ellipse(mouse_x, player_y, 10, 10) #Draw collision point
```

--- /collapse ---

--- /task ---

--- task ---

**Optional:** At the moment, you are just detecting collisions at one pixel on your player. You could also detect collisions at other pixels at the edge of your player, such as the bottom or left- and right-most edges.

--- collapse ---
---
title: Collision detection with multiple pixels
---

```python
def draw_player():

  player_y = int(height * 0.8)
  #Useful for debugging
  #Draw circles around the pixels to check for collisions

  no_fill()
  ellipse(mouse_x, player_y, 10, 10) #Draw collision point
  ellipse(mouse_x, player_y + 40, 10, 10)
  ellipse(mouse_x - 12, player_y + 20, 10, 10)
  ellipse(mouse_x + 12, player_y + 20, 10, 10)

  collide = get(mouse_x, player_y)
  collide2 = get(mouse_x - 12, player_y + 20)
  collide3 = get(mouse_x + 12, player_y + 20)
  collide4 = get(mouse_x, player_y + 40)

  if mouse_x < width: #Off the left of the screen
    collide2 = safe

  if mouse_x > width: #Off the right of the screen
    collide3 = safe

  if collide == safe and collide2 == safe and collide3 == safe and collide4 == safe:
    text('🎈', mouse_x, player_y)
  else:
    text('💥', mouse_x, player_y)
```

--- /collapse ---

You could even use a loop and check lots of different pixels. This is how collision detection works in games.

--- /task ---

--- save ---
