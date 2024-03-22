#!/bin/python3

# Importe les librairies de code
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
        ob_x %= width  # envelopper
        text('💩', ob_x, ob_y)
    
# La fonction dessine_joueur vient ici
def dessine_joueur():
    global score, niveau
    
    joueur_x = int(width * 0.2)
    joueur_y = mouse_y
    
    collision = get(joueur_x + 50, joueur_y + 15)
    collision2 = get(joueur_x + 50, joueur_y - 15).hex
    collision3 = get(joueur_x, joueur_y + 15).hex
    collision4 = get(joueur_x, joueur_y - 15).hex
    collision5 = get(joueur_x - 50, joueur_y + 15).hex
    collision6 = get(joueur_x - 50, joueur_y - 15).hex
    
    if joueur_y > height - 18: # Hors du bas de l'écran
        collision = sur.hex
        collision3 = sur.hex
        collision5 = sur.hex
      
    elif joueur_y < 18: # Hors du haut de l'écran
        collision2 = sur.hex
        collision4 = sur.hex
        collision6 = sur.hex
      
    if collision == sur.hex and collision2 == sur.hex and collision3 == sur.hex and collision4 == sur.hex:
        image(voiture, joueur_x, joueur_y, 100, 31)
        score += niveau
    else:
        text('💥', joueur_x, joueur_y)
        niveau = 0


def setup():
    # Configure ton animation ici
    size(400, 400)
    global voiture
    voiture = load_image('car.png')
    image_mode(CENTER)
  
  
def draw():
    # Choses à faire dans chaque image
    global score, sur, niveau
    sur = Color(128)
    
    if niveau > 0:
        background(sur)
        fill(255)
        text_size(16)
        text_align(RIGHT, TOP)
        text('Score', width * 0.45, 10, width * 0.5, 20)
        text(str(score), width * 0.45, 25, width * 0.5, 20)
        text_size(20)
        text_align(CENTER, TOP)  # position près du centre, en haut
        dessine_obstacles()
        dessine_joueur() 
  
run()
