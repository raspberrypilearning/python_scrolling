## Versnellen!

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
De meeste eindeloze runner-games verhogen de moeilijkheidsgraad van het spel naarmate de speler vordert en geven een score.
</div>
<div>

![Voorbeeldproject met tekstscore op het scherm.](images/score.png){:width="300px"}

</div>
</div>

### Moeilijkheidsgraden toevoegen

Door duidelijke moeilijkheidsgraden te creëren, wordt het voor je speler gemakkelijker om te begrijpen wat er gebeurt.

--- task ---

Maak een `global` `level` variabele om het niveau van de speler bij te houden. Stel het in op `1` zodat spelers een nieuw spel beginnen op het eerste niveau.

--- code ---
---
language: python filename: main.py
line_numbers: false
---

# Voeg hier global variabelen toe
level = 1

--- /code ---

--- /task ---

--- task ---

Deze code gebruikt de `height` en de `frame_count` om de variabele `level` te verhogen elke keer als de speler een scherm voltooit, en drukt vervolgens het nieuwe niveau voor de speler af.

**Kies:** Deze code beperkt de niveaus tot vijf, dus het wordt niet al te moeilijk om te spelen. Er is geen reden waarom je spel er vijf moet gebruiken, maar je moet wel een limiet kiezen. Mensen kunnen beperkt snel bewegen!

--- code ---
---
language: python filename: main.py — draw_obstacles()
line_numbers: false
---

def teken_obstakels():

  global level #Gebruik het global level

  if frame_count % height == height - 1 and level < 5: level += 1 print('Je hebt level', level, 'bereikt')

--- /code ---

--- /task ---

--- task ---


De twee belangrijkste opties voor het verhogen van de moeilijkheidsgraad zijn om het spel sneller te laten gaan en om het aantal obstakels te vergroten.

--- collapse ---
---
title: Versnel je spel
---

De snelheid van het spel wordt bepaald door hoe snel obstakels naar de speler lijken te bewegen. Deze code versnelt dit door `frame_count * level` toe te voegen aan de `y` coördinaat tijdens het genereren van obstakels.

In plaats van je obstakels met één pixel in elk frame te verplaatsen, verplaatst deze code deze in plaats daarvan met het `level` aantal pixels.

Als je naar de code kijkt, zou je kunnen verwachten dat de snelheid met meer dan het `level` aantal pixels zal toenemen. Bijvoorbeeld, op het punt net voordat je `level` toeneemt, is de `frame_count` `799` — aangezien het `level` één frame toeneemt voordat de `frame_count` een even veelvoud is van de `height` (ingesteld op `400` pixels) — en `799 * 3` is aanzienlijk groter dan `799 * 2`. De extra pixels die worden gecreëerd door het geheel van `frame_count` te vermenigvuldigen met een groter getal, worden echter verborgen door `obstakel_y %= height`. Hierdoor resteert alleen het `level` aantal extra pixels in elke stap.


--- code ---
---
language: python filename: main.py — draw_obstacles()
line_numbers: false
---

  for i in range(6): obstakel_x = randint(0, height) obstakel_y = randint(0, height) + (frame_count * level) obstakel_y %= height #Omwentelen text('🌵', obstakel_x, obstakel_y)

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Meer obstakels toevoegen
---

Het toevoegen van extra obstakels is gewoon een kwestie van het aantal keren verhogen van de `for` lus die ze creëert. Je kunt dit doen door het getal dat je doorgeeft aan de functie `range()` te verhogen met `level`.

**Tip:** Natuurlijk kun je altijd `level * 2`gebruiken, of zelfs grotere veelvouden, als je je spel moeilijker wilt maken.

--- /collapse ---

--- /task ---

### Score bijhouden

Hoe langer een speler het volhoudt zonder tegen een obstakel te botsen, hoe beter hij jouw spel speelt. Door een score toe te voegen, kunnen ze zien hoe goed ze het doen.

--- task ---

Maak een global `score`-variabele om de score van de speler bij te houden. Stel het in op `0` zodat spelers een nieuw spel beginnen zonder punten.

--- code ---
---
language: python filename: main.py
line_numbers: false
---

# Voeg hier global variabelen toe
score = 0

--- /code ---

--- /task ---

--- task ---

Je kunt de score van je speler verhogen voor elk frame waar ze niet tegen een obstakel zijn gebotst door hun score te verhogen wanneer je controleert op een botsing in `teken_speler()`.

**Kies:** Je kunt beslissen hoeveel punten elk frame waard is, maar het verhogen van de score van de speler met `level` beloont spelers die kunnen overleven op hogere moeilijkheidsgraden.

--- code ---
---
language: python
filename: main.py — draw_player()
---

global score

  if botsen == veilig: text('🎈', muis_x, speler_y) score += level else: text('💥', muis_x, speler_y)

--- /code ---

--- /task ---

--- task ---

Spelers moeten hun score kunnen zien. Omdat het zo snel toeneemt, zou het gebruik van `print()` niet erg goed werken. Gebruik de p5-functie `text()` in je `draw()`-functie om deze in plaats daarvan als tekst op het spelscherm weer te geven.

[[[processing-python-text]]]

Je kunt de operator `+` gebruiken om twee of meer tekenreeksen te combineren als je een koptekst wilt geven zoals 'score' of 'punten'. Omdat `score` een getal is, moet je het naar een tekenreeks converteren voordat je het kunt samenvoegen met een andere tekenreeks. Je kunt dit doen met `str()`:

`boodschap = 'Score: ' + str(score)`

**Tip:** `str()` is een afkorting voor 'string' — programmeurs verwijderen vaak letters op deze manier, zodat ze niet zoveel hoeven te typen!

--- /task ---

### Game over!

Wanneer een speler tegen een obstakel is gebotst, moet het spel stoppen met bewegen en zou de score niet meer moeten toenemen.

--- task ---

Je kunt de `level`-variabele gebruiken om 'Game over' te signaleren door deze op 0 in te stellen — een waarde die hij op geen enkele andere manier zal bereiken. Doe dit in de stap `else` van je botsingsdetectie code.

--- /task ---

--- task ---

Maak een `if` statement in `draw()` dat test of `level > 0` voordat een van de functies — zoals `background()`, `teken_obstakels()`, en `teken_speler()` wordt aangeroepen — die het spel updaten. Omdat deze functies niet worden aangeroepen, lijkt het hele spel te eindigen, ook al draait je programma nog.

--- /task ---

--- task ---

**Debug:** Mogelijk vindt je enkele fouten in jouw project die je moet oplossen. Hier zijn enkele veelvoorkomende fouten.

--- collapse ---
---
title: De score wordt niet weergegeven
---

Zorg ervoor dat je de functie `text()` hebt opgenomen die de score van de speler op het juiste punt tekent in je functie `draw()`, en dat je deze de juiste waarden hebt doorgegeven:

`text('Te tonen tekst', x, y)`

Het zou er ongeveer zo uit moeten zien:

--- code ---
---
language: python
filename: main.py — draw()
---

  if level > 0: background(veilig) fill(255) text('Score: ' + str(score), width/2, 20) teken_obstakels() teken_speler()

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Het spel stopt niet na een botsing
---

Als je denkt dat je game botsingen totaal niet correct detecteert, probeer dan eerst de foutopsporingsinstructies in de vorige stap, onder 'Er is geen botsing wanneer de speler een obstakel bereikt'.


Als je spel botsingen correct detecteert, controleer dan of je de code binnen het `if level > 0` statement correct is ingesprongen, om er zeker van te zijn dat het alleen wordt uitgevoerd als dat statement waar is. Bijvoorbeeld:

--- code ---
---
language: python
filename: main.py — draw()
---

  if level > 0: background(veilig) fill(255) text('Score: ' + str(score), width/2, 20) teken_obstakels() teken_speler()

--- /code ---

Ten slotte, als beide correct werken, is het mogelijk dat je spel de `level = 0` niet correct instelt wanneer er een botsing plaatsvindt. Bijvoorbeeld:

--- code ---
---
language: python
filename: main.py — draw_player()
---

  if botsen == veilig: text('🎈', muis_x, speler_y) score += level else: text('💥', muis_x, speler_y) level = 0

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Het spel gaat niet sneller
---

Controleer eerst of `level` correct opgehoogd wordt. Je zou een bericht moeten zien worden afgedrukt elke keer dat het omhoog gaat. Als dit niet gebeurt, controleer dan zowel de code voor het afdrukken van het bericht als de code voor het verhogen van het level.

Als het level correct stijgt, controleer dan je `teken_obstakels()` functie. Controleer in het bijzonder of je `obstakel_y = randint(0, height) + (frame_count * level)` goed hebt. Het zou er ongeveer zo uit moeten zien:

--- code ---
---
language: python filename: main.py — draw_obstacles()
line_numbers: false
---

  for i in range(6 + level): obstakel_x = randint(0, height) obstakel_y = randint(0, height) + (frame_count * level) obstaklel_y %= height #Omkeren text('🌵', obstakel_x, obstakel_y)

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Nieuwe obstakels verschijnen niet
---

Er zijn een paar redenen waarom dit kan gebeuren. En er zijn nog enkele redenen waarom het lijkt te gebeuren, terwijl dat niet zo is. Ten eerste, omdat er nieuwe obstakels worden toegevoegd op basis van `level`, moet je controleren of `level` correct toeneemt. Je zou een bericht moeten zien worden afgedrukt elke keer dat het omhoog gaat. Als dit niet gebeurt, controleer dan zowel de code voor het afdrukken van het bericht als de code voor het verhogen van het level.

Als het niveau correct stijgt, controleer dan je functie `teken_obstakels()` om er zeker van te zijn dat je `level` gebruikt in de `range()`-functie van de `for`-lus die de obstakels tekent. Het zou er ongeveer zo uit moeten zien:

--- code ---
---
language: python filename: main.py — draw_obstacles()
line_numbers: false
---

  for i in range(6 + level): obstakel_x = randint(0, height) obstakel_y = randint(0, height) + (frame_count * level) obstakel_y %= height #Omkeren text('🌵', obstakel_x, obstakel_y)

--- /code ---

Als je al deze controles hebt gedaan en het lijkt er nog steeds niet op dat het aantal obstakels toeneemt, is het mogelijk dat dat wel zo is, maar dat je ze niet ziet. Je moet enkele van deze stappen proberen om dit te testen:
  - Vertraag het spel door `frame_rate()` te gebruiken in je `setup()` functie om je meer tijd te geven om te tellen
  - Verander de seed die je gebruikt voor je willekeurige getallen. Het is onwaarschijnlijk, maar het is mogelijk dat sommige obstakels willekeurig direct boven elkaar verschijnen
  - Voeg een `print()` toe aan de `for`-lus in `teken_obstakels()` die de waarde van `i` in elke passage van de lus afdrukt, zodat je kunt controleren of deze het juiste aantal keren wordt uitgevoerd
  - Verander, alleen voor testdoeleinden, `range(6 + level)` in `range(6 * level)` - die toename moet gemakkelijker te herkennen zijn!


--- /collapse ---

--- /task ---

--- save ---
