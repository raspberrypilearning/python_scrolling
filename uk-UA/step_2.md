## Вибір теми

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Встанови тему своєї гри та створи персонажа, який буде слідувати за курсором миші.

</div>
<div>

![Зображення черепахи розміром 100х100 на синьому фоні з розміром екрана 400х400.](images/theme-turtle.png){:width="300px"}

</div>
</div>

Яка тематика твоєї гри? Here are some ideas:
- Спорт або хобі
- Фільм, шоу або гра
- Наука або природа
- Або що-небудь інше!

--- task ---

Open the [Don't Collide! starter project](https://editor.raspberrypi.org/en/projects/dont-collide-starter){:target="_blank"} project. The code editor will open in another browser tab.

If you have a Raspberry Pi account, you can click on the **Save** button to save a copy to your **Projects**.

--- /task ---

--- task ---

**Choose:** Set the size of your canvas.

--- code ---
---
def setup():    
size(400, 400)
filename: main.py - setup()
---

def setup(): size(400, 400)

--- /code ---

--- /task ---

--- task ---

Це колір, на якому гравець може безпечно перебувати, і ти будеш використовувати цю змінну пізніше.

This is the colour that it is safe for the player to be on and you will use this variable again later.

--- code ---
---
def draw():    
safe = color(200, 100, 0) #Додай колір, відповідно до твоєї теми   
background(safe)
filename: main.py - draw()
---

def draw(): global safe safe = Color(200, 100, 0)  # Add the colour of your theme background(safe)

--- /code ---

[[[generic-theory-simple-colours]]]

--- /task ---

--- task ---

**Test:** Run your code to see the background colour. Change it until you are happy with the colour and the size of the screen.

--- /task ---

Now choose the character that is playing the game and avoiding the obstacles. Is it an object, person, animal, or something else?

The player will appear at a fixed `y` position and same `x` position as the mouse pointer, which is stored in the `p5` variable `mouse_x`.

--- task ---

Визнач функцію `draw_player()` та створи позицію `player_y`, для фіксації позиції гравця `y`:

Define a `draw_player()` function and create a `player_y` position for the fixed `y` position of the player:

--- code ---
---
def draw_player():    
player_y = int(height * 0.8) #Розташування в напрямку до нижньої частини екрана
line_highlights: 12-14
---

def draw_player(): player_y = int(height * 0.8)  # Positioned towards the screen bottom

--- /code ---

Add code to `draw()` to call `draw_player()` each frame.

--- code ---
---
def draw():    
safe = color(200, 100, 0) #Обраний тобою колір    
background(safe)    
draw_player()
filename: main.py - draw()
---

def draw(): global safe safe = Color(200, 100, 0)  # Your chosen colour background(safe) draw_player()

--- /code ---

--- /task ---

Next you will add code to the `draw_player()` function to draw your shape. You may also need to add `setup()` code.

--- task ---

**Choose:** What does your player look like? Your player could be:
+ Зображення, які наведені у стартовому проєкті
+ Емодзі 🎈 або текст
+ Малюнок, виконаний за допомогою декількох фігур

--- collapse ---
---
title: Використання стартового зображення
---

Images included in the starter project will be shown in the `Image gallery`.

![The Image gallery displaying the included images.](images/starter-images.png)

Make a note of the name of the image you want to use.

Запиши назву зображення, яке ти хочеш використати.

--- code ---
---
language: python filename: main.py - setup() line_numbers: true line_number_start: 9
filename: main.py - setup()
---

def setup(): size(400, 400) global player player = load_image('turtle.png')  # Load your image

--- /code ---

Call the `image()` and set it as global in the `draw_player()` function.

--- code ---
---
language: python filename: main.py - draw_player() line_numbers: true line_number_start: 14
line_highlights: 16
---

def draw_player(): player_y = int(height * 0.8)  # Positioned towards the screen bottom image(player, mouse_x, player_y, 30, 30)

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Використання символів емодзі
---

You can use emoji characters in the p5 `text()` function to use an emoji to represent your player.

Here's an example:

--- code ---
---
Ти можеш використовувати символи емодзі у функції p5 `text()`, щоб зобразити свого персонажа у вигляді емодзі.
filename: main.py - setup()
---

Ось приклад:

--- /code ---

Call the `text()` and set it as global in the `draw_player()` function.

--- code ---
---
language: python filename: main.py - draw_player() line_numbers: true line_number_start: 14
line_highlights: 16-17
---

def draw_player(): player_y = int(height * 0.8) text('🎈', mouse_x, player_y)

--- /code ---

--- /collapse ---

[[[processing-python-text]]]

[[[generic-theory-simple-colours]]]

[[[processing-python-ellipse]]]

[[[processing-python-rect]]]

[[[processing-python-triangle]]]

[[[processing-tint]]]

[[[processing-stroke]]]

**Tip:** You can use several simple shapes in the same function to create a more complex player.

--- collapse ---
---
title: Малювання персонажа за допомогою декількох фігур
---

![A face shape made from a green circle as a background and two eyes drawn from blue circles, with black circles within and a glint within those using a white circle.](images/face_player.png)

--- code ---
---
language: python
filename: main.py - draw_player()
---

def draw_player(): player_y = int(height * 0.8) noStroke() # Face fill(0, 200, 100) ellipse(mouse_x, player_y, 60, 60)

    # Eyes
    fill(0, 100, 200)
    ellipse(mouse_x - 10, player_y - 10, 20, 20)
    ellipse(mouse_x + 10, player_y - 10, 20, 20)
    fill(0)
    ellipse(mouse_x - 10, player_y - 10, 10, 10)
    ellipse(mouse_x + 10, player_y - 10, 10, 10)
    fill(255)
    ellipse(mouse_x - 12, player_y - 12, 5, 5)
    ellipse(mouse_x + 12, player_y - 12, 5, 5)

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

**Test:** Run your code and move the mouse to control the player.

Does it move like you expect?

--- /task ---

**Debug:** You might find some bugs in your project that you need to fix. Here are some common bugs.

--- task ---

--- collapse ---
---
title: Я не бачу персонажа
---

Try switching to full screen. Also, check the `x` and `y` coordinates that you used to draw the player — make sure they are inside the canvas you created with `size()`.

--- /collapse ---

--- collapse ---
---
title: Зображення не завантажується
---

First, check that the image is in the `Image gallery`. Then, check the filename really carefully — remember capital letters are different to lower case letters and punctuation is important.

--- /collapse ---

--- collapse ---
---
title: Зображення має неправильний розмір
---

Check the inputs that control the width and height of the image:

```python
image(image_file, x_coord, y_coord, width, height)
```

--- /collapse ---

--- collapse ---
---
title: Емодзі має неправильний розмір
---

Слід перевірити код, який визначає ширину та висоту зображення:

--- /collapse ---

--- /task ---

--- save ---
