"""
The snap mode constants are used by {{docs_url_fn[ui.getSnapMode]}} and
{{docs_url_fn[ui.setSnapMode]}} to represent FL Studio's snap mode.
"""

Snap_Default = -2
"""
Use main snap mode. This only works for the piano roll and playlist snap modes.
"""

Snap_Line = 0
"""
Snap to lines.
"""

Snap_Cell = 1
"""
Snap to cells.
"""

Snap_None = 3
"""
Don't use snapping.
"""

Snap_SixthStep = 4
"""
Snap to 1/6 of a step.
"""

Snap_FourthStep = 5
"""
Snap to 1/4 of a step.
"""

Snap_ThirdStep = 6
"""
Snap to 1/3 of a step.
"""

Snap_HalfStep = 7
"""
Snap to 1/2 of a step.
"""

Snap_Step = 8
"""
Snap to steps.
"""

Snap_SixthBeat = 9
"""
Snap to 1/6 of a beat.
"""

Snap_FourthBeat = 10
"""
Snap to 1/4 of a beat.
"""

Snap_ThirdBeat = 11
"""
Snap to 1/3 of a beat.
"""

Snap_HalfBeat = 12
"""
Snap to 1/2 of a beat.
"""

Snap_Beat = 13
"""
Snap to beats.
"""


Snap_SixthBar = 14
"""
Snap to 1/6 of a bar.
"""

Snap_FourthBar = 15
"""
Snap to 1/4 of a bar.
"""

Snap_ThirdBar = 16
"""
Snap to 1/3 of a bar.
"""

Snap_HalfBar = 17
"""
Snap to 1/2 of a bar.
"""


Snap_Bar = 14
"""
Snap to bars.
"""

Snap_Events = 16
"""
Snap to events.
"""

Snap_Markers = 17
"""
Snap to markers.
"""


Snap_ForceCell = 1 << 8
Snap_AltNone = 2 << 8
Snap_FlagsMask = 0xFF
