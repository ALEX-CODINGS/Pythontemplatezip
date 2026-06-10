
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
print( "je hebt nog "+ str(aantal_levens)+ " levens over om het woord te raden")
print("de woord lengte is " + str(len(gekozen_woord)))
#de computer vraagt de gebruiker om een letter te in te voeren.
letter = input("kies een letter:")

#lijst met streepjes defineren
woordjes = ["_"] * len(gekozen_woord)

#zorgt ervoor dat de letter op de juiste plek komt
for i in range(len(gekozen_woord)):
    if gekozen_woord[i] == letter:
        woordjes[i] = letter
        print("je hebt een letter goed geraden")
else:
    aantal_levens -= 1
    print("Fout geraden!")
    print("Je hebt nog", aantal_levens, "levens over.")
if "_" not in woordjes:
        print("goed gedaan! Je hebt het woord geraden!:", gekozen_woord)
else:
        print("Game over!")
        print("Het woord was:", gekozen_woord) 
#printen van de juiste letter op de juiste plek.


    
   
print(" ".join(woordjes))









    

   
    











