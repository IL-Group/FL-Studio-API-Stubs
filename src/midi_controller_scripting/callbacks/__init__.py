"""
{{module_title[callbacks]}}

This page documents the callback functions used by the MIDI Controller
Scripting API. Note that these functions cannot be imported, instead, you
should defined the ones that you need within your script's entrypoint file
(`device_*.py`).

## Example entrypoint file

```py
# name=My Script


def OnInit():
    print("FL Studio initialized my script!")
```

## Note on `FlMidiMsg` callbacks

The MIDI Controller Scripting API provides many callback functions for handling
incoming events. If an event isn't handled by an earlier callback, it is passed
to later callbacks.

For simple scripts, these callbacks can be used as an alternative to writing
more complex event handling code. For example, if your script handles control
change (CC) events differently to note events, it may be simpler to write
separate logic for `OnNoteOn`, `OnNoteOff` and `OnControlChange` than it is to
handle all the events in `OnMidiMsg`.
"""
from typing import Literal

from fl_classes import FlMidiMsg


def OnInit() -> None:
    """
    Called when FL Studio initializes the script.

    Note that the script may be kept in memory after being de-initialized with
    {{docs_url_fn[callbacks.OnDeInit]}}, so this function may be called more
    than once during the lifetime of this Python script.

    Included since API Version 1.
    """


def OnDeInit() -> None:
    """
    Called before FL Studio de-initializes the script.

    This function should be used to shut down the attached device (eg by
    sending a "goodbye" message).

    Included since API Version 1.
    """


def OnMidiIn(msg: FlMidiMsg) -> None:
    """
    Called when any MIDI message is received.

    This is the first opportunity to handle the event, and occurs before any
    processing is done by FL Studio. As such, setting `event.handled = True`
    here will prevent the event from being handled entirely.

    This function is only intended for filtering events using `event.handled`.
    Actual processing of MIDI events should be performed in
    {{docs_url_fn[callbacks.OnMidiMsg]}} rather than here.

    ## Args

    * `msg` ({{docs_url_attr[fl_classes.FlMidiMsg]}}): incoming MIDI message

    Included since API Version 1.
    """


def OnMidiMsg(msg: FlMidiMsg) -> None:
    """
    Called after {{docs_url_fn[callbacks.OnMidiIn]}} if the event was not
    handled.

    This is the second opportunity to handle incoming MIDI events.

    ## Args

    * `msg` ({{docs_url_attr[fl_classes.FlMidiMsg]}}): incoming MIDI message.

    Included since API Version 1.
    """


def OnSysEx(msg: FlMidiMsg) -> None:
    """
    Called after {{docs_url_fn[callbacks.OnMidiMsg]}} for system-exclusive MIDI
    events.

    ## Args

    * `msg` ({{docs_url_attr[fl_classes.FlMidiMsg]}}): incoming system-exclusive MIDI message.

    Included since API Version 1.
    """


def OnNoteOn(msg: FlMidiMsg) -> None:
    """
    Called after {{docs_url_fn[callbacks.OnMidiMsg]}} for note-on MIDI events.

    ## Args

    * `msg` ({{docs_url_attr[fl_classes.FlMidiMsg]}}): incoming note-on MIDI message.

    Included since API Version 1.
    """


def OnNoteOff(msg: FlMidiMsg) -> None:
    """
    Called after {{docs_url_fn[callbacks.OnMidiMsg]}} for note-off MIDI events.

    ## Args

    * `msg` ({{docs_url_attr[fl_classes.FlMidiMsg]}}): incoming note-off MIDI message.

    Included since API Version 1.
    """


def OnControlChange(msg: FlMidiMsg) -> None:
    """
    Called after {{docs_url_fn[callbacks.OnMidiMsg]}} for control change (CC)
    MIDI events.

    ## Args

    * `msg` ({{docs_url_attr[fl_classes.FlMidiMsg]}}): incoming control change MIDI message.

    Included since API Version 1.
    """


def OnProgramChange(msg: FlMidiMsg) -> None:
    """
    Called after {{docs_url_fn[callbacks.OnMidiMsg]}} for program change MIDI events.

    ## Args

    * `msg` ({{docs_url_attr[fl_classes.FlMidiMsg]}}): incoming program change MIDI message.

    Included since API Version 1.
    """


def OnPitchBend(msg: FlMidiMsg) -> None:
    """
    Called after {{docs_url_fn[callbacks.OnMidiMsg]}} for pitch bend MIDI events.

    ## Args

    * `msg` ({{docs_url_attr[fl_classes.FlMidiMsg]}}): incoming pitch bend MIDI message.

    Included since API Version 1.
    """


def OnKeyPressure(msg: FlMidiMsg) -> None:
    """
    Called after {{docs_url_fn[callbacks.OnMidiMsg]}} for key pressure (note
    after-touch) MIDI events.

    ## Args

    * `msg` ({{docs_url_attr[fl_classes.FlMidiMsg]}}): incoming MIDI message.

    Included since API Version 1.
    """


def OnChannelPressure(msg: FlMidiMsg) -> None:
    """
    Called after {{docs_url_fn[callbacks.OnMidiMsg]}} for channel pressure
    (channel after-touch) MIDI events.

    ## Args

    * `msg` ({{docs_url_attr[fl_classes.FlMidiMsg]}}): incoming MIDI message.

    Included since API Version 1.
    """


def OnMidiOutMsg(msg: FlMidiMsg) -> None:
    """
    Called when MIDI messages are sent from the
    [MIDI Out plugin](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/plugins/MIDI%20Out.htm).
    to the connected MIDI device.

    TODO: Test this more to document it better

    ## Args

    * `msg` ({{docs_url_attr[fl_classes.FlMidiMsg]}}): outgoing MIDI message?

    Included since API Version 1.
    """


def OnIdle() -> None:
    """
    Called frequently (roughly once every 20ms). Scripts can use this callback
    to perform small tasks (such as animating controller LEDs or updating
    activity meters).

    !!! WARNING
        If this function runs too slowly, it can cause your script to lag, as
        FL Studio will get behind in the event loop, meaning that your script
        won't receive incoming MIDI messages fast enough. Be careful to keep
        operations performed within this callback minimal.

    Included since API Version 1.
    """


# I don't like that I have to hard-code these values -- need to find a way to
# reference the constants from midi.py directly.
def OnProjectLoad(status: Literal[0, 100, 101]) -> None:
    """
    Called when a project is loaded.

    ## Args

    * `status` (`int`): the status of the load operation.

          * {{docs_url_attr[midi.PL_Start]}}: project loading started
          * {{docs_url_attr[midi.PL_LoadOk]}}: project loaded successfully
          * {{docs_url_attr[midi.PL_LoadError]}}: project failed to load

    Included since API Version 16.
    """


def OnRefresh(flags: int) -> None:
    """
    Called when certain events occur within FL Studio. Scripts should use the
    provided flags to update required interfaces on their associated
    controllers.

    `flags` values will be a bitwise combination of the
    {{docs_url_page("OnRefresh flags", "midi_controller_scripting/midi/on refresh flags")}}.

    ## Args

    * `flags` (`int`): flags to represent the changes in FL Studio's state.

    Included since API Version 1.
    """


def OnDoFullRefresh() -> None:
    """
    Similar to {{docs_url_fn[callbacks.OnRefresh]}}, but everything should be
    updated.

    Included since API Version 1.
    """


def OnUpdateBeatIndicator(value: Literal[0, 1, 2]) -> None:
    """
    Called when the beat indicator should be updated.

    ## Args

    * `value` (`Literal[0, 1, 2]`):

          * `0`: off (paused or half-beat)
          * `1`: bar
          * `2`: beat

    Included since API Version 1.
    """


def OnDisplayZone() -> None:
    """
    Called when the playlist zone has changed

    Included since API Version 1.
    """


def OnUpdateLiveMode(lastTrack: int) -> None:
    """
    Called when something about performance mode has changed.

    ## Args

    * `lastTrack` (`int`): ???

    Included since API Version 1.
    """


def OnDirtyMixerTrack(index: int) -> None:
    """
    Called when a mixer track has changed status.

    Do not handle refreshing the track (leave that for {{docs_url_fn[callbacks.OnRefresh]}}),
    but collect information about dirty tracks.

    ## Args

    * `index` (`int`): index of dirty track (or `-1` for all tracks)

    Included since API Version 1.
    """


def OnDirtyChannel(index: int) -> None:
    """
    Called when a channel on the channel rack has changed status.

    Do not handle refreshing the channel (leave that for {{docs_url_fn[callbacks.OnRefresh]}}),
    but collect information about dirty channels.

    ## Args

    * `index` (`int`): index of dirty channel (or `-1` for all channels)

    Included since API Version 16.
    """


def OnFirstConnect() -> None:
    """
    Called when the device is connected for the first time ever.

    Included since API Version 17.
    """


def OnUpdateMeters() -> None:
    """
    Called when peak meters need to be updated.

    In order to receive this callback, scripts must call {{docs_url_fn[device.setHasMeters]}}
    within {{docs_url_fn[callbacks.OnInit]}}.

    Included since API Version 1.
    """


def OnWaitingForInput() -> None:
    """
    Called when FL Studio is in [waiting mode](https://www.image-line.com/support/flstudio_online_manual/html/toolbar_panels.htm#panel_shortcuticons_wait)

    Included since API Version 1.
    """


def OnSendTempMsg(message: str, duration: int) -> None:
    """
    Called when a hint message should be displayed on the controller.

    ## Args

    * `message` (`str`): message to display

    * `duration` (`int`): duration (in ms)

    Included since API Version 1.
    """
