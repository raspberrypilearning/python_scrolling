#!/bin/python3

# Mewngludo cod llyfrgell
from p5 import *
from random import randint, seed

lefel = 1
sgor = 0

# Mae'r swyddogaeth llunio_rhwystrau yn mynd fan hyn
def llunio_rhwystrau():
  
  global lefel
  
  seed(123456789)
  
  if frame_count % width == width - 1 and lefel < 10:
    lefel += 1
    print('Wedi cyrraedd lefel', lefel)
    
  for i in range(6 + lefel):
    rh_x = randint(0, width) - (frame_count * lefel)
    rh_y = randint(0, height) 
    rh_x %= width # Amlapio
    text('💩', rh_x, rh_y)
    
# Mae'r swyddogaeth llunio_chwaraewr yn mynd fan hyn
def llunio_chwaraewr():
  
  global sgor, lefel
  
  chwaraewr_x = int(width * 0.2)
  chwaraewr_y = mouse_y
  
  taro = get(chwaraewr_x + 50, chwaraewr_y + 15)
  taro2 = get(chwaraewr_x + 50, chwaraewr_y - 15)
  taro3 = get(chwaraewr_x, chwaraewr_y + 15)
  taro4 = get(chwaraewr_x, chwaraewr_y - 15)
  taro5 = get(chwaraewr_x - 50, chwaraewr_y + 15)
  taro6 = get(chwaraewr_x - 50, chwaraewr_y - 15)
  
  if chwaraewr_y > height - 18: # Oddi ar waelod y sgrin
    taro = diogel
    taro3 = diogel
    taro5 = diogel
    
  elif chwaraewr_y < 18: # Oddi ar frig y sgrin
    taro2 = diogel
    taro4 = diogel
    taro6 = diogel
    
  if taro == diogel and taro2 == diogel and taro3 == diogel and taro4 == diogel:
    image(car, chwaraewr_x, chwaraewr_y, 100, 31)
    sgor += lefel
  else:
    text('💥', chwaraewr_x, chwaraewr_y)
    lefel = 0
    
  
def setup():
  # Gosodwch eich animeiddiad yma
  global car
  
  size(400, 400)
  car = load_image('car.png')
  image_mode(CENTER)
  
  
def draw():
  # Pethau i'w gwneud ym mhob ffrâm
  global sgor, diogel, lefel
  diogel = color(128)
  
  if lefel > 0:
    background(diogel)
    fill(255)
    text_size(16)
    text_align(RIGHT, TOP)
    text('Sgor', width * 0.45, 10, width * 0.5, 20)
    text(str(sgor), width * 0.45, 25, width * 0.5, 20)
    text_size(20)
    text_align(CENTER, TOP) # Lleoli o amgylch y canol, brig
    llunio_rhwystrau()
    llunio_chwaraewr()
  
run()
