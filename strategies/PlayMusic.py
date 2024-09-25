import math
import random
from interfaces.Strategy import Strategy
from chat.Chat import Chat
from services.Spotify import SpotifyService




class PlayMusic (Strategy):
        
    @classmethod
    def isAppropriate(cls) -> bool:
        return cls.searchWord(Chat.getMessage(len(Chat.messages)-2), 'MUSICA') and  cls.searchWord(Chat.getLastMessage(), 'BIEN') 
    
    @classmethod
    def run(cls):
        SpotifyService.playSong(
            SpotifyService.likedSongs[math.floor(random.random()*len(SpotifyService.likedSongs))]['uri']
            )
        return 'playing song'
    

