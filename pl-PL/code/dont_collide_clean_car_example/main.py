#!/bin/python3

# Importuj kod biblioteki
from p5 import *
from random import randint, seed

poziom = 1
wynik = 0

# Funkcja draw_przeszkoda pojawi się tutaj
def rysowanie_przeszkody():
    poziom globalny
    
    seed(123456789)
    
    if frame_count % width == width - 1 and level < 10:
        poziom += 1
        Print('osiągnąłeś poziom', poziom)
      
    for i in range(6 + poziom):
        ob_x = randint(0, szerokość) - (liczba_klatek * poziom)
        ob_y = randint(0, wysokość) 
        ob_x %= szerokość # zawiń wokół
        text('?', ob_x, ob_y)
    
# Funkcja draw_player pojawia się tutaj
def draw_player():
    globalny wynik, poziom
    
    player_x = int(szerokość * 0.2)
    player_y = mysz_y
    
    collide = get(gracz_x + 50, gracz_y + 15).hex
    kolizy2 = get(gracz_x + 50, gracz_y - 15).hex
    kolizy3 = get(player_x, player_y + 15).hex
    collide4 = get(gracz_x, gracz_y - 15).hex
    collide5 = get(player_x - 50, player_y + 15).hex
    collide6 = get(gracz_x - 50, gracz_y - 15).hex
    
    IF player_y > wysokość - 18: # Off the bottom of the screen
        collide = safe.hex
        kolizy3 = safe.hex
        kolidowa5 = safe.hex
      
    elif player_y < 18: # Off the top of the screen
        kolizy2 = safe.hex
        kolizy4 = safe.hex
        kolizy6 = safe.hex
      
    if collide == safe.hex and collide2 == safe.hex and collide3 == safe.hex and collide4 == safe.hex:
        obraz(samochód, player_x, player_y, 100, 31)
        wynik += poziom
    else:
        text('?', player_x, player_y)
        poziom = 0


def setup():
    # Ustaw swoją animację tutaj
    size(400, 400)
    globalny samochód
    car = load_image('car.png')
    image_mode(CENTER)
  
  
def draw():
    # Rzeczy do zrobienia w każdej klatce
    globalny wynik, bezpieczny, poziom
    Bezpieczny = Kolor(128)
    
    if poziom > 0:
        tło(bezpieczne)
        fill(255)
        text_size(16)
        text_align(RIGHT, TOP)
        Tekst('Wynik', szerokość * 0.45, 10, szerokość * 0.5, 20)
        tekst(str(wynik), szerokość * 0.45, 25, szerokość * 0.5, 20)
        text_size(20)
        Text_align(ŚRODEK, GÓRA) # pozycja wokół środka, na górze
        rysowanie_przeszkody()
        draw_player()
  
run()
