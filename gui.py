from enum import Enum, auto


class Inputs(Enum):
    pass


class Outputs(Enum):
    TEMPERATURE = auto()
    CURRENT_SONG = auto()


def layout(sg):
    return [
        [sg.Text('Temperatura: '), sg.Text(size=(30, 1), key=Outputs.TEMPERATURE)],
        [sg.Text('Current song: '), sg.Text(size=(30, 1), key=Outputs.CURRENT_SONG)],
    ]
