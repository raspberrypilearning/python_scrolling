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
punteggio = 5000
vite = 2

if punteggio >= 5000 and vite >= 3:
  print('Gran volo!')

if punteggio >= 5000: 
  print('Stai facendo bene!')
  if vite > 1:
    print('Continua così!')
  else:
    print('Ma fa attenzione!')

elif vite > 1:
  print('Insisti!')

else:
  print('Verso la base!')
```

--- choices ---

- ( )
```
Gran volo!
```
  --- feedback ---

Mentre `punteggio >= 5000` è vero, per ognuna delle condizioni `and` entrambe devono essere vere, e `vite >= 3` falsa.

  --- /feedback ---

- (x)
```
Stai facendo bene!
Continua così!
```
  --- feedback ---

Questo è corretto — `punteggio >= 5000` è vera, e così lo è `vite > 1` sulla dichiarazione indentata `if`.

  --- /feedback ---

- ( )
```
Stai facendo bene!
```
  --- feedback ---

Ci sei vicino, ma `punteggio >= 5000` non è la sola condizione che il programma riterrebbe vera durante l'esecuzione.

  --- /feedback ---

- ( )
```
Insisti!
```
  --- feedback ---

Mentre `vite > 1` è vera, solo il codice dentro la prima condizione vera nelle dichiarazioni `if`/`elif`/`else` è eseguita, e `vite > 1` non è la prima condizione che è vera.

  --- /feedback ---

--- /choices ---

--- /question ---
