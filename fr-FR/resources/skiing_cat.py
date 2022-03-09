#!/bin/python3

# Importer le code de la bibliothèque
from p5 import *
from random import randint, seed

niveau = 1
score = 0

# La fonction dessine_obstacle vient ici
def dessine_obstacles():
  
  global niveau
  
  seed(12345678)
  
  if frame_count % height == height - 1 and niveau < 5:
    niveau += 1
    print('Tu as atteint le niveau', niveau)
    
  for i in range(6 + niveau):
    ob_x = randint(0, height)
    ob_y = randint(0, height) + (frame_count * niveau)
    ob_y %= height # enveloppant
    text('🌵', ob_x, ob_y)

    
# La fonction dessine_joueur vient ici
def dessine_joueur():
  
  global score, niveau
  
  joueur_y = int(height * 0.8)
  
  no_fill()
  #ellipse(mouse_x, joueur_y, 10, 10) # dessine le point de collision
  #ellipse(mouse_x, joueur_y + 40, 10, 10)
  #ellipse(mouse_x - 12, joueur_y + 20, 10, 10)
  #ellipse(mouse_x + 12, joueur_y + 20, 10, 10)

  collision = get(mouse_x, joueur_y)
  collision2 = get(mouse_x - 12, joueur_y + 20)
  collision3 = get(mouse_x + 12, joueur_y + 20)
  collision4 = get(mouse_x, joueur_y + 40)
  
  if mouse_x < width: # sur la gauche de l'écran
    collision2 = sur
  
  if mouse_x > width: # à droite de l'écran
    collision3 = sur
    
  if collision == sur and collision2 == sur and collision3 == sur and collision4 == sur:
    text('🎈', mouse_x, joueur_y)
    score += niveau
  else:
    text('💥', mouse_x, joueur_y)
    niveau = 0
    
  
def setup():
  # Configure ton animation ici
  text_size(40)
  text_align(CENTER, TOP) # position près du centre, en haut
  size(400, 400)
  
  
def draw():
  # Choses à faire dans chaque image
  global score, sur, niveau
  sur = color(200, 150, 0)
  
  if niveau > 0:
    background(sur) 
    fill(255)
    text('Score: ' + str(score), width/2, 20)
    dessine_obstacles()
    dessine_joueur()
  
run()
