"""
device > __fl

Communication with FL Studio
"""
import midi
from fl_classes import FlMidiMsg


def processMIDICC(eventData: FlMidiMsg) -> None:
    """
    Let FL Studio process a MIDI CC message.

    ## Args

    * `eventData` (`FlMidiMsg`): FL MIDI Event to process.

    Included since API version 1.
    """


def forwardMIDICC(message: int, mode: int = 1) -> None:
    """
    Forwards a MIDI CC message to the currently focused plugin.

    ## Args

    * `message` (`int`): MIDI message to forward.

    * `mode` (`int`, optional): Where to send the message:
          * `0`: Send the message to all plugins.

          * `1` (default): Send the message to only the focused plugin.

          * `2`: Send the message to all selected channels.

    Included since API version 7.
    """


def findEventID(controlId: int, flags: int = 0) -> int:
    """
    Given a hardware control ID, returns the eventId of the software control
    that it is linked to or `midi.REC_InvalidID` if it is not linked.

    ## Args

    * `controlId` (`int`): ID of control surface.

    * `flags` (`int`, optional): ???. Defaults to 0.

    ## Returns

    * `int`: event ID.

    Included since API version 1.
    """
    return 0


def getLinkedValue(eventID: int) -> float:
    """
    Returns value of the software control associated with `eventID` between
    `0.0` and `1.0`, or `-1` if there is no linked control.

    ## Args

    * `eventID` (`int`): eventID.

    ## Returns

    * `float`: Current value of the controller parameter.

    ## Example usage

    ```py
    # Gets the volume and panning of channel 0
    >>> channel_rec_id = channels.getRecEventId(0)
    >>> device.getLinkedValue(channel_rec_id + midi.REC_Chan_Vol)
    0.78125
    >>> device.getLinkedValue(channel_rec_id + midi.REC_Chan_Pan)
    0.5
    ```

    Included since API version 1.
    """
    return 0.0


def getLinkedValueString(eventID: int) -> str:
    """
    Returns text value of the REC event at `eventID`.

    The text representation is formatted appropriately based on the
    REC parameter.

    ## Args

    * `eventID` (`int`): eventID.

    ## Returns

    * `str`: Parameter value string.

    ## Example usage

    ```py
    >>> channel_rec_id = channels.getRecEventId(0)
    >>> device.getLinkedValueString(channel_rec_id + midi.REC_Chan_Vol)
    '-5.2 dB'
    >>> device.getLinkedValueString(channel_rec_id + midi.REC_Chan_Pan)
    'Centered'
    ```

    Included since API version 10.
    """
    return ""


def getLinkedParamName(eventID: int) -> str:
    """
    Returns the parameter name of the REC event at `eventID`.

    ## Args

    * `eventID` (`int`): eventID.

    ## Returns

    * `str`: Parameter name.

    ## Example usage

    ```py
    >>> channel_rec_id = channels.getRecEventId(0)
    >>> device.getLinkedParamName(channel_rec_id + midi.REC_Chan_Vol)
    'Channel volume'
    >>> device.getLinkedParamName(channel_rec_id + midi.REC_Chan_Pan)
    'Channel panning'
    ```

    Included since API version 10.
    """
    return ""


def getLinkedInfo(eventID: int) -> int:
    """
    Returns information about a linked control via `eventID`.

    ## Args

    * `eventID` (`int`): eventID (see the {{docs_url_page("event mapping tutorial", "tutorials/event_mapping")}}).

    ## Returns

    * `int`: linked control info:
          * `-1`: no linked control.

          * `Event_CantInterpolate` (`1`): ???

          * `Event_Float` (`2`): ???

          * `Event_Centered` (`4`): ???

    Included since API version 1.
    """
    return 0


def linkToLastTweaked(
    controlIndex: int,
    channel: int,
    global_link: bool = False,
    eventId: int = midi.REC_None,
) -> int:
    """
    Links the control with the given index to the last tweaked parameter.

    ## WARNING

    * This function is subject to change before the release of FL Studio 21.

    ## Args

    * `controlIndex` (`int`): the control ID to link.

    * `channel` (`int`): ???

    * `global_link` (`bool`, optional): Whether to make a global link (applies
      to all projects, `True`), or a standard link (only for this project,
      `False`). Defaults to `False`.

    * `eventId` (`int`, optional): ID of the event to link to. If this is
      unset, the link will be created with the most recently tweaked parameter.
      Defaults to `midi.REC_None`.

    ## Returns

    * `0`: successfully created link.

    * `1`: no parameters recently tweaked.

    * `2`: control with this controlId is already assigned.

    Included since API Version 21.
    """
    return 0


def getLinkedChannel(eventId: int) -> int:
    """
    Returns the MIDI channel associated with a linked control.

    This is the MIDI channel of the event that is mapped to the linked control.
    Result is -1 if there is no linked control.

    ## Args

    * `eventId` (`int`): event ID to get channel for.

    ## Returns

    * `int`: MIDI channel.

    Included since API Version 27.
    """
    return 0


def getIdleElapsed() -> float:
    """
    ???

    WARNING:

    * This function is not officially documented

    ## Returns

    * `float`: ???

    Included since API Version ???
    """
    return 0.0
