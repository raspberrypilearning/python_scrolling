## Het opzetten van het thema

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Stel het thema van je spel in en maak een spelerspersonage dat de muisaanwijzer volgt.

</div>
<div>

![Afbeelding van cartoonschildpad van bovenaf gezien tegen een blauwe achtergrond.](images/theme-turtle.png){:width="300px"}

</div>
</div>

Wat is het thema van je spel? Hier zijn enkele ideeën:
- Sport
- Hobbies
- Wetenschap
- Natuur

--- task ---

Open de [Bots niet! startproject](https://editor.raspberrypi.org/nl-NL/projects/dont-collide-starter){:target="_blank"} project. De code editor wordt geopend in een ander browsertabblad.

Als je een Raspberry Pi-account hebt, kun je op de **Save** knop klikken om een kopie op te slaan in je **Projects**.

--- /task ---

--- task ---

**Kies:** Stel de grootte van je canvas in.

--- code ---
---
language: python
filename: main.py - setup()
line_numbers: true
line_number_start: 9
line_highlights: 10
---

def setup():    
    size(400, 400)

--- /code ---

--- /task ---

--- task ---

Maak een variabele met de naam `veilig` om de achtergrondkleur op te slaan op basis van het thema dat je voor jouw spel wilt.

Dit is de kleur waarop de speler veilig kan staan en je zult deze variabele later opnieuw gebruiken.

--- code ---
---
language: python
filename: main.py - draw()
line_numbers: true
line_number_start: 13
line_highlights: 14, 15, 16
---

def draw():
    global veilig
    veilig = Color(200, 100, 0)  # Voeg de kleur van je thema toe
    background(veilig)

--- /code ---

[[[generic-theory-simple-colours]]]

--- /task ---

--- task ---

**Test:** Voer je code uit om de achtergrondkleur te zien. Verander het totdat je tevreden bent met de kleur en de grootte van het scherm.

--- /task ---

Kies nu het personage dat het spel speelt en de obstakels ontwijkt. Is het een object, persoon, dier of iets anders?

De speler verschijnt op een vaste `y` positie en dezelfde `x` positie als de muisaanwijzer, die is opgeslagen in de `p5` variabele `mouse_x`.

--- task ---

Het is een goed idee om de code voor het personage van de speler in een functie op te nemen.

Definieer een `teken_speler()` functie en creëer een `speler_y` positie voor de vaste `y` positie van de speler:

--- code ---
---
language: python
filename: main.py - draw_player()
line_numbers: true
line_number_start: 12
line_highlights: 12-14
---

def teken_speler():    
    speler_y = int(height * 0.8) # Gepositioneerd naar de onderkant van het scherm

--- /code ---

Voeg code toe aan `draw()` om `teken_speler()` voor elk frame aan te roepen.

--- code ---
---
language: python
filename: main.py - draw()
line_numbers: true
line_number_start: 15
line_highlights: 19
---

def draw():
    global veilig
    veilig = Color(200, 100, 0)  # Jouw gekozen kleur
    background(veilig)
    teken_speler()

--- /code ---

--- /task ---

Vervolgens voeg je code toe aan de functie `teken_speler()` om je vorm te tekenen. Mogelijk moet je ook `setup()` code toevoegen.

--- task ---

**Kies:** Hoe ziet je speler eruit? Je speler kan zijn:
+ Een afbeelding in het startproject
+ Een emoji 🎈 of tekst
+ Getekend met een reeks vormen

--- collapse ---
---
title: Gebruik een startafbeelding
---

Afbeeldingen die in het startproject zijn opgenomen, worden weergegeven in de lijst `Image library` (Afbeeldingenbibliotheek).

![De afbeeldingengalerij met de meegeleverde afbeeldingen.](images/starter-images.png)

Noteer de naam van de afbeelding die je wilt gebruiken.

Laad de afbeelding in de `setup()` functie

--- code ---
---
language: python
filename: main.py - setup()
line_numbers: true
line_number_start: 9
line_highlights: 11-12
---

def setup():   
    size(400, 400) 
    global speler   
    speler = load_image('turtle.png') # Laad je afbeelding

--- /code ---

Roep de `image()` aan en stel deze in als global in de `teken_speler()` functie.

--- code ---
---
language: python
filename: main.py - draw_player()
line_numbers: true
line_number_start: 14
line_highlights: 16
---

def teken_speler():
    speler_y = int(height * 0.8)  # Gepositioneerd naar de onderkant van het scherm
    image(speler, mouse_x, speler_y, 30, 30)

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Emoji-tekens gebruiken
---

Je kunt emoji-tekens gebruiken in de p5-functie `text()` om een emoji als speler te gebruiken.

Hier is een voorbeeld:

--- code ---
---
language: python
filename: main.py - setup()
line_numbers: true
line_number_start: 9
line_highlights: 11-13
---

def setup():    
    size(400, 400)     
    text_size(40) # Bepaalt de grootte van de emoji     
    text_align(CENTER, TOP) # Positie rond het midden

--- /code ---

Roep de `text()` aan en stel deze in als global in de functie `teken_speler()`.

--- code ---
---
language: python
filename: main.py - draw_player()
line_numbers: true
line_number_start: 14
line_highlights: 16-17
---

def teken_speler():     
    speler_y = int(height * 0.8)    
    text('🎈', mouse_x, speler_y)

--- /code ---

--- /collapse ---

[[[processing-python-text]]]

[[[generic-theory-simple-colours]]]

[[[processing-python-ellipse]]]

[[[processing-python-rect]]]

[[[processing-python-triangle]]]

[[[processing-tint]]]

[[[processing-stroke]]]

**Tip:** Je kunt meerdere eenvoudige vormen in dezelfde functie gebruiken om een complexere speler te maken.

--- collapse ---
---
title: Teken een speler met meerdere vormen
---

![Een gezichtsvorm gemaakt van een groene cirkel als achtergrond en twee ogen getekend uit blauwe cirkels, met zwarte cirkels erin en een glinstering binnenin die met een witte cirkel werd gemaakt.](images/face_player.png)

--- code ---
---
language: python
filename: main.py - draw_player()
---

def teken_speler():
    speler_y = int(height * 0.8)
    noStroke()
    # Gezicht
    fill(0, 200, 100)
    ellipse(mouse_x, speler_y, 60, 60)
    
    # Ogen
    fill(0, 100, 200)
    ellipse(mouse_x - 10, speler_y - 10, 20, 20)
    ellipse(mouse_x + 10, speler_y - 10, 20, 20)
    fill(0)
    ellipse(mouse_x - 10, speler_y - 10, 10, 10)
    ellipse(mouse_x + 10, speler_y - 10, 10, 10)
    fill(255)
    ellipse(mouse_x - 12, speler_y - 12, 5, 5)
    ellipse(mouse_x + 12, speler_y - 12, 5, 5)

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

**Test:** Voer je code uit en beweeg de muis om de speler te besturen.

Beweegt het zoals verwacht?

--- /task ---

**Debug:** Mogelijk vindt je enkele fouten in jouw project die je moet oplossen. Hier zijn enkele veelvoorkomende fouten.

--- task ---

--- collapse ---
---
title: Ik zie de speler niet
---

Probeer over te schakelen naar volledig scherm. Controleer ook de `x` en `y` coördinaten die je hebt gebruikt om de speler te tekenen — zorg ervoor dat ze binnen het canvas staan dat je hebt gemaakt met `size()`.

--- /collapse ---

--- collapse ---
---
title: Een afbeelding wordt niet geladen
---

Controleer eerst of de afbeelding in de `Afbeeldingenbibliotheek`staat. Controleer vervolgens de bestandsnaam heel zorgvuldig - onthoud dat hoofdletters anders zijn dan kleine letters en interpunctie is belangrijk.

--- /collapse ---

--- collapse ---
---
title: Een afbeelding heeft de verkeerde afmeting
---

Controleer de invoer die de breedte en hoogte van de afbeelding bepaalt:

```python
image(afbeelding_bestand, x_coord, y_coord, breedte, hoogte)
```

--- /collapse ---

--- collapse ---
---
title: Een emoji heeft de verkeerde afmeting
---

Als je emoji te groot of te klein is, verander je de invoer in `text_size()`.

--- /collapse ---

--- /task ---

--- save ---
