#!/bin/python3

# Importuj kod biblioteki
from p5 import *
from random import randint, seed

poziom = 1
wynik = 0

# Funkcja draw_przeszkoda pojawi się tutaj
def rysowanie_przeszkody():
    poziom globalny
  
    seed(12345678)
  
    if frame_count % height == height - 1 and level < 5:
        poziom += 1
        Print('osiągnąłeś poziom', poziom)
  
    for i in range(6 + poziom):
        ob_x = randint(0, wysokość)
        ob_y = randint(0, wysokość) + (liczba_klatek * poziom)
        ob_y %= wysokość # owijanie
        text('?', ob_x, ob_y)


# Funkcja draw_player pojawia się tutaj
def draw_player():
    globalny wynik, poziom
  
    player_y = int(wysokość * 0.8)
  
    collide = get(mouse_x, player_y).hex
    collide2 = get(mouse_x - 12, player_y + 20).hex
    kolizy3 = get(mouse_x + 12, player_y + 20).hex
    collide4 = get(mouse_x, player_y + 40).hex
  
    if mouse_x < width: # off the left of the screen
        kolizy2 = safe.hex
  
    if mouse_x > width: # off the right of the screen
        kolizy3 = safe.hex
  
    if collide == safe.hex and collide2 == safe.hex and collide3 == safe.hex and collide4 == safe.hex:
        text('?', mouse_x, player_y)
        wynik += poziom
    else:
        text('?', mouse_x, player_y)
        poziom = 0


def setup():
    # Ustaw swoją animację tutaj
    size(400, 400)
    text_size(40)
    Text_align(ŚRODEK, GÓRA) # pozycja wokół środka, na górze


def draw():
    # Rzeczy do zrobienia w każdej klatce
    globalny wynik, bezpieczny, poziom
    Bezpieczny = Kolor(200, 150, 0)

    if poziom > 0:
        tło(bezpieczne)
        fill(255)
        Text('Wynik: ' + str(wynik), width/2, 20)
        rysowanie_przeszkody()
        draw_player()

run()
