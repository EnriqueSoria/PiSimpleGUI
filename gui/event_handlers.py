from gui.enumerations import Inputs, Outputs
from integrations.mqtt.utils import publish


def next(window, event, *args, **kwargs):
    publish(
        topic='music/state/change/next',
        message=''
    )


def prev(window, event, *args, **kwargs):
    publish(
        topic='music/state/change/prev',
        message=''
    )


def play(window, event, *args, **kwargs):
    publish(
        topic='music/state/change/play',
        message=''
    )


def pause(window, event, *args, **kwargs):
    publish(
        topic='music/state/change/play',
        message=''
    )


def play_pause(window, event, *args, **kwargs):
    play(window, event, *args, **kwargs)


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
