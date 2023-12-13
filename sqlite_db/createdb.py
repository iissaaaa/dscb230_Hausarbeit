import sqlite3


def create_Tables(sql_query):

    """
    Diese Funktion führt eine sql_query aus die man als Parameter dieser Funktion übergibt. Die query sollte ein String
    sein.

    :param sql_query:
    :type sql_query: str
    :return:
    """

    try:
        # Verbindung zur Datenbank herstellen (wenn die Datenbank nicht vorhanden ist, wird sie erstellt)
        conn = sqlite3.connect('musikdatenbank.db')

        # Ein Cursor-Objekt erstellen, um SQL-Befehle auszuführen
        cursor = conn.cursor()

        # Tabelle erstellen
        cursor.execute(sql_query)

        # Änderungen speichern und Verbindung schließen
        conn.commit()
        print("Tabelle erfolgreich erstellt.")
    except sqlite3.Error as e:
        print("Fehler beim Erstellen der Tabelle:", e)
    finally:
        # Verbindung schließen
        conn.close()


def datenbankabfrage(sql_query):
    """
    Diese Funktion führt eine sql_query aus, die als Parameter übergeben wird. Die query sollte ein String sein.

    :param sql_query:
    :type sql_query: str
    """
    try:
        # Verbindung zur Datenbank herstellen (wenn die Datenbank nicht vorhanden ist, wird sie erstellt)
        conn = sqlite3.connect('musikdatenbank.db')

        # Ein Cursor-Objekt erstellen, um SQL-Befehle auszuführen
        cursor = conn.cursor()

        # SQL-Abfrage ausführen
        cursor.execute(sql_query)

        # Alle Zeilen der Ergebnisse direkt drucken
        rows = cursor.fetchall()

        for row in rows:
            print(row)

        # Verbindung schließen
        conn.close()
    except sqlite3.Error as e:
        print("Fehler bei der Datenbankabfrage:", e)


def delete_tables():
    """
    Löscht alle vorhandenen Datenbanken. Dient nur zum testen. Wird irgendwann entfernt.
    :return:
    """
    try:
        # Verbindung zur Datenbank herstellen (wenn die Datenbank nicht vorhanden ist, wird sie erstellt)
        conn = sqlite3.connect('musikdatenbank.db')

        # Ein Cursor-Objekt erstellen, um SQL-Befehle auszuführen
        cursor = conn.cursor()

        # Liste aller Tabellen in der Datenbank abrufen
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name!='sqlite_sequence';")
        tables = cursor.fetchall()

        # Tabellen löschen
        for table in tables:
            cursor.execute(f"DROP TABLE IF EXISTS {table[0]};")

        # Änderungen speichern und Verbindung schließen
        conn.commit()
        print("Alle Tabellen erfolgreich gelöscht.")
    except sqlite3.Error as e:
        print("Fehler beim Löschen der Tabellen:", e)
    finally:
        # Verbindung schließen
        conn.close()


if __name__ == "__main__":

    delete_tables()

    # schreibe die queries für das erstellen der Tabellen
    create_Table_Track = '''
        CREATE TABLE IF NOT EXISTS Track (
            trackID INTEGER PRIMARY KEY,
            trackname TEXT NOT NULL,
            dauer INTEGER,
            albumID INTEGER,
            artistID INTEGER,
            genreID INTEGER,
            videoID INTEGER,
            FOREIGN KEY (albumID) REFERENCES Album(albumID),
            FOREIGN KEY (artistID) REFERENCES Artists(artistID),
            FOREIGN KEY (genreID) REFERENCES Genre(genreID),
            FOREIGN KEY (videoID) REFERENCES Musikvideo(videoID)
        )'''

    create_Table_Album = '''
        CREATE TABLE IF NOT EXISTS Album (
            albumID INTEGER PRIMARY KEY,
            albumname TEXT NOT NULL
        )
    '''

    create_Table_Artists = '''
        CREATE TABLE IF NOT EXISTS Artists (
            artistID INTEGER PRIMARY KEY,
            artistname TEXT NOT NULL UNIQUE
        )
    '''

    create_Table_Chartjahr = '''
        CREATE TABLE IF NOT EXISTS Chartjahr (
            chartjahr INTEGER PRIMARY KEY
        )
    '''

    create_Table_Platzierung = '''
        CREATE TABLE IF NOT EXISTS Platzierung (
            chartjahr INTEGER,
            trackID INTEGER,
            platzierung INTEGER NOT NULL,
            PRIMARY KEY (chartjahr, trackID),
            FOREIGN KEY (chartjahr) REFERENCES Chartjahr(chartjahr),
            FOREIGN KEY (trackID) REFERENCES Track(trackID)
        )
    '''

    create_Table_Genre = '''
        CREATE TABLE IF NOT EXISTS Genre (
            genreID INTEGER PRIMARY KEY AUTOINCREMENT,
            genrename TEXT UNIQUE
        )
    '''

    create_Table_Musikvideo = '''
        CREATE TABLE IF NOT EXISTS Musikvideo (
            videoID INTEGER PRIMARY KEY AUTOINCREMENT,
            ytlink TEXT UNIQUE,
            likes INTEGER,
            dislikes INTEGER,
            views INTEGER
        )
    '''

    # Erstelle eine Liste aus diesen queries
    tabellenListe = [create_Table_Musikvideo,
                     create_Table_Artists,
                     create_Table_Chartjahr,
                     create_Table_Musikvideo,
                     create_Table_Genre,
                     create_Table_Album,
                     create_Table_Track,
                     create_Table_Platzierung
                     ]

    # iteriere duch jede query
    for query in tabellenListe:
        create_Tables(query)


