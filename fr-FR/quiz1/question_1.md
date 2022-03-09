## Réflexion

Bravo, tu as créé un jeu !  Maintenant, il est temps de réfléchir - la réflexion est une partie importante de l'apprentissage, car elle aide à établir de nouvelles connexions dans ton cerveau.

Réponds aux trois questions ci-dessous pour réfléchir à ce que tu as appris.

Après chaque question, appuie sur **soumettre**. Tu seras guidé vers la bonne réponse. Tu peux faire cette activité autant de fois que tu le souhaites.

Amuse-toi bien !

--- question ---
---
legend: Question 1 sur 3
---

Tu as utilisé beaucoup d'instructions `if` pour contrôler le comportement de ton jeu. Certains d'entre elles auraient pu avoir des conditions plus complexes, utilisant `and` pour effectuer plusieurs tests à la fois. Si tu exécutais le morceau de code conditionnel suivant, à quoi t'attendrais-tu comme résultat ?

```python
score = 5000
vies = 2

if score >= 5000 and vies >= 3:
  print('Superbe vol !')

if score >= 5000: 
  print('Ça va bien !')
  if vies > 1 :
    print('Continue !')
  else:
    print('Mais attention !')

elif vies > 1:
  print('Pousse plus fort !')

else :
  print('Va à la base !')
```

--- choices ---

- ( )
```
Superbe vol !
```
  --- feedback ---

Tant que `score >= 5000` est vrai, pour une condition `et` les deux parties doivent être vraies, et `vies >= 3` est faux.

  --- /feedback ---

- (x)
```
Ça va bien !
Continue !
```
  --- feedback ---

C'est correct - `score >= 5000` est vrai, de même que `vies > 1` sur l'instruction imbriquée `if`.

  --- /feedback ---

- ( )
```
Ça va bien !
```
  --- feedback ---

Proche, mais `score >= 5000` n'est pas la seule condition que le programme trouverait vraie pendant son exécution.

  --- /feedback ---

- ( )
```
Pousse plus fort!
```
  --- feedback ---

Tant que `vies > 1` est vrai, seul le code à l'intérieur de la première condition vraie dans une instruction `if`/`elif`/`else` est exécuté, et `vies > 1` n'est pas la première condition qui est vraie.

  --- /feedback ---

--- /choices ---

--- /question ---
