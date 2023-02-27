## Beth nesaf?

Answer the three questions. There are hints to guide you to the correct answer.

Atebwch y tri chwestiwn isod i fyfyrio ar yr hyn rydych chi wedi'i ddysgu.

Ar ôl bob cwestiwn, pwyswch **cyflwyno**. Byddi di'n cael dy dywys i'r ateb cywir. Galli di wneud hyn gymaint ag y mynni.

--- question ---
---
legend: Cwestiwn 1 o 3
---

You have used a lot of `if` statements to control your game's behaviour. Some of them might have had more complex conditions, using `and` to make multiple tests at once. If you ran the following piece of conditional code, what would you expect the output to be?

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
Hedfan heb ei ail!
```
  --- feedback ---

While `score >= 5000` is true, for an `and` condtion both parts must be true, and `lives >= 3` is false.

  --- /feedback ---

- (x)
```
Ti'n gwneud yn dda!
Dal ati!
```
  --- feedback ---

This is correct — `score >= 5000` is true, and so is `lives > 1` on the nested `if` statement.

  --- /feedback ---

- ( )
```
Ti'n gwneud yn dda!
```
  --- feedback ---

Close, but `score >= 5000` isn't the only condition the program would find true as it ran.

  --- /feedback ---

- ( )
```
Gwthia'n galetach!
```
  --- feedback ---

While `lives > 1` is true, only the code inside the first true condition in an `if`/`elif`/`else` statement is executed, and `lives > 1` is not the first condition that is true.

  --- /feedback ---

--- /choices ---

--- /question ---
