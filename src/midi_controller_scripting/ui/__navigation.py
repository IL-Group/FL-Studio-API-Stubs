"""
ui > navigation

UI functions for navigating FL Studio
"""


def jog(value: int) -> int:
    """
    Jog control. Used to map a jog wheel to selections.

    ## Args

    * `value` (`int`): delta value (increment), for example:
          * `1`: next.

          * `-1`: previous.

    ## Returns

    * `int`: ?

    Included since API version 1.
    """
    return 0


def jog2(value: int) -> int:
    """
    Alternate jog control. Used to map a jog wheel to relocate.

    ## Args

    * `value` (`int`): delta value (increment), for example:
          * `1`: next.

          * `-1`: previous.

    ## Returns

    * `int`: ?

    Included since API version 1.
    """
    return 0


def strip(value: int) -> int:
    """
    Used by touch-sensitive strip controls.

    ## HELP WANTED
    * What controls does this apply to?

    ## Args

    * `value` (`int`): ???

    ## Returns

    * `int`: ?

    Included since API version 1.
    """
    return 0


def stripJog(value: int) -> int:
    """
    Touch-sensitive strip in jog mode.

    ## Args

    * `value` (`int`): delta value (increment).

    ## Returns

    * `int`: ?

    Included since API version 1.
    """
    return 0


def stripHold(value: int) -> int:
    """
    Touch-sensitive strip in hold mode.

    ## Args

    * `value` (`int`):
          * `0`: release.

          * `1`: 1-finger centered mode.

          * `2`: 2-fingers centered mode.

          * `-1`: 1-finger jog mode.

          * `-2`: 2-finger jog mode.

    ## Returns

    * `int`: ?

    Included since API version 1.
    """
    return 0


def previous() -> int:
    """
    Move selection to previous element.

    * in mixer: select previous track.

    * in channel rack: select previous channel.

    * in browser: scroll to previous item.

    * in plugin: switch to previous preset (since API version 9).

    ## Returns

    * `int`: ?

    Included since API version 1.
    """
    return 0


def next() -> int:
    """
    Move selection to next element.

    * in mixer: select next track.

    * in channel rack: select next channel.

    * in browser: scroll to next item.

    * in plugin: switch to next preset (since API version 9).

    ## Returns

    * `int`: ?

    Included since API version 1.
    """
    return 0


def moveJog(value: int) -> int:
    """
    Used to relocate items with a jog control.

    ## HELP WANTED

    * How does this differ from `jog2()`?

    ## Args

    * `value` (`int`): delta value (increment).

    ## Returns

    * `int`: ?

    Included since API version 1.
    """
    return 0


def horZoom(value: int) -> int:
    """
    Zoom horizontally by `value`.

    ## Args

    * `value` (`int`): amount to zoom by. Negative zooms out, positive zooms in.
      Larger magnitudes zoom more, but the scale doesn't seem consistent.

    ## Returns

    * `int`: ?

    Included since API version 1.
    """
    return 0


def verZoom(value: int) -> int:
    """
    Zoom vertically by `value`.

    ## Args

    * `value` (`int`): amount to zoom by. Negative zooms out, positive zooms
      in. Larger magnitudes zoom more, but the scale doesn't seem consistent.

    ## Returns

    * `int`: ?

    Included since API version 1.
    """
    return 0


def isInPopupMenu() -> bool:
    """
    Returns `True` when a popup menu is open (for example a right-click or
    drop-down menu).

    ## Returns

    * `bool`: whether a popup menu is open

    Included since API version 1.
    """
    return False


def closeActivePopupMenu() -> None:
    """
    Closes a currently-open popup menu (for example a rick-click or drop-down
    menu).

    Included since API version 1.
    """
