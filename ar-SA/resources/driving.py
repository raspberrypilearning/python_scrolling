#!/bin/python3

# استيراد مكتبة الشفرات البرمجية
from p5 import *
from random import randint, seed

level = 1
score = 0

# تظهر دالة draw_obstacle هنا
def draw_obstacles():
  
  global level
  
  seed(123456789)
  
  if frame_count % width == width - 1 and level < 10:
    level += 1
    print('You reached level', level)
    
  for i in range(6 + level):
    ob_x = randint(0, width) - (frame_count * level)
    ob_y = randint(0, height) 
    ob_x %= width # wrap around
    text('💩', ob_x, ob_y)
    
# تذهب دالة draw_player هنا
def draw_player():
  
  global score, level
  
  player_x = int(width * 0.2)
  player_y = mouse_y
  
  collide = get(player_x + 50, player_y + 15)
  collide2 = get(player_x + 50, player_y - 15)
  collide3 = get(player_x, player_y + 15)
  collide4 = get(player_x, player_y - 15)
  collide5 = get(player_x - 50, player_y + 15)
  collide6 = get(player_x - 50, player_y - 15)
  
  if player_y> height - 18: # إيقاف الجزء السفلي من الشاشة
    collide = safe
    collide3 = safe
    collide5 = safe
    
  elif player_y <18: # خارج الجزء العلوي من الشاشة
    collide2 = safe
    collide4 = safe
    collide6 = safe
    
  if collide == safe and collide2 == safe and collide3 == safe and collide4 == safe:
    image(car, player_x, player_y, 100, 31)
    score += level
  else:
    text('💥', player_x, player_y)
    level = 0
    
  
def setup():
  # قم بإعداد الرسوم المتحركة الخاصة بك هنا
  global car
  
  size(400, 400)
  car = load_image('car.png')
  image_mode(CENTER)
  
  
def draw():
  # أشياء للقيام بها في كل إطار
  global score, safe, level
  safe = color(128)
  
  if level > 0:
    background(safe)
    fill(255)
    text_size(16)
    text_align(RIGHT, TOP)
    text('Score', width * 0.45, 10, width * 0.5, 20)
    text(str(score), width * 0.45, 25, width * 0.5, 20)
    text_size(20)
    text_align(CENTER, TOP) # position around the centre, top
    draw_obstacles()
    draw_player()
  
run()
