#!/bin/python3

# Importa la libreria di codice
from p5 import *
from random import randint, seed

velocita = 1
punteggio = 0

# La funzione draw_ background va qui
def disegnare_ostacoli():
    global velocita
    
    seed(12345678)
    
    if frame_count % height == height - 1 and velocita < 5:
        velocita += 1
        print('Hai raggiunto il livello', velocita)
      
    for i in range(6):
        ob_x = randint(0, height)
        ob_y = randint(0, height) + (frame_count * velocita)
        ob_y %= height  # arrotolare
        no_stroke()
        fill(0,255,0)
        triangle(ob_x + 20, ob_y + 20, ob_x + 10, ob_y + 40, ob_x + 30, ob_y + 40)
        triangle(ob_x + 20, ob_y + 30, ob_x + 5, ob_y + 55, ob_x + 35, ob_y + 55)
        triangle(ob_x + 20, ob_y + 40, ob_x + 0, ob_y + 70, ob_x + 40, ob_y + 70)
        fill(150,100,100)
        rect(ob_x + 15, ob_y + 70, 10, 10)
    
# La funzione disegna_giocatore va qui
def disegna_giocatore():
    global punteggio, velocita, sciare, incidenti
    
    giocatore_y = int(height * 0.8)
    
    fill(safe)
  
    collisione = get(mouse_x, giocatore_y).hex
    
    if collisione == safe.hex:
        image(sciare, mouse_x, giocatore_y, 30, 30)
        punteggio += velocita
    else:
        image(incidenti, mouse_x, giocatore_y, 30, 30)
        velocita = 0
    
  
def setup(): 
    # Imposta la tua animazione qui
    size(400, 400)
    text_size(40)
    text_align(CENTER, TOP) # posizione attorno al centro
    global sciare, incidenti
    sciare = load_image('skiing.png')
    incidenti = load_image('fallenover.png')
  
def draw():
    # Cose da fare in ogni fotogramma
    global punteggio, sicurezza, velocita, sciare, incidenti
    sicurezza = Color(255)
  
    if velocita > 0:
        background(sicurezza) 
        fill(0)
        text('Punteggio: ' + str(punteggio), width/2, 20)
        disegnare_ostacoli()
        disegna_giocatore()
  
run()
