#!/bin/python3

# Importa la libreria di codice
from p5 import *
from random import randint, seed

livello = 1
punteggio = 0

# La funzione disegnare_ostacoli va qui
def disegnare_ostacoli():
    global livello
  
    seed(12345678)
  
    if frame_count % height == height - 1 and livello < 5:
        livello += 1
        print('Hai raggiunto il livello', livello)
  
    for i in range(6 + livello):
        
        ob_y = randint(0, height) + (frame_count * livello)
        ob_y %= height  # arrotolare
        


# La funzione disegna_giocatore va qui
def disegna_giocatore():
    global punteggio, livello
  
    giocatore_y = int(height * 0.8)
  
    collisione = get(mouse_x, giocatore_y).hex
    collisione2 = get(mouse_x - 12, giocatore_y + 20).hex
    collisione3 = get(mouse_x + 12, giocatore_y + 20).hex
    collisione4 = get(mouse_x, giocatore_y + 40).hex
  
    if mouse_x < width: # fuori a sinistra dello schermo
        collisione2 = safe.hex
  
    if mouse_x > width:  # fuori a destra dello schermo
        collisione3 = safe.hex
  
    if collisione == safe.hex and collisione2 == safe.hex and collisione3 == safe.hex and collisione4 == safe.hex:
        text('🎈', mouse_x, giocatore_y)
        punteggio += livello
    else:
        text('💥', mouse_x, giocatore_y)
        livello = 0


def setup():
    # Imposta la tua animazione qui
    size(400, 400)
    text_size(40)
    text_align(CENTER, TOP) # posizione attorno al centro, in alto


def draw():
    # Cose da fare in ogni fotogramma
    global punteggio, safe, livello
    

    if livello > 0:
        
        fill(255)
        text('Punteggio: ' + str(punteggio), width/2, 20)
        disegnare_ostacoli()
        disegna_giocatore()

run()
