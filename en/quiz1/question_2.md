
--- question ---

---
legend: Question 2 of 3
---

In this project you used procedural generation — having the computer create and place parts of your world for you. While doing this is a great time saver, particularly if you're creating very large levels, it can create some issues. Most of the probelms below would be issues you would have to deal with — you may even have seen some of them in your project. Which issue would not appear as a result of using procedural generation?

--- choices ---

- (x) Obstacles are generated outside of the screen.

  --- feedback ---
This wouldn't happen unless you want it to: you control the size of your canvas, and the upper and lower limits of the random numbers your program will select for x and y coordinates. Can you think of a reason you might want to generate obstacles outside of the screen?
  --- /feedback ---

- ( ) Obstacles could be generated that leave the player with no route forward.

  --- feedback ---
This can happen with procedurally generated obstacles, particularly when the game first starts. You could work around this issue by preventing obstacles from appearing too close to the player's starting position. Can you think of other solutions?
  --- /feedback ---

- ( ) Obstacles appear directly underneath the player.

  --- feedback ---
This can happen either at the start of the game, or when new obstacles are added as a result of increasing the difficulty level, if they happen to choose a position close to the player's. A potential solution might be to make the player temporarially immune to collision with all obstacles, or even only newly-created obstacles, for a short time after a level increase. What problem might having the obstacle choose a new position if it was too close to the player create? 
  --- /feedback ---

- ( ) The obstacles are all grouped together, leaving too much open space elsewhere.

  --- feedback ---
Because random generation can randomly choose groups of numebers that are close together, this can be a problem. One solution might be to switch to semi-random generation — break the screen up in to pieces and use random numbers to generate obstacles inside each of those pieces. Can you think of how you could use this sort of procedural generation to make your game more interesting, or more challenging?
  --- /feedback ---

--- /choices ---

--- /question ---
