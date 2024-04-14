"""
These flags are used for {{docs_url_fn("playlist.triggerLiveClip", suffix="()")}},
allowing you to specify options for how live clips should be triggered.
"""

TLC_MuteOthers = 1
"""
TODO
"""

TLC_Fill = 1 << 1
"""
TODO
"""

TLC_Queue = 1 << 2
"""
Queue mode.
"""

TLC_Release = 1 << 5
"""
TODO
"""

TLC_NoPlayCheck = 1 << 6
"""
TODO
"""

TLC_NoHardwareUpdate = 1 << 30
"""
TODO
"""

TLC_SecondPass = 1 << 31  # system
"""
TODO
"""


TLC_ColumnMode = 1 << 7  # scene
"""
Scene mode.
"""

TLC_WeakColumnMode = 1 << 8  # +scene
"""
+ Scene mode.
"""

TLC_TriggerCheckColumnMode = 1 << 9  # same press mode
"""
TODO
"""

TLC_TrackSnap = 0 << 3
"""
Use performance mode track setting as trigger snap.
"""

TLC_GlobalSnap = 1 << 3
"""
Use FL Studio's global snap value as trigger snap.
"""

TLC_NoSnap = 2 << 3
"""
Bypass all trigger snapping.
"""

TLC_SubNum_Normal = 0 << 16
"""
TODO
"""

TLC_SubNum_ClipPos = 1 << 16
"""
TODO
"""

TLC_SubNum_GroupNum = 2 << 16
"""
TODO
"""

TLC_SubNum_Read = 3 << 16
"""
TODO
"""

TLC_SubNum_Leave = 4 << 16
"""
TODO
"""
