## Melhore o seu projeto

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Se você tiver tempo, você pode melhorar o seu projeto.
</div>
<div>

![Example space project with lives.](images/example1.png){:width="300px"}

</div>
</div>

Aqui estão algumas ideias que você pode tentar:

### Inclua uma variedade de obstáculos
Você pode adicionar variedade aos seus obstáculos de algumas maneiras:
 - Escolha aleatoriamente entre várias imagens, emojis ou funções de desenho de obstáculos
 - Ajuste aleatoriamente a cor, forma ou tamanho dos obstáculos alterando os parâmetros que os desenham
 - Anime o obstáculo adicionando rotação, mudança de cor ou alguma outra diferença visual controlada por `frame_count`

### Adicionar uma condição de vitória
Você pode fazer com que os jogadores ganhem o jogo de algumas maneiras:
 - Alcançar uma pontuação vencedora
 - Atingir um certo nível do jogo

Assim que eles ganharem, você deve dizer a eles de alguma forma - talvez usando `print()` ou `text()` e então pare o jogo.

### Dê aos jogadores mais de uma vida
Adicione vidas ao seu jogo, para permitir que os jogadores sobrevivam a algumas colisões. This is a little trickier than just doing `lives -= 1` every time they collide with something:
 - O jogador pode gastar vários quadros em contato com um objeto e, portanto, perder mais de uma vida por uma única colisão - você precisará evitar que isso aconteça
 - Você também precisará de uma maneira de os jogadores saberem quantas vidas ainda restam e talvez algum tipo de aviso que diga a eles quando estão em sua última vida
 - Você pode adicionar um objeto que, quando o jogador colidir com ele, dê a ele uma vida extra. Lembre-se de que você precisará modificar seu código de colisão regular para que ele não subtraia uma vida ao mesmo tempo!

Each example project in the Introduction allows you to look at the code, get ideas, and see how they work.

The "Dodge Asteroids" project below has all of these features:

**Dodge asteroids**:
<iframe src="https://editor.raspberrypi.org/en/embed/viewer/dodge-asteroids-example" width="600" height="700" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
</iframe>

You can find the Dodge asteroids project [here](https://editor.raspberrypi.org/en/projects/dodge-asteroids-example){:target="_blank"}

Take a look at some Don't collide projects created by community members in the Raspberry Pi Foundation’s [Don't collide - Community library](https://wke.lt/w/s/KobNfx){:target="_blank"}.

--- save ---
