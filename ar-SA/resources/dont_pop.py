#!/bin/python3

# استيراد مكتبة الشفرات البرمجية
from p5 import *
from random import randint, seed

level = 1
score = 0

# تظهر دالة draw_obstacle هنا
def draw_obstacles ():
  
  المستوى العالمي
  
  seed(12345678)

  
  if frame_count % height == height - 1 and level < 5:
    level += 1
    print('You reached level', level)
    
  for i in range(6 + level):
    ob_x = randint(0, height)
    ob_y = randint(0, height) + (frame_count * level)
    ob_y %= height # wrap around
    text('🌵', ob_x, ob_y)

    
# تذهب دالة draw_player هنا
def draw_player():
  
  global score, level
  
  player_y = int(height * 0.8)
  
  no_fill()
  #ellipse (mouse_x، player_y، 10، 10) # رسم نقطة الاصطدام
  #ellipse(mouse_x, player_y + 40, 10, 10)
  #ellipse(mouse_x - 12, player_y + 20, 10, 10)
  #ellipse(mouse_x + 12, player_y + 20, 10, 10)

  collide = get(mouse_x, player_y)
  collide2 = get(mouse_x - 12, player_y + 20)
  collide3 = get(mouse_x + 12, player_y + 20)
  collide4 = get(mouse_x, player_y + 40)
  
  if mouse_x <العرض: # من يسار الشاشة
    collide2 = safe
  
  if mouse_x> width: # من يمين الشاشة
    collide3 = safe
    
  if collide == safe and collide2 == safe and collide3 == safe and collide4 == safe:
    text('🎈', mouse_x, player_y)
    score += level
  else:
    text('💥', mouse_x, player_y)
    level = 0
    
  
def setup():
  # قم بإعداد الرسوم المتحركة الخاصة بك هنا
  text_size(40)
  text_align (CENTER ، TOP) # موضع حول المركز ، أعلى
  size(400, 400)
  
  
def draw():
  # أشياء للقيام بها في كل إطار
  global score, safe, level
  safe = color(200, 150, 0)
  
  if level > 0:
    background(safe) 
    fill(255)
    text('Score: ' + str(score), width/2, 20)
    draw_obstacles()
    draw_player()
  
run()
