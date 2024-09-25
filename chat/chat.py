from typing import List, TypedDict

from chat import Message
from services.Spotify import SpotifyService

class MessageDict(TypedDict, total=False):
    content: str
    role: str
class Chat:
    messages:List[MessageDict] = [{"role": "system", "content":"Cuando te pida reproducir una cancion usa esta lista: "+SpotifyService.getSongsString()}]
    
    @classmethod
    def getLastMessage (cls) ->str :
        message = cls.messages[len(cls.messages)-1].get('content')
        
        if message is None:
            raise Exception("Message array is empty")
        
        return message
    
    @classmethod
    def addMessage (cls,role:str, message):
        cls.messages.append({"role": role,"content":message})
        if(len(cls.messages) >12) :
            cls.messages.pop(1)
    @classmethod
    def addToolMessage (cls,toolId, content):
        cls.messages.append({"role": "tool","content":content,"tool_call_id":toolId})
        if(len(cls.messages) >12) :
            cls.messages.pop(1)

    @classmethod
    def addAny (cls,any):
        cls.messages.append(any)
        if(len(cls.messages) >12) :
            cls.messages.pop(1)
            
    @classmethod
    def getMessage (cls, index:int) -> str :
        message = cls.messages[index].get('content')
        
        if message is None:
            raise Exception("Message index out of bounds")
        
        return message