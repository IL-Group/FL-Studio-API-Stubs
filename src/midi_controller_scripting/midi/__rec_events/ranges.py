"""
These constants are used to define ranges of values for {{docs_url_page(
    "rec events",
    "midi_controller_scripting/tutorials/event_mapping"
)}}.
"""

REC_ItemRange = 0x10000
"""
The number of event IDs allocated to each item (channel or mixer track or
plugin).
"""

REC_TrackRange = 0x10
REC_EnvRange = 0x100
REC_PluginBase = 0x8000
REC_PluginRange = 0x8000
REC_ItemMask = 0xFFFF

REC_MaxChan = 0x1000
"""
The maximum number of channels supported by FL Studio.
"""

REC_MaxPat = 0x1000
"""
The maximum number of patterns supported by FL Studio.
"""

REC_GlobalChan = REC_MaxChan - 1

REC_GlobalPlugTrack = 128 - 1
REC_GlobalPlug = (0x2000 >> 6) + REC_GlobalPlugTrack
REC_MixerMask = 0x3FFFFF

REC_Chan_First = 0
"""
Rec event ID for first event associated with channels.
"""

REC_Chan_Last = REC_MaxChan * REC_ItemRange - 1
"""
Rec event ID for last event associated with channels.
"""
REC_Global_First = 0x4000 * REC_ItemRange
"""
Rec event ID for first event associated with global FL Studio parameters.
"""
REC_Global_Last = REC_Global_First + REC_ItemRange
"""
Rec event ID for last event associated with global FL Studio parameters.
"""
