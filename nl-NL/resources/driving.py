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
    obstakel_x = randint(0, width) - (frame_count * level)
    obstakel_y = randint(0, height) 
    obstakel_x %= width # omwikkelen
    text('💩', obstakel_x, obstakel_y)
    
# De teken_speler functie komt hier
def teken_speler():
  
  global score, level
  
  speler_x = int(width * 0.2)
  speler_y = muis_y
  
  botsen = get(speler_x + 50, speler_y + 15)
  botsen2 = get(speler_x + 50, speler_y - 15)
  botsen3 = get(speler_x, speler_y + 15)
  botsen4 = get(speler_x, speler_y - 15)
  botsen5 = get(speler_x - 50, speler_y + 15)
  botsen6 = get(speler_x - 50, speler_y - 15)
  
  if speler_y > height - 18: # Voorbij de onderkant van het scherm
    botsen = veilig
    botsen3 = veilig
    botsen5 = veilig
    
  elif speler_y < 18: # Voorbij de bovenkant van het scherm
    botsen2 = veilig
    botsen4 = veilig
    botsen6 = veilig
    
  if botsen == veilig and botsen2 == veilig and botsen3 == veilig and botsen4 == veilig:
    image(auto, speler_x, speler_y, 100, 31)
    score += level
  else:
    text('💥', speler_x, speler_y)
    level = 0
    
  
def setup():
  # Stel hier je animatie in
  global auto
  
  size(400, 400)
  auto = load_image('car.png')
  image_mode(CENTER)
  
  
def draw():
  # Dingen om te doen in elk frame
  global score, veilig, level
  veilig = color(128)
  
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
