## تفكير

أحسنت صنع لعبة!  الآن ، حان وقت التفكير - التفكير جزء مهم من التعلم ، لأنه يساعد في إنشاء روابط جديدة في عقلك.

أجب عن الأسئلة الثلاثة أدناه للتفكر فيما تعلمته.

بعد كل سؤال ، اضغط على**submit**. سيتم توجيهك نحو الإجابة الصحيحة. يمكنك القيام بهذا النشاط عدة مرات كما تريد.

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

While `score >= 5000` is true, for an `and` condtion both parts must be true, and `lives >= 3` is false.

  --- /feedback ---

- (x)
```
أحسنت صنعاً!
واصل التقدم!
```
  --- feedback ---

This is correct — `score >= 5000` is true, and so is `lives > 1` on the nested `if` statement.

  --- /feedback ---

- ( )
```
أحسنت صنعاً!
```
  --- feedback ---

Close, but `score >= 5000` isn't the only condition the program would find true as it ran.

  --- /feedback ---

- ( )
```
Push harder!
```
  --- feedback ---

While `lives > 1` is true, only the code inside the first true condition in an `if`/`elif`/`else` statement is executed, and `lives > 1` is not the first condition that is true.

  --- /feedback ---

--- /choices ---

--- /question ---
