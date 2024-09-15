from typing import List, TypedDict

from chat import Message

class MessageDict(TypedDict, total=False):
    content: str
    role: str
class Chat:
    messages:List[MessageDict] = [{ "role" : "system" , "content":"Cuando te parezca adecuado puedes responder con: 'MUSICA' para reproducir musica, o 'VERDE' para cambiar el color a verde"}]
    
    @classmethod
    def getLastMessage (cls:'Chat') ->str :
        return cls.messages[len(cls.messages)-1].get('content')
    
    @classmethod
    def addMessage (cls:'Chat',role:str, message:str):
        cls.messages.append({"role": role,"content":message})
        if(len(cls.messages) >12) :
            cls.messages.pop(1)

    @classmethod
    def getMessage (cls:'Chat', index:int) -> str :
        return cls.messages[index].get('content')