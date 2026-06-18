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
# dit is de fuctie die de galg tekent hier hadden we AI gebruikt, want we wisten niet hoe we de galg moesten maken
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


opnieuw = "ja"
# de spel word verder gespeeld zolang je ja blijft zeggen
while opnieuw.lower() == "ja":
    print("\n=== Het spel wordt (verder) gespeeld! ===")

    
    gekozen_woord = random.choice(woord_lijst)
    #Dit zijn de startwaarden voor het spel. Hier staat in hoe veel levens je hebt en de underscores voor de letters van het woord en hier worden ook de foute letters opgeslagen
    aantal_levens = 5
    woordjes = ["_"] * len(gekozen_woord)
    foute_letters = []

    print("= GALGJE =")
    print("Je hebt nog " + str(aantal_levens) + " levens.")
    print("Het woord bestaat uit " + str(len(gekozen_woord)) + " letters.")

    # dit is de game lus dat je de letter kan invoeren en als het fout is komt dat er te staan
    while aantal_levens > 0 and "_" in woordjes:
        toon_galg(aantal_levens)
        print("\nWoord:", " ".join(woordjes))

        if len(foute_letters) > 0:
            print("Foute letters:", ", ".join(foute_letters))

        letter = input("Kies een letter: ").lower()
        gevonden = False
        # We lopen met 'i' door elke positie van het gekozen woord.  Op elke positie controleren we of de geraden letter overeenkomtmet de letter die op die plek in het woord staat. Als dat zo is, vullen we op die positie de underscore in met de juiste letter. Ook zetten we 'gevonden' op True, zodat het spel weet dat de spelereen correcte letter heeft geraden en dus geen leven verliest.
        for i in range(len(gekozen_woord)):
            if gekozen_woord[i] == letter:
                woordjes[i] = letter
                gevonden = True
# hier zegt de computer als je een letter goed hebt geraden dat je het goed hebt en het heeft de kleur groen en als je fout hebt geraden zegt de computer in kleur rood dat je het fout hebt
        if gevonden:
            print("\033[32mGoed geraden!\033[0m")
        else:
            aantal_levens -= 1
            foute_letters.append(letter)
            print("\033[31mFout geraden!\033[0m")
            print("Je hebt nog " + str(aantal_levens) + " levens.")

    # Einde van de speelronde uitslag. Hier hadden we ook ai gebruikt want hier deed onze code heel raar en we wisten niet wat er mis was dus we vroegen ai om help.
    if "_" not in woordjes:
        print("\nGoed gedaan!")
        print("Je hebt het woord geraden:", gekozen_woord)
    else:
        toon_galg(0)
        print("\nHelaas, je hebt verloren.")
        print("Het woord was:", gekozen_woord)

    # Je vraagt aan de speler of hij verder wilt spelen hij moet kiezen uit ja of nee
    opnieuw = input("\nWil je het spel verder spelen ja/nee: ")

# Als de speler "nee" typt, breekt de game en voert Python dit uit
print("Het spel is gestopt! Bedankt voor het spelen.")

