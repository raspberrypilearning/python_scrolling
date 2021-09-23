## Movement and collision

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Get the obstacles to move, and check if the player character hits an obstacle.
</div>
<div>
![image of finished project](images/move-and-detect.gif){:width="300px"}
</div>
</div>

The obstacles will move so that it appears as though the game is scrolling. You can use `frame_count` to update the obstacles in each frame so that the player character moves through them.

--- task ---

Create a function to move your obstacles and call the `translate()` function within it. Don't forget to call your new function in `draw()`

[[[processing-translation]]]
<<<mark>>> add ingredient here for push/pop matrix, make sure it is short, then add it to the invent project as well (at the same time as the loops ingredient)<<</mark>>>

--- /task ---

--- task ---

**Test** Experiment with moving the obstacles.

[[[processing-translation]]]

[[[processing-rotation]]]

[[[python-operators]]]

--- /task ---

Now you can set up your game to detect if there is a collision.

--- task ---

Add a function for your player character's actions and use conditions to find out if the mouse is touching an obstacle, then do something if it is.

A collision will occur if the mouse is touching a certain colour (the obstacle colour).

Have fun with emojis and/or the player character image.

--- collapse ---
---
title: Conditionals
---

Here is how conditionals are used in the example skiing project to see if the player has touched an obstacle:

```python 
  mouse_colour = color(get(mouse_x, mouse_y))
  
  if mouse_colour == GREEN: # hit a tree
    image(crashed, mouse_x, mouse_y, 30, 30)
    print('💥💥💥💥💥⛷️')
  else:
    image(skiing, mouse_x, mouse_y, 30, 30)
```

--- /collapse ---

**Tip:** Collisions don't have to be bad things. A character running into a power-up, or collecting an item for points, is also a kind of collision.

--- /task ---

--- task ---

**Test:** Check if a collision is detected.

--- /task ---

--- task ---

**Debug:** You might find some bugs in your project that you need to fix. Here are some common bugs.

--- collapse ---

---
title: Ordering
---

Ordering of functions, particularly re: translation

--- /collapse ---

--- collapse ---

---
title: There is no collision when the player reaches an obstacle
---

If your player character is touching the finishing and nothing is happening, there are a few things you should check:

 - Are you using the exact same colour when drawing the object and in the `if` statement checking for the win? You can make sure of this by using the same `global` variable in both places.
 - Are you drawing the player character sprite before checking the colour at the mouse coordinates? If so, you are only ever going to get the colours from the sprite image. You need to check the colour, **then** draw the sprite.
 - Is there code inside your if statement that will run to let you know when the win has happened? Add a `print()` statement with a unique message to be sure this code is running.
 - Have you correctly indented the code for your `if` statement so it runs when the condition is met?

--- /collapse ---

--- /task ---

--- save ---