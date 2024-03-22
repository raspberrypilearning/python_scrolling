## Verbeter je project

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Als je tijd hebt, kunt je jouw project verbeteren.
</div>
<div>

![Voorbeeld van een project met levens.](images/example1.png){:width="300px"}

</div>
</div>

Hier zijn enkele ideeën die je zou kunnen proberen:

### Voeg veel verschillende obstakels toe
Je kunt op een paar manieren variatie aan je obstakels toevoegen:
 - Kies willekeurig tussen meerdere afbeeldingen, emoji's of functies voor het tekenen van obstakels
 - Pas willekeurig de kleur, vorm of grootte van obstakels aan door de parameters te wijzigen waarmee ze getekend worden
 - Animeer het obstakel door rotatie, een kleurverandering of een ander visueel verschil toe te voegen dat wordt bestuurd door `frame_count`

### Een winvoorwaarde toevoegen
Je kunt spelers het spel op een aantal manieren laten winnen:
 - Een winnende score behalen
 - Een bepaald level van het spel bereiken

Als ze eenmaal hebben gewonnen, moet je ze dat op de een of andere manier laten weten - misschien door `print()` of `text()` te gebruiken en dan het spel te stoppen.

### Geef spelers meer dan één leven
Voeg levens toe aan je spel, zodat spelers een paar botsingen kunnen overleven. Dit is een beetje lastiger dan gewoon `levens -= 1` te doen, elke keer dat ze ergens tegenaan botsen:
 - De speler kan meerdere frames in contact komen met een object, en dus meer dan één leven verliezen voor een enkele botsing - je moet voorkomen dat dit gebeurt
 - Je hebt ook een manier nodig waarop spelers kunnen zien hoeveel levens ze nog hebben, en misschien een soort waarschuwing die hen vertelt wanneer ze met hun laatste leven spelen
 - Je zou een object kunnen toevoegen dat, wanneer de speler ermee in botsing komt, hij een extra leven krijgt. Onthoud dat je je normale botsingscode moet wijzigen, zodat er niet tegelijkertijd een leven wordt afgetrokken!

Bij elk voorbeeldproject in de Inleiding kun je de code bekijken, ideeën opdoen en zien hoe ze werken.

Het onderstaande project "Ontwijk asteroiden" heeft al deze functies:

**Ontwijk asteroïden**:
<iframe src="https://editor.raspberrypi.org/en/embed/viewer/dodge-asteroids-example" width="600" height="700" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
</iframe>

Je kunt het Ontwijk-asteroïdenproject [hier vinden](https://editor.raspberrypi.org/en/projects/dodge-asteroids-example){:target="_blank"}

Bekijk enkele Niet botsen-projecten die zijn gemaakt door communityleden in [Don't Collide - Communitybibliotheek](https://wke.lt/w/s/KobNfx){:target="_blank"} van de Raspberry Pi Foundation.

--- save ---
