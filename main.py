#!/usr/bin/python3

import queue
import threading

from gui.enumerations import Outputs
from gui.main import the_gui
from integrations.api_calls.calls import api_calls
from integrations.mqtt.utils import mqtt_sub_worker
from integrations.temp_sensor import get_sensor
from integrations.temp_sensor.worker import read_temp
from settings import VISIT_COUNT_FREQ


def mqtt_receiver(client, userdata, message):
    print('mqtt_receiver -> ', message.topic, message.payload)
    gui_queue.put({
        Outputs.CURRENT_SONG: message.payload.decode("utf-8")
    })


if __name__ == '__main__':
    # -- Create a Queue to communicate with GUI --
    gui_queue = queue.Queue()  # queue used to communicate between the gui and the threads

    # -- Start worker threads
    temp_sensor = get_sensor()
    threading.Thread(target=read_temp, args=(temp_sensor, 5000, gui_queue,), daemon=True).start()

    # -- API calls
    threading.Thread(target=api_calls, args=(VISIT_COUNT_FREQ, gui_queue,), daemon=True).start()

    mqtt_subscriber = threading.Thread(
        target=mqtt_sub_worker,
        args=(mqtt_receiver,),
        daemon=True
    )
    mqtt_subscriber.start()

    # -- Start the GUI passing in the Queue --
    the_gui(gui_queue)
    print('Exiting Program')
