from enum import Enum, auto


class Inputs(Enum):
    pass


class Outputs(Enum):
    TEMPERATURE = auto()
    CURRENT_SONG = auto()


def layout(sg):
    font = (sg.DEFAULT_FONT[0], 40)

    return [
        [sg.Text('Temperatura: ', font=font,), sg.Text(size=(30, 1), font=font, key=Outputs.TEMPERATURE)],
        [sg.Text('Sonant ara: ', font=font,), sg.Text(size=(30, 1), font=font, key=Outputs.CURRENT_SONG)],
    ]
