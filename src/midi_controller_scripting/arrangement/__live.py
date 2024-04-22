"""
These functions allow for you to access information about the live (performance
mode) selection for an arrangement.
"""


def liveSelection(time: int, stop: bool) -> None:
    """
    Set a live selection point at `time`.

    Set `stop` to True, to use end point of the selection (instead of start).

    ## HELP WANTED

    * A better explanation would be good.

    ## Args

    * `time` (`int`): ???

    * `stop` (`bool`): ???

    Included since API version 1.
    """


def liveSelectionStart() -> int:
    """
    Returns the start time of the current live selection.

    ## Returns

    * `int`: start of selection time.

    Included since API version 1.
    """
    return 0
