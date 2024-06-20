#!/bin/python3

# Importar código da biblioteca
from p5 import *
from random import randint, seed

nivel = 1
pontos = 0

# A função desenhar_obstáculo vai aqui
def desenhar_obstaculos():
    global nivel
    
    seed(123456789)
    
    if frame_count % width == width - 1 e nivel < 10:
        nivel += 1
        print('Você atingiu o nível', nivel)
      
    for i in range (6 + nível):
        ob_x = randint(0, width) - (frame_count * nivel)
        ob_x = randint(0, height) 
        ob_x %= width  # Envolve toda a largura
        text('💩', ob_x, ob_y)
    
# A função desenhar_jogador vai aqui
def desenhar_jogador():
    global pontos, nivel
    
    jogador_x = int(width * 0.2)
    jogador_y = mouse_y
    
    colide = get(jogador_x + 50, jogador_y + 15).hex
    colide2 = get(jogador_x + 50, jogador_y - 15).hex
    colide3 = get(jogador_x, jogador_y + 15).hex
    colide4 = get(jogador_x, jogador_y - 15).hex
    colide5 = get(jogador_x - 50, jogador_y + 15).hex
    colide6 = get(jogador_x - 50, jogador_y - 15).hex
    
    if jogador_y > height - 18: # Fora da parte inferior da tela
        colide = seguro.hex
        colide3 = seguro.hex
        colide5 = seguro.hex
      
    if jogador_y < 18: # Fora da parte superior da tela
        colide2 = seguro.hex
        colide4 = seguro.hex
        colide6 = seguro.hex
      
    if colide == seguro.hex and colide2 == seguro.hex and colide3 == seguro.hex and colide4 == seguro.hex:
        image(carro, jogador_x, jogador_y, 100, 31)
        pontos += nivel
    else:
        text('💥', jogador_x, jogador_y)
        nivel = 0


def setup():
    # Configure sua animação aqui
    size(400, 400)
    global carro
    carro = load_image('car.png')
    image_mode(CENTER)
  
  
def draw():
    # Coisas para fazer em cada quadro
    global pontos, seguro, nivel
    seguro = Color(128)
    
    if nivel > 0:
        background(seguro)
        fill(255)
        text_size(16)
        text_align(RIGHT, TOP)
        text('Pontos', width * 0.45, 10, width * 0.5, 20)
        text(str(pontos), width * 0.45, 25, width * 0.5, 20)
        text_size(20)
        text_align(CENTER, TOP) # posição em torno do centro, topo
        desenhar_obstaculos()
        desenhar_jogador()
  
run()
