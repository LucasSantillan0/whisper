
from interfaces import Behavior, Strategy
from strategies.AskToLLM import AskToLLM
from strategies.PlayMusic import PlayMusic


class GeneralBehavior(Behavior.Behavior):
    pass

GeneralBehavior.addStrategy(AskToLLM)