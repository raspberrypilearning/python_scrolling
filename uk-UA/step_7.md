## Вдосконалення твого проєкту

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Якщо у тебе є час, ти можеш вдосконалити свій проєкт.
</div>
<div>

![Приклад космічного проєкту з життям.](images/example1.png){:width="300px"}

</div>
</div>

Ось декілька ідей, які ти можеш спробувати:

### Додай різноманітні перешкоди
Ти можеш урізноманітнити свої перешкоди кількома способами:
 - Випадковим чином вибирати зображення, емодзі або функції для малювання перешкод
 - Випадковим чином налаштовувати колір, форму або розмір перешкод, змінюючи параметри, які їх малюють
 - Анімуй перешкоду, додавши обертання, зміну кольору або іншу візуальну дію, яка контролюється за допомогою `frame_count`

### Додай умову перемоги
Додати можливість перемоги у грі можна кількома способами:
 - Досягнення переможного рахунку
 - Досягнення певного рівня гри

Тобі потрібно повідомити гравця про його перемогу - можливо, використовуючи `print()` або `text()`, а потім зупинити гру.

### Дай гравцям більше одного життя
Додай у гру "життя", щоб дозволити гравцям пережити декілька зіткнень. This is a little trickier than just doing `lives -= 1` every time they collide with something:
 - Гравець може провести декілька кадрів в контакті з об'єктом - таким чином можна більше одного життя за одне зіткнення. Тобі потрібно не допустити цього
 - Тобі також треба зробити, щоб гравці знали, скільки життів у них залишилося, і, можливо, якесь попередження, щоб повідомити їх, якщо залишилось останнє життя
 - Можна додати об'єкт, який при зіткненні з гравцем подарує йому додаткове життя. Пам'ятай, що тобі потрібно буде внести зміни до твого звичайного коду для зіткнень, щоб він водночас не віднімав життя!

Each example project in the Introduction allows you to look at the code, get ideas, and see how they work.

The "Dodge Asteroids" project below has all of these features:

**Dodge asteroids**:
<iframe src="https://editor.raspberrypi.org/en/embed/viewer/dodge-asteroids-example" width="600" height="700" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
</iframe>

You can find the Dodge asteroids project [here](https://editor.raspberrypi.org/en/projects/dodge-asteroids-example){:target="_blank"}

Take a look at some Don't collide projects created by community members in the Raspberry Pi Foundation’s [Don't collide - Community library](https://wke.lt/w/s/KobNfx){:target="_blank"}.

--- save ---
