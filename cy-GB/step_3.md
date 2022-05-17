## Creu rhwystrau

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Ewch ati i greu'r rhwystrau bydd angen eu hosgoi i barhau i chwarae'r gêm.
</div>
<div>

![Enghraifft o brosiect sgïo gyda choed fel rhwystrau](images/obstacles.png){:width="300px"}

</div>
</div>

### Dechreuwch gydag un rhwystr

Fe allwch chi wneud rhwystrau yn yr un modd ag y gwnaethoch chi eich chwaraewr. Sut mae'r rhwystrau'n cyd-fynd â'ch thema?

Byddwch chi'n defnyddio dolen `for` i wneud llawer o gopïau felly dim ond un rhwystr mae angen i chi ei wneud neu ei ddewis.

--- task ---

Diffiniwch swyddogaeth `llunio_rhwystrau()`:

--- code ---
---
language: python
filename: main.py - llunio_rhwystrau()
---

def llunio_rhwystrau():
   rh_x = width/2
   rh_y = height/2
   text('🌵', rh_x, rh_y) #Disodli gyda'ch rhwystr

--- /code ---

Ychwanegwch god at `draw()` i alw `llunio_rhwystrau()` bob ffrâm.

--- code ---
---
language: python
filename: main.py - draw()
---

def draw():
    diogel = color(200, 100, 0) #Ychwanegwch liw eich thema
    background(diogel)  
    llunio_rhwystrau() #Cyn llunio'r chwaraewr
    llunio_chwaraewr()

--- /code ---

--- /task ---

--- task ---

**Dewis:** Sut mae eich rhwystr yn edrych? Fe allai eich rhwystr fod:
+ Yn ddelwedd wedi'i darparu yn y prosiect dechreuol
+ Yn emoji 🌵 neu'n destun
+ Wedi'i lunio gan ddefnyddio cyfres o siapiau

--- collapse ---
---
title: Defnyddio delwedd ddechreuol
---

Cliciwch yr eicon **manage images**.

![Yr eicon delweddau yng nghornel dde uchaf yr ardal cod.](images/manage-images.png)

Bydd delweddau yn y prosiect dechreuol wedi'u dangos yn y rhestr `Image library`.

![Y llyfrgell ddelweddau gyda rhestr o'r delweddau wedi'u cynnwys.](images/starter-images.png)

Gwnewch nodyn o enw'r ddelwedd rydych chi am ei defnyddio.

Llwythwch y ddelwedd i'r swyddogaeth `setup()`.

--- code ---
---
language: python
filename: main.py - setup()
---

def setup():
    size(400, 400)
    chwaraewr = load_image('skiing.png') #Llwytho eich delwedd
    rhwystr = load_image('rocket.png') #Llwytho eich delwedd

--- /code ---

Galwch `image()` a'i osod fel un gyffredinol (global) yn y swyddogaeth `llunio_rhwystrau()`.

--- code ---
---
language: python
filename: main.py - llunio_rhwystrau()
---

def llunio_rhwystrau():
   rh_x = width/2
   rh_y = height/2
   
   global rhwystr
   
   image(rhwystr, rh_x, rh_y, 30, 30) #Newidiwch y maint i gyd-fynd â'ch thema

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Defnyddio cymeriadau emoji
---

Fe allwch chi ddefnyddio cymeriadau emoji yn y swyddogaeth p5 `text()` i gynrychioli eich rhwystrau.

Dyma enghraifft:

--- code ---
---
language: python
filename: main.py - setup()
---

def setup():
  size(400, 400)
  text_size(40) #Rheoli maint yr emoji 
  text_align(CENTER, TOP) #Lleoli o amgylch y canol

--- /code ---

--- code ---
---
language: python
filename: main.py - llunio_rhwystrau()
---

def llunio_rhwystrau():
  rh_x = width/2
  rh_y = height/2
  text('🌵', rh_x, rh_y)

--- /code ---

--- /collapse ---

[[[processing-python-text]]]

[[[generic-theory-simple-colours]]]

[[[processing-python-ellipse]]]

[[[processing-python-rect]]]

[[[processing-python-triangle]]]

[[[processing-tint]]]

[[[processing-stroke]]]

**Cyngor:** Fe allwch chi ddefnyddio nifer o siapiau syml yn yr un swyddogaeth i greu rhwystr mwy cymhleth.

--- collapse ---
---
title: Llunio rhwystr gan ddefnyddio nifer o siapiau
---

![desc](images/tree_obstacle.png)

--- code ---
---
language: python
filename: main.py - llunio_rhwystrau()
---

def llunio_rhwystrau():
    rh_x = width/2
    rh_y = height/2
    #Llunio coeden bîn
    no_stroke()
    fill(0,255,0) #Gwyrdd i'r nodwyddau
    triangle(rh_x + 20, rh_y + 20, rh_x + 10, rh_y + 40, rh_x + 30, rh_y + 40)
    triangle(rh_x + 20, rh_y + 30, rh_x + 5, rh_y + 55, rh_x + 35, rh_y + 55)
    triangle(rh_x + 20, rh_y + 40, rh_x + 0, rh_y + 70, rh_x + 40, rh_y + 70)
    fill(150,100,100) # Brown i'r boncyff
    rect(rh_x + 15, rh_y + 70, 10, 10)

--- /code ---

--- /collapse ---

--- /task ---

### Gwneud i'ch rhwystr symud

--- task ---

Nawr, ychwanegwch god i gynyddu safle `y` y rhwystr ym mhob ffrâm, a'i gael i amlapio pan fydd yn cyrraedd y gwaelod i greu effaith rhwystr arall.

Mae'r newidyn p5 `frame_count` yn dechrau cyfri'r fframiau pan fyddwch chi'n clicio rhedeg.

Mae `rh_y %= height` yn gosod y safle `y` ar gyfer y gweddill pan gaiff ei rannu â `height`. Gyda `height` o '400', bydd hyn yn troi `401` yn `1` felly pan fydd y rhwystrau'n diflannu oddi ar waelod y sgrin, mae'n ailymddangos ar y brig.

--- code ---
---
language: python
filename: main.py - llunio_rhwystrau()
---

def llunio_rhwystrau():
   rh_x = width/2
   rh_y = height/2 + frame_count #Cynyddu bob ffrâm
   rh_y %= height #Amlapio
   text('🌵', rh_x, rh_y) #Disodli gyda'ch rhwystr

--- /code ---

--- /task ---

### Rhwystrau di-ri

Fe allech chi lunio llawer o gopïau o'ch rhwystr mewn gwahanol safleoedd dechreuol ond mae hynny'n gryn dipyn o waith. Dewch i ni ddefnyddio llwybr byr.


<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;"> 
Mae <span style="color: #0faeb0">**cynhyrchu gweithdrefnol**</span> yn cael ei ddefnyddio wrth greu bydoedd mewn gemau, rhwystrau a golygfeydd ffilmiau i greu natur ar hap ond gyda rheolau penodol ar waith hefyd. Mae <span style="color: #0faeb0">seed</span> yn golygu eich bod yn gallu cynhyrchu'r un canlyniadau bob tro rydych chi'n defnyddio'r un dosbarthiad.</p>

--- task ---

Mae'r cod hwn yn defnyddio dolen `for` gyda `randint()` i ddewis safleoedd rhwystrau i chi. Mae galw'r swyddogaeth `seed()` ar hap yn gyntaf yn golygu byddwch chi'n cael yr un rhifau ar hap bob amser. Mae hyn yn golygu na fydd y rhwystrau'n neidio o gwmpas bob ffrâm a'ch bod yn gallu newid y dosbarthiad nes eich bod yn cael un sy'n lleoli'r rhwystrau'n deg.

--- code ---
---
language: python
filename: main.py - llunio_rhwystrau()
---

def llunio_rhwystrau():
  
  seed(12345678) #Unrhyw rif yn iawn
  
  for i in range(6):  
    rh_x = randint(0, height)
    rh_y = randint(0, height) + frame_count
    rh_y %= height
    text('🌵', rh_x, rh_y) #Disodli gyda'ch rhwystr

--- /code ---

Gwybodaeth ddefnyddiol:

[[[using-seed-in-python]]]

[[[generic-python-for-loop-repeat]]]

--- /task ---

--- collapse ---
---
title: Rhybudd epilepsi
---

Mae profi eich rhaglen yn gallu achosi ffit i bobl ag epilepsi ffotosensitif. Os oes gennych chi epilepsi ffotosensitif neu'n teimlo gallech chi fod yn dueddol i gael ffit, peidiwch â rhedeg eich rhaglen. Yn hytrach, fe allwch chi wneud y canlynol:
- Gwneud yn siŵr eich bod wedi ychwanegu'r llinell cod `seed()` i sicrhau nad yw eich rhwystrau'n neidio o gwmpas
- Gofyn i rywun ei rhedeg ar eich rhan
- Symud ymlaen a chwblhau'r prosiect, gan ofyn i rywun redeg y prosiect i chi ar y diwedd er mwyn i chi allu difa chwilod
- Newid y gyfradd fframiau cyn rhedeg eich rhaglen drwy ychwanegu `frame_rate(1)` ar ddechrau `setup()` — fe allwch chi dynnu hwn ar ôl cadarnhau nad oes chwilen

--- /collapse ---

--- task ---

**Profi:** Rhedwch eich rhaglen ac fe ddylech chi weld nifer o wrthrychau ar y sgrin, yn amlapio pan fyddan nhw'n cyrraedd y gwaelod.

Newidiwch eich cod nes eich bod yn fodlon ar y rhwystrau sydd gennych chi. Fe allwch chi:

+ Newid y dosbarthiad i roi rhwystrau mewn gwahanol safleoedd dechreuol
+ Newid sawl gwaith mae'r ddolen yn ailadrodd i gael nifer gwahanol o rwsytrau
+ Addasu maint y rhwystrau

**Cyngor:** Gwnewch yn siŵr ei bod yn bosib osgoi eich rhwystrau ond nad oes llwybr hawdd drwy eich gêm.

--- /task ---

--- task ---

**Difa chwilod:** Efallai bydd angen i chi drwsio chwilod yn eich prosiect. Dyma rai chwilod cyffredin.

--- collapse ---
---
title: Dim ond un rhwystr sy'n cael ei lunio
---

Tarwch olwg ar eich swyddogaeth sy'n llunio nifer o rwystrau:
 + Gwnewch yn siŵr ei bod yn defnyddio dolen `for` i alw'r swyddogaeth llunio rhwystrau fwy nag unwaith
 + Gwnewch yn siŵr ei bod yn defnyddio `randint()` i newid y cyfesurynnau (x, y) mae'n eu pasio i'r swyddogaeth llunio rhwystrau
 + Gwnewch yn siŵr eich bod wedi defnyddio `rh_x` a `rh_y` fel cyfesurynnau eich rhwystr

Er enghraifft:

--- code ---
---
language: python
filename: main.py — llunio_rhwystrau()
---

def llunio_rhwystrau():

  seed(12345678)
  
  for i in range(6):  
    rh_x = randint(0, height)
    rh_y = randint(0, height) + frame_count
    rh_y %= height
    text('🌵', rh_x, rh_y) #Disodli gyda'ch rhwystr

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Mae'r rhwystrau'n newid safle bob tro mae ffrâm yn cael ei llunio
---

Gwnewch yn siŵr eich bod wedi defnyddio `seed()` tu mewn i'r swyddogaeth sy'n llunio nifer o rwystrau.

--- /collapse ---

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;"> 
Mae rhaglenwyr yn defnyddio nifer o driciau clyfar fel defnyddio'r gweithredwr `%` i wneud i wrthrychau lapio o amgylch y sgrin a'r swyddogaeth `seed()` i gynhyrchu'r un rhifau ar hap. Po fwyaf o godio rydych chi'n ei wneud, y mwyaf o driciau clyfar byddwch chi'n eu dysgu.</p>

--- save ---
