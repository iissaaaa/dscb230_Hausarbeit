import os
import sqlite3


def fill_chartjahr_table(folder_path):
    """
    Diese Funktion befüllt die Chartjahr Tabelle.
    :param folder_path:
    :return:
    """
    try:
        # Verbindung zur Datenbank herstellen (wenn die Datenbank nicht vorhanden ist, wird sie erstellt)
        conn = sqlite3.connect('musikdatenbank.db')

        # Ein Cursor-Objekt erstellen, um SQL-Befehle auszuführen
        cursor = conn.cursor()

        # Durchsuche den Ordner nach CSV-Dateien
        for file_name in os.listdir(folder_path):
            if file_name.endswith(".csv"):
                # Extrahiere die Jahreszahl aus dem Dateinamen
                chart_year = int(os.path.splitext(file_name)[0])

                # Füge die Jahreszahl in die Tabelle Chartjahr ein
                # Falls Jahr schon vorhanden ist, mache nichts
                cursor.execute("INSERT INTO Chartjahr (chartjahr) VALUES (?) ON CONFLICT (chartjahr) DO NOTHING",
                               (chart_year,))

        # Änderungen speichern und Verbindung schließen
        conn.commit()
        print("Daten erfolgreich in die Tabelle Chartjahr eingefügt.")
    except sqlite3.Error as e:
        print("Fehler beim Einfügen der Daten:", e)
    finally:
        # Verbindung schließen
        conn.close()


if __name__ == "__main__":
    # einfügen der Jahre in die Datenbank
    fill_chartjahr_table("../Billdboard_Top_100_csv")
