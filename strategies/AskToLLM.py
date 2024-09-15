from interfaces.Strategy import Strategy
from services.LLM import LLM
from chat.Chat import Chat


class AskToLLM(Strategy):
    @staticmethod
    def isAppropriate():
        return True
    @staticmethod
    def run ():
        response = LLM.call()
        Chat.addMessage('assistant',response)
        return response