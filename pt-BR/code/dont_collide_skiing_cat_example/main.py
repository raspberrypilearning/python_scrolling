#!/bin/python3

# Importar código da biblioteca
from p5 import *
from random import randint, seed

velocidade = 1
pontos = 0

# A função desenhar_fundo vai aqui
def desenhar_obstaculos():
    global velocidade
    
    seed(12345678)
    
    if frame_count % height == height - 1 and velocidade < 5:
        velocidade += 1
        print('Você atingiu o nível', velocidade)
      
    for i in range(6):
        ob_x = randint(0, height)
        ob_y = randint(0, height) + (frame_count * velocidade)
        ob_y %= height  # Envolve toda a altura
        no_stroke()
        fill(0,255,0)
        triangle(ob_x + 20, ob_y + 20, ob_x + 10, ob_y + 40, ob_x + 30, ob_y + 40)
        triangle(ob_x + 20, ob_y + 30, ob_x + 5, ob_y + 55, ob_x + 35, ob_y + 55)
        triangle(ob_x + 20, ob_y + 40, ob_x + 0, ob_y + 70, ob_x + 40, ob_y + 70)
        fill(150,100,100)
        rect(ob_x + 15, ob_y + 70, 10, 10)
    
# A função desenhar_jogador vai aqui
def desenhar_jogador():
    global pontos, velocidade, esquiando, colidido
    
    jogador_y = int(height * 0.8)
    
    fill(seguro)
  
    colide = get(mouse_x, jogador_y).hex
    
    if colide == seguro.hex:
        image(esquiando, mouse_x, jogador_y, 30, 30)
        pontos += velocidade
    else:
        image(colidido, mouse_x, jogador_y, 30, 30)
        velocidade = 0
    
  
def setup(): 
    # Configure sua animação aqui
    size(400, 400)
    text_size(40)
    text_align(CENTER, TOP) # posição em torno do centro
    global esquiando, colidido
    esquiando = load_image('skiing.png')
    colidido = load_image('fallenover.png')
  
def draw():
    # Coisas para fazer em cada quadro
    global pontos, seguro, velocidade, esquiando, colidido
    seguro = Color(255)
  
    if velocidade > 0:
        background(seguro) 
        fill(0)
        text('Pontos: ' + str(pontos), width/2, 20)
        desenhar_obstaculos()
        desenhar_jogador()
  
run()
