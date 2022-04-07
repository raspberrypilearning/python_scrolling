## Elige el tema

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Elige el tema de tu juego y crea un personaje que siga el puntero del ratón (mouse).

</div>
<div>

![Imagen de una tortuga de tamaño 100x100 con un fondo azul con un tamaño de pantalla de 400x400.](images/theme-turtle.png){:width="300px"}

</div>
</div>

¿Cuál es el tema de tu juego? Puedes elegir el que quieras. Aquí tienes algunas sugerencias:
- Un deporte o pasatiempo
- Una película, programa de Tv o juego
- Ciencias o naturaleza
- ¡Cualquier otro tema!

--- task ---

Abre el [proyecto inicial](https://trinket.io/python/f7d338e40f){:target="_blank"}. Trinket se abrirá en otra pestaña del navegador.

--- /task ---

--- task ---

**Elige:** Delimita el tamaño de tu canvas (espacio de trabajo).

--- code ---
---
language: python
filename: main.py - setup()
---

def setup():    
    size(400, 400)

--- /code ---

--- /task ---

--- task ---

Crea una variable llamada `a_salvo` para almacenar el color de fondo según el tema que elegiste para tu juego.

Este es el color en el que tu personaje estará a salvo, más adelante tendrás que usar esta variable nuevamente.

--- code ---
---
language: python
filename: main.py - draw()
---

def draw():    
    a_salvo = color(200, 100, 0) #Agrega el color de tu tema   
    background(a_salvo)

--- /code ---

[[[generic-theory-simple-colours]]]

--- /task ---

--- task ---

**Prueba:** Ejecuta tu código para ver el color de fondo. Cámbialo hasta que estés satisfecho con el color y el tamaño de la pantalla.

--- /task ---

Ahora elige el personaje que va a jugar y evitar los obstáculos. ¿Es un objeto, una persona, un animal o algo más?

Tu jugador aparecerá en una posición fija de `y` y en la misma posición de `x` que el puntero del ratón (mouse), que se almacena en la variable `mouse_x` de la biblioteca `p5`.

--- task ---

Es una buena idea organizar el código para dibujar tu personaje dentro de una función.

Define una función `dibujar_jugador()` y crea una posición `jugador_y` para la posición fija `y` del jugador:

--- code ---
---
language: python
filename: main.py - dibujar_jugador()
---

def dibujar_jugador():    
  jugador_y = int(height * 0.8) #Ubicado en la parte inferior de la pantalla

--- /code ---

Agrega código a `draw()` para llamar a tu función `dibujar_jugador()` cada cuadro (frame).

--- code ---
---
language: python
filename: main.py - draw()
---

def draw():    
    a_salvo = color(200, 100, 0) #Tu color elegido    
    background(a_salvo)    
    dibujar_jugador()

--- /code ---

--- /task ---

Luego, agregarás código a la función `dibujar_jugador()` para dibujar tu forma. Probablemente también tengas que agregar código para `setup()`.

--- task ---

**Elige:** ¿Cómo luce tu personaje? Este podría ser:
+ Una imagen proporcionada en el proyecto inicial
+ Un emoji 🎈 o texto
+ Un dibujo hecho con varias formas

--- collapse ---
---
title: Usa una imagen de inicio
---

Haz clic en el ícono **manage images** (administrar imágenes).

![El ícono de la imagen en la parte superior derecha del área del código.](images/manage-images.png)

Las imagenes incluídas en el proyecto inicial se mostrarán en una lista al hacer clic en `Image library` (Biblioteca de imágenes).

![La biblioteca de imágenes (Image library) con la lista de imágenes incluidas.](images/starter-images.png)

Apunta el nombre de la imagen que quieras utilizar.

Carga la imagen ('load_image') dentro de la función `setup()`

--- code ---
---
language: python
filename: main.py - setup()
---

def setup():   
    size(400, 400)    
    jugador = load_image('skiing.png') #Carga tu imagen

--- /code ---

Llama a tu imagen con `image()` y configúralo como global en la función `dibujar_jugador()`.

--- code ---
---
language: python
filename: main.py - dibujar_jugador()
---

def dibujar_jugador():    
  jugador_y = int(height * 0.8) #Ubicado en la parte inferior de la pantalla

  global jugador

  image(jugador, mouse_x, jugador_y, 30, 30)

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Usa emojis
---

Puedes usar emojis con la función `text()` de la bilbioteca p5 para representar a tu jugador.

Aquí tienes un ejemplo:

--- code ---
---
language: python
filename: main.py - setup()
---

def setup():    
  size(400, 400)     
  text_size(40) #Controla el tamaño del emoji     
  text_align(CENTER, TOP) #Ubicado alrededor del centro

--- /code ---

--- code ---
---
language: python
filename: main.py - dibujar_jugador()
---

def dibujar_jugador():     
  jugador_y = int(height * 0.8)    
  text('🎈', mouse_x, jugador_y)

--- /code ---

--- /collapse ---

[[[processing-python-text]]]

[[[generic-theory-simple-colours]]]

[[[processing-python-ellipse]]]

[[[processing-python-rect]]]

[[[processing-python-triangle]]]

[[[processing-tint]]]

[[[processing-stroke]]]

**Sugerencia:** Puedes usar varias formas sencillas en la misma función para crear un jugador más complejo.

--- collapse ---
---
title: Dibuja un personaje usando múltiples formas
---

![desc](images/face_player.png)

--- code ---
---
language: python
filename: main.py - dibujar_jugador()
---

def dibujar_jugador():    
  jugador_y = int(height * 0.8)    
  noStroke()    
  #Cara    
  fill(0, 200, 100)    
  ellipse(mouse_x, jugador_y, 60, 60)

  #Ojos    
  fill(0, 100, 200)    
  ellipse(mouse_x - 10, jugador_y - 10, 20, 20)    
  ellipse(mouse_x + 10, jugador_y - 10, 20, 20)    
  fill(0)    
  ellipse(mouse_x - 10, jugador_y - 10, 10, 10)     
  ellipse(mouse_x + 10, jugador_y - 10, 10, 10)     
  fill(255)    
  ellipse(mouse_x - 12, jugador_y - 12, 5, 5)    
  ellipse(mouse_x + 12, jugador_y - 12, 5, 5)

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

**Prueba:** Ejecuta tu código y mueve el ratón (mouse) para controlar a tu jugador.

¿Se mueve como lo esperabas?

--- /task ---

**Depuración:** Es posible que encuentres algunos errores en tu proyecto que tendrás que corregir. Aquí hay algunos errores comunes.

--- task ---

--- collapse ---
---
title: No puedo ver el jugador
---

Intenta cambiar a pantalla completa. Además, verifica las coordenadas `x` e `y` que usaste para dibujar tu jugador; asegúrate de que estén dentro del canvas (espacio de trabajo) que creaste con `size()`.

--- /collapse ---

--- collapse ---
---
title: Una imagen no se carga
---

Primero, asegúrate de que la imagen esté en `Image library` (Biblioteca de imágenes). Luego, lee el nombre del archivo con mucho cuidado: recuerda que las letras mayúsculas son diferentes a las minúsculas y que la puntuación es importante.

--- /collapse ---

--- collapse ---
---
title: Una imagen tiene el tamaño incorrecto
---

Comprueba las entradas (inputs) que controlan el ancho (width) y el alto (height) de la imagen:

```python
image(Archivo_de_imagen, coordenada_x, coordenada_y, ancho, alto)
```

--- /collapse ---

--- collapse ---
---
title: Un emoji tiene el tamaño incorrecto
---

Si tu emoji es demasiado grande o pequeño, cambia la entrada de `text_size()`.

--- /collapse ---

--- /task ---

--- save ---
