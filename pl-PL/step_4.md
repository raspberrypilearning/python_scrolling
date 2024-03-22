## Wykrywanie kolizji

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Niekończące się gry biegaczy często kończą się, gdy gracz zderzy się z przeszkodą.
</div>
<div>

![Obraz ukończonego kroku.](images/collision.png){:width="300px"}

</div>
</div>

Teraz możesz skonfigurować gracza tak, aby reagował na kolizję z przeszkodami.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">**Wykrywanie kolizji**</span> określa, kiedy dwa obiekty utworzone wewnątrz symulacji komputerowej — czy to gra, animacja, czy coś innego — stykają się. Istnieje kilka sposobów, aby to zrobić, na przykład:
- Sprawdzanie, czy kolory pojawiające się w miejscu obiektu są kolorami tego obiektu
, czy innym - śledzenie kształtu każdego obiektu, i sprawdzanie, czy te kształty nakładają się na siebie
- tworzenie zestawu punktów granicznych lub linii wokół obiektu i sprawdzanie, czy wchodzą w kontakt z innymi "
kolidującymi" obiektami, gdy taka kolizja zostanie wykryta, program może zareagować w jakiś sposób. W grze wideo zwykle ma to na celu zadawanie obrażeń (jeśli gracz zderzy się z wrogiem lub zagrożeniem) lub dawanie korzyści (jeśli gracz zderzy się z zasilaniem).
</p>

--- task ---

W funkcji ` draw_player()` utwórz zmienną o nazwie ` ` i ustaw ją tak, aby uzyskać wartość koloru szesnastkowego (heksadecymalnego) w pozycji gracza.

--- code ---
---
language: python
filename: main.py - draw_player()
---

    collide = get(mouse_x, player_y).hex

--- /code ---

--- /task ---

--- task ---

Utwórz warunek, aby sprawdzić ` ` Zmienna ` ` jest taka sama jak zmienna ` ` — jeśli tak, to Twój gracz bezpiecznie dotyka tła i nie zderzył się z żadną przeszkodą.

Przenieś swój kod, aby narysować gracza wewnątrz swojego ` jeśli zderzenie == warunek ` i dodaj kod w instrukcji ` `, aby gracz zareagował na kolizję.

** Wybierz:** jak powinien zareagować Twój gracz? Możesz:
+ Użyj innego emoji dla gracza
+ Możesz użyć ` tint()`, aby zmienić wygląd obrazu, nie zapomnij zadzwonić do ` no_tint()` po narysowaniu obrazu

--- collapse ---
---
Title: Użyj znaków emoji
---

Możesz użyć znaków emoji w funkcji p5 ` text()`, aby reprezentować swojego zderzonego gracza.

Oto przykład:

--- code ---
---
language: python
filename: main.py - setup()
---

def setup(): size(400, 400) text_size(40)  # Controls the size of the emoji text_align(CENTER, TOP)  # Position around the centre

--- /code ---

--- code ---
---
language: python
filename: main.py - draw_player()
---

def draw_player(): if collide == safe.hex:  # On background text('🎈', mouse_x, player_y) else:  # Collided text('💥', mouse_x, player_y)

--- /code ---

--- /collapse ---

[[[processing-tint]]]

[[[generic-theory-simple-colours]]]

--- /task ---

--- task ---

Test **:** Sprawdź, czy kolizja została wykryta i reakcja ma miejsce za każdym razem, gdy wystąpi kolizja.

--- /task ---

--- task ---

** Debug:** Możesz znaleźć kilka błędów w swoim projekcie, które musisz naprawić. Oto kilka typowych robaków.

--- collapse ---
---
Title: Nie ma kolizji, gdy gracz dotrze do przeszkody
---

Jeśli Twoja postać gracza dotknie przeszkody i nic się nie stanie, musisz sprawdzić kilka rzeczy:

 - Upewnij się, że wywołasz ` draw_obstancts()` przed ` draw_player()`. Jeśli przed rysowaniem przeszkód w ramce sprawdzisz, czy nie ma żadnych przeszkód, z którymi można się zderzyć!
 - Upewnij się, że używasz dokładnie tego samego koloru podczas rysowania obiektu i w instrukcji ` ` sprawdzając obecność kolizji. Możesz to zrobić, używając tej samej zmiennej ` global ` w obu miejscach.
 - Czy rysujesz postać gracza przed sprawdzeniem koloru za pomocą współrzędnych myszy? Jeśli tak, to zawsze będziesz otrzymywać kolory od gracza. Musisz najpierw sprawdzić kolor, a następnie **, a następnie ** narysuj gracza.
 - Czy masz kod w części ` `, aby zrobić coś innego po wykryciu kolizji, na przykład zastosowanie odcienia lub użycie emoji?
 - Czy poprawnie wcięłeś kod instrukcji ` `, aby działał, gdy warunek jest spełniony?

Drukowanie koloru sprawdzanego piksela pod kątem kolizji może być przydatne:

```python
    print(red(collide), green(collide), blue(collide))
```

Możesz również wydrukować okrąg wokół sprawdzanego punktu i dostosować sprawdzany punkt, jeśli musisz:

```python
    no_fill()
    ellipse(mouse_x, player_y, 10, 10)  # Draw collision point
```

--- /collapse ---

--- /task ---

--- task ---

** Opcjonalnie:** w tej chwili wykrywasz tylko kolizje o jednym pikselu na swoim odtwarzaczu. Możesz również wykryć kolizje w innych pikselach na krawędzi odtwarzacza, takich jak dolna lub lewa i prawa krawędź.

--- collapse ---
---
Title: Wykrywanie kolizji z wieloma pikselami
---

```python
def draw_player():

    player_y = int(height * 0.8)
    # Useful for debugging
    # Draw circles around the pixels to check for collisions

    no_fill()
    ellipse(mouse_x, player_y, 10, 10)  # Draw collision point
    ellipse(mouse_x, player_y + 40, 10, 10)
    ellipse(mouse_x - 12, player_y + 20, 10, 10)
    ellipse(mouse_x + 12, player_y + 20, 10, 10)

    collide = get(mouse_x, player_y).hex
    collide2 = get(mouse_x - 12, player_y + 20).hex
    collide3 = get(mouse_x + 12, player_y + 20).hex
    collide4 = get(mouse_x, player_y + 40).hex

    if mouse_x < width:  # Off the left of the screen
        collide2 = safe.hex

    if mouse_x > width:  # Off the right of the screen
        collide3 = safe.hex

    if collide == safe.hex and collide2 == safe.hex and collide3 == safe.hex and collide4 == safe.hex:
        text('🎈', mouse_x, player_y)
    else:
        text('💥', mouse_x, player_y)
```

--- /collapse ---

Możesz nawet użyć pętli i sprawdzić wiele różnych pikseli. Tak działa wykrywanie kolizji w grach.

--- /task ---

--- save ---
