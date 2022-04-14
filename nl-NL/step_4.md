## Botsingsdetectie

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Eindeloze runner-games eindigen vaak wanneer de speler tegen een obstakel botst.
</div>
<div>

![Afbeelding van voltooide stap.](images/collision.png){:width="300px"}

</div>
</div>

Nu kun je je speler instellen om te reageren op een botsing met een obstakel.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">**Botsingsdetectie**</span> bepaalt wanneer twee objecten die in een computersimulatie zijn gemaakt elkaar raken, of dat nu een game is, een animatie of iets anders. Er zijn verschillende manieren om dit te doen, bijvoorbeeld: 
  - controleren of de kleuren die op de locatie van een object verschijnen de kleuren van dat object zijn, of een andere kleur
  - de vorm van elk object bijhouden en controleren of die vormen elkaar overlappen
  - een reeks grenspunten of lijnen rond een object maken en controleren of ze in contact komen met andere 'botsbare' objecten
Wanneer een dergelijke botsing wordt gedetecteerd, kan het programma op de een of andere manier reageren. In een videogame is dit meestal om schade aan te richten (als de speler in botsing komt met een vijand of gevaar) of om een voordeel te geven (als de speler in botsing komt met een power-up).
</p>

--- task ---

Maak in je `teken_speler()`-functie een variabele met de naam `botsen` en stel deze in om de kleur op de positie van de speler op te vragen.

--- code ---
---
language: python
filename: main.py - draw_player()
---

botsen = get(muis_x, speler_y)

--- /code ---

--- /task ---

--- task ---

Creëer een voorwaarde om te controleren `of` de `botsen` variabele gelijk is aan de `veilig` variabele — als dat zo is, dan raakt je speler veilig de achtergrond en is hij niet tegen een obstakel gebotst.

Verplaats je code om je speler te tekenen binnen jouw `if botsen == veilig` voorwaarde en voeg code toe aan de `else` voorwaarde om de speler te laten reageren op de botsing.

**Kies:** Hoe moet je speler reageren? Je zou:
+ De afbeelding kunnen veranderen in een `gecrashte` versie
+ Een andere emoji voor de speler gebruiken
+ Je zou `tint()` kunnen gebruiken om het uiterlijk van een afbeelding te veranderen, vergeet niet om `no_tint()` aan te roepen na het tekenen van de afbeelding

--- collapse ---
---
title: Verander de afbeelding
---

Je kunt een andere afbeelding gebruiken om je speler weer te geven wanneer deze tegen een obstakel botst.

Hier is een voorbeeld:

--- code ---
---
language: python
filename: main.py - draw_player()
---

def teken_speler(): speler_y = int(height * 0,8)

  botsen = get(muis_x, speler_y)

  if botsen == veilig: #Gelijk aan achtergrondkleur image(skien, muis_x, speler_y, 30, 30) else: #Gebotst image(gecrasht, muis_x, speler_y, 30, 30)

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Emoji-tekens gebruiken
---

Je kunt emoji-tekens in de p5-functie `text()` gebruiken om jouw gebotste speler weer te geven.

Hier is een voorbeeld:

--- code ---
---
language: python
filename: main.py - setup()
---

def setup(): size(400, 400) text_size(40) #Controleert de grootte van de emoji text_align(CENTER, TOP) #Positie rond het midden

--- /code ---

--- code ---
---
language: python
filename: main.py - draw_player()
---

def teken_speler(): if botsen == veilig: #Gelijk aan chtergrondkleur text('🎈', muis_x, speler_y) else: #Gebotst text('💥', muis_x, speler_y)

--- /code ---

--- /collapse ---

[[[processing-tint]]]

[[[generic-theory-simple-colours]]]

--- /task ---

--- task ---

**Test:** Controleer of er een botsing wordt gedetecteerd en de reactie plaatsvindt bij elke botsing.

--- /task ---

--- task ---

**Debug:** Mogelijk vindt je enkele fouten in jouw project die je moet oplossen. Hier zijn enkele veelvoorkomende fouten.

--- collapse ---
---
title: Er is geen botsing wanneer de speler een obstakel bereikt
---

Als je speler een obstakel raakt en er gebeurt niets, zijn er een paar dingen die je moet controleren:

 - Zorg ervoor dat je `teken_obstakels()` aanroept voor `teken_speler()`. Als je op botsingen controleert voordat je de obstakels in een frame tekent, zijn er geen obstakels om tegen te botsen!
 - Zorg ervoor dat je exact dezelfde kleur gebruikt bij het tekenen van het object en in de `if` functie om te controleren op de botsing. Je kunt hiervoor zorgen door op beide plaatsen dezelfde `global`-variabele te gebruiken.
 - Teken je het personage van de speler voordat je de kleur bij de muiscoördinaten controleert? Als dat zo is, krijg je alleen de kleuren van de speler. Je moet eerst de kleur controleren en **dan** de speler tekenen.
 - Heb je code in het `else`-gedeelte staan om iets anders te doen wanneer een botsing wordt gedetecteerd, zoals het aanbrengen van een kleur of het gebruik van een andere afbeelding?
 - Heb je de code voor je `if`-commando correct ingesprongen, zodat het wordt uitgevoerd wanneer aan de voorwaarde is voldaan?

Het kan handig zijn om de kleur af te drukken van de pixel waarop je controleert op een botsing:

```python
  print(red(botsen), green(botsen), blue(botsen))
```

Je kunt ook een cirkel afdrukken rond het punt dat je aan het controleren bent en dat punt aanpassen als dat nodig is:

```python
  no_fill()
  ellipse(muis_x, speler_y, 10, 10) #Teken botsingspunt
```

--- /collapse ---

--- /task ---

--- task ---

**Optioneel:** Op dit moment detecteer je alleen botsingen op één pixel op jouw speler. Je kunt ook botsingen detecteren bij andere pixels aan de rand van je speler, zoals de onderste of de linker- en rechterrand.

--- collapse ---
---
title: Botsingsdetectie met meerdere pixels
---

```python
teken_speler():
  speler_y = int(height * 0.8)
  #Nuttig voor het opsporen van fouten
  #Teken cirkels rond de pixels om te controleren op botsingen

  no_fill()
  ellipse(muis_x, speler_y, 10, 10) #Teken botsingspunt
  ellipse(muis_x, speler_y + 40, 10, 10)
  ellipse(muis_x - 12, speler_y + 20, 10, 10)
  ellips(muis_x + 12, speler_y + 20, 10, 10)

  botsen = get(muis_x, speler_y)
  botsen2 = get(muis_x - 12, speler_y + 20)
  botsen3 = get(muis_x + 12, speler_y + 20)
  botsen4 = get(muis_x, speler_y + 40)

  if muis_x < width: #Voorbij linkerkant van het scherm
    botsen2 = veilig

  if muis_x > width: #Voorbij rechterkant van het scherm
    botsen3 = veilig

  if botsen == veilig and botsen2 == veilig and botsen3 == veilig and botsen4 == veilig:
    text('🎈', muis_x, speler_y)
  else:
    text('💥', muis_x, speler_y)
```

--- /collapse ---

Je zou zelfs een lus kunnen gebruiken en veel verschillende pixels kunnen controleren. Dat is hoe botsingsdetectie werkt in games.

--- /task ---

--- save ---
