#!/bin/python3

# Bibliotheekcode importeren
from p5 import *
from random import randint, seed

level = 1
score = 0

# De teken_obstakel functie komt hier
def teken_obstakels():
    global level
  
    seed(12345678)
  
    if frame_count % height == height - 1 and level < 5:
        level += 1
        print('Je hebt level', level, 'bereikt')
  
    for i in range(6 + level):
        obstakel_x = randint(0, height)
        obstakel_y = randint(0, height) + (frame_count * level)
        obstakel_y %= height # omwikkelen
        text('🌵', obstakel_x, obstakel_y)


# De teken_speler functie komt hier
def teken_speler():
    global score, level
  
    speler_y = int(height * 0.8)
  
    botsen = get(mouse_x, speler_y).hex
    botsen2 = get(mouse_x, speler_y + 20).hex
    botsen3 = get(mouse_x + 12, speler_y + 20).hex
    botsen4 = get(mouse_x, speler_y + 40).hex
  
    if mouse_x < width: # aan de linkerkant van het scherm
        botsen2 = veilig.hex
  
    if mouse_x > width: # voorbij de rechterkant van het scherm
        botsen3 = veilig.hex
  
    if botsen == veilig.hex and botsen2 == veilig.hex and botsen3 == veilig.hex and botsen4 == veilig.hex:
        text('🎈', mouse_x, speler_y)
        score += level
    else:
        text('💥', mouse_x, speler_y)
        level = 0


def setup():
    # Stel hier je animatie in
    size(400, 400)
    text_size(40)
    text_align(CENTER, TOP) # positie rond het midden, bovenaan


def draw():
    # Dingen om te doen in elk frame
    global score, veilig, level
    veilig = Color(200, 150, 0)

    if level > 0:
        background(veilig)
        fill(255)
        text('Score: ' + str(score), width/2, 20)
        teken_obstakels()
        teken_speler()

run()
