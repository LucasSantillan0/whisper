from typing import List, Self

from interfaces import Strategy


class Behavior:

    strategies: List[Strategy.Strategy] = []
    
    @classmethod
    def respond(cls) -> str:
        for strategy in cls.strategies:
            
            if(strategy.isAppropriate()):
                return strategy.run()
            
        return "No hay estrategia adecuada para responder"
    
    @classmethod
    def addStrategy(cls, strategy:Strategy.Strategy): 
        cls.strategies.append(strategy)