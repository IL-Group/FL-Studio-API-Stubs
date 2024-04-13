"""
ui > browser

Code for navigating the browser.
"""


def navigateBrowser(direction: int, shiftHeld: bool) -> str:
    """
    Navigates through the browser. `direction` can be 0 for previous
    or > 0 for next.

    Shift held will cause the browser item to expand/open  if it's a
    folder/collection ie `Node Type <= -100`, similar to keyboard navigation.

    ## Args

    * `direction` (`int`):
            * `40`: previous item
            * `41`: next item

    * `shiftHeld` (`bool`): whether to expand the selected item if it is a
      folder.

    ## WARNING

    * This doesn't seem to work very reliably, at least on my machine.

    ## Returns

    * `str`: the name of the newly selected item in the browser.

    Included since API Version 22.
    """
    return ""


def navigateBrowserMenu(direction: int, shiftHeld: bool) -> str:
    """
    Navigates through the browser. `direction` can be 0 for previous
    or > 0 for next.

    Shift held will cause the browser item to expand/open  if it's a
    folder/collection ie `Node Type <= -100`, similar to keyboard navigation.

    ## WARNING

    * This function is undocumented.

    * This appears to be a duplicate of `ui.navigateBrowser`. Consider using it
      instead.

    ## Args

    * `direction` (`int`):
            * `40`: previous item
            * `41`: next item

    * `shiftHeld` (`bool`): whether to expand the selected item if it is a
      folder.

    ## Returns

    * `str`: the name of the newly selected item in the browser.

    Included since API Version 22.
    """
    return ""


def navigateBrowserTabs(direction: int) -> str:
    """
    Navigates between browser tabs, returning the name of the newly selected
    tab.

    The direction should be one of the MIDI FPT direction constants.

    ## Args

    * `direction` (`int`): one of:
            * `midi.FPT_Left` (`42`): change tabs left
            * `midi.FPT_Right` (`43`): change tabs right
            * any other value: navigate to first tab

    ## Returns

    * `str`: name of the newly selected tab.

    Included since API Version 22.
    """
    return ""


def previewBrowserMenuItem():
    """
    Preview the highlighted item in the browser.

    This will play a selected audio clip.

    Included since API Version 20.
    """


def selectBrowserMenuItem():
    """
    Selects the currently highlighted browser menu item, which is the
    equivalent of clicking it.

    ## WARNING:
    * This function appears to open the File menu, rather than navigating the
      browser.

    Included since API Version 20.
    """


def getFocusedNodeCaption() -> str:
    """
    Returns the filename associated with the currently selected item in the
    browser.

    ## Returns

    * `str`: node caption.

    Included since API Version 20.
    """
    return ""


def getFocusedNodeFileType() -> int:
    """
    Returns a value based on the type of the selected file in the browser.

    ## Returns

    * `int`: One of the file type constants represented in the FL Studio
      constants.

    Refer to the {{fl_manual_anchor[BrowserFileTypes]}}.

    Included since API Version 20.
    """
    return 0


def isBrowserAutoHide() -> bool:
    """
    Returns whether the browser is set to auto-hide.

    ## Returns

    * `bool`: auto-hide status.

    Included since API Version 20.
    """
    return False


def setBrowserAutoHide(value: bool):
    """
    Toggle whether the browser is set to auto-hide.

    ## Args

    * `value` (`bool`): whether the browser should auto-hide (`True`) or not
      (`False`).

    Included since API Version 20.
    """


def toggleBrowserNode(value: int = -1) -> None:
    """
    Toggle whether the browser node is expanded.

    ## Args

    * `value` (`int`, optional): whether to expand (`1`), collapse (`0`) or
      toggle (`-1`) the node. Defaults to `-1`.

    Included since API Version 34
    """
