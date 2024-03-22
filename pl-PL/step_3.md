## Tworzenie przeszkód

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Stwórz przeszkody, których będziesz musiał unikać, aby kontynuować grę.
</div>
<div>

![przykład projektu narciarskiego z przeszkodami drzew](images/objects.png){:width="300px"}

</div>
</div>

### Zacznij od jednej przeszkody

Możesz tworzyć przeszkody w taki sam sposób, w jaki stworzyłeś swojego gracza. Jak przeszkody pasują do Twojego motywu?

Użyjesz pętli ` `, aby wykonać wiele kopii, więc musisz tylko wykonać lub wybrać jedną przeszkodę.

--- task ---

Zdefiniuj funkcję ` draw_objects()`:

--- code ---
---
język: python nazwa pliku: main.py - draw_objects() line_numbers: false line_number_start:
line_highlights: 4
---

def draw_obstacles(): ob_x = width/2 ob_y = height/2 text('🌵', ob_x, ob_y)  # Replace with your obstacle

--- /code ---

Dodaj kod do ` draw()`, aby wywołać ` draw_objects()` każdą klatkę.

--- code ---
---
language: python filename: main.py - draw() line_numbers: false line_number_start:
line_highlights: 5
---

def draw(): global safe safe = Color(200, 100, 0)  # Add the colour of your theme background(safe) draw_obstacles()  # Before drawing the player draw_player()

--- /code ---

--- /task ---

--- task ---

** Wybierz:** jak wygląda Twoja przeszkoda? Twoja przeszkoda może być:
+ Obraz dostarczony w projekcie startowym
+ Emoji? lub tekst
+ Narysowany przy użyciu serii kształtów

--- collapse ---
---
Title: Użyj obrazu startowego
---

Obrazy zawarte w projekcie startowym zostaną pokazane w galerii obrazów `.`.

![Galeria obrazów przedstawiająca dołączone obrazy.](images/starter-images.png)

Zanotuj nazwę obrazu, którego chcesz użyć.

Załaduj obraz do funkcji ` setup()`

--- code ---
---
language: python filename: main.py - setup() line_numbers: true line_number_start: 9
line_highlights: 12
---

def setup(): size(400, 400) global player player = load_image('skiing.png')  # Load your player image obstacle = load_image('rocket.png')  # Load your obstacle image

--- /code ---

Znajdź linię `# Zachowaj to, aby uruchomić swój kod `. Przed tą linią zdefiniuj nową funkcję ` draw_obstancts()`, wywołaj ` ` jako zmienną globalną i użyj jej w wywołaniu do ` image()`.

--- code ---
---
language: python
filename: main.py - draw_obstacles()
---

def draw_obstacles(): ob_x = width/2 ob_y = height/2

    global obstacle
    
    image(obstacle, ob_x, ob_y, 30, 30)  # Resize to fit your theme

--- /code ---

--- /collapse ---

--- collapse ---
---
Title: Użyj znaków emoji
---

Możesz użyć znaków emoji w funkcji p5 ` text()`, aby reprezentować swoje przeszkody.

Oto przykład:

--- code ---
---
language: python
filename: main.py - setup()
---

def setup(): size(400, 400) text_size(40)  # Controls the size of the emoji text_align(CENTER, TOP)  # Position around the centre

--- /code ---

Znajdź linię `# Zachowaj to, aby uruchomić swój kod `. Przed tą linią zdefiniuj nową funkcję ` draw_objects()` .

--- code ---
---
language: python
filename: main.py - draw_obstacles()
---

def draw_obstacles(): ob_x = width/2 ob_y = height/2 text('🌵', ob_x, ob_y)

--- /code ---

--- /collapse ---

[[[processing-python-text]]]

[[[generic-theory-simple-colours]]]

[[[processing-python-ellipse]]]

[[[processing-python-rect]]]

[[[processing-python-triangle]]]

[[[processing-tint]]]

[[[processing-stroke]]]

** Wskazówka:** Możesz użyć kilku prostych kształtów w tej samej funkcji, aby stworzyć bardziej złożoną przeszkodę.

--- collapse ---
---
Title: Narysuj przeszkodę za pomocą wielu kształtów
---

![Drzewo narysowane z zielonymi trójkątami dla ciała i brązowym prostokątem dla pnia](images/tree_obstacle.png)

--- code ---
---
language: python
filename: main.py - draw_obstacles()
---

def draw_obstacles(): ob_x = width/2 ob_y = height/2 # Draw a fir tree no_stroke() fill(0,255,0)  # Green for needles triangle(ob_x + 20, ob_y + 20, ob_x + 10, ob_y + 40, ob_x + 30, ob_y + 40) triangle(ob_x + 20, ob_y + 30, ob_x + 5, ob_y + 55, ob_x + 35, ob_y + 55) triangle(ob_x + 20, ob_y + 40, ob_x + 0, ob_y + 70, ob_x + 40, ob_y + 70) fill(150,100,100)  # Brown for trunk rect(ob_x + 15, ob_y + 70, 10, 10)

--- /code ---

--- /collapse ---

--- /task ---

### Spraw, aby Twoja przeszkoda się poruszyła

--- task ---

Teraz dodaj kod, aby zwiększyć pozycję przeszkody `.` każdej klatce i sprawić, aby zawinęła, gdy dotrze do dołu, aby stworzyć efekt innej przeszkody.

Zmienna p5 ` frame_` zaczyna odliczać ramki po kliknięciu przycisku uruchom.

` ob_y %= wysokość ` ustawia pozycję `.` na pozostałą po podzieleniu przez ` `. Z ` ` '400' spowoduje to zmianę ` ` w ` `, więc gdy przeszkody zsuną się na dole ekranu, pojawia się ponownie u góry.

--- code ---
---
language: python
filename: main.py - draw_obstacles()
---

def draw_obstacles(): ob_x = width/2 ob_y = height/2 + frame_count  # Increases each frame ob_y %= height  # Wrap around text('🌵', ob_x, ob_y)  # Replace with your obstacle

--- /code ---

--- /task ---

### Wiele przeszkód

Możesz narysować wiele kopii swojej przeszkody w różnych miejscach startowych, ale to całkiem sporo pracy. Użyjmy skrótu.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;"> 
<span style="color: #0faeb0">**Generacja proceduralna**</span> jest używany do tworzenia światów gry, przeszkód i scen filmowych w celu stworzenia losowości, ale z zastosowaniem określonych zasad. <span style="color: #0faeb0"> seed </span> oznacza, że możesz wygenerować te same wyniki za każdym razem, gdy używasz tego samego źródła.</p>

--- task ---

Ten kod używa pętli ` ` z ` randint()` do wyboru pozycji przeszkód dla Ciebie. Wywołanie funkcji losowej ` seed()` oznacza, że zawsze otrzymasz te same losowe liczby. Oznacza to, że przeszkody nie skaczą po każdej klatce i możesz zmienić ziarno, dopóki nie otrzymasz takiego, które pozycjonuje przeszkody sprawiedliwie.

--- code ---
---
language: python
filename: main.py - draw_obstacles()
---

def draw_obstacles(): seed(12345678)  # Any number is fine

    for i in range(6):  
        ob_x = randint(0, height)
        ob_y = randint(0, height) + frame_count
        ob_y %= height
        text('🌵', ob_x, ob_y)  # Replace with your obstacle

--- /code ---

Przydatne informacje:

[[[using-seed-in-python]]]

[[[generic-python-for-loop-repeat]]]

--- /task ---

--- collapse ---
---
Title: Ostrzeżenie o padaczce
---

Testowanie twojego programu może wywołać drgawki u osób z padaczką światłoczułą. Jeśli masz padaczkę światłoczułą lub czujesz, że możesz być podatny na atak, nie uruchamiaj programu. Zamiast tego możesz:
- Upewnij się, że dodałeś linię kodu ` seed()`, aby upewnić się, że przeszkody nie skaczą
- Poproś kogoś, aby uruchomił go za Ciebie
- Przejdź do i ukończ projekt, prosząc kogoś o uruchomienie projektu za Ciebie na końcu, abyś mógł debugować
- Zwolnij grę, używając ` frame_rate = 10 ` w swoim połączeniu z ` run()` w następujący sposób:

```python
run(frame_rate = 10)
```
Możesz zmienić prędkość gry, zmieniając ` ` na wyższą lub niższą wartość.

--- /collapse ---

--- task ---

Test **:** Uruchom swój program i powinieneś zobaczyć wiele obiektów na ekranie, owijając się, gdy dotrą do dołu.

Zmień swój kod, aż będziesz zadowolony z przeszkód, które masz. Możesz:

+ Zmień ziarno, aby uzyskać przeszkody w różnych pozycjach startowych
+ Zmień liczbę powtórzeń pętli, aby uzyskać inną liczbę przeszkód
+ Dostosuj rozmiar przeszkód

** Wskazówka:** Upewnij się, że możliwe jest uniknięcie przeszkód, ale nie ma łatwej ścieżki przez twoją grę.

--- /task ---

--- task ---

** Debug:** Możesz znaleźć kilka błędów w swoim projekcie, które musisz naprawić. Oto kilka typowych robaków.

--- collapse ---
---
Title: Rysowana jest tylko jedna przeszkoda
---

Sprawdź swoją funkcję, która rysuje wiele przeszkód:
 + Upewnij się, że używa pętli ` ` do wywołania funkcji rysowania przeszkód więcej niż raz
 + Upewnij się, że używa ` randint()` do zmiany współrzędnych (x, y), które przechodzi do funkcji rysowania przeszkód
 + Sprawdź, czy użyłeś współrzędnych ` ob_` i ` ob_` jako współrzędnych przeszkody

Na przykład:

--- code ---
---
language: python
filename: main.py — draw_obstacles()
---

def draw_obstacles(): seed(12345678)

    for i in range(6):  
        ob_x = randint(0, height)
        ob_y = randint(0, height) + frame_count
        ob_y %= height
        text('🌵', ob_x, ob_y)  # Replace with your obstacle

--- /code ---

--- /collapse ---

--- collapse ---
---
Title: Przeszkody zmieniają pozycję za każdym razem, gdy ramka jest rysowana
---

Upewnij się, że użyłeś ` seed()` wewnątrz funkcji, która rysuje wiele przeszkód.

--- /collapse ---

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;"> 
Programiści używają wielu zgrabnych sztuczek, takich jak użycie operatora "%", aby obiekty owijały się po ekranie, a funkcja "seed()" generująca te same losowe liczby. Im więcej zrobisz kodowanie, tym bardziej schludne sztuczki się nauczysz.</p>

--- save ---
