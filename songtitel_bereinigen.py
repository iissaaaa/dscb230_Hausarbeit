# import string


# import csv
# import requests
# import json
# import os

# #wir iterieren über die Jahre, um unterordner anlegen zu können, und um jedes einmal zu unterschieden
# for i in range(1):

#     jahr=1990+i

#     uebergeordneter_ordner = "json_datei"

#     # Name des zu erstellenden Unterordners
#     unterordner_name = f"{jahr}"

#     # Erstelle den Pfad zum Unterordner
#     unterordner_pfad = os.path.join(uebergeordneter_ordner, unterordner_name)

#     # os.makedirs(unterordner_pfad)

#     # Öffne die CSV-Datei im Lesemodus
#     with open(f'Billdboard_Top_100_csv/{jahr}.csv','r', encoding='utf8') as csv_file:
#         csv_reader = csv.reader(csv_file)
#         #sorgt dafür, dass die erste Zeile der ausgelesenen Datei übersprungen wird
#         next(csv_reader, None)
#         #erstellt notwendige Listen
#         liste_artists=[]
#         liste_songtitel=[]
#         liste_platzierung=[]

#         #füllt die Listen iterierend mit der CSV Datei mit Werten
#         for row in csv_reader:
        
#             liste_artists.append(row[1])
#             liste_songtitel.append(row[2])
#             liste_platzierung.append(row[0])

#     # Neue Liste, in der nur die Zeichenfolgen vor dem Schlüsselwort erscheinen
#     schluesselwoerter = ["feat.", "and",",","&"," X "," x ", ":"]

#     # Neue Liste, in der nur die Zeichenfolgen vor den Schlüsselwörtern erscheinen
#     bereinigte_liste_artists = []

#     for artist in liste_artists:
#         for schluesselwort in schluesselwoerter:
#             if schluesselwort in artist:
#                 teil_string = artist.split(schluesselwort)[0].strip()
#                 bereinigte_liste_artists.append(teil_string)
#                 break  # Sobald ein Schlüsselwort gefunden wurde, die Schleife verlassen
#         else:
#             bereinigte_liste_artists.append(artist)
liste_songtitel=["Wherever You Want / Also","Ich? frage mich immer","vlt* geht das ja alles so/ oder nicht"]

bereinigte_liste_songtitel = []
for songtitel in liste_songtitel:
    # Teile den String am Satzzeichen "/"
    teile = songtitel.split("/")
    # Füge den bereinigten Titel zur Liste hinzu
    bereinigte_liste_songtitel.append(teile[0])

print(bereinigte_liste_songtitel)

satzzeichen_zum_ersetzen = ["?", '"', "/", "*"]
songtitel_zum_dateinamen=[]
for songtitel in bereinigte_liste_songtitel:
    # Ersetze Satzzeichen durch einen Unterstrich für jeden Teil des Strings
    titel_zum_dateinamen = ''.join(['_' if zeichen in satzzeichen_zum_ersetzen else zeichen for zeichen in songtitel])
    songtitel_zum_dateinamen.append(titel_zum_dateinamen)
print(songtitel_zum_dateinamen)
