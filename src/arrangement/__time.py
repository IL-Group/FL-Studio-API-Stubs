"""
# Arrangement / Time

Functions for getting information about the current time in an arrangement.
"""


def currentTime(snap: int) -> int:
    """
    Returns the current time in the current arrangement, in terms of ticks.

    Note that by default, most projects have a PPQ of 96. Use
    {{docs_url_fn[general.getRecPPQ]}} to get the PPQ of the project.

    ## Args

    * `snap` (`int`): whether to get time snapped to grid.

    ## Returns

    * `int`: current time.

    Included since API version 1.
    """
    return 0


def currentTimeHint(
    mode: int,
    time: int,
    setRecPPB: int = 0,
    isLength: int = 0,
) -> str:
    """
    Returns a hint string for the given time, formatted as: `"Bar:Beat?:Tick"`.

    ## Args

    * `mode` (`int`): pattern mode (`0`) or song mode (`1`).

    * `time` (`int`): time in ticks.

    * `setRecPPB` (`int`, optional): ???. Defaults to ?.

    * `isLength` (`int`, optional): ???. Defaults to 0.

    ## Returns

    * `str`: current time as string hint.

    Included since API version 1.
    """
    return ""
