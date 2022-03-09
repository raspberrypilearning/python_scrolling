## Accélérer !

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
La plupart des jeux de coureurs sans fin augmentent la difficulté du jeu au fur et à mesure que le joueur progresse et lui attribuent un score.
</div>
<div>

![Exemple de projet avec un score textuelle à l'écran.](images/score.png){:width="300px"}

</div>
</div>

### Ajouter des niveaux de difficulté

La création de niveaux de difficulté clairs permettra à ton joueur de comprendre plus facilement ce qui se passe.

--- task ---

Crée une variable `global` `niveau` pour suivre le niveau actuel du joueur. Régle-la sur `1` pour que les joueurs commencent une nouvelle partie au premier niveau.

--- code ---
---
language: python 
filename: main.py
line_numbers: false
---

#Inclure les variables globales ici
niveau = 1

--- /code ---

--- /task ---

--- task ---

Ce code utilise le `height` et le `frame_count` pour augmenter la variable `niveau` chaque fois que le joueur termine un écran, puis imprime le nouveau niveau pour le joueur.

**Choisir :** Ce code limite les niveaux à cinq, pour que le jeu ne devienne pas trop difficile. Il n'y a aucune raison pour que ton jeu en utilise cinq, mais tu dois choisir une limite. Les humains peuvent seulement se déplacer si vite !

--- code ---
---
language: python 
filename: main.py — draw_obstacles()
line_numbers: false
---

def dessine_obstacles():

  global niveau #Utiliser global niveau

  if frame_count % height == height - 1 and niveau < 5: 
    niveau += 1 
    print('Tu as atteint le niveau', niveau)

--- /code ---

--- /task ---

--- task ---


Les deux principales options pour augmenter la difficulté sont d'accélérer le jeu et d'augmenter le nombre d'obstacles.

--- collapse ---
---
title: Accélérer ton jeu
---

La vitesse du jeu est contrôlée par la vitesse à laquelle les obstacles semblent se déplacer vers le joueur. Ce code accélère cela en ajoutant `frame_count * niveau` à la coordonnée `y` lors de la génération de l'obstacle.

Au lieu de déplacer tes obstacles d'un pixel dans chaque image, ce code les déplace effectivement par `niveau` de pixels à la place.

En regardant le code, tu peux t'attendre à ce que la vitesse augmente de plus de `niveau` de pixels. Par exemple, juste avant que ton `niveau` n'augmente, le `frame_count` est `799` — comme le `niveau` augmente d'une image avant le `frame_count` est un multiple pair de `height` (fixé à `400` pixels) — et `799 * 3` est nettement plus grand que `799 * 2`. Cependant, les pixels supplémentaires créés en multipliant l'ensemble de `frame_count` par un nombre plus grand sont cachés par `ob_y %= height`. Cela ne laisse que les pixels supplémentaires de `niveau` à chaque étape.


--- code ---
---
language: python 
filename: main.py — draw_obstacles()
line_numbers: false
---

  for i in range(6): 
    ob_x = randint(0, height) 
    ob_y = randint(0, height) + (frame_count * niveau) 
    ob_y %= height #enroulement 
    text('🌵', ob_x, ob_y )

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Ajouter plus d'obstacles
---

L'ajout d'obstacles supplémentaires consiste simplement à augmenter le nombre de fois que la boucle `for` qui les crée s'exécute. Tu peux le faire en augmentant le nombre que tu passes à la fonction `range()` par `niveau`.

**Astuce :**Bien sûr, tu peux toujours utiliser `niveau* 2`, ou des multiples encore plus grands, si tu veux rendre ton jeu plus difficile.

--- /collapse ---

--- /task ---

### Garder le score

Plus un joueur dure longtemps sans entrer en collision avec un obstacle, mieux il joue à ton jeu. L'ajout d'un score leur permettra de voir dans quelle mesure ils s'en sortent.

--- task ---

Crée une variable globale `score` pour suivre le score du joueur. Mets-la à `0` pour que les joueurs commencent une nouvelle partie sans aucun point.

--- code ---
---
language: python 
filename: main.py
line_numbers: false
---

#Inclure les variables globales ici
score = 0

--- /code ---

--- /task ---

--- task ---

Tu peux augmenter le score de ton joueur pour chaque image où il n'est pas entré en collision avec un obstacle en augmentant son score lorsque tu vérifies la collision dans `dessine_joueur()`.

**Choisir :** Tu peux décider du nombre de points que vaut chaque image, mais augmenter le score du joueur par `niveau` récompense les joueurs qui peuvent survivre à des niveaux de difficulté plus élevés.

--- code ---
---
language: python
filename: main.py — draw_player()
---

global score

  if collision == sur: 
    text('🎈', mouse_x, joueur_y) score += niveau 
  else: 
    text('💥', mouse_x, joueur_y)

--- /code ---

--- /task ---

--- task ---

Les joueurs devraient pouvoir voir leur score. Parce qu'il augmente si rapidement, utiliser `print()` ne fonctionnerait pas très bien. Utilise la fonction p5 `text()` dans ta fonction `draw()` pour l'afficher sous forme de texte sur l'écran de jeu à la place.

[[[processing-python-text]]]

Tu peux utiliser l'opérateur `+` pour combiner deux ou plusieurs chaînes si tu souhaites donner un titre comme « score » ou « points ». Étant donné que `score` est un nombre, tu devras le convertir en chaîne avant de pouvoir le joindre à une autre chaîne. Tu peux le faire avec `str()`:

`message = 'Score : ' + str(score)`

**Astuce :** `str()` est l'abréviation de « string » — les programmeurs suppriment souvent des lettres comme celle-ci, donc ils n'ont pas à taper autant !

--- /task ---

### Perdu !

Lorsqu'un joueur est entré en collision avec un obstacle, le jeu doit cesser de bouger et son score doit cesser d'augmenter.

--- task ---

Tu peux utiliser la variable `niveau` pour signaler « Perdu » en la réglant sur 0 — une valeur qu'elle n'atteindra jamais autrement. Fais cela dans l'étape `else` de ton code de détection de collision.

--- /task ---

--- task ---

Crée une instruction `if` dans `draw()` qui teste si `niveau > 0` avant d'appeler l'une des fonctions — comme `background()`, `dessine_obstacles()`et `dessine_joueur()` — qui mettent à jour le jeu. Étant donné que ces fonctions ne sont pas appelées, le jeu entier semble se terminer, même si ton programme est toujours en cours d'exécution.

--- /task ---

--- task ---

**Débogage :** Il est possible que tu trouves des bogues dans ton projet que tu dois corriger. Voici quelques bogues assez courants.

--- collapse ---
---
title: Le score ne s'affiche pas
---

Assure-toi que tu as inclus la fonction `text()` qui dessine le score du joueur au point approprié dans ta fonction `draw()` et que tu lui as transmis les valeurs correctes :

`text('Texte à afficher', x, y)`

Ça devrait ressembler a quelque chose comme çà :

--- code ---
---
language: python
filename: main.py — draw()
---

  if niveau > 0: 
    background(sur) 
    fill(255) 
    text('Score: ' + str(score), width/2, 20) 
    dessine_obstacles() 
    dessine_joueur()

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Le jeu ne s'arrête pas après une collision
---

Si tu penses que ton jeu ne détecte pas du tout correctement les collisions, essaye d'abord les instructions de débogage de l'étape précédente, sous « Il n'y a pas de collision lorsque le joueur atteint un obstacle ».


Si ton jeu détecte correctement les collisions, vérifie que tu as correctement indenté le code qui dessine ton jeu à l'intérieur de l'énoncé `if niveau > 0`, pour t'assurer qu'il ne s'exécute que si cet énoncé est vrai. Par exemple :

--- code ---
---
language: python
filename: main.py — draw()
---

  if niveau > 0: 
    background(sur) 
    fill(255) 
    text('Score: ' + str(score), width/2, 20) 
    dessine_obstacles() 
    dessine_joueur()

--- /code ---

Enfin, si les deux fonctionnent correctement, ton jeu peut ne pas définir correctement le `niveau= 0` lorsqu'une collision se produit. Par exemple :

--- code ---
---
language: python
filename: main.py — draw_player()
---

  if collision == sur: 
    text('🎈', mouse_x, joueur_y) score += niveau 
  else: 
    text('💥', mouse_x, joueur_y) niveau = 0

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Le jeu ne va pas plus vite
---

Vérifie d'abord que `niveau` augmente correctement. Tu devrais voir un message imprimé à chaque fois qu'il monte. Si ce n'est pas le cas, vérifie à la fois le code pour imprimer le message et le code pour augmenter le niveau.

Si le niveau augmente correctement, vérifie ta fonction `dessine_obstacles()`. En particulier, vérifie que tu as `ob_y = randint(0, height) + (frame_count * niveau)`. Ça devrait ressembler a quelque chose comme çà :

--- code ---
---
language: python 
filename: main.py — draw_obstacles()
line_numbers: false
---

  for i in range(6 + niveau): 
    ob_x = randint(0, height) 
    ob_y = randint(0, height) + (frame_count * niveau) 
    ob_y %= height #enroulement 
    text('🌵', ob_x, ob_y)

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Les nouveaux obstacles n'apparaissent pas
---

Il y a plusieurs raisons pour lesquelles cela pourrait se produire. Et il y a d'autres raisons pour lesquelles cela peut sembler se produire, alors que ce n'est pas le cas. Tout d'abord, étant donné que de nouveaux obstacles sont ajoutés en fonction de `niveau`, vérifie que `niveau` augmente correctement. Tu devrais voir un message imprimé à chaque fois qu'il monte. Si ce n'est pas le cas, vérifie à la fois le code pour imprimer le message et le code pour augmenter le niveau.

Si le niveau augmente correctement, vérifie ta fonction `dessine_obstacles()` pour t'assurer que tu as utilisé `niveau` dans la fonction `range()` de la boucle `for` qui dessine les obstacles. Ça devrait ressembler a quelque chose comme çà :

--- code ---
---
language: python 
filename: main.py — draw_obstacles()
line_numbers: false
---

  for i in range(6 + niveau): 
    ob_x = randint(0, height) 
    ob_y = randint(0, height) + (frame_count * niveau) 
    ob_y %= height #enroulement 
    text('🌵', ob_x, ob_y)

--- /code ---

Si tu as effectué toutes ces vérifications et qu'il ne semble toujours pas que le nombre d'obstacles augmente, il est possible qu'ils le soient, mais tu ne le vois pas. Tu devrais essayer certaines de ces étapes pour tester ceci :
  - Ralentis le jeu en utilisant `frame_rate()` dans ta fonction `setup()` pour te donner plus de temps pour compter
  - Change la seed que tu utilises pour tes nombres aléatoires. C'est peu probable, mais il est possible que certains obstacles apparaissent au hasard directement les uns sur les autres
  - Ajoute un `print()` à la boucle `for` dans `dessine_obstacles()` qui imprime la valeur de `i` à chaque passage de la boucle, afin que tu puisses vérifier si elle s'exécute le nombre de fois qu'elle devrait
  - Juste à des fins de test, change `range (6 + niveau)` en `range (6 * niveau)` - cette augmentation devrait être plus facile à repérer !


--- /collapse ---

--- /task ---

--- save ---
