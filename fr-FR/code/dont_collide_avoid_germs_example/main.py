#!/bin/python3

from p5 import *
from random import randint, seed

niveau = 1
score = 0

def joueur_sur():
    global joueur_y
    
    # Le visage
    fill(200, 134, 145)
    ellipse(mouse_x, joueur_y, 60, 60)
  
    # Les yeux
    fill(178, 200, 145)
    ellipse(mouse_x - 10, joueurs_y - 10, 20, 20)
    ellipse(mouse_x + 10, joueur_y - 10, 20, 20)
    fill(0)
    ellipse(mouse_x - 10, joueur_y - 10, 10, 10)
    ellipse(mouse_x + 10, joueur_y - 10, 10, 10)
    fill(255)
    ellipse(mouse_x - 12, joueur_y - 12, 5, 5)
    ellipse(mouse_x + 12, joueur_y - 12, 5, 5)
    
    # La bouche
    fill(0)
    ellipse(mouse_x, joueur_y + 10, 15, 10)
    fill(200, 134, 145)
    ellipse(mouse_x, joueur_y + 5, 10, 10)

def joueur_ecrase():
    global joueur_y
    
    # Le visage
    fill(178, 200, 145)
    ellipse(mouse_x, joueur_y, 60, 60)
  
    # Les yeux
    fill(149, 161, 195)
    ellipse(mouse_x - 10, joueur_y - 10, 20, 20)
    ellipse(mouse_x + 10, joueur_y - 10, 20, 20)
    fill(0)
    ellipse(mouse_x - 10, joueur_y - 10, 10, 10)
    ellipse(mouse_x + 10, joueur_y - 10, 10, 10)
    fill(255)
    ellipse(mouse_x - 12, joueur_y - 12, 5, 5)
    ellipse(mouse_x + 12, joueur_y - 12, 5, 5)
    
    # La bouche
    fill(0)
    ellipse(mouse_x, joueur_y + 15, 15, 10)
    fill(178, 200, 145)
    ellipse(mouse_x, joueur_y + 20, 10, 10)
  
def dessine_joueur():
  
    global joueur_y, sur, score, niveau
    
    joueur_y = int(height * 0.8)
    
    collision = get(mouse_x, joueur_y).hex
    collision2 = get(mouse_x, joueur_y + 30).hex
    collision3 = get(mouse_x + 30, joueur_y).hex
    collision4 = get(mouse_x, joueur_y - 30).hex
    
    if mouse_x < width: # dépasse la gauche de l'écran
        collision2 = sur.hex
    
    if mouse_x > width : # dépasse la droite de l'écran
        collision3 = sur.hex
      
    #print(collision, collision2, collision3, collision4)
      
    if collision == sur.hex and collision2 == sur.hex and collision3 == sur.hex and collision4 == sur.hex:
        joueur_sur() 
        score += niveau
    else: # Collision
        joueur_ecrase()
        niveau = 0
  
def dessine_obstacles():
    global niveau
    
    seed(41143644)
    
    if frame_count & height == height - 1 and niveau < 5:
        niveau += 1
        print('Tu as atteint le niveau', niveau)
    
    for i in range(9 + niveau):
        ob_x = randint(0, width)
        ob_y = randint(0, height) + frame_count
        ob_y %= height
        text('🦠', ob_x, ob_y)

def setup():
    # Mets le code à exécuter au démarrage ici
    size(400, 400) # largeur et hauteur
    no_stroke()
    text_size(40)
    text_align(CENTER, TOP)

def draw():
    # Mets le code à exécuter à chaque image ici
    global sur, score, niveau
  
    sur = Color(149, 161, 195)
  
    if niveau > 0:
        background(sur)
        fill(145, 134, 126)
        text('Score: ' + str(score), width/2, 20)
        dessine_obstacles()
        dessine_joueur() 
  
# Garde ceci pour exécuter ton code
run()
