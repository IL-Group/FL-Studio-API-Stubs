"""
# device > util

Utility functions in device module
"""


def createRefreshThread() -> None:
    """
    Start a threaded refresh of the entire MIDI device.

    ## HELP WANTED

    * What do refresh threads do?

    Included since API version 1
    """


def destroyRefreshThread() -> None:
    """
    Stop a previously started threaded refresh.

    ## HELP WANTED

    * What do refresh threads do?

    Included since API version 1
    """


def fullRefresh() -> None:
    """
    Trigger a previously started threaded refresh. If there is none, the
    refresh is triggered immediately.

    ## HELP WANTED

    * What do refresh threads do?

    Included since API version 1
    """


def isDoubleClick(index: int) -> bool:
    """
    Returns whether the function was called with the same index shortly
    before, indicating a double click.

    ## Args

    * `index` (`int`): a unique value representing the current control.

    ## Returns

    * `bool`: whether the event was a double click.

    Included since API version 1.
    """
    return False


def setHasMeters() -> None:
    """
    Registers the controller as having peak meters, meaning that the
    `OnUpdateMeters()` function will be called. This function should be called
    within `OnInit()`.

    Included since API version 1.
    """


def baseTrackSelect(index: int, step: int) -> None:
    """
    Base track selection (for control surfaces). Set `step` to `MaxInt` to
    reset.

    ## HELP WANTED

    * What does this do?

    ## Args:
     * `index` (`int`): ???

     * `step` (`int`): ???

    Included since API version 1.
    """


def hardwareRefreshMixerTrack(index: int) -> None:
    """
    Hardware refresh mixer track at `index`.

    ## HELP WANTED

    * What does this mean?

    ## Args

    * `index` (`int`): track index. `-1` refreshes all tracks.

    Included since API version 1.
    """
