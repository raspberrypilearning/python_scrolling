## Quick quiz

Answer the three questions. There are hints to guide you to the correct answer.

When you have answered each question, click on **Check my answer**.

Have fun!

--- question ---
---
legend: 質問1/3
---

You have used a lot of `if` statements to control your game's behaviour. Some of them might have had more complex conditions, using `and` to make multiple tests at once. If you ran the following piece of conditional code, what would you expect the output to be?

```python
score = 5000
lives = 2

if score >= 5000 and lives >= 3:
  print('素晴らしい飛行です!')

if score >= 5000: 
  print('よくできました!')
  if lives > 1:
    print('どんどん行きましょう!')
  else:
    print('でも気をつけてください!')

elif lives > 1:
  print('がんばりましょう!')

else:
  print('基地に向かいましょう!')
```

--- choices ---

- ( )
```
素晴らしい飛行です！
```
  --- feedback ---

While `score >= 5000` is true, for an `and` condtion both parts must be true, and `lives >= 3` is false.

  --- /feedback ---

- (x)
```
よくできました!
どんどん行きましょう！
```
  --- feedback ---

This is correct — `score >= 5000` is true, and so is `lives > 1` on the nested `if` statement.

  --- /feedback ---

- ( )
```
よくできました!
```
  --- feedback ---

Close, but `score >= 5000` isn't the only condition the program would find true as it ran.

  --- /feedback ---

- ( )
```
がんばりましょう！
```
  --- feedback ---

While `lives > 1` is true, only the code inside the first true condition in an `if`/`elif`/`else` statement is executed, and `lives > 1` is not the first condition that is true.

  --- /feedback ---

--- /choices ---

--- /question ---
