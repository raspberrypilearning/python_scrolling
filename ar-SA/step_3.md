## اصنع عقبات

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
قم بإنشاء العقبات التي سيتعين عليك تجنبها لمواصلة لعب اللعبة.
</div>
<div>

! [مثال لمشروع تزلج بعوائق شجرية] (images / brothers.png) {: width = "300px"}

</div>
</div>

### ابدأ بعائق واحد

يمكنك صنع العوائق بنفس الطرق التي صنعت بها لاعبك. كيف تتناسب العقبات مع موضوعك؟

ستستخدم حلقة `مقابل` لعمل الكثير من النسخ لذا ما عليك سوى عمل أو اختيار عقبة واحدة.

--- task ---

حدد دالة `draw_obstacles ()`:

--- code ---
---
language: python
filename: main.py - draw_obstacles()
---

def draw_obstacles (): ob_x = العرض / 2 ob_y = الارتفاع / 2 نص ('🌵'، ob_x، ob_y) # استبدل بعقبتك


--- /code ---

أضف الكود إلى `draw ()` لاستدعاء `draw_obstacles ()` لكل إطار.

--- code ---
---
language: python
filename: main.py - draw()
---

def draw (): safe = color (200، 100، 0) # أضف لون السمة الخاصة بك الخلفية (آمنة)  
draw_obstacles () # قبل رسم اللاعب draw_player ()

--- /code ---

--- /task ---

--- task ---

**اختر:** كيف تبدو العقبة التي تواجهك؟ قد تكون عقبتك:
+ صورة مقدمة في مشروع البداية
+ رمز تعبيري 🌵 أو نص
+ مرسومة باستخدام سلسلة من الأشكال

--- collapse ---
---
العنوان: استخدم صورة أولية
---

انقر على **إدارة الصور** أيقونة.

![The picture icon in the top right of the code area.](images/manage-images.png)

سيتم عرض الصور المضمنة في مشروع البداية في قائمة `مكتبة الصور`.

![The Image library with a list of included images.](images/starter-images.png)

قم بتدوين اسم الصورة التي تريد استخدامها.

قم بتحميل الصورة في دالة `setup ()`.

--- code ---
---
language: python
filename: main.py - setup()
---

إعداد def (): الحجم (400 ، 400) لاعب = load_image ('skiing.png') # تحميل صورتك عقبة = تحميل صورتك ('صاروخ. png') # تحميل صورتك

--- /code ---

استدع الصورة `()` واضبطها على أنها عامة في دالة `draw_player ()`.

--- code ---
---
language: python
filename: main.py - draw_obstacles()
---

def draw_obstacles (): ob_x = العرض / 2 ob_y = الارتفاع / 2

   عقبة عالمية

   image (عقبة ، ob_x ، ob_y ، 30 ، 30) #Resize لتناسب موضوعك

--- /code ---

--- /collapse ---

--- collapse ---
---
العنوان: استخدم أحرف الرموز التعبيرية
---

يمكنك استخدام أحرف الرموز التعبيرية في دالة النص p5 `()` لاستخدام رمز تعبيري لتمثيل المشغل الخاص بك.

إليك مثالاً:

--- code ---
---
language: python
filename: main.py - setup()
---

إعداد def (): size (400، 400) text_size (40) # يتحكم في حجم الرموز التعبيرية text_align (CENTER، TOP) # الموضع حول المركز

--- /code ---

--- code ---
---
language: python
filename: main.py - draw_obstacles()
---

def draw_obstacles (): ob_x = العرض / 2 ob_y = الارتفاع / 2 نص ('🌵'، ob_x، ob_y) # استبدل بعقبتك

--- /code ---

--- /collapse ---

[[[processing-python-text]]]

[[[generic-theory-simple-colours]]]

[[[processing-python-ellipse]]]

[[[processing-python-rect]]]

[[[processing-python-triangle]]]

[[[processing-tint]]]

[[[processing-stroke]]]

**نصيحة:** يمكنك استخدام عدة أشكال بسيطة في نفس الدالة لإنشاء مشغل أكثر تعقيدًا.

--- collapse ---
---
العنوان: ارسم لاعبًا باستخدام أشكال متعددة
---

![desc](images/tree_obstacle.png)

--- code ---
---
language: python
filename: main.py - draw_obstacles()
---

def draw_obstacles(): ob_x = width/2 ob_y = height/2 #رسم شجرة الصنوبر no_stroke() fill(0,255,0) #اخضر للاوراق الإبرية triangle(ob_x + 20, ob_y + 20, ob_x + 10, ob_y + 40, ob_x + 30, ob_y + 40) triangle(ob_x + 20, ob_y + 30, ob_x + 5, ob_y + 55, ob_x + 35, ob_y + 55) triangle(ob_x + 20, ob_y + 40, ob_x + 0, ob_y + 70, ob_x + 40, ob_y + 70) fill(150,100,100) # بني للساق rect(ob_x + 15, ob_y + 70, 10, 10)

--- /code ---

--- /collapse ---

--- /task ---

### احصل على عقبة تتحرك

--- task ---

أضف الآن تعليمات برمجية لزيادة موضع العائق `ص` لكل إطار ، واجعله يلتف حوله عندما يصل إلى أسفل لإنشاء تأثير عقبة أخرى.

يبدأ المتغير p5 `frame_count` في حساب الإطارات عند النقر فوق "تشغيل".

`ob_y٪ = height` يعين موضع `y` على الباقي عند القسمة على `ارتفاع`. مع ارتفاع `` "400" ، سيؤدي ذلك إلى تحويل 2401 `إلى` `` ، لذلك عندما تنحرف العوائق عن أسفل الشاشة ، فإنها تظهر مرة أخرى في الأعلى.

--- code ---
---
language: python
filename: main.py - draw_obstacles()
---

def draw_obstacles (): ob_x = العرض / 2 ob_y = الارتفاع / 2 + frame_count # زيادة كل إطار ob_y٪ = height # الالتفاف حول نص ('🌵'، ob_x، ob_y) # استبدل العقبة الخاصة بك

--- /code ---

--- /task ---

### الكثير من العقبات

يمكنك رسم الكثير من نسخ العائق الخاص بك في مواقع بدء مختلفة ولكن هذا يتطلب الكثير من العمل. دعنا نستخدم الاختصار.


<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;"> 
<span style="color: #0faeb0">** الجيل الإجرائي **</span> يُستخدم في إنشاء عوالم اللعبة والعقبات ومشاهد الأفلام لإنشاء عشوائية ولكن مع تطبيق قواعد معينة. يعني <span style="color: #0faeb0">بذرة</span> أنه يمكنك الحصول على نفس النتائج في كل مرة تستخدم فيها نفس البذرة.</p>

--- task ---

يستخدم هذا الرمز حلقة من `لـ` مع `randint ()` لاختيار مواضع العائق لك. استدعاء الدالة العشوائية `()` أولاً يعني أنك ستحصل دائمًا على نفس الأرقام العشوائية. هذا يعني أن العوائق لن تقفز حول كل إطار ويمكنك تغيير البذرة حتى تحصل على واحدة تضع العوائق بشكل عادل.

--- code ---
---
language: python
filename: main.py - draw_obstacles()
---

def draw_obstacles():

  seed(12345678) #Any number is fine

  for i in range(6):  
ob_x = randint(0, height) ob_y = randint(0, height) + frame_count ob_y %= height text('🌵', ob_x, ob_y) #Replace with your obstacle

--- /code ---

Useful information:

[[[using-seed-in-python]]]

[[[generic-python-for-loop-repeat]]]

--- /task ---

--- collapse ---
---
title: Epilepsy warning
---

Testing your program has the potential to induce seizures for people with photosensitive epilepsy. If you have photosensitive epilepsy or feel you may be susceptible to a seizure, do not run your program. Instead, you can:
- Make sure you have added the `seed()` line of code to make sure your obstacles don't jump around
- Ask somebody to run it for you
- Move on and complete the project, asking someone to run the project for you at the end so you can debug
- Change the frame rate before you run your program by adding `frame_rate(1)` at the start of `setup()` — you can remove this once you have confirmed there is no bug

--- /collapse ---

--- task ---

**Test:** Run your program and you should see mutliple objects on the screen, wrapping around when they get to the bottom.

Change your code until you are happy with the obstacles you have. You can:

+ Change the seed to get obstacles in different starting positions
+ Change the number of times to loop repeats to get a different number of obstacles
+ Adjust the size of the obstacles

**Tip:** Make sure it is possible to avoid your obstacles but that there is no easy path through your game.

--- /task ---

--- task ---

**Debug:** You might find some bugs in your project that you need to fix. Here are some common bugs.

--- collapse ---
---
title: Only one obstacle is being drawn
---

Check your function that draws multiple obstacles:
 + Make sure it uses a `for` loop to call the obstacle drawing function more than once
 + Make sure it uses `randint()` to change the (x, y) coordinates it is passing to the obstacle drawing function
 + Check that you have used `ob_x` and `ob_y` as the coordinates for your obstacle

For example:

--- code ---
---
language: python
filename: main.py — draw_obstacles()
---

def draw_obstacles():

  seed(12345678)

  for i in range(6):  
ob_x = randint(0, height) ob_y = randint(0, height) + frame_count ob_y %= height text('🌵', ob_x, ob_y) #Replace with your obstacle

--- /code ---

--- /collapse ---

--- collapse ---
---
title: The obstacles are changing position every time a frame is drawn
---

Make sure that you have used `seed()` inside the function that draws multiple obstacles.

--- /collapse ---

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;"> 
Programmers use lots of neat tricks like using the `%` operator to make objects wrap around the screen and the `seed()` function to generate the same random numbers. The more coding you do, the more neat tricks you will learn.</p>

--- save ---
