## Creu rhwystrau

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Ewch ati i greu'r rhwystrau bydd angen eu hosgoi i barhau i chwarae'r gêm.
</div>
<div>

![Enghraifft o brosiect sgïo gyda choed fel rhwystrau](images/obstacles.png){:width="300px"}

</div>
</div>

### Dechreuwch gydag un rhwystr

Fe allwch chi wneud rhwystrau yn yr un modd ag y gwnaethoch chi eich chwaraewr. Sut mae'r rhwystrau'n cyd-fynd â'ch thema?

Byddwch chi'n defnyddio dolen `for` i wneud llawer o gopïau felly dim ond un rhwystr mae angen i chi ei wneud neu ei ddewis.

--- task ---

Diffiniwch swyddogaeth `llunio_rhwystrau()`:

--- code ---
---
language: python filename: main.py - draw_obstacles() line_numbers: false line_number_start:
filename: main.py - llunio_rhwystrau()
---

def llunio_rhwystrau(): rh_x = width/2 rh_y = height/2 text('🌵', rh_x, rh_y) #Disodli gyda'ch rhwystr

--- /code ---

Ychwanegwch god at `draw()` i alw `llunio_rhwystrau()` bob ffrâm.

--- code ---
---
language: python filename: main.py - draw() line_numbers: false line_number_start:
filename: main.py - draw()
---

def draw(): diogel = color(200, 100, 0) #Ychwanegwch liw eich thema background(diogel)  
llunio_rhwystrau() #Cyn llunio'r chwaraewr llunio_chwaraewr()

--- /code ---

--- /task ---

--- task ---

**Dewis:** Sut mae eich rhwystr yn edrych? Fe allai eich rhwystr fod:
+ Yn ddelwedd wedi'i darparu yn y prosiect dechreuol
+ Yn emoji 🌵 neu'n destun
+ Wedi'i lunio gan ddefnyddio cyfres o siapiau

--- collapse ---
---
title: Defnyddio delwedd ddechreuol
---

Cliciwch yr eicon **manage images**.

![Yr eicon delweddau yng nghornel dde uchaf yr ardal cod.](images/starter-images.png)

Bydd delweddau yn y prosiect dechreuol wedi'u dangos yn y rhestr `Image library`.

Load the image into the `setup()` function

--- code ---
---
Llwythwch y ddelwedd i'r swyddogaeth `setup()`.
line_highlights: 12
---

def setup(): size(400, 400) global player player = load_image('skiing.png')  # Load your player image obstacle = load_image('rocket.png')  # Load your obstacle image

--- /code ---

Find the line `# Keep this to run your code`. Before that line, define a new `draw_obstacles()` function, call `obstacle` as a global variable and use it in the call to `image()`.

--- code ---
---
language: python
filename: main.py - draw_obstacles()
---

def draw_obstacles(): ob_x = width/2 ob_y = height/2

    global obstacle
    
    image(obstacle, ob_x, ob_y, 30, 30)  # Resize to fit your theme

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Defnyddio cymeriadau emoji
---

image(rhwystr, rh_x, rh_y, 30, 30) #Newidiwch y maint i gyd-fynd â'ch thema

Here's an example:

--- code ---
---
language: python
filename: main.py - setup()
---

Fe allwch chi ddefnyddio cymeriadau emoji yn y swyddogaeth p5 `text()` i gynrychioli eich rhwystrau.

--- /code ---

Find the line `# Keep this to run your code`. Before that line, define a new `draw_obstacles()` function.

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
title: Llunio rhwystr gan ddefnyddio nifer o siapiau
---

![A tree drawn with green triangles for the body and a brown rectangle for the trunk](images/tree_obstacle.png)

--- code ---
---
language: python
filename: main.py - draw_obstacles()
---

def draw_obstacles(): ob_x = width/2 ob_y = height/2 # Draw a fir tree no_stroke() fill(0,255,0)  # Green for needles triangle(ob_x + 20, ob_y + 20, ob_x + 10, ob_y + 40, ob_x + 30, ob_y + 40) triangle(ob_x + 20, ob_y + 30, ob_x + 5, ob_y + 55, ob_x + 35, ob_y + 55) triangle(ob_x + 20, ob_y + 40, ob_x + 0, ob_y + 70, ob_x + 40, ob_y + 70) fill(150,100,100)  # Brown for trunk rect(ob_x + 15, ob_y + 70, 10, 10)

--- /code ---

--- /collapse ---

--- /task ---

### Gwneud i'ch rhwystr symud

--- task ---

Now add code to increase the `y` position of the obstacle each frame, and have it wrap around when it gets to the bottom to create the effect of another obstacle.

The p5 `frame_count` variable starts counting the frames when you click run.

`ob_y %= height` sets the `y` position to the remainder when divided by `height`. With a `height` of '400', this will turn `401` into `1` so when the obstacles goes off the bottom of the screen, it reappears at the top.

--- code ---
---
language: python
filename: main.py - draw_obstacles()
---

Mae `rh_y %= height` yn gosod y safle `y` ar gyfer y gweddill pan gaiff ei rannu â `height`. Gyda `height` o '400', bydd hyn yn troi `401` yn `1` felly pan fydd y rhwystrau'n diflannu oddi ar waelod y sgrin, mae'n ailymddangos ar y brig.

--- /code ---

--- /task ---

### Rhwystrau di-ri

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

Mae'r cod hwn yn defnyddio dolen `for` gyda `randint()` i ddewis safleoedd rhwystrau i chi. Mae galw'r swyddogaeth `seed()` ar hap yn gyntaf yn golygu byddwch chi'n cael yr un rhifau ar hap bob amser. Mae hyn yn golygu na fydd y rhwystrau'n neidio o gwmpas bob ffrâm a'ch bod yn gallu newid y dosbarthiad nes eich bod yn cael un sy'n lleoli'r rhwystrau'n deg.

    for i in range(6):  
        ob_x = randint(0, height)
        ob_y = randint(0, height) + frame_count
        ob_y %= height
        text('🌵', ob_x, ob_y)  # Replace with your obstacle

--- /code ---

Useful information:

[[[using-seed-in-python]]]

[[[generic-python-for-loop-repeat]]]

--- /task ---

--- collapse ---
---
title: Rhybudd epilepsi
---

Testing your program has the potential to induce seizures for people with photosensitive epilepsy. If you have photosensitive epilepsy or feel you may be susceptible to a seizure, do not run your program. Instead, you can:
- Gwneud yn siŵr eich bod wedi ychwanegu'r llinell cod `seed()` i sicrhau nad yw eich rhwystrau'n neidio o gwmpas
- Gofyn i rywun ei rhedeg ar eich rhan
- Symud ymlaen a chwblhau'r prosiect, gan ofyn i rywun redeg y prosiect i chi ar y diwedd er mwyn i chi allu difa chwilod
- Newid y gyfradd fframiau cyn rhedeg eich rhaglen drwy ychwanegu `frame_rate(1)` ar ddechrau `setup()` — fe allwch chi dynnu hwn ar ôl cadarnhau nad oes chwilen

```python
run(frame_rate = 10)
```
You can alter the speed of the game by changing `10` to a higher or lower value.

--- /collapse ---

--- task ---

**Test:** Run your program and you should see multiple objects on the screen, wrapping around when they get to the bottom.

Change your code until you are happy with the obstacles you have. You can:

+ Newid y dosbarthiad i roi rhwystrau mewn gwahanol safleoedd dechreuol
+ Newid sawl gwaith mae'r ddolen yn ailadrodd i gael nifer gwahanol o rwsytrau
+ Addasu maint y rhwystrau

**Tip:** Make sure it is possible to avoid your obstacles but that there is no easy path through your game.

--- /task ---

--- task ---

**Debug:** You might find some bugs in your project that you need to fix. Here are some common bugs.

--- collapse ---
---
title: Dim ond un rhwystr sy'n cael ei lunio
---

Check your function that draws multiple obstacles:
 + Gwnewch yn siŵr ei bod yn defnyddio dolen `for` i alw'r swyddogaeth llunio rhwystrau fwy nag unwaith
 + Gwnewch yn siŵr ei bod yn defnyddio `randint()` i newid y cyfesurynnau (x, y) mae'n eu pasio i'r swyddogaeth llunio rhwystrau
 + Gwnewch yn siŵr eich bod wedi defnyddio `rh_x` a `rh_y` fel cyfesurynnau eich rhwystr

For example:

--- code ---
---
language: python
filename: main.py — draw_obstacles()
---

Tarwch olwg ar eich swyddogaeth sy'n llunio nifer o rwystrau:

    for i in range(6):  
        ob_x = randint(0, height)
        ob_y = randint(0, height) + frame_count
        ob_y %= height
        text('🌵', ob_x, ob_y)  # Replace with your obstacle

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Mae'r rhwystrau'n newid safle bob tro mae ffrâm yn cael ei llunio
---

def llunio_rhwystrau():

--- /collapse ---

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;"> 
Programmers use lots of neat tricks like using the `%` operator to make objects wrap around the screen and the `seed()` function to generate the same random numbers. The more coding you do, the more neat tricks you will learn.</p>

--- save ---
