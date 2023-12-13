import os
import requests
import json

# Name des Unterordners, in dem die Daten gespeichert werden sollen
unterordner_name = "json_datei"

# Erstelle den Pfad zum Unterordner
unterordner_pfad = os.path.join(os.getcwd(), unterordner_name)

url = "https://theaudiodb.p.rapidapi.com/searchtrack.php"


querystring = {"s": "Ed Sheeran", "t": "lub Of You"}
headers = {
        "X-RapidAPI-Key": "efb193ae9fmsh0ccf4ee211d91f1p1e328cjsn0957c54e32c6",
        "X-RapidAPI-Host": "theaudiodb.p.rapidapi.com"
    }

response = requests.get(url, headers=headers, params=querystring)

    # Überprüfe, ob die Anfrage erfolgreich war
if response.status_code == 200:
    # JSON-Datei erstellen und schreiben
        json_filename = f"Shape Of You.json"
        json_dateipfad = os.path.join(unterordner_pfad, json_filename)
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






