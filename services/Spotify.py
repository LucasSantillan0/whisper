
import os
import random
from typing import List
import spotipy # type: ignore
from spotipy.oauth2 import SpotifyOAuth # type: ignore

from interfaces.Tracks import TrackData


SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET =  os.getenv('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')

scope = "user-modify-playback-state user-read-playback-state playlist-read-private playlist-read-collaborative playlist-modify-private playlist-modify-public user-library-modify user-library-read user-read-email user-read-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
            client_secret=SPOTIPY_CLIENT_SECRET,
            redirect_uri=SPOTIPY_REDIRECT_URI,
            scope=scope))

class SpotifyService:
    likedSongs:List[TrackData]=[]
    
    @classmethod
    def playSong(cls, song:str):
        print(song)
        
        devices = sp.devices()
        print(devices)
        if len(devices['devices']) == 0:
            print("No hay dispositivos activos para reproducción.")
            return

        deviceId = devices['devices'][0]['id']
        sp.start_playback(
            device_id=deviceId, 
            uris=[song], 
            position_ms=0
            )

        
    @classmethod
    def getLikedSongs(cls):
        results = sp.current_user_saved_tracks(limit=50)
        songs = results['items']
        
        while results['next']:
            results = sp.next(results)
            songs.extend(results['items'])
        print(songs)

        for idx, item in enumerate(songs):
            track = item['track']
            cls.likedSongs.append(track)
            print(f"{idx + 1}. {track['name']} - {track['artists'][0]['name']}")

    @classmethod
    def getSongsString(cls):
        songString = ''
        for song in random.sample(cls.likedSongs,8):
            songString= songString + f" songName: {song['name']}, songUri: {song['uri']}, author:{song['artists'][0]['name']} //"
        print(songString)
        return songString