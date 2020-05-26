from integrations.temp_sensor.lm75 import LM75
from integrations.temp_sensor.mockup import MockupLM75


def get_sensor():
    """ Get temperature in celsius"""
    try:
        return LM75()
    except PermissionError as e:
        return MockupLM75()