import pandas as pd
from src.song import find_song

from src.album import tracks

songs_url = "./data/top-500-songs.txt"
songs_df = pd.read_csv(songs_url, sep='\t', header = None, names = ['rank', 'song', 'artist', 'year'])
songs = songs_df.to_dict('records')

track_url = "./data/track_data.json"
albums_and_tracks = pd.read_json(track_url)
albums_tracks = albums_and_tracks.to_dict('records')

albums_url = "./data/data.csv"
df = pd.read_csv(albums_url)
albums = df.to_dict('records')

