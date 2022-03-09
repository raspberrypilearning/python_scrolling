#!/bin/python3

# Importer le code de la bibliothèque
from p5 import *
from random import randint, seed

niveau = 1
score = 0

# La fonction dessine_obstacle vient ici
def dessine_obstacles():
  
  global niveau
  
  seed(123456789)
  
  if frame_count % width == width - 1 and niveau < 10:
    niveau += 1
    print('Tu as atteint le niveau', niveau)
    
  for i in range(6 + niveau):
    ob_x = randint(0, width) - (frame_count * niveau)
    ob_y = randint(0, height) 
    ob_x %= width # envelopper
    text('💩', ob_x, ob_y)
    
# La fonction dessine_joueur vient ici
def dessine_joueur():
  
  global score, niveau
  
  joueur_x = int(width * 0.2)
  joueur_y = mouse_y
  
  collision = get(joueur_x + 50, joueur_y + 15)
  collision2 = get(joueur_x + 50, joueur_y - 15)
  collision3 = get(joueur_x, joueur_y + 15)
  collision4 = get(joueur_x, joueur_y - 15)
  collision5 = get(joueur_x - 50, joueur_y + 15)
  collision6 = get(joueur_x - 50, joueur_y - 15)
  
  if joueur_y > height - 18: # Hors dessous de l'écran
    collision = sur
    collision3 = sur
    collision5 = sur
    
  elif joueur_y < 18: # hors dessus écran
    collision2 = sur
    collision4 = sur
    collision6 = sur
    
  if collision == sur and collision2 == sur and collision3 == sur and collision4 == sur:
    image(car, joueur_x, joueur_y, 100, 31)
    score += niveau
  else:
    text('💥', joueur_x, joueur_y)
    niveau = 0
    
  
def setup():
  # Configure ton animation ici
  global car
  
  size(400, 400)
  car = load_image('car.png')
  image_mode(CENTER)
  
  
def draw():
  # Choses à faire dans chaque image
  global score, sur, niveau
  sur = color(128)
  
  if niveau > 0:
    background(sur)
    fill(255)
    text_size(16)
    text_align(RIGHT, TOP)
    text('Score', width * 0.45, 10, width * 0.5, 20)
    text(str(score), width * 0.45, 25, width * 0.5, 20)
    text_size(20)
    text_align(CENTER, TOP) # position près du centre, en haut
    dessine_obstacles()
    dessine_joueur()
  
run()
