## 衝突を検出する

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
エンドレスランナーゲームは、プレイヤーが障害物にぶつかると終了するものが多いです。
</div>
<div>

![ゲームが終了した画像](images/collision.png){:width="300px"}

</div>
</div>

では、プレーヤーが障害物とぶつかった時に反応するようにしていきましょう。

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">**衝突検出**</span> とは、コンピューターシミュレーション（ゲームであるか、アニメーションであるか、その他のものであるか）内に作られた2つのものがぶつかったかを見つけ出すことです。 これを行うには、いくつかの方法があります。たとえば、 
  - 対象となるものの位置に表示されている色がその対象物の色であるか、別のものの色であるかをチェックする。 - すべてのものの姿を追跡し、それらが重なっているかどうかをチェックする。 - 対象となるものの周囲に境界を示す点または線を作成し、それらが他の「衝突するかもしれない」ものに触れたかどうかをチェックする。
このような衝突が検出されると、プログラムは何らかの方法で反応することができます。 ビデオゲームでは、これは通常、ダメージを与える（プレイヤーが敵または障害物と衝突する場合）か、利益を与える（プレイヤーがパワーアップアイテムと衝突する場合）ためです。
</p>

--- task ---

`draw_player()` 関数で、 `collide` という変数を作成し、プレーヤーの位置の色を取得するように設定します。

--- code ---
---
language: python
filename: main.py - draw_player()
---

    collide = get(mouse_x, player_y)

--- /code ---

--- /task ---

--- task ---

if collide == safe: #背景上 image(skiing, mouse_x, player_y, 30, 30) else: #ぶつかった image(crashed, mouse_x, player_y, 30, 30)

`if colide == safe` 条件の中にプレーヤーを描くコードを移動し、 `else` ステートメントの中に、プレーヤーが衝突に反応するコードを追加します。

**選択：** プレーヤーにどう反応させますか？ こんなことができます:
+ プレーヤーの絵文字を別のものにする
+ `tint()` を使用して画像の見た目を変えることができます。 その場合、画像を描いた後に `no_tint()` を呼び出すことを忘れないでください。

--- collapse ---
---
title: 絵文字を使用する
---

p5の `text()` 関数で絵文字を使えるので、ぶつかったプレーヤーを絵文字で表すことができます。

次に例を示します：

--- code ---
---
language: python
filename: main.py - setup()
---

def setup(): size(400, 400) text_size(40) #絵文字の大きさ text_align(CENTER, TOP) #真ん中に置く

--- /code ---

--- code ---
---
language: python
filename: main.py - draw_player()
---

def draw_player(): if collide == safe: #背景上 text('🎈', mouse_x, player_y) else: #ぶつかった text('💥', mouse_x, player_y)

--- /code ---

--- /collapse ---

[[[processing-tint]]]

[[[generic-theory-simple-colours]]]

--- /task ---

--- task ---

**テスト：** 衝突が検出されること、衝突のたびに反応が起こることを確認します。

--- /task ---

--- task ---

**デバッグ：** プロジェクトに修正が必要なバグが見つかる場合があります。 一般的なバグは次のとおりです。

--- collapse ---
---
title: プレイヤーが障害物に達しても衝突が起きない
---

プレイヤーキャラクターが障害物に触れても何も起こらない場合、チェックすることがいくつかあります。

 - `draw_players()`の前に `draw_obstacles()` を呼び出していることを確認してください。 フレームで障害物を描く前に衝突をチェックしても、その時点では衝突する障害物はありません！
 - オブジェクトを描く色と、 `if` ステートメントで衝突をチェックする色が、まったく同じであることを確認してください。 どちらにも、同じ `グローバル` 変数を使用すれば確実です。
 - マウス座標の色を確認する前に、プレイヤーキャラクターを描いていますか？ もしそうなら、あなたはプレイヤーの色を取得しているだけです。 最初に色を確認**してから** プレイヤーを描く必要があります。
 - 衝突が検出されたときに、色合いを変えたり、別の画像を使ったりするなど、なにか別のことを行うコードが `else` の部分にありますか？
 - 条件が満たされたときにコードが実行されるように、 `if` ステートメントのコードを正しくインデントしましたか？

衝突をチェックするピクセルの色を出力(print) することも有効です。

```python
    print(red(collide), green(collide), blue(collide))
```

チェックするポイントの周りに円を描き、必要に応じてチェックするポイントを調整することもできます。

```python
    def draw_player():

  player_y = int(height * 0.8)
  #デバッグに有効
  #衝突をチェックするピクセルの周りに円を描く

  no_fill()
  ellipse(mouse_x, player_y, 10, 10) #衝突点の描画
  ellipse(mouse_x, player_y + 40, 10, 10)
  ellipse(mouse_x - 12, player_y + 20, 10, 10)
  ellipse(mouse_x + 12, player_y + 20, 10, 10)

  collide = get(mouse_x, player_y)
  collide2 = get(mouse_x - 12, player_y + 20)
  collide3 = get(mouse_x + 12, player_y + 20)
  collide4 = get(mouse_x, player_y + 40)

  if mouse_x < width: #スクリーンの左に外れた
    collide2 = safe

  if mouse_x > width: #スクリーンの右に外れた
    collide3 = safe

  if collide == safe and collide2 == safe and collide3 == safe and collide4 == safe:
    text('🎈', mouse_x, player_y)
  else:
    text('💥', mouse_x, player_y)
```

--- /collapse ---

--- /task ---

--- task ---

**オプション：** 現時点では、プレーヤーの1つのピクセルで衝突を検出しているだけです。 プレーヤーのエッジにある他のピクセル（下の端、左または右の端など）での衝突を検出することもできます。

--- collapse ---
---
title: いくつかのピクセルでの衝突検出
---

```python
no_fill()
  ellipse(mouse_x, player_y, 10, 10) #衝突点の描画
```

--- /collapse ---

ループを使用して、さまざまなピクセルをチェックすることもできます。 これが、ゲームで衝突を検出する仕組みです。

--- /task ---

--- save ---
