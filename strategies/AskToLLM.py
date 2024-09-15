from interfaces import Strategy


class AskToLLM(Strategy.Strategy):
    @staticmethod
    def isAppropriate(userInput:str):
        return True
    @staticmethod
    def run (userInput:str):
        return 'test'