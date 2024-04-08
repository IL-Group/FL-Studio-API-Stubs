"""
device > dispatch

Functions for dispatching MIDI messages between scripts.
"""
from typing import Optional, overload, Literal


@overload
def dispatch(
    ctrlIndex: int,
    message: Literal[0xF0],
    sysex: bytes,
) -> None:
    ...


@overload
def dispatch(
    ctrlIndex: int,
    message: int,
) -> None:
    ...


def dispatch(
    ctrlIndex: int,
    message: int,
    sysex: Optional[bytes] = None,
) -> None:
    """
    Dispatch a MIDI message (either via a standard MIDI Message or through a
    system exclusive (SysEx) message) that is sent to another controller
    script. This allows communication between different devices provided that
    they have a standardized communication method.

    MIDI messages sent through this method are received in the same way as all
    other messages, so it should be ensured that they can be differentiated
    by the receiving controller.

    In order to allow a device to receive MIDI messages via a dispatch command,
    it must have a `receiveFrom` pre-processor comment for FL Studio to detect
    when the script is loaded. This comment should be at the top of the
    `device_MyController.py` file along with the name and URL, for example:

    ```py
    # name=My Controller
    # receiveFrom=My Other Controller
    ```

    After this declaration, the script named "My Other Controller" will be able
    to dispatch MIDI messages to the script named "My Controller".

    ## Args

    * `ctrlIndex` (`int`): index of the controller to dispatch to.

    * `message` (`int`): MIDI message to send (`0xF0` for a SysEx message).

    * `sysex` (`bytes`, optional): SysEx data to send, if applicable.

    ## Example Usage

    ```py
    # Send a standard MIDI event (middle C note on) to the device indexed 0.
    device.dispatch(0, 0x90 + (0x3C << 8) + (0x7F << 16))

    # Send a sysex MIDI event to the device indexed 0. Note that the full
    # message is still contained within the bytes object, even though the
    # `0xF0` is also given as `message`.
    device.dispatch(0, 0xF0, bytes([0xF0, 0x7E, 0x7F, 0x06, 0x01, 0xF7]))
    ```

    Included since API version 1.
    """


def dispatchReceiverCount() -> int:
    """
    Returns the number of device scripts that this script can dispatch to.

    ## Returns

    * `int`: number of available receiver devices.

    Included since API version 1.
    """
    return 0


def dispatchGetReceiverPortNumber(ctrlIndex: int) -> int:
    """
    Returns the port of the receiver device specified by `ctrlIndex`.

    ## Args

    * `ctrlIndex` (`int`): device script to check.

    ## Returns

    * `int`: MIDI port associated with the receiver device.

    Included since API version 5.
    """
    return 0
