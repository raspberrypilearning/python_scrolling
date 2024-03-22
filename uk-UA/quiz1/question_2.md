--- question ---
---
legend: Question 2 of 3
---

In this project you used procedural generation — having the computer create and place parts of your world for you. While doing this is a great time saver, particularly if you're creating very large levels, it can create some issues. Which of these issues should you look out for when testing your procedural generation?

--- choices ---

- (x) All of them

  --- feedback ---

Correct! All of these can happen when using procedural generation. You can either add more code to check for and work around these issues, or try different seeds until you find one that works.

  --- /feedback ---

- ( ) Obstacles could be generated that leave the player with no route forward.

  --- feedback ---

Not quite. This can happen with procedurally generated obstacles, particularly when the game first starts.


**Tip:** You could work around this issue by preventing obstacles from appearing too close to the player's starting position. Can you think of other solutions?

  --- /feedback ---

- ( ) Obstacles appear directly underneath the player.

  --- feedback ---

Not quite. This can happen either at the start of the game, or when new obstacles are added as a result of increasing the difficulty level, if they happen to choose a position close to the player's.


**Tip:** A potential solution might be to make the player temporarily immune to collision with all obstacles, or even only newly created obstacles, for a short time after a level increase. What problems might having the obstacle choose a new position create if it was too close to the player?

  --- /feedback ---

- ( ) The obstacles are all grouped together, leaving too much open space elsewhere.

  --- feedback ---

Not quite. Because random generation can choose groups of numbers that are close together, this can be a problem.


**Tip:** One solution might be to switch to semi-random generation — break the screen up in to pieces and use random numbers to generate obstacles inside each of those pieces. Can you think of how you could use this sort of procedural generation to make your game more interesting, or more challenging?

  --- /feedback ---

--- /choices ---

--- /question ---
