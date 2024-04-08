"""
Mixer > Selection

Functions for interacting with the mixer selection.
"""


def trackNumber() -> int:
    """
    Returns the index of the first currently selected mixer track.

    ## Returns

    * `int`: selected mixer track.

    Included since API version 1.
    """
    return 0


def setTrackNumber(trackNumber: int, flags: int = 0) -> None:
    """
    Selects the mixer track at `trackNumber`.

    ## Note

    * All functionality except for scrolling flag can be replicated more
      easily using {{docs_url_fn[mixer.selectTrack]}}.

    ## Args

     * `trackNumber` (`int`): the track index to select.

     * `flags` (`int`, optional): Options to do with new track selection.
          * `curfxScrollToMakeVisible` (`1`): Scroll to make the
            newly-selected track visible.

          * `curfxCancelSmoothing` (`2`): Effect unknown.

          * `curfxNoDeselectAll` (`4`): Prevent the deselection of other
            selected tracks??? Doesn't seem to work.

          * `curfxMinimalLatencyUpdate` (`8`): Effect unknown.

        Defaults to `0`.

    Included since API version 1.
    """


def isTrackSelected(index: int) -> bool:
    """
    Returns whether the track at `index` is selected.

    ## Args

    * `index` (`int`): track index.

    ## Returns

    * `bool`: whether the track is selected.

    Included since API version 1.
    """
    return False


def selectTrack(index: int) -> None:
    """
    Toggles whether the track at `index` is selected.

    ## Args

    * `index` (`int`): track index.

    Included since API version 1.
    """


def selectAll() -> None:
    """
    Selects all tracks.

    Included since API version 1.
    """


def deselectAll() -> None:
    """
    Deselects all tracks.

    Included since API version 1.
    """


def setActiveTrack(index: int):
    """
    Exclusively selects the mixer track at index.

    This means any other selected tracks will be deselected.

    ## Args

    * `index` (`int`): track index.

    Included since API Version 27.
    """
