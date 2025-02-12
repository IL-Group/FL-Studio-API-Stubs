"""
{{module_title[playlist]}}

FL Studio built-in module.

Allows you to control and interact with the FL Studio Playlist.

## Note

* Playlist tracks are 1-indexed.

* For information on performance mode, see the
{{docs_url_page("performance mode tutorial", "midi_controller_scripting/tutorials/performance_mode/")}}.
"""

from .__performance import (
    getDisplayZone,
    getLiveBlockColor,
    getLiveBlockStatus,
    getLiveLoopMode,
    getLivePosSnap,
    getLiveStatus,
    getLiveTriggerMode,
    getLiveTrigSnap,
    getPerformanceModeState,
    getSongStartTickPos,
    getVisTimeBar,
    getVisTimeStep,
    getVisTimeTick,
    incLiveLoopMode,
    incLivePosSnap,
    incLiveTrigMode,
    incLiveTrigSnap,
    liveBlockNumToTime,
    liveDisplayZone,
    liveTimeToBlockNum,
    lockDisplayZone,
    refreshLiveClips,
    scrollTo,
    triggerLiveClip,
)
from .__tracks import (
    deselectAll,
    getTrackActivityLevel,
    getTrackActivityLevelVis,
    getTrackColor,
    getTrackName,
    isTrackMuted,
    isTrackMuteLock,
    isTrackSelected,
    isTrackSolo,
    muteTrack,
    muteTrackLock,
    selectAll,
    selectTrack,
    setTrackColor,
    setTrackName,
    soloTrack,
    trackCount,
)

__all__ = [
    "trackCount",
    "getTrackName",
    "setTrackName",
    "getTrackColor",
    "setTrackColor",
    "isTrackMuted",
    "muteTrack",
    "isTrackMuteLock",
    "muteTrackLock",
    "isTrackSolo",
    "soloTrack",
    "isTrackSelected",
    "selectTrack",
    "selectAll",
    "deselectAll",
    "getTrackActivityLevel",
    "getTrackActivityLevelVis",
    "getDisplayZone",
    "lockDisplayZone",
    "liveDisplayZone",
    "getLiveLoopMode",
    "getLiveTriggerMode",
    "getLivePosSnap",
    "getLiveTrigSnap",
    "getLiveStatus",
    "getLiveBlockStatus",
    "getLiveBlockColor",
    "triggerLiveClip",
    "refreshLiveClips",
    "incLivePosSnap",
    "incLiveTrigSnap",
    "incLiveLoopMode",
    "incLiveTrigMode",
    "getVisTimeBar",
    "getVisTimeTick",
    "getVisTimeStep",
    "getPerformanceModeState",
    "getSongStartTickPos",
    "liveBlockNumToTime",
    "liveTimeToBlockNum",
    "scrollTo",
]
