## Upgrade your project 

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
If you have time you can upgrade your project.
</div>
<div>
![.](images/example1.png)
</div>
</div>

Here are some ideas you could try:

### Include a variety of obstacles
You can add variety to your obstacles in a few ways:
 - Randomly choose between multiple images, emojis, or obstacle drawing functions
 - Randomly adjust the colour, shape, or size of obstacles by changing the parameters that draw them
 - Animate the obstacle by adding rotation, a colour change, or some other visual difference controlled by `frame_count`

### Add a win condition
You can have players win the game in a few ways:
 - Achieving a winning score
 - Reaching a certain level of the game

Once they have won, you should tell them somehow — maybe using `print()` or `text()` and then stop the game.

### Give players more than one life
Add lives to your game, to allow players to survive a few collisions. This is a little trickier than just doing `lives =- 1` every time they collide with something:
 - The player may spend multiple frames in contact with an object, and so lose more than one life for a single collision — you'll need to prevent that from happening 
 - You will also need a way for players to know how many lives they have left, and maybe some sort of warning that tells them when they're on their last life
 - You could add an object that, when the player collides with it, gives them an extra life. Remember that you'll need to modify your regular collision code so as it doesn't subtract a life at the same time!

Each example project in the [Introduction](./) has a **See Inside** link for you to open the project and look at the code to get ideas and see how they work.

Take a look at some Don't collide projects created by community members in the Raspberry Pi Foundation’s [Don't collide - Community library](https://wke.lt/w/s/KobNfx){:target="_blank"}.

--- save ---
