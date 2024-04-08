"""
patterns > properties

Managing properties of patterns
"""

from typing import Optional


def patternNumber() -> int:
    """
    Returns the index for the currently active pattern.

    This is the pattern where notes and step sequencing will be modified. It is
    usually equal to the most recently selected pattern. If that pattern is
    deselected, it the pattern number will return to the first selected
    pattern, or if there are no selections, it will remain the same.

    ## Returns

    * `int`: index of the currently active pattern.

    Included since API version 1.
    """
    return 0


def patternCount() -> int:
    """
    Returns the number of patterns in the project which have been modified from
    their default state.

    ## Warning

    There is no guarantee that these patterns are all adjacent, as the API
    allows for the modification of patterns at any index at any time. You
    should only rely on this pattern for indexes if your script manages
    patterns in a responsible manner.

    ## Returns

    * `int`: the number of patterns.

    Included since API version 1.
    """
    return 0


def patternMax() -> int:
    """
    Returns the maximum number of patterns that can be created. In FL Studio
    20, this is 999.

    ## Returns

    * `int`: max number of patterns.

    Included since API version 1.
    """
    return 0


def getPatternName(index: int) -> str:
    """
    Returns the name of the pattern at `index`.

    ## Args

    * `index` (`int`): pattern index.

    ## Returns

    * `str`: name of pattern.

    Included since API version 1.
    """
    return ""


def setPatternName(index: int, name: str) -> None:
    """
    Sets the name of pattern at `index`.

    Setting the name to an empty string will reset the name of the pattern to
    its default.

    ## Args

    * index (`int`): index of pattern.

    * name (`str`): new name.

    Included since API version 1.
    """


def getPatternColor(index: int) -> int:
    """
    Returns the color of the pattern at `index`.

    {{note[colors]}}

    ## Args

    * `index` (`int`): pattern index.

    ## Returns

    * `int`: color of pattern (0x--BBGGRR).

    Included since API version 1.
    """
    return 0


def setPatternColor(index: int, color: int) -> None:
    """
    Sets the color of the pattern at `index`.

    {{note[colors]}}

    ## Args

    * `index` (`int`): pattern index.

    * `color` (`int`): color of pattern (0x--BBGGRR).

    Included since API version 1.
    """


def getPatternLength(index: int) -> int:
    """
    Returns the length of the pattern at `index` in beats.

    ## Args

    * `index` (`int`): pattern index.

    ## Returns

    * `int`: length of pattern in beats.

    Included since API version 1.
    """
    return 0


def jumpToPattern(index: int) -> None:
    """
    Scroll the patterns list to the pattern at `index`, then activate it and
    select it if it isn't already selected.

    ## Note

    * It is possible to jump to non-existent patterns. They will be created at
      the requested index. Script writers should be careful not to create
      patterns at unusual indexes. For example, creating a "Pattern 999" as the
      second pattern in a project would be somewhat confusing for user.

    ## Args

    * index (`int`): pattern index.

    Included since API version 1.
    """


def findFirstNextEmptyPat(flags: int, x: int = -1, y: int = -1) -> None:
    """
    Selects the first or next empty pattern.

    ## HELP WANTED

    * What do the `x` and `y` values do?

    ## Args

    * `flags` (`int`):
          * `FFNEP_FindFirst` (`0`): Find first pattern.

          * `FFNEP_DontPromptName` (`2`): Don't prompt pattern name.

    * `x` (`int`, optional): ???. Defaults to -1.

    * `y` (`int`, optional): ???. Defaults to -1.

    Included since API version 1.
    """


def isPatternSelected(index: int) -> bool:
    """
    Returns whether the pattern at `index` is selected.

    ## Args

    * `index` (`int`): pattern index.

    ## Returns

    * `bool`: whether pattern is selected.

    Included since API version 2.
    """
    return False


def selectPattern(
    index: int,
    value: int = -1,
    preview: bool = False,
) -> None:
    """Selects the pattern at `index`.

    ## Args

    * `index` (`int`): pattern index.

    * `value` (`int`, optional): selection mode:
          * `-1`: Toggle (default).

          * `0`: Deselect.

          * `1`: Select.

    * `preview` (`bool`, optional): whether set FL Studio to pattern mode and
      start playback if the pattern gets selected. Defaults to `False`.

    Included since API version 2.
    """


def selectAll() -> None:
    """
    Selects all patterns.

    Hidden patterns will not be selected.

    Included since API version 2.
    """


def deselectAll() -> None:
    """
    Deselects all patterns.

    Included since API version 2.
    """


def burnLoop(index: int, storeUndo: int = 1, updateUi: int = 1) -> None:
    """
    For a pattern where looping of step sequenced channels is enabled, disable
    looping for the channel at index `i`.

    # KNOWN ISSUES

    * Once this is disabled, it cannot be reenabled, except by disabling step
      sequenced looping and reenabling it.

    ## Args

    * `index` (`int`): Index of channel to disable step sequencer looping for

    * `storeUndo` (`bool`, optional): whether to store a point in the undo
      history. Defaults to `True`.

    * `updateUi` (`bool`, optional): whether the function should do anything.
      Setting this to `False` will make nothing happen. Defaults to `True`.

    Included since API version 9
    """


def isPatternDefault(index: int) -> bool:
    """
    Returns whether the pattern at the given index has changed from the default
    empty state.

    ## Args

    * `index` (`int`): pattern index

    ## Returns

    * `bool`: whether the pattern has changed

    Included since API Version 23
    """
    return True


def clonePattern(index: Optional[int] = None):
    """
    Clones the pattern at the given index

    Note that doing so will close the piano roll, in order to prevent the user
    from making unintentional edits to the wrong pattern.

    ## Args

    * `index` (`int | None`): index of pattern. If not provided, defaults to
      the currently selected pattern.

    Included since API Version 25
    """


def getChannelLoopStyle(pattern: int, channel: int, /) -> int:
    """
    Return the loop point of the given channel for the pattern at the given
    index.

    ## WARNING

    * This function is not officially documented.

    * Giving invalid arguments to this function can cause FL Studio to crash.

    * This function does not appear to support keyword arguments.

    ## Args

    * `pattern` (`int`): pattern index (1-indexed).

    * `channel` (`int`): channel index (0-indexed).

    ## Returns

    * `int`: loop point for the channel within the pattern.

    Included since API Version ???
    """
    return 0


def setChannelLoop(channel: int, loopPoint: int, /) -> str:
    """
    Set the loop point of the given channel for the current pattern.

    ## WARNING

    * This function is not officially documented.

    * Giving invalid arguments to this function can cause FL Studio to crash.

    * This function does not appear to support keyword arguments.

    ## Args

    * `channel` (`int`): channel index.

    * `loopPoint` (`int`): loop point (or `0` to disable looping).

    ## Returns

    * `int`: new loop point value as a string.

    Included since API Version ???.
    """
    return "---"
