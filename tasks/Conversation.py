from time import sleep
from behaviors.General import GeneralBehavior
from chat.Chat import Chat
from mic_control import mute_mic, unmute_mic
from pyttsx3 import Engine # type: ignore

def runConversation (text:str, engine:Engine):
   Chat.addMessage('user',text)
   response = GeneralBehavior.respond()
   mute_mic()
   engine.say(response)
   engine.runAndWait()
   sleep(1)
   unmute_mic()