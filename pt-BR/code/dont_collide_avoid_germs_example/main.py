#!/bin/python3

from p5 import *
from random import randint, seed

nivel = 1
pontos = 0

def jogador_seguro():
    global jogador_y
    
    # Face
    fill(200, 134, 145)
    ellipse(mouse_x, jogador_y, 60, 60)
  
    # Olhos
    fill(178, 200, 145)
    ellipse(mouse_x - 10, jogador_y - 10, 20, 20)
    ellipse(mouse_x + 10, jogador_y - 10, 20, 20)
    fill(0)
    ellipse(mouse_x - 10, jogador_y - 10, 10, 10)
    ellipse(mouse_x + 10, jogador_y - 10, 10, 10)
    fill(255)
    ellipse(mouse_x - 12, jogador_y - 12, 5, 5)
    ellipse(mouse_x + 12, jogador_y - 12, 5, 5)
    
    # Boca
    fill(0)
    ellipse(mouse_x, jogador_y + 10, 15, 10)
    fill(200, 134, 145)
    ellipse(mouse_x, jogador_y + 5, 10, 10)

def jogador_colidido():
    global jogador_y
    
    # Face
    fill(178, 200, 145)
    ellipse(mouse_x, jogador_y, 60, 60)
  
    # Olhos
    fill(149, 161, 195)
    ellipse(mouse_x - 10, jogador_y - 10, 20, 20)
    ellipse(mouse_x + 10, jogador_y - 10, 20, 20)
    fill(0)
    ellipse(mouse_x - 10, jogador_y - 10, 10, 10)
    ellipse(mouse_x + 10, jogador_y - 10, 10, 10)
    fill(255)
    ellipse(mouse_x - 12, jogador_y - 12, 5, 5)
    ellipse(mouse_x + 12, jogador_y - 12, 5, 5)
    
    # Boca
    fill(0)
    ellipse(mouse_x, jogador_y + 15, 15, 10)
    fill(178, 200, 145)
    ellipse(mouse_x, jogador_y + 20, 10, 10)
  
def desenhar_jogador():
  
    global jogador_y, seguro, pontos, nivel
    
    jogador_y = int(height * 0.8)
    
    colide = get(mouse_x, jogador_y).hex
    colide2 = get(mouse_x, jogador_y + 30).hex
    colide3 = get(mouse_x + 30, jogador_y).hex
    colide4 = get(mouse_x, jogador_y - 30).hex
    
    if mouse_x < width: # à esquerda da tela
        colide2 = seguro.hex
    
    if mouse_x > width: # à direita da tela
        colide3 = seguro.hex
      
    #print(colide, colide2, colide3, colide4)
      
    if colide == seguro.hex and colide2 == seguro.hex and colide3 == seguro.hex and colide4 == seguro.hex:
        jogador_seguro()
        pontos += nivel
    else: # Colidiu
        jogador_colidido()
        nivel = 0
  
def desenhar_obstaculos():
    global nivel
    
    seed(41143644)
    
    if frame_count & height == height - 1 and nivel < 5:
        nivel += 1
        print('Você atingiu o nível', nivel)
    
    for i in range(9 + nivel):
        ob_x = randint(0, width)
        ob_y = randint(0, height) + frame_count
        ob_y %= height
        text('🦠', ob_x, ob_y)

def setup():
    # Coloque aqui o código para ser executado uma vez
    size(400, 400) # largura e altura
    no_stroke()
    text_size(40)
    text_align(CENTER, TOP)

def draw():
    # Coloque aqui o código para ser executado em cada quadro
    global seguro, pontos, nivel
  
    seguro = Color(149, 161, 195)
  
    if nivel > 0:
        background(seguro)
        fill(145, 134, 126)
        text('Pontos: ' + str(pontos), width/2, 20)
        desenhar_obstaculos()
        desenhar_jogador()
  
# Mantenha isto para executar seu código
run()
