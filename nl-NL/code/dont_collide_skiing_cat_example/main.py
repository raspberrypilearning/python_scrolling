#!/bin/python3

# Bibliotheekcode importeren
from p5 import *
from random import randint, seed

snelheid = 1
score = 0

# De functie teken_achtergrond komt hier
def teken_obstakels():
    global snelheid
    
    seed(12345678)
    
    if frame_count % height == height - 1 and snelheid < 5:
        snelheid += 1
        print('Je hebt snelheid', snelheid, 'bereikt')
      
    for i in range(6):
        obstakel_x = randint(0, height)
        obstakel_y = randint(0, height) + (frame_count * snelheid)
        obstakel_y %= height # omwikkelen
        no_stroke()
        fill(0,255,0)
        triangle(obstakel_x + 20, obstakel_y + 20, obstakel_x + 10, obstakel_y + 40, obstakel_x + 30, obstakel_y + 40)
        triangle(obstakel_x + 20, obstakel_y + 30, obstakel_x + 5, obstakel_y + 55, obstakel_x + 35, obstakel_y + 55)
        triangle(obstakel_x + 20, obstakel_y + 40, obstakel_x + 0, obstakel_y + 70, obstakel_x + 40, obstakel_y + 70)
        fill(150,100,100)
        rect(obstakel_x + 15, obstakel_y + 70, 10, 10)
    
# De teken_speler functie komt hier
def teken_speler():
    global score, snelheid, skien, gecrasht
    
    speler_y = int(height * 0.8)
    
    fill(veilig)
  
    botsen = get(mouse_x, speler_y).hex
    
    if botsen == veilig.hex:
        image(skien, mouse_x, speler_y, 30, 30)
        score += snelheid
    else:
        image(gecrasht, mouse_x, speler_y, 30, 30)
        snelheid = 0
    
  
def setup(): 
    # Stel hier je animatie in
    size(400, 400)
    text_size(40)
    text_align(CENTER, TOP) # positie rond het midden, bovenaan
    global skien, gecrasht
    skien = load_image('skiing.png')
    gecrasht = load_image('fallenover.png')
  
def draw():
    # Dingen om te doen in elk frame
    global score, veilig, skien, gecrasht
    veilig = Color(255)
  
    if snelheid > 0:
        background(veilig) 
        fill(0)
        text('Score: ' + str(score), width/2, 20)
        teken_obstakels()
        teken_speler()
  
run()
