"""
Function definitions for interacting with the step sequencer.

## Examples

Count the number of active steps on the first channel:

```py
import channels

count = 0
# Assuming pattern length of 16 steps
for i in range(16):
    if channels.getGridBit(0, i):
        count += 1
print(f"There are {count} steps active")
```

Make a basic rock beat in the step sequencer:

```py
import channels

def fill_channel(idx: int, interval: int, offset: int):
    for i in range(16):
        if (i - offset) % interval == 0:
            channels.setGridBit(idx, i, True)

# Kick
fill_channel(0, 4, 0)
# Clap
fill_channel(1, 8, 4)
# Hi-hat
fill_channel(2, 2, 0)
# Snare
fill_channel(3, 8, 4)
```
"""


def getGridBit(
    index: int,
    position: int,
    useGlobalIndex: bool = False,
) -> bool:
    """
    Returns whether the grid bit on channel at `index` in `position` is set.

    ## Args

    * `index` (`int`): channel index.

    * `position` (`int`): index of grid bit (horizontal axis).

    * `useGlobalIndex` (`bool`, optional): whether to use the global channel
      index.

    ## Returns

    * `bool`: whether grid bit is set.

    Included since API version 1.

    ## API Changes

    * v33: add `useGlobalIndex` flag.
    """
    return False


def getGridBitWithLoop(
    index: int,
    position: int,
    useGlobalIndex: bool = False,
) -> bool:
    """
    Get value of grid bit on channel `index` in `position` accounting for
    loops.

    ## Args

    * `index` (`int`): channel index.

    * `position` (`int`): position on grid (horizontal axis).

    * `useGlobalIndex` (`bool`, optional): whether to use the global channel
      index.

    ## Returns

    * `bool`: whether grid bit is set.

    Included since API version 1.

    ## API Changes

    * v33: add `useGlobalIndex` flag.
    """
    return False


def setGridBit(
    index: int,
    position: int,
    value: bool,
    useGlobalIndex: bool = False,
) -> None:
    """
    Sets the value of the grid bit on channel at `index` in `position`.

    ## Args

    * `index` (`int`): channel index.

    * `position` (`int`): index of grid bit (horizontal axis).

    * `value` (`bool`): whether grid bit is set (`True`) or not (`False`).

    * `useGlobalIndex` (`bool`, optional): whether to use the global channel
      index.

    Included since API version 1

    ## API Changes

    * v33: add `useGlobalIndex` flag.
    """


def isGridBitAssigned(index: int, useGlobalIndex: bool = False) -> bool:
    """
    Returns `True` when the grid bit at `index` is assigned.

    ## HELP WANTED

    What does it mean for a grid bit to be assigned?

    ## Args

    * `index` (`int`): channel index.

    * `useGlobalIndex` (`bool`, optional): whether to use the global channel
      index.

    ## Returns

    * `bool`: whether the grid bit is assigned.

    Included since API Version 1
    """
    return False


def getStepParam(
    step: int,
    param: int,
    offset: int,
    startPos: int,
    padsStride: int = 16,
    useGlobalIndex: bool = False,
) -> int:
    """
    Get the values of properties associated with a step in the step sequencer.
    This provides an interface to access the graph editor.

    ## Args

    * `step` (`int`): step (grid bit index) to get parameter for.

    * `param` (`int`): one of the parameter types (see below).

    * `offset` (`int`): ???

    * `startPos` (`int`): ????

    * `padsStride` (`int`, optional): ?????. Defaults to 16.

    * `useGlobalIndex` (`bool`, optional): whether to use the global channel
      index.

    ## Returns

    * `int`: value for step parameter.

    ## See also

    * {{docs_url_fn[channels.getCurrentStepParam]}}

    * {{docs_url_fn[channels.setStepParameterByIndex]}}

    ## Step parameter types

    * `0`: Note pitch (MIDI note number, default 60 for middle C)
    * `1`: Velocity (0 - 127, default 100)
    * `2`: Release velocity (0 - 127, default 64)
    * `3`: Fine pitch (in cents: 0 - 240, with default 120 for no tuning)
    * `4`: Panning (0 - 127, with default 64 for centered)
    * `5`: Mod X (0-127, with default 64 for midpoint)
    * `6`: Mod Y (0-127, with default 64 for midpoint)
    * `7`: Number of ticks to offset the note by (0 - PPQN / 4; , with default
      0 for no shifting)

    Included since API version 1.
    """
    return 0


def getCurrentStepParam(
    index: int,
    step: int,
    param: int,
    useGlobalIndex: bool = False,
) -> int:
    """
    Get current step parameter for channel at `index` and for step at `step`.

    ## HELP WANTED

    * How is it different from {{docs_url_fn[channels.getStepParam]}}?

    ## Args

    * `index` (`int`): channel index.

    * `step` (`int`): step (grid bit index) to get parameter for.

    * `param` (`int`): one of the parameter types (see below).

    * `useGlobalIndex` (`bool`, optional): whether to use the global channel
      index.

    ## Returns

    * `int`: value for step parameter.

    ## Step parameter types

    * `0`: Note pitch (MIDI note number, default 60 for middle C)
    * `1`: Velocity (0 - 127, default 100)
    * `2`: Release velocity (0 - 127, default 64)
    * `3`: Fine pitch (in cents: 0 - 240, with default 120 for no tuning)
    * `4`: Panning (0 - 127, with default 64 for centered)
    * `5`: Mod X (0-127, with default 64 for midpoint)
    * `6`: Mod Y (0-127, with default 64 for midpoint)
    * `7`: Number of ticks to offset the note by (0 - PPQN / 4; , with default
      0 for no shifting)

    Included since API version 1

    ## API Changes

    * v33: add `useGlobalIndex` flag.
    """
    return 0


def setStepParameterByIndex(
    index: int,
    patNum: int,
    step: int,
    param: int,
    value: int,
    useGlobalIndex: bool = False,
) -> None:
    """
    Set the value of a step parameter at the given location.

    ## Args

    * `index` (`int`): channel index.

    * `patNum` (`int`): pattern number to set step parameter on (1-indexed).

    * `step` (`int`): step index.

    * `param` (`int`): step parameter to set (see below).

    * `value` (`int`): value to set parameter to.

    * `useGlobalIndex` (`bool`, optional): whether to use a global index for the
      channel. Defaults to `False`.

    ## Step parameter types

    * `0`: Note pitch (MIDI note number, default 60 for middle C)
    * `1`: Velocity (0 - 127, default 100)
    * `2`: Release velocity (0 - 127, default 64)
    * `3`: Fine pitch (in cents: 0 - 240, with default 120 for no tuning)
    * `4`: Panning (0 - 127, with default 64 for centered)
    * `5`: Mod X (0-127, with default 64 for midpoint)
    * `6`: Mod Y (0-127, with default 64 for midpoint)
    * `7`: Number of ticks to offset the note by (0 - PPQN / 4; , with default
      0 for no shifting)

    Included since API Version 1.
    """


def updateGraphEditor() -> None:
    """
    ???

    ## WARNING

    * This function has no official documentation

    Included since API Version 20?
    """


def closeGraphEditor(index: int, /) -> None:
    """
    ???

    ## WARNING

    * This function has no official documentation

    Included since API Version 33?
    """
