#!/bin/python3

# Εισαγωγή του κώδικα της βιβλιοθήκης
from p5 import *
from random import randint, seed

level = 1
score = 0

# Η συνάρτηση draw_obstacle πηγαίνει εδώ
def draw_obstacles():
  
  global level
  
  seed(12345678)
  
  if frame_count % height == height - 1 and level < 5:
    level += 1
    print('Έφτασες στο επίπεδο', level)
    
  for i in range(6 + level):
    ob_x = randint(0, height)
    ob_y = randint(0, height) + (frame_count * level)
    ob_y %= height # επανεμφάνιση στην αντίθετη πλευρά
    text('🌵', ob_x, ob_y)

    
# Η συνάρτηση draw_player πηγαίνει εδώ
def draw_player():
  
  global score, level
  
  player_y = int(height * 0.8)
  
  no_fill()
  #ellipse(mouse_x, player_y, 10, 10) # σχεδίαση του σημείου σύγκρουσης
  #ellipse(mouse_x, player_y + 40, 10, 10)
  #ellipse(mouse_x - 12, player_y + 20, 10, 10)
  #ellipse(mouse_x + 12, player_y + 20, 10, 10)

  collide = get(mouse_x, player_y)
  collide2 = get(mouse_x - 12, player_y + 20)
  collide3 = get(mouse_x + 12, player_y + 20)
  collide4 = get(mouse_x, player_y + 40)
  
  if mouse_x < width: # Εκτός της αριστερής πλευράς της οθόνης
    collide2 = safe
  
  if mouse_x > width: # Εκτός της δεξιάς πλευράς της οθόνης
    collide3 = safe
    
  if collide == safe and collide2 == safe and collide3 == safe and collide4 == safe:
    text('🎈', mouse_x, player_y)
    score += level
  else:
    text('💥', mouse_x, player_y)
    level = 0
    
  
def setup():
  # Ορισμός της κινούμενης εικόνας σου εδώ
  text_size(40)
  text_align(CENTER, TOP) # θέση γύρω από το κέντρο, επάνω
  size(400, 400)
  
  
def draw():
  # Ενέργειες που πρέπει να γίνονται σε κάθε καρέ
  global score, safe, level
  safe = color(200, 150, 0)
  
  if level > 0:
    background(safe) 
    fill(255)
    text('Σκορ: ' + str(score), width/2, 20)
    draw_obstacles()
    draw_player()
  
run()
