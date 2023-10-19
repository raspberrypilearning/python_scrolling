## 障害物を作る

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
ゲームに出てくる障害物を作成します。この障害物を避け続けることでゲームを続けられます。
</div>
<div>

![木の障害物があるスキープロジェクトの例](images/obstacles.png){:width="300px"}

</div>
</div>

### 1つの障害物から始める

プレイヤーを作ったのと同じ方法で障害物を作ることができます。 障害物はあなたのテーマにふさわしいですか？

コピーをたくさん作るのに `for` ループを使うので、障害物は1つ作るか選ぶだけで済みます。

--- task ---

`draw_obstacles()` 関数を定義します。

--- code ---
---
def draw_obstacles():
line_highlights: 4
---

def draw_obstacles(): ob_x = width/2 ob_y = height/2 text('🌵', ob_x, ob_y) #作ったか選んだ障害物にしてください

--- /code ---

`draw()`にコードを追加して、フレームごとに`draw_obstacles()`を呼び出すようにします。

--- code ---
---
filename: main.py - draw()
line_highlights: 5
---

def draw(): safe = color(200, 100, 0) #テーマの色 background(safe)  
draw_obstacles() #プレーヤーを描く前に draw_player() --- /code ---

--- /code ---

--- /task ---

--- task ---

**選択：** 障害物はどのように見えますか？ 障害物は次のどれかです。
+ スタータープロジェクトで用意された画像
+ 絵文字🌵またはテキスト
+ さまざまな形を使って描いたもの

--- collapse ---
---
title: スタータープロジェクトの画像を使う
---

スタータープロジェクトで用意された画像は、 `Image Library` のリストに出て来ます。

![The Image gallery displaying the included images.](images/starter-images.png)

使いたい画像の名前をメモします。

`setup()` 関数で画像を読み込みます.

--- code ---
---
language: python filename: main.py - setup() line_numbers: true line_number_start: 9
line_highlights: 12
---

def setup(): size(400, 400) player = load_image('skiing.png') #選んだ画像 obstacle = load_image('rocket.png') #選んだ画像

--- /code ---

Find the line `# Keep this to run your code`. `draw_obstacle()` 関数で`image()` を呼び出し、 obstacle変数をグローバルに設定します。

--- code ---
---
language: python
filename: main.py - draw_obstacles()
---

def draw_obstacles(): ob_x = width/2 ob_y = height/2

    image(obstacle, ob_x, ob_y, 30, 30) #テーマに合わせてサイズを変更

--- /code ---

--- /collapse ---

--- collapse ---
---
title: 絵文字を使用する
---

p5の `text()` 関数で絵文字を使うことができるので、障害物を絵文字で表現することができます。

次に例を示します：

--- code ---
---
language: python
filename: main.py - setup()
---

def setup(): size(400, 400) text_size(40) #絵文字の大きさ text_align(CENTER, TOP) #真ん中に置く

--- /code ---

Find the line `# Keep this to run your code`. Before that line, define a new `draw_obstacles()` function.

--- code ---
---
language: python
filename: main.py - draw_obstacles()
---

def draw_obstacles(): ob_x = width/2 ob_y = height/2 text('🌵', ob_x, ob_y)

--- /code ---

--- /collapse ---

[[[processing-python-text]]]

[[[generic-theory-simple-colours]]]

[[[processing-python-ellipse]]]

[[[processing-python-rect]]]

[[[processing-python-triangle]]]

[[[processing-tint]]]

[[[processing-stroke]]]

**ヒント：** 一つの関数の中で、いくつかの単純な図形を使用して、より複雑な障害物を作ることができます。

--- collapse ---
---
title: いくつかの図形を使って障害物を描く
---

![A tree drawn with green triangles for the body and a brown rectangle for the trunk](images/tree_obstacle.png)

--- code ---
---
language: python
filename: main.py - draw_obstacles()
---

def draw_obstacles(): ob_x = width/2 ob_y = height/2 #モミの木を描く no_stroke() fill(0,255,0) #葉の部分は緑 triangle(ob_x + 20, ob_y + 20, ob_x + 10, ob_y + 40, ob_x + 30, ob_y + 40) triangle(ob_x + 20, ob_y + 30, ob_x + 5, ob_y + 55, ob_x + 35, ob_y + 55) triangle(ob_x + 20, ob_y + 40, ob_x + 0, ob_y + 70, ob_x + 40, ob_y + 70) fill(150,100,100) # 幹は茶色 rect(ob_x + 15, ob_y + 70, 10, 10)

--- /code ---

--- /collapse ---

--- /task ---

### 障害物を動かす

--- task ---

次に、フレームごとに障害物の `y` の位置を増やすコードを追加します。

p5の`frame_count`変数は、実行ボタンをクリックするとフレームのカウントを始めます。

`ob_y ％= height` は `ob_y`を`height`(画面の高さ) で割った余りが `height`が「400 」の場合、この計算は`401`を`1`に変えるため、障害物が画面の下部から外れると、上部に再び表示されます。

--- code ---
---
language: python
filename: main.py - draw_obstacles()
---

def draw_obstacles(): ob_x = width/2 ob_y = height/2 + frame_count #フレームごとに増やす ob_y %= height #下に外れたら上から出てくるように text('🌵', ob_x, ob_y) #作ったか選んだ障害物にしてください

--- /code ---

--- /task ---

### たくさんの障害物

さまざまな場所に障害物のコピーをたくさん描くことができますが、それはかなりの作業です。 手っ取り早い方法でやりましょう。

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;"> 
<span style="color: #0faeb0">**手続き型生成**</span>とは、ゲームワールド、障害物、および映画のシーンを作り出す使われる手法で、ランダムであるが、ある一定のルールに基づいてそれらを作り出すものです。 <span style="color: #0faeb0">seed(シード)</span> は、同じseed(シード) を使用するたびに同じ結果を生成できることを意味します。</p>

--- task ---

このコードでは、`for`ループと `randint()` を使って、障害物の位置を決めています。 最初にランダムの`seed()` 関数を呼び出すことで、何度やっても同じ乱数が得られます。 これによって、障害物がフレームごとにあちこちに現れることがなくなり、障害物がうまく出てくるタネを見つけるまでいくらでもタネを変更できるようになります。

--- code ---
---
language: python
filename: main.py - draw_obstacles()
---

seed(12345678) #どんな数でもよい

    for i in range(6):<br x-id="2" />
        ob_x = randint(0, height)
        ob_y = randint(0, height) + frame_count
        ob_y %= height
        text('🌵', ob_x, ob_y) #作ったか選んだ障害物にしてください

--- /code ---

役立つ情報：

[[[using-seed-in-python]]]

[[[generic-python-for-loop-repeat]]]

--- /task ---

--- collapse ---
---
title: てんかんの警告
---

プログラムをテストすると、光過敏性てんかんのある人に発作を引き起こす可能性があります。 光過敏性てんかんを患っている方や発作を起こしやすいと感じている方は、プログラムを実行しないでください。 代わりに、次のことができます。
- 障害物があちこちに現れないように `seed ()` のコード行追加したことを確認してください
- プログラムの実行を誰かに頼んでください
- 先に進めてプロジェクトを完了し、最後に誰かにプロジェクトを実行してもらい、デバッグできるようにしてください
- プログラムを実行する前に、`setup()` の最初のところに `frame_rate(1)` を追加して、フレームレートを変更します。

```python
run(frame_rate = 10)
```
You can alter the speed of the game by changing `10` to a higher or lower value.

--- /collapse ---

--- task ---

**テスト：** プログラムを実行すると、画面にたくさんの障害物が表示され、一番下に到達すると上に回り込んでまた現れます。

障害の出来具合に満足するまでコードの変更を繰り返します。 やり方は以下のとおりです。

+ 乱数のタネを変更して、色々な所から障害物が現れるようにします
+ 障害物の数が変わるまでのループ回数を変更します
+ 障害物のサイズを調整します

**ヒント：** 障害物を避けることができて、簡単には通り抜けられないことを確認してください。

--- /task ---

--- task ---

**デバッグ：** プロジェクトに修正が必要なバグが見つかる場合があります。 一般的なバグは次のとおりです。

--- collapse ---
---
title: 障害物が1つしか現れない
---

障害物をたくさん描く関数を確認してください。
 + 障害物を描く関数を2回以上呼び出すために、 `for` ループを使っていることを確認してください
 + 障害物を描く関数に渡す(x, y) 座標を変えるのに、`randint()` を使っていることを確認してください
 + 障害物の座標として `ob_x` と `ob_y` を使っていることを確認してください

例えば:

--- code ---
---
language: python
filename: main.py — draw_obstacles()
---

def draw_obstacles():

    for i in range(6):<br x-id="2" />
        ob_x = randint(0, height)
        ob_y = randint(0, height) + frame_count
        ob_y %= height
        text('🌵', ob_x, ob_y) #作ったか選んだ障害物にしてください

--- /code ---

--- /collapse ---

--- collapse ---
---
title: フレームが描かれるたびに障害物の位置が変わります
---

`seed()`が、たくさんの障害物を描く関数の中に入っていることを確認してください。

--- /collapse ---

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;"> 
プログラマーは、 `%`演算子を使ってオブジェクトを画面から出てすぐにまた現れるようにしたり、 `seed()`関数を使って同じ乱数を生成したりするなど、多くの巧みなトリックを使っています。 コーディングをすればするほど、より巧みなトリックを身につけることができます。</p>

--- save ---
