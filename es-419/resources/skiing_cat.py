#!/bin/python3

# Importar el código de la Biblioteca p5
from p5 import *
from random import randint, seed

velocidad = 1
puntaje = 0

# The draw_obstacles function goes here
def dibujar_obstaculos():
  
  global velocidad
  
  seed(12345678)
  
  if frame_count % height == height - 1 and velocidad < 5:
    velocidad += 1
    print('Llegaste al nivel', velocidad)
    
  for i in range(6):
    obstaculo_x = randint(0, height)
    obstaculo_y = randint(0, height) + (frame_count * velocidad)
    obstaculo_y %= height # recircular
    no_stroke()
    fill(0,255,0)
    triangle(obstaculo_x + 20, obstaculo_y + 20, obstaculo_x + 10, obstaculo_y + 40, obstaculo_x + 30, obstaculo_y + 40)
    triangle(obstaculo_x + 20, obstaculo_y + 30, obstaculo_x + 5, obstaculo_y + 55, obstaculo_x + 35, obstaculo_y + 55)
    triangle(obstaculo_x + 20, obstaculo_y + 40, obstaculo_x + 0, obstaculo_y + 70, obstaculo_x + 40, obstaculo_y + 70)
    fill(150,100,100)
    rect(obstaculo_x + 15, obstaculo_y + 70, 10, 10)
    
# Aquí va la función dibujar_jugador
def dibujar_jugador():
  
  global puntaje, velocidad, esquiador, estrellado
  
  jugador_y = int(height * 0.8)
  
  fill(a_salvo)

  colision = get(mouse_x, jugador_y)
  
  if colision == a_salvo:
    image(esquiador, mouse_x, jugador_y, 30, 30)
    puntaje += velocidad
  else:
    image(estrellado, mouse_x, jugador_y, 30, 30)
    velocidad = 0
    
  
def setup():
  
  global esquiador, estrellado
  
  # Configura tu animación aquí
  text_size(40)
  text_align(CENTER, TOP) # ubicado relativamente al centro
  size(400, 400)
  esquiador = load_image('skiing.png')
  estrellado = load_image('fallenover.png')
  
def draw():
  # Cosas que hacer en cada cuadro (Frame)
  global puntaje, a_salvo, velocidad, esquiador, estrellado
  a_salvo = color(255)

  if velocidad > 0:
    background(a_salvo) 
    fill(0)
    text('Puntaje: ' + str(puntaje), width/2, 20)
    dibujar_obstaculos()
    dibujar_jugador()
  
run()
