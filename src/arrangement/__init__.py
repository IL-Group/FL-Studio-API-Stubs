"""
# Arrangement

FL Studio built-in module.

Allows you to control and interact with FL Studio Arrangements, including
markers, selections and timestamps.
"""
__all__ = [
    'liveSelection',
    'liveSelectionStart',
    'jumpToMarker',
    'getMarkerName',
    'addAutoTimeMarker',
    'selectionStart',
    'selectionEnd',
    'currentTime',
    'currentTimeHint',
]


from .__live import (
    liveSelection,
    liveSelectionStart,
)
from .__markers import (
    jumpToMarker,
    getMarkerName,
    addAutoTimeMarker,
)
from .__selection import (
    selectionStart,
    selectionEnd,
)
from .__time import (
    currentTime,
    currentTimeHint,
)
