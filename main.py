from gui import Outputs
from integrations.temp_sensor.lm75 import LM75


def get_temp():
    """ Get temperature in celsius"""
    try:
        sensor = LM75()
        return sensor.get_temp()
    except PermissionError as e:
        print(str(e))
    # TODO: remove this line
    return 27


import PySimpleGUI as sg

sg.theme('BluePurple')

layout = [
    [sg.Text('Temperatura: '), sg.Text(size=(15, 1), key=Outputs.TEMPERATURE)],
]

window = sg.Window('PiSimpleGUI', layout)

while True:
    event, values = window.read(timeout=100)

    if event in (None, 'Exit'):
        break
    window[Outputs.TEMPERATURE].update(get_temp())

window.close()
