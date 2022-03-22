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
language: python 
filename: main.py
line_numbers: false
---

#Incluye variables globales aquí
nivel = 1

--- /code ---

--- /task ---

--- task ---

Este código usa `height` (altura) y `frame_count` (recuento de cuadros o fotogramas) para aumentar la variable `nivel` cada vez que el jugador despeja una pantalla, luego genera el nuevo nivel para el jugador.

**Elige:** Este código limita los niveles a cinco, para que no sea demasiado difícil de jugar. No hay ninguna razón por la que tu juego tenga que usar cinco niveles, pero deberías elegir un límite. ¡Los humanos tienen límites para moverse!

--- code ---
---
language: python 
filename: main.py — draw_obstacles()
line_numbers: false
---

def dibujar_obstaculos():

  global nivel #Usa el nivel global

  if frame_count % height == height - 1 and nivel < 5: 
    nivel += 1 
    print('Llegaste al nivel', nivel)

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
language: python 
filename: main.py — draw_obstacles()
line_numbers: false
---

  for i in range(6): 
    obstaculo_x = randint(0, height) 
    obstaculo_y = randint(0, height) + (frame_count * nivel) 
    obstaculo_y %= height #Recircular 
    text('🌵', obstaculo_x, obstaculo_y)

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Agrega más obstáculos
---

Puedes agregar obstáculos adicionales tan solo aumentando la cantidad de veces que se ejecuta el bucle `for` que los crea. Puedes hacer esto aumentando el número que le pasas a la función `range()` por `nivel`.

**Sugerencia:** Siempre puedes usar `nivel* 2`, o incluso múltiplos más grandes, si quieres aumentar la dificultad de tu juego.

--- /collapse ---

--- /task ---

### Registra el puntaje

Cuanto más dure un jugador sin chocar contra un obstáculo, mejor estarán jugando. Agregar el puntaje les permitirá ver qué tan bien lo están haciendo.

--- task ---

Crea una variable global `puntaje` para hacer el seguimiento del puntaje del jugador. Establécela en `0` para que los jugadores nuevos empiecen con cero puntos.

--- code ---
---
language: python 
filename: main.py
line_numbers: false
---

#Incluye variables globales aquí
puntaje = 0

--- /code ---

--- /task ---

--- task ---

Puedes aumentar el puntaje de tu jugador por cada cuadro (frame) en el que no haya chocado con un obstáculo, aumentando su puntaje cuando compruebe si hay colisión en `dibujar_jugador()`.

**Elige:** Puedes decidir cuántos puntos vale cada cuadro (frame), pero incrementar el puntaje del jugador por `nivel` premia a los jugadores que pueden sobrevivir en niveles de dificultad más altos.

--- code ---
---
language: python
filename: main.py — draw_player()
---

global puntaje

  if colision == a_salvo: 
    text('🎈', mouse_x, jugador_y) 
    puntaje += nivel 
  else: 
    text('💥', mouse_x, jugador_y)

--- /code ---

--- /task ---

--- task ---

Los jugadores deberían poder ver su puntaje. Como este aumenta tan rápido, usar `print()` no funcionaría muy bien. Usa en su lugar, la función `text()` de la biblioteca p5, dentro de tu función `draw()` para mostrarlo como texto en la pantalla del juego.

[[[processing-python-text]]]

Puedes usar el operador `+` para combinar dos o más cadenas si quieres darle un título como 'puntaje' o 'puntos'. Debido a que `puntaje` es un número, tendrás que convertirlo en una cadena antes de poder unirlo con otra cadena. Puedes hacer esto con `str()`:

`mensaje = 'Puntaje: ' + str(puntaje)`

**Sugerencia:** `str()` es la abreviatura de 'string' (cadena); los programadores a menudo eliminan letras como esta, ¡para no tener que escribir tanto!

--- /task ---

### ¡Fin del juego!

Cuando un jugador ha chocado con un obstáculo, el juego debería dejar de moverse y su puntaje debería dejar de aumentar.

--- task ---

Puedes usar la variable `nivel` para señalar el 'Fin del juego' estableciendola en 0, un valor que no puede alcanzarse de otra manera. Haz esto en el paso `else` de tu código de detección de colisiones.

--- /task ---

--- task ---

Crea una sentecia `if` dentro de `draw()` que compruebe si `nivel > 0` antes de llamar alguna función como `background()`, `dibujar_obstaculos()`, y `dibujar_jugador()`; ya que estas actualizan el juego. Debido a que estas funciones no pueden llamarse, todo el juego parece llegar a su fin, aunque tu programa todavía se siga ejecutando.

--- /task ---

--- task ---

**Depuración:** Es posible que encuentres algunos errores en tu proyecto que tendrás que corregir. Aquí hay algunos errores comunes.

--- collapse ---
---
title: El puntaje no se muestra
---

Asegúrate de haber incluido la función `text()` que dibuja el puntaje del jugador en el punto apropiado en tu función `draw()` y también de haberle dado los valores correctos:

`texto('Texto a mostrar', x, y)`

Debería verse parecido a lo siguiente:

--- code ---
---
language: python
filename: main.py — draw()
---

  if nivel > 0: 
    background(a_salvo) 
    fill(255) 
    text('Puntaje: ' + str(puntaje), width/2, 20) 
    dibujar_obstaculos() 
    dibujar_jugador()

--- /code ---

--- /collapse ---

--- collapse ---
---
title: El juego no se detiene después de una colisión
---

Si crees que tal vez tu juego no está detectando correctamente las colisiones, prueba primero las instrucciones de depuración del paso anterior, en "No hay colisión cuando el jugador alcanza un obstáculo".


Si tu juego está detectando colisiones correctamente, verifica que hayas indentado (dado sangría) correctamente el código que dibuja tu juego y que esté dentro de la sentencia `if nivel > 0`, para asegurarte de que solo se ejecute si esta es verdadera. Por ejemplo:

--- code ---
---
language: python
filename: main.py — draw()
---

  if nivel > 0: 
    background(a_salvo) 
    fill(255) 
    text('Puntaje: ' + str(puntaje), width/2, 20) 
    dibujar_obstaculos() 
    dibujar_jugador()

--- /code ---

Finalmente, si ambos funcionan correctamente, es posible que tu juego no esté configurando `nivel = 0` correctamente cuando ocurre una colisión. Por ejemplo:

--- code ---
---
language: python
filename: main.py — draw_player()
---

  if colision == a_salvo: 
    text('🎈', mouse_x, jugador_y) 
    puntaje += nivel 
  else: 
    text('💥', mouse_x, jugador_y) 
    nivel = 0

--- /code ---

--- /collapse ---

--- collapse ---
---
title: El juego no acelera
---

Primero, verifica que el `nivel` esté aumentando correctamente. Deberías ver un mensaje impreso cada vez que sube. Si esto no sucede, verifica tanto el código para imprimir el mensaje como el código para aumentar el nivel.

Si el nivel aumenta correctamente, verifica tu función `dibujar_obstaculos()`. En particular, verifica que tenga `obstaculo_y = randint(0, height) + (frame_count * nivel)`. Debería verse parecido a lo siguiente:

--- code ---
---
language: python 
filename: main.py — draw_obstacles()
line_numbers: false
---

  for i in range(6 + nivel): 
    obstaculo_x = randint(0, height) 
    obstaculo_y = randint(0, height) + (frame_count * nivel) 
    obstaculo_y %= height #Recircular 
    text('🌵', obstaculo_x, obstaculo_y)

--- /code ---

--- /collapse ---

--- collapse ---
---
title: No aparecen nuevos obstáculos
---

Hay algunas razones por las que esto podría estar sucediendo. Y hay algunas otras más por las que podría parecer que esto está sucediendo, cuando no es así. Primero, debido a que los nuevos obstáculos se agregan en base al `nivel`, verifica que el `nivel` esté subiendo correctamente. Deberías ver un mensaje impreso cada vez que sube. Si esto no sucede, verifica tanto el código para imprimir el mensaje como el código para aumentar el nivel.

Si el nivel aumenta correctamente, verifica tu función `dibujar_obtaculos()` para asegurarte de que tienes `nivel` utilizado en la función `range()` del bucle `for` que dibuja los obstáculos. Debería verse parecido a lo siguiente:

--- code ---
---
language: python 
filename: main.py — draw_obstacles()
line_numbers: false
---

  for i in range(6 + nivel): 
    obstaculo_x = randint(0, height) 
    obstaculo_y = randint(0, height) + (frame_count * nivel) 
    obstaculo_y %= height #Recircular 
    text('🌵', obstaculo_x, obstaculo_y)

--- /code ---

Si has realizado todas estas comprobaciones y todavía no parece que la cantidad de obstáculos esté aumentando, es posible que sí lo estén, pero no lo estás viendo. Deberías probar algunos de los siguientes pasos para poner esto a prueba:
  - Desacelera tu juego usando `frame_rate()` en tu función `setup()` para darte más tiempo para contar
  - Cambia la seed (semilla) que estás usando para tus números aleatorios. Es poco probable, pero es posible que algunos obstáculos estén apareciendo aleatoriamente uno encima del otro
  - Agrega un `print()` a el bucle `for` en `dibujar_obstaculos()` que imprime el valor `i` en cada paso del bucle, para que puedas verificar si se está ejecutando la cantidad de veces que debería
  - Solo para fines de prueba, cambia `range(6 + nivel)` a `range(6 * nivel)`; ¡ese aumento debería ser más fácil de detectar!


--- /collapse ---

--- /task ---

--- save ---
