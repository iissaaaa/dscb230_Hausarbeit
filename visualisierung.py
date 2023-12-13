import pandas as pd
import plotly.express as px

# Beispieldaten
years = ['Jahr 1', 'Jahr 2']

genre_count_1 = {'Pop': 2, 'Latin': 1, 'Hip-Hop': 1, 'House': 2, 'Indie': 1, 'Rap': 1}
genre_count_2 = {'Hip-Hop': 1, 'Rap': 1, 'House': 2, 'Pop': 4, 'Indie': 2}

# Daten für das Diagramm vorbereiten
genres = set(list(genre_count_1.keys()) + list(genre_count_2.keys()))

# DataFrame erstellen
data = {'Year': [], 'Genre': [], 'Count': []}

for year in years:
    for genre in genres:
        data['Year'].append(year)
        data['Genre'].append(genre)
        data['Count'].append(eval(f'genre_count_{years.index(year) + 1}.get("{genre}", 0)'))

df = pd.DataFrame(data)

# Histogramm erstellen
fig = px.histogram(df, x="Year", y="Count", color="Genre", barmode="group",
                   labels={"Count": "Genre Count", "Year": "Year", "Genre": "Genre"},
                   title="Genre Distribution Over Years")
fig.show()
