#!/usr/bin/python3

# Rather than importing individual classes such as threading.Thread or queue.Queue, this
#   program is doing a simple import and then indicating the package name when the functions
#   are called.  This seemed like a great way for the reader of the code to get an understanding
#   as to exactly which package is being used.  It's purely for educational and explicitness purposes
import queue
import threading
import time
import itertools

import PySimpleGUI as sg

from gui import Outputs
from integrations.temp_sensor.lm75 import LM75

"""
    DESIGN PATTERN - Multithreaded GUI
    One method for running multiple threads in a PySimpleGUI environment.
    The PySimpleGUI code, and thus the underlying GUI framework, runs as the primary, main thread
    Other parts of the software are implemented as threads

    A queue.Queue is used by the worker threads to communicate with code that calls PySimpleGUI directly.
    The PySimpleGUI code is structured just like a typical PySimpleGUI program.  A layout defined,
        a Window is created, and an event loop is executed.
    What's different is that within this otherwise normal PySimpleGUI Event Loop, there is a check for items
        in the Queue.  If there are items found, process them by making GUI changes, and continue.

    This design pattern works for all of the flavors of PySimpleGUI including the Web and also repl.it
    You'll find a repl.it version here: https://repl.it/@PySimpleGUI/Async-With-Queue-Communicationspy
"""


def worker_thread(sensor, run_freq, gui_queue):
    """
    A worker thrread that communicates with the GUI
    These threads can call functions that block withouth affecting the GUI (a good thing)
    Note that this function is the code started as each thread. All threads are identical in this way
    :param sensor: Temperature sensor
    :param run_freq: How often the thread should run in milliseconds
    :param gui_queue: Queue used to communicate with the GUI
    :return:
    """
    while True:
        time.sleep(run_freq / 1000)  # sleep for a while
        gui_queue.put(sensor.get_temp())


def the_gui(gui_queue):
    """
    Starts and executes the GUI
    Reads data from a Queue and displays the data to the window
    Returns when the user exits / closes the window
        (that means it does NOT return until the user exits the window)
    :param gui_queue: Queue the GUI should read from
    :return:
    """
    layout = [
        [sg.Text('Temperatura: '), sg.Text(size=(15, 1), key=Outputs.TEMPERATURE)],
    ]

    window = sg.Window('Multithreaded Window').Layout(layout)
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
                window.Element(Outputs.TEMPERATURE).Update(message)
                window.Refresh()  # do a refresh because could be showing multiple messages before next Read

    # if user exits the window, then close the window and exit the GUI func
    window.Close()


from integrations.temp_sensor.mockup import LM75 as LM75Mockup


def get_sensor():
    """ Get temperature in celsius"""
    try:
        return LM75()
    except PermissionError as e:
        return LM75Mockup()


if __name__ == '__main__':
    # -- Create a Queue to communicate with GUI --
    gui_queue = queue.Queue()  # queue used to communicate between the gui and the threads
    # -- Start worker threads, one runs twice as often as the other
    threading.Thread(target=worker_thread, args=(get_sensor(), 500, gui_queue,), daemon=True).start()
    # -- Start the GUI passing in the Queue --
    the_gui(gui_queue)
    print('Exiting Program')
