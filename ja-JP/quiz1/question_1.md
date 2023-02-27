## Quick quiz

Answer the three questions. 正しい答えが表示されます。

各質問の後、**答えを確認する**を押してください。

お楽しみください!

--- question ---
---
legend: 質問1/3
---

ゲームの動きを制御するために、多くの `if` ステートメントを使いました。 中には、 `and` を使って一度にいくつもの条件を調べるなど、より複雑な条件を持ったものもありました。 次の条件分岐コードを動かした場合、出力はどのようになると思いますか？

```python
score = 5000
lives = 2

if score >= 5000 and lives >= 3:
  print('素晴らしい飛行です!')

if score >= 5000: 
  print('よくできました!')
  if lives > 1:
    print('どんどん行きましょう!')
  else:
    print('でも気をつけてください!')

elif lives > 1:
  print('がんばりましょう!')

else:
  print('基地に向かいましょう!')
```

--- choices ---

- ( )
```
素晴らしい飛行です！
```
  --- feedback ---

`score >= 5000` は真ですが、 `and` 条件では両方の条件が真でなければならず、 `lives >= 3` は偽です。

  --- /feedback ---

- (x)
```
よくできました!
どんどん行きましょう！
```
  --- feedback ---

ふりかえり

  --- /feedback ---

- ( )
```
よくできました!
```
  --- feedback ---

がんばりましょう！

  --- /feedback ---

- ( )
```
がんばりましょう！
```
  --- feedback ---

以下の3つの質問に答えて、学んだことをふりかえってみましょう。

  --- /feedback ---

--- /choices ---

--- /question ---
