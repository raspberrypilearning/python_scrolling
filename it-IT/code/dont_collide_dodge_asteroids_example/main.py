#!/bin/python3

# Importa la libreria di codice
from p5 import *
from random import randint, seed

livello = 1
punteggio = 0
vite = 3


# La funzione draw_obstacle va qui
def disegnare_ostacoli():
    global livello
    
    seed(random_seed)
    
    if frame_count % height == height - 1 and livello < 8:
        livello += 1
        print('Hai raggiunto il livello', livello)
      
    for i in range(6 + livello):
        ob_x = randint(0, width)
        ob_y = randint(0, height) + (frame_count * livello)
        ob_y %= height  # arrotolare
        push_matrix()
        translate(ob_x, ob_y)
        rotate(degrees(randint(1, 359)+frame_count / 1000))
        image(rock, 0, 0, randint(18,24), randint(18,24))
        pop_matrix()

    
# La funzione disegna_giocatore va qui
def disegna_giocatore():
    global punteggio, livello, vite, invun
    
    giocatore_y = int(height * 0.8)
    giocatore_x = mouse_x
    
    collisione = get(giocatore_x, giocatore_y).hex
    collisione2 = get(giocatore_x - 18, giocatore_y + 17).hex
    collisione3 = get(giocatore_x + 18, giocatore_y + 17).hex
    collide4 = get(giocatore_x, giocatore_y + 25).hex
    
    if giocatore_x < width:  # fuori a sinistra dello schermo
        collisione2 = safe.hex
    
    if giocatore_x > width:  # fuori a destra dello schermo
        collisione3 = safe.hex
      
    if (collisione == safe.hex and collisione2 == safe.hex and collisione3 == safe.hex and collisione4 == safe.hex) or invun > 0:
        if vite == 0 and frame_count % 12 == 0:
            tint(200, 0, 0)
      
        image(rocket, giocatore_x, giocatore_y + 25, 64, 64)
        punteggio += livello
        invun -= 1
        no_tint()
      
        if invun > 0:
            stroke(220)
            fill(220, 220, 220, 60)
            ellipse(giocatore_x, giocatore_y + 18, 47, 47)
        
    elif vite > 1:
        vite -= 1
        invun = 50
        tint(200, 0, 0)
        image(rocket, giocatore_x, giocatore_y + 25, 64, 64)
        no_tint()
        punteggio += livello
    else:
        text('💥', giocatore_x + 10, giocatore_y + 5)
        livello = 0
    

def mostra_punteggio():
    global livello
    
    fill(255)
    text_size(16)
    text_align(RIGHT, TOP)
    text('Punteggio', width * 0.45, 10, width * 0.5, 20)
    text(str(punteggio), width * 0.45, 25, width * 0.5, 20)
    
    if punteggio > 10000:
        livello = 0
        print('🎉🎉 Hai vinto! 🎉🎉')

  
def mostra_vite():
    fill(255)
    text_size(16)
    text_align(LEFT, TOP)
    text('Vite', width * 0.05, 10, 30, 20)
    
    for i in range(vite):
        
  

def setup():
    # Imposta la tua animazione qui
    size(400, 400)
    global rocket, rock, random_seed
    
    text_size(40)
    text_align(CENTER, TOP) # posizione attorno al centro, in alto
    
    rocket = load_image('rocket.png')
    rock = load_image('moon.png')
    random_seed = randint(0, 1000000)
  
def draw():
    # Cose da fare in ogni fotogramma
    global punteggio, safe, livello
    safe = Color(0)
    
    if livello > 0:
        background(safe) 
        fill(255)
        image_mode(CENTER)
        disegnare_ostacoli()
        disegna_giocatore()
        mostra_punteggio()
        mostra_vite()
  
run()
