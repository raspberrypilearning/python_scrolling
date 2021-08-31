## Win the game

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">

In this step you will create a finishing point for your game.

</div>
<div>
Image, gif or video showing what they will achieve by the end of the step. ![image of finished project](images/image.png){:width="300px"}
</div>
</div>

--- task ---

Add code to your collision detection function for your player character and check to find out if the mouse is touching a finishing point, then do something if it is.

Winning the game will occur if the mouse is touching a certain colour (the finishing colour).

Have fun with emojis and/or the player character image.

--- collapse ---
---
title: Conditionals
---

Here is how conditionals are used in the example skiing project to see if the player has touched an obstacle or the finishing point:

```python 
  mouse_colour = color(get(mouse_x, mouse_y))
  
  if mouse_colour == GREEN: # hit a tree
    image(crashed, mouse_x, mouse_y, 30, 30)
    print('💥💥💥💥💥⛷️')
  elif mouse_colour == RED: # crossed the finish line
    print('🥳🥳🥳🥳🥳⛷️')
  else:
    image(skiing, mouse_x, mouse_y, 30, 30)
```

--- /collapse ---

--- /task ---

--- task ---

**Test:** Check if the win is detected.

--- /task ---

--- task ---

**Debug:** You might find some bugs in your project that you need to fix. Here are some common bugs.

--- collapse ---

---
title: There is no winning reaction when the player reaches the finishing point
---

If your player character is touching the finishing and nothing is happening, there are a few things you should check:

 - Are you using the exact same colour when drawing the object and in the `if` statement checking for the win? You can make sure of this by using the same `global` variable in both places.
 - Are you drawing the player character sprite before checking the colour at the mouse coordinates? If so, you are only ever going to get the colours from the sprite image. You need to check the colour, **then** draw the sprite.
 - Is there code inside your if statement that will run to let you know when the win has happened? Add a `print()` statement with a unique message to be sure this code is running.
 - Have you correctly indented the code for your `if` statement so it runs when the condition is met?

--- /collapse ---

--- /task ---

--- save ---