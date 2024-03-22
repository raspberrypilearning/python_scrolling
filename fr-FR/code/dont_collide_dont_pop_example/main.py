#!/bin/python3

# Importe les librairies de code
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
        ob_y %= height  # envelopper
        text('🌵', ob_x, ob_y)


# La fonction dessine_joueur vient ici
def dessine_joueur():
    global score, niveau
  
    joueur_y = int(height * 0.8)
  
    collision = get(mouse_x, joueur_y).hex
    collision2 = get(mouse_x - 12, joueur_y + 20).hex
    collision3 = get(mouse_x + 12, joueur_y + 20).hex
    collision4 = get(mouse_x, joueur_y + 40).hex
  
    if mouse_x < width : # hors de la gauche de l'écran
        collision2 = sur.hex
  
    if mouse_x > width : # hors de la droite de l'écran
        collision3 = sur.hex
  
    if collision == sur.hex and collision2 == sur.hex and collision3 == sur.hex and collision4 == sur.hex:
        text('🎈', mouse_x, joueur_y)
        score += niveau
    else:
        text('💥', mouse_x, joueur_y)
        niveau = 0


def setup():
    # Configure ton animation ici
    size(400, 400)
    text_size(40)
    text_align(CENTER, TOP)  # position près du centre, en haut


def draw():
    # Choses à faire dans chaque image
    global score, sur, niveau
    sur = Color(200, 150, 0)

    if niveau > 0:
        background(sur)
        fill(255)
        text('Score: ' + str(score), width/2, 20)
        dessine_obstacles()
        dessine_joueur()

run()
