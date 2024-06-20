#!/bin/python3

# Importar código da biblioteca
from p5 import *
from random import randint, seed

nivel = 1
pontos = 0

# A função desenhar_obstáculo vai aqui
def desenhar_obstaculos():
    global nivel
  
    seed(12345678)
  
    if frame_count % height == height - 1 and nivel < 5:
        nivel += 1
        print('Você atingiu o nível', nivel)
  
    for i in range (6 + nível):
        ob_x = randint(0, height)
        ob_y = randint(0, height) + (frame_count * nivel)
        ob_y %= height  # Envolve toda a altura
        text('🌵', ob_x, ob_y)


# A função desenhar_jogador vai aqui
def desenhar_jogador():
    global pontos, nivel
  
    jogador_y = int(height * 0.8)
  
    colide = get(mouse_x, jogador_y).hex
    colide2 = get(mouse_x - 12, jogador_y + 20).hex
    colide3 = get(mouse_x + 12, jogador_y + 20).hex
    colide4 = get(mouse_x, jogador_y + 40).hex
  
    if mouse_x < width: # fora do lado esquerdo da tela
        colide2 = seguro.hex
  
    if mouse_x > width: # fora do lado direito da tela
        colide3 = seguro.hex
  
    if colide == seguro.hex and colide2 == seguro.hex and colide3 == seguro.hex and colide4 == seguro.hex:
        text('🎈', mouse_x, jogador_y)
        pontos += nivel
    else:
        text('💥', mouse_x, jogador_y)
        nivel = 0


def setup():
    # Configure sua animação aqui
    size(400, 400)
    text_size(40)
    text_align(CENTER, TOP) # posição em torno do centro, topo


def draw():
    # Coisas para fazer em cada quadro
    global pontos, seguro, nivel
    seguro = Color(200, 150, 0)

    if nivel > 0:
        background(seguro)
        fill(255)
        text('Pontos: ' + str(pontos), width/2, 20)
        desenhar_obstaculos()
        desenhar_jogador()

run()
