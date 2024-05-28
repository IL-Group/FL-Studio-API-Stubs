"""
Function definitions for triggering and managing notes on channels.

## Examples

Play a C major chord in the first instrument

```py
import channels

MIDDLE_C = 60

channels.midiNoteOn(0, MIDDLE_C, 100)
channels.midiNoteOn(0, MIDDLE_C + 4, 100)
channels.midiNoteOn(0, MIDDLE_C + 4 + 3, 100)
```

Stop the infinitely long notes from the previous example

```py
import channels

MIDDLE_C = 60

# A velocity of zero is considered a note off
channels.midiNoteOn(0, MIDDLE_C, 0)
channels.midiNoteOn(0, MIDDLE_C + 4, 0)
channels.midiNoteOn(0, MIDDLE_C + 4 + 3, 0)
```
"""


def midiNoteOn(
    indexGlobal: int,
    note: int,
    velocity: int,
    channel: int = -1,
) -> None:
    """
    Set a MIDI Note for the channel at `indexGlobal` (not respecting groups).

    This can be used to create extra notes (eg mapping one note to a chord).

    Note that triggering notes using this function rather than allowing FL
    Studio to process them may result in users' manual note mappings won't be
    respected. Developers should be sure to check
    {{docs_url_fn[channels.getChannelMidiInPort]}} on all channels to ensure
    that no channels receive MIDI events from this script.

    ## Note

    * Specifying a `channel` doesn't appear to do anything.

    ## Args

    * `indexGlobal` (`int`): channel index (not respecting groups).

    * `note` (`int`): note number (0-127).

    * `velocity` (`int`): note velocity (1-127, 0 is note off).

    * `channel` (`int`, optional): MIDI channel to use. Defaults to -1.

    Included since API version 1.
    """


def quickQuantize(
    index: int,
    startOnly: int = 1,
    useGlobalIndex: bool = False,
) -> None:
    """
    Perform a quick quantize operation on the channel at index

    ## Args

    * `index` (`int`): channel index, respecting groups

    * `startOnly` (`int`, optional): ???. Defaults to `1`.

    * `useGlobalIndex` (`bool`, optional): whether to use the global channel
      index when quantizing notes on the channel.

    Included since API Version 9.

    ## API Changes

    * v33: add `useGlobalIndex` flag.
    """
