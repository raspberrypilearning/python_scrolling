## Ulepsz swój projekt

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Jeśli masz czas, możesz ulepszyć swój projekt.
</div>
<div>

![przykład projektu kosmicznego z życiami.](images/przykład1.png){:width="300px"}

</div>
</div>

Oto kilka pomysłów, które możesz wypróbować:

### Uwzględnij różne przeszkody
Możesz dodać różnorodność do swoich przeszkód na kilka sposobów:
 - Losowo wybieraj spośród wielu obrazów, emotikonów lub funkcji rysowania przeszkód
 - Losowo dostosuj kolor, kształt lub rozmiar przeszkód, zmieniając parametry, które je rysują
 - Animuj przeszkodę, dodając obrót, zmianę koloru lub inną różnicę wizualną kontrolowaną przez `_`

### Dodaj warunek wygranej
Gracze mogą wygrać grę na kilka sposobów:
 - Osiągnięcie zwycięskiego wyniku
 - Osiągnięcie określonego poziomu gry

Kiedy już wygrają, powinieneś im jakoś powiedzieć - może używając ` print()` lub ` text()`, a następnie zatrzymać grę.

### Daj graczom więcej niż jedno życie
Dodaj życia do swojej gry, aby umożliwić graczom przetrwanie kilku kolizji. Jest to trochę trudniejsze niż robienie ` Lives -= 1 ` za każdym razem, gdy coś zderzy:
 - Gracz może spędzić wiele klatek w kontakcie z obiektem, a więc stracić więcej niż jedno życie za pojedynczą kolizję - będziesz musiał temu zapobiec
 - Będziesz także potrzebować sposobu, aby gracze wiedzieli, ile życia pozostawili, i być może jakiegoś ostrzeżenia, które powie im, kiedy są w ostatnim życiu
 - Możesz dodać obiekt, który, gdy gracz się z nim zderzy, daje mu dodatkowe życie. Pamiętaj, że będziesz musiał zmodyfikować swój regularny kod kolizji, aby nie odejmował życia w tym samym czasie!

Każdy przykładowy projekt w części Wprowadzenie pozwala spojrzeć na kod, uzyskać pomysły i zobaczyć, jak działają.

Poniższy projekt "Dodge Asteroids" ma wszystkie te funkcje:

** Dodge **:
<iframe src="https://editor.raspberrypi.org/en/embed/viewer/dodge-asteroids-example" width="600" height="700" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
</iframe>

Możesz znaleźć projekt asteroidy Dodge [ ](https://editor.raspberrypi.org/en/projects/dodge-asteroids-example){:target="_blank"}

Spójrz na niektóre projekty nie zderzaj się z projektami stworzonymi przez członków społeczności w [ Fundacji Raspberry Pi nie zderzaj się - Biblioteka ](https://wke.lt/w/s/KobNfx){:target="_blank"}.

--- save ---
