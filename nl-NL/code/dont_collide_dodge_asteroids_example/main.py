#!/bin/python3

# Bibliotheekcode importeren
from p5 import *
from random import randint, seed

level = 1
score = 0
levens = 3
onkwetsbaar = 0

# De teken_obstakel functie komt hier
def teken_obstakels():
    global level
    
    seed(random_seed)
    
    if frame_count % height == height - 1 and level < 8:
        level += 1
        print('Je hebt level', level, 'bereikt')
      
    for i in range(6 + level):
        obstakel_x = randint(0, width)
        obstakel_y = randint(0, height) + (frame_count * level)
        obstakel_y %= height # omwikkelen
        push_matrix()
        translate(obstakel_x, obstakel_y)
        rotate(degrees(randint(1, 359)+frame_count / 1000))
        image(rots, 0, 0, randint(18,24), randint(18,24))
        pop_matrix()

    
# De teken_speler functie komt hier
def teken_speler():
    global score, level, levens, onkwetsbaar
    
    speler_y = int(height * 0.8)
    speler_x = mouse_x
    
    botsen = get(speler_x, speler_y).hex
    botsen2 = get(speler_x + 18, speler_y - 17).hex
    botsen3 = get(speler_x + 18, speler_y + 17).hex
    botsen4 = get(speler_x, speler_y + 25).hex
    
    if speler_x < width: # aan de linkerkant van het scherm
        botsen2 = veilig.hex
    
    if speler_x > width: # aan de rechterkant van het scherm
        botsen3 = veilig.hex
      
    if (botsen == veilig.hex and botsen2 == veilig.hex and botsen3 == veilig.hex and botsen4 == veilig.hex) or onkwetsbaar >0:
        if levens == 0 and frame_count % 12 == 0:
            tint(200, 0, 0)
      
        image(raket, speler_x, speler_y + 25, 64, 64)
        score += level
        onkwetsbaar -= 1
        no_tint()
      
        if onkwetsbaar > 0:
            stroke(220)
            fill(220, 220, 220, 60)
            ellipse(speler_x, speler_y + 18, 47, 47)
        
    elif levens > 1:
        levens -= 1
        onkwetsbaar = 50
        tint(200, 0, 0)
        image(raket, speler_x, speler_y + 25, 64, 64)
        no_tint()
        score += level
    else:
        text('💥', speler_x + 10, speler_y + 5)
        level = 0
    

def toon_score():
    global level
    
    fill(255)
    text_size(16)
    text_align(RIGHT, TOP)
    text('Score', width * 0.45, 10, width * 0.5, 20)
    text(str(score), width * 0.45, 25, width * 0.5, 20)
    
    if score > 10000:
        level = 0
        print('🎉🎉 Jij wint! 🎉🎉')

  
def toon_levens():
    fill(255)
    text_size(16)
    text_align(LEFT, TOP)
    text('Levens', width * 0.05, 10, 30, 20)
    
    for i in range(levens):
        image(raket, width * 0.05 + i * 25, 40, 20, 20)
  

def setup():
    # Stel hier je animatie in
    size(400, 400)
    global raket, rots, random_seed
    
    text_size(40)
    text_align(CENTER, TOP) # positie rond het midden, bovenaan
    
    raket = load_image('rocket.png')
    rots = load_image('moon.png')
    random_seed = randint(0, 1000000)
  
def draw():
    # Dingen om te doen in elk frame
    global score, veilig, level
    veilig = Color(0)
    
    if level > 0:
        background(veilig) 
        fill(255)
        image_mode(CENTER)
        teken_obstakels()
        teken_speler()
        toon_score()
        toon_levens()
  
run()
