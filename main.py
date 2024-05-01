from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv, dotenv_values

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
website = response.text

soup = BeautifulSoup(website, "html.parser")
songs = soup.select(selector="li ul li h3", id="title-of-a-story")

song_list = [song.string.translate(str.maketrans({'\n': '', '\t': ''})) for song in songs]
# print(song_list)

load_dotenv()
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_SECRET = os.getenv("SPOTIFY_SECRET")
SPOTIFY_REDIRECT = os.getenv("SPOTFIY_REDIRECT")
USERNAME = os.getenv("USERNAME")

import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=SPOTIFY_REDIRECT,
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username=USERNAME
        
    )
)
user_id = sp.current_user()["id"]

uris = []
year = date.split("-")[0]
for song in song_list:
    try:
        results = sp.search(q=f"{song} year:{year}", type="track")
        item = results['tracks']['items'][0]['uri']
        uris.append(item)
        # print(song_list)
        # print(item)
    except IndexError:
        print(f"{song} does not exist")


playlist = sp.user_playlist_create(user=USERNAME, name=f"{date} Billboard 100", public=False, collaborative=False, description='Takes top 100 music from date in past to create a Spotify playlist')
playlist = playlist["id"]
sp.playlist_add_items( playlist_id=playlist, items=uris)

