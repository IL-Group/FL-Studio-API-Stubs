"""
Functions for communicating with the attached MIDI hardware controller.

## Example usage

Check that a device is assigned, and display its name and port number.

```py
import device

if device.isAssigned():
    port_num = device.getPortNumber()
    name = device.getName()
    print(f"The device '{name}' is connected on port {port_num}")
```

Send a note-on event to the device

```py
import device

# Middle C on channel 0, at velocity 100
device.midiOutMsg(0x9, 0x0, 60, 100)
```
"""
from typing import overload

from fl_classes import FlMidiMsg


def isAssigned() -> bool:
    """
    Returns `True` if an output interface is linked to the script, meaning that
    the script can send MIDI messages to that device.

    ## Returns

    * `bool`: whether the device is assigned.

    Included since API version 1.
    """
    return False


def isMidiOutAssigned() -> bool:
    """
    ???

    ## WARNING

    * This function is not officially documented.

    * Calling this function in an interpreter not associated with a device
      causes FL Studio to crash.

    ## Returns

    * `bool`: ???

    Included since API Version ???
    """
    return False


def getPortNumber() -> int:
    """
    Returns the port number for the input device that the script is attached
    to.

    If the device requires two-way communication, the output port (where
    functions like {{docs_url_fn[device.midiOutMsg]}} send their data to)
    should be set to the value of the input port, which is returned by this
    function.

    ## Returns

    * `int`: port number of the input device.

    Included since API version 1.
    """
    return 0


def getName() -> str:
    """
    Returns the name of the device.

    ## Returns

    * `str`: device name.

    Included since API version 7.
    """
    return ""


@overload
def midiOutMsg(message: int) -> None:
    ...


@overload
def midiOutMsg(message: int, channel: int, data1: int, data2: int) -> None:
    ...


def midiOutMsg(
    message: int,
    channel: int = -1,
    data1: int = -1,
    data2: int = -1,
) -> None:
    """
    Sends a MIDI message to the linked output device.

    This can be done either through a single combined message, or in its
    distinct components.

    ## Args

    * `message` (`int`):
          * the MIDI message to send (if sending a complete message):
              * Lowest byte: `status`.

              * Middle byte: `data 1`.

              * Upper byte: `data 2`.

          * OR the message type (if sending a partial MIDI message,
            eg `0xB` for a CC message).

    * `channel` (`int`, optional): the channel to send the message to (if
      sending a partial MIDI message).

    * `data1` (`int`, optional): the note data value for the message (if
      sending a partial MIDI message).

    * `data2` (`int`, optional): the velocity data value for the message (if
      sending a partial MIDI message).

    Included since API version 1, with the component options added in API
    version 2.
    """


def midiOutNewMsg(slotIndex: int, message: int) -> None:
    """
    Sends a MIDI message to the linked output device, but only if the
    message being sent has changed compared to the last message sent with the
    same `slotIndex`.

    ## Args

    * `slotIndex` (`int`): index for MIDI message comparison.

    * `message` (`int`): message to potentially send.

    Included since API version 1.
    """


def midiOutSysex(message: bytes) -> None:
    """
    Send a sysex message to the (linked) output device.

    The sysex data must include the sysex start `0xF0` and sysex end `0xF7`
    bytes, or FL Studio will ignore the function call entirely.

    ## Args

    * `message` (`str`): Sysex message to send.

    Included since API version 1.
    """


def sendMsgGeneric(
    id: int,
    message: str,
    lastMsg: str,
    offset: int = 0,
    /,
) -> str:
    """
    Send a text string as a sysex message to the linked output device.

    ## WARNING:

    * This function is deprecated.

    ## Args

    * `id` (`int`): the first 6 bytes of the message (the end value `0xF7` is
      added automatically).

    * `message` (`str`): the text to send.

    * `lastMsg` (`str`): the string returned by the previous call to this
      function.

    * `offset` (`int`, optional): ???. Defaults to 0.

    ## Returns

    * `str`: value to use in the next call of this function.

    Included since API version 1.

    Deprecated since API version 9.
    """
    return ""


def directFeedback(eventData: FlMidiMsg, /) -> None:
    """
    Send a received message to the linked output device.

    ## Args

    * `eventData` (`eventData`): event to send.

    Included since API version 1.
    """


def repeatMidiEvent(
    eventData: FlMidiMsg,
    delay: int = 300,
    rate: int = 300,
) -> None:
    """
    Start repeatedly sending out the message in `eventData` every `rate` ms
    after `delay` ms.

    ## Args

    * `eventData` (`eventData`): event to repeat.

    * `delay` (`int`, optional): initial delay before sending in ms. Defaults
    to 300.

    * `rate` (`int`, optional): time between each send in ms. Defaults to 300.

    Included since API version 1.
    """


def stopRepeatMidiEvent() -> None:
    """
    Stop sending a currently repeating MIDI event.

    Refer to {{docs_url_fn[device.repeatMidiEvent]}}.

    Included since API version 1.
    """


def setMasterSync(value: bool) -> None:
    """
    Control the value of the "send master sync" option in FL Studio's MIDI
    settings for this device.

    This option controls whether stop, pause and play transport notifications
    are sent to the MIDI device. This shouldn't be enabled unless the device
    explicitly requires it, as it can lead to unpredictable and sometimes
    broken behavior.

    ## Args

    * `value` (`bool`): Whether to enable (or disable) the "send master sync"
      option.

    Included since API Version 18.
    """


def getMasterSync() -> bool:
    """
    Returns the value of the "send master sync" option in FL Studio's MIDI
    settings for this device.

    This option returns whether stop, pause and play transport notifications
    are sent to the MIDI device, and shouldn't be enabled unless the device
    explicitly requires it, as it can lead to unpredictable and sometimes
    broken behavior.

    ## Returns

    * `bool`: Whether master sync is enabled.

    Included since API Version 19.
    """
    return False


def getDeviceID() -> bytes:
    """
    Returns the unique device identifier of the connected device, as determined
    by FL Studio when connecting the device.

    Note that this does not include the Sysex header, or ending byte.

    For example, if the device responded to a universal device enquiry with:

    ```py
    bytes([
        0xF0, 0x7E, 0x01, 0x06, 0x02,
        0x00, 0x20, 0x29, 0x02, 0x01,
        0x00, 0x00, 0x00, 0x04, 0x02,
        0x05, 0xF7,
    ])
    ```

    This function would only return:

    ```py
    bytes([0x00, 0x20, 0x29, 0x02, 0x01, 0x00, 0x00, 0x00, 0x04, 0x02, 0x05])
    ```

    ## Returns

    * `bytes`: device ID.

    Included since API Version 25.
    """
    return b""
