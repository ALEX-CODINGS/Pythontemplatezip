
#lijst aan woorden om te raden.
woord_lijst = [
    "informatica",
    "informatiekunde",
    "spelletje",
    "aardigheidje",
    "scholier",
    "fotografie",
    "waardebepaling",
    "specialiteit",
    "verzekering",
    "universiteit",
    "heesterperk"
]
#computer kiest een willekeurige woord uit de lijst die je kunt raden.
#computer gaat langs de lijst en kiest met een random functie een willekeurige woord. en slaat die op in een variabele.
import random
gekozen_woord = random.choice(woord_lijst)
#de computer geeft de gebruiker 5 levens.
aantal_levens = 5
print( "je hebt nog "+ str(aantal_levens)+ "levens over om het woord te raden")
print("de woord lengte is" + (len(gekozen_woord))
#de computer vraagt de gebruiker om een letter te in te voeren.
print = input("kies een letter:")












