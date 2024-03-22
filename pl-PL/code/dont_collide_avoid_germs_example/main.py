#!/bin/python3

from p5 import *
from random import randint, seed

poziom = 1
wynik = 0

def safe_player():
    global player_y
    
    # Ściana
    fill(200, 134, 145)
    elipsa(mysz_x, gracz_y, 60, 60)
  
    # Oczy
    fill(178, 200, 145)
    elipsa(mysz_x - 10, gracz_y - 10, 20, 20)
    elipsa(mysz_x + 10, gracz_y - 10, 20, 20)
    fill(0)
    elipsa(mysz_x - 10, gracz_y - 10, 10, 10)
    elipsa(mysz_x + 10, gracz_y - 10, 10, 10)
    fill(255)
    elipsa(mysz_x - 12, gracz_y - 12, 5, 5)
    elipsa(mysz_x + 12, gracz_y - 12, 5, 5)
    
    # Usta
    fill(0)
    elipsa(mysz_x, gracz_y + 10, 15, 10)
    fill(200, 134, 145)
    elipsa(mysz_x, gracz_y + 5, 10, 10)

def rozbity_gracz():
    global player_y
    
    # Ściana
    fill(178, 200, 145)
    elipsa(mysz_x, gracz_y, 60, 60)
  
    # Oczy
    fill(149, 161, 195)
    elipsa(mysz_x - 10, gracz_y - 10, 20, 20)
    elipsa(mysz_x + 10, gracz_y - 10, 20, 20)
    fill(0)
    elipsa(mysz_x - 10, gracz_y - 10, 10, 10)
    elipsa(mysz_x + 10, gracz_y - 10, 10, 10)
    fill(255)
    elipsa(mysz_x - 12, gracz_y - 12, 5, 5)
    elipsa(mysz_x + 12, gracz_y - 12, 5, 5)
    
    # Usta
    fill(0)
    elipsa(mysz_x, gracz_y + 15, 15, 10)
    fill(178, 200, 145)
    elipsa(mysz_x, gracz_y + 20, 10, 10)
  
def draw_player():
  
    global player_y, safe, score, level
    
    player_y = int(wysokość * 0.8)
    
    collide = get(mouse_x, player_y).hex
    collide2 = get(mouse_x, player_y + 30).hex
    kolizy3 = get(mouse_x + 30, player_y).hex
    collide4 = get(mouse_x, player_y - 30).hex
    
    if mouse_x < width: # off the left of the screen
        kolizy2 = safe.hex
    
    if mouse_x > width: # off the right of the screen
        kolizy3 = safe.hex
      
    #print(zderzenie, kolidowa2, kolidowa3, kolidowa4)
      
    if collide == safe.hex and collide2 == safe.hex and collide3 == safe.hex and collide4 == safe.hex:
        safe_player()
        wynik += poziom
    Inne: # Zderzenie
        crashed_player()
        poziom = 0
  
def rysowanie_przeszkody():
    poziom globalny
    
    seed(41143644)
    
    if frame_count & height == wysokość - 1 i poziom < 5:
        poziom += 1
        Print('osiągnąłeś poziom', poziom)
    
    for i in range(9 + poziom):
        ob_x = randint(0, szerokość)
        ob_y = randint(0, height) + frame_count
        ob_y %= wysokość
        text('?', ob_x, ob_y)

def setup():
    # Wstaw kod, aby uruchomić go raz tutaj
    rozmiar(400, 400) # szerokość i wysokość
    no_stroke()
    text_size(40)
    text_align(CENTER, TOP)

def draw():
    # Wstaw kod, aby uruchomić każdą klatkę tutaj
    global safe, wynik, poziom
  
    Bezpieczny = Kolor(149, 161, 195)
  
    if poziom > 0:
        tło(bezpieczne)
        fill(145, 134, 126)
        Text('Wynik: ' + str(wynik), width/2, 20)
        rysowanie_przeszkody()
        draw_player()
  
# Zatrzymaj to, aby uruchomić swój kod
run()
