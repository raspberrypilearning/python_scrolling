## Detecção de colisão

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Os jogos de corrida sem fim geralmente terminam quando o jogador colide com um obstáculo.
</div>
<div>

![Imagem da etapa concluída.](images/collision.png){:width="300px"}

</div>
</div>

Agora você pode configurar seu jogador para reagir à uma colisão de obstáculos.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">**Detecção de colisão**</span> determina quando dois objetos criados dentro de uma simulação de computador — seja um jogo, uma animação ou qualquer outra coisa — estão se tocando. Existem várias maneiras de fazer isso, por exemplo: 
  - verificando se as cores que aparecem no local de um objeto são as cores desse objeto ou outras
  - acompanhando a forma de cada objeto e verificando se essas formas se sobrepõem
  - criando um conjunto de pontos de limite, ou linhas, ao redor de um objeto e verificando se eles entram em contato com quaisquer outros objetos 'colidíveis'
Quando tal colisão é detectada, o programa pode reagir de alguma forma. Em um videogame, isso geralmente ocorre para causar dano (se o jogador colidir com um inimigo ou perigo) ou para conceder um benefício (se o jogador colidir com um bônus).
</p>

--- task ---

Na sua função `desenhar_jogador()`, crie uma variável chamada `colide` e configure-a para obter o valor da cor hexadecimal (hex) na posição do jogador.

--- code ---
---
language: python
filename: main.py - desenhar_jogador()
---

    colide = get(mouse_x, jogador_y).hex

--- /code ---

--- /task ---

--- task ---

Crie uma condição para verificar `if` a variável `colide` é a mesma que a variável `seguro` - se for, então seu jogador está tocando o fundo com segurança e não colidiu com nenhum obstáculo.

Mova seu código para desenhar seu jogador dentro de sua condição `if colide == seguro` e adicione o código na instrução `else` para fazer o jogador reagir à colisão.

**Escolha:** Como seu jogador deve reagir? Você poderia:
+ Usar um emoji diferente para o jogador
+ Você poderia usar `tint()` para alterar a aparência de uma imagem, não se esqueça de chamar `no_tint()` após desenhar a imagem

--- collapse ---
---
title: Use caracteres emoji
---

Você pode usar caracteres emoji na função p5 `text()` para representar seu jogador colidido.

Aqui está um exemplo:

--- code ---
---
language: python
filename: main.py - setup()
---

def setup():
    size(400, 400)
    text_size(40)  # Controla o tamanho do emoji
    text_align(CENTER, TOP)  # Posicione ao redor do centro

--- /code ---

--- code ---
---
language: python
filename: main.py - desenhar_jogador()
---

def desenhar_jogador():
    if colide == seguro.hex:  # On background
        text('🎈', mouse_x, jogador_y)
    else:  # Collided
        text('💥', mouse_x, jogador_y)

--- /code ---

--- /collapse ---

[[[processing-tint]]]

[[[generic-theory-simple-colours]]]

--- /task ---

--- task ---

**Teste:** Verifique se uma colisão é detectada e a reação ocorre cada vez que ocorre uma colisão.

--- /task ---

--- task ---

**Depurar:** Talvez você encontre alguns bugs em seu projeto que precisam de correção. Aqui estão alguns bugs comuns.

--- collapse ---
---
title: Não há colisão quando o jogador atinge um obstáculo
---

Se o seu personagem tocar no obstáculo e nada acontecer, há algumas coisas que você deve verificar:

 - Certifique-se de chamar `desenhar_obstaculos()` antes de `desenhar_jogador()`. Se você verificar as colisões antes de desenhar os obstáculos em um quadro, não haverá nenhum obstáculo para colidir!
 - Certifique-se de usar exatamente a mesma cor ao desenhar o objeto e verificar a colisão na instrução `if`. Você pode ter certeza disso usando a mesma variável `global` em ambos os lugares.
 - Você está desenhando o jogador antes de verificar a cor nas coordenadas do mouse? Nesse caso, você só obterá as cores do jogador. Você precisa verificar a cor primeiro e **depois** desenhar o jogador.
 - Você tem código na parte `else` para fazer algo diferente quando uma colisão é detectada, como aplicar uma tonalidade ou usar um emoji?
 - Você identou o código corretamente para sua instrução `if` para que seja executado quando a condição for atendida?

Imprimir a cor do píxel que você está verificando para uma colisão pode ser útil:

```python
    print(red(colide), green(colide), blue(colide))
```

Você também pode imprimir um círculo ao redor do ponto que está verificando e ajustar o ponto verificado se precisar:

```python
    no_fill()
    ellipse(mouse_x, jogador_y, 10, 10)  # Desenhar ponto de colisão
```

--- /collapse ---

--- /task ---

--- task ---

**Opcional:** No momento, você está apenas detectando colisões em um píxel do seu jogador. Você também pode detectar colisões em outros píxeis na borda do jogador, como a parte inferior ou as bordas mais à esquerda e à direita.

--- collapse ---
---
title: Detecção de colisão com vários píxeis
---

```python
def desenhar_jogador():

    jogador_y = int(height * 0.8)
    # Útil para depuração
    # Desenhe círculos ao redor dos pixels para verificar colisões

    no_fill()
    ellipse(mouse_x, jogador_y, 10, 10)  # Desenhar ponto de colisão
    ellipse(mouse_x, jogador_y + 40, 10, 10)
    ellipse(mouse_x - 12, jogador_y + 20, 10, 10)
    ellipse(mouse_x + 12, jogador_y + 20, 10, 10)

    collide = get(mouse_x, jogador_y).hex
    collide2 = get(mouse_x - 12, jogador_y + 20).hex
    collide3 = get(mouse_x + 12, jogador_y + 20).hex
    collide4 = get(mouse_x, jogador_y + 40).hex

    if mouse_x < width:  # À esquerda da tela
        collide2 = seguro.hex

    if mouse_x > width:  # À direita da tela
        collide3 = seguro.hex

    if collide == seguro.hex and collide2 == seguro.hex and collide3 == seguro.hex and collide4 == seguro.hex:
        text('🎈', mouse_x, jogador_y)
    else:
        text('💥', mouse_x, jogador_y)
```

--- /collapse ---

Você pode até usar um laço e verificar vários pixels diferentes. É assim que funciona a detecção de colisão em jogos.

--- /task ---

--- save ---
