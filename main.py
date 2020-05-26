from gui import Outputs
from integrations.temp_sensor.lm75 import LM75
from integrations.temp_sensor.mockup import LM75 as LM75Mockup


def get_sensor():
    """ Get temperature in celsius"""
    try:
        return LM75()
    except PermissionError as e:
        return LM75Mockup()


import PySimpleGUI as sg

sg.theme('BluePurple')

layout = [
    [sg.Text('Temperatura: '), sg.Text(size=(15, 1), key=Outputs.TEMPERATURE)],
]

window = sg.Window('PiSimpleGUI', layout)
sensor = get_sensor()

while True:
    event, values = window.read(timeout=100)

    if event in (None, 'Exit'):
        break
    window[Outputs.TEMPERATURE].update(sensor.get_temp())

window.close()
