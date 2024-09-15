import re


class Strategy:
    @classmethod
    def isAppropriate() -> bool:
        pass
    @classmethod
    def run():
        pass
    @classmethod
    def searchWord (string:str, word:str) -> bool:
        return re.search(rf'\b{word}\b', string, re.IGNORECASE)