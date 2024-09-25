from typing import Any, Callable, List, TypedDict, Unpack
from config.AppLoop import runAppLoop
from services.LLM import LLM
from services.Spotify import SpotifyService


class OptionsType(TypedDict):
    tasks:List[Callable[[str,Any],None]]

def bootstrapApplication (**kwargs: Unpack[OptionsType]):
    options: OptionsType = {
        'tasks' : [],
    }
    SpotifyService.getLikedSongs()
    LLM.initLLM()
    options.update(kwargs)
    runAppLoop(options['tasks'])
    pass