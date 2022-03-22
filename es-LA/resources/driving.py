#!/bin/python3

# Importar el código de la Biblioteca p5
from p5 import *
from random import randint, seed

nivel = 1
puntaje = 0

# Aquí va la función dibujar_obstaculos
def dibujar_obstaculos():
  
  global nivel
  
  seed(123456789)
  
  if frame_count % width == width - 1 and nivel < 10:
    nivel += 1
    print('Llegaste al nivel', nivel)
    
  for i in range(6 + nivel):
    obstaculo_x = randint(0, width) - (frame_count * nivel)
    obstaculo_y = randint(0, height) 
    obstaculo_x %= width # recircular
    text('💩', obstaculo_x, obstaculo_y)
    
# Aquí va la función dibujar_jugador
def dibujar_jugador():
  
  global puntaje, nivel
  
  jugador_x = int(width * 0.2)
  jugador_y = mouse_y
  
  colision = get(jugador_x + 50, jugador_y + 15)
  colision2 = get(jugador_x + 50, jugador_y - 15)
  colision3 = get(jugador_x, jugador_y + 15)
  colision4 = get(jugador_x, jugador_y - 15)
  colision5 = get(jugador_x - 50, jugador_y + 15)
  colision6 = get(jugador_x - 50, jugador_y - 15)
  
  if jugador_y > height - 18: # A la parte inferior de la pantalla
    colision = a_salvo
    colision3 = a_salvo
    colision5 = a_salvo
    
  elif jugador_y < 18: # A la parte superior de la pantalla
    colision2 = a_salvo
    colision4 = a_salvo
    colision6 = a_salvo
    
  if colision == a_salvo and colision2 == a_salvo and colision3 == a_salvo and colision4 == a_salvo:
    image(carro, jugador_x, jugador_y, 100, 31)
    puntaje += nivel
  else:
    text('💥', jugador_x, jugador_y)
    nivel = 0
    
  
def setup():
  # Configura tu animación aquí
  global carro
  
  size(400, 400)
  carro = load_image('car.png')
  image_mode(CENTER)
  
  
def draw():
  # Cosas que hacer en cada cuadro (Frame)
  global puntaje, a_salvo, nivel
  a_salvo = color(128)
  
  if nivel > 0:
    background(a_salvo)
    fill(255)
    text_size(16)
    text_align(RIGHT, TOP)
    text('Puntaje', width * 0.45, 10, width * 0.5, 20)
    text(str(puntaje), width * 0.45, 25, width * 0.5, 20)
    text_size(20)
    text_align(CENTER, TOP) # ubicado al centro y arriba
    dibujar_obstaculos()
    dibujar_jugador()
  
run()
