import json
import os
import csv
#from api_abfrage import liste_platzierung, liste_songtitel


#wir iterieren über die Jahre, um unterordner anlegen zu können, und um jedes einmal zu unterschieden
for i in range(1):

    jahr=2017+i
    # Öffne die CSV-Datei im Lesemodus
    with open(f'Billdboard_Top_100_csv/{jahr}.csv','r', encoding='utf8') as csv_file:
        csv_reader = csv.reader(csv_file)
        #sorgt dafür, dass die erste Zeile der ausgelesenen Datei übersprungen wird
        next(csv_reader, None)
        #erstellt notwendige Listen
        liste_artists=[]
        liste_songtitel=[]
        liste_platzierung=[]

        #füllt die Listen iterierend mit der CSV Datei mit Werten
        for row in csv_reader:
        
            liste_artists.append(row[1])
            liste_songtitel.append(row[2])
            liste_platzierung.append(row[0])
    
print(liste_songtitel)
print(liste_platzierung)

    # Initialisiere ein leeres Dictionary für die Genres
genres_dict = {}

for x in liste_platzierung:

    unterordner_name = "json_datei\\2017"
    print(x)
    x=int(x)-1

    # Erstelle den Pfad zum Unterordner
    unterordner_pfad = os.path.join(os.getcwd(), unterordner_name)

    # Dateiname mit Erweiterung
    json_filename = f"{liste_songtitel[x]}.json"

    # Erstelle den vollen Pfad zur JSON-Datei
    json_dateipfad = os.path.join(unterordner_pfad, json_filename)

    # Öffne die JSON-Datei im Lesemodus
    with open(json_dateipfad, "r") as json_file:
        data = json.load(json_file)


    # Durchlaufe die Liste der Tracks und speichere die Genres im Dictionary
    for track in data["track"]:
        strTrack = track["strTrack"]
        strGenre = track["strGenre"]

        if strGenre==None:
            continue
        # Überprüfen, ob das Genre bereits im Dictionary vorhanden ist
        elif strGenre in genres_dict:
            # Wenn ja, erhöhe den Wert um 1
            genres_dict[strGenre] += 1
        else:
            # Wenn nicht, füge es zum Dictionary hinzu und setze den Wert auf 1
            genres_dict[strGenre] = 1

    # Jetzt enthält genres_dict die Anzahl der Vorkommen jedes Genres
    print(genres_dict)

