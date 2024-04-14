"""
The following events can be used to access properties of channels by combining
them with the return value of {{docs_url_fn[channels.getRecEventId]}}.

```py
import channels
import general
import midi

# Create event ID to target channel 1's channel pitch
event_id = channels.getRecEventId(1) + midi.REC_Chan_Pitch

# Process the event to set the channel pitch to the minimum value (likely -200
# cents)
general.processRECEvent(event_id, 0, midi.REC_MIDIController)
```
"""
from .ranges import REC_Chan_First, REC_PluginBase, REC_PluginRange

REC_Chan_Vol = REC_Chan_First
"""
Event ID offset for channel volume.
"""

REC_Chan_Pan = REC_Chan_First + 1
"""
Event ID offset for channel pan.
"""

REC_Chan_FCut = REC_Chan_First + 2
"""
Event ID offset for channel filter cutoff.
"""

REC_Chan_FRes = REC_Chan_First + 3
"""
Event ID offset for channel filter resonance.
"""

REC_Chan_Pitch = REC_Chan_First + 4
"""
Event ID offset for channel pitch.
"""

REC_Chan_FType = REC_Chan_First + 5
"""
Event ID offset for channel filter type.
"""

REC_Chan_PortaTime = REC_Chan_First + 6
"""
Event ID offset for channel portamento time.
"""

REC_Chan_Mute = REC_Chan_First + 7
"""
Event ID offset for channel mute.
"""

REC_Chan_FXTrack = REC_Chan_First + 8
"""
Event ID offset for channel target FX track.
"""

REC_Chan_GateTime = REC_Chan_First + 9
"""
Event ID offset for channel gate time.
"""

REC_Chan_Crossfade = REC_Chan_First + 10
"""
Event ID offset for channel cross-fade.
"""

REC_Chan_TimeOfs = REC_Chan_First + 11
"""
Event ID offset for channel time offset.
"""

REC_Chan_SwingMix = REC_Chan_First + 12
"""
Event ID offset for channel swing mix.
"""

REC_Chan_SmpOfs = REC_Chan_First + 13
"""
Event ID offset for channel sample offset.
"""

REC_Chan_StretchTime = REC_Chan_First + 14
"""
Event ID offset for channel time stretch (time).
"""

REC_Chan_OfsPan = REC_Chan_First + 16
"""
Event ID offset for pan offset (in levels adjustment section of "Miscellaneous
functions")
"""

REC_Chan_OfsVol = REC_Chan_First + 17
"""
Event ID offset for volume offset (in levels adjustment section of
"Miscellaneous functions")
"""

REC_Chan_OfsPitch = REC_Chan_First + 18
"""
Event ID offset for pitch offset (in levels adjustment section of
"Miscellaneous functions").
"""

REC_Chan_OfsFCut = REC_Chan_First + 19
"""
Event ID offset for modulation X offset  (in levels adjustment section of
"Miscellaneous functions").
"""

REC_Chan_OfsFRes = REC_Chan_First + 20
"""
Event ID offset for modulation Y offset  (in levels adjustment section of
"Miscellaneous functions").
"""

# delay
REC_Chan_Delay_First = REC_Chan_First + 0x200
"""
Start of event IDs for channel built-in delay.
"""
REC_Chan_Delay_Last = REC_Chan_Delay_First + 0x100 - 1
"""
End of event IDs for channel built-in delay.
"""
REC_Chan_Delay_Time = REC_Chan_Delay_First + 4
"""
Delay time for channel built-in delay.
"""

REC_Chan_Arp_First = REC_Chan_First + 0x300
"""
Start of event IDs for channel built-in arpeggiator.
"""
REC_Chan_Arp_Last = REC_Chan_Arp_First + 0x100 - 1
"""
End of event IDs for channel built-in arpeggiator.
"""
REC_Chan_Arp_Chord = REC_Chan_Arp_First + 2
"""
Chord type for channel built-in arpeggiator.
"""
REC_Chan_Arp_Time = REC_Chan_Arp_First + 3
"""
Arpeggio time for channel built-in arpeggiator.
"""
REC_Chan_Arp_Gate = REC_Chan_Arp_First + 4
"""
Gate for channel built-in arpeggiator.
"""
REC_Chan_Arp_Repeat = REC_Chan_Arp_First + 5
"""
Repeat option for channel built-in arpeggiator.
"""

# misc
REC_Chan_Misc = REC_Chan_First + 0x400

# tracking
REC_Chan_Track_First = REC_Chan_First + 0x500
REC_Chan_Track_PLast = REC_Chan_Track_First + 2
REC_Chan_Track_Last = REC_Chan_Track_First + 0x100 - 1

# automation articulator
REC_Chan_AC_First = REC_Chan_First + 0x600
REC_Chan_AC_Last = REC_Chan_AC_First + 0x100 - 1

# envelope
REC_Chan_Env_First = REC_Chan_First + 0x1000
REC_Chan_Env_LFO_First = REC_Chan_Env_First + 9
REC_Chan_Env_MA = REC_Chan_Env_First + 8
REC_Chan_Env_LFOA = REC_Chan_Env_First + 11
REC_Chan_Env_Hole = REC_Chan_Env_LFOA + 2
REC_Chan_Env_PLast = REC_Chan_Env_Hole + 3
REC_Chan_Env_Last = REC_Chan_Env_First + 0x800 - 1

# note events
REC_Chan_Note_First = REC_Chan_First + 0x4000
REC_Chan_Note_Num = 0x20
REC_Chan_Note_Last = REC_Chan_Note_First + REC_Chan_Note_Num

REC_Chan_NoteOn = REC_Chan_Note_First
REC_Chan_NoteMask = 0xFFFFFFF0
# slides
REC_Chan_NoteSlideMask = 8
REC_Chan_NoteSlide = REC_Chan_NoteOn + REC_Chan_NoteSlideMask
REC_Chan_NoteSlideTo = REC_Chan_NoteSlide
REC_Chan_NoteSlideOfs = REC_Chan_NoteSlide + 1
# misc
REC_Chan_NoteOff = REC_Chan_NoteOn + 0x20
REC_Chan_PianoRoll = REC_Chan_NoteOn

REC_Chan_Clip = REC_Chan_First + 0x5000

# linked plugin (>0x8000)
REC_Chan_Plugin_First = REC_Chan_First + REC_PluginBase
REC_Chan_Plugin_Last = REC_Chan_Plugin_First + REC_PluginRange - 1
