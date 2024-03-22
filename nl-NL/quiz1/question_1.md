## Snelle quiz

Beantwoord de drie vragen. Je wordt naar het juiste antwoord geleid.

Klik na het beantwoorden van elke vraag op **Controleer mijn antwoord**.

Veel plezier!

--- question ---
---
legend: Vraag 1 van 3
---

Je hebt veel `if` commando's gebruikt om het gedrag van je spel te sturen. Sommigen van hen hadden mogelijk complexere voorwaarden, waarbij ze `and` gebruikten om meerdere tests tegelijk uit te voeren. Als je het volgende stukje voorwaardelijke code zou uitvoeren, wat zou je dan verwachten als uitvoer?

```python
score = 5000
levens = 2

if score >= 5000 and levens >= 3:
  print('Dat vliegt geweldig!')

if score >= 5000: 
  print('Je doet het goed!')
  if levens > 1:
    print('Ga door!')
  else:
    print('Maar wees voorzichtig!')

elif levens > 1:
  print('Harder werken!')

else:
  print('Ga naar de basis!')
```

--- choices ---

- ( )
```
Dat vliegt geweldig!
```
  --- feedback ---

Hoewel `score >= 5000` waar is, moeten voor een `and` voorwaarde beide delen waar zijn, en `levens >= 3` is onwaar.

  --- /feedback ---

- (x)
```
Je doet het goed!
Ga door!
```
  --- feedback ---

Dit is correct — `score >= 5000` is waar, en dat geldt ook voor `levens > 1` in de geneste `if`-conditie.

  --- /feedback ---

- ( )
```
Je doet het goed!
```
  --- feedback ---

Bijna, maar `score >= 5000` is niet de enige voorwaarde die het programma "waar" zou vinden terwijl het werd uitgevoerd.

  --- /feedback ---

- ( )
```
Harder werken!
```
  --- feedback ---

Terwijl `levens > 1` waar is, wordt alleen de code binnen de eerste ware voorwaarde in een `if`/`elif`/`else` instructie uitgevoerd, en `levens > 1` is niet de eerste voorwaarde die waar is.

  --- /feedback ---

--- /choices ---

--- /question ---
