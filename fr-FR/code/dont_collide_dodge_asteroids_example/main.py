#!/bin/python3

# Importe les librairies de code
from p5 import *
from random import randint, seed

niveau = 1
score = 0
vies = 3
invun = 0

# La fonction dessine_obstacle vient ici
def dessine_obstacles():
    global niveau
    
    seed(random_seed)
    
    if frame_count % height == height - 1 and niveau < 8:
        niveau += 1
        print('Tu as atteint le niveau', niveau)
      
    for i in range(6 + niveau):
        ob_x = randint(0, width)
        ob_y = randint(0, height) + (frame_count * niveau)
        ob_y %= height  # envelopper
        push_matrix()
        translate(ob_x, ob_y)
        rotate(degrees(randint(1, 359)+frame_count / 1000))
        image(rock, 0, 0, randint(18,24), randint(18,24))
        pop_matrix()

    
# La fonction dessine_joueur vient ici
def dessine_joueur():
    global score, niveau, vies, invun
    
    joueur_y = int(height * 0.8)
    joueur_x = mouse_x
    
    collision = get(joueur_x, joueur_y).hex
    collision2 = get(joueur_x - 18, joueur_y + 17).hex
    collision3 = get(joueur_x + 18, joueur_y + 17).hex
    collision4 = get(joueur_x, joueur_y + 25).hex
    
    if joueur_x < width: # hors de la gauche de l'écran
        collision2 = sur.hex
    
    if joueur_x > width: # hors de la droite de l'écran
        collision3 = sur.hex
      
    if (collision == sur.hex and collision2 == sur.hex and collision3 == sur.hex and collision4 == sur.hex) or invun > 0:
        if vies == 0 and frame_count % 12 == 0:
            tint(200, 0, 0)
      
        image(rocket, joueur_x, joueur_y + 25, 64, 64)
        score += niveau
        invun -= 1
        no_tint()
      
        if invun > 0:
            stroke(220)
            fill(220, 220, 220, 60)
            ellipse(joueur_x, joueur_y + 18, 47, 47)
        
    elif vies > 1:
        vies -= 1
        invun = 50
        tint(200, 0, 0)
        image(rocket, joueur_x, joueur_y + 25, 64, 64)
        no_tint()
        score += niveau
    else:
        text('💥', joueur_x + 10, joueur_y + 5)
        niveau = 0
    

def affichage_score():
    global niveau
    
    fill(255)
    text_size(16)
    text_align(RIGHT, TOP)
    text('Score', width * 0.45, 10, width * 0.5, 20)
    text(str(score), width * 0.45, 25, width * 0.5, 20)
    
    if score > 10000:
        niveau = 0
        print('🎉🎉 Tu as gagné ! 🎉🎉')

  
def affichage_vies():
    fill(255)
    text_size(16)
    text_align(LEFT, TOP)
    text('Vies', width * 0.05, 10, 30, 20)
    
    for i in range(vies):
        image(rocket, width * 0.05 + i * 25, 40, 20, 20)
  

def setup():
    # Configure ton animation ici
    size(400, 400)
    global rocket, rock, random_seed
    
    text_size(40)
    text_align(CENTER, TOP)  # position près du centre, en haut
    
    rocket = load_image('rocket.png')
    rock = load_image('moon.png')
    random_seed = randint(0, 1000000)
  
def draw():
    # Choses à faire dans chaque image
    global score, sur, niveau
    sur = Color(0)
    
    if niveau > 0:
        background(sur) 
        fill(255)
        image_mode(CENTER)
        dessine_obstacles()
        dessine_joueur()
        affichage_score()
        affichage_vies()
  
run()
