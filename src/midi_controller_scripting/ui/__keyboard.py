"""
The keyboard functions within the `ui` module are used for emulating
key-presses within FL Studio. They can be used to perform common
keyboard-related actions such as copying and pasting, and dismissing dialog
boxes.

!!! warning

    In versions of FL Studio before FL Studio 21.0, these functions had the
    capability to interact with applications outside of FL Studio on Windows.

    They now only interact with FL Studio, even if it isn't the active window.
"""


def cut() -> int:
    """
    Cut the selection.

    ## Returns

    * `int`: ?

    Included since API version 1.
    """
    return 0


def copy() -> int:
    """
    Copy the selection.

    ## Returns

    * `int`: ?

    Included since API version 1.
    """
    return 0


def paste() -> int:
    """
    Paste the selection.

    ## Returns

    * `int`: ?

    Included since API version 1.
    """
    return 0


def insert() -> int:
    """
    Press the insert key.

    ## Returns

    * `int`: ?

    Included since API version 1.
    """
    return 0


def delete() -> int:
    """
    Press the delete key.

    ## Returns

    * `int`: ?

    Included since API version 1.
    """
    return 0


def enter() -> int:
    """
    Press the enter key.

    ## Returns

    * `int`: ?

    Included since API version 1.
    """
    return 0


def escape() -> int:
    """
    Press the escape key.

    ## Returns

    * `int`: ?

    Included since API version 1.
    """
    return 0


def yes() -> int:
    """
    Press the y key.

    ## Returns

    * `int`: ?

    Included since API version 1.
    """
    return 0


def no() -> int:
    """
    Press the n key.

    ## Returns

    * `int`: ?

    Included since API version 1.
    """
    return 0


def up(value: int = 1) -> int:
    """
    Press the up arrow key.

    ## HELP WANTED:
    * What does the `value` variable do?

    ## Args

    * `value` (`int`, optional): ???. Defaults to 1.

    ## Returns

    * `int`: ?

    Included since API version 1, with option parameter since API version 4.
    """
    return 0


def down(value: int = 1) -> int:
    """
    Press the down arrow key.

    ## HELP WANTED:
    * What does the `value` variable do?

    ## Args

    * `value` (`int`, optional): ???. Defaults to 1.

    ## Returns

    * `int`: ?

    Included since API version 1, with option parameter since API version 4
    """
    return 0


def left(value: int = 1) -> int:
    """
    Press the left arrow key.

    ## HELP WANTED:
    * What does the `value` variable do?

    ## Args

    * `value` (`int`, optional): ???. Defaults to 1.

    ## Returns

    * `int`: ?

    Included since API version 1, with option parameter since API version 4
    """
    return 0


def right(value: int = 1) -> int:
    """
    Press the right arrow key.

    ## HELP WANTED:
    * What does the `value` variable do?

    ## Args

    * `value` (`int`, optional): ???. Defaults to 1.

    ## Returns

    * `int`: ?

    Included since API version 1, with option parameter since API version 4
    """
    return 0
