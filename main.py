#!/usr/bin/python3

# Rather than importing individual classes such as threading.Thread or queue.Queue, this
#   program is doing a simple import and then indicating the package name when the functions
#   are called.  This seemed like a great way for the reader of the code to get an understanding
#   as to exactly which package is being used.  It's purely for educational and explicitness purposes
import queue
import threading
import paho.mqtt.client as mqtt

import PySimpleGUI as sg

from gui import Outputs, layout
from integrations.temp_sensor import get_sensor
from integrations.temp_sensor.worker import read_temp


def the_gui(layout, gui_queue):
    """
    Starts and executes the GUI
    Reads data from a Queue and displays the data to the window
    Returns when the user exits / closes the window
        (that means it does NOT return until the user exits the window)
    :param gui_queue: Queue the GUI should read from
    :return:
    """
    sg.set_options(border_width=0)
    window = sg.Window(
        'Multithreaded Window',
        no_titlebar=True,
        grab_anywhere=True,
        size=(1000, 600)
    )
    window = window.Layout(layout)

    # --------------------- EVENT LOOP ---------------------
    while True:
        event, values = window.Read(timeout=100)  # wait for up to 100 ms for a GUI event
        if event is None or event == 'Exit':
            break
        # --------------- Loop through all messages coming in from threads ---------------
        while True:  # loop executes until runs out of messages in Queue
            try:  # see if something has been posted to Queue
                message = gui_queue.get_nowait()
            except queue.Empty:  # get_nowait() will get exception when Queue is empty
                break  # break from the loop if no more messages are queued up
            # if message received from queue, display the message in the Window
            if message:
                for key, value in message.items():
                    window.Element(key).Update(value)
                window.Refresh()  # do a refresh because could be showing multiple messages before next Read

    # if user exits the window, then close the window and exit the GUI func
    window.Close()


def mqtt_receiver(client, userdata, message):
    gui_queue.put({
        Outputs.CURRENT_SONG: message.payload.decode("utf-8")
    })


def get_client(gui_queue, topic='#', client_name='test', client_host='localhost'):
    try:
        client = mqtt.Client(client_name)
        client.connect(client_host)
        client.on_message = mqtt_receiver
        return client
    except ConnectionRefusedError as e:
        print(e)


def mqtt_worker(client, topic='#'):
    client.loop_start()
    client.subscribe(topic)


if __name__ == '__main__':
    # -- Create a Queue to communicate with GUI --
    gui_queue = queue.Queue()  # queue used to communicate between the gui and the threads

    # -- Start worker threads
    temp_sensor = get_sensor()
    threading.Thread(target=read_temp, args=(temp_sensor, 5000, gui_queue,), daemon=True).start()

    mqtt_client = get_client(gui_queue)
    if mqtt_client:
        threading.Thread(target=mqtt_worker, args=(mqtt_client,), daemon=True).start()

    # -- Start the GUI passing in the Queue --
    the_gui(layout(sg), gui_queue)
    print('Exiting Program')
