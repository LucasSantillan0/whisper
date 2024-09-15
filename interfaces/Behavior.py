from typing import List, Self

from interfaces import Strategy


class Behavior:

    strategies: List[Strategy.Strategy] = []
    
    @classmethod
    def respond(cls:'Behavior') -> str:
        for strategy in cls.strategies:
            
            if(strategy.isAppropriate()):
                return strategy.run()
    
    @classmethod
    def addStrategy(cls:'Behavior', strategy:Strategy.Strategy): 
        cls.strategies.append(strategy)