#!/bin/python3

from p5 import *
from random import randint, seed

livello = 1
punteggio = 0

def giocatore_salvo():
    global giocatore_y
    
    # Volto
    fill(200, 134, 145)
    ellipse(mouse_x, giocatore_y, 60, 60)
  
    # Occhi
    fill(178, 200, 145)
    ellipse(mouse_x - 10, giocatore_y - 10, 20, 20)
    ellipse(mouse_x + 10, giocatore_y - 10, 20, 20)
    fill(0)
    ellipse(mouse_x - 10, giocatore_y - 10, 10, 10)
    ellipse(mouse_x + 10, giocatore_y - 10, 10, 10)
    fill(255)
    ellipse(mouse_x - 12, giocatore_y - 12, 5, 5)
    ellipse(mouse_x + 12, giocatore_y - 12, 5, 5)
    
    # Bocca
    fill(0)
    ellipse(mouse_x, giocatore_y + 10, 15, 10)
    fill(200, 134, 145)
    ellipse(mouse_x, giocatore_y + 5, 10, 10)

def giocatore_eliminato():
    global giocatore_y
    
    # Volto
    fill(178, 200, 145)
    ellipse(mouse_x, giocatore_y, 60, 60)
  
    # Occhi
    fill(149, 161, 195)
    ellipse(mouse_x - 10, giocatore_y - 10, 20, 20)
    ellipse(mouse_x + 10, giocatore_y - 10, 20, 20)
    fill(0)
    ellipse(mouse_x - 10, giocatore_y - 10, 10, 10)
    ellipse(mouse_x + 10, giocatore_y - 10, 10, 10)
    fill(255)
    ellipse(mouse_x - 12, giocatore_y - 12, 5, 5)
    ellipse(mouse_x + 12, giocatore_y - 12, 5, 5)
    
    # Bocca
    fill(0)
    ellipse(mouse_x, giocatore_y + 15, 15, 10)
    fill(178, 200, 145)
    ellipse(mouse_x, giocatore_y + 20, 10, 10)
  
def disegna_giocatore():
  
    global giocatore_y, safe, punteggio, livello
    
    giocatore_y = int(height * 0.8)
    
    collisione = get(mouse_x, giocatore_y).hex
    collisione2 = get(mouse_x, giocatore_y + 30).hex
    collisione3 = get(mouse_x + 30, giocatore_y).hex
    collisione4 = get(mouse_x, giocatore_y - 30).hex
    
    if mouse_x < width: # fuori a sinistra dello schermo
        collisione2 = safe.hex
    
    if mouse_x > width:  # fuori a destra dello schermo
        collisione3 = safe.hex
      
    #print(collisione, collisione2, collisione3, collisione4)
      
    if collisione == safe.hex and collisione2 == safe.hex and collisione3 == safe.hex and collisione4 == safe.hex:
        giocatore_salvo()
        punteggio += livello
    else: #Collisione
        giocatore_eliminato()
        livello = 0
  
def disegnare_ostacoli():
    global livello
    
    seed(41143644)
    
    if frame_count & height == height - 1 and livello < 5:
        livello += 1
        print('Hai raggiunto il livello', livello)
    
    for i in range(9 + livello):
        ob_x = randint(0, width)
        ob_y = randint(0, height) + frame_count
        ob_y %= height
        text('🦠', ob_x, ob_y)

def setup():
    # Metti qui sotto il codice che verrà eseguito una sola volta
    size(400, 400)  # larghezza e altezza
    no_stroke()
    text_size(40)
    text_align(CENTER, TOP)

def draw():
    # Metti qui sotto il codice che verrà eseguito ad ogni cambio di frame
    global safe, punteggio, livello
  
    safe = Color(149, 161, 195)
  
    if livello > 0:
        background(safe)
        fill(145, 134, 126)
        text('Punteggio: ' + str(punteggio), width/2, 20)
        disegnare_ostacoli()
        disegna_giocatore()
  
# Conserva questa parte per eseguire il codice
run()
