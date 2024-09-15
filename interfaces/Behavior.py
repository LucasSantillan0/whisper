from typing import List, Self

from interfaces import Strategy


class Behavior:

    strategies: List[Strategy.Strategy] = []
    
    @classmethod
    def respond(cls:'Behavior', userInput:str) -> str:
        for strategy in cls.strategies:
            
            if(strategy.isAppropriate(userInput)):
                return strategy.run(userInput)
    
    @classmethod
    def addStrategy(cls:'Behavior', strategy:Strategy.Strategy): 
        cls.strategies.append(strategy)