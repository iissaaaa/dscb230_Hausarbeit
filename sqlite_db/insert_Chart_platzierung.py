import sqlite3
import os
import csv


def fetch_chart_year(file_path):
    year = int(os.path.splitext(os.path.basename(file_path))[0])
    return year


def read_csv(file_path):
    """
    Liest eine CSV-Datei ein und gibt die Daten als Liste von Dictionaries zurück.
    Jede Zeile der CSV-Datei wird als ein Dictionary mit den Spaltennamen als Schlüssel interpretiert.
    """
    data = []
    with open(file_path, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)

    chartyear = fetch_chart_year(file_path)

    return data, chartyear


def get_track_id(song_title):
    # Führen Sie eine Abfrage aus, um die Track-ID für den angegebenen Künstler und Song-Titel zu erhalten
    # Diese Abfrage hängt von der genauen Struktur Ihrer Datenbank ab
    query = f"SELECT trackID FROM Track WHERE trackname = ?"

    # Verbindung zur Datenbank herstellen (wenn die Datenbank nicht vorhanden ist, wird sie erstellt)
    conn = sqlite3.connect('musikdatenbank.db')

    # Ein Cursor-Objekt erstellen, um SQL-Befehle auszuführen
    cursor = conn.cursor()

    cursor.execute(query, (song_title,))
    result = cursor.fetchone()
    print(result)

    if result:
        conn.close()
        return result[0]
    else:
        conn.close()
        return None


def fill_platzierung_table(csv, chart_year):
    for row in csv:
        print(row)
        song_title = row["Song Title"]
        platzierung = row["Position"]

        track_id = get_track_id(song_title)

        # Verbindung zur Datenbank herstellen (wenn die Datenbank nicht vorhanden ist, wird sie erstellt)
        conn = sqlite3.connect('musikdatenbank.db')

        # Ein Cursor-Objekt erstellen, um SQL-Befehle auszuführen
        cursor = conn.cursor()

        if track_id is not None:
            # Fügen Sie die Platzierung in die Platzierungstabelle ein
            cursor.execute("INSERT INTO Platzierung (chartjahr, trackID, platzierung) VALUES (?, ?, ?) ON CONFLICT (chartjahr, trackID) DO NOTHING",
                           (chart_year, track_id, platzierung))
        conn.commit()
        conn.close()


if __name__ == "__main__":

    csv_dir = "../Billdboard_Top_100_csv"

    for file_name in os.listdir(csv_dir):
        if file_name.endswith(".csv"):
            file_path = os.path.join(csv_dir, file_name)
            csv_data, chartyear = read_csv(file_path)
            fill_platzierung_table(csv_data, chartyear)
