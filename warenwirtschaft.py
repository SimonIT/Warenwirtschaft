import os

fileNameArtikel = "artikel.txt"
fileNameLieferanten = "lieferanten.txt"

if os.path.isfile(fileNameArtikel):
    file = open(fileNameArtikel)

    lines = file.readlines()

