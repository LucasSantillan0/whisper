from abc import ABC, abstractmethod

class Action (ABC):
    @property
    @abstractmethod
    def actionName(self):
        pass
    @classmethod
    @abstractmethod
    def run(self,data):
        pass