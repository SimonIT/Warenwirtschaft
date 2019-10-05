filename_article = "artikel.txt"
filename_delivery_man = "lieferanten.txt"


def add_article():
    print("Bitte geben Sie die Artikelnummer ein: ")
    article_number = input()
    print("Bitte geben Sie die Bezeichnung ein:")
    name = input()
    print("Bitte geben Sie den Nettopreis in Euro ein: (ohne Eurozeichen)")
    net_price = input()
    print("Bitte geben Sie den Mehrwertsteuersatz in Prozent ein: (ohne Prozentzeichen)")
    vat_rate = input()
    print("Bitte geben Sie den Bestand ein:")
    inventory = input()
    print("Bitte geben Sie die Lieferantenummer ein:")
    deliveryman_number = input()

    with open(filename_article, "a") as file:
        file.write(
            article_number + ";" + name + ";" + net_price + ";" + vat_rate + ";" + inventory + ";" + deliveryman_number + "\n")


def get_delivery_man(delivery_man_number):
    with open(filename_delivery_man, "r") as file:
        lines = file.readlines()

        deliverymen = []
        for i in lines:
            deliverymen.append(i.split(";"))

        for i in deliverymen:
            if i[0] == delivery_man_number:
                return i[1:]


def show_article():
    with open(filename_article, "r") as file:
        lines = file.readlines()

        article = []

        for i in lines:
            this_article = i.split(";")

            net_price = float(this_article[2].replace("€", ""))
            vat_rate = float(this_article[3].replace("%", "")) / 100

            gross_price = net_price * (1 + vat_rate)

            this_article.insert(4, str(gross_price))

            delivery_man_information = get_delivery_man(this_article[6].replace("\n", ""))

            this_article.pop()

            this_article += delivery_man_information

            article.append(this_article)

        line_length = [15, 13, 12, 20, 13, 9, 11, 8, 14, 5]

        for i in article:
            counter = 0
            for j in i:
                if len(j) > line_length[counter]:
                    line_length[counter] = len(j.replace('\n', '')) + 2
                counter += 1

        print("Artikelnummer".ljust(line_length[0]) + "Bezeichnung".ljust(line_length[1]) + "Nettopreis".ljust(
            line_length[2]) + "Mehrwertsteuersatz".ljust(line_length[3]) + "Bruttopreis".ljust(
            line_length[4]) + "Bestand".ljust(
            line_length[5]) + "Lieferant".ljust(line_length[6]) + "Straße".ljust(
            line_length[7]) + "Postleitzahl".ljust(
            line_length[8]) + "Ort".ljust(line_length[9]) + "\n")

        for i in article:
            counter = 0
            for j in i:
                print(j.replace('\n', '').ljust(line_length[counter]), end="")
                counter += 1
            print()


if __name__ == "__main__":
    while True:
        print("1. Artikel hinzufügen\n2. Artikel anzeigen\n")
        choice = input()

        if "1" in choice:
            add_article()
        elif "2" in choice:
            show_article()
