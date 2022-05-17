#!/bin/python3

from p5 import *
from random import randint, seed

lefel = 1
sgor = 0

def chwaraewr_diogel():
  
  global chwaraewr_y
  
  # Wyneb
  fill(200, 134, 145)
  ellipse(mouse_x, chwaraewr_y, 60, 60)

  # Llygaid
  fill(178, 200, 145)
  ellipse(mouse_x - 10, chwaraewr_y - 10, 20, 20)
  ellipse(mouse_x + 10, chwaraewr_y - 10, 20, 20)
  fill(0)
  ellipse(mouse_x - 10, chwaraewr_y - 10, 10, 10)
  ellipse(mouse_x + 10, chwaraewr_y - 10, 10, 10)
  fill(255)
  ellipse(mouse_x - 12, chwaraewr_y - 12, 5, 5)
  ellipse(mouse_x + 12, chwaraewr_y - 12, 5, 5)
  
  # Ceg
  fill(0)
  ellipse(mouse_x, chwaraewr_y + 10, 15, 10)
  fill(200, 134, 145)
  ellipse(mouse_x, chwaraewr_y + 5, 10, 10)

def chwaraewr_wedi_taro():
  
  global chwaraewr_y
  
  # Wyneb
  fill(178, 200, 145)
  ellipse(mouse_x, chwaraewr_y, 60, 60)

  # Llygaid
  fill(149, 161, 195)
  ellipse(mouse_x - 10, chwaraewr_y - 10, 20, 20)
  ellipse(mouse_x + 10, chwaraewr_y - 10, 20, 20)
  fill(0)
  ellipse(mouse_x - 10, chwaraewr_y - 10, 10, 10)
  ellipse(mouse_x + 10, chwaraewr_y - 10, 10, 10)
  fill(255)
  ellipse(mouse_x - 12, chwaraewr_y - 12, 5, 5)
  ellipse(mouse_x + 12, chwaraewr_y - 12, 5, 5)
  
  # Ceg
  fill(0)
  ellipse(mouse_x, chwaraewr_y + 15, 15, 10)
  fill(178, 200, 145)
  ellipse(mouse_x, chwaraewr_y + 20, 10, 10)
  
def llunio_chwaraewr():
  
  global chwaraewr_y, diogel, sgor, lefel
  
  chwaraewr_y = int(height * 0.8)
  
  taro = get(mouse_x, chwaraewr_y)
  taro2 = get(mouse_x, chwaraewr_y + 30)
  taro3 = get(mouse_x + 30, chwaraewr_y)
  taro4 = get(mouse_x, chwaraewr_y - 30)
  
  if mouse_x < width: # Oddi ar ochr chwith y sgrin
    taro2 = diogel
  
  if mouse_x > width: # Oddi ar ochr dde'r sgrin
    taro3 = diogel
    
  #print(taro, taro2, taro3, taro4)
    
  if taro == diogel and taro2 == diogel and taro3 == diogel and taro4 == diogel:
    chwaraewr_diogel()
    sgor += lefel
  else: # Wedi_taro
    chwaraewr_wedi_taro()
    lefel = 0
  
def llunio_rhwystrau():
  
  global lefel
  
  seed(41143644)
  
  if frame_count & height == height - 1 and lefel < 5:
    lefel += 1
    print('Wedi cyrraedd lefel', lefel)
  
  for i in range(9 + lefel):
    rh_x = randint(0, width)
    rh_y = randint(0, height) + frame_count
    rh_y %= height
    text('🦠', rh_x, rh_y)

def setup():
# Rhowch god i redeg unwaith yma
  size(400, 400) # Lled ac uchder
  noStroke()
  text_size(40)
  text_align(CENTER, TOP)

def draw():
# Rhowch god i redeg ym mhob ffrâm yma
  global diogel, sgor, lefel
  
  diogel = color(149, 161, 195)
  
  if lefel > 0:
    background(diogel)
    fill(145, 134, 126)
    text('Sgor: ' + str(sgor), width/2, 20)
    llunio_rhwystrau()
    llunio_chwaraewr()
  
# Cadwch hwn i redeg eich cod
run()
