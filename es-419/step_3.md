## Crea los obstáculos

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Crea los obstáculos que tendrás que esquivar para seguir jugando.
</div>
<div>

![Ejemplo del proyecto esquiando con obstaculos de árboles](images/obstacles.png){:width="300px"}

</div>
</div>

### Empieza con un único obstáculo

Puedes crear obstáculos de la misma manera que creaste tu jugador. ¿Cómo encajan estos obstáculos con tu tema?

Vas a usar un bucle `for` para crear muchas copias, así que solo tendrás que crear o elegir un único obstáculo.

--- task ---

Define una función `dibujar_obstaculos()`:

--- code ---
---
language: python filename: main.py - draw_obstacles() line_numbers: false line_number_start:
line_highlights: 4
---

def draw_obstacles(): ob_x = width/2 ob_y = height/2 text('🌵', ob_x, ob_y)  # Replace with your obstacle

--- /code ---

Agrega código a `draw()` para llamar a tu función `dibujar_obstaculos()` cada cuadro (frame).

--- code ---
---
language: python filename: main.py - draw() line_numbers: false line_number_start:
line_highlights: 5
---

def draw(): global safe safe = Color(200, 100, 0)  # Add the colour of your theme background(safe) draw_obstacles()  # Before drawing the player draw_player()

--- /code ---

--- /task ---

--- task ---

**Elige:** ¿Cómo luce tu obstáculo? Tu obstáculo podría ser:
+ Una imagen proporcionada en el proyecto inicial
+ Un emoji 🌵 o texto
+ Un dibujo hecho combinando varias formas

--- collapse ---
---
title: Usa una imagen de inicio
---

Images included in the starter project will be shown in the `Image gallery`.

![The Image gallery displaying the included images.](images/starter-images.png)

Make a note of the name of the image you want to use.

Load the image into the `setup()` function

--- code ---
---
language: python filename: main.py - setup() line_numbers: true line_number_start: 9
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
title: Usa emojis
---

You can use emoji characters in the p5 `text()` function to represent your obstacles.

Here's an example:

--- code ---
---
language: python
filename: main.py - setup()
---

def setup(): size(400, 400) text_size(40)  # Controls the size of the emoji text_align(CENTER, TOP)  # Position around the centre

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
title: Dibuja un obstáculo usando múltiples formas
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

### Haz que tu obstáculo se mueva

--- task ---

Now add code to increase the `y` position of the obstacle each frame, and have it wrap around when it gets to the bottom to create the effect of another obstacle.

The p5 `frame_count` variable starts counting the frames when you click run.

`ob_y %= height` sets the `y` position to the remainder when divided by `height`. With a `height` of '400', this will turn `401` into `1` so when the obstacles goes off the bottom of the screen, it reappears at the top.

--- code ---
---
language: python
filename: main.py - draw_obstacles()
---

def draw_obstacles(): ob_x = width/2 ob_y = height/2 + frame_count  # Increases each frame ob_y %= height  # Wrap around text('🌵', ob_x, ob_y)  # Replace with your obstacle

--- /code ---

--- /task ---

### Muchos obstáculos

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

def draw_obstacles(): seed(12345678)  # Any number is fine

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
title: Advertencia de epilepsia
---

Testing your program has the potential to induce seizures for people with photosensitive epilepsy. If you have photosensitive epilepsy or feel you may be susceptible to a seizure, do not run your program. Instead, you can:
- Asegúrate de haber agregado la línea de código `seed ()` para asegurarte de que tus obstáculos no salten
- Pídele a alguien que lo ejecute por ti
- Continúa y completa el proyecto, pídele a alguien que ejecute el proyecto por ti cuando acabes para que puedas depurar
- Slow the game down by using `frame_rate = 10` in your call to `run()` like this:

```python
run(frame_rate = 10)
```
You can alter the speed of the game by changing `10` to a higher or lower value.

--- /collapse ---

--- task ---

**Test:** Run your program and you should see multiple objects on the screen, wrapping around when they get to the bottom.

Change your code until you are happy with the obstacles you have. You can:

+ Cambiar la semilla (seed) para conseguir obstáculos en diferentes posiciones de inicio
+ Cambiar la cantidad de veces que se repite el bucle para obtener una cantidad diferente de obstáculos
+ Ajustar el tamaño de los obstáculos

**Tip:** Make sure it is possible to avoid your obstacles but that there is no easy path through your game.

--- /task ---

--- task ---

**Debug:** You might find some bugs in your project that you need to fix. Here are some common bugs.

--- collapse ---
---
title: Solo se dibuja un obstáculo
---

Check your function that draws multiple obstacles:
 + Asegúrate de que use un bucle `for` para llamar a la función de dibujo de obstáculos más de una vez
 + Asegúrate de que esté usando `randint()` para cambiar las coordenadas (x, y) que está pasando a la función de dibujo de obstáculos
 + Comprueba que haz utilizado `obstaculo_x` y `obstaculo_y` como las coordenadas de tu obstáculo

For example:

--- code ---
---
language: python
filename: main.py — draw_obstacles()
---

def draw_obstacles(): seed(12345678)

    for i in range(6):  
        ob_x = randint(0, height)
        ob_y = randint(0, height) + frame_count
        ob_y %= height
        text('🌵', ob_x, ob_y)  # Replace with your obstacle

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Los obstáculos cambian de posición cada vez que se dibuja un fotograma
---

Make sure that you have used `seed()` inside the function that draws multiple obstacles.

--- /collapse ---

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;"> 
Programmers use lots of neat tricks like using the `%` operator to make objects wrap around the screen and the `seed()` function to generate the same random numbers. The more coding you do, the more neat tricks you will learn.</p>

--- save ---
