#!/bin/python3

# Mewngludo cod llyfrgell
from p5 import *
from random import randint, seed

lefel = 1
sgor = 0

# Mae'r swyddogaeth llunio_rhwystrau yn mynd fan hyn
def llunio_rhwystrau():
  
  global lefel
  
  seed(12345678)
  
  if frame_count % height == height - 1 and lefel < 5:
    lefel += 1
    print('Wedi cyrraedd lefel', lefel)
    
  for i in range(6 + lefel):
    rh_x = randint(0, height)
    rh_y = randint(0, height) + (frame_count * lefel)
    rh_y %= height # Amlapio
    text('🌵', rh_x, rh_y)

    
# Mae'r swyddogaeth llunio_chwaraewr yn mynd fan hyn
def llunio_chwaraewr():
  
  global sgor, lefel
  
  chwaraewr_y = int(height * 0.8)
  
  no_fill()
  #ellipse(mouse_x, chwaraewr_y, 10, 10) # Llunio pwynt gwrthdaro
  #ellipse(mouse_x, chwaraewr_y + 40, 10, 10)
  #ellipse(mouse_x - 12, chwaraewr_y + 20, 10, 10)
  #ellipse(mouse_x + 12, chwaraewr_y + 20, 10, 10)

  taro = get(mouse_x, chwaraewr_y)
  taro2 = get(mouse_x - 12, chwaraewr_y + 20)
  taro3 = get(mouse_x + 12, chwaraewr_y + 20)
  taro4 = get(mouse_x, chwaraewr_y + 40)
  
  if mouse_x < width: # Oddi ar ochr chwith y sgrin
    taro2 = diogel
  
  if mouse_x > width: # Oddi ar ochr dde'r sgrin
    taro3 = diogel
    
  if taro == diogel and taro2 == diogel and taro3 == diogel and taro4 == diogel:
    text('🎈', mouse_x, chwaraewr_y)
    sgor += lefel
  else:
    text('💥', mouse_x, chwaraewr_y)
    lefel = 0
    
  
def setup():
  # Gosodwch eich animeiddiad yma
  text_size(40)
  text_align(CENTER, TOP) # Lleoli o amgylch y canol, brig
  size(400, 400)
  
  
def draw():
  # Pethau i'w gwneud ym mhob ffrâm
  global sgor, diogel, lefel
  diogel = color(200, 150, 0)
  
  if lefel > 0:
    background(diogel) 
    fill(255)
    text('Sgor: ' + str(sgor), width/2, 20)
    llunio_rhwystrau()
    llunio_chwaraewr()
  
run()
