## Prueba Rapida

Contesta las tres preguntas. Hay pistas que te guiaran a la respuesta correcta.

When you have answered each question, click on **Check my answer**.

Have fun!

--- question ---
---
legend: Pregunta 1 de 3
---

You have used a lot of `if` statements to control your game's behaviour. Some of them might have had more complex conditions, using `and` to make multiple tests at once. If you ran the following piece of conditional code, what would you expect the output to be?

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

While `score >= 5000` is true, for an `and` condtion both parts must be true, and `lives >= 3` is false.

  --- /feedback ---

- (x)
```
¡Vas bien!
¡Sigue así!
```
  --- feedback ---

This is correct — `score >= 5000` is true, and so is `lives > 1` on the nested `if` statement.

  --- /feedback ---

- ( )
```
¡Vas bien!
```
  --- feedback ---

Close, but `score >= 5000` isn't the only condition the program would find true as it ran.

  --- /feedback ---

- ( )
```
¡Ponle más ganas!
```
  --- feedback ---

While `lives > 1` is true, only the code inside the first true condition in an `if`/`elif`/`else` statement is executed, and `lives > 1` is not the first condition that is true.

  --- /feedback ---

--- /choices ---

--- /question ---
