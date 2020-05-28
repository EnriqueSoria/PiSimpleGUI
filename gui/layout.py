from gui.enumerations import Inputs, Outputs


def layout(sg):
    font = (sg.DEFAULT_FONT[0], 40)

    DATETIME_ROWS = [
        [sg.Text('----', size=(30, 1), font=font, key=Outputs.NOW)]
    ]
    TEMPERATURE_ROWS = [
        [sg.Text('Temperatura: ', font=font, ), sg.Text(size=(30, 1), font=font, key=Outputs.TEMPERATURE)],
    ]
    MUSIC_ROWS = [
        [sg.Text('Sonant ara: ', font=font, ), sg.Text(size=(30, 1), font=font, key=Outputs.CURRENT_SONG)],
        [
            sg.Button('<|', font=font, key=Inputs.PREVIOUS_SONG),
            sg.Button('||', font=font, key=Inputs.PLAY_PAUSE_SONG),
            sg.Button('|>', font=font, key=Inputs.NEXT_SONG),
        ]
    ]

    return [
        *DATETIME_ROWS,
        *TEMPERATURE_ROWS,
        *MUSIC_ROWS,
    ]
