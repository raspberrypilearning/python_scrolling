## Canfod gwrthdrawiad

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Mae gemau rhedeg diddiwedd yn dod i ben yn aml pan fydd y chwaraewr yn taro rhwystr.
</div>
<div>

![Delwedd o gam gorffenedig.](images/collision.png){:width="300px"}

</div>
</div>

Nawr fe allwch chi osod sut bydd eich chwaraewr yn ymateb i daro rhwystr.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Ystyr <span style="color: #0faeb0">**canfod gwrthdrawiad**</span> yw pennu pan fydd dau wrthrych wedi'u creu mewn efelychiad cyfrifiadurol — gêm, animeiddiad neu rywbeth arall — yn cyffwrdd. Mae sawl ffordd o wneud hyn, er enghraifft: 
  - gwirio ai'r lliwiau sy'n ymddangos yn safle gwrthych yw lliwiau'r gwrthrych hwnnw, neu liwiau un arall
  - cadw golwg ar siâp bob gwrthrych a gwirio a yw'r siapiau hynny'n gorgyffwrdd
  - creu cyfres o bwyntiau ffin neu linellau o amgylch gwrthrych a gwirio a ydyn nhw'n dod i gysylltiad ag unrhyw wrthrychau eraill y gellir eu taro
Pan fydd gwrthdrawiad o'r fath yn cael ei ganfod, gall y rhaglen ymateb mewn rhyw ffordd. Mewn gêm fideo, fel arfer, mae hyn i ddifrodi (os yw'r chwaraewr yn taro gelyn neu berygl) neu i roi mantais (os yw'r chwaraewr yn taro adnodd nerth).
</p>

--- task ---

Yn eich swyddogaeth `llunio_chwaraewr()`, ewch ati i greu newidyn o'r enw `taro` a'i osod i gael y lliw yn safle'r chwaraewr.

--- code ---
---
language: python
filename: main.py - draw_player()
---

collide = get(mouse_x, player_y)

--- /code ---

--- /task ---

--- task ---

Ewch ati i greu amod i wirio, gan ddefnyddio `if`, a yw'r newidyn `taro` yr un fath â'r newidyn `diogel` — os felly, mae eich chwaraewr yn cyffwrdd y cefndir ac nid yw wedi taro rhwystr.

Symudwch eich cod i lunio eich chwaraewr tu mewn eich amod `if taro == diogel` ac ychwanegu cod yn y datganiad `else` i wneud i'r chwaraewr ymateb i'r gwrthdrawiad.

**Dewis:** Sut dylai eich chwaraewr ymateb? Fe allech chi:
+ Newid y ddelwedd i fersiwn `wedi_taro`
+ Defnyddio emoji gwahanol i'r chwaraewr
+ Fe allech chi ddefnyddio `tint()` i newid ymddangosiad delwedd, ond cofiwch alw `no_tint()` ar ôl llunio'r ddelwedd

--- collapse ---
---
title: Newid y ddelwedd
---

Fe allwch chi ddefnyddio delwedd wahanol i gynrychioli eich chwaraewr pan fydd yn taro rhwystr.

Dyma enghraifft:

--- code ---
---
language: python
filename: main.py - draw_player()
---

def draw_player(): player_y = int(height * 0.8)

  collide = get(mouse_x, player_y)

  if collide == safe: #On background image(skiing, mouse_x, player_y, 30, 30) else: #Collided image(crashed, mouse_x, player_y, 30, 30)

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Defnyddio cymeriadau emoji
---

Fe allwch chi ddefnyddio cymeriadau emoji yn y swyddogaeth p5 `text()` i gynrychioli eich chwaraewr sydd wedi taro.

Dyma enghraifft:

--- code ---
---
language: python
filename: main.py - setup()
---

def setup(): size(400, 400) text_size(40) #Controls the size of the emoji text_align(CENTER, TOP) #Position around the centre

--- /code ---

--- code ---
---
language: python
filename: main.py - draw_player()
---

def draw_player(): if collide == safe: #On background text('🎈', mouse_x, player_y) else: #Collided text('💥', mouse_x, player_y)

--- /code ---

--- /collapse ---

[[[processing-tint]]]

[[[generic-theory-simple-colours]]]

--- /task ---

--- task ---

**Profi:** Gwiriwch a yw gwrthdrawiad yn cael ei ganfod ac a yw'r ymateb yn digwydd bob tro.

--- /task ---

--- task ---

**Difa chwilod:** Efallai bydd angen i chi drwsio chwilod yn eich prosiect. Dyma rai chwilod cyffredin.

--- collapse ---
---
title: Does dim gwrthdrawiad pan fydd y chwaraewr yn cyrraedd rhwystr
---

Os yw eich cymeriad chwarae'n cyffwrdd rhwystr a does dim byd yn digwydd, mae ambell beth i'w gwirio:

 - Gwnewch yn siŵr eich bod yn galw `llunio_rhwystrau()` cyn `llunio_chwaraewr()`. Os byddwch chi'n gwirio am wrthdaro cyn llunio'r rhwystrau mewn ffrâm, ni fydd unrhyw rwystrau i daro mewn iddyn nhw!
 - Gwnewch yn siŵr eich bod yn defnyddio'r union un lliw wrth lunio'r gwrthrych ac yn y datganiad `if` sy'n gwirio am wrthdaro. Fe allwch chi wneud yn siŵr o hyn drwy ddefnyddio'r newidyn `global` mewn dau le.
 - Ydych chi'n llunio'r cymeriad chwarae cyn gwirio'r lliw yng nghyfesurynnau'r llygoden? Os felly, dim ond y lliwiau gan y chwaraewr fyddwch chi'n eu cael bob amser. Rhaid i chi wirio'r lliw yn gyntaf ac **wedyn** llunio'r chwaraewr.
 - Oes gennych chi god yn y rhan `else` i wneud rhywbeth gwahanol pan fydd gwrthdrawiad yn cael ei ganfod, fel rhoi arlliw neu ddefnyddio delwedd wahanol?
 - Ydych chi wedi mewnoli'r cod ar gyfer eich datganiad `if` yn gywir fel ei fod yn rhedeg pan fydd yr amod yn cael ei fodloni?

Mae printio lliw'r picsel rydych chi'n ei wirio am wrthdrawiad yn gallu bod yn ddefnyddiol:

```python
  print(red(collide), green(collide), blue(collide))
```

Fe allwch chi hefyd brintio cylch o amgylch y pwynt rydych chi'n ei wirio ac addasu'r pwynt rydych chi'n ei wirio os oes angen:

```python
  no_fill()
  ellipse(mouse_x, player_y, 10, 10) #Draw collision point
```

--- /collapse ---

--- /task ---

--- task ---

**Dewisol:** Ar hyn o bryd, dim ond canfod gwrthdrawiad ar un picsel ar eich chwaraewr ydych chi. Fe allech chi hefyd ganfod gwrthdrawiad ar bicseli eraill ar ymyl eich chwaraewr, fel y gwaelod neu'r ymylon chwith a dde.

--- collapse ---
---
title: Canfod gwrthdrawiad â mwy nag un picsel
---

```python
def draw_player():

  player_y = int(height * 0.8)
  #Useful for debugging
  #Draw circles around the pixels to check for collisions

  no_fill()
  ellipse(mouse_x, player_y, 10, 10) #Draw collision point
  ellipse(mouse_x, player_y + 40, 10, 10)
  ellipse(mouse_x - 12, player_y + 20, 10, 10)
  ellipse(mouse_x + 12, player_y + 20, 10, 10)

  collide = get(mouse_x, player_y)
  collide2 = get(mouse_x - 12, player_y + 20)
  collide3 = get(mouse_x + 12, player_y + 20)
  collide4 = get(mouse_x, player_y + 40)

  if mouse_x < width: #Off the left of the screen
    collide2 = safe

  if mouse_x > width: #Off the right of the screen
    collide3 = safe

  if collide == safe and collide2 == safe and collide3 == safe and collide4 == safe:
    text('🎈', mouse_x, player_y)
  else:
    text('💥', mouse_x, player_y)
```

--- /collapse ---

Fe allech chi hyd yn oed ddefnyddio dolen a gwirio nifer o bicseli gwahanol. Dyma sut mae canfod gwrthdrawiad yn gweithio mewn gemau.

--- /task ---

--- save ---
