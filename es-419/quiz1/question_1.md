## Prueba Rapida

Contesta las tres preguntas. Hay pistas que te guiaran a la respuesta correcta.

Cuando hayas respondido cada pregunta, haz click en **Verificar mi respuesta**.

¡Que te diviertas!

--- question ---
---
legend: Pregunta 1 de 3
---

Ha utilizado muchas declaraciones `si` para controlar el comportamiento de su juego. Algunos de ellos podrían haber tenido condiciones más complejas, usando `y` para hacer múltiples pruebas a la vez. Si ejecutaras el siguiente fragmento de código condicional, ¿cuál esperarías que fuera el resultado?

```python
puntaje = 5000
vidas = 2

if puntaje >= 5000 and vidas >= 3:
  print('¡Excelente vuelo!')

if puntaje >= 5000: 
  print('¡Vas bien!')
  if vidas > 1:
    print(¡Sigue así!')
  else:
    print('¡Pero ve con cuidado!')

elif vidas > 1:
  print('¡Ponle más ganas!')

else:
  print('¡Regresa a la base!')
```

--- choices ---

- ( )
```
¡Excelente vuelo!
```
  --- feedback ---

While `score >= 5000` is true, for an `and` condition both parts must be true, and `lives >= 3` is false.

  --- /feedback ---

- (x)
```
¡Vas bien!
¡Sigue así!
```
  --- feedback ---

Esto es correcto: `puntaje >= 5000` es verdadero, y también lo es `vidas > 1` en la declaración anidada `si`.

  --- /feedback ---

- ( )
```
¡Vas bien!
```
  --- retroalimentación ---

Cerca, pero `puntaje >= 5000` no es la única condición que el programa encontraría verdadera mientras se ejecuta.

  --- /feedback ---

- ( )
```
¡Ponle más ganas!
```
  --- feedback ---

Mientras que `vidas > 1` es verdadera, solo se ejecuta el código dentro de la primera condición en una sentencia `if`/`elif`/`else` y `vidas > 1` no es la primera condición verdadera.

  --- /feedback ---

--- /choices ---

--- /question ---
