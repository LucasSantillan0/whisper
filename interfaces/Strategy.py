from abc import ABC, abstractmethod
import re


class Strategy(ABC):
    
    @classmethod
    @abstractmethod
    def isAppropriate(cls) -> bool:
        pass
    
    @abstractmethod
    @classmethod
    def run(cls) -> str:
        pass
    
    @abstractmethod
    @classmethod
    def searchWord (cls,string:str, word:str) -> bool:
        return (re.search(rf'\b{word}\b', string, re.IGNORECASE) is not None)