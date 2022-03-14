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
language: python
filename: main.py - draw_obstacles()
---

def dibujar_obstaculos(): obstaculo_x = width/2 obstaculo_y = height/2 text('🌵', obstaculo_x, obstaculo_y) #Reemplázalo con tu obstáculo


--- /code ---

Add code to `draw()` to call `draw_obstacles()` each frame.

--- code ---
---
language: python
filename: main.py - draw()
---

def draw(): a_salvo = color(200, 100, 0) #Agrega el color de tu tema background(a_salvo)  
dibujar_obstaculos() #Antes de dibujar tu jugador dibujar_jugador()

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

Haz clic en el ícono **manage images** (administrar imágenes).

![El ícono de la imagen en la parte superior derecha del área del código.](images/manage-images.png)

Las imagenes incluídas en el proyecto inicial se mostrarán en una lista al hacer clic en `Image library` (Biblioteca de imágenes).

![La biblioteca de imágenes (Image library) con una lista de imágenes incluidas.](images/starter-images.png)

Apunta el nombre de la imagen que quieras utilizar.

Carga la imagen ('load_image') dentro de la función `setup()`.

--- code ---
---
language: python
filename: main.py - setup()
---

def setup(): size(400, 400) jugador = load_image('skiing.png') #Carga la imagen de tu jugador obstaculo = load_image('rocket.png') #Carga la imagen de tu obstáculo

--- /code ---

Llama a tu imagen con `image()` y configúralo como global en la función `dibujar_obstaculos()`.

--- code ---
---
language: python
filename: main.py - draw_obstacles()
---

def draw_obstacles(): ob_x = width/2 ob_y = height/2

   global obstaculo

   image(obstaculo, obstaculo_x, obstaculo_y, 30, 30) #Cambia el tamaño para que se adapte a tu tema

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Usa emojis
---

Puedes usar emojis en la función `text()` de la bilbioteca p5 para representar tus obstáculos.

Aquí tienes un ejemplo:

--- code ---
---
language: python
filename: main.py - setup()
---

def setup(): size(400, 400) text_size(40) #Controla el tamaño del emoji text_align(CENTER, TOP) #Ubicado alrededor del centro

--- /code ---

--- code ---
---
language: python
filename: main.py - draw_obstacles()
---

def dibujar_obstaculos(): obstaculo_x = width/2 obstaculo_y = height/2 text('🌵', obstaculo_x, obstaculo_y)

--- /code ---

--- /collapse ---

[[[processing-python-text]]]

[[[generic-theory-simple-colours]]]

[[[processing-python-ellipse]]]

[[[processing-python-rect]]]

[[[processing-python-triangle]]]

[[[processing-tint]]]

[[[processing-stroke]]]

**Sugerencia:** Puedes usar varias formas sencillas en la misma función para crear un obstáculo más complejo.

--- collapse ---
---
title: Dibuja un obstáculo usando múltiples formas
---

![desc](images/tree_obstacle.png)

--- code ---
---
language: python
filename: main.py - draw_obstacles()
---

def draw_obstacles(): ob_x = width/2 ob_y = height/2 #Draw a fir tree no_stroke() fill(0,255,0) #Green for needles triangle(ob_x + 20, ob_y + 20, ob_x + 10, ob_y + 40, ob_x + 30, ob_y + 40) triangle(ob_x + 20, ob_y + 30, ob_x + 5, ob_y + 55, ob_x + 35, ob_y + 55) triangle(ob_x + 20, ob_y + 40, ob_x + 0, ob_y + 70, ob_x + 40, ob_y + 70) fill(150,100,100) # brown for trunk rect(ob_x + 15, ob_y + 70, 10, 10)

--- /code ---

--- /collapse ---

--- /task ---

### Haz que tu obstáculo se mueva

--- task ---

Now add code to increase the `y` position of the obstacle each frame, and have it wrap around when it gets to the bottom to create the effect of another obstacle.

La variable `frame_count` de la biblioteca p5 comienza a contar los cuadros (frames) cuando haces clic en run (ejecutar).

`obstaculo_y %= height` fija la posición `y` en el resto cuando se divide por `height`. Con una `height` (altura) de '400', esto convertirá `401` en `1`, de modo que cuando los obstáculos desaparezcan de la parte inferior de la pantalla, reaparecerán en la parte superior.

--- code ---
---
language: python
filename: main.py - draw_obstacles()
---

def dibujar_obstaculos(): obstaculo_x = width/2 obstaculo_y = height/2 + frame_count #Aumenta cada frame obstaculo_y %= height #Recircular text('🌵', obstaculo_x, obstaculo_y) #Reemplaza con tu obstáculo

--- /code ---

--- /task ---

### Muchos obstáculos

Podrías dibujar muchas copias de tu obstáculo con diferentes posiciones de inicio, pero eso sería mucho trabajo. Usemos un atajo.


<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;"> 
<span style="color: #0faeb0">**Procedural generation**</span> is used in the creation of game worlds, obstacles, and movie scenes to create randomness but with certain rules applied. Una <span style="color: #0faeb0">seed</span> (semilla) significa que puedes generar los mismos resultados cada vez que uses la misma semilla.</p>

--- task ---

Este código usa un bucle `for` con `randint()` para elegir las posiciones de los obstáculos por ti. Si llamas primero a la función aleatoria `seed()` significa que siempre obtendrás los mismos números aleatorios. This means that the obstacles won't jump around every frame and you can change the seed until you get one that positions the obstacles fairly.

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

Change your code until you are happy with the obstacles you have. You can:

+ Change the seed to get obstacles in different starting positions
+ Change the number of times to loop repeats to get a different number of obstacles
+ Adjust the size of the obstacles

**Tip:** Make sure it is possible to avoid your obstacles but that there is no easy path through your game.

--- /task ---

--- task ---

**Debug:** You might find some bugs in your project that you need to fix. Here are some common bugs.

--- collapse ---
---
title: Only one obstacle is being drawn
---

Check your function that draws multiple obstacles:
 + Make sure it uses a `for` loop to call the obstacle drawing function more than once
 + Make sure it uses `randint()` to change the (x, y) coordinates it is passing to the obstacle drawing function
 + Check that you have used `ob_x` and `ob_y` as the coordinates for your obstacle

For example:

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
