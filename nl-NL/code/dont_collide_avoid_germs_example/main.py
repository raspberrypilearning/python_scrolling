#!/bin/python3

from p5 import *
from random import randint, seed

level = 1
score = 0

def speler_veilig():
    global speler_y
    
    # Gezicht
    fill(200, 134, 145)
    ellipse(mouse_x, speler_y, 60, 60)
  
    # Ogen
    fill(178, 200, 145)
    ellipse(mouse_x - 10, speler_y - 10, 20, 20)
    ellipse(mouse_x + 10, speler_y - 10, 20, 20)
    fill(0)
    ellipse(mouse_x - 10, speler_y - 10, 10, 10)
    ellipse(mouse_x + 10, speler_y - 10, 10, 10)
    fill(255)
    ellipse(mouse_x - 12, speler_y - 12, 5, 5)
    ellipse(mouse_x + 12, speler_y - 12, 5, 5)
    
    # Mond
    fill(0)
    ellipse(mouse_x, speler_y + 10, 15, 10)
    fill(200, 134, 145)
    ellipse(mouse_x, speler_y + 5, 10, 10)

def speler_gebotst():
    global speler_y
    
    # Gezicht
    fill(178, 200, 145)
    ellipse(mouse_x, speler_y, 60, 60)
  
    # Ogen
    fill(149, 161, 195)
    ellipse(mouse_x - 10, speler_y - 10, 20, 20)
    ellipse(mouse_x + 10, speler_y - 10, 20, 20)
    fill(0)
    ellipse(mouse_x - 10, speler_y - 10, 10, 10)
    ellipse(mouse_x + 10, speler_y - 10, 10, 10)
    fill(255)
    ellipse(mouse_x - 12, speler_y - 12, 5, 5)
    ellipse(mouse_x + 12, speler_y - 12, 5, 5)
    
    # Mond
    fill(0)
    ellipse(mouse_x, speler_y + 15, 15, 10)
    fill(178, 200, 145)
    ellipse(mouse_x, speler_y + 20, 10, 10)
  
def teken_speler():
  
    global speler_y, veilig, score, level
    
    speler_y = int(height * 0.8)
    
    botsen = get(mouse_x, speler_y).hex
    botsen2 = get(mouse_x, speler_y + 30).hex
    botsen3 = get(mouse_x + 30, speler_y).hex
    botsen4 = get(mouse_x, speler_y - 30).hex
    
    if mouse_x < width: # voorbij de linkerkant van het scherm
        botsen2 = veilig.hex
    
    if mouse_x > width: # voorbij de rechterkant van het scherm
        botsen3 = veilig.hex
      
    #print(botsen, botsen2, botsen3, botsen4)
      
    if botsen == veilig.hex and botsen2 == veilig.hex and botsen3 == veilig.hex and botsen4 == veilig.hex:
        speler_veilig()
        score += level
    else: # Gebotst
        speler_gebotst()
        level = 0
  
def teken_obstakels():
    global level
    
    seed(41143644)
    
    if frame_count & height == height - 1 and level < 5:
        level += 1
        print('Je hebt level', level, 'bereikt')
    
    for i in range(9 + level):
        ob_x = randint(0, width)
        ob_y = randint(0, height) + frame_count
        ob_y %= height
        text('🦠', ob_x, ob_y)

def setup():
    # Zet de code om eenmalig uit te voeren hier onder
    size(400, 400) # breedte en hoogte
    no_stroke()
    text_size(40)
    text_align(CENTER, TOP)

def draw():
    # Zet hier code om bij elk frame uit te voeren
    global score, veilig, level
  
    veilig = Color(149, 161, 195)
  
    if level > 0:
        background(veilig)
        fill(145, 134, 126)
        text('Score: ' + str(score), width/2, 20)
        teken_obstakels()
        teken_speler()
  
# Bewaar dit om je code uit te voeren
run()
