"""
Mixer > Properties

Properties of the mixer and other aspects of FL Studio as a whole
"""
from typing import Optional, overload, Literal
import midi


def getTrackInfo(mode: int) -> int:
    """
    Returns the index of a special mixer track depending on `mode`.

    This function can serve to help potentially future-proof scripts by
    ensuring that they continue to use the correct indexes for mixer tracks.

    ## Args

    * `mode` (`int`): Determines the type of information provided.

          * `TN_Master` (`0`): Index of master track.

          * `TN_FirstIns` (`1`): Index of first insert track.

          * `TN_LastIns` (`2`): Index of last insert track.

          * `TN_Sel` (`3`): Index of the "current" track (the one with the
            large peak meter docked to the left).

    ## Returns

    * `int`: requested track index.

    Included since API version 1.
    """
    return 0


def trackCount() -> int:
    """
    Returns the number of tracks available on the mixer.

    The value returned by this function includes master and "current track"
    tracks.

    The range of accessible tracks is from `0` to `trackCount() - 1`.

    ## Returns

    * `int`: number of tracks.

    Included since API version 1.
    """
    return 0


def getSongStepPos() -> int:
    """
    Returns the current position in the song, measured in steps.

    ## Returns

    * `int`: song position.

    Included since API version 1.
    """
    return 0


@overload
def getCurrentTempo(asInt: Literal[True]) -> int:
    ...


@overload
def getCurrentTempo(asInt: Literal[False] = False) -> float:
    ...


def getCurrentTempo(asInt: bool = False) -> 'int | float':
    """
    Returns the current tempo of the song.

    ## Args

    * `asInt` (`bool`, optional): whether to return the tempo as an `int`
      (`True`) or not (`False`). Defaults to `False`.

    ## Returns

    * `int` or `float`: Current tempo.

    Included since API version 1.
    """
    return 0


def getRecPPS() -> int:
    """
    Returns the recording PPS.

    This value is determined by the the timebase (PPQ) value of the current
    project.

    ## Returns

    * `int`: recording PPS.

    Included since API version 1.
    """
    return 0


@overload
def getSongTickPos(mode: Literal[0] = 0) -> int:
    ...


@overload
def getSongTickPos(mode: Literal[1, 2]) -> float:
    ...


def getSongTickPos(mode: int = midi.ST_Int) -> 'int | float':
    """
    Returns the current position in the song, measured in ticks.

    ## Args

    * `mode` (`int`, optional): the format to return the tick position in. See
      {{docs_url_page("the documentation", "midi_controller_scripting/midi/song tick modes")}}.

    ## Returns

    * `int` or `float`: song position in ticks.

    Included since API version 1.
    """
    return 0


def getLastPeakVol(section: int) -> float:
    """
    Returns last peak volume.

    ## Args

    * `section` (`int`): audio channel

          * `0`: left channel.

          * `1`: right channel.

    ## Returns

    * `float`: last peak volume (`0.0` for silence, `1.0` for 0 dB, `>1.0` for
      clipping).

    Included since API version 9.
    """
    return 0.0


def focusEditor(index: int, plugIndex: int):
    """
    Focus the editor the effect plugin at the given location.

    ## Args

    * `index` (`int`): track index of plugin.

    * `plugIndex` (`int`): mixer slot index of plugin.

    Included since API Version 25.
    """


def getActiveEffectIndex() -> Optional[tuple[int, int]]:
    """
    Returns the index of the active effects plugin, or None if there isn't one.

    ## Returns

    * `tuple[int, int]`: `(index, plugIndex)`, or `None`.

    Included since API Version 25.
    """
    return None
