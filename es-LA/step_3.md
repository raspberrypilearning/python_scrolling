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
filename: main.py - dibujar_obstaculos()
---

def dibujar_obstaculos(): 
   obstaculo_x = width/2 
   obstaculo_y = height/2 
   text('🌵', obstaculo_x, obstaculo_y) #Reemplázalo con tu obstáculo


--- /code ---

Agrega código a `draw()` para llamar a tu función `dibujar_obstaculos()` cada cuadro (frame).

--- code ---
---
language: python
filename: main.py - draw()
---

def draw(): 
    a_salvo = color(200, 100, 0) #Agrega el color de tu tema 
    background(a_salvo)  
    dibujar_obstaculos() #Antes de dibujar tu jugador 
    dibujar_jugador()

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

def setup(): 
    size(400, 400) 
    jugador = load_image('skiing.png') #Carga la imagen de tu jugador 
    obstaculo = load_image('rocket.png') #Carga la imagen de tu obstáculo

--- /code ---

Llama a tu imagen con `image()` y configúralo como global en la función `dibujar_obstaculos()`.

--- code ---
---
language: python
filename: main.py - dibujar_obstaculos()
---

def dibujar_obstaculos(): 
   obstaculo_x = width/2 
   obstaculo_y = height/2

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
filename: main.py - dibujar_obstaculos()
---

def dibujar_obstaculos(): 
  obstaculo_x = width/2 
  obstaculo_y = height/2 
  text('🌵', obstaculo_x, obstaculo_y)

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
filename: main.py - dibujar_obstaculos()
---

def dibujar_obstaculos(): 
    obstaculo_x = width/2 
    obstaculo_y = height/2 #Dibuja un árbol de pino 
    no_stroke() 
    fill(0,255,0) # Verde para la hojas 
    triangle(obstaculo_x + 20, obstaculo_y + 20, obstaculo_x + 10, obstaculo_y + 40, obstaculo_x + 30, obstaculo_y + 40) 
    triangle(obstaculo_x + 20, obstaculo_y + 30, obstaculo_x + 5, obstaculo_y + 55, obstaculo_x + 35, obstaculo_y + 55) 
    triangle(obstaculo_x + 20, obstaculo_y + 40, obstaculo_x + 0, obstaculo_y + 70, obstaculo_x + 40, obstaculo_y + 70) 
    fill(150,100,100) # Marrón para el tronco 
    rect(obstaculo_x + 15, obstaculo_y + 70, 10, 10)

--- /code ---

--- /collapse ---

--- /task ---

### Haz que tu obstáculo se mueva

--- task ---

Ahora agrega código para aumentar la posición `y` del obstáculo en cada cuadro (frame), y haz que se envuelva cuando llegue al fondo para crear el efecto de otro obstáculo.

La variable `frame_count` de la biblioteca p5 comienza a contar los cuadros (frames) cuando haces clic en run (ejecutar).

`obstaculo_y %= height` fija la posición `y` en el resto cuando se divide por `height`. Con una `height` (altura) de '400', esto convertirá `401` en `1`, de modo que cuando los obstáculos desaparezcan de la parte inferior de la pantalla, reaparecerán en la parte superior.

--- code ---
---
language: python
filename: main.py - dibujar_obstaculos()
---

def dibujar_obstaculos(): 
   obstaculo_x = width/2 
   obstaculo_y = height/2 + frame_count #Aumenta cada frame 
   obstaculo_y %= height #Recircular 
   text('🌵', obstaculo_x, obstaculo_y) #Reemplaza con tu obstáculo

--- /code ---

--- /task ---

### Muchos obstáculos

Podrías dibujar muchas copias de tu obstáculo con diferentes posiciones de inicio, pero eso sería mucho trabajo. Usemos un atajo.


<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;"> 
<span style="color: #0faeb0">**Procedural generation**</span> (Generación de procedimientos) se usa en la creación de mundos para juegos, obstáculos y escenas de películas para crear aleatoriedad, pero donde aplican algunas reglas. Una <span style="color: #0faeb0">seed</span> (semilla) significa que puedes generar los mismos resultados cada vez que uses la misma semilla.</p>

--- task ---

Este código usa un bucle `for` con `randint()` para elegir las posiciones de los obstáculos por ti. Si llamas primero a la función aleatoria `seed()` significa que siempre obtendrás los mismos números aleatorios. Esto significa que los obstáculos no saltarán alrededor de cada cuadro (frame) y puedes cambiar la semilla hasta que obtengas una que coloque los obstáculos de manera balanceada.

--- code ---
---
language: python
filename: main.py - dibujar_obstaculos()
---

def dibujar_obstaculos():

  seed(12345678) #Cualquier número funcionará

  for i in range(6):  
    obstaculo_x = randint(0, height) 
    obstaculo_y = randint(0, height) + frame_count 
    obstaculo_y %= height 
    text('🌵', obstaculo_x, obstaculo_y) #Reemplaza con tu obstáculo

--- /code ---

Información útil:

[[[using-seed-in-python]]]

[[[generic-python-for-loop-repeat]]]

--- /task ---

--- collapse ---
---
title: Advertencia de epilepsia
---

Probar tu programa tiene el potencial de inducir convulsiones en personas con epilepsia fotosensible. Si tienes epilepsia fotosensible o sientes que puedes ser susceptible a una convulsión, no ejecutes tu programa. En su lugar, puedes:
- Asegúrate de haber agregado la línea de código `seed ()` para asegurarte de que tus obstáculos no salten
- Pídele a alguien que lo ejecute por ti
- Continúa y completa el proyecto, pídele a alguien que ejecute el proyecto por ti cuando acabes para que puedas depurar
- Cambia la velocidad de fotogramas antes de ejecutar tu programa agregando `frame_rate(1)` al comienzo de `setup()`; puedes eliminar esto una vez que hayas confirmado que no hay ningún error

--- /collapse ---

--- task ---

**Prueba:** Ejecuta tu programa y deberías ver múltiples objetos en la pantalla, envolviéndose cuando llegan al fondo.

Modifica tu código hasta que estés satisfecho con los obstáculos que tienes. Puedes:

+ Cambiar la semilla (seed) para conseguir obstáculos en diferentes posiciones de inicio
+ Cambiar la cantidad de veces que se repite el bucle para obtener una cantidad diferente de obstáculos
+ Ajustar el tamaño de los obstáculos

**Sugerencia:** Asegúrate de que es posible evitar los obstáculos, pero que no exista un camino demasiado fácil en el juego.

--- /task ---

--- task ---

**Depuración:** Es posible que encuentres algunos errores en tu proyecto que tendrás que corregir. Aquí hay algunos errores comunes.

--- collapse ---
---
title: Solo se dibuja un obstáculo
---

Comprueba que tu función dibuje múltiples obstáculos:
 + Asegúrate de que use un bucle `for` para llamar a la función de dibujo de obstáculos más de una vez
 + Asegúrate de que esté usando `randint()` para cambiar las coordenadas (x, y) que está pasando a la función de dibujo de obstáculos
 + Comprueba que haz utilizado `obstaculo_x` y `obstaculo_y` como las coordenadas de tu obstáculo

Por ejemplo:

--- code ---
---
language: python
filename: main.py — dibujar_obstaculos()
---

def dibujar_obstaculos():

  seed(12345678)

  for i in range(6):  
    obstaculo_x = randint(0, height) 
    obstaculo_y = randint(0, height) + frame_count 
    obstaculo_y %= height 
    text('🌵', obstaculo_x, obstaculo_y) #Reemplaza con tu obstáculo

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Los obstáculos cambian de posición cada vez que se dibuja un fotograma
---

Asegúrate de haber usado `seed()` dentro de la función que dibuja múltiples obstáculos.

--- /collapse ---

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;"> 
Los programadores usan muchos trucos ingeniosos como usar el operador `%` para hacer que los objetos recirculen en la pantalla y la función `seed()` para generar los mismos números aleatorios. Cuanto más codifiques, mejores trucos aprenderás.</p>

--- save ---
