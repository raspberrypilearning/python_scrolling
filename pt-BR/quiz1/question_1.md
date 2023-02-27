## Teste rápido

Responda as três perguntas. Há dicas para guiá-lo para a resposta correta.

Depois de responder a cada pergunta, clique em **Verificar resposta**.

Divirta-se!

--- questão ---
---
legenda: Pergunta 1 de 3
---

Você usou muitas declarações `if` para controlar o comportamento do seu jogo. Algumas delas podem ter condições mais complexas, usando `and` para fazer vários testes de uma vez. Se você executasse o seguinte trecho de código condicional, que resultado você esperaria?

```python
pontos = 5.000
vidas = 2

se pontos >= 5.000 e vidas >= 3:
  print('Ótimo vôo!')

if score >= 5000: 
  print('Indo bem!')
  if lives > 1:
    print('Continue!')
  else:
    print('Mas tenha cuidado!')

elif vive > 1:
  print('Se esforce mais!')

else:
  print('Direto para a base!')
```

-- opções --

- ( )
```
Ótimo vôo!
```
  --- feedback ---

Enquanto `score >= 5000` for verdadeiro, para uma condição `and` as duas partes tem de ser verdade, e `lives>= 3` é falso.

  --- /feedback ---

- (x)
```
Indo bem!
Continue!
```
  --- /feedback ---

Isso está correto — `score >= 5000` é verdadeiro, assim como `lives > 1` na instrução aninhada `if`.

  --- /feedback ---

- ( )
```
Indo bem!
```
  --- feedback ---

Quase, mas `score >= 5.000` não é a única condição que o programa consideraria verdadeira durante a execução.

  --- /feedback ---

- ( )
```
Força!
```
  --- feedback ---

Enquanto `lives > 1` for verdadeiro, somente o código na primeira condição verdadeira de uma instrução `if`/`elif`/`else` é executado, e `lives > 1` não é a primeira condição que é verdadeira.

  --- /feedback ---

-- /opções --

--- /questão ---
