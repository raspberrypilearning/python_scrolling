#!/bin/python3

# Εισαγωγή του κώδικα της βιβλιοθήκης
from p5 import *
from random import randint, seed

level = 1
score = 0
lives = 3
invun = 0

# Η συνάρτηση draw_obstacle πηγαίνει εδώ
def draw_obstacles():
  
  global level
  
  seed(random_seed)
  
  if frame_count % height == height - 1 and level < 8:
    level += 1
    print('Έφτασες στο επίπεδο', level)
    
  for i in range(6 + level):
    ob_x = randint(0, width)
    ob_y = randint(0, height) + (frame_count * level)
    ob_y %= height # επανεμφάνιση στην αντίθετη πλευρά
    push_matrix()
    translate(ob_x, ob_y)
    rotate(degrees(randint(1, 359)+frame_count / 1000))
    image(rock, 0, 0, randint(18,24), randint(18,24))
    pop_matrix()

    
# Η συνάρτηση draw_player πηγαίνει εδώ
def draw_player():
  
  global score, level, lives, invun
  
  player_y = int(height * 0.8)
  player_x = mouse_x
  
  collide = get(player_x, player_y)
  collide2 = get(player_x - 18, player_y + 17)
  collide3 = get(player_x + 18, player_y + 17)
  collide4 = get(player_x, player_y + 25)
  
  if player_x < width: # εκτός της αριστερής πλευράς της οθόνης
    collide2 = safe
  
  if player_x > width: # εκτός της δεξιάς πλευράς της οθόνης
    collide3 = safe
    
  if (collide == safe and collide2 == safe and collide3 == safe and collide4 == safe) or invun > 0:
    if lives == 0 and frame_count % 12 == 0:
      tint(200, 0, 0)
    
    image(rocket, player_x, player_y + 25, 64, 64)
    score += level
    invun -= 1
    no_tint()
    
    if invun > 0:
      stroke(220)
      fill(220, 220, 220, 60)
      ellipse(player_x, player_y + 18, 47, 47)
      
  elif lives > 0:
    lives -= 1
    invun = 50
    tint(200, 0, 0)
    image(rocket, player_x, player_y + 25, 64, 64)
    no_tint()
    score += level
  else:
    text('💥', player_x + 10, player_y + 5)
    level = 0
    

def display_score():
  global level
  
  fill(255)
  text_size(16)
  text_align(RIGHT, TOP)
  text('Σκορ', width * 0.45, 10, width * 0.5, 20)
  text(str(score), width * 0.45, 25, width * 0.5, 20)
  
  if score > 10000:
    level = 0
    print('🎉🎉 Νίκησες! 🎉🎉')

  
def display_lives():
  fill(255)
  text_size(16)
  text_align(LEFT, TOP)
  text('Ζωές', width * 0.05, 10, 30, 20)
  
  for i in range(lives):
    image(rocket, width * 0.05 + i * 25, 40, 20, 20)
  

def setup():
  # Ορισμός της κινούμενης εικόνας σου εδώ
  global rocket, rock, random_seed
  
  text_size(40)
  text_align(CENTER, TOP) # θέση γύρω από το κέντρο, επάνω
  size(400, 400)
  
  rocket = load_image('rocket.png')
  rock = load_image('moon.png')
  random_seed = randint(0, 1000000)
  
def draw():
  # Ενέργειες που πρέπει να γίνονται σε κάθε καρέ
  global score, safe, level
  safe = color(0)
  
  if level > 0:
    background(safe) 
    fill(255)
    image_mode(CENTER)
    draw_obstacles()
    draw_player()
    display_score()
    display_lives()
  
run()
