#!/bin/python3

from p5 import *
from random import randint, seed

level = 1
score = 0

def safe_player():
  
  global player_y
  
  # Πρόσωπο
  fill(200, 134, 145)
  ellipse(mouse_x, player_y, 60, 60)

  #Μάτια
  fill(178, 200, 145)
  ellipse(mouse_x - 10, player_y - 10, 20, 20)
  ellipse(mouse_x + 10, player_y - 10, 20, 20)
  fill(0)
  ellipse(mouse_x - 10, player_y - 10, 10, 10)
  ellipse(mouse_x + 10, player_y - 10, 10, 10)
  fill(255)
  ellipse(mouse_x - 12, player_y - 12, 5, 5)
  ellipse(mouse_x + 12, player_y - 12, 5, 5)
  
  # Στόμα
  fill(0)
  ellipse(mouse_x, player_y + 10, 15, 10)
  fill(200, 134, 145)
  ellipse(mouse_x, player_y + 5, 10, 10)

def crashed_player():
  
  global player_y
  
  # Πρόσωπο
  fill(178, 200, 145)
  ellipse(mouse_x, player_y, 60, 60)

  # Μάτια
  fill(149, 161, 195)
  ellipse(mouse_x - 10, player_y - 10, 20, 20)
  ellipse(mouse_x + 10, player_y - 10, 20, 20)
  fill(0)
  ellipse(mouse_x - 10, player_y - 10, 10, 10)
  ellipse(mouse_x + 10, player_y - 10, 10, 10)
  fill(255)
  ellipse(mouse_x - 12, player_y - 12, 5, 5)
  ellipse(mouse_x + 12, player_y - 12, 5, 5)
  
  # Στόμα
  fill(0)
  ellipse(mouse_x, player_y + 15, 15, 10)
  fill(178, 200, 145)
  ellipse(mouse_x, player_y + 20, 10, 10)
  
def draw_player():
  
  global player_y, safe, score, level
  
  player_y = int(height * 0.8)
  
  collide = get(mouse_x, player_y)
  collide2 = get(mouse_x, player_y + 30)
  collide3 = get(mouse_x + 30, player_y)
  collide4 = get(mouse_x, player_y - 30)
  
  if mouse_x < width: # Εκτός της αριστερής πλευράς της οθόνης
    collide2 = safe
  
  if mouse_x > width: # Εκτός της δεξιάς πλευράς της οθόνης
    collide3 = safe
    
  #print(collide, collide2, collide3, collide4)
    
  if collide == safe and collide2 == safe and collide3 == safe and collide4 == safe:
    safe_player()
    score += level
  else: # Σύγκρουση
    crashed_player()
    level = 0
  
def draw_obstacles():
  
  global level
  
  seed(41143644)
  
  if frame_count & height == height - 1 and level < 5:
    level += 1
    print('Έφτασες στο επίπεδο', level)
  
  for i in range(9 + level):
    ob_x = randint(0, width)
    ob_y = randint(0, height) + frame_count
    ob_y %= height
    text('🦠', ob_x, ob_y)

def setup():
# Βάλε εδώ κώδικα που θα εκτελεστεί μια φορά
  size(400, 400) # πλάτος και ύψος
  no Stroke()
  text_size(40)
  text_align(CENTER, TOP)

def draw():
# Βάλε εδώ κώδικα που θα εκτελείται σε κάθε καρέ
  global safe, score, level
  
  safe = color(149, 161, 195)
  
  if level > 0:
    background(safe)
    fill(145, 134, 126)
    text('Σκορ: ' + str(score), width/2, 20)
    draw_obstacles()
    draw_player()
  
# Από εδώ εκτελείς τον κώδικά σου
run()
