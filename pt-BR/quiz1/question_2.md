--- question ---
---
legend: Pergunta 2 de 3
---

Neste projeto, você usou a geração procedural — fazendo com que o computador criasse e colocasse partes do seu mundo para você. Embora isso economize muito tempo, principalmente se você estiver criando níveis muito grandes, isso pode criar alguns problemas. Quais desses problemas você deve observar ao testar sua geração procedural?

--- choices ---

- (x) Todos eles

  --- feedback ---

Correto! Tudo isso pode acontecer ao usar a geração procedural. Você pode adicionar mais código para verificar e solucionar esses problemas ou tentar diferentes sementes até encontrar uma que funcione.

  --- /feedback ---

- ( ) Podem ser gerados obstáculos que deixam o jogador sem rota para desviar.

  --- feedback ---

Não exatamente. Isso pode acontecer com obstáculos gerados proceduralmente, principalmente quando o jogo começa.


**Dica:** Você pode contornar esse problema evitando que os obstáculos apareçam muito perto da posição inicial do jogador. Você consegue pensar em outras soluções?

  --- /feedback ---

- ( ) Obstáculos aparecem diretamente abaixo do jogador.

  --- feedback ---

Não exatamente. Isso pode acontecer tanto no início do jogo, quanto quando novos obstáculos são adicionados como resultado do aumento do nível de dificuldade, caso eles escolham uma posição próxima à do jogador.


**Tip:** A potential solution might be to make the player temporarily immune to collision with all obstacles, or even only newly created obstacles, for a short time after a level increase. Que problemas pode criar o obstáculo que escolhe uma nova posição se estiver muito perto do jogador?

  --- /feedback ---

- ( ) Os obstáculos estão todos agrupados, deixando muito espaço aberto em outros lugares.

  --- feedback ---

Não exatamente. Because random generation can choose groups of numbers that are close together, this can be a problem.


**Dica:** Uma solução pode ser mudar para geração semi-aleatória — divida a tela em pedaços e use números aleatórios para gerar obstáculos dentro de cada um desses pedaços. Você consegue pensar em como poderia usar esse tipo de geração procedural para tornar seu jogo mais interessante ou mais desafiador?

  --- /feedback ---

--- /choices ---

--- /question ---
