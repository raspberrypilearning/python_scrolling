--- question ---
---
legend : Question 2 sur 3
---

Dans ce projet, tu as utilisé la génération procédurale, c'est-à-dire que l'ordinateur crée et place des parties de ton monde pour toi. Bien que cela permette de gagner beaucoup de temps, en particulier si tu crées des niveaux très volumineux, cela peut créer des problèmes. Lequel de ces problèmes dois tu rechercher lorsque tu testes ta génération procédurale ?

--- choices ---

- (x) Tous

  --- feedback ---

Correct ! Tout cela peut se produire lors de l'utilisation de la génération procédurale. Tu peux soit ajouter plus de code pour vérifier et contourner ces problèmes, soit essayer différentes seeds jusqu'à ce que tu en trouves une qui fonctionne.

  --- /feedback ---

- ( ) Des obstacles peuvent être générés qui ne laissent au joueur aucune route vers l'avant.

  --- feedback ---

Pas tout à fait. Cela peut se produire avec des obstacles générés de manière procédurale, en particulier lorsque le jeu démarre pour la première fois.


**Astuce :** Tu peux contourner ce problème en empêchant les obstacles d'apparaître trop près de la position de départ du joueur. Peux-tu penser à d'autres solutions ?

  --- /feedback ---

- ( ) Les obstacles apparaissent directement sous le joueur.

  --- feedback ---

Pas tout à fait. Cela peut se produire soit au début du jeu, soit lorsque de nouveaux obstacles sont ajoutés à la suite de l'augmentation du niveau de difficulté, s'ils choisissent une position proche de celle du joueur.


**Astuce :** Une solution potentielle pourrait être de rendre le joueur temporairement immunisé contre les collisions avec tous les obstacles, ou même uniquement les obstacles nouvellement créés, pendant une courte période après une augmentation de niveau. Quels problèmes le fait que l'obstacle choisisse une nouvelle position pourrait-il créer s'il était trop proche du joueur ?

  --- /feedback ---

- ( ) Les obstacles sont tous regroupés, laissant trop d'espace libre ailleurs.

  --- feedback ---

Pas tout à fait. Étant donné que la génération aléatoire peut choisir des groupes de nombres proches les uns des autres, cela peut poser problème.


**Astuce :** Une solution pourrait consister à passer à la génération semi-aléatoire - divise l'écran en morceaux et utilise des nombres aléatoires pour générer des obstacles à l'intérieur de chacun de ces morceaux. Peux-tu penser à la manière dont tu pourrais utiliser ce type de génération procédurale pour rendre ton jeu plus intéressant ou plus stimulant ?

  --- /feedback ---

--- /choices ---

--- /question ---
