"""
Functions for managing the channel rack UI.

## Examples

Open the plugin window for the selected channel.

```py
import channels

channels.focusEditor(channels.channelNumber())
```
"""


def isHighLighted() -> bool:
    """
    Returns `True` when a red highlight rectangle is displayed on the channel
    rack. This rectangle can be displayed using
    {{docs_url_fn[ui.crDisplayRect]}}.

    These hints can be used to visually indicate on the channel rack where your
    script is mapping to.

    ## Returns

    * `bool`: whether highlight rectangle is visible.

    Included since API version 1
    """
    return False


def showGraphEditor(
    temporary: bool,
    param: int,
    step: int,
    index: int,
    useGlobalIndex: bool = True,
) -> None:
    """
    Show the graph editor for a step parameter on the channel at `index`.

    ## Args

    * `temporary` (`bool`): whether the editor should be temporary or stay
      open.

    * `param` (`int`): step parameter, see the {{fl_manual_anchor[stepParams]}}

    * `step` (`int`): step ???.

    * `index` (`int`): index of channel.

    * `globalIndex` (`int`, optional): whether index should be global (`True`)
      or not (`False`). Defaults to `True`.

    Included since API Version 1.

    ## API Changes

    * v20: add `useGlobalIndex` flag.
    """


def isGraphEditorVisible() -> bool:
    """
    Returns whether the graph editor is currently visible.
    """
    return False


def showEditor(
    index: int,
    value: int = -1,
    useGlobalIndex: bool = False,
) -> None:
    """
    Toggle whether the plugin window for the channel at `index` is shown. The
    value parameter can be used to control whether the editor is hidden or
    shown.

    ## Args

    * `index` (`int`): channel index.

    * `value` (`int`): whether to hide (`0`) or show (`1`) the plugin window.
      Defaults to `-1` (toggle).

    * `useGlobalIndex` (`bool`, optional): whether to use the global channel
      index when

    Included since API version 1.

    ## API Changes

    * v3: Add `value` parameter.

    * v33: add `useGlobalIndex` flag.
    """


def focusEditor(index: int, useGlobalIndex: bool = False) -> None:
    """
    Focus the plugin window for the channel at `index`.

    ## Args

     * `index` (`int`): channel index.

    * `useGlobalIndex` (`bool`, optional): whether to use the global channel
      index when

    Included since API version 1.

    ## API Changes

    * v33: add `useGlobalIndex` flag.
    """


def showCSForm(
    index: int,
    state: int = 1,
    useGlobalIndex: bool = False,
) -> None:
    """
    Show the channel settings window (or plugin window for plugins) for channel
    at `index`.

    This appears to perform the same action as {{docs_url_fn[channels.focusEditor]}}.

    ## Args

    * `index` (int): channel index

    * `state` (`int`, optional): whether to hide (`0`), show
      (`1`) or toggle (`-1`) the plugin window. Defaults to `1`.

    * `useGlobalIndex` (`bool`, optional): whether to use the global channel
      index when

    Included since API version 1.

    ## API Changes

    * v9: Add `state` parameter.

    * v33: add `useGlobalIndex` flag.
    """


def getActivityLevel(index: int, useGlobalIndex: bool = False) -> float:
    """Return the note activity level for channel at `index`. Activity level
    refers to how recently a note was played, as well as whether any notes are
    currently playing.

    ## Args

    * `index` (`int`): channel index.

    * `useGlobalIndex` (`bool`, optional): whether to use the global channel
      index when

    ## Returns

    * `float`: activity level.

    Included since API version 9.

    ## API Changes

    * v33: add `useGlobalIndex` flag.
    """
    return 0.0
