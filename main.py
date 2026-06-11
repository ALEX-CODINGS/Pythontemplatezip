import random

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


gekozen_woord = random.choice(woord_lijst)

aantal_levens = 5

woordjes = ["_"] * len(gekozen_woord)


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



print("= GALGJE =")
print("Je hebt nog " + str(aantal_levens) + " levens.")
print("Het woord bestaat uit " + str(len(gekozen_woord)) + " letters.")


while aantal_levens > 0 and "_" in woordjes:

    toon_galg(aantal_levens)

    print("\nWoord:", " ".join(woordjes))

    if len(foute_letters) > 0:
        print("Foute letters:", ", ".join(foute_letters))


    letter = input("Kies een letter: ").lower()

    gevonden = False


    for i in range(len(gekozen_woord)):
        if gekozen_woord[i] == letter:
            woordjes[i] = letter
            gevonden = True


    if gevonden:
        print("Goed geraden!")
    else:
        aantal_levens -= 1
        foute_letters.append(letter)
        print("Fout geraden!")
        print("Je hebt nog " + str(aantal_levens) + " levens.")


if "_" not in woordjes:
    print("\nGoed gedaan!")
    print("Je hebt het woord geraden:", gekozen_woord)
else:
    toon_galg(0)
    print("\nHelaas, je hebt verloren.")
    print("Het woord was:", gekozen_woord)