## Szybki quiz

Odpowiedz na trzy pytania. Istnieją wskazówki, które poprowadzą Cię do prawidłowej odpowiedzi.

Po udzieleniu odpowiedzi na każde pytanie kliknij ** Sprawdź moją odpowiedź **.

Miłej zabawy!

--- question ---
---
legend: Pytanie 1 z 3
---

Użyłeś wielu instrukcji ` `, aby kontrolować zachowanie twojej gry. Niektóre z nich mogły mieć bardziej złożone warunki, używając ` ` do wykonywania wielu testów jednocześnie. Gdybyś uruchomił następujący fragment kodu warunkowego, jaki byłby wynik?

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
Świetne latanie!
```
  --- feedback ---

Podczas gdy wynik ` >= 5000 ` jest prawdą, dla warunku ` ` obie części muszą być prawdziwe, a ` żyje >= 3 ` jest fałszywe.

  --- /feedback ---

- (x)
```
Dobrze sobie radzisz!
Nie przestawaj!
```
  --- feedback ---

To prawda — wynik ` >= 5000 ` jest prawdą, podobnie jak ` Lives > 1 ` w zagnieżdżonym wyrażeniu ` iff `.

  --- /feedback ---

- ( )
```
Dobrze sobie radzisz!
```
  --- feedback ---

Zamknij, ale wynik ` >= 5000 ` nie jest jedynym warunkiem, który program uzna za prawdziwy podczas jego uruchamiania.

  --- /feedback ---

- ( )
```
Naciskaj mocniej!
```
  --- feedback ---

Podczas gdy ` żyje > 1 ` jest prawdą, tylko kod wewnątrz pierwszego warunku true w instrukcji ` iff `/` elilife `/` ` jest wykonywany, a ` Lives > 1 ` nie jest pierwszym warunkiem, który jest prawdziwy.

  --- /feedback ---

--- /choices ---

--- /question ---
