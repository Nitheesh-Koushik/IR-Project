import requests
import json
import lyricsgenius as lg
with open("data.json", "r") as file:
    data = json.load(file)
    file.close()

access_token = ""

genius = lg.Genius(access_token)
genius.timeout = 10265
master = {}
j = 0
for _, i in enumerate(data):
    print(_)
    k = i.split("-")
    title, artist = k[0], k[-1]
    song = genius.search_song(title= title, artist = artist)
    try:
        lyric = song.lyrics
        master[i] = lyric
    except:
        master[i] = None

with open('lyrics.json', 'w', encoding='utf-8') as f:
    json.dump(master, f, ensure_ascii=False, indent=4)
