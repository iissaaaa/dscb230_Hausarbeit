import os
import sqlite3
import json


def insert_artists(json_data):
    # Verbindung zur Datenbank herstellen (wenn die Datenbank nicht vorhanden ist, wird sie erstellt)
    conn = sqlite3.connect('musikdatenbank.db')
    cursor = conn.cursor()

    # JSON-Daten laden
    data = json.loads(json_data)
    print(data)

    # Durchlaufe die Track-Einträge im JSON
    if data.get('track') is not None:
        for track_entry in data.get('track', []):
            # Extrahiere die Albumdaten aus dem Track-Eintrag
            artist_id = int(track_entry.get('idArtist', 0))
            artist_name = track_entry.get('strArtist', '')

            # Füge die Daten in die Tabelle Album ein (und ignoriere vorhandene Einträge)
            cursor.execute("INSERT INTO Artists (artistID, artistname) VALUES (?, ?) ON CONFLICT (artistID) DO NOTHING",
                           (artist_id, artist_name))

    # Änderungen speichern und Verbindung schließen
    conn.commit()
    conn.close()


def insert_album(json_data):
    # Verbindung zur Datenbank herstellen (wenn die Datenbank nicht vorhanden ist, wird sie erstellt)
    conn = sqlite3.connect('musikdatenbank.db')
    cursor = conn.cursor()

    # JSON-Daten laden
    data = json.loads(json_data)

    # Durchlaufe die Track-Einträge im JSON
    if data.get('track') is not None:
        for track_entry in data.get('track', []):
            # Extrahiere die Albumdaten aus dem Track-Eintrag
            album_id = int(track_entry.get('idAlbum', 0))
            album_name = track_entry.get('strAlbum', '')

            # Füge die Daten in die Tabelle Album ein (und ignoriere vorhandene Einträge)
            cursor.execute("INSERT INTO Album (albumID, albumname) VALUES (?, ?) ON CONFLICT (albumID) DO NOTHING",
                           (album_id, album_name))

    # Änderungen speichern und Verbindung schließen
    conn.commit()
    conn.close()


def insert_genre(json_data):
    # Verbindung zur Datenbank herstellen (wenn die Datenbank nicht vorhanden ist, wird sie erstellt)
    conn = sqlite3.connect('musikdatenbank.db')
    cursor = conn.cursor()

    # JSON-Daten laden
    data = json.loads(json_data)

    # Durchlaufe die Track-Einträge im JSON
    if data.get('track') is not None:
        for track_entry in data.get('track', []):
            # Extrahiere die Albumdaten aus dem Track-Eintrag
            genre_name = track_entry.get('strGenre', '')

            # Füge die Daten in die Tabelle Album ein (und ignoriere vorhandene Einträge)
            if genre_name is not None:
                cursor.execute("INSERT INTO Genre (genrename) VALUES (?) ON CONFLICT (genrename) DO NOTHING",
                               (genre_name,))

    # Änderungen speichern und Verbindung schließen
    conn.commit()
    conn.close()


def insert_musikvideo(json_data):
    # Verbindung zur Datenbank herstellen (wenn die Datenbank nicht vorhanden ist, wird sie erstellt)
    conn = sqlite3.connect('musikdatenbank.db')
    cursor = conn.cursor()

    # JSON-Daten laden
    data = json.loads(json_data)

    # Durchlaufe die Track-Einträge im JSON
    if data.get('track') is not None:
        for track_entry in data.get('track', []):
            # Extrahiere die Albumdaten aus dem Track-Eintrag
            mv_link = track_entry.get('strMusicVid', '')
            mv_views = track_entry.get('intMusicVidViews')
            mv_likes = track_entry.get('intMusicVidLikes')
            mv_dislikes = track_entry.get('intMusicVidDislikes')

            # Füge die Daten in die Tabelle Album ein (und ignoriere vorhandene Einträge)
            if mv_link is not None and mv_views is not None and mv_likes is not None and mv_dislikes is not None:
                cursor.execute("INSERT INTO Musikvideo (ytlink, likes, dislikes, views) VALUES (?, ?, ? , ?) ON CONFLICT (ytlink) DO NOTHING",
                               (mv_link, mv_likes, mv_dislikes, mv_views))

    # Änderungen speichern und Verbindung schließen
    conn.commit()
    conn.close()


def insert_tracks(json_data):
    # Verbindung zur Datenbank herstellen (wenn die Datenbank nicht vorhanden ist, wird sie erstellt)
    conn = sqlite3.connect('musikdatenbank.db')
    cursor = conn.cursor()

    # JSON-Daten laden
    data = json.loads(json_data)

    # Durchlaufe die Track-Einträge im JSON
    if data.get('track') is not None:
        for track_entry in data.get('track', []):
            # Extrahiere die Albumdaten aus dem Track-Eintrag
            trackid = int(track_entry.get('idTrack', 0))
            trackname = track_entry.get('strTrack', '')
            duration = int(track_entry.get('intDuration', 0))
            f_albumid = int(track_entry.get('idAlbum', 0))
            f_artistid = int(track_entry.get('idArtist', 0))
            f_genreid = track_entry.get('strGenre', '')
            f_mvid = track_entry.get('strMusicVid', '')

            # Füge die Daten in die Tabelle Album ein (und ignoriere vorhandene Einträge)
            cursor.execute(
                "INSERT INTO Track (trackID, trackname, dauer, albumID, artistID, genreID, videoID) VALUES (?, ?, ? , ?, ?, ?, ?) ON CONFLICT (trackid) DO NOTHING",
                (trackid, trackname, duration, f_albumid, f_artistid, f_genreid, f_mvid))

    # Änderungen speichern und Verbindung schließen
    conn.commit()
    conn.close()


def manage_insertion(json_direcrtory):
    # Iteriere durch jedes Unterverzeichnis (Jahr) im angegebenen Verzeichnis
    for year_directory in os.listdir(json_direcrtory):
        year_path = os.path.join(json_direcrtory, year_directory)

        # Überprüfe, ob es sich um ein Verzeichnis handelt
        if os.path.isdir(year_path):
            # Iteriere durch jede JSON-Datei im Jahr-Verzeichnis
            for json_file in os.listdir(year_path):
                if json_file.endswith(".json"):
                    json_path = os.path.join(year_path, json_file)

                    # Lese den Inhalt der JSON-Datei
                    with open(json_path, 'r', encoding='utf-8') as file:
                        json_data = file.read()

                    # Rufe die Funktionen für die Datenbankeintragung auf
                    insert_artists(json_data)
                    insert_album(json_data)
                    insert_genre(json_data)
                    insert_musikvideo(json_data)
                    insert_tracks(json_data)


if __name__ == "__main__":

    JSON_ordner = "../json_datei"

    manage_insertion(JSON_ordner)
