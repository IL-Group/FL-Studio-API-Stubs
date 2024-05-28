"""
These constants can be used to match against status codes for MIDI messages,
accessed from {{docs_url_attr("fl_classes.FlMidiMsg", ".status")}}.

```py
import midi

def OnMidiIn(msg: FlMidiMsg):
    # Use a bitwise and to discard the channel number
    if msg.status & 0xF0 == midi.MIDI_NOTEON:
        print("event is a note on event")
```
"""

MIDI_NOTEON = 0x90
"""
MIDI note-on

* `data1` is note number
* `data2` is velocity (`0` for note off)
"""

MIDI_NOTEOFF = 0x80
"""
MIDI note-off

* `data1` is note number
* `data2` is release value
"""

MIDI_KEYAFTERTOUCH = 0xA0
"""
MIDI key after-touch

* `data1` is note number
* `data2` is after-touch value
"""

MIDI_CONTROLCHANGE = 0xB0
"""
MIDI control change
"""

MIDI_PROGRAMCHANGE = 0xC0
"""
MIDI program change

* `data1` contains the program number (instrument) to select
"""

MIDI_CHANAFTERTOUCH = 0xD0
"""
MIDI channel after-touch

* `data1` is after-touch value
"""

MIDI_PITCHBEND = 0xE0
"""
MIDI pitch-bend

Both `data1` and `data2` are combined to produce a 14-bit pitch-bend value.

```py
def pitch_bend_event_to_float(event: FlMidiMsg) -> float:
    return (event.data1 + (event.data2 << 7)) / 16383
```
"""

MIDI_SYSTEMMESSAGE = 0xF0
"""
MIDI system-exclusive (sysex) message.

Remaining data is included in the `event.sysex` property.
"""

MIDI_BEGINSYSEX = 0xF0
"""
MIDI system-exclusive message start.

This should be the first byte of all sysex messages.
"""

MIDI_ENDSYSEX = 0xF7
"""
MIDI system-exclusive message end.

This should be the final byte of all sysex messages.
"""

MIDI_MTCQUARTERFRAME = 0xF1
"""
MIDI Time Code quarter-frame message.

* `data1` contains a time code value
"""

MIDI_SONGPOSPTR = 0xF2
"""
TODO
"""

MIDI_SONGSELECT = 0xF3
"""
TODO
"""

MIDI_TIMINGCLOCK = 0xF8
"""
TODO
"""

MIDI_START = 0xFA
"""
TODO
"""

MIDI_CONTINUE = 0xFB
"""
TODO
"""

MIDI_STOP = 0xFC
"""
TODO
"""

MIDI_ACTIVESENSING = 0xFE
"""
TODO
"""

MIDI_SYSTEMRESET = 0xFF
"""
A system reset message. This is a single byte `0xFF` that instructs the
recipient to reset itself to the default state.
"""

EventNameT = [
    'Note Off',
    'Note On ',  # INVESTIGATE: is this space intentional
    'Key Aftertouch',
    'Control Change',
    'Program Change',
    'Channel Aftertouch',
    'Pitch Bend',
    'System Message',
]
"""
A list of event names, used by some scripts to show information about events.
"""
