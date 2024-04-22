"""
{{module_title[arrangement]}}

The `arrangement` module provides functions to allow for interaction with
FL Studio arrangements, including markers, selections and timestamps.

## Table of contents

* {{docs_url_page("Live", "midi_controller_scripting/arrangement/live")}}: live
  performance functions.

* {{docs_url_page("Markers", "midi_controller_scripting/arrangement/markers")}}:
  accessing information about markers on the playlist.

* {{docs_url_page("Selection", "midi_controller_scripting/arrangement/selection")}}:
  access information about the current selection on the playlist.

* {{docs_url_page("Time", "midi_controller_scripting/arrangement/time")}}:
  access information about the current time within the song.
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
