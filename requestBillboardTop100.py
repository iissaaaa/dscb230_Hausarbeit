import requests
import json
import os
from dotenv import load_dotenv

url = "https://theaudiodb.p.rapidapi.com/searchtrack.php"
load_dotenv()

querystring = {"s": "Ed Sheeran", "t": "Shape Of You"}

headers = {
    "X-RapidAPI-Key": os.getenv("API_TOKEN"),
    "X-RapidAPI-Host": os.getenv("API_HOST")
}

response = requests.get(url, headers=headers, params=querystring)

# Überprüfe, ob die Anfrage erfolgreich war
if response.status_code == 200:
    # JSON-Datei erstellen und schreiben
    json_filename = "ed_sheeran_shape_of_you.json"
    with open(json_filename, "w") as jsonfile:
        json.dump(response.json(), jsonfile)
    
    print(f"Die Daten wurden in '{json_filename}' als JSON-Datei gespeichert.")
else:
    print("Die Anfrage war nicht erfolgreich. Die Daten wurden nicht gespeichert.")

