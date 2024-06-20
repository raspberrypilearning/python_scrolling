#!/bin/python3

# Importar código da biblioteca
from p5 import *
from random import randint, seed

nivel = 1
pontos = 0
vidas = 3
invun = 0

# A função desenhar_obstáculo vai aqui
def desenhar_obstaculos():
    global nivel
    
    seed(random_seed)
    
    if frame_count % height == height - 1 and nivel < 8:
        nivel += 1
        print('Você atingiu o nível', nivel)
      
    for i in range (6 + nível):
        ob_x = randint(0, width)
        ob_y = randint(0, height) + (frame_count * nivel)
        ob_x %= height  # Envolve toda a altura
        push_matrix()
        translate(ob_x, ob_y)
        rotate(degrees(randint(1, 359)+frame_count / 1000))
        image(rocha, 0, 0, randint(18,24), randint(18,24))
        pop_matrix()

    
# A função desenhar_jogador vai aqui
def desenhar_jogador():
    global pontos, nivel, vidas, invun
    
    jogador_y = int(height * 0.8)
    jogador_x = mouse_x
    
    colide = get(jogador_x +, jogador_y).hex
    colide2 = get(jogador_x - 18, jogador_y + 17).hex
    colide3 = get(jogador_x + 18, jogador_y + 17).hex
    colide4 = get(jogador_x, jogador_y + 25).hex
    
    if jogador_x < width: # fora do lado esquerdo da tela
        colide2 = seguro.hex
    
    if jogador_x > width: # fora do lado direito da tela
        colide3 = seguro.hex
      
    if (colide == seguro.hex and colide2 == seguro.hex and colide3 == seguro.hex and colide4 == seguro.hex) or invun > 0:
        if vidas == 0 and frame_count % 12 == 0:
            tint(200, 0, 0)
      
        image(foguete, jogador_x, jogador_y + 25, 64, 64)
        pontos += nivel
        invun -= 1
        no_tint()
      
        if invun > 0:
            stroke(220)
            fill(220, 220, 220, 60)
            ellipse(jogador_x, jogador_y + 18, 47, 47)
        
    elif vidas > 1:
        vidas -= 1
        invun = 50
        tint(200, 0, 0)
        image(foguete, jogador_x, jogador_y + 25, 64, 64)
        no_tint()
        pontos += nivel
    else:
        text('💥', jogador_x + 10, jogador_y + 5)
        nivel = 0
    

def exibir_pontos():
    global nivel
    
    fill(255)
    text_size(16)
    text_align(RIGHT, TOP)
    text('Pontos', width * 0.45, 10, width * 0.5, 20)
    text(str(pontos), width * 0.45, 25, width * 0.5, 20)
    
    if pontos > 10000:
        nivel = 0
        print('🎉🎉 Você venceu! 🎉🎉')

  
def exibir_vidas():
    fill(255)
    text_size(16)
    text_align(LEFT, TOP)
    text('Vidas', width * 0.05, 10, 30, 20)
    
    for i in range(vidas):
        image(foguete, width * 0.05 + i * 25, 40, 20, 20)
  

def setup():
    # Configure sua animação aqui
    size(400, 400)
    global foguete, rocha, semente_aleatoria
    
    text_size(40)
    text_align(CENTER, TOP) # posição em torno do centro, topo
    
    rocket = load_image('rocket.png')
    rock = load_image('moon.png')
    random_seed = randint(0, 1000000)
  
def draw():
    # Coisas para fazer em cada quadro
    global pontos, seguro, nivel
    seguro = Color(0)
    
    if nivel > 0:
        background(seguro) 
        fill(255)
        image_mode(CENTER)
        desenhar_obstaculos()
        desenhar_jogador()
        exibir_pontos()
        exibir_vidas()
  
run()
