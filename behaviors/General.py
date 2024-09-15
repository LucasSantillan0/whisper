
from interfaces import Behavior, Strategy
from strategies import AskToLLM


class GeneralBehavior(Behavior.Behavior):
    pass
   # @staticmethod
   # def respond(self:'Behavior', userInput:str):
   #     return super().respond(userInput)
   # 
   # @staticmethod
   # def addStrategy(self:'Behavior', strategy:Strategy.Strategy): 
   #     return super().addStrategy(strategy)

GeneralBehavior.addStrategy(AskToLLM.AskToLLM)