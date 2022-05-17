## Beth nesaf?

Da iawn, rydych chi wedi gwneud gêm!  Amser myfyrio nawr — mae myfyrio'n rhan bwysig o ddysgu oherwydd mae'n helpu i wneud cysylltiadau newydd yn eich ymennydd.

Atebwch y tri chwestiwn isod i fyfyrio ar yr hyn rydych chi wedi'i ddysgu.

Ar ôl bob cwestiwn, pwyswch **cyflwyno**. Byddi di'n cael dy dywys i'r ateb cywir. Galli di wneud hyn gymaint ag y mynni.

Mwynha!

--- question ---
---
legend: Cwestiwn 1 o 3
---

Rydych chi wedi defnyddio llawer o ddatganiadau `if` i reoli ymddygiad eich gêm. Mae'n bosib bod gan rai ohonyn nhw amodau mwy cymhleth, gan ddefnyddio `and` i wneud mwy nag un prawf ar unwaith. Pe baech chi'n rhedeg y darn canlynol o god amodol, pa allbwn fyddech chi'n ei ddisgwyl?

```python
score = 5000
lives = 2

if score >= 5000 and lives >= 3:
  print('Hedfan heb ei ail!')

if score >= 5000: 
  print('Ti\'n gwneud yn dda!')
  if lives > 1:
    print('Dal ati!')
  else:
    print('Ond bydd yn ofalus!')

elif lives > 1:
  print('Gwthia\'n galetach!')

else:
  print('Am adre!')
```

--- choices ---

- ( )
```
Hedfan heb ei ail!
```
  --- feedback ---

Er bod `sgor >= 5000` yn wir, ar gyfer amod `and` mae'n rhaid i'r ddwy ran fod yn wir, ac nid yw `bywydau >= 3` yn wir.

  --- /feedback ---

- (x)
```
Ti'n gwneud yn dda!
Dal ati!
```
  --- feedback ---

Cywir — Mae `sgor >= 5000` yn wir fel y mae `bywydau > 1` ar y datganiad `if` wedi'i nythu.

  --- /feedback ---

- ( )
```
Ti'n gwneud yn dda!
```
  --- feedback ---

Agos, ond nid `sgor >= 5000` yw'r unig amod byddai'r rhaglen yn ei ganfod yn wir wrth redeg.

  --- /feedback ---

- ( )
```
Gwthia'n galetach!
```
  --- feedback ---

Er bod `bywydau > 1` yn wir, dim ond y cod tu mewn i'r amod gwir cyntaf mewn datganiad `if`/`elif`/`else` sy'n cael ei weithredu, ac nid `bywydau > 1` yw'r amod cyntaf sy'n wir.

  --- /feedback ---

--- /choices ---

--- /question ---
