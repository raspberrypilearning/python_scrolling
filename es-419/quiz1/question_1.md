## Reflexión

¡Bien hecho, creaste un juego!  Ahora es el momento de reflexionar: reflexionar es una parte importante del aprendizaje porque ayuda a establecer nuevas conexiones en tu cerebro.

Responde las tres preguntas siguientes para reflexionar sobre lo que has aprendido.

Después de responder cada pregunta, haz clic en **Enviar**. Vamos a guiarte hacia la respuesta correcta. Puedes realizar esta actividad tantas veces como quieras.

¡Qué te diviertas!

--- question ---
---
legend: Pregunta 1 de 3
---

Has utilizado muchas sentencias `if` para controlar el comportamiento de tu juego. Algunas de ellos podrían haber tenido condiciones más complejas, usando `and` para hacer varias pruebas a la vez. Si ejecutaras el siguiente fragmento de código condicional, ¿cuál esperarías que fuera el resultado?

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

Mientras que `puntaje >= 5000` es verdadera, para una condición `and` ambas partes deben ser verdaderas, y `vidas >= 3` debe ser falsa.

  --- /feedback ---

- (x)
```
¡Vas bien!
¡Sigue así!
```
  --- feedback ---

Esto es correcto — `puntaje >= 5000` es verdadera, y también lo es `vidas > 1` en la sentencia anidada `if`.

  --- /feedback ---

- ( )
```
¡Vas bien!
```
  --- feedback ---

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
