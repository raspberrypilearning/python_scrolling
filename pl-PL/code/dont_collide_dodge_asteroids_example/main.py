#!/bin/python3

# Importuj kod biblioteki
from p5 import *
from random import randint, seed

poziom = 1
wynik = 0
życia = 3
invun = 0

# Funkcja draw_przeszkoda pojawi się tutaj
def rysowanie_przeszkody():
    poziom globalny
    
    seed(random_seed)
    
    if frame_count % height == height - 1 and level < 8:
        poziom += 1
        Print('osiągnąłeś poziom', poziom)
      
    for i in range(6 + poziom):
        ob_x = randint(0, szerokość)
        ob_y = randint(0, wysokość) + (liczba_klatek * poziom)
        ob_y %= wysokość # owijanie
        push_matrix()
        translate(ob_x, ob_y)
        obróć(stopnie(randint(1, 359)+frame_count / 1000))
        image(rock, 0, randint(18,24), randint(18,24))
        pop_matrix()

    
# Funkcja draw_player pojawia się tutaj
def draw_player():
    globalny wynik, poziom, życia, invun
    
    player_y = int(wysokość * 0.8)
    player_x = mysz_x
    
    collide = get(gracz_x, gracz_y).hex
    kolizy2 = get(gracz_x - 18, gracz_y + 17).hex
    kolizy3 = get(player_x + 18, player_y + 17).hex
    collide4 = get(gracz_x, gracz_y + 25).hex
    
    if player_x < width: # off the left of the screen
        kolizy2 = safe.hex
    
    if player_x > width: # na prawo od ekranu
        kolizy3 = safe.hex
      
    if (zderzenie == safe.hex and collide2 == safe.hex and collide3 == safe.hex and collide4 == safe.hex) lub invun > 0:
        if lives == 0 and frame_count % 12 == 0:
            tint(200, 0, 0)
      
        image(rakieta, gracz_x, gracz_y + 25, 64, 64)
        wynik += poziom
        invun -= 1
        no_tint()
      
        if invun > 0:
            stroke(220)
            fill(220, 220, 220, 60)
            elipsa(gracz_x, gracz_y + 18, 47, 47)
        
    elif żyje > 1:
        życia -= 1
        invun = 50
        tint(200, 0, 0)
        image(rakieta, gracz_x, gracz_y + 25, 64, 64)
        no_tint()
        wynik += poziom
    else:
        text('?', player_x + 10, player_y + 5)
        poziom = 0
    

def display_score():
    poziom globalny
    
    fill(255)
    text_size(16)
    text_align(RIGHT, TOP)
    Tekst('Wynik', szerokość * 0.45, 10, szerokość * 0.5, 20)
    tekst(str(wynik), szerokość * 0.45, 25, szerokość * 0.5, 20)
    
    if wynik > 10000:
        poziom = 0
        print('?? Wygrasz! ??')

  
def display_lives():
    fill(255)
    text_size(16)
    text_align(LEFT, TOP)
    Tekst('życia', szerokość * 0.05, 10, 30, 20)
    
    for i in range(lives):
        obraz(rakieta, szerokość * 0.05 + i * 25, 40, 20, 20)
  

def setup():
    # Ustaw swoją animację tutaj
    size(400, 400)
    global rocket, rock, random_seed
    
    text_size(40)
    Text_align(ŚRODEK, GÓRA) # pozycja wokół środka, na górze
    
    rocket = load_image('rocket.png')
    rock = load_image('moon.png')
    random_seed = randint(0, 1000000)
  
def draw():
    # Rzeczy do zrobienia w każdej klatce
    globalny wynik, bezpieczny, poziom
    Bezpieczny = Kolor(0)
    
    if poziom > 0:
        tło(bezpieczne) 
        fill(255)
        image_mode(CENTER)
        rysowanie_przeszkody()
        draw_player()
        display_score()
        display_lives()
  
run()
