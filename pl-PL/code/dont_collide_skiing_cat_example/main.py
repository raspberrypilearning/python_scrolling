#!/bin/python3

# Importuj kod biblioteki
from p5 import *
from random import randint, seed

prędkość = 1
wynik = 0

# Funkcja draw_background pojawia się tutaj
def rysowanie_przeszkody():
    globalna prędkość
    
    seed(12345678)
    
    if frame_count % height == height - 1 and speed < 5:
        prędkość += 1
        Print('osiągnąłeś poziom', prędkość)
      
    for i in range(6):
        ob_x = randint(0, wysokość)
        ob_y = randint(0, wysokość) + (liczba_klatek * prędkość)
        ob_y %= wysokość # owijanie
        no_stroke()
        fill(0,255,0)
        trójkąt(ob_x + 20, ob_y + 20, ob_x + 10, ob_y + 40, ob_x + 30, położnictwo_y + 40)
        trójkąt(ob_x + 20, ob_y + 30, ob_x + 5, ob_y + 55, ob_x + 35, położnictwo_y + 55)
        trójkąt(ob_x + 20, ob_y + 40, ob_x + 0, ob_y + 70, ob_x + 40, położnictwo_y + 70)
        fill(150,100,100)
        rect(ob_x + 15, ob_y + 70, 10, 10)
    
# Funkcja draw_player pojawia się tutaj
def draw_player():
    globalny wynik, prędkość, jazda na nartach, rozbił się
    
    player_y = int(wysokość * 0.8)
    
    fill(bezpieczne)
  
    collide = get(mouse_x, player_y).hex
    
    if collide == safe.hex:
        image(narty, mouse_x, player_y, 30, 30)
        wynik += prędkość
    else:
        obraz(rozbity, mysz_x, gracz_y, 30, 30)
        prędkość = 0
    
  
def setup(): 
    # Ustaw swoją animację tutaj
    size(400, 400)
    text_size(40)
    Text_align(ŚRODEK, GÓRA) # pozycja wokół środka
    globalne narty, rozbił się
    narciarstwo = load_image('skiing.png')
    rozbity = load_image('fallenover.png')
  
def draw():
    # Rzeczy do zrobienia w każdej klatce
    globalny wynik, bezpieczny, prędkość, jazda na nartach, rozbił się
    Bezpieczny = Kolor(255)
  
    if prędkość > 0:
        tło(bezpieczne) 
        fill(0)
        Text('Wynik: ' + str(wynik), width/2, 20)
        rysowanie_przeszkody()
        draw_player()
  
run()
