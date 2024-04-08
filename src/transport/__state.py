"""
transport > state

Constant states of transport
"""
from typing import overload, Literal
import midi


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
          * [default] (`-1`): as a fraction of the total length between `0` and `1` (eg `0.5` would indicate we were half-way through the song). Returns as `float`.

          * `SONGLENGTH_MS` (`0`): milliseconds (as `int`).

          * `SONGLENGTH_S` (`1`): seconds (as `int`).

          * `SONGLENGTH_ABSTICKS` (`2`): ticks (as `int`).

          * `SONGLENGTH_BARS` (`3`): bars-steps-ticks format, bars component (as `int`).

          * `SONGLENGTH_STEPS` (`4`): bars-steps-ticks format, steps component (as `int`).

          * `SONGLENGTH_TICKS` (`5`): bars-steps-ticks format, ticks component (as `int`).

    ## Example Usage

    An overall bars-steps-ticks position can be gathered through making
    three calls to the function as follows:
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
          * [default] (`-1`): as a fraction of the total length between `0`
            and `1` (eg `0.5` would indicate we were half-way through the
            song). Requires position to be passed as type `float`.

          * `SONGLENGTH_MS` (`0`): milliseconds (as `int`)

          * `SONGLENGTH_S` (`1`): seconds (as `int`).

          * `SONGLENGTH_ABSTICKS` (`2`): absolute number of ticks (as `int`).

          * `SONGLENGTH_BARS` (`3`): bars-steps-ticks format, bars component (as `int`).

          * `SONGLENGTH_STEPS` (`4`): bars-steps-ticks format, steps component (as `int`).

          * `SONGLENGTH_TICKS` (`5`): bars-steps-ticks format, ticks component (as `int`).

    ## WARNING

    * Positions currently won't work when using bars (`mode = 3`),
      steps (`mode = 4`) or ticks (`mode = 5`).

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

          * `SONGLENGTH_ABSTICKS` (`2`): ticks.

          * `SONGLENGTH_BARS` (`3`): bars-steps-ticks format, bars component.

          * `SONGLENGTH_STEPS` (`4`): bars-steps-ticks format, steps component.

          * `SONGLENGTH_TICKS` (`5`): bars-steps-ticks format, ticks component.

    ## Returns

    * `int`: song length.

    Included since API version 3.
    """
    return 0


def getSongPosHint() -> str:
    """
    Returns a hint for the current playback position as `"bars:steps:ticks"`.

    This applies to both pattern mode and song mode.

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
