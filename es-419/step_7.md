## Mejora tu proyecto

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Si tienes algo de tiempo, puedes mejorar tu proyecto.
</div>
<div>

![Ejemplo del proyecto Esquiva Asteroides con vidas.](images/example1.png){:width="300px"}

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
Agrega más vidas a tu juego para que los jugadores puedan sobrevivir varias colisiones. Esto es un poco más complicado que simplemente hacer que `vidas =- 1` cada vez que chocan con algo:
 - El jugador podría pasar varios cuadros (frames) en contacto con un objeto y, por lo tanto, perder más de una vida por una sola colisión; tienes que evitar que eso suceda
 - También necesitarás una forma para que los jugadores sepan cuántas vidas les quedan, y tal vez algún tipo de advertencia que les indique cuando están en su última vida
 - Podrías agregar un objeto que le de una vida adicional al jugador cuando choque con este. ¡Recuerda que deberás modificar tu código para una colisión habitual para que no te reste una vida al mismo tiempo!

Cada proyecto de ejemplo en la [Introducción](./) tiene un enlace **Ver dentro** para que puedas abrir el proyecto, mirar el código para inspirarte y ver cómo funciona. El proyecto "Esquiva asteroides" a continuación tiene todas estas características:

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 175px; flex-grow: 1">  

**Esquiva asteroides**: [Ver dentro](https://trinket.io/python/d156014e67){:target="_blank"}
<div class="trinket">
<iframe src="https://trinket.io/embed/python/d156014e67?outputOnly=true" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
</div>

</div>
</div>

Échale un vistazo a algunos proyectos No choques creados por miembros de la comunidad en [No choques - Biblioteca comunitaria](https://wke.lt/w/s/KobNfx){:target="_blank"} de Raspberry Pi Foundation’s.

--- save ---
