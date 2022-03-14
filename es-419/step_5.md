## ¡Acelera!

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
La mayoría de los juegos tipo endless runner (corredor infinito) aumentan la dificultad del juego a medida que el jugador avanza y les dan un puntaje.
</div>
<div>

![Proyecto de ejemplo con el texto puntaje en la pantalla.](images/score.png){:width="300px"}

</div>
</div>

### Agregar niveles de dificultad

Crear niveles de dificultad claros facilitará que tu jugador entienda lo que está sucediendo.

--- task ---

Crea una variable `nivel` que sea `global` para hacer seguimiento del nivel en el que se encuentra actualmente el jugador. Establece el valor de la variable en `1` para que los jugadores comiencen un nuevo juego en el primer nivel.

--- code ---
---
language: python filename: main.py
line_numbers: false
---

# Incluye variables globales aquí
nivel = 1

--- /code ---

--- /task ---

--- task ---

Este código usa `height` (altura) y `frame_count` (recuento de cuadros o fotogramas) para aumentar la variable `nivel` cada vez que el jugador despeja una pantalla, luego genera el nuevo nivel para el jugador.

**Elige:** Este código limita los niveles a cinco, para que no sea demasiado difícil de jugar. No hay ninguna razón por la que tu juego tenga que usar cinco niveles, pero deberías elegir un límite. ¡Los humanos tienen límites para moverse!

--- code ---
---
language: python filename: main.py — draw_obstacles()
line_numbers: false
---

def dibujar_obstaculos():

  global nivel #Usa el nivel global

  if frame_count % height == height - 1 and nivel < 5: nivel += 1 print('Llegaste al nivel', nivel)

--- /code ---

--- /task ---

--- task ---


Las dos opciones principales para aumentar la dificultad son hacer que el juego vaya más rápido y aumentar la cantidad de obstáculos.

--- collapse ---
---
title: Acelera tu juego
---

La velocidad del juego está controlada por la rapidez con la que los obstáculos parecen moverse hacia el jugador. Este código acelera esto al agregar `frame_count * nivel` a la coordenada `y` durante la generación de obstáculos.

En lugar de mover los obstáculos por píxel en cada cuadro (frame), este código los mueve en cambio por píxeles de `nivel`.

Al observar este código, es posible que esperes que la velocidad aumente más que por píxeles de `nivel`. Por ejemplo, en el punto justo antes de que cambie el `nivel` a uno superior, el `frame_count` es `799` — debido a que el `nivel` incrementa un cuadro (frame) antes de que el `frame_count` sea un múltiplo par de la altura o `height` (Establecida en `400` píxeles) — y `799 * 3` es notablemente mayor que `799 * 2`. Sin embargo, los píxeles adicionales creados al multiplicar el total de `frame_count` por un número mayor están siendo ocultados por `obstaculo_y %= height`. Esto solo deja los píxeles adicionales del `nivel` en cada paso.


--- code ---
---
language: python filename: main.py — draw_obstacles()
line_numbers: false
---

  for i in range(6): obstaculo_x = randint(0, height) obstaculo_y = randint(0, height) + (frame_count * nivel) obstaculo_y %= height #Recircular text('🌵', obstaculo_x, obstaculo_y)

--- /code ---

--- /collapse ---

--- collapse ---
---
titulo: Agrega más obstáculos
---

Puedes agregar obstáculos adicionales tan solo aumentando la cantidad de veces que se ejecuta el bucle `for` que los crea. Puedes hacer esto aumentando el número que le pasas a la función `range()` por `nivel`.

**Sugerencia:** Siempre puedes usar `nivel * 2`, o incluso múltiplos más grandes, si quieres aumentar la dificultad de tu juego.

--- /collapse ---

--- /task ---

### Registra el puntaje

Cuanto más dure un jugador sin chocar contra un obstáculo, mejor estarán jugando. Agregar el puntaje les permitirá ver qué tan bien lo están haciendo.

--- task ---

Create a global `score` variable to track the player's score. Set it to `0` so players start a new game without any points.

--- code ---
---
language: python filename: main.py
line_numbers: false
---

# Include global variables here
score = 0

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

  if collide == safe: text('🎈', mouse_x, player_y) score += level else: text('💥', mouse_x, player_y)

--- /code ---

--- /task ---

--- task ---

Players should be able to see their score. Because it increases so quickly, using `print()` wouldn't work very well. Use the p5 `text()` function inside your `draw()` function, to display it as text on the game screen instead.

[[[processing-python-text]]]

You can use the `+` operator to combine two or more strings if you want to give a heading like 'score' or 'points'. Because `score` is a number, you will need to convert it to a string before you can join it with another string. You can do this with `str()`:

`message = 'Score: ' + str(score)`

**Tip:** `str()` is short for 'string' — programmers often remove letters like this, so they don't have to type as much!

--- /task ---

### Game over!

When a player has collided with an obstacle, the game should stop moving and their score should stop increasing.

--- task ---

You can use the `level` variable to signal 'Game over' by setting it to 0 — a value it will never reach any other way. Do this in the `else` step of your colision detection code.

--- /task ---

--- task ---

Create an `if` statement in `draw()` that tests whether `level > 0` before calling any of the functions — like `background()`, `draw_obstacles()`, and `draw_player()` — that update the game. Because these functions are not called, the entire game seems to end, even though your program is still running.

--- /task ---

--- task ---

**Debug:** You might find some bugs in your project that you need to fix. Here are some common bugs.

--- collapse ---
---
title: The score doesn't display
---

Make sure that you've included the `text()` function that draws the player's score at the appropriate point in your `draw()` function, and that you've passed it the correct values:

`text('Text to display', x, y)`

It should look something like this:

--- code ---
---
language: python
filename: main.py — draw()
---

  if level > 0: background(safe) fill(255) text('Score: ' + str(score), width/2, 20) draw_obstacles() draw_player()

--- /code ---

--- /collapse ---

--- collapse ---
---
title: The game doesn't stop after a collision
---

If you think your game might not be correctly detecting collisions at all, first try the debug instructions in the previous step, under 'There is no collision when the player reaches an obstacle'.


If your game is correctly detecting collisons, then check that you have properly indented the code that draws your game inside the `if level > 0` satement, to make sure it only runs if that statement is true. For example:

--- code ---
---
language: python
filename: main.py — draw()
---

  if level > 0: background(safe) fill(255) text('Score: ' + str(score), width/2, 20) draw_obstacles() draw_player()

--- /code ---

Finally, if both of those are working correctly, your game may not be setting `level = 0` correctly when a collision happens. For example:

--- code ---
---
language: python
filename: main.py — draw_player()
---

  if collide == safe: text('🎈', mouse_x, player_y) score += level else: text('💥', mouse_x, player_y) level = 0

--- /code ---

--- /collapse ---

--- collapse ---
---
title: The game doesn't get faster
---

First, check that `level` is increasing correctly. You should see a message printed out every time it goes up. If this isn't happening, check both the code for printing the message and the code for increasing the level.

If level is increasing correctly, check your `draw_obstacles()` function. In particular, check that you have `ob_y = randint(0, height) + (frame_count * level)`. It should look something like this:

--- code ---
---
language: python filename: main.py — draw_obstacles()
line_numbers: false
---

  for i in range(6 + level): ob_x = randint(0, height) ob_y = randint(0, height) + (frame_count * level) ob_y %= height #Wrap around text('🌵', ob_x, ob_y)

--- /code ---

--- /collapse ---

--- collapse ---
---
title: New obstacles don't appear
---

There are a few reasons this could be happening. And there are some more reasons why it might appear to be happening, when it isn't. First, because new obstacles are added based on `level`, check that `level` is increasing correctly. You should see a message printed out every time it goes up. If this isn't happening, check both the code for printing the message and the code for increasing the level.

If level is increasing correctly, check your `draw_obstacles()` function to ensure that you have `level` used in the `range()` function of the `for` loop that draws the obstacles. It should look something like this:

--- code ---
---
language: python filename: main.py — draw_obstacles()
line_numbers: false
---

  for i in range(6 + level): ob_x = randint(0, height) ob_y = randint(0, height) + (frame_count * level) ob_y %= height #Wrap around text('🌵', ob_x, ob_y)

--- /code ---

If you've done all these checks and it still doesn't look like the number of obstacles is increasing, it's possible that they are but you aren't seeing it. You should try some of these steps to test this:
  - Slow the game down by using `frame_rate()` in your `setup()` function to give you more time to count
  - Change the seed you're using for your random numbers. It's unlikely, but it is possible that some obstacles are randomly appearing directly on top of each other
  - Add a `print()` to the `for` loop in `draw_obstacles()` that prints out the value of `i` in each pass of the loop, so you can verify whether it's running the number of times it should
  - Just for testing purposes, change `range(6 + level)` to `range(6 * level)` — that increase should be easier to spot!


--- /collapse ---

--- /task ---

--- save ---
