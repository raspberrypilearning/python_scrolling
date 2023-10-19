## Cyflymu pethau!

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Mae'r rhan fwyaf o gemau rhedeg diddiwedd yn mynd yn anoddach wrth i'r chwaraewr fynd yn ei flaen, ac yn rhoi sgôr i'r chwaraewr.
</div>
<div>

![Enghraifft o brosiect gyda thestun sgôr ar y sgrin.](images/score.png){:width="300px"}

</div>
</div>

### Ychwanegu lefelau anhawster

Bydd creu lefelau anhawster clir yn ei gwneud hi'n haws i'ch chwaraewr ddeall beth sy'n digwydd.

--- task ---

Ewch ati i greu newidyn `level` `global` i gadw golwg ar ba lefel mae'r chwaraewr arni ar y pryd. Gosodwch hwn ar `1` er mwyn i chwaraewyr ddechrau gêm newydd ar y lefel gyntaf.

--- code ---
---
language: python filename: main.py
line_highlights: 7
---

# Rhowch newidynnau cyffredinol yma
level = 1

--- /code ---

--- /task ---

--- task ---

Mae'r cod yn defnyddio `height` a `frame_count` i gynyddu'r newidyn `level` bob tro mae'r chwaraewr yn gorffen sgrin, ac yna'n printio'r lefel newydd i'r chwaraewr.

**Dewis:** Mae'r cod hwn yn cyfyngu ar nifer y lefelau i bump, felly ni fydd yn mynd yn rhy anodd. Does dim rhaid i'ch gêm gadw at bump, ond fe ddylech chi ddewis terfyn. Yn y pen draw, fydd y gêm rhy gyflym i bobl!

--- code ---
---
language: python
filename: main.py — draw_obstacles()
---

def llunio_rhwystrau():

    if frame_count % height == height - 1 and level < 5:
        level += 1
        print('You have reached level', level)

--- /code ---

--- /task ---

--- task ---

The two main options for increasing difficulty are to make the game move faster, and to increase the number of obstacles.

--- collapse ---
---
title: Cyflymu eich gêm
---

The speed of the game is controlled by how fast obstacles seem to be moving towards the player. This code speeds this up by adding `frame_count * level` to the `y` coordinate during obstacle generation.

Instead of moving your obstacles by one pixel in every frame, this code effectively moves it by `level` pixels instead.

Looking at the code, you might expect the speed to increase by more than `level` pixels. For example, at the point just before your `level` increases, the `frame_count` is `799` — as the `level` increases one frame before the `frame_count` is an even multiple of `height` (set at `400` pixels) — and `799 * 3` is notably bigger than `799 * 2`. However, the extra pixels created by multiplying the whole of `frame_count` by a bigger number are hidden by `ob_y %= height`. This leaves only the `level` extra pixels in each step.

--- code ---
---
Gan edrych ar y cod, efallai byddech chi'n disgwyl i'r cyflymder gynyddu mwy na'r picseli `lefel`. Er enghraifft, ar y pwynt cyn i'ch `lefel` gynyddu, mae'r `frame_count` yn `799` — gan fod y `lefel` yn cynyddu un ffrâm cyn bod `frame_count` yn eil-luosrif o `height` (wedi'i osod ar `400` picsel) — ac mae `799 * 3` yn sylweddol fwy na `799 * 2`. Ond mae'r picseli ychwanegol sy'n cael eu creu drwy luosi `frame_count` yn ei gyfanrwydd â rhif uwch wedi'u cuddio gan `rh_y %= height`. Mae hyn yn gadael dim ond y picseli `lefel` ychwanegol ym mhob cam.
line_numbers: false
---

    for i in range(6):
        ob_x = randint(0, height)
        ob_y = randint(0, height) + (frame_count * level)
        ob_y %= height  # Wrap around
        text('🌵', ob_x, ob_y)

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Ychwanegu mwy o rwystrau
---

Adding extra obstacles is just a matter of increasing the number of times the `for` loop that creates them runs. You can do this by increasing the number you pass to the `range()` function by `level`.

**Tip:** Of course, you can always use `level * 2`, or even larger multiples, if you want to make your game harder.

--- /collapse ---

--- /task ---

### Cadw sgôr

The longer a player lasts without colliding with an obstacle, the better they're playing your game. Adding a score will let them see how well they're doing.

--- task ---

Create a global `score` variable to track the player's score. Set it to `0` so players start a new game without any points.

--- code ---
---
language: python filename: main.py
line_numbers: false
---

# Rhowch newidynnau cyffredinol yma
Ewch ati i greu newidyn `sgor` cyffredinol i gadw golwg ar sgôr y chwaraewr. Gosodwch hwn ar `0` er mwyn i chwaraewyr ddechrau gêm newydd heb bwyntiau.

--- /code ---

--- /task ---

--- task ---

You can increase your player's score for every frame where they have not collided with an obstacle by increasing their score when you check for collision in `draw_player()`.

**Choose:** You can decide how many points each frame is worth, but increasing the player's score by `level` rewards players who can survive at higher difficulty levels.

--- code ---
---
language: python
filename: main.py — draw_player()
---

    global score
    
    if collide == safe.hex:
        text('🎈', mouse_x, player_y)
        score += level
    else:
        text('💥', mouse_x, player_y)

--- /code ---

--- /task ---

--- task ---

Players should be able to see their score. Because it increases so quickly, using `print()` wouldn't work very well. Use the p5 `text()` function inside your `draw()` function, to display it as text on the game screen instead.

[[[processing-python-text]]]

You can use the `+` operator to combine two or more strings if you want to give a heading like 'score' or 'points'. Because `score` is a number, you will need to convert it to a string before you can join it with another string. You can do this with `str()`:

```python
message = 'Score: ' + str(score)
```
**Tip:** `str()` is short for 'string' — programmers often remove letters like this, so they don't have to type as much!

--- /task ---

### Gêm drosodd!

Fe ddylai chwaraewyr allu gweld eu sgôr. Oherwydd ei fod yn cynyddu mor gyflym, fyddai defnyddio `print()` ddim yn gweithio cystal. Defnyddiwch y swyddogaeth p5 `text()` tu mewn i'ch swyddogaeth `draw()` i'w ddangos fel testun ar sgrin y gêm yn lle.

--- task ---

You can use the `level` variable to signal 'Game over' by setting it to 0 — a value it will never reach any other way. Do this in the `else` step of your collision detection code.

--- /task ---

--- task ---

Create an `if` statement in `draw()` that tests whether `level > 0` before calling any of the functions — like `background()`, `draw_obstacles()`, and `draw_player()` — that update the game. Because these functions are not called, the entire game seems to end, even though your program is still running.

--- /task ---

--- task ---

**Debug:** You might find some bugs in your project that you need to fix. Here are some common bugs.

--- collapse ---
---
title: Dydy'r sgôr ddim i'w weld
---

Make sure that you've included the `text()` function that draws the player's score at the appropriate point in your `draw()` function, and that you've passed it the correct values:

```python
text('Text to display', x, y)`
```

Ewch ati i greu datganiad `if` yn `draw()` sy'n profi a yw `lefel > 0` cyn galw unrhyw swyddogaeth — fel `background()`, `llunio_rhwystrau()`, a `llunio_chwaraewr()` — sy'n diweddaru'r gêm. Oherwydd nad yw'r swyddogaethau hyn yn cael eu galw, mae'n ymddangos bod y gêm wedi dod i ben, er bod eich rhaglen yn dal yn rhedeg.

--- code ---
---
language: python
filename: main.py — draw()
---

    if level > 0:
        background(safe) 
        fill(255)
        text('Score: ' + str(score), width/2, 20)
        draw_obstacles()
        draw_player()

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Dydy'r gêm ddim yn dod i ben ar ôl gwrthdrawiad
---

If you think your game might not be correctly detecting collisions at all, first try the debug instructions in the previous step, under 'There is no collision when the player reaches an obstacle'.

If your game is correctly detecting collisions, then check that you have properly indented the code that draws your game inside the `if level > 0` statement, to make sure it only runs if that statement is true. For example:

--- code ---
---
language: python
filename: main.py — draw()
---

    if level > 0:
        background(safe)
        fill(255)
        text('Score: ' + str(score), width/2, 20)
        draw_obstacles()
        draw_player()

--- /code ---

Finally, if both of those are working correctly, your game may not be setting `level = 0` correctly when a collision happens. For example:

--- code ---
---
language: python
filename: main.py — draw_player()
---

    if collide == safe.hex:
        text('🎈', mouse_x, player_y)
        score += level
    else:
        text('💥', mouse_x, player_y)
        level = 0

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Dydy'r gêm ddim yn cyflymu
---

First, check that `level` is increasing correctly. You should see a message printed out every time it goes up. If this isn't happening, check both the code for printing the message and the code for increasing the level.

If level is increasing correctly, check your `draw_obstacles()` function. In particular, check that you have `ob_y = randint(0, height) + (frame_count * level)`. It should look something like this:

--- code ---
---
Yn olaf, os yw'r ddau beth hynny'n gywir, efallai nad yw eich gêm yn gosod `lefel = 0` yn gywir pan fydd gwrthdrawiad. Er enghraifft:
line_numbers: false
---

    for i in range(6 + level):
        ob_x = randint(0, height)
        ob_y = randint(0, height) + (frame_count * level)
        ob_y %= height  # Wrap around
        text('🌵', ob_x, ob_y)

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Does dim rhwystrau newydd yn ymddangos
---

There are a few reasons this could be happening. And there are some more reasons why it might appear to be happening, when it isn't. First, because new obstacles are added based on `level`, check that `level` is increasing correctly. You should see a message printed out every time it goes up. If this isn't happening, check both the code for printing the message and the code for increasing the level.

If level is increasing correctly, check your `draw_obstacles()` function to ensure that you have `level` used in the `range()` function of the `for` loop that draws the obstacles. It should look something like this:

--- code ---
---
Yn gyntaf, gwnewch yn siŵr bod `lefel` yn cynyddu'n gywir. Fe ddylech chi weld neges yn cael ei phrintio bob tro mae'n cynyddu. Os nad yw hyn yn digwydd, gwiriwch y cod ar gyfer printio'r neges a'r cod ar gyfer cynyddu'r lefel.
line_numbers: false
---

    for i in range(6 + level):
        ob_x = randint(0, height)
        ob_y = randint(0, height) + (frame_count * level)
        ob_y %= height  # Wrap around
        text('🌵', ob_x, ob_y)

--- /code ---

If you've done all these checks and it still doesn't look like the number of obstacles is increasing, it's possible that they are but you aren't seeing it. You should try some of these steps to test this:
  - Arafu'r gêm gan ddefnyddio `frame_rate()` yn eich swyddogaeth `setup()` i roi mwy o amser i chi gyfri

```python
run(frame_rate = 10)
```

language: python filename: main.py — llunio_rhwystrau()

  - Change the seed you're using for your random numbers. It's unlikely, but it is possible that some obstacles are randomly appearing directly on top of each other
  - Add a `print()` to the `for` loop in `draw_obstacles()` that prints out the value of `i` in each pass of the loop, so you can verify whether it's running the number of times it should
  - Just for testing purposes, change `range(6 + level)` to `range(6 * level)` — that increase should be easier to spot!

--- /collapse ---

--- /task ---

--- save ---
