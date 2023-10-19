## Detección de colisiones

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Los juegos tipo endless runner a menudo terminan cuando el jugador choca contra un obstáculo.
</div>
<div>

![Imagen del paso completado.](images/collision.png){:width="300px"}

</div>
</div>

Ahora puedes configurar tu jugador para que reaccione ante la colisión contra un obstáculo.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">**Collision detection**</span> (Detección de colisiones) es determinante cuando dos objetos son creados dentro de una simulación por computadora se tocan; ya sea en un juego, una animación, o algo más. Hay varias maneras de hacer esto, por ejemplo: 
  - verificar si los colores que aparecen en la ubicación de un objeto son los colores de ese objeto, o uno diferente
  - hacer un seguimiento de la forma de cada objeto y verificar si  las formas se superponen
  - crear un conjunto de puntos límite, o líneas, alrededor de un objeto y verificar si entran en contacto con otros objetos 'colisionables'
Cuando se detecta una colisión de este tipo, el programa puede reaccionar de alguna manera. In a video game, this is usually to deal damage (if the player collides with an enemy or hazard) or to give a benefit (if the player collides with a power up).
</p>

--- task ---

In your `draw_player()` function, create a variable called `collide` and set it to get the hexadecimal (hex) colour value at the position of the player.

--- code ---
---
language: python
filename: main.py - draw_player()
---

    collide = get(mouse_x, player_y).hex

--- /code ---

--- /task ---

--- task ---

Create a condition to check `if` the `collide` variable is the same as the `safe` variable — if it is, then your player is safely touching the background and has not collided with an obstacle.

Move your code to draw your player inside your `if collide == safe` condition and add code in the `else` statement to get the player to react to the collision.

**Choose:** How should your player react? You could:
+ Use a different emoji for the player
+ You could use `tint()` to change the appearance of an image, don't forget to call `no_tint()` after drawing the image

--- collapse ---
---
title: Use emoji characters
---

You can use emoji characters in the p5 `text()` function to represent your collided player.

Here's an example:

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
filename: main.py - draw_player()
---

def draw_player(): if collide == safe.hex:  # On background text('🎈', mouse_x, player_y) else:  # Collided text('💥', mouse_x, player_y)

--- /code ---

--- /collapse ---

[[[processing-tint]]]

[[[generic-theory-simple-colours]]]

--- /task ---

--- task ---

**Test:** Check if a collision is detected and the reaction takes place each time a collision occurs.

--- /task ---

--- task ---

**Debug:** You might find some bugs in your project that you need to fix. Here are some common bugs.

--- collapse ---
---
title: There is no collision when the player reaches an obstacle
---

If your player character touches the obstacle and nothing happens, there are a few things you should check:

 - Make sure you call `draw_obstacles()` before `draw_player()`. Si verificas las colisiones antes de dibujar los obstáculos en un cuadro (frame), ¡entonces no habrá obstáculos con los que chocar!
 - Asegúrate de estar usando exactamente el mismo color cuando dibujes el objeto y en la sentencia `if` cuando estés verificando la colisión. Puedes asegurarte de esto usando la misma variable `global` en ambos lugares.
 - ¿Estás dibujando el personaje del jugador antes de verificar el color en las coordenadas del ratón (mouse)? Si es así, solo obtendrás los colores del jugador. Primero deberías verificar el color y **después** dibujar al jugador.
 - Do you have code in the `else` part to do something different when a collision is detected, such as applying a tint or using an emoji?
 - ¿Has indentado (dado sangría) correctamente tu código para tu sentencia `if` para que se ejecute cuando se cumpla la condición?

Printing the colour of the pixel you are checking for a collision can be useful:

```python
    print(red(collide), green(collide), blue(collide))
```

You can also print a circle around the point you are checking and adjust the point you check if you need to:

```python
    no_fill()
    ellipse(mouse_x, player_y, 10, 10)  # Draw collision point
```

--- /collapse ---

--- /task ---

--- task ---

**Optional:** At the moment, you are just detecting collisions at one pixel on your player. You could also detect collisions at other pixels at the edge of your player, such as the bottom or left- and right-most edges.

--- collapse ---
---
title: Collision detection with multiple pixels
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
