#!/bin/python3

# Importa le librerie di codice
from p5 import *
from random import randint, seed

livello = 1
punteggio = 0

# La funzione disegnare_ostacoli va qui
def disegnare_ostacoli():
    global livello
    
    seed(123456789)
    
    if frame_count % width == width - 1 and livello < 10:
        livello += 1
        print('Hai raggiunto il livello:', livello)
      
    for i in range(6 + livello):
        ob_y = randint(0, width) + (frame_count * livello)
        ob_y = randint(0, height) 
        ob_x %= width  # arrotolare
        text('💩', ob_x, ob_y)
    
# La funzione disegna_giocatore va qui
def disegna_giocatore():
    global punteggio, livello
    
    giocatore_x = int(width * 0.2)
    giocatore_y = mouse_y
    
    collisione = get(giocatore_x + 50, giocatore_y + 15).hex
    collisione2 = get(giocatore_x + 50, giocatore_y - 15).hex
    collisione3 = get(giocatore_x, giocatore_y + 15).hex
    collisione4 = get(giocatore_x, giocatore_y - 15).hex
    collisione5 = get(giocatore_x - 50, giocatore_y + 15).hex
    collisione6 = get(giocatore_x - 50, giocatore_y - 15).hex
    
    if giocatore_y > height - 18:  # Fuori dalla parte inferiore dello schermo
        collisione = safe.hex
        collisione3 = safe.hex
        collisione5 = safe.hex
      
    elif giocatore_y < 18:  # Fuori dalla parte superiore dello schermo
        collisione2 = safe.hex
        collisione4 = safe.hex
        collisione6 = safe.hex
      
    if collisione == safe.hex and collisione2 == safe.hex and collisione3 == safe.hex and collisione4 == safe.hex:
        image(auto, giocatore_x, giocatore_y, 100, 31)
        punteggio += livello
    else:
        text('💥', giocatore_x, giocatore_y)
        livello = 0


def setup():
    # Imposta la tua animazione qui
    size(400, 400)
    global auto
    auto = load_image('car.png')
    image_mode(CENTER)
  
  
def draw():
    # Cose da fare in ogni fotogramma
    global punteggio, safe, livello
    safe = Color(128)
    
    if livello > 0:
        background(safe)
        fill(255)
        text_size(16)
        text_align(RIGHT, TOP)
        text('Punteggio', width * 0.45, 10, width * 0.5, 20)
        text(str(punteggio), width * 0.45, 25, width * 0.5, 20)
        text_size(20)
        text_align(CENTER, TOP) # posizione attorno al centro, in alto
        disegnare_ostacoli()
        disegna_giocatore()
  
run()
