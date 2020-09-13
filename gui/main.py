import queue

import PySimpleGUI as sg
import arrow

from gui.enumerations import Outputs
from gui.event_handlers import handler
from gui.layout import layout


def the_gui(gui_queue, **kwargs):
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
        size=(1000, 600)
    )
    window = window.Layout(layout(sg))

    # --------------------- EVENT LOOP ---------------------
    while True:
        event, values = window.Read(timeout=100)  # wait for up to 100 ms for a GUI event
        if event is None or event == 'Exit':
            break

        # -------------------
        # handle events
        handler(window, event)

        # -------------------
        now = arrow.now().time()
        now = now.strftime("%H:%M")
        window.Element(Outputs.NOW).Update(now)

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
