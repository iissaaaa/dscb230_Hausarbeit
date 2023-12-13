import csv
import requests
import json
import os
from dotenv import load_dotenv



#wir iterieren über die Jahre, um unterordner anlegen zu können, und um jedes einmal zu unterschieden
for i in range(1):

    jahr=2017+i

    uebergeordneter_ordner = "json_datei"

    # Name des zu erstellenden Unterordners
    unterordner_name = f"{jahr}"

    # Erstelle den Pfad zum Unterordner
    unterordner_pfad = os.path.join(uebergeordneter_ordner, unterordner_name)

    os.makedirs(unterordner_pfad)

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

    print(liste_artists)
    print(liste_songtitel)

    # Neue Liste, in der nur die Zeichenfolgen vor dem Schlüsselwort erscheinen
    schluesselwoerter = ["feat.", "and",",","&"," X "," x ", ":"]

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

    #API-Abfrage
    url = "https://theaudiodb.p.rapidapi.com/searchtrack.php"
    load_dotenv()

    #Iteriert durch die Länge der erstellten Listen
    for x in range(len(liste_songtitel)):

        #hier wird gefiltert wonach geschaut wird
        querystring = {"s": bereinigte_liste_artists[x], "t": liste_songtitel[x]}

        headers = {
            "X-RapidAPI-Key": os.getenv("API_TOKEN"),
            "X-RapidAPI-Host": os.getenv("API_HOST")
                }

        #es wird die API-Abfrage durchgeführt
        response = requests.get(url, headers=headers, params=querystring)

        # Überprüfe, ob die Anfrage erfolgreich war
        if response.status_code == 200:
        # der Name der json Datei wird festgelegt
            json_filename = f"{liste_songtitel[x]}.json"
            #der Ordner, in den die Datei gespeichert wird, wird geändert
            json_dateipfad=os.path.join(unterordner_pfad, json_filename)
            #json Datei wird geschreiben
            with open(json_dateipfad, "w") as jsonfile:
                json.dump(response.json(), jsonfile)
    
            print(f"Die Daten wurden in '{json_filename}' als JSON-Datei gespeichert.")
        else:
            print("Die Anfrage war nicht erfolgreich. Die Daten wurden nicht gespeichert.")

        # # Öffne die JSON-Datei im Lesemodus
        # with open(json_dateipfad, "r") as json_file:
        #     data = json.load(json_file)

        # # Initialisiere ein leeres Dictionary für die Genres
        # genres_dict = {}

        # # Durchlaufe die Liste der Tracks und speichere die Genres im Dictionary
        # for track in data["track"]:
        #     strTrack = track["strTrack"]
        #     strGenre = track["strGenre"]
        #     genres_dict[strTrack] = strGenre

        # # Ausgabe des Genre-Dictionary
        # print(genres_dict)


        
