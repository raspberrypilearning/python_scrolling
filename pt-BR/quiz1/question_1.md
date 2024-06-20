## Teste rápido

Responda às três perguntas. Existem dicas para guiá-lo para a resposta correta.

Após responder cada pergunta, clique em **Ver minha resposta**.

Divirta-se!

--- question ---
---
legend: Pergunta 1 de 3
---

Você usou muitas declarações `if` para controlar o comportamento do seu jogo. Algumas delas podem ter condições mais complexas, usando `and` para fazer vários testes de uma vez. Se você executasse o seguinte trecho de código condicional, que resultado você esperaria?

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
Ótimo vôo!
```
  --- feedback ---

Enquanto `pontos >= 5000` for verdadeiro, para uma condição `and` as duas partes devem ser verdadeiras, e `vidas >= 3` é falso.

  --- /feedback ---

- (x)
```
Indo bem!
Continue!
```
  --- feedback ---

Isso está correto — `pontos >= 5000` é verdadeiro, assim como `vidas > 1` na instrução aninhada `if`.

  --- /feedback ---

- ( )
```
Indo bem!
```
  --- feedback ---

Quase, mas `pontos >= 5.000` não é a única condição que o programa consideraria verdadeira durante a execução.

  --- /feedback ---

- ( )
```
Se esforce mais!
```
  --- feedback ---

Enquanto `vidas > 1` for verdadeiro, somente o código na primeira condição verdadeira de uma instrução `if`/`elif`/`else` é executado, e `vidas > 1` não é a primeira condição que é verdadeira.

  --- /feedback ---

--- /choices ---

--- /question ---
