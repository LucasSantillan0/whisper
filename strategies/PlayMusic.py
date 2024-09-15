from interfaces.Strategy import Strategy
from chat.Chat import Chat


class PlayMusic (Strategy):
    @classmethod
    def isAppropriate(cls:'PlayMusic') -> bool:
        return cls.searchWord(Chat.getMessage(len(Chat.messages)-2),'MUSIC' ) and  cls.searchWord( Chat.getLastMessage() ,'Bien') 
    @classmethod
    def run():
        pass
