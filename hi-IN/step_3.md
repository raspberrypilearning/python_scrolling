## Create obstacles

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Create the obstacles that you will have to avoid to keep playing the game.
</div>
<div>

![Example skiing project with tree obstacles](images/obstacles.png){:width="300px"}

</div>
</div>

### Start with one obstacle

You can make obstacles in the same ways that you made your player. How do the obstacles fit with your theme?

You are going to use a `for` loop to make lots of copies so you only need to make or choose one obstacle.

--- task ---

Define a `draw_obstacles()` function:

--- code ---
---
language: python
filename: main.py - draw_obstacles()
---

def draw_obstacles(): ob_x = width/2 ob_y = height/2 text('🌵', ob_x, ob_y) #Replace with your obstacle


--- /code ---

Add code to `draw()` to call `draw_obstacles()` each frame.

--- code ---
---
language: python
filename: main.py - draw()
---

def draw(): safe = color(200, 100, 0) #Add the colour of your theme background(safe)  
draw_obstacles() #Before drawing the player draw_player()

--- /code ---

--- /task ---

--- task ---

**Choose:** What does your obstacle look like? Your obstacle could be:
+ An image provided in the starter project
+ An emoji 🌵 or text
+ Drawn using a series of shapes

--- collapse ---
---
title: Use a starter image
---

Click on the **manage images** icon.

![The picture icon in the top right of the code area.](images/manage-images.png)

Images included in the starter project will be shown in the `Image library` list.

![The Image library with a list of included images.](images/starter-images.png)

Make a note of the name of the image you want to use.

Load the image into the `setup()` function.

--- code ---
---
language: python
filename: main.py - setup()
---

def setup(): size(400, 400) player = load_image('skiing.png') #Load your image obstacle = load_image('rocket.png') #Load your image

--- /code ---

Call the `image()` and set it as global in the `draw_obstacles()` function.

--- code ---
---
language: python
filename: main.py - draw_obstacles()
---

def draw_obstacles(): ob_x = width/2 ob_y = height/2

   global obstacle

   image(obstacle, ob_x, ob_y, 30, 30) #Resize to fit your theme

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Use emoji characters
---

You can use emoji characters in the p5 `text()` function to represent your obstacles.

यहाँ एक उदाहरण है:

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
filename: main.py - draw_obstacles()
---

def draw_obstacles(): ob_x = width/2 ob_y = height/2 text('🌵', ob_x, ob_y)

--- /code ---

--- /collapse ---

[[[processing-python-text]]]

[[[generic-theory-simple-colours]]]

[[[processing-python-ellipse]]]

[[[processing-python-rect]]]

[[[processing-python-triangle]]]

[[[processing-tint]]]

[[[processing-stroke]]]

**Tip:** You can use several simple shapes in the same function to create a more complex obstacle.

--- collapse ---
---
title: Draw an obstacle using multiple shapes
---

![विवरण](images/tree_obstacle.png)

--- code ---
---
language: python
filename: main.py - draw_obstacles()
---

def draw_obstacles(): ob_x = width/2 ob_y = height/2 #Draw a fir tree no_stroke() fill(0,255,0) #Green for needles triangle(ob_x + 20, ob_y + 20, ob_x + 10, ob_y + 40, ob_x + 30, ob_y + 40) triangle(ob_x + 20, ob_y + 30, ob_x + 5, ob_y + 55, ob_x + 35, ob_y + 55) triangle(ob_x + 20, ob_y + 40, ob_x + 0, ob_y + 70, ob_x + 40, ob_y + 70) fill(150,100,100) # brown for trunk rect(ob_x + 15, ob_y + 70, 10, 10)

--- /code ---

--- /collapse ---

--- /task ---

### Get your obstacle moving

--- task ---

Now add code to increase the `y` position of the obstacle each frame, and have it wrap around when it gets to the bottom to create the effect of another obstacle.

The p5 `frame_count` variable starts counting the frames when you click run.

`ob_y %= height` sets the `y` position to the remainder when divided by `height`. With a `height` of '400', this will turn `401` into `1` so when the obstacles goes off the bottom of the screen, it reappears at the top.

--- code ---
---
language: python
filename: main.py - draw_obstacles()
---

def draw_obstacles(): ob_x = width/2 ob_y = height/2 + frame_count #Increases each frame ob_y %= height #Wrap around text('🌵', ob_x, ob_y) #Replace with your obstacle

--- /code ---

--- /task ---

### Lots of obstacles

You could draw lots of copies of your obstacle at different starting locations but that's quite a lot of work. Let's use a shortcut.


<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;"> 
<span style="color: #0faeb0">**Procedural generation**</span> is used in the creation of game worlds, obstacles, and movie scenes to create randomness but with certain rules applied. A <span style="color: #0faeb0">seed</span> means you can generate the same results every time you use the same seed.</p>

--- task ---

This code uses a `for` loop with `randint()` to choose obstacle positions for you. Calling the random `seed()` function first means that you will always get the same random numbers. This means that the obstacles won't jump around every frame and you can change the seed until you get one that positions the obstacles fairly.

--- code ---
---
language: python
filename: main.py - draw_obstacles()
---

def draw_obstacles():

  seed(12345678) #Any number is fine

  for i in range(6):  
ob_x = randint(0, height) ob_y = randint(0, height) + frame_count ob_y %= height text('🌵', ob_x, ob_y) #Replace with your obstacle

--- /code ---

Useful information:

[[[using-seed-in-python]]]

[[[generic-python-for-loop-repeat]]]

--- /task ---

--- collapse ---
---
title: Epilepsy warning
---

Testing your program has the potential to induce seizures for people with photosensitive epilepsy. If you have photosensitive epilepsy or feel you may be susceptible to a seizure, do not run your program. Instead, you can:
- Make sure you have added the `seed()` line of code to make sure your obstacles don't jump around
- Ask somebody to run it for you
- Move on and complete the project, asking someone to run the project for you at the end so you can debug
- Change the frame rate before you run your program by adding `frame_rate(1)` at the start of `setup()` — you can remove this once you have confirmed there is no bug

--- /collapse ---

--- task ---

**Test:** Run your program and you should see mutliple objects on the screen, wrapping around when they get to the bottom.

Change your code until you are happy with the obstacles you have. आप ऐसा कर सकते हैं

+ Change the seed to get obstacles in different starting positions
+ Change the number of times to loop repeats to get a different number of obstacles
+ Adjust the size of the obstacles

**Tip:** Make sure it is possible to avoid your obstacles but that there is no easy path through your game.

--- /task ---

--- task ---

**डीबग:** आपको अपने प्रोजेक्ट में कुछ बग मिल सकते हैं जिन्हें आपको ठीक करने की आवश्यकता है। Here are some common bugs.

--- collapse ---
---
title: Only one obstacle is being drawn
---

Check your function that draws multiple obstacles:
 + Make sure it uses a `for` loop to call the obstacle drawing function more than once
 + Make sure it uses `randint()` to change the (x, y) coordinates it is passing to the obstacle drawing function
 + Check that you have used `ob_x` and `ob_y` as the coordinates for your obstacle

उदाहरण के लिए:

--- code ---
---
language: python
filename: main.py — draw_obstacles()
---

def draw_obstacles():

  seed(12345678)

  for i in range(6):  
ob_x = randint(0, height) ob_y = randint(0, height) + frame_count ob_y %= height text('🌵', ob_x, ob_y) #Replace with your obstacle

--- /code ---

--- /collapse ---

--- collapse ---
---
title: The obstacles are changing position every time a frame is drawn
---

Make sure that you have used `seed()` inside the function that draws multiple obstacles.

--- /collapse ---

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;"> 
Programmers use lots of neat tricks like using the `%` operator to make objects wrap around the screen and the `seed()` function to generate the same random numbers. The more coding you do, the more neat tricks you will learn.</p>

--- save ---
