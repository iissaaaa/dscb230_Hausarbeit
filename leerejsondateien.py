# import csv
# import os
# import json

# #leere Liste für die leeren JSON-Dateien wird erstellt
# leere_lieder_infos=[]

# for i in range(1):
#     print(i)
#     jahr=2017+i
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


#     for x in liste_platzierung:

#         unterordner_name = f"json_datei\\{jahr}"
#         print(x)
#         x=int(x)-1

#         # Erstelle den Pfad zum Unterordner
#         unterordner_pfad = os.path.join(os.getcwd(), unterordner_name)

#         # Dateiname mit Erweiterung
#         json_filename = f"{liste_songtitel[x]}.json"
#         print(liste_songtitel[x])

#         # Erstelle den vollen Pfad zur JSON-Datei
#         json_dateipfad = os.path.join(unterordner_pfad, json_filename)

#         # Öffne die JSON-Datei im Lesemodus
#         with open(json_dateipfad, "r") as json_file:
#             data = json.load(json_file)

#         print(data["track"])
#         #überprüfen, ob die Json-Datei leer ist
#         if data["track"] == None:
#             leere_lieder_infos.append(liste_songtitel[x])
        
# print(leere_lieder_infos)

for i in range(2):
    print(i)