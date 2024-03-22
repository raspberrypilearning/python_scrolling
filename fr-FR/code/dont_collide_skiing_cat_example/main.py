#!/bin/python3

# Importe les librairies de code
from p5 import *
from random import randint, seed

vitesse = 1
score = 0

# La fonction dessine_arriere_plan vient ici
def dessine_obstacles():
    global vitesse
    
    seed(12345678)
    
    if frame_count % height == height - 1 and vitesse < 5:
        vitesse += 1
        print('Tu as atteint le niveau', vitesse)
      
    for i in range(6):
        ob_x = randint(0, height)
        ob_y = randint(0, height) + (frame_count * vitesse)
        ob_y %= height  # envelopper
        no_stroke()
        fill(0,255,0)
        triangle(ob_x + 20, ob_y + 20, ob_x + 10, ob_y + 40, ob_x + 30, ob_y + 40)
        triangle(ob_x + 20, ob_y + 30, ob_x + 5, ob_y + 55, ob_x + 35, ob_y + 55)
        triangle(ob_x + 20, ob_y + 40, ob_x + 0, ob_y + 70, ob_x + 40, ob_y + 70)
        fill(150,100,100)
        rect(ob_x + 15, ob_y + 70, 10, 10)
    
# La fonction dessine_joueur vient ici
def dessine_joueur():
    global score, vitesse, ski, chute
    
    joueur_y = int(height * 0.8)
    
    fill(sur)
  
    collision = get(mouse_x, joueur_y).hex
    
    if collision == sur.hex:
        image(ski, mouse_x, joueur_y, 30, 30)
        score += vitesse
    else:
        image(chute, mouse_x, joueur_y, 30, 30)
        vitesse = 0
    
  
def setup(): 
    # Configure ton animation ici
    size(400, 400)
    text_size(40)
    text_align(CENTER, TOP)  # position près du centre
    global ski, chute
    ski = load_image('skiing.png')
    chute = load_image('fallenover.png')
  
def draw():
    # Choses à faire dans chaque image
    global score, sur, vitesse, ski, chute
    sur = Color(255)
  
    if vitesse > 0:
        background(sur) 
        fill(0)
        text('Score: ' + str(score), width/2, 20)
        dessine_obstacles()
        dessine_joueur()
  
run()
