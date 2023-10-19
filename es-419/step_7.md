## Mejora tu proyecto

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Si tienes algo de tiempo, puedes mejorar tu proyecto.
</div>
<div>

![Example space project with lives.](images/example1.png){:width="300px"}

</div>
</div>

Aquí tienes algunas ideas que podrías probar:

### Incluye una variedad de obstáculos
Puedes agregar variedad a sus obstáculos de varias maneras:
 - Elige aleatoriamente entre múltiples imágenes, emojis o funciones de dibujo de obstáculos
 - Ajusta aleatoriamente el color, la forma o el tamaño de los obstáculos cambiando los parámetros que los dibujan
 - Anima el obstáculo agregando rotación, un cambio de color o alguna otra diferencia visual controlada por `frame_count`

### Agrega una condición para ganar
Puedes hacer que los jugadores ganen el juego de varias maneras:
 - Al lograr una puntuación ganadora
 - Al alcanzar cierto nivel del juego

Cuando hayan logrado ganar, deberías decírselo de alguna manera, podrías usar `print()` o `text()` y luego detener el juego.

### Dale a los jugadores más de una vida
Agrega más vidas a tu juego para que los jugadores puedan sobrevivir varias colisiones. This is a little trickier than just doing `lives -= 1` every time they collide with something:
 - El jugador podría pasar varios cuadros (frames) en contacto con un objeto y, por lo tanto, perder más de una vida por una sola colisión; tienes que evitar que eso suceda
 - También necesitarás una forma para que los jugadores sepan cuántas vidas les quedan, y tal vez algún tipo de advertencia que les indique cuando están en su última vida
 - Podrías agregar un objeto que le de una vida adicional al jugador cuando choque con este. ¡Recuerda que deberás modificar tu código para una colisión habitual para que no te reste una vida al mismo tiempo!

Each example project in the Introduction allows you to look at the code, get ideas, and see how they work.

The "Dodge Asteroids" project below has all of these features:

**Dodge asteroids**:
<iframe src="https://editor.raspberrypi.org/en/embed/viewer/dodge-asteroids-example" width="600" height="700" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
</iframe>

You can find the Dodge asteroids project [here](https://editor.raspberrypi.org/en/projects/dodge-asteroids-example){:target="_blank"}

Take a look at some Don't collide projects created by community members in the Raspberry Pi Foundation’s [Don't collide - Community library](https://wke.lt/w/s/KobNfx){:target="_blank"}.

--- save ---
