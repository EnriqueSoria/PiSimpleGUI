from enum import Enum, auto


class Inputs(Enum):
    PREVIOUS_SONG = auto()
    PLAY_PAUSE_SONG = auto()
    NEXT_SONG = auto()


class Outputs(Enum):
    TEMPERATURE = auto()
    CURRENT_SONG = auto()
    NOW = auto()
    TODAY_VISITS = auto()