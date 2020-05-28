from gui.enumerations import Inputs, Outputs
from integrations.mqtt.utils import publish


def next(window, event, *args, **kwargs):
    pass


def prev(window, event, *args, **kwargs):
    pass


def play(window, event, *args, **kwargs):
    pass


def pause(window, event, *args, **kwargs):
    pass


def play_pause(window, event, *args, **kwargs):
    text = window.Element(Outputs.CURRENT_SONG).DisplayText
    message = 'play' if text in ('', 'pause') else 'pause'
    publish(
        topic='music/state/change',
        message=message
    )


music_events = {
    Inputs.PREVIOUS_SONG: prev,
    Inputs.PLAY_PAUSE_SONG: play_pause,
    Inputs.NEXT_SONG: next,
}


def noop(*args, **kwargs):
    pass


def handler(window, event):
    music_handler = music_events.get(event, noop)
    _ = music_handler(window, event)
