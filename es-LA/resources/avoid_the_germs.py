#!/bin/python3

from p5 import *
from random import randint, seed

nivel = 1
puntaje = 0

def jugador_a_salvo():
  
  global jugador_y
  
  # Cara
  fill(200, 134, 145)
  ellipse(mouse_x, jugador_y, 60, 60)

  # Ojos
  fill(178, 200, 145)
  ellipse(mouse_x - 10, jugador_y - 10, 20, 20)
  ellipse(mouse_x + 10, jugador_y - 10, 20, 20)
  fill(0)
  ellipse(mouse_x - 10, jugador_y - 10, 10, 10)
  ellipse(mouse_x + 10, jugador_y - 10, 10, 10)
  fill(255)
  ellipse(mouse_x - 12, jugador_y - 12, 5, 5)
  ellipse(mouse_x + 12, jugador_y - 12, 5, 5)
  
  # Boca
  fill(0)
  ellipse(mouse_x, jugador_y + 10, 15, 10)
  fill(200, 134, 145)
  ellipse(mouse_x, jugador_y + 5, 10, 10)

def jugador_estrellado():
  
  global jugador_y
  
  # Cara
  fill(178, 200, 145)
  ellipse(mouse_x, jugador_y, 60, 60)

  # Ojos
  fill(149, 161, 195)
  ellipse(mouse_x - 10, jugador_y - 10, 20, 20)
  ellipse(mouse_x + 10, jugador_y - 10, 20, 20)
  fill(0)
  ellipse(mouse_x - 10, jugador_y - 10, 10, 10)
  ellipse(mouse_x + 10, jugador_y - 10, 10, 10)
  fill(255)
  ellipse(mouse_x - 12, jugador_y - 12, 5, 5)
  ellipse(mouse_x + 12, jugador_y - 12, 5, 5)
  
  # Boca
  fill(0)
  ellipse(mouse_x, jugador_y + 15, 15, 10)
  fill(178, 200, 145)
  ellipse(mouse_x, jugador_y + 20, 10, 10)
  
def dibujar_jugador():
  
  global jugador_y, a_salvo, puntaje, nivel
  
  jugador_y = int(height * 0.8)
  
  colision = get(mouse_x, jugador_y)
  colision2 = get(mouse_x, jugador_y + 30)
  colision3 = get(mouse_x + 30, jugador_y)
  colision4 = get(mouse_x, jugador_y - 30)
  
  if mouse_x < width: # a la izquierda de la pantalla
    colision2 = a_salvo
  
  if mouse_x > width: # a la derecha de la pantalla
    colision3 = a_salvo
    
  #print(colision, colision2, colision3, colision4)
    
  if colision == a_salvo and colision2 == a_salvo and colision3 == a_salvo and colision4 == a_salvo:
    jugador_a_salvo()
    puntaje += nivel
  else: # Estrellado
    jugador_estrellado()
    nivel = 0
  
def dibujar_obstaculos():
  
  global nivel
  
  seed(41143644)
  
  if frame_count & height == height - 1 and nivel < 5:
    nivel += 1
    print('Llegaste al nivel', nivel)
  
  for i in range(9 + nivel):
    obstaculo_x = randint(0, width)
    obstaculo_y = randint(0, height) + frame_count
    obstaculo_y %= height
    text('🦠', obstaculo_x, obstaculo_y)

def setup():
# Ejecuta tu código una vez llegues aquí
  size(400, 400) # ancho y alto
  noStroke()
  text_size(40)
  text_align(CENTER, TOP)

def draw():
# Ejecuta tu código cada cuadro (frame) aquí
  global a_salvo, puntaje, nivel
  
  a_salvo = color(149, 161, 195)
  
  if nivel > 0:
    background(a_salvo)
    fill(145, 134, 126)
    text('Puntaje: ' + str(puntaje), width/2, 20)
    dibujar_obstaculos()
    dibujar_jugador()
  
# Mantén lo siguiente para ejecutar tu código
run()
