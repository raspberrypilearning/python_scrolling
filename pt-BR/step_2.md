## Defina o tema

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Defina o tema do seu jogo e crie um personagem de jogador que siga o ponteiro do mouse.

</div>
<div>

![Imagem de tartaruga tamanho 100x100 contra um fundo azul com tamanho de tela 400x400.](images/theme-turtle.png){:width="300px"}

</div>
</div>

Qual é o tema do seu jogo? Você pode escolher o que quiser. Aqui estão algumas idéias:
- Um esporte ou hobby
- Um filme, programa ou jogo
- Ciência ou natureza
- Qualquer outra coisa!

--- task ---

Abra o [projeto inicial](https://trinket.io/python/cda05e5911){:target="_blank"}. O Trinket será aberto em outra aba do navegador.

--- /task ---

--- task ---

**Escolha:** Defina o tamanho da sua tela.

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

Crie uma variável chamada `safe` para armazenar a cor de fundo com base no tema que você quer para o seu jogo.

Esta é a cor segura para o jogador e você vai usar esta variável de novo mais tarde.

--- code ---
---
language: python
filename: main.py - draw()
---

def draw():    
safe = color(200, 100, 0) #Add the colour of your theme   
background(safe)

--- /code ---

[[[generic-theory-simple-colours]]]

--- /task ---

--- task ---

**Teste:** Execute seu código para ver a cor de fundo. Mude-o até ficar satisfeito com a cor e o tamanho da tela.

--- /task ---

Now choose the character that is playing the game and avoiding the obstacles. Is it an object, person, animal, or something else?

The player will appear at a fixed `y` position and same `x` position as the mouse pointer, which is stored in the `p5` variable `mouse_x`.

--- task ---

It's a good idea to organise the code for drawing the player character into a function.

Define a `draw_player()` function and create a `player_y` position for the fixed `y` position of the player:

--- code ---
---
language: python
filename: main.py - draw_player()
---

def draw_player():    
player_y = int(height * 0.8) #Positioned towards the screen bottom

--- /code ---

Add code to `draw()` to call `draw_player()` each frame.

--- code ---
---
language: python
filename: main.py - draw()
---

def draw():    
safe = color(200, 100, 0) #Your chosen colour    
background(safe)    
draw_player()

--- /code ---

--- /task ---

Next you will add code to the `draw_player()` function to draw your shape. You may also need to add `setup()` code.

--- task ---

**Choose:** What does your player look like? Your player could be:
+ An image provided in the starter project
+ An emoji 🎈 or text
+ Drawn using a series of shapes

--- collapse ---
---
title: Use a starter image
---

Click on the **manage images** icon.

![O ícone de imagem no canto superior direito da área de código.](images/manage-images.png)

Images included in the starter project will be shown in the `Image library` list.

![A biblioteca de imagens com a lista de imagens incluídas.](images/starter-images.png)

Make a note of the name of the image you want to use.

Load the image into the `setup()` function

--- code ---
---
language: python
filename: main.py - setup()
---

def setup():   
size(400, 400)    
player = load_image('skiing.png') #Load your image

--- /code ---

Call the `image()` and set it as global in the `draw_player()` function.

--- code ---
---
language: python
filename: main.py - draw_player()
---

def draw_player():    
player_y = int(height * 0.8) #Positioned towards the screen bottom

  global player

  image(player, mouse_x, player_y, 30, 30)

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Use emoji characters
---

You can use emoji characters in the p5 `text()` function to use an emoji to represent your player.

Aqui está um exemplo:

--- code ---
---
language: python
filename: main.py - setup()
---

def setup():    
size(400, 400)     
text_size(40) #Controls the size of the emoji     
text_align(CENTER, TOP) #Position around the centre

--- /code ---

--- code ---
---
language: python
filename: main.py - draw_player()
---

def draw_player():     
player_y = int(height * 0.8)    
text('🎈', mouse_x, player_y)

--- /code ---

--- /collapse ---

[[[processing-python-text]]]

[[[generic-theory-simple-colours]]]

[[[processing-python-ellipse]]]

[[[processing-python-rect]]]

[[[processing-python-triangle]]]

[[[processing-tint]]]

[[[processing-stroke]]]

**Tip:** You can use several simple shapes in the same function to create a more complex player.

--- collapse ---
---
title: Desenhe um jogador usando várias formas
---

![desc](images/face_player.png)

--- code ---
---
language: python
filename: main.py - draw_player()
---

def draw_player():    
player_y = int(height * 0.8)    
noStroke()    
#Face    
fill(0, 200, 100)    
ellipse(mouse_x, player_y, 60, 60)

  #Eyes    
fill(0, 100, 200)    
ellipse(mouse_x - 10, player_y - 10, 20, 20)    
ellipse(mouse_x + 10, player_y - 10, 20, 20)    
fill(0)    
ellipse(mouse_x - 10, player_y - 10, 10, 10)     
ellipse(mouse_x + 10, player_y - 10, 10, 10)     
fill(255)    
ellipse(mouse_x - 12, player_y - 12, 5, 5)    
ellipse(mouse_x + 12, player_y - 12, 5, 5)

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

**Teste:** Execute seu código e mova o mouse para controlar o jogador.

Ele se move como você espera?

--- /task ---

**Depurar:** Você pode encontrar alguns bugs em seu projeto que precisa corrigir. Aqui estão alguns bugs comuns.

--- task ---

--- collapse ---
---
título: não vejo o jogador
---

Tente mudar para tela cheia. Além disso, verifique as coordenadas `x` e `y` que você usou para desenhar o jogador — certifique-se de que elas estejam dentro da tela que você criou com `size()`.

--- /collapse ---

--- collapse ---
---
title: Uma imagem não está carregando
---

Primeiro, verifique se a imagem está na biblioteca `Image`. Em seguida, verifique o nome do arquivo com muito cuidado - lembre-se de que as letras maiúsculas são diferentes das letras minúsculas e a pontuação é importante.

--- /collapse ---

--- collapse ---
---
title: Uma imagem tem o tamanho errado
---

Verifique as entradas que controlam a largura e a altura da imagem:

```python
imagem(imagem_arquivo, x_coord, y_coord, largura, altura)
```

--- /collapse ---

--- collapse ---
---
title: Uma imagem tem o tamanho errado
---

Se o seu emoji for muito grande ou muito pequeno, altere a entrada para `text_size()`.

--- /collapse ---

--- /task ---

--- save ---
