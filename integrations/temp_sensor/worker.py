import time

from gui import Outputs


def read_temp(sensor, run_freq, gui_queue):
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
        gui_queue.put({
            Outputs.TEMPERATURE: sensor.get_temp()
        })
