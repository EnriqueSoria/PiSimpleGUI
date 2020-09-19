import time
import requests

from gui.enumerations import Outputs
from settings import VISIT_COUNT_API, VISIT_COUNT_TOKEN


def visit_count():
    data = {
        "when": "today",
        "token": VISIT_COUNT_TOKEN
    }
    r = requests.post(url=VISIT_COUNT_API, data=data)

    count = r.json().get("count", "error")

    return f"Visites hui: {count}"


def api_calls(run_freq: int, gui_queue):
    """
    A worker thrread that communicates with the GUI
    These threads can call functions that block withouth affecting the GUI (a good thing)
    Note that this function is the code started as each thread. All threads are identical in this way
    :param run_freq: How often the thread should run in seconds
    :param gui_queue: Queue used to communicate with the GUI
    :return:
    """
    while True:
        time.sleep(run_freq)  # sleep for a while

        gui_queue.put({
            Outputs.TODAY_VISITS: visit_count()
        })
