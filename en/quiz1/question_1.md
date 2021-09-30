## Reflection

Well done, you made a game!  Now it's time to reflect — reflecting is an important part of learning because it helps make new connections in your brain.

Answer the three questions below to reflect on what you've learnt.

After each question, press **submit**. You will be guided towards the correct answer. You can do this activity as many times as you want to.

Have fun!

--- question ---

---
legend: Question 1 of 3
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
Great flying!
```
  --- feedback ---
While `score >= 5000` is true, for an `and` condtion both parts must be true, and `lives >= 3` is false.
  --- /feedback ---

- (x) 
```
Doing well!
Keep going!
```
  --- feedback ---
This is correct — `score >= 5000` is true, and so is `lives > 1` on the nested `if` statement.
  --- /feedback ---

- ( ) 
```
Doing well!
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
