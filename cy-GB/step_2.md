## Gosod y thema

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Gosodwch thema eich gêm a chreu cymeriad chwarae sy'n dilyn pwyntydd y llygoden.

</div>
<div>

![Delwedd o grwban maint 100x100 yn erbyn cefndir glas gyda maint sgrin o 400x400.](images/theme-turtle.png){:width="300px"}

</div>
</div>

Beth yw thema eich gêm? Here are some ideas:
- Camp neu hobi
- Ffilm, sioe deledu neu gêm
- Gwyddoniaeth neu fyd natur
- Neu unrhyw beth arall!

--- task ---

Open the [Don't Collide! starter project](https://editor.raspberrypi.org/en/projects/dont-collide-starter){:target="_blank"} project. The code editor will open in another browser tab.

If you have a Raspberry Pi account, you can click on the **Save** button to save a copy to your **Projects**.

--- /task ---

--- task ---

**Choose:** Set the size of your canvas.

--- code ---
---
def setup():    
size(400, 400)
filename: main.py - setup()
---

def setup(): size(400, 400)

--- /code ---

--- /task ---

--- task ---

Dyma'r lliw mae'n ddiogel i'r chwaraewr fod arno a byddwch chi'n defnyddio'r newidyn hwn eto nes 'mlaen.

This is the colour that it is safe for the player to be on and you will use this variable again later.

--- code ---
---
def draw():    
diogel = color(200, 100, 0) #Ychwanegwch liw eich thema   
background(diogel)
filename: main.py - draw()
---

def draw(): global safe safe = Color(200, 100, 0)  # Add the colour of your theme background(safe)

--- /code ---

[[[generic-theory-simple-colours]]]

--- /task ---

--- task ---

**Test:** Run your code to see the background colour. Change it until you are happy with the colour and the size of the screen.

--- /task ---

Now choose the character that is playing the game and avoiding the obstacles. Is it an object, person, animal, or something else?

The player will appear at a fixed `y` position and same `x` position as the mouse pointer, which is stored in the `p5` variable `mouse_x`.

--- task ---

Diffiniwch swyddogaeth `llunio_chwaraewr()` a chreu safle `chwaraewr_y` ar gyfer safle `y` sefydlog y chwaraewr:

Define a `draw_player()` function and create a `player_y` position for the fixed `y` position of the player:

--- code ---
---
def llunio_chwaraewr():    
llunio_chwaraewr_y = int(height * 0.8) #Lleoli tua gwaelod y sgrin
filename: main.py - llunio_chwaraewr()
---

def draw_player(): player_y = int(height * 0.8)  # Positioned towards the screen bottom

--- /code ---

Add code to `draw()` to call `draw_player()` each frame.

--- code ---
---
def draw():    
diogel = color(200, 100, 0) #Y lliw o'ch dewis    
background(diogel)    
llunio_chwaraewr()
filename: main.py - draw()
---

def draw(): global safe safe = Color(200, 100, 0)  # Your chosen colour background(safe) draw_player()

--- /code ---

--- /task ---

Next you will add code to the `draw_player()` function to draw your shape. You may also need to add `setup()` code.

--- task ---

**Choose:** What does your player look like? Your player could be:
+ Yn ddelwedd wedi'i darparu yn y prosiect dechreuol
+ Yn emoji 🎈 neu'n destun
+ Wedi'i lunio gan ddefnyddio cyfres o siapiau

--- collapse ---
---
title: Defnyddio delwedd ddechreuol
---

Images included in the starter project will be shown in the `Image gallery`.

![The Image gallery displaying the included images.](images/starter-images.png)

Make a note of the name of the image you want to use.

Gwnewch nodyn o enw'r ddelwedd rydych chi am ei defnyddio.

--- code ---
---
language: python filename: main.py - setup() line_numbers: true line_number_start: 9
filename: main.py - setup()
---

def setup(): size(400, 400) global player player = load_image('turtle.png')  # Load your image

--- /code ---

Call the `image()` and set it as global in the `draw_player()` function.

--- code ---
---
language: python filename: main.py - draw_player() line_numbers: true line_number_start: 14
filename: main.py - llunio_chwaraewr()
---

def draw_player(): player_y = int(height * 0.8)  # Positioned towards the screen bottom image(player, mouse_x, player_y, 30, 30)

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Defnyddio cymeriadau emoji
---

You can use emoji characters in the p5 `text()` function to use an emoji to represent your player.

Here's an example:

--- code ---
---
Fe allwch chi ddefnyddio cymeriadau emoji yn y swyddogaeth p5 `text()` i ddefnyddio emoji i gynrychioli eich chwaraewr.
filename: main.py - setup()
---

Dyma enghraifft:

--- /code ---

Call the `text()` and set it as global in the `draw_player()` function.

--- code ---
---
language: python filename: main.py - draw_player() line_numbers: true line_number_start: 14
filename: main.py - llunio_chwaraewr()
---

def draw_player(): player_y = int(height * 0.8) text('🎈', mouse_x, player_y)

--- /code ---

--- /collapse ---

[[[processing-python-text]]]

[[[generic-theory-simple-colours]]]

[[[processing-python-ellipse]]]

[[[processing-python-rect]]]

[[[processing-python-triangle]]]

[[[processing-tint]]]

[[[processing-stroke]]]

**Tip:** You can use several simple shapes in the same function to create a more complex player.

--- collapse ---
---
title: Llunio chwaraewr gan ddefnyddio nifer o siapiau
---

![A face shape made from a green circle as a background and two eyes drawn from blue circles, with black circles within and a glint within those using a white circle.](images/face_player.png)

--- code ---
---
language: python
filename: main.py - draw_player()
---

def draw_player(): player_y = int(height * 0.8) noStroke() # Face fill(0, 200, 100) ellipse(mouse_x, player_y, 60, 60)

    image(image_file, x_coord, y_coord, lled, uchder)

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

**Test:** Run your code and move the mouse to control the player.

Does it move like you expect?

--- /task ---

**Debug:** You might find some bugs in your project that you need to fix. Here are some common bugs.

--- task ---

--- collapse ---
---
title: Wela' i ddim y chwaraewr
---

Try switching to full screen. Also, check the `x` and `y` coordinates that you used to draw the player — make sure they are inside the canvas you created with `size()`.

--- /collapse ---

--- collapse ---
---
title: Dyw delwedd ddim yn llwytho
---

First, check that the image is in the `Image gallery`. Then, check the filename really carefully — remember capital letters are different to lower case letters and punctuation is important.

--- /collapse ---

--- collapse ---
---
title: Mae yna ddelwedd o'r maint anghywir
---

Yn gyntaf, gwnewch yn siŵr bod y ddelwedd yn yr `Image library`. Wedyn gwnewch yn fanwl siŵr bod enw'r ffeil yn gywir — cofiwch fod priflythrennau'n wahanol i lythrennau bach a bod atalnodi'n bwysig.

```python
image(image_file, x_coord, y_coord, width, height)
```

--- /collapse ---

--- collapse ---
---
title: Mae yna emoji o'r maint anghywir
---

Gwiriwch y mewnbynnau sy'n rheoli lled ac uchder y ddelwedd:

--- /collapse ---

--- /task ---

--- save ---
