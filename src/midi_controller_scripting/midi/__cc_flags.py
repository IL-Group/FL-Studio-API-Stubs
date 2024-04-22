"""
These flags are almost entirely undocumented. I am not sure how they are used.
"""

CC_Normal = 0
"""
Standard CC.
"""
CC_Special = 128
"""
Non-CC are mapped to CC after 128.
"""

CC_PitchBend = 255
"""
Pitch bend?
"""

CC_KeyAfterTouch = 254
"""
Key after-touch?
"""

CC_ChanAfterTouch = 253
"""
Channel after-touch?
"""

CC_Note = 256
"""
When notes are linked to parameters.
"""

CC_Free = 256 + 128
"""
???
"""
CC_PLTrack = CC_Free
"""
Playlist track XY control (performance mode).
"""
