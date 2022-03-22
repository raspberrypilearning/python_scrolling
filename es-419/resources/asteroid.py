#!/bin/python3

# Importar el código de la Biblioteca p5
from p5 import *
from random import randint, seed

nivel = 1
puntaje = 0
vidas = 3
invul = 0 #invulnerabilidad

# Aquí va la función dibujar_obstaculos
def dibujar_obstaculos():
  
  global nivel
  
  seed(semilla_aleatoria)
  
  if frame_count % height == height - 1 and nivel < 8:
    nivel += 1
    print('Llegaste al nivel', nivel)
    
  for i in range(6 + nivel):
    obstaculo_x = randint(0, width)
    obstaculo_y = randint(0, height) + (frame_count * nivel)
    obstaculo_y %= height # recircular
    push_matrix()
    translate(obstaculo_x, obstaculo_y)
    rotate(degrees(randint(1, 359)+frame_count / 1000))
    image(asteroide, 0, 0, randint(18,24), randint(18,24))
    pop_matrix()

    
# Aquí va la función dibujar_jugador
def dibujar_jugador():
  
  global puntaje, nivel, vidas, invul
  
  jugador_y = int(height * 0.8)
  jugador_x = mouse_x
  
  colision = get(jugador_x, jugador_y)
  colision2 = get(jugador_x - 18, jugador_y + 17)
  colision3 = get(jugador_x + 18, jugador_y + 17)
  colision4 = get(jugador_x, jugador_y + 25)
  
  if jugador_x < width: # a la izquierda de la pantalla
    colision2 = a_salvo
  
  if jugador_x > width: # a la derecha de la pantalla
    colision3 = a_salvo
    
  if (colision == a_salvo and colision2 == a_salvo and colision3 == a_salvo and colision4 == a_salvo) or invul > 0:
    if vidas == 0 and frame_count % 12 == 0:
      tint(200, 0, 0)
    
    image(cohete, jugador_x, jugador_y + 25, 64, 64)
    puntaje += nivel
    invul -= 1
    no_tint()
    
    if invul > 0:
      stroke(220)
      fill(220, 220, 220, 60)
      ellipse(jugador_x, jugador_y + 18, 47, 47)
      
  elif vidas > 0:
    vidas -= 1
    invul = 50
    tint(200, 0, 0)
    image(cohete, jugador_x, jugador_y + 25, 64, 64)
    no_tint()
    puntaje += nivel
  else:
    text('💥', jugador_x + 10, jugador_y + 5)
    nivel = 0
    

def mostrar_puntaje():
  global nivel
  
  fill(255)
  text_size(16)
  text_align(RIGHT, TOP)
  text('Puntaje', width * 0.45, 10, width * 0.5, 20)
  text(str(puntaje), width * 0.45, 25, width * 0.5, 20)
  
  if puntaje > 10000:
    nivel = 0
    print('🎉🎉 ¡Ganaste! 🎉🎉')

  
def mostrar_vidas():
  fill(255)
  text_size(14.9)
  text_align(LEFT, TOP)
  text('Vidas', width * 0.05, 10, 30, 20)
  
  for i in range(vidas):
    image(cohete, width * 0.05 + i * 25, 40, 20, 20)
  

def setup():
  # Configura tu animación aquí
  global cohete, asteroide, semilla_aleatoria
  
  text_size(40)
  text_align(CENTER, TOP) # ubicado al centro y arriba
  size(400, 400)
  
  cohete = load_image('rocket.png')
  asteroide = load_image('moon.png')
  semilla_aleatoria = randint(0, 1000000)
  
def draw():
  # Cosas que hacer en cada cuadro (Frame)
  global puntaje, a_salvo, nivel
  a_salvo = color(0)
  
  if nivel > 0:
    background(a_salvo) 
    fill(255)
    image_mode(CENTER)
    dibujar_obstaculos()
    dibujar_jugador()
    mostrar_puntaje()
    mostrar_vidas()
  
run()
