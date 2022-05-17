#!/bin/python3

# Mewngludo cod llyfrgell
from p5 import *
from random import randint, seed

lefel = 1
sgor = 0
bywydau = 3
anorchfygol = 0

# Mae'r swyddogaeth llunio_rhwystrau yn mynd fan hyn
def llunio_rhwystrau():
  
  global lefel
  
  seed(random_seed)
  
  if frame_count % height == height - 1 and lefel < 8:
    lefel += 1
    print('Wedi cyrraedd lefel', lefel)
    
  for i in range(6 + lefel):
    rh_x = randint(0, width)
    rh_y = randint(0, height) + (frame_count * lefel)
    rh_y %= height # Amlapio
    push_matrix()
    translate(rh_x, rh_y)
    rotate(degrees(randint(1, 359)+frame_count / 1000))
    image(craig, 0, 0, randint(18,24), randint(18,24))
    pop_matrix()

    
# Mae'r swyddogaeth llunio_chwaraewr yn mynd fan hyn
def llunio_chwaraewr():
  
  global sgor, lefel, bywydau, anorchfygol
  
  chwaraewr_y = int(height * 0.8)
  chwaraewr_x = mouse_x
  
  taro = get(chwaraewr_x, chwaraewr_y)
  taro2 = get(chwaraewr_x - 18, chwaraewr_y + 17)
  taro3 = get(chwaraewr_x + 18, chwaraewr_y + 17)
  taro4 = get(chwaraewr_x, chwaraewr_y + 25)
  
  if chwaraewr_x < width: # Oddi ar ochr chwith y sgrin
    taro2 = diogel
  
  if chwaraewr_x > width: # Oddi ar ochr dde'r sgrin
    taro3 = diogel
    
  if (taro == diogel and taro2 == diogel and taro3 == diogel and taro4 == diogel) or anorchfygol > 0:
    if bywydau == 0 and frame_count % 12 == 0:
      tint(200, 0, 0)
    
    image(roced, chwaraewr_x, chwaraewr_y + 25, 64, 64)
    sgor += lefel
    anorchfygol -= 1
    no_tint()
    
    if anorchfygol > 0:
      stroke(220)
      fill(220, 220, 220, 60)
      ellipse(chwaraewr_x, chwaraewr_y + 18, 47, 47)
      
  elif bywydau > 0:
    bywydau -= 1
    anorchfygol = 50
    tint(200, 0, 0)
    image(roced, chwaraewr_x, chwaraewr_y + 25, 64, 64)
    no_tint()
    sgor += lefel
  else:
    text('💥', chwaraewr_x + 10, chwaraewr_y + 5)
    lefel = 0
    

def dangos_sgor():
  global lefel
  
  fill(255)
  text_size(16)
  text_align(RIGHT, TOP)
  text('Sgor', width * 0.45, 10, width * 0.5, 20)
  text(str(sgor), width * 0.45, 25, width * 0.5, 20)
  
  if sgor > 10000:
    lefel = 0
    print('🎉🎉 Wedi ennill! 🎉🎉')

  
def dangos_bywydau():
  fill(255)
  text_size(16)
  text_align(LEFT, TOP)
  text('Bywydau', width * 0.05, 10, 60, 20)
  
  for i in range(bywydau):
    image(roced, width * 0.05 + i * 25, 40, 20, 20)
  

def setup():
  # Gosodwch eich animeiddiad yma
  global roced, craig, random_seed
  
  text_size(40)
  text_align(CENTER, TOP) # Lleoli o amgylch y canol, brig
  size(400, 400)
  
  roced = load_image('rocket.png')
  craig = load_image('moon.png')
  random_seed = randint(0, 1000000)
  
def draw():
  # Pethau i'w gwneud ym mhob ffrâm
  global sgor, diogel, lefel
  diogel = color(0)
  
  if lefel > 0:
    background(diogel) 
    fill(255)
    image_mode(CENTER)
    llunio_rhwystrau()
    llunio_chwaraewr()
    dangos_sgor()
    dangos_bywydau()
  
run()
