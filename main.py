import random

# Dit is de lijst met mogelijke woorden die de computer dan kiest
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

speler_naam = input("Wat is je naam? ")
print(f"Welkom bij Galgje, {speler_naam}!")

# Functie die de galg tekent op basis van het aantal levens (0 t/m 5)
def toon_galg(levens):
    galg = [
        """
        -----

        |   |
        O   |
       /|\\  |
       / \\  |
            |
        =========
        """,  # 0 levens (volledige galg)
        """
        -----

        |   |
        O   |
       /|\\  |
       /    |
            |
        =========
        """,  # 1 leven
        """
        -----

        |   |
        O   |
       /|\\  |
            |
            |
        =========
        """,  # 2 levens
        """
        -----

        |   |
        O   |
       /|   |
            |
            |
        =========
        """,  # 3 levens
        """
        -----

        |   |
        O   |

        |   |
            |
            |
        =========
        """,  # 4 levens
        """
        -----

        |   |
            |
            |
            |
            |
        =========
        """   # 5 levens
    ]
    print(galg[levens])

opnieuw = "ja"

# Het spel wordt gespeeld zolang de speler 'ja' intypt
while opnieuw.lower() == "ja":
    print("\n=== Het spel wordt (verder) gespeeld! ===")

    gekozen_woord = random.choice(woord_lijst)
    aantal_levens = 5
    woordjes = ["_"] * len(gekozen_woord)
    foute_letters = []

    print("\n= GALGJE =")
    print("Het woord bestaat uit " + str(len(gekozen_woord)) + " letters.")

    # De game-lus voor het raden van de letters
    while aantal_levens > 0 and "_" in woordjes:
        toon_galg(aantal_levens)
        print("\nWoord:", " ".join(woordjes))

        if len(foute_letters) > 0:
            print("Foute letters:", ", ".join(foute_letters))

        letter = input("Kies een letter: ").lower()

        # Controleer of de invoer wel één letter is
        if len(letter) != 1 or not letter.isalpha():
            print("Typ alstublieft één letter in.")
            continue

        gevonden = False

        for i in range(len(gekozen_woord)):
            if gekozen_woord[i] == letter:
                woordjes[i] = letter
                gevonden = True

        if gevonden:
            print("\033[32mGoed geraden!\033[0m")
        else:
            aantal_levens -= 1
            foute_letters.append(letter)
            print("\033[31mFout geraden!\033[0m")
            print("Je hebt nog " + str(aantal_levens) + " levens.")

    # Controleer of de speler heeft gewonnen of verloren (binnen de herhalingslus)
    if "_" not in woordjes:
        print("\nGoed gedaan!")
        print("Je hebt het woord geraden:", gekozen_woord)
    else:
        toon_galg(0)
        print("\nHelaas, je hebt verloren.")
        print("Het woord was:", gekozen_woord)

    # Vraag IN de lus of de speler nog een keer wil spelen
    opnieuw = input("\nWil je het spel verder spelen ja/nee: ")

# Zodra de speler 'nee' (of iets anders dan ja) typt, stopt de code hier
print("\nHet spel is gestopt! Bedankt voor het spelen.")
