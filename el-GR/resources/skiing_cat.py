#!/bin/python3

#Εισαγωγή του κώδικα της βιβλιοθήκης
from p5 import *
from random import randint, seed

speed = 1
score = 0

# The draw_obstacles function goes here
def draw_obstacles():
  
  global speed
  
  seed(12345678)
  
  if frame_count % height == height - 1 and speed < 5:
    speed += 1
    print('Έφτασες στο επίπεδο', level)
    
  for i in range(6):
    ob_x = randint(0, height)
    ob_y = randint(0, height) + (frame_count * speed)
    ob_y %= height # επανεμφάνιση στην αντίθετη πλευρά
    no_stroke()
    fill(0,255,0)
    triangle(ob_x + 20, ob_y + 20, ob_x + 10, ob_y + 40, ob_x + 30, ob_y + 40)
    triangle(ob_x + 20, ob_y + 30, ob_x + 5, ob_y + 55, ob_x + 35, ob_y + 55)
    triangle(ob_x + 20, ob_y + 40, ob_x + 0, ob_y + 70, ob_x + 40, ob_y + 70)
    fill(150,100,100)
    rect(ob_x + 15, ob_y + 70, 10, 10)
    
# Η συνάρτηση draw_player πηγαίνει εδώ
def draw_player():
  
  global score, speed, skiing, crashed
  
  player_y = int(height * 0.8)
  
  fill(safe)

  collide = get(mouse_x, player_y)
  
  if collide == safe:
    image(skiing, mouse_x, player_y, 30, 30)
    score += speed
  else:
    image(crashed, mouse_x, player_y, 30, 30)
    speed = 0
    
  
def setup():
  
  global skiing, crashed
  
  # Ορισμός της κινούμενης εικόνας σου εδώ
  text_size(40)
  text_align(CENTER, TOP) # θέση γύρω από το κέντρο, επάνω
  size(400, 400)
  skiing = load_image('skiing.png')
  crashed = load_image('fallenover.png')
  
def draw():
  # Ενέργειες που πρέπει να γίνονται σε κάθε καρέ
  global score, safe, speed, skiing, crashed
  safe = color(255)

  if speed > 0:
    background(safe) 
    fill(0)
    text('Σκορ: ' + str(score), width/2, 20)
    draw_obstacles()
    draw_player()
  
run()
