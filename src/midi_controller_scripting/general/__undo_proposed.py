"""
undo.py

What I imagine undo/redo with the FL Studio API should be like.

If this ended up being put into a module called `undo` I would remove `undo`
from most of the function names to make it more clean and readable (eg people
would call undo.toggle() rather than undo.toggleUndo()).
"""


def undo() -> bool:
    """
    Jump one element backwards in the undo history. Returns whether anything
    was undone (ie False if nothing to undo).
    """
    return False


def redo() -> bool:
    """
    Jump one element forwards in the undo history. Returns whether anything
    was redone (ie False if nothing to redo).
    """
    return False


def toggleUndo() -> bool:
    """
    Undo if there's nothing to redo, otherwise redo. Returns True if we undid
    something and False if we redid something (or if there was nothing to
    undo/redo)
    """
    return False


def getUndoPosition() -> int:
    """
    Returns the current undo position, with 0 being the most recent element in
    the history.
    """
    return 0


def setUndoPosition(index: int) -> bool:
    """
    Jump to a particular index in the undo history. If that index is out of
    range, jump to the closest in-range value. Returns True if we jumped to
    that particular index, or False if we jumped to the closest in-range value.
    """
    return False


def setUndoPositionRelative(delta: int) -> bool:
    """
    Jump by a particular index relative to the current index. If that index is
    out of range, jump to the closest in-range value. Returns True if we jumped
    to that particular index, or False if we jumped to the closest in-range
    value.
    """
    # Would be implemented as
    return setUndoPosition(getUndoPosition() + delta)


def getUndoHistoryLength() -> int:
    """
    Returns the number of items in the undo history.
    """
    return 0


def trimUndoHistoryNew(amount: int) -> int:
    """
    Removes the newest `n = amount` elements from the undo history. Returns the
    new number of elements in the history.
    """
    return 0


def trimUndoHistoryOld(amount: int) -> int:
    """
    Removes the oldest `n = amount` elements from the undo history. Returns the
    new number of elements in the history.
    """
    return 0


def saveUndo(name: str, flags: int, update: bool = True) -> None:
    """
    Add the current state of FL Studio to the undo history. Same as the current
    function of th same name
    """


def getUndoElementName(index: int) -> str:
    """
    Returns the name of the element at index in the undo history.
    """
    return ""


def getUndoElementFlags(index: int) -> int:
    """
    Returns the flags of the element at index in the undo history.
    """
    return 0
