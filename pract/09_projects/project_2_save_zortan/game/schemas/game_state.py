from enum import Enum,auto

class GameState(Enum):
    INITILIZING=auto()
    IN_PROGRESS=auto()

    WIN=auto()
    LOST=auto()

