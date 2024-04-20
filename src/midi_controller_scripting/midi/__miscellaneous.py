"""
Miscellaneous constants and functions defined within `midi.py`.
"""
from .__midi_codes import MIDI_NOTEON


def EncodeRemoteControlID(PortNum: int, ChanNum: int, CCNum: int) -> int:
    """
    Generates a `controlId` given information about an event

    ## Args:
    * `PortNum` (`int`): the port that this event was sent to

    * `ChanNum` (`int`): the channel of this event

    * `CCNum` (`int`): the CC number of this event

    ## Returns:
    * `int`: `controlId`

    Included since API Version 1
    """
    return CCNum + (ChanNum << 16) + ((PortNum + 1) << 22)


MaxInt = 2147483647
"""Maximum signed 32-bit integer."""

GPN_GetCurrentPreset = -1
"""FPN_Preset flags? Potentially a typo?"""

TranzPort_OffOnT = [MIDI_NOTEON, MIDI_NOTEON + (0x7F << 16)]
"""???"""
TranzPort_OffBlinkT = [MIDI_NOTEON, MIDI_NOTEON + (1 << 16)]
"""???"""
TranzPort_OffOnBlinkT = [
    MIDI_NOTEON,
    MIDI_NOTEON + (0x7F << 16),
    MIDI_NOTEON + (1 << 16),
]
"""???"""

FromMIDI_Max = 1073741824
"""
Maximum value allowed when specifying the {{docs_url_attr[midi.REC_FromMIDI]}}
flag when processing a Red event with {{docs_url_fn[general.processRECEvent]}}.
"""
FromMIDI_Half = FromMIDI_Max >> 1
"""
Half of the maximum `midi.REC_FromMIDI` value for Rec events.
"""


EKRes = 1 / 24
"""
Default endless knob (encoder) resolution.

This is set to be 24 ticks per revolution by default.
"""

TrackNum_Master = 0
"""
Track number for the master track in the mixer.
"""

SM_Pat = 0
"""
Pattern loop mode.
"""
SM_Song = 1
"""
Song loop mode.
"""
