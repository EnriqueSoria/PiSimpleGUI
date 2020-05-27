from enum import Enum, auto


class Inputs(Enum):
    PREVIOUS_SONG = auto()
    PLAY_PAUSE_SONG = auto()
    NEXT_SONG = auto()


class Outputs(Enum):
    TEMPERATURE = auto()
    CURRENT_SONG = auto()


def layout(sg):
    font = (sg.DEFAULT_FONT[0], 40)

    TEMPERATURE_ROWS = [
        [sg.Text('Temperatura: ', font=font,), sg.Text(size=(30, 1), font=font, key=Outputs.TEMPERATURE)],
    ]
    MUSIC_ROWS = [
        [sg.Text('Sonant ara: ', font=font,), sg.Text(size=(30, 1), font=font, key=Outputs.CURRENT_SONG)],
        [
            sg.Button('<|', key=Inputs.PREVIOUS_SONG),
            sg.Button('||', key=Inputs.PLAY_PAUSE_SONG),
            sg.Button('|>', Inputs.NEXT_SONG),
        ]
    ]

    return [
        *TEMPERATURE_ROWS,
        *MUSIC_ROWS,
    ]
