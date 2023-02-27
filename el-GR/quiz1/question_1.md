## Αναστοχασμός

Answer the three questions. There are hints to guide you to the correct answer.

Απάντησε στις τρεις ερωτήσεις παρακάτω για να διαπιστώσεις τι έμαθες.

Have fun!

--- question ---
---
legend: Ερώτηση 1 από 3
---

You have used a lot of `if` statements to control your game's behaviour. Some of them might have had more complex conditions, using `and` to make multiple tests at once. If you ran the following piece of conditional code, what would you expect the output to be?

```python
score = 5000
lives = 2

if score >= 5000 and lives >= 3:
  print('Υπέροχη πτήση!')

if score >= 5000: 
  print('Καλά τα πας!')
  if lives > 1:
    print('Συνέχισε!')
  else:
    print('Αλλά πρόσεχε!')

elif lives > 1:
  print('Προσπάθησε πιο πολύ!')

else:
  print('Κατευθύνσου προς τη βάση!')
```

--- choices ---

- ( )
```
Υπέροχη πτήση!
```
  --- feedback ---

While `score >= 5000` is true, for an `and` condtion both parts must be true, and `lives >= 3` is false.

  --- /feedback ---

- (x)
```
Τα πας καλά!
Συνέχισε!
```
  --- feedback ---

This is correct — `score >= 5000` is true, and so is `lives > 1` on the nested `if` statement.

  --- /feedback ---

- ( )
```
Τα πας καλά!
```
  --- feedback ---

Close, but `score >= 5000` isn't the only condition the program would find true as it ran.

  --- /feedback ---

- ( )
```
Προσπάθησε πιο πολύ!
```
  --- feedback ---

While `lives > 1` is true, only the code inside the first true condition in an `if`/`elif`/`else` statement is executed, and `lives > 1` is not the first condition that is true.

  --- /feedback ---

--- /choices ---

--- /question ---
