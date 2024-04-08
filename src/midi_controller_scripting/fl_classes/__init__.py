"""
{{module_title[fl_classes]}}

This module contains definitions for FL Studio's built-in types, which can be
used to assist with type hinting in your project.

NOTE: This module is not included in FL Studio's runtime.

```py
try:
    from fl_classes import FlMidiMsg
except ImportError:
    FlMidiMsg = 'FlMidiMsg'

def OnMidiIn(event: FlMidiMsg) -> None:
    ...
```
"""
from typing import Optional, overload
from typing_extensions import TypeGuard


class FlMidiMsg:
    """
    A shadow of FL Studio's `FlMidiMsg` object. Note that although creating
    these is possible, it should be avoided during runtime as FL Studio's API
    won't accept it as an argument for any of its functions. It can be used
    within a testing environment, however.

    Note that two sub-types are also included, which allow for type narrowing
    by separating standard MIDI events and Sysex MIDI events. These will work
    for FL Studio's types as well.

    * `isMidiMsgStandard()`

    * `isMidiMsgSysex()`

    Basic type checking is performed when accessing properties of `FlMidiMsg`
    objects, to ensure that incorrect properties aren't accessed (for example
    accessing `data1` for a sysex event). These checks won't be performed
    during runtime for your script, but can help to add more certainty to your
    tests.
    """

    @overload
    def __init__(
        self,
        status_sysex: int,
        data1: int,
        data2: int,
    ) -> None:
        ...

    @overload
    def __init__(
        self,
        status_sysex: 'list[int] | bytes',
    ) -> None:
        ...

    def __init__(
        self,
        status_sysex: 'int | list[int] | bytes',
        data1: Optional[int] = None,
        data2: Optional[int] = None,
        pmeFlags: int = 0b101110,
    ) -> None:
        """
        Create an `FlMidiMsg` object.

        Note that this object will be incompatible with FL Studio's API, and so
        cannot be used as a parameter for any API functions during runtime.

        ### Args:
        * `status_sysex` (`int | list[int] | bytes`): status byte or sysex data

        * `data1` (`Optional[int]`, optional): data1 byte if applicable.
          Defaults to `None`.

        * `data2` (`Optional[int]`, optional): data2 byte if applicable.
          Defaults to `None`.

        * `pmeFlags` (`int`, optional): PME flags of event. Defaults to
          `PME_System | PME_System_Safe | PME_PreviewNote | PME_FromMIDI`.

        ### Example Usage

        ```py
        # Create a note on event on middle C
        msg = FlMidiMsg(0x90, 0x3C, 0x7F)

        # Create a CC#10 event
        msg = FlMidiMsg(0xB0, 0x0A, 0x00)

        # Create a sysex event for a universal device enquiry
        msg = FlMidiMsg([0xF0, 0x7E, 0x7F, 0x06, 0x01, 0xF7])
        ```
        """
        if isinstance(status_sysex, int):
            if data1 is None:
                raise TypeError(
                    "data1 value cannot be None for standard events")
            if data2 is None:
                raise TypeError(
                    "data2 value cannot be None for standard events")
            self.__status = status_sysex
            self.__sysex: Optional[bytes] = None
        else:
            if data1 is not None:
                raise TypeError(
                    "data1 value must be None for sysex events")
            if data2 is not None:
                raise TypeError(
                    "data2 value must be None for sysex events")
            self.__sysex = bytes(status_sysex)
            self.__status = 0xF0
        self.__data1 = data1
        self.__data2 = data2

        self.__timestamp = 0
        self.__handled = False
        self.__port = 0
        self.__pitch_bend = 1
        self.__is_increment = False
        self.__res = 0.0
        self.__in_ev = 0
        self.__out_ev = 0
        self.__midi_id = 0
        self.__midi_chan = 0
        self.__midi_chan_ex = 0
        self.__pme_flags = pmeFlags

    def __repr__(self) -> str:
        if self.__sysex is not None:
            return f"FlMidiMsg([{', '.join(f'0x{b:02X}' for b in self.sysex)})"
        else:
            return (
                f"FlMidiMsg("
                f"0x{self.status:02X}, "
                f"0x{self.data1:02X}, "
                f"0x{self.data2:02X})"
            )

    def __eq__(self, other: object) -> bool:
        if isinstance(other, FlMidiMsg):
            if (isMidiMsgStandard(self) and isMidiMsgStandard(other)):
                return all([
                    self.status == other.status
                    and self.data1 == other.data1
                    and self.data2 == other.data2
                ])
            elif (isMidiMsgSysex(self) and isMidiMsgSysex(other)):
                return self.sysex == other.sysex
        elif isinstance(other, int):
            if isMidiMsgStandard(self):
                return eventToRawData(self) == other
        elif isinstance(other, bytes):
            if isMidiMsgSysex(self):
                return eventToRawData(self) == other
        return False

    @staticmethod
    def __standard_check(value: Optional[int], prop: str) -> int:
        """Check that it's a standard event, then return the value"""
        if value is None:
            raise ValueError(
                f"Attempt to access {prop} on sysex event. "
                f"Are you type narrowing your events correctly?"
            )
        return value

    @staticmethod
    def __range_check(value: int, prop: str) -> int:
        """Check that the value is within the allowed range, then return it"""
        if value < 0:
            raise ValueError(f"Attempt to set {prop} to {value} (< 0)")
        if value > 0x7F:
            raise ValueError(f"Attempt to set {prop} to {value} (> 0x7F)")
        return value

    @property
    def handled(self) -> bool:
        """Whether the event is considered to be handled by FL Studio.

        If this is set to `True`, the event will stop propagating after this
        particular callback returns.

        You script should set it when an event is processed successfully.
        """
        return self.__handled

    @handled.setter
    def handled(self, handled: bool) -> None:
        self.__handled = handled

    @property
    def timestamp(self) -> int:
        """The timestamp of the event

        ### HELP WANTED:
        * This seems to only ever be zero. I can't determine what it is for. If
          you know how it is used, create a pull request with details.

        This value is read-only.
        """
        return self.__timestamp

    @property
    def status(self) -> int:
        """The status byte of the event

        This can be used to determine the type of MIDI event using the upper
        nibble, and the channel of the event using the lower nibble.

        ```py
        e_type = event.status & 0xF0
        channel = event.status & 0xF
        ```

        Note that for sysex messages, this property is `0xF0`. Other standard
        event properties are inaccessible.

        ## Event types
        * `0x8` Note off (`data1` is note number, `data2` is release value)

        * `0x9` Note on (`data1` is note number, `data2` is velocity)

        * `0xA` Note after-touch (`data1` is note number, `data2` is pressure
          value)

        * `0xB` Control change (CC, `data1` is control number as per your
          controller's documentation, `data2` is value)

        * `0xC` Program change (used to assign instrument selection, `data1` is
          instrument number)

        * `0xD` Channel after-touch (`data1` is value, `data2` is unused)

        * `0xE` Pitch bend (`data1` and `data2` are value, as per the formula
          `data1 + (data2 << 7)`, yielding a range of `0` - `16384`)
        """
        return self.__status

    @status.setter
    def status(self, status: int) -> None:
        self.__status = self.__range_check(status, "status")

    @property
    def data1(self) -> int:
        """The first data byte of a MIDI message.

        This is used to determine the control number for CC events, the note
        number for note events, and various other values.

        Note that this property is inaccessible for sysex events.
        """
        return self.__standard_check(self.__data1, "data1")

    @data1.setter
    def data1(self, data1: int) -> None:
        self.__data1 = self.__range_check(data1, "data1")

    @property
    def data2(self) -> int:
        """The second data byte of a MIDI message.

        This is used to determine the value for CC events, the velocity for
        note events, and various other values.

        Note that this property is inaccessible for sysex events.
        """
        return self.__standard_check(self.__data2, "data2")

    @data2.setter
    def data2(self, data2: int) -> None:
        self.__data2 = self.__range_check(data2, "data2")

    @property
    def port(self) -> int:
        """The port of the message

        ### HELP WANTED:
        * This value always appears to be zero. How should it be used?

        Note that this property is read-only.
        """
        return self.__port

    @property
    def note(self) -> int:
        """The note number of a MIDI note on/off message.

        This is a shadow of the `data1` property. Modifications to this will
        affect all `data1` derived properties.

        Note that this property is inaccessible for sysex events.
        """
        return self.__standard_check(self.__data1, "note")

    @note.setter
    def note(self, note: int) -> None:
        self.__data1 = self.__range_check(note, "note")

    @property
    def velocity(self) -> int:
        """The velocity of a MIDI note on/off message.

        This is a shadow of the `data2` property. Modifications to this will
        affect all `data2` derived properties

        Note that this property is inaccessible for sysex events.
        """
        return self.__standard_check(self.__data2, "velocity")

    @velocity.setter
    def velocity(self, velocity: int) -> None:
        self.__data2 = self.__range_check(velocity, "velocity")

    @property
    def pressure(self) -> int:
        """The pressure value for a channel after-touch event.

        This is a shadow of the `data1` property. Modifications to this will
        affect all `data1` derived properties.

        Note that this property is inaccessible for sysex events.
        """
        return self.__standard_check(self.__data1, "pressure")

    @pressure.setter
    def pressure(self, pressure: int) -> None:
        self.__data1 = self.__range_check(pressure, "pressure")

    @property
    def progNum(self) -> int:
        """The instrument number for a program change event.

        This is a shadow of the `data1` property. Modifications to this will
        affect all `data1` derived properties.

        Note that this property is inaccessible for sysex events.
        """
        return self.__standard_check(self.__data1, "progNum")

    @progNum.setter
    def progNum(self, progNum: int) -> None:
        self.__data1 = self.__range_check(progNum, "progNum")

    @property
    def controlNum(self) -> int:
        """The control number for a control change event.

        This is a shadow of the `data1` property. Modifications to this will
        affect all `data1` derived properties.

        Note that this property is inaccessible for sysex events.
        """
        return self.__standard_check(self.__data1, "controlNum")

    @controlNum.setter
    def controlNum(self, controlNum: int) -> None:
        self.__data1 = self.__range_check(controlNum, "controlNum")

    @property
    def controlVal(self) -> int:
        """The value of a control change event.

        This is a shadow of the `data2` property. Modifications to this will
        affect all `data2` derived properties

        Note that this property is inaccessible for sysex events.
        """
        return self.__standard_check(self.__data2, "controlVal")

    @controlVal.setter
    def controlVal(self, controlVal: int) -> None:
        self.__data2 = self.__range_check(controlVal, "controlVal")

    @property
    def pitchBend(self) -> int:
        """MIDI pitch bend value

        ### HELP WANTED:
        * This only ever seems to equal `1`. How should it be used?

        Note that this property is read-only.
        """
        return self.__pitch_bend

    @property
    def sysex(self) -> bytes:
        """Data for a sysex event

        Contains the full event data from sysex events.

        This property is inaccessible for standard events.
        """
        if self.__sysex is None:
            raise ValueError(
                "Attempt to access sysex data on standard event. "
                "Are you type narrowing your events correctly?"
            )
        return self.__sysex

    @sysex.setter
    def sysex(self, sysex: bytes) -> None:
        if len(sysex) == 0:
            raise ValueError("New sysex data has length of zero")
        if sysex[0] != 0xF0:
            raise ValueError("New sysex data doesn't first value of 0xF0")
        self.__sysex = sysex

    @property
    def isIncrement(self) -> bool:
        """Whether the event should be an increment event

        If the script sets this to `True`, FL Studio will consider it to be a
        relative event, meaning that it will change values relative to that
        value, rather than setting them absolutely.

        ### HELP WANTED:
        * Notes on the particular cases where this happens.
        """
        return self.__is_increment

    @isIncrement.setter
    def isIncrement(self, isIncrement: bool) -> None:
        self.__is_increment = isIncrement

    @property
    def res(self) -> float:
        """MIDI res

        ### HELP WANTED:
        * How is this used?
        """
        return self.__res

    @res.setter
    def res(self, res: float) -> None:
        self.__res = res

    @property
    def inEv(self) -> int:
        """MIDI inEv

        ### HELP WANTED:
        * What is this?
        """
        return self.__in_ev

    @inEv.setter
    def inEv(self, inEv: int) -> None:
        self.__in_ev = inEv

    @property
    def outEv(self) -> int:
        """MIDI outEv

        ### HELP WANTED:
        * What is this?
        """
        return self.__out_ev

    @outEv.setter
    def outEv(self, outEv: int) -> None:
        self.__out_ev = outEv

    @property
    def midiId(self) -> int:
        """MIDI ID

        ### HELP WANTED:
        * What is this?
        """
        return self.__midi_id

    @midiId.setter
    def midiId(self, midiId: int) -> None:
        self.__midi_id = midiId

    @property
    def midiChan(self) -> int:
        """MIDI chan

        ### HELP WANTED:
        * What is this?

        * No, it's not a channel. It always seems to be zero, regardless of the
          channel of the event.
        """
        return self.__midi_chan

    @midiChan.setter
    def midiChan(self, midiChan: int) -> None:
        self.__midi_chan = midiChan

    @property
    def midiChanEx(self) -> int:
        """MIDI chanEx

        ### HELP WANTED:
        * What is this?
        """
        return self.__midi_chan_ex

    @midiChanEx.setter
    def midiChanEx(self, midiChanEx: int) -> None:
        self.__midi_chan_ex = midiChanEx

    @property
    def pmeFlags(self) -> int:
        """Flags used by FL Studio to indicate the permissions of the script in
        the current environment.

        These can be used to ensure safety while running the script. If a
        script ever attempts to execute unsafe behavior, a `TypeError` will be
        raised.

        ```py
        TypeError("Operation unsafe at current time")
        ```

        ## Flag analysis

        The flags can be analyzed by performing bitwise operations to determine
        the current permissions of the script.

        * `0b000010` (`PME_System`) System operations allowed (play/pause,
          etc).

        * `0b000100` (`PME_System_Safe`) Critical operations allowed (add
          markers, etc). Things that can't be done when a modal dialog is
          showing.

        * `0b001000` (`PME_PreviewNote`) Note events will trigger a preview.

        * `0x010000` (`PME_FromHost`) FL Studio is being hosted as a VSTi
          (meaning it's probably a bad idea to do anything meaningful as it
          could interfere with the behavior of other DAWs). In my testing,
          using MIDI scripts in the FL Studio VST causes a crash anyway, so I
          suppose it isn't that important either way.

        * `0x100000` This event was triggered by a MIDI event.

        ## Alternate to flag analysis

        It could be considered to be more Pythonic, as well as much simpler to
        catch this exception rather than checking the flags. The following is
        a simple decorator that will catch the exception. This does come with
        the risk that any unsafe behavior that FL Studio misses will cause
        a system lock-up in FL Studio.

        ```py
        def catchUnsafeOperation(func):
            '''
            Decorator to prevent exceptions due to unsafe operations

            ### Args:
            * `func` (`Callable`): function to decorate
            '''
            def wrapper(*args, **kwargs):
                try:
                    func(*args, **kwargs)
                except TypeError as e:
                    if e.args != ("Operation unsafe at current time",):
                        raise e
            return wrapper
        ```
        """
        return self.__pme_flags


class StandardMidiMsg(FlMidiMsg):
    """
    An FlMidiMsg object which has been type narrowed to a StandardFlMidiMsg.

    Note that as FL Studio events are actually of a different type to these
    shadow types, you should never use the `isinstance` function in order to
    perform type-narrowing operations, as it will lead to very obscure bugs
    when your type checks never work inside FL Studio, even if they work in
    your tests.

    Instead, you can type narrow to a `StandardFlMidiMsg` object using the
    `isMidiMsgStandard()` function.
    """

    def __init__(self, status: int, data1: int, data2: int) -> None:
        super().__init__(status, data1, data2)


class SysexMidiMsg(FlMidiMsg):
    """
    An FlMidiMsg object which has been type narrowed to a SysexFlMidiMsg.

    Note that as FL Studio events are actually of a different type to these
    shadow types, you should never use the `isinstance` function in order to
    perform type-narrowing operations, as it will lead to very obscure bugs
    when your type checks never work inside FL Studio, even if they work in
    your tests.

    Instead, you can type narrow to a `SysexFlMidiMsg` object using the
    `isMidiMsgSysex()` function.
    """

    def __init__(self, sysex: list[int]) -> None:
        super().__init__(sysex)


def isMidiMsgStandard(event: FlMidiMsg) -> 'TypeGuard[StandardMidiMsg]':
    """
    Returns whether an event is a standard event

    ### Args:
    * `event` (`FlMidiMsg`): event to check

    ### Returns:
    * `TypeGuard[SysexFlMidiMsg]`: type guarded event
    """
    return not isMidiMsgSysex(event)


def isMidiMsgSysex(event: FlMidiMsg) -> 'TypeGuard[SysexMidiMsg]':
    """
    Returns whether an event is a sysex event

    ### Args:
    * `event` (`FlMidiMsg`): event to check

    ### Returns:
    * `TypeGuard[SysexFlMidiMsg]`: type guarded event
    """
    return event.status == 0xF0


def eventToRawData(event: FlMidiMsg) -> 'int | bytes':
    """
    Convert event to raw data.

    For standard events data is presented as little-endian, meaning that the
    status byte has the lowest component value in the integer.

    ### Returns:
    * `int | bytes`: data
    """
    if isMidiMsgStandard(event):
        return (event.status) + (event.data1 << 8) + (event.data2 << 16)
    else:
        assert isMidiMsgSysex(event)
        return event.sysex
