## プロジェクトをアップグレードする

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
時間があれば、プロジェクトをアップグレードしてみましょう。
</div>
<div>

![Example space project with lives.](images/example1.png){:width="300px"}

</div>
</div>

たとえばこんなアイデアがあります。

### 障害物の種類を増やす
障害物の種類を増やす方法はいくつかあります。
 - いくつかの画像、絵文字、障害物描画関数からランダムに選ぶ
 - 障害物を描くパラメータを変更して、色、形、サイズをランダムに変える
 - `frame_count`を使って、障害物の角度、色、その他の見た目の変化を追加して、障害物をアニメーション化する

### 勝ちとなる条件を追加する
プレイヤーがゲームに勝つことができるようにする方法がいくつかあります。
 - 勝ちとなるスコアに達する
 - ゲームの決まったレベルに達する

勝ちになったら、どうにかして伝える必要があります — `print()` や `text()` を使って表示し、ゲームを停止する、などです。

### プレイヤーに2つ以上のライフを与える
ゲームにライフを追加して、プレイヤーが何度か障害物にぶつかってもゲームを続けられるようにします。 This is a little trickier than just doing `lives -= 1` every time they collide with something:
 - プレイヤーはオブジェクトと接触のが複数のフレームをわたることがあるため、1回の衝突で複数のライフを失う可能性があります。これを防ぐ必要があります。
 - また、プレイヤーが残されたライフの数を知る方法が必要になります。そして、最後のライフになったことを知らせる警告のようなものも必要になります。
 - プレイヤーがそれにぶつかったときに、追加のライフがもらえるようなオブジェクトを追加してもいいでしょう。 同時にライフを差し引かないように、通常の衝突コードを変更する必要があることを忘れないでください！

Each example project in the Introduction allows you to look at the code, get ideas, and see how they work.

The "Dodge Asteroids" project below has all of these features:

**Dodge asteroids**:
<iframe src="https://editor.raspberrypi.org/en/embed/viewer/dodge-asteroids-example" width="600" height="700" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
</iframe>

You can find the Dodge asteroids project [here](https://editor.raspberrypi.org/en/projects/dodge-asteroids-example){:target="_blank"}

Take a look at some Don't collide projects created by community members in the Raspberry Pi Foundation’s [Don't collide - Community library](https://wke.lt/w/s/KobNfx){:target="_blank"}.

--- save ---
