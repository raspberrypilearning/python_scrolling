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
  
  speler_y = int(height * 0,8)
  
  no_fill()
  #ellipse(muis_x, speler_y, 10, 10) # teken botsingspunt
  #ellipse(muis_x, speler_y + 40, 10, 10)
  #ellipse(muis_x - 12, speler_y + 20, 10, 10)
  #ellipse(muis_x + 12, speler_y + 20, 10, 10)

  botsen = get(muis_x, speler_y)
  botsen2 = get(muis_x - 12, speler_y + 20)
  botsen3 = get(muis_x + 12, speler_y + 20)
  botsen4 = get(muis_x, speler_y + 40)
  
  if muis_x < width: # voorbij de linkerkant van het scherm
    botsen2 = veilig
  
  if muis_x > width: # voorbij de rechterkant van het scherm
    botsen3 = veilig
    
  if botsen == veilig and botsen2 == veilig and botsen3 == veilig and botsen4 == veilig:
    text('🎈', muis_x, speler_y)
    score += level
  else:
    text('💥', muis_x, speler_y)
    level = 0
    
  
def setup():
  # Stel hier je animatie in
  text_size(40)
  text_align(CENTER, TOP) # positie rond het midden, bovenaan
  size(400, 400)
  
  
def draw():
  # Dingen om te doen in elk frame
  global score, veilig, level
  veilig = color(200, 150, 0)
  
  if level > 0:
    background(veilig) 
    fill(255)
    text('Score: ' + str(score), width/2, 20)
    teken_obstakels()
    teken_speler()
  
run()
