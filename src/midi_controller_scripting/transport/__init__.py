"""
{{module_title[transport]}}

The `transport` module contains functions for controlling FL Studio's
transport, including playback, song position, loop mode and recording.

For example, this code would set FL Studio into song mode, enable recording,
then start playback:

```py
import transport

transport.setLoopMode()
transport.record()
transport.start()
```
"""
from typing import Literal, overload

import midi


def start() -> None:
    """
    Start or pause playback (play/pause).

    Included since API version 1.
    """


def stop() -> None:
    """
    Stop playback.

    Included since API version 1.
    """


def isPlaying() -> bool:
    """
    Returns `True` if playback is currently occurring.

    ## Returns

    * `bool`: whether playback is active.

    Included since API version 1.
    """
    return False


def record() -> None:
    """
    Toggles recording.

    Included since API version 1.
    """


def isRecording() -> bool:
    """
    Returns whether recording is enabled.

    ## Returns

    * `bool`: whether recording is enabled.

    Included since API version 1.
    """
    return False


def getLoopMode() -> int:
    """
    Returns the current looping mode.

    ## Returns

    * `int`: looping mode:
          * `0`: Pattern.

          * `1`: Song.

    Included since API version 1.
    """
    return 0


def setLoopMode() -> None:
    """
    Toggles the looping mode between pattern and song.

    Included since API version 1.
    """


def globalTransport(
    command: int,
    value: int,
    pmeflags: int = midi.PME_System,
    flags=midi.GT_All,
) -> int:
    """
    Used as a generic way to run transport commands if a specific function
    doesn't exist for it.

    ## WARNING

    * It is not recommended to use this function if a dedicated
      function is available for it. Its usage can make code difficult to read and
      comprehend. Almost all functionality provided by this function can be done
      more easily and cleanly by using the dedicated functions.

    ## Args

    * `command` (`int`): command to execute, refer to {{fl_manual_anchor[globalTransportCommands]}}.

    * `value` (`int`): ???

    * `pmeflags` (`int`, optional): current PME Flags. Defaults to
      `midi.PME_System`.

    * `flags` (`int`, optional): ??? refer to {{fl_manual_anchor[globalTransportFlags]}}.

    ## Returns

    * `int`: ???

    Included since API version 1.
    """
    return 0


@overload
def getSongPos(mode: Literal[-1] = -1) -> float:
    ...


@overload
def getSongPos(mode: Literal[0, 1, 2, 3, 4, 5]) -> int:
    ...


def getSongPos(mode: int = -1) -> 'float | int':
    """
    Returns the playback position.

    ## Note

    * This will get the position in the song in song mode, or the position
      in the pattern, depending on the state of {{docs_url_fn[transport.getLoopMode]}}.

    ## Args

    * `mode` (`int`, optional): mode for return:
          * [default] (`-1`):  {{docs_url_page("fractional time", "midi_controller_scripting/tutorials/time_units/#fractional")}}. Returns as `float`.

          * `SONGLENGTH_MS` (`0`): milliseconds (as `int`).

          * `SONGLENGTH_S` (`1`): seconds (as `int`).

          * `SONGLENGTH_ABSTICKS` (`2`): {{docs_url_page("absolute ticks", "midi_controller_scripting/tutorials/time_units/#ticks")}} (as `int`).

          * `SONGLENGTH_BARS` (`3`): {{docs_url_page("B:S:T format", "midi_controller_scripting/tutorials/time_units/#bst")}}, bars component (as `int`).

          * `SONGLENGTH_STEPS` (`4`): {{docs_url_page("B:S:T format", "midi_controller_scripting/tutorials/time_units/#bst")}}, steps component (as `int`).

          * `SONGLENGTH_TICKS` (`5`): {{docs_url_page("B:S:T format", "midi_controller_scripting/tutorials/time_units/#bst")}}, ticks component (as `int`).

    ## Example Usage

    The {{docs_url_fn[transport.getSongPosHint]}} function (returning time in
    {{docs_url_page("B:S:T", "midi_controller_scripting/tutorials/time_units/#bst")}}
    (bars-steps-ticks) format) can be emulated through making three calls to
    the function as follows:

    ```py
    bars = transport.getSongPosition(3)
    steps = transport.getSongPosition(4)
    ticks = transport.getSongPosition(5)
    overall_str = f"{bars}:{steps}:{ticks}"
    ```

    ## Returns

    * `float` or `int`: song position.

    Included since API version 1, with optional parameter added in API version
    3.
    """
    return 0


@overload
def setSongPos(position: float, mode: Literal[-1] = -1) -> None:
    ...


@overload
def setSongPos(position: int, mode: Literal[0, 1, 2, 3, 4, 5]) -> None:
    ...


def setSongPos(position: 'float | int', mode: int = -1) -> None:
    """
    Sets the playback position.

    This will set the position in the song in song mode, or the position
    in the pattern.

    ## Args

    * `position` (`float` or `int`): new song position (type depends on
      `mode`).

    * `mode` (`int`, optional): mode for `position`:
          * [default] (`-1`):  {{docs_url_page("fractional time", "midi_controller_scripting/tutorials/time_units/#fractional")}}. Requires position to be passed as type `float`.

          * `SONGLENGTH_MS` (`0`): milliseconds (as `int`)

          * `SONGLENGTH_S` (`1`): seconds (as `int`).

          * `SONGLENGTH_ABSTICKS` (`2`): {{docs_url_page("absolute ticks", "midi_controller_scripting/tutorials/time_units/#ticks")}} (as `int`).

    Included since API version 1, with optional parameter added in API version
    4.
    """


def getSongLength(mode: int) -> int:
    """
    Returns the total length of the song.

    This only applies to the full song, not to the currently selected pattern
    when in pattern mode. To get the length of the current pattern, use
    `patterns.getPatternLength()` with the index of the current pattern.

    ## Args

    * `mode` (`int`): mode for length:
          * `SONGLENGTH_MS` (`0`): milliseconds.

          * `SONGLENGTH_S` (`1`): seconds.

          * `SONGLENGTH_ABSTICKS` (`2`): {{docs_url_page("absolute ticks", "midi_controller_scripting/tutorials/time_units/#ticks")}}.

          * `SONGLENGTH_BARS` (`3`): {{docs_url_page("B:S:T format", "midi_controller_scripting/tutorials/time_units/#bst")}}, bars component.

          * `SONGLENGTH_STEPS` (`4`): {{docs_url_page("B:S:T format", "midi_controller_scripting/tutorials/time_units/#bst")}}, steps component.

          * `SONGLENGTH_TICKS` (`5`): {{docs_url_page("B:S:T format", "midi_controller_scripting/tutorials/time_units/#bst")}}, ticks component.

    ## Returns

    * `int`: song length.

    Included since API version 3.
    """
    return 0


def getSongPosHint() -> str:
    """
    Returns a hint for the current playback position in .

    This applies to both pattern mode and song mode.

    Note that unlike FL Studio's time panel, this function won't return
    positions past the end of a song or pattern, instead returning the position
    of the last tick within the song/pattern. If you want to emulate the
    behavior of the time panel, consider using
    {{docs_url_fn[playlist.getVisTimeBar]}}, {{docs_url_fn[playlist.getVisTimeStep]}}
    and {{docs_url_fn[playlist.getVisTimeTick]}} instead.

    ## Returns

    * `str`: song position.

    Included since API version 1.
    """
    return ""


def markerJumpJog(value: int, flags: int = midi.GT_All) -> None:
    """
    Jump to a marker position, where `value` is an delta (increment) value.

    ## Args

    * `value` (`int`): delta.

    * `flags` (`int`, optional): ??? refer to the {{fl_manual_anchor[globalTransportFlags]}}.

    Included since API version 1.
    """


def markerSelJog(value: int, flags: int = midi.GT_All) -> None:
    """
    Select a marker, where `value` is an delta (increment) value.

    ## Args

    * `value` (`int`): delta.

    * `flags` (`int`, optional): ??? refer to the {{fl_manual_anchor[globalTransportFlags]}}.

    Included since API version 1.
    """


def getHWBeatLEDState() -> int:
    """
    Returns the state of the beat indicator.

    ## HELP WANTED

    * I couldn't get this to return anything other than zero.

    ## Returns

    * `int`: beat indicator state.

    Included since API version 1.
    """
    return 0


def rewind(startStop: int, flags: int = midi.GT_All) -> None:
    """
    Rewinds the playback position.

    Rewinding should be considered as a toggle. All calls to this function
    beginning rewinding with the `SS_Start` or `SS_StartStep` should have a pair
    call where rewinding is stopped using the `SS_Stop` option, otherwise FL
    Studio will rewind forever.

    ## Args

    * `startStop` (`int`): start-stop option:
          * `SS_Stop` (`0`): Stop movement.

          * `SS_StartStep` (`1`): Start movement, but only if FL Studio is in step editing mode.

          * `SS_Start` (`2`); Start movement.

    * `flags` (`int`, optional): ??? refer to the {{fl_manual_anchor[globalTransportFlags]}}.

    Included since API version 1.
    """


def fastForward(startStop: int, flags: int = midi.GT_All) -> None:
    """
    Fast-forwards the playback position.

    Fast-forwarding should be considered as a toggle. All calls to this
    function beginning fast-forwarding with the `SS_Start` or `SS_StartStep`
    should have a pair call where fast-forwarding is stopped using the
    `SS_Stop` option, otherwise FL Studio will fast-forward forever.

    ## Args

    * `startStop` (`int`): start-stop option:
          * `SS_Stop` (`0`): Stop movement.

          * `SS_StartStep` (`1`): Start movement, but only if FL Studio is in step editing mode.

          * `SS_Start` (`2`); Start movement.

    * `flags` (`int`, optional): ??? refer to the {{fl_manual_anchor[globalTransportFlags]}}.

    Included since API version 1.
    """


def continuousMove(speed: int, startStop: int) -> None:
    """
    Sets playback speed, allowing a scrub-like functionality.

    Scrubbing should be considered as a toggle. All calls to this
    function beginning scrubbing with the `SS_Start` or `SS_StartStep`
    should have a pair call where scrubbing is stopped using the `SS_Stop`
    option, otherwise FL Studio will scrub forever.

    ## Args

    * `speed` (`int`): speed multiplier. Negative means reverse, `0` is
       stopped, and `1` is normal playback speed.

    * `startStop` (`int`): start-stop option:
          * `SS_Stop` (`0`): Stop movement.

          * `SS_StartStep` (`1`): Start movement, but only if FL Studio is in step editing mode.

          * `SS_Start` (`2`); Start movement.

    Included since API version 1.
    """


def continuousMovePos(speed: int, startStop: int) -> None:
    """
    Sets playback speed, allowing a scrub-like functionality.

    ## HELP WANTED

    * How is this different to `continuousMove()`?

    Scrubbing should be considered as a toggle. All calls to this
    function beginning scrubbing with the `SS_Start` or `SS_StartStep`
    should have a pair call where scrubbing is stopped using the `SS_Stop`
    option, otherwise FL Studio will scrub forever.

    ## Args

    * `speed` (`int`): speed multiplier. Negative means reverse, `0` is
      stopped, and `1` is normal playback speed.

    * `startStop` (`int`): start-stop option:
          * `SS_Stop` (`0`): Stop movement.

          * `SS_StartStep` (`1`): Start movement, but only if FL Studio is in step editing mode.

          * `SS_Start` (`2`); Start movement.

    Included since API version 2.
    """


def setPlaybackSpeed(speedMultiplier: float) -> None:
    """
    Sets a playback speed multiplier.

    This differs from the `continuousMove` function as it only controls
    speed when playback is active, rather than scrubbing through song or
    pattern regardless of whether playback is active.

    ## Args

    * `speedMultiplier` (`float`): speed:
          * `1.0`: Normal speed.

          * `0.25`: Minimum speed.

          * `4.0`: Maximum speed.

    Included since API version 1.
    """


# Clean up imports
del midi, overload, Literal
