"""
Special Rec event IDs, which facilitate remote control from external apps.

None of these appear to have any effect, so I am unsure how to use them.
"""

REC_Reserved = 0x80000000
"""Reserved for future use."""

# special commands
# for remote control by external apps
REC_Special = -1
"""End of special event IDs -- all special event IDs are < this value."""

REC_StartStop = REC_Special  # 0=Stop, 1=Start
"""
Start/stop.

* `0` = stop
* `1` = start
"""
REC_SongPosition = REC_Special - 1
"""Get/set song position (in bars)."""
REC_SongLength = REC_Special - 2
"""Get song length (in bars)."""

REC_LastTweakedFirst = -32
"""Last-tweaked parameter?"""

REC_LastTweakedLast = REC_LastTweakedFirst + 1
"""Another last-tweaked parameter?"""

REC_Proj_First = REC_Special - 0x100
"""For the project browser."""
