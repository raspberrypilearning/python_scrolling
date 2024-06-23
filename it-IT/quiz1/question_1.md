## Quiz veloce

Rispondi alle tre domande. Ci sono alcuni suggerimenti per aiutarti a trovare la risposta corretta.

Dopo aver risposto a ciascuna domanda, fai clic su **Controlla la mia risposta**.

Divertiti!

--- question ---
---
legend: Domanda 1 di 3
---

Hai usato molte istruzioni `if` per controllare il comportamento del tuo gioco. Alcuni di loro potrebbero aver avuto condizioni più complesse, utilizzando `and` per eseguire più test contemporaneamente. Se eseguissi la seguente parte di codice condizionale, quale ti aspetteresti che sia l'output?

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
Gran volo!
```
  --- feedback ---

Mentre `score >= 5000` è vero, per ognuna delle condizioni `and` entrambe devono essere vere, e `lives >= 3` falsa.

  --- /feedback ---

- (x)
```
Stai facendo bene!
Continua così!
```
  --- feedback ---

Questo è corretto — `score >= 5000` è vera, e così lo è `lives > 1` sulla dichiarazione indentata `if`.

  --- /feedback ---

- ( )
```
Stai facendo bene!
```
  --- feedback ---

Ci sei vicino, ma `score >= 5000` non è la sola condizione che il programma riterrebbe vera durante l'esecuzione.

  --- /feedback ---

- ( )
```
Insisti!
```
  --- feedback ---

Mentre `lives > 1` è vera, solo il codice dentro la prima condizione vera nelle dichiarazioni `if`/`elif`/`else` è eseguita, e `lives > 1` non è la prima condizione che è vera.

  --- /feedback ---

--- /choices ---

--- /question ---
