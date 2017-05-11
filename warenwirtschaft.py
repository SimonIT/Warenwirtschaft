import os

fileNameArtikel = "artikel.txt"
fileNameLieferanten = "lieferanten.txt"


def addArtikel():
    print("Bitte geben Sie die Artikelnummer ein: ")
    Artikelnummer = input()
    print("Bitte geben Sie die Bezeichnung ein:")
    Bezeichnung = input()
    print("Bitte geben Sie den Nettopreis in Euro ein: (ohne Eurozeichen)")
    Nettopreis = input()
    print("Bitte geben Sie den Mehrwertsteuersatz in Prozent ein: (ohne Prozentzeichen)")
    Mehrwertsteuersatz = input()
    print("Bitte geben Sie den Bestand ein:")
    Bestand = input()
    print("Bitte geben Sie die Lieferantenummer ein:")
    Lieferantenummer = input()

    file = open(fileNameArtikel, "a")

    file.write(
        Artikelnummer + ";" + Bezeichnung + ";" + Nettopreis + ";" + Mehrwertsteuersatz + ";" + Bestand + ";" + Lieferantenummer + "\n")


def getLieferant(Lieferantenummer):
    if os.path.isfile(fileNameLieferanten):
        file = open(fileNameLieferanten, "r")

        lines = file.readlines()

        Lieferanten = []
        for i in lines:
            Lieferanten.append(i.split(";"))

        for i in Lieferanten:
            if i[0] == Lieferantenummer:
                return i[1:]


def showArtikel():
    if os.path.isfile(fileNameArtikel):
        file = open(fileNameArtikel, "r")

        lines = file.readlines()

        Artikel = []

        for i in lines:
            dieserArtikel = i.split(";")

            Nettopreis = float(dieserArtikel[2].replace("€", ""))
            Mehrwertsteuersatz = float(dieserArtikel[3].replace("%", "")) / 100

            Bruttopreis = Nettopreis * (1 + Mehrwertsteuersatz)

            dieserArtikel.insert(4, str(Bruttopreis))

            LieferantenInformationen = getLieferant(dieserArtikel[6].replace("\n", ""))

            dieserArtikel.pop()

            dieserArtikel += LieferantenInformationen

            Artikel.append(dieserArtikel)

        Zeilenlänge = [15, 13, 12, 20, 13, 9, 11, 8, 14, 5]

        for i in Artikel:
            counter = 0
            for j in i:
                if len(j) > Zeilenlänge[counter]:
                    Zeilenlänge[counter] = len(j.replace('\n', '')) + 2
                counter += 1

        print("Artikelnummer".ljust(Zeilenlänge[0]) + "Bezeichnung".ljust(Zeilenlänge[1]) + "Nettopreis".ljust(
            Zeilenlänge[2]) + "Mehrwertsteuersatz".ljust(Zeilenlänge[3]) + "Bruttopreis".ljust(Zeilenlänge[4]) + "Bestand".ljust(
            Zeilenlänge[5]) + "Lieferant".ljust(Zeilenlänge[6]) + "Straße".ljust(Zeilenlänge[7]) + "Postleitzahl".ljust(
            Zeilenlänge[8]) + "Ort".ljust(Zeilenlänge[9]) + "\n")

        for i in Artikel:
            counter = 0
            for j in i:
                print(j.replace('\n', '').ljust(Zeilenlänge[counter]), end="")
                counter += 1
            print()


while True:
    print("1. Artikel Hinzufügen\n2. Artikel Anzeigen\n")
    choice = input()

    if "1" in choice:
        addArtikel()
    elif "2" in choice:
        showArtikel()
