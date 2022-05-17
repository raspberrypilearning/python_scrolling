#!/bin/python3

# Mewngludo cod llyfrgell
from p5 import *
from random import randint, seed

cyflymder = 1
sgor = 0

# Mae'r swyddogaeth llunio_rhwystrau yn mynd fan hyn
def llunio_rhwystrau():
  
  global cyflymder
  
  seed(12345678)
  
  if frame_count % height == height - 1 and cyflymder < 5:
    cyflymder += 1
    print('Wedi cyrraedd cyflymder', cyflymder)
    
  for i in range(6):
    rh_x = randint(0, height)
    rh_y = randint(0, height) + (frame_count * cyflymder)
    rh_y %= height # Amlapio
    no_stroke()
    fill(0,255,0)
    triangle(rh_x + 20, rh_y + 20, rh_x + 10, rh_y + 40, rh_x + 30, rh_y + 40)
    triangle(rh_x + 20, rh_y + 30, rh_x + 5, rh_y + 55, rh_x + 35, rh_y + 55)
    triangle(rh_x + 20, rh_y + 40, rh_x + 0, rh_y + 70, rh_x + 40, rh_y + 70)
    fill(150,100,100)
    rect(rh_x + 15, rh_y + 70, 10, 10)
    
# Mae'r swyddogaeth llunio_chwaraewr yn mynd fan hyn
def llunio_chwaraewr():
  
  global sgor, cyflymder, sgio, wedi_taro
  
  chwaraewr_y = int(height * 0.8)
  
  fill(diogel)

  taro = get(mouse_x, chwaraewr_y)
  
  if taro == diogel:
    image(sgio, mouse_x, chwaraewr_y, 30, 30)
    sgor += cyflymder
  else:
    image(wedi_taro, mouse_x, chwaraewr_y, 30, 30)
    cyflymder = 0
    
  
def setup():
  
  global sgio, wedi_taro
  
  # Gosodwch eich animeiddiad yma
  text_size(40)
  text_align(CENTER, TOP) # Lleoli o amgylch y canol
  size(400, 400)
  sgio = load_image('skiing.png')
  wedi_taro = load_image('fallenover.png')
  
def draw():
  # Pethau i'w gwneud ym mhob ffrâm
  global sgor, diogel, cyflymder, sgio, wedi_taro
  diogel = color(255)

  if cyflymder > 0:
    background(diogel) 
    fill(0)
    text('Sgor: ' + str(sgor), width/2, 20)
    llunio_rhwystrau()
    llunio_chwaraewr()
  
run()
