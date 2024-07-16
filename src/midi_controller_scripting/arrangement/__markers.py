"""
# Arrangement / Markers

Functions for interacting with markers within the arrangement.
"""


def jumpToMarker(delta: int, select: bool) -> None:
    """
    Jumps to the marker at the given delta index.

    For example, to jump to the previous marker, use a delta of `-1`.

    ## Args

    * delta (`int`): relative marker index.

    * select (`bool`): whether to select the marker.

    Included since API version 1.
    """


def getMarkerName(index: int) -> str:
    """
    Returns the name of the marker at `index`.

    Note that this uses an absolute index, not a relative index.

    ## Args

    * index (`int`): marker index.

    ## Returns

    * `str`: name of the marker.

    Included since API version 1.
    """
    return ""


def addAutoTimeMarker(time: int, name: str) -> None:
    """
    Add an automatic time marker at the given `time`.

    ## Args

    * `time` (`int`): time, in
      {{docs_url_page("absolute ticks", "midi_controller_scripting/tutorials/time_units/#ticks")}}.
      A value can be gathered using the {{docs_url_fn[transport.getSongPos]}}
      function.

    * `name` (`str`): name of new marker.

    Included since API version 1.
    """
