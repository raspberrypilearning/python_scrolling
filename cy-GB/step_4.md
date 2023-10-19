## Canfod gwrthdrawiad

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Mae gemau rhedeg diddiwedd yn dod i ben yn aml pan fydd y chwaraewr yn taro rhwystr.
</div>
<div>

![Delwedd o gam gorffenedig.](images/collision.png){:width="300px"}

</div>
</div>

Nawr fe allwch chi osod sut bydd eich chwaraewr yn ymateb i daro rhwystr.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Ystyr <span style="color: #0faeb0">**canfod gwrthdrawiad**</span> yw pennu pan fydd dau wrthrych wedi'u creu mewn efelychiad cyfrifiadurol — gêm, animeiddiad neu rywbeth arall — yn cyffwrdd. Mae sawl ffordd o wneud hyn, er enghraifft: 
  - gwirio ai'r lliwiau sy'n ymddangos yn safle gwrthych yw lliwiau'r gwrthrych hwnnw, neu liwiau un arall
  - cadw golwg ar siâp bob gwrthrych a gwirio a yw'r siapiau hynny'n gorgyffwrdd
  - creu cyfres o bwyntiau ffin neu linellau o amgylch gwrthrych a gwirio a ydyn nhw'n dod i gysylltiad ag unrhyw wrthrychau eraill y gellir eu taro
Pan fydd gwrthdrawiad o'r fath yn cael ei ganfod, gall y rhaglen ymateb mewn rhyw ffordd. In a video game, this is usually to deal damage (if the player collides with an enemy or hazard) or to give a benefit (if the player collides with a power up).
</p>

--- task ---

Yn eich swyddogaeth `llunio_chwaraewr()`, ewch ati i greu newidyn o'r enw `taro` a'i osod i gael y lliw yn safle'r chwaraewr.

--- code ---
---
language: python
filename: main.py - draw_player()
---

    print(red(taro), green(taro), blue(taro))

--- /code ---

--- /task ---

--- task ---

Create a condition to check `if` the `collide` variable is the same as the `safe` variable — if it is, then your player is safely touching the background and has not collided with an obstacle.

Ewch ati i greu amod i wirio, gan ddefnyddio `if`, a yw'r newidyn `taro` yr un fath â'r newidyn `diogel` — os felly, mae eich chwaraewr yn cyffwrdd y cefndir ac nid yw wedi taro rhwystr.

**Choose:** How should your player react? You could:
+ Newid y ddelwedd i fersiwn `wedi_taro`
+ Defnyddio emoji gwahanol i'r chwaraewr

--- collapse ---
---
title: Newid y ddelwedd
---

You can use emoji characters in the p5 `text()` function to represent your collided player.

Fe allwch chi ddefnyddio delwedd wahanol i gynrychioli eich chwaraewr pan fydd yn taro rhwystr.

--- code ---
---
language: python
filename: main.py - setup()
---

def setup(): size(400, 400) text_size(40)  # Controls the size of the emoji text_align(CENTER, TOP)  # Position around the centre

--- /code ---

--- code ---
---
language: python
title: Defnyddio cymeriadau emoji
---

def draw_player(): if collide == safe.hex:  # On background text('🎈', mouse_x, player_y) else:  # Collided text('💥', mouse_x, player_y)

--- /code ---

--- /collapse ---

[[[processing-tint]]]

[[[generic-theory-simple-colours]]]

--- /task ---

--- task ---

def setup(): size(400, 400) text_size(40) #Rheoli maint yr emoji text_align(CENTER, TOP) #Lleoli o amgylch y canol

--- /task ---

--- task ---

**Debug:** You might find some bugs in your project that you need to fix. Here are some common bugs.

--- collapse ---
---
title: There is no collision when the player reaches an obstacle
---

If your player character touches the obstacle and nothing happens, there are a few things you should check:

 - Make sure you call `draw_obstacles()` before `draw_player()`. Os byddwch chi'n gwirio am wrthdaro cyn llunio'r rhwystrau mewn ffrâm, ni fydd unrhyw rwystrau i daro mewn iddyn nhw!
 - Gwnewch yn siŵr eich bod yn defnyddio'r union un lliw wrth lunio'r gwrthrych ac yn y datganiad `if` sy'n gwirio am wrthdaro. Fe allwch chi wneud yn siŵr o hyn drwy ddefnyddio'r newidyn `global` mewn dau le.
 - Ydych chi'n llunio'r cymeriad chwarae cyn gwirio'r lliw yng nghyfesurynnau'r llygoden? Os felly, dim ond y lliwiau gan y chwaraewr fyddwch chi'n eu cael bob amser. Rhaid i chi wirio'r lliw yn gyntaf ac **wedyn** llunio'r chwaraewr.
 - Oes gennych chi god yn y rhan `else` i wneud rhywbeth gwahanol pan fydd gwrthdrawiad yn cael ei ganfod, fel rhoi arlliw neu ddefnyddio delwedd wahanol?
 - Ydych chi wedi mewnoli'r cod ar gyfer eich datganiad `if` yn gywir fel ei fod yn rhedeg pan fydd yr amod yn cael ei fodloni?

Printing the colour of the pixel you are checking for a collision can be useful:

```python
    no_fill()
  ellipse(mouse_x, chwaraewr_y, 10, 10) #Llunio pwynt gwrthdaro
```

You can also print a circle around the point you are checking and adjust the point you check if you need to:

```python
    def llunio_chwaraewr():

  chwaraewr_y = int(height * 0.8)
  #Defnyddiol ar gyfer difa chwilod
  #Llunio cylchoedd o amgylch y picseli i wirio am wrthdrawiad

  no_fill()
  ellipse(mouse_x, chwaraewr_y, 10, 10) #Llunio pwynt gwrthdaro
  ellipse(mouse_x, chwaraewr_y + 40, 10, 10)
  ellipse(mouse_x - 12, chwaraewr_y + 20, 10, 10)
  ellipse(mouse_x + 12, chwaraewr_y + 20, 10, 10)

  taro = get(mouse_x, chwaraewr_y)
  taro2 = get(mouse_x - 12, chwaraewr_y + 20)
  taro3 = get(mouse_x + 12, chwaraewr_y + 20)
  taro4 = get(mouse_x, chwaraewr_y + 40)

  if mouse_x < width: #Oddi ar ochr chwith y sgrin
    taro2 = diogel

  if mouse_x > width: #Oddi ar ochr dde'r sgrin
    taro3 = diogel

  if taro == diogel and taro2 == diogel and taro3 == diogel and taro4 == diogel:
    text('🎈', mouse_x, chwaraewr_y)
  else:
    text('💥', mouse_x, chwaraewr_y)
```

--- /collapse ---

--- /task ---

--- task ---

**Optional:** At the moment, you are just detecting collisions at one pixel on your player. You could also detect collisions at other pixels at the edge of your player, such as the bottom or left- and right-most edges.

--- collapse ---
---
filename: main.py - llunio_chwaraewr()
---

```python
def draw_player():

    player_y = int(height * 0.8)
    # Useful for debugging
    # Draw circles around the pixels to check for collisions

    no_fill()
    ellipse(mouse_x, player_y, 10, 10)  # Draw collision point
    ellipse(mouse_x, player_y + 40, 10, 10)
    ellipse(mouse_x - 12, player_y + 20, 10, 10)
    ellipse(mouse_x + 12, player_y + 20, 10, 10)

    collide = get(mouse_x, player_y).hex
    collide2 = get(mouse_x - 12, player_y + 20).hex
    collide3 = get(mouse_x + 12, player_y + 20).hex
    collide4 = get(mouse_x, player_y + 40).hex

    if mouse_x < width:  # Off the left of the screen
        collide2 = safe.hex

    if mouse_x > width:  # Off the right of the screen
        collide3 = safe.hex

    if collide == safe.hex and collide2 == safe.hex and collide3 == safe.hex and collide4 == safe.hex:
        text('🎈', mouse_x, player_y)
    else:
        text('💥', mouse_x, player_y)
```

--- /collapse ---

You could even use a loop and check lots of different pixels. This is how collision detection works in games.

--- /task ---

--- save ---
