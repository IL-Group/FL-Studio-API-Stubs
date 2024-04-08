"""
# Screen

FL Studio built-in module.

Helper functions for controlling the screen of the AKAI FL Studio Fire MIDI
controller.

These likely aren't useful for most scripts, but if you're writing a script for
the Fire they might be handy.

## HELP WANTED

These functions are undocumented. If you know how they work, I'd massively
appreciate a pull request with improvements to the type safety and
documentation.
"""


def init(
    display_width: int,
    display_height: int,
    text_row_height: int,
    font_size: int,
    value_a: int,
    value_b: int,
    /,
) -> None:
    """
    Initialize the screen of the AKAI Fire

    This should be called before using any of the other functions in the
    `screen` module. After calling it, the `screen.setup` function should be
    called to allow the screen to be used.

    ## Args:
    * `display_width` (`int`): width of the display in pixels

    * `display_height` (`int`): height of the display in pixels

    * `text_row_height` (`int`): height of a text row (in what units?)

    * `font_size` (`int`): font size to use (in what units?)

    * `value_a` (`int`): unknown

    * `value_b` (`int`): unknown

    Included since API Version 1
    """


def deInit() -> None:
    """
    De-initialize the screen of the AKAI Fire

    This should be called before the script closes.

    Included since API Version 1
    """


def setup(
    sysex_header: int,
    screen_active_timeout: int,
    screen_auto_timeout: int,
    text_scroll_pause: int,
    text_scroll_speed: int,
    text_display_time: int,
    /,
) -> None:
    """
    Set up the AKAI Fire screen.

    This should be called after `screen.init` in order to perform more setup

    ## Args:
    * `sysex_header` (`int`): header for sysex message for device

    * `screen_active_timeout` (`int`): unknown

    * `screen_auto_timeout` (`int`): unknown

    * `text_scroll_pause` (`int`): unknown

    * `text_scroll_speed` (`int`): unknown

    * `text_display_time` (`int`): unknown

    Included since API Version 1
    """


def update() -> None:
    """
    Notify the Fire that it should update its screen contents

    This should be called after performing updates to the device's screen.

    Included since API Version 1
    """


def addMeter(*args) -> None:
    ...


def addTextLine(text: str, line: int, /) -> None:
    """
    Add text to a line on the screen?

    ## Args:
    * `text` (`str`): text to add

    * `line` (`int`): line on the screen

    Included since API Version 1
    """


def animateText(*args) -> None:
    ...


def blank(*args) -> None:
    ...


def displayBar(*args) -> None:
    ...


def displayText(*args) -> None:
    ...


def displayTimedText(*args) -> None:
    ...


def drawRect(*args) -> None:
    ...


def drawText(*args) -> None:
    ...


def eraseRect(*args) -> None:
    ...


def fillRect(
    start_x: int,
    start_y: int,
    end_x: int,
    end_y: int,
    value: int,
    /,
) -> None:
    """
    Draw a filled rectangle to the given position on the screen.

    It is drawn from the start values up to (but not including) the end values.

    ## Args:
    * `start_x` (`int`): starting horizontal position

    * `start_y` (`int`): starting vertical position

    * `end_x` (`int`): ending horizontal position

    * `end_y` (`int`): ending vertical position

    * `value` (`int`): unknown, maybe color?

    Included since API Version 1
    """


def findTextLine(*args) -> None:
    ...


def getScreenActiveCounter(*args) -> None:
    ...


def hideMenu(*args) -> None:
    ...


def isBlanked(*args) -> None:
    ...


def isUnBlank(*args) -> None:
    ...


def keepDisplayActive(*args) -> None:
    ...


def menuItemClick(*args) -> None:
    ...


def menuNext(*args) -> None:
    ...


def menuPrev(*args) -> None:
    ...


def menuShowing(*args) -> None:
    ...


def removeTextLine(*args) -> None:
    ...


def setScreenActiveCounter(*args) -> None:
    ...


def unBlank(*args) -> None:
    ...
