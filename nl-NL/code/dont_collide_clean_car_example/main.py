#!/bin/python3

# Bibliotheekcode importeren
from p5 import *
from random import randint, seed

level = 1
score = 0

# De teken_obstakel functie komt hier
def teken_obstakels():
    global level
    
    seed(123456789)
    
    if frame_count % width == width - 1 and level < 10:
        level += 1
        print('Je hebt level', level, 'bereikt')
      
    for i in range(6 + level):
        ob_x = randint(0, width) - (frame_count * level)
        ob_y = randint(0, height) 
        ob_x %= width #omwikkelen
        text('💩', ob_x, ob_y)
    
# De teken_speler functie komt hier
def teken_speler():
    global score, level
    
    speler_x = int(width * 0.2)
    speler_y = mouse_y
    
    botsen = get(speler_x + 50, speler_y + 15).hex
    botsen2 = get(speler_x + 50, speler_y - 15).hex
    botsen3 = get(speler_x, speler_y + 15).hex
    botsen4 = get(speler_x, speler_y - 15).hex
    botsen5 = get(speler_x - 50, speler_y + 15).hex
    botsen6 = get(speler_x - 50, speler_y - 15).hex
    
    if speler_y > height - 18: # Aan de onderkant van het scherm
        botsen = veilig.hex
        botsen3 = veilig.hex
        botsen5 = veilig.hex
      
    elif speler_y < 18: # Buiten de bovenkant van het scherm
        botsen2 = veilig.hex
        botsen4 = veilig.hex
        botsen6 = veilig.hex
      
    if botsen == veilig.hex and botsen2 == veilig.hex and botsen3 == veilig.hex and botsen4 == veilig.hex:
        image(auto, speler_x, speler_y, 100, 31)
        score += level
    else:
        text('💥', speler_x, speler_y)
        level = 0


def setup():
    # Stel hier je animatie in
    size(400, 400)
    global auto
    auto = load_image('car.png')
    image_mode(CENTER)
  
  
def draw():
    # Dingen om te doen in elk frame
    global score, veilig, level
    veilig = Color(128)
    
    if level > 0:
        background(veilig)
        fill(255)
        text_size(16)
        text_align(RIGHT, TOP)
        text('Score', width * 0.45, 10, width * 0.5, 20)
        text(str(score), width * 0.45, 25, width * 0.5, 20)
        text_size(20)
        text_align(CENTER, TOP) # positie rond het midden, bovenaan
        teken_obstakels()
        teken_speler()
  
run()
