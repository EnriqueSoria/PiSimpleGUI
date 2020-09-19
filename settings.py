import os

from decouple import AutoConfig

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
config = AutoConfig(f'{BASE_DIR}/')

MQTT_SERVER = config('MQTT_SERVER', default='localhost')

VISIT_COUNT_API = config("VISIT_COUNT_API")
VISIT_COUNT_TOKEN = config("VISIT_COUNT_TOKEN")
VISIT_COUNT_FREQ = config("VISIT_COUNT_FREQ", 60, cast=int)
