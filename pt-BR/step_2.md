## Defina o tema

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Defina o tema do seu jogo e crie um personagem de jogador que siga o ponteiro do mouse.

</div>
<div>

![Imagem de desenho animado de tartaruga vista de cima contra um fundo azul.](images/theme-turtle.png){:width="300px"}

</div>
</div>

Qual é o tema do seu jogo? Aqui estão algumas ideias:
- Esportes
- Passatempos
- Ciência
- Natureza

--- task ---

Abra o [Não Colida! projeto inicial](https://editor.raspberrypi.org/pt-BR/projects/dont-collide-starter){:target="_blank"} projeto. O editor de código será aberto em outra guia do navegador.

Se você tiver uma conta Trinket, você pode clicar no botão **Remix** para salvar uma cópia em sua biblioteca **My Trinkets**.

--- /task ---

--- task ---

**Escolha:** Defina o tamanho da sua tela.

--- code ---
---
language: python
filename: main.py - setup()
line_numbers: true
line_number_start: 9
line_highlights: 10
---

def setup():
    size(400, 400)

--- /code ---

--- /task ---

--- task ---

Crie uma variável chamada `seguro` para armazenar a cor de fundo com base no tema que você quer para o seu jogo.

Esta é a cor segura para o jogador e você vai usar esta variável de novo mais tarde.

--- code ---
---
language: python
filename: main.py - draw()
line_numbers: true
line_number_start: 13
line_highlights: 14, 15, 16
---

def draw():
    global seguro
    seguro = Color(200, 100, 0)  # Adicione a cor do seu tema
    background(seguro)

--- /code ---

[[[generic-theory-simple-colours]]]

--- /task ---

--- task ---

**Teste:** Execute seu código para ver a cor de fundo. Mude-o até ficar satisfeito com a cor e o tamanho da tela.

--- /task ---

Agora escolha o personagem que está jogando o jogo e evitando os obstáculos. É um objeto, pessoa, animal, ou outra coisa?

O jogador aparecerá em uma posição de `y` fixa e na mesma posição `x` do ponteiro do mouse, que é armazenado na variável `mouse_x` da `p5`.

--- task ---

É uma boa ideia organizar o código para desenhar o jogador em uma função.

Defina uma função `desenhar_jogador()` e crie uma `jogador_y` para a posição fixa `y` do jogador:

--- code ---
---
language: python
filename: main.py - desenhar_jogador()
line_numbers: true
line_number_start: 12
line_highlights: 12-14
---

def desenhar_jogador():
    jogador_y = int(height * 0.8)  # Posicionado em direção à parte inferior da tela

--- /code ---

Adicione o código a `draw()` para chamar `desenhar_jogador()` a cada quadro.

--- code ---
---
language: python
filename: main.py - draw()
line_numbers: true
line_number_start: 15
line_highlights: 19
---

def draw():
    global seguro
    seguro = Color(200, 100, 0)  # Sua cor escolhida
    background(seguro)
    desenhar_jogador()
  
--- /code ---

--- /task ---

Em seguida, você adicionará código à função `desenhar_jogador()` para desenhar sua forma. Você também pode precisar adicionar o código `setup()`.

--- task ---

**Escolha:** Qual é a aparência do seu jogador? Seu jogador pode ser:
+ Uma imagem fornecida no projeto inicial
+ Um emoji 🎈 ou texto
+ Desenhado usando uma série de formas

--- collapse ---
---
title: Use uma imagem inicial
---

As imagens incluídas no projeto inicial serão mostradas na `Galeria de imagens`.

![A galeria de imagens exibindo as imagens incluídas.](images/starter-images.png)

Anote o nome da imagem que deseja usar.

Carregue a imagem na função `setup()`

--- code ---
---
language: python
filename: main.py - setup()
line_numbers: true
line_number_start: 9
line_highlights: 11-12
---

def setup():
    size(400, 400)
    global jogador
    jogador = load_image('turtle.png')  # Carregue sua imagem

--- /code ---

Chame o `image()` e defina-o como global na função `desenhar_jogador()`.

--- code ---
---
language: python
filename: main.py - desenhar_jogador()
line_numbers: true
line_number_start: 14
line_highlights: 16
---

def desenhar_jogador():
    jogador_y = int(height * 0.8)  # Posicionado em direção à parte inferior da tela
    image(jogador, mouse_x, jogador_y, 30, 30)

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Use caracteres emoji
---

Você pode usar caracteres emoji na função p5 `text()` para usar um emoji para representar seu jogador.

Aqui está um exemplo:

--- code ---
---
language: python
filename: main.py - setup()
line_numbers: true
line_number_start: 9
line_highlights: 11-13
---

def setup():
    size(400, 400)
    text_size(40)  # Controla o tamanho do emoji
    text_align(CENTER, TOP)  # Posicionado em direção à parte inferior da tela

--- /code ---

Chame o `text()` e defina-o como global na função `desenhar_jogador()`.

--- code ---
---
language: python
filename: main.py - desenhar_jogador()
line_numbers: true
line_number_start: 14
line_highlights: 16-17
---

def desenhar_jogador():
    jogador_y = int(height * 0.8)
    text('🎈', mouse_x, jogador_y)

--- /code ---

--- /collapse ---

[[[processing-python-text]]]

[[[generic-theory-simple-colours]]]

[[[processing-python-ellipse]]]

[[[processing-python-rect]]]

[[[processing-python-triangle]]]

[[[processing-tint]]]

[[[processing-stroke]]]

**Dica:** Você pode usar várias formas simples na mesma função para criar um jogador mais complexo.

--- collapse ---
---
title: Desenhe um jogador usando várias formas
---

![Um formato de rosto feito de um círculo verde como fundo e dois olhos desenhados de círculos azuis, com círculos pretos dentro e um brilho dentro deles usando um círculo branco.](images/face_player.png)

--- code ---
---
language: python
filename: main.py - desenhar_jogador()
---

def desenhar_jogador():
    jogador_y = int(height * 0.8)
    noStroke()
    # Face
    fill(0, 200, 100)
    ellipse(mouse_x, jogador_y, 60, 60)
    
    # Olhos
    fill(0, 100, 200)
    ellipse(mouse_x - 10, jogador_y - 10, 20, 20)
    ellipse(mouse_x + 10, jogador_y - 10, 20, 20)
    fill(0)
    ellipse(mouse_x - 10, jogador_y - 10, 10, 10)
    ellipse(mouse_x + 10, jogador_y - 10, 10, 10)
    fill(255)
    ellipse(mouse_x - 12, jogador_y - 12, 5, 5)
    ellipse(mouse_x + 12, jogador_y - 12, 5, 5)

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

**Teste:** Execute seu código e mova o mouse para controlar o jogador.

Ele se move como você espera?

--- /task ---

**Depurar:** Talvez você encontre alguns bugs em seu projeto que precisam de correção. Aqui estão alguns bugs comuns.

--- task ---

--- collapse ---
---
title: não vejo o jogador
---

Tente mudar para tela cheia. Além disso, verifique as coordenadas `x` e `y` que você usou para desenhar o jogador — certifique-se de que elas estejam dentro da tela que você criou com `size()`.

--- /collapse ---

--- collapse ---
---
title: Uma imagem não está carregando
---

Primeiro, verifique se a imagem está na `Galeria de imagens`. Em seguida, verifique o nome do arquivo com muito cuidado - lembre-se de que as letras maiúsculas são diferentes das letras minúsculas e a pontuação é importante.

--- /collapse ---

--- collapse ---
---
title: Uma imagem tem o tamanho errado
---

Verifique as entradas que controlam a largura e a altura da imagem:

```python
image(arquivo_imagem, x_coord, y_coord, largura, altura)
```

--- /collapse ---

--- collapse ---
---
title: Uma imagem tem o tamanho errado
---

Se o seu emoji for muito grande ou muito pequeno, altere o valor em `text_size()`.

--- /collapse ---

--- /task ---

--- save ---
