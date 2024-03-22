## قم بترقية مشروعك

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
إذا كان لديك الوقت ، يمكنك تطوير مشروعك.
</div>
<div>

![Example space project with lives.](images/example1.png){:width="300px"}

</div>
</div>

إليك بعض الأفكار لمساعدتك:

### قم بتضمين مجموعة متنوعة من العقبات
يمكنك إضافة مجموعة متنوعة إلى عقباتك بعدة طرق:
 - اختر عشوائيًا بين العديد من الصور أو الرموز التعبيرية أو دوال رسم العوائق
 - اضبط لون العوائق أو شكلها أو حجمها عشوائيًا عن طريق تغيير المتغيرات التي ترسمها
 - حرك العائق عن طريق إضافة دوران ، أو تغيير اللون ، أو بعض الاختلافات المرئية الأخرى التي يتم التحكم فيها بواسطة `frame_count`

### أضف شرط الفوز
يمكنك جعل اللاعبين يفوزون باللعبة بعدة طرق:
 - تحقيق نتيجة الفوز
 - الوصول إلى مستوى معين من اللعبة

بمجرد فوزهم ، يجب أن تخبرهم بطريقة ما - ربما باستخدام `print()` أو `text()` ثم إيقاف اللعبة.

### امنح اللاعبين أكثر من حياة واحدة
أضف الأرواح إلى لعبتك ، للسماح للاعبين بالنجاة من بعض الاصطدامات. This is a little trickier than just doing `lives -= 1` every time they collide with something:
 - قد يقضي اللاعب إطارات متعددة على اتصال بجسم ما ، وبالتالي يفقد أكثر من حياة لتصادم واحد - ستحتاج إلى منع حدوث ذلك
 - ستحتاج أيضًا إلى وسيلة للاعبين لمعرفة عدد الأرواح المتبقية لديهم ، وربما نوعًا من التحذير يخبرهم عندما يكونون في حياتهم الأخيرة
 - يمكنك إضافة كائن ، عندما يصطدم به اللاعب ، يمنحه حياة إضافية. تذكر أنك ستحتاج إلى تعديل الشفرة البرمجية للاصطدام العادي بحيث لا يطرح الحياة في نفس الوقت!

Each example project in the Introduction allows you to look at the code, get ideas, and see how they work.

The "Dodge Asteroids" project below has all of these features:

**Dodge asteroids**:
<iframe src="https://editor.raspberrypi.org/en/embed/viewer/dodge-asteroids-example" width="600" height="700" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
</iframe>

You can find the Dodge asteroids project [here](https://editor.raspberrypi.org/en/projects/dodge-asteroids-example){:target="_blank"}

Take a look at some Don't collide projects created by community members in the Raspberry Pi Foundation’s [Don't collide - Community library](https://wke.lt/w/s/KobNfx){:target="_blank"}.

--- save ---
