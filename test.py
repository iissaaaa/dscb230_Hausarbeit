import csv
import os
import requests
import json

# Öffne die CSV-Datei im Lesemodus
with open('Billdboard_Top_100_csv/2015.csv','r', encoding='utf8') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader, None)
    liste_artists=[]
    liste_songtitel=[]
    liste_platzierung=[]

    for row in csv_reader:
        
        liste_artists.append(row[1])
        liste_songtitel.append(row[2])
        liste_platzierung.append(row[0])

print(liste_artists)
print(liste_songtitel)



# Neue Liste, in der nur die Zeichenfolgen vor dem Schlüsselwort erscheinen
schluesselwoerter = ["feat.", "and",","]

# Neue Liste, in der nur die Zeichenfolgen vor den Schlüsselwörtern erscheinen
bereinigte_liste_artists = []

for artist in liste_artists:
    for schluesselwort in schluesselwoerter:
        if schluesselwort in artist:
            teil_string = artist.split(schluesselwort)[0].strip()
            bereinigte_liste_artists.append(teil_string)
            break  # Sobald ein Schlüsselwort gefunden wurde, die Schleife verlassen
    else:
        bereinigte_liste_artists.append(artist)

print(bereinigte_liste_artists)
