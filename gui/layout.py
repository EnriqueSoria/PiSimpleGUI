from gui.enumerations import Inputs, Outputs


def layout(sg):
    font = (sg.DEFAULT_FONT[0], 40)
    bigger_font = (sg.DEFAULT_FONT[0], 200)

    DATETIME_ROWS = [
        [sg.Text('----', size=(30, 1), font=bigger_font, justification="center", key=Outputs.NOW)]
    ]
    TEMPERATURE_ROWS = [
        [sg.Text(size=(30, 1), font=font, justification="center", key=Outputs.TEMPERATURE)],
    ]
    MUSIC_ROWS = [
        [sg.Text(size=(30, 1), font=font, justification="center", key=Outputs.CURRENT_SONG)],
        [
            sg.Button('ᐊ', font=font, key=Inputs.PREVIOUS_SONG),
            sg.Button('⬜', font=font, key=Inputs.PLAY_PAUSE_SONG),
            sg.Button('ᐅ', font=font, key=Inputs.NEXT_SONG),
        ]
    ]

    return [
        [],[],
        *DATETIME_ROWS,
        *MUSIC_ROWS,
        *TEMPERATURE_ROWS,
        [sg.Exit()],
    ]
