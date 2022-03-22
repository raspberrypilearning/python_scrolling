#!/bin/python3

# Importar el código de la Biblioteca p5
from p5 import *
from random import randint, seed

nivel = 1
puntaje = 0

# Aquí va la función dibujar_obstaculos
def dibujar_obstaculos():
  
  global nivel
  
  seed(12345678)
  
  if frame_count % height == height - 1 and nivel < 5:
    nivel += 1
    print('Llegaste al nivel', nivel)
    
  for i in range(6 + nivel):
    obstaculo_x = randint(0, height)
    obstaculo_y = randint(0, height) + (frame_count * nivel)
    obstaculo_y %= height # recircular
    text('🌵', obstaculo_x, obstaculo_y)

    
# Aquí va la función dibujar_jugador
def dibujar_jugador():
  
  global puntaje, nivel
  
  jugador_y = int(height * 0.8)
  
  no_fill()
  #ellipse(mouse_x, jugador_y, 10, 10) # dibuja el punto de colisión
  #ellipse(mouse_x, jugador_y + 40, 10, 10)
  #ellipse(mouse_x - 12, jugador_y + 20, 10, 10)
  #ellipse(mouse_x + 12, jugador_y + 20, 10, 10)

  colision = get(mouse_x, jugador_y)
  colision2 = get(mouse_x - 12, jugador_y + 20)
  colision3 = get(mouse_x + 12, jugador_y + 20)
  colision4 = get(mouse_x, jugador_y + 40)
  
  if mouse_x < width: # a la izquierda de la pantalla
    colision2 = a_salvo
  
  if mouse_x > width: # a la derecha de la pantalla
    colision3 = a_salvo
    
  if colision == a_salvo and colision2 == a_salvo and colision3 == a_salvo and colision4 == a_salvo:
    text('🎈', mouse_x, jugador_y)
    puntaje += nivel
  else:
    text('💥', mouse_x, jugador_y)
    nivel = 0
    
  
def setup():
  # Configura tu animación aquí
  text_size(40)
  text_align(CENTER, TOP) # ubicado al centro y arriba
  size(400, 400)
  
  
def draw():
  # Cosas que hacer en cada cuadro (Frame)
  global puntaje, a_salvo, nivel
  a_salvo = color(200, 150, 0)
  
  if nivel > 0:
    background(a_salvo) 
    fill(255)
    text('Puntaje: ' + str(puntaje), width/2, 20)
    dibujar_obstaculos()
    dibujar_jugador()
  
run()
