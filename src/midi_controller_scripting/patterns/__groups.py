"""
patterns > groups

Managing pattern groups
"""


def getActivePatternGroup() -> int:
    """
    Returns the index of the currently-selected pattern group.

    The default "All patterns" grouping has index `-1`. User-defined pattern
    groups have indexes starting from `0`.

    ## Returns

    * `int`: index of the current pattern group.

    Included since API Version 28.
    """
    return -1


def getPatternGroupCount() -> int:
    """
    Returns the number of user-defined pattern groups.

    The default "All patterns" grouping is not included.

    ## Returns

    * `int`: number of pattern groups.

    Included since API Version 28.
    """
    return 0


def getPatternGroupName(index: int, /) -> str:
    """
    Returns the name of the pattern group at index.

    The default "All patterns" group's name cannot be accessed.

    ## Returns

    * `str`: name of pattern group.

    Included since API Version 28.
    """
    return ""


def getPatternsInGroup(index: int, /) -> tuple[int, ...]:
    """
    Returns a tuple containing all the patterns in the group at index.

    The default "All patterns" group returns a tuple containing all the
    patterns that haven't been added to any other groups.

    ## Returns

    * `tuple[int, ...]`: tuple of patterns in group.

    Included since API Version 28.
    """
    return tuple()
