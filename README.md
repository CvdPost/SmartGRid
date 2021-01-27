# SmartSplitters
## Programmeertheorie 2021
Anne Muller, Christophe van der Post en Lotte Levelt
&nbsp;
## Introductie SmartGrid
#
Groene energie is de energie van de toekomst, en zelf produceren is de mode van nu. Veel huizen hebben tegenwoordig zonnepanelen, windmolens of andere installaties om zelf energie mee te produceren. Fortuinlijk genoeg produceren die installaties vaak meer dan voor eigen consumptie nodig is. Het overschot zou kunnen worden terugverkocht aan de leverancier, maar de infrastructuur (het grid) is daar veelal niet op berekend. Om de pieken in consumptie en produktie te kunnen managen moeten er batterijen geplaatst worden.
## Opdracht
#
Voor de opdacht is er data beschikbaar van 3 verschillende wijken/districten die in onze case worden omschreven als 'grids'. Op elke grid bevinden zich 5 batterijen en 150 huizen. Voor elk huis worden de (x,y)-coordinaten gegeven en de max-output van een huis. Voor elke batterij worden ook de (x,y)-coordinaten gegeven en een max-capaciteit. Het doel van de opdracht is om de elk huis te verbinden aan een batterij en de kosten te minimaliseren. Een huis wordt via een kabel verbonden aan een batterij, een stuk kabel kost 9 euro per grid-segment. Ook zijn er vaste kosten van 5000 euro per batterij. In requirements.txt kunnen de requirements gevonden worden die niet overschreden mogen worden tijdens de realisatie van het doel.
&nbsp;
## Voorbeeld Grid
#
<img src="docs/grid_district_1.png" style="width: 400px">

&nbsp;
## De Algoritmes
#

### Randomise Algoritme (baseline)
De randomise functie legt random verbindingen tussen huizen en kabels. Dit betekent dat altijd als het algoritme wordt gerund, het algoritme bijna altijd een andere uitkomst genereerd. De randomise functie bestaat uit twee delen. In het eerste deel itereren we over alle huizen in de grid (District #), kiezen we een random batterij gekozen uit de vijf mogelijkheden (met behulp van Python’s random.choice functie uit de random module) en kijken we of er een connectie gemaakt kan worden tussen het huis en de batterij. Als er een connectie mogelijk is wordt het huis toegevoegd aan de connectielijst van de batterij. Als er geen connectie mogelijk is omdat anders de capaciteit van de batterij overschreden wordt, wordt het huis aan een lijst ‘resthuizen’ toegevoegd. In het tweede deel van de functie itereren we over de resthuizen en wordt er weer een random batterij gekozen. En begint het process van het toewijzen van huizen aan batterijen opnieuw. Als er geen huizen meer in de leftover lijst staan returnt de functie True en zijn alle huizen aan de batterijen verbonden.
&nbsp;
### Hillclimber Algoritme
Het tweede algoritme betreft een iteratief algoritme, namelijk de Hillclimber. Het algoritme begint met een willekeurige start staat, kiest dan twee random batterijen en 2 random huizen uit de connectielijst van de batterijen. Er wordt dan gechekt of de capaciteit van de batterijen niet wordt overschreden als er geswitcht wordt en of de lengte van huis tot batterij korter is als er geswitched wordt. Als er aan deze twee condities is voldaan, worden de huizen geswitched en als dit lagere kosten opleveert wordt deze nieuwe staat opgeslagen. Het Hillclimber algoritme is gebaseerd op het voorbeeld van Quinten van der Post en Wouter Vrielink.
&nbsp;
### Depth-First Algoritme
Het Depth First algoritme maakt gebruik van een stack (ofwel LIFO), om een oplossing te genereren.
Dit gebeurt op een willekeurige manier omdat we niet een voorkeur geven aan de verbinding die een huis maakt met een batterij. Met het greedy algoritme geven wij een voorkeur mee.
Het Depth First algoritme is geprogrammeerd op basis van het voorbeeld zoals gedemonstreerd in het Live Coding college van Quinten van der Post en Wouter Vrielink.2
&nbsp;
### Greedy Algoritme
Het greedy algoritme is gebaseerd op de depth first methode. Echter in de greedy is de voorkeur gegeven aan de state waar het huis het dichtsbij de batterij staat. Dit doen we door wanneer we de children states maken deze te sorteren van langeste afstand tot kortste afstand zodat met de LIFO methode de korste afstand altijd als eerste gepakt word.
&nbsp;
## Aan de slag
#
### Vereisten
Deze codebase is volledig geschreven in Python 3.7. Om de code succesvol te draaien is de volgende istallatie nodig:
```
pip3 install bokeh
``` 
### Gebruik
Om de algoritme te runnen moet je in de terminal het volgende command invoeren: 
```
python3 main.py
```
### Structuur
De hierop volgende lijst beschrijf de belangrijkste mappen en files in het project, en waar je ze kan vinden:
- **/code**: bevat alle code van dit project
    - **/code/algorithms**: bevat code voor de algoritmes
        - **/code/algorithms/future_work**: bevat code die nog niet bug free is
    - **/code/classes**: bevat de benodigde classes voor deze case
    - **/code/visualisation**: bevat de de bokeh code voor het maken van een visualisatie van de case
- **/data**: bevat de verschillende data bestanden om de grids te vullen met huizen en batterijen
- **/results**: bevat de bestanden waar de resultaten in worden opgeslagen
    - **/results/data**: bevat de gegenereerde data in een .json file
    - **/results/visual**: bevat de html bestanden van de visualisatie