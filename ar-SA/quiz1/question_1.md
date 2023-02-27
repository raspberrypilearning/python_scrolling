## Quick quiz

Answer the three questions. There are hints to guide you to the correct answer.

بعد كل سؤال ، اضغط على **إرسال**. سيتم توجيهك نحو الإجابة الصحيحة.

إستمتع!

--- question ---
---
القائمة: السؤال 1 من 3
---

لقد استخدمت الكثير من عبارات `if`للتحكم في سلوك لعبتك. بعض العبارات قد يتم استخدامها في حالات أكثر تعقيدًا ، مثل استخدام `and` لإجراء اختبارات متعددة في وقت واحد. إذا قمت بتشغيل الجزء التالي من الكود الشرطي، فماذا تتوقع أن يكون الناتج؟

```python
score = 5000
lives = 2

if score >= 5000 and lives >= 3:
  print('Great flying!')

if score >= 5000: 
  print('Doing well!')
  if lives > 1:
    print('Keep going!')
  else:
    print('But be careful!')

elif lives > 1:
  print('Push harder!')

else:
  print('Head for base!')
```

--- choices ---

- ( )
```
Great flying!
```
  --- feedback ---

بينما `score >= 5000` صحيحة ، يجب أن يكون كلا الجزأين صحيحين للشرط `و` ، و `lives >= 3` خطأ.

  --- /feedback ---

- (x)
```
!Doing well
!Keep going
```
  --- feedback ---

هذا صحيح - `score >= 5000` صحيحة ، وكذلك `lives > 1` على جملة `if` المتداخلة.

  --- /feedback ---

- ( )
```
!Doing well
```
  --- feedback ---

أغلق ، لكن `score >= 5000` ليس الشرط الوحيد الذي سيجده البرنامج صحيحًا أثناء تشغيله.

  --- /feedback ---

- ( )
```
!Push harder
```
  --- feedback ---

بينما `lives > 1`هو صحيح ، فقط التعليمات البرمجية داخل الشرط الحقيقي الأول في `if`/`elif`/`else` إذا تم تنفيذ و`lives > 1` ليس الشرط الاول يكون صحيحًا.

  --- /feedback ---

--- /choices ---

--- /question ---
