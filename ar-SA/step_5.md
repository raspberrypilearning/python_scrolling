## اسرع!

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
تزيد معظم ألعاب الركض التي لا نهاية لها من صعوبة اللعبة مع تقدم اللاعب ، ومنحهم درجة.
</div>
<div>

! [مثال لمشروع مع درجة نصية على الشاشة.] (images / Score.png) {: width = "300px"}

</div>
</div>

### أضف مستويات الصعوبة

سيؤدي إنشاء مستويات صعوبة واضحة إلى تسهيل فهم اللاعب لما يحدث.

--- task ---

أنشئ متغيرًا `global` `level`من المستوى لتتبع المستوى الذي يتواجد فيه اللاعب حاليًا. اضبطه على `1` ليبدأ اللاعبون لعبة جديدة في المستوى الأول.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 6
line_highlights: 7
---

# قم بتضمين المتغيرات العالمية هنا
المستوى = 1

--- /code ---

--- /task ---

--- task ---

تستخدم هذه الشفرة البرمجية `height` و `frame_count` لزيادة المتغير `level` في كل مرة ينهي فيها اللاعب الشاشة، ثم تطبع المستوى الجديد للاعب.

**اختر:** تحدد هذه الشفرة البرمجية المستويات إلى خمسة ، لذلك لا يصعب جدًا اللعب. لا يوجد سبب لاستخدام لعبتك خمسة ، ولكن يجب عليك اختيار حد. يمكن للبشر فقط التحرك بسرعة!

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

The two main options for increasing difficulty are to make the game move faster, and to increase the number of obstacles.

--- collapse ---
---
العنوان: تسريع اللعبة
---

The speed of the game is controlled by how fast obstacles seem to be moving towards the player. This code speeds this up by adding `frame_count * level` to the `y` coordinate during obstacle generation.

Instead of moving your obstacles by one pixel in every frame, this code effectively moves it by `level` pixels instead.

Looking at the code, you might expect the speed to increase by more than `level` pixels. For example, at the point just before your `level` increases, the `frame_count` is `799` — as the `level` increases one frame before the `frame_count` is an even multiple of `height` (set at `400` pixels) — and `799 * 3` is notably bigger than `799 * 2`. However, the extra pixels created by multiplying the whole of `frame_count` by a bigger number are hidden by `ob_y %= height`. This leaves only the `level` extra pixels in each step.

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
العنوان: أضف المزيد من العقبات
---

Adding extra obstacles is just a matter of increasing the number of times the `for` loop that creates them runs. You can do this by increasing the number you pass to the `range()` function by `level`.

**Tip:** Of course, you can always use `level * 2`, or even larger multiples, if you want to make your game harder.

--- /collapse ---

--- /task ---

### الحفاظ على النتيجة

The longer a player lasts without colliding with an obstacle, the better they're playing your game. Adding a score will let them see how well they're doing.

--- task ---

Create a global `score` variable to track the player's score. Set it to `0` so players start a new game without any points.

--- code ---
---
language: python filename: main.py
line_numbers: false
---

# قم بتضمين المتغيرات العالمية هنا
score = 0

--- /code ---

--- /task ---

--- task ---

You can increase your player's score for every frame where they have not collided with an obstacle by increasing their score when you check for collision in `draw_player()`.

**Choose:** You can decide how many points each frame is worth, but increasing the player's score by `level` rewards players who can survive at higher difficulty levels.

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

Players should be able to see their score. Because it increases so quickly, using `print()` wouldn't work very well. Use the p5 `text()` function inside your `draw()` function, to display it as text on the game screen instead.

[[[processing-python-text]]]

You can use the `+` operator to combine two or more strings if you want to give a heading like 'score' or 'points'. Because `score` is a number, you will need to convert it to a string before you can join it with another string. You can do this with `str()`:

```python
message = 'Score: ' + str(score)
```
**Tip:** `str()` is short for 'string' — programmers often remove letters like this, so they don't have to type as much!

--- /task ---

### انتهت اللعبة!

When a player has collided with an obstacle, the game should stop moving and their score should stop increasing.

--- task ---

You can use the `level` variable to signal 'Game over' by setting it to 0 — a value it will never reach any other way. Do this in the `else` step of your collision detection code.

--- /task ---

--- task ---

Create an `if` statement in `draw()` that tests whether `level > 0` before calling any of the functions — like `background()`, `draw_obstacles()`, and `draw_player()` — that update the game. Because these functions are not called, the entire game seems to end, even though your program is still running.

--- /task ---

--- task ---

**Debug:** You might find some bugs in your project that you need to fix. Here are some common bugs.

--- collapse ---
---
العنوان: النتيجة لا تظهر
---

Make sure that you've included the `text()` function that draws the player's score at the appropriate point in your `draw()` function, and that you've passed it the correct values:

```python
text('Text to display', x, y)`
```

It should look something like this:

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
العنوان: اللعبة لا تتوقف بعد الاصطدام
---

If you think your game might not be correctly detecting collisions at all, first try the debug instructions in the previous step, under 'There is no collision when the player reaches an obstacle'.

If your game is correctly detecting collisions, then check that you have properly indented the code that draws your game inside the `if level > 0` statement, to make sure it only runs if that statement is true. For example:

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

Finally, if both of those are working correctly, your game may not be setting `level = 0` correctly when a collision happens. For example:

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
العنوان: اللعبة لا تسرع
---

First, check that `level` is increasing correctly. You should see a message printed out every time it goes up. If this isn't happening, check both the code for printing the message and the code for increasing the level.

If level is increasing correctly, check your `draw_obstacles()` function. In particular, check that you have `ob_y = randint(0, height) + (frame_count * level)`. It should look something like this:

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
العنوان: لا تظهر عقبات جديدة
---

There are a few reasons this could be happening. And there are some more reasons why it might appear to be happening, when it isn't. First, because new obstacles are added based on `level`, check that `level` is increasing correctly. You should see a message printed out every time it goes up. If this isn't happening, check both the code for printing the message and the code for increasing the level.

If level is increasing correctly, check your `draw_obstacles()` function to ensure that you have `level` used in the `range()` function of the `for` loop that draws the obstacles. It should look something like this:

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

If you've done all these checks and it still doesn't look like the number of obstacles is increasing, it's possible that they are but you aren't seeing it. You should try some of these steps to test this:
  - Slow the game down by using `frame_rate = 10` in your call to `run()` to give you more time to count:

```python
run(frame_rate = 10)
```

You can alter the speed of the game by changing `10` to a higher or lower value.

  - Change the seed you're using for your random numbers. It's unlikely, but it is possible that some obstacles are randomly appearing directly on top of each other
  - Add a `print()` to the `for` loop in `draw_obstacles()` that prints out the value of `i` in each pass of the loop, so you can verify whether it's running the number of times it should
  - Just for testing purposes, change `range(6 + level)` to `range(6 * level)` — that increase should be easier to spot!

--- /collapse ---

--- /task ---

--- save ---
