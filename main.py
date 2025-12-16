import random

def hangman():
    woerter = [
        "apfel", "banane", "schokolade", "haus", "urlaub", "strand",
        "sonne", "wolke", "regen", "schnee", "garten", "blume",
        "baum", "fahrrad", "auto", "zug", "flugzeug", "kuchen",
        "wasserfall", "berge", "insel", "himmel", "meer", "wald",
        "vogel", "schmetterling", "kirsche", "pilz", "mond", "stern",
        "fluss", "see", "fee", "zauber", "tanz", "musik", "lied",
        "ball", "spielen", "freund", "schule", "lehrer", "kino",
    ]

    galgen = [
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
          /    |
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

    spielen = True

    while spielen:
        wort = random.choice(woerter)
        geraten = []
        leben = 6

        print("\n Willkommen zu Hangman!")

        while True:
            # Anzeige Galgen
            print(galgen[6 - leben])

            # Anzeige Wort
            anzeigen = ""
            for buchstabe in wort:
                if buchstabe in geraten:
                    anzeigen += buchstabe + " "
                else:
                    anzeigen += "_ "
            print("\nWort:", anzeigen)
            print("Leben übrig:", leben)

            # Buchstabe raten
            tipp = input("Gib einen Buchstaben ein: ").lower()

            if len(tipp) != 1 or not tipp.isalpha():
                print("Bitte nur einen einzelnen Buchstaben eingeben!")
                continue

            if tipp in geraten:
                print("Diesen Buchstaben hast du schon versucht.")
                continue

            geraten.append(tipp)

            if tipp not in wort:
                leben -= 1
                print(" Falsch!")
            else:
                print(" Richtig!")

            if all(b in geraten for b in wort):
                print("\n Glückwunsch! Du hast das Wort erraten:", wort)
                break

            if leben == 0:
                print(galgen[6])
                print("\n Keine Leben mehr! Das Wort war:", wort)
                break

        # Möchte der Spieler nochmal spielen?
        erneut = input("\nMöchtest du nochmal spielen? (j/n): ").lower()
        if erneut != "j":
            spielen = False
            print("\n Danke fürs Spielen! Auf Wiedersehen!")
            input("Drücke Enter, um das Programm zu beenden...")

hangman()
