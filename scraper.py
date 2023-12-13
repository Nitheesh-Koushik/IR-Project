import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
client_id = ''
client_secret = ''

# Initialize Spotipy with your credentials
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)


# Use the Spotify API
# For example, search for tracks
playlistIDs = [ "3XYVhAAF3AbFke9wlAGjfJ"]

def getting_tracknames(playlistID):
    offset = 0
    songs = []
    while True:
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager, requests_timeout=20)
        tracks = sp.playlist_tracks(playlistID, offset=offset)
        if not tracks['items']:
            break

        for idx, item in enumerate(tracks['items']):
            track = item['track']
            songs.append(f"{track['name']} - {', '.join([artist['name'] for artist in track['artists']])}")
        offset += len(tracks['items'])
    return songs
masterSongs = []
for id in playlistIDs:
    songs = getting_tracknames(id)
    masterSongs.extend(songs)
masterSongs = list(set(masterSongs))
print(len(masterSongs))
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(masterSongs, f, ensure_ascii=False, indent=4)
