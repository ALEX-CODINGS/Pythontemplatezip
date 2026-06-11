import random 
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
    "heesterperk" ]
#computer kiest een willekeurige woord uit de lijst die je kunt raden.
#computer gaat langs de lijst en kiest met een random functie een willekeurige woord. en slaat die op in een variabele.
gekozen_woord = random.choice(woord_lijst)

aantal_levens = 5

woordes = ["_"] * len(gekozen_woord)


foute_letters = []

def toon_galg(levens):
    galg = [
        """
        -----
        |   |
            |
            |
            |
            |
        =========
        """,
        """
        -----
        |   |
        O   |
            |
            |
            |
        =========
        """,
        """
        -----
        |   |
        O   |
        |   |
            |
            |
        =========
        """,
        """
        -----
        |   |
        O   |
       /|   |
            |
            |
        =========
        """,
        """
        -----
        |   |
        O   |
       /|\\  |
            |
            |
        =========
        """,
        """
        -----
        |   |
        O   |
       /|\\  |
       / \\  |
            |
        =========
        """
    ]

    print(galg[5 - levens])

print("= Galgje =")
print("je hebt nog" + str(aantal_levens) + "levens")
print("Het woord bestaat uit " + str(len(gekozen_woord)) + " letters.")









    

   
    











