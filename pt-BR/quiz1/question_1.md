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
pontos = 5000
vidas = 2

if pontos >= 5000 and vidas >= 3:
  print('Ótimo voo!')

if pontos >= 5000: 
  print('Indo bem!')
  if vidas > 1:
    print('Continue!')
  else:
    print('Mas tenha cuidado!')

elif vidas > 1:
  print('Se esforce mais!')

else:
  print('Vá para a base!')
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

Quase, mas `pontos >= 5000` não é a única condição que o programa consideraria verdadeira durante a execução.

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
