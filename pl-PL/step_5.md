## Przyspiesz!

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Większość niekończących się gier dla biegaczy zwiększa trudność gry w miarę postępów gracza i daje im wynik.
</div>
<div>

![przykładowy projekt z wynikiem tekstowym na ekranie.](images/score.png){:width="300px"}

</div>
</div>

### Dodaj poziomy trudności

Stworzenie jasnych poziomów trudności ułatwi graczowi zrozumienie, co się dzieje.

--- task ---

Utwórz zmienną ` global ` ` `, aby śledzić poziom, na którym aktualnie znajduje się gracz. Ustaw go na ` `, aby gracze zaczęli nową grę na pierwszym poziomie.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 6
line_highlights: 7
---

# Uwzględnij zmienne globalne tutaj
level = 1

--- /code ---

--- /task ---

--- task ---

Ten kod używa ` ` i ` frame_`, aby zwiększyć zmienną ` ` za każdym razem, gdy gracz ukończy ekran, a następnie wydrukuje nowy poziom dla gracza.

** Wybierz:** Ten kod ogranicza poziomy do pięciu, więc gra nie jest zbyt trudna. Nie ma powodu, dla którego Twoja gra musi używać pięciu, ale powinieneś wybrać limit. Ludzie mogą poruszać się tylko tak szybko!

--- code ---
---
language: python
filename: main.py — draw_obstacles()
---

def draw_obstacles(): global level  # Use the global level

    if frame_count % height == height - 1 and level < 5:
        level += 1
        print('You have reached level', level)

--- /code ---

--- /task ---

--- task ---

Dwie główne opcje zwiększające trudność to szybsze poruszanie się gry i zwiększenie liczby przeszkód.

--- collapse ---
---
Title: Przyspiesz swoją grę
---

Prędkość gry jest kontrolowana przez to, jak szybko przeszkody wydają się poruszać w kierunku gracza. Ten kod przyspiesza to, dodając ` frame_count * ` do współrzędnej `.` podczas generowania przeszkód.

Zamiast przesuwać przeszkody o jeden piksel w każdej klatce, ten kod skutecznie przesuwa go o piksele ` `.

Patrząc na kod, możesz oczekiwać, że prędkość wzrośnie o więcej niż piksele </code> na poziomie `. 
Na przykład, w punkcie tuż przed zwiększeniem poziomu <code> `, wartość </code> frame_` to ` 799 </code> — ponieważ wskaźnik ` ` zwiększa się o jedną klatkę, zanim ` frame_` będzie parzystą wielokrotnością ` ` (ustawioną na piksele </code> 400 `) — a <code> 799 * 3 ` jest znacznie większa niż ` 799 * 2<code>. Jednak dodatkowe piksele utworzone przez pomnożenie całości <code>_` przez większą liczbę są ukryte przez ` ob_y %= `. Pozostawia to tylko dodatkowe piksele ` ` w każdym kroku.

--- code ---
---
language: python filename: main.py — draw_obstacles()
line_numbers: false
---

    for i in range(6):
        ob_x = randint(0, height)
        ob_y = randint(0, height) + (frame_count * level)
        ob_y %= height  # Wrap around
        text('🌵', ob_x, ob_y)

--- /code ---

--- /collapse ---

--- collapse ---
---
Title: Dodaj więcej przeszkód
---

Dodanie dodatkowych przeszkód to tylko kwestia zwiększenia liczby uruchomień pętli ` `, która tworzy je. Możesz to zrobić, zwiększając liczbę przekazywaną do funkcji ` range()` przez ` `.

** Wskazówka:** Oczywiście zawsze możesz używać ` level * 2 `, a nawet większych wielokrotności, jeśli chcesz, aby Twoja gra była trudniejsza.

--- /collapse ---

--- /task ---

### Zachowaj wynik

Im dłużej gracz trwa bez zderzenia z przeszkodą, tym lepiej gra w twoją grę. Dodanie wyniku pozwoli im zobaczyć, jak dobrze sobie radzą.

--- task ---

Utwórz globalną zmienną ` `, aby śledzić wynik gracza. Ustaw go na ` 0 `, aby gracze rozpoczynali nową grę bez żadnych punktów.

--- code ---
---
language: python filename: main.py
line_numbers: false
---

# Uwzględnij zmienne globalne tutaj
score = 0

--- /code ---

--- /task ---

--- task ---

Możesz zwiększyć wynik gracza za każdą klatkę, w której nie zderzył się z przeszkodą, zwiększając swój wynik podczas sprawdzania kolizji w ` draw_player()`.

** Wybierz:** Możesz zdecydować, ile punktów jest warta każda klatka, ale zwiększenie wyniku gracza o ` ` nagradza graczy, którzy mogą przetrwać na wyższych poziomach trudności.

--- code ---
---
language: python
filename: main.py — draw_player()
---

    global score
    
    if collide == safe.hex:
        text('🎈', mouse_x, player_y)
        score += level
    else:
        text('💥', mouse_x, player_y)

--- /code ---

--- /task ---

--- task ---

Gracze powinni być w stanie zobaczyć swój wynik. Ponieważ wzrasta tak szybko, użycie ` print()` nie działałoby zbyt dobrze. Użyj funkcji p5 ` text()` wewnątrz funkcji ` draw()`, aby wyświetlić ją jako tekst na ekranie gry.

[[[processing-python-text]]]

Możesz użyć operatora `+`, aby połączyć dwa lub więcej ciągów, jeśli chcesz nadać nagłówek taki jak „wynik” lub „punkty”. Ponieważ ` ` to liczba, musisz ją przekonwertować na ciąg, zanim będziesz mógł połączyć z innym ciągiem. Możesz to zrobić za pomocą ` str()`:

```python
message = 'Score: ' + str(score)
```
** Wskazówka:** ` str()` to skrót od „string” — programiści często usuwają litery w ten sposób, więc nie muszą wpisywać zbyt wiele!

--- /task ---

### Koniec gry!

Gdy gracz zderzy się z przeszkodą, gra powinna przestać się poruszać, a ich wynik powinien przestać rosnąć.

--- task ---

Możesz użyć zmiennej ` `, aby zasygnalizować „koniec gry”, ustawiając ją na 0 — wartość, której nigdy nie osiągnie w inny sposób. Zrób to w kroku ` ` kodu wykrywania kolizji.

--- /task ---

--- task ---

Utwórz instrukcję ` ` w ` losw()`, która sprawdza, czy ` level > 0 ` przed wywołaniem którejkolwiek z funkcji — takich jak ` background()`, ` draw_obstancts()` i ` draw_player()` — które aktualizują grę. Ponieważ te funkcje nie są wywoływane, cała gra wydaje się się kończyć, nawet jeśli twój program jest nadal uruchomiony.

--- /task ---

--- task ---

** Debug:** Możesz znaleźć kilka błędów w swoim projekcie, które musisz naprawić. Oto kilka typowych robaków.

--- collapse ---
---
Title: Wynik nie jest wyświetlany
---

Upewnij się, że uwzględniłeś funkcję ` text()`, która rysuje wynik gracza w odpowiednim punkcie w funkcji ` draw()` i że przekazałeś jej prawidłowe wartości:

```python
text('Text to display', x, y)`
```

Powinien wyglądać coś takiego:

--- code ---
---
language: python
filename: main.py — draw()
---

    if level > 0:
        background(safe) 
        fill(255)
        text('Score: ' + str(score), width/2, 20)
        draw_obstacles()
        draw_player()

--- /code ---

--- /collapse ---

--- collapse ---
---
Title: Gra nie zatrzymuje się po kolizji
---

Jeśli uważasz, że Twoja gra może w ogóle nie wykrywać prawidłowo kolizji, najpierw wypróbuj instrukcje debugowania w poprzednim kroku, w sekcji „nie ma kolizji, gdy gracz dotrze do przeszkody”.

Jeśli Twoja gra prawidłowo wykrywa kolizje, sprawdź, czy prawidłowo wcięto kod, który rysuje twoją grę wewnątrz instrukcji ` if poziom > 0 ` , aby upewnić się, że działa tylko wtedy, gdy to stwierdzenie jest prawdziwe. Na przykład:

--- code ---
---
language: python
filename: main.py — draw()
---

    if level > 0:
        background(safe)
        fill(255)
        text('Score: ' + str(score), width/2, 20)
        draw_obstacles()
        draw_player()

--- /code ---

Na koniec, jeśli oba działają poprawnie, Twoja gra może nie ustawić ` level = 0 ` poprawnie, gdy dojdzie do kolizji. Na przykład:

--- code ---
---
language: python
filename: main.py — draw_player()
---

    if collide == safe.hex:
        text('🎈', mouse_x, player_y)
        score += level
    else:
        text('💥', mouse_x, player_y)
        level = 0

--- /code ---

--- /collapse ---

--- collapse ---
---
Title: Gra nie robi się szybsza
---

Najpierw sprawdź, czy ` ` rośnie prawidłowo. Powinieneś zobaczyć wiadomość wydrukowaną za każdym razem, gdy zostanie podniesiona. Jeśli tak się nie stanie, sprawdź zarówno kod do wydrukowania wiadomości, jak i kod do zwiększenia poziomu.

Jeśli poziom wzrasta prawidłowo, sprawdź funkcję ` draw_obstancts()` . W szczególności sprawdź, czy masz ` ob_y = randint(0, height) + (frame_count * level)`. Powinien wyglądać coś takiego:

--- code ---
---
language: python filename: main.py — draw_obstacles()
line_numbers: false
---

    for i in range(6 + level):
        ob_x = randint(0, height)
        ob_y = randint(0, height) + (frame_count * level)
        ob_y %= height  # Wrap around
        text('🌵', ob_x, ob_y)

--- /code ---

--- /collapse ---

--- collapse ---
---
Title: Nowe przeszkody nie pojawiają się
---

Istnieje kilka powodów, dla których może się to zdarzyć. I jest jeszcze kilka powodów, dla których może się to wydawać, że dzieje się, gdy tak nie jest. Po pierwsze, ponieważ nowe przeszkody są dodawane w oparciu o ` `, sprawdź, czy ` ` rośnie prawidłowo. Powinieneś zobaczyć wiadomość wydrukowaną za każdym razem, gdy zostanie podniesiona. Jeśli tak się nie stanie, sprawdź zarówno kod do wydrukowania wiadomości, jak i kod do zwiększenia poziomu.

Jeśli poziom wzrasta prawidłowo, sprawdź funkcję ` draw_obstancts()` </code>, aby upewnić się, że w funkcji ` range()` pętli </code>, która rysuje przeszkody, użyto ` <code>. Powinien wyglądać coś takiego:</p>

<p spaces-before="0">--- code ---</p>

<hr />

<p spaces-before="0">language: python
filename: main.py — draw_obstacles()</p>

<h2 spaces-before="0">line_numbers: false</h2>

<pre><code>for i in range(6 + level):
    ob_x = randint(0, height)
    ob_y = randint(0, height) + (frame_count * level)
    ob_y %= height  # Wrap around
    text('🌵', ob_x, ob_y)
`</pre>

--- /code ---

Jeśli wykonałeś wszystkie te kontrole i nadal nie wygląda na to, że liczba przeszkód rośnie, możliwe, że są, ale nie widzisz tego. Powinieneś wypróbować niektóre z tych kroków, aby to przetestować:
  - Zwolnij grę, używając ` frame_rate = 10 ` w swoim połączeniu z ` run()`, aby dać ci więcej czasu na liczenie:

```python
run(frame_rate = 10)
```

Możesz zmienić prędkość gry, zmieniając ` ` na wyższą lub niższą wartość.

  - Zmień źródło, którego używasz do losowych liczb. Jest to mało prawdopodobne, ale możliwe jest, że niektóre przeszkody pojawiają się losowo bezpośrednio nad sobą
  - Dodaj ` print()` do pętli ` ` w ` draw_objects()`, która wyświetla wartość ` ` w każdym przejściu pętli, aby móc sprawdzić, czy działa ona tyle razy, ile powinna
  - Tylko do celów testowych zmień ` range(6 + poziom)` na ` range(6 * poziom)` — ten wzrost powinien być łatwiejszy do wykrycia!

--- /collapse ---

--- /task ---

--- save ---
