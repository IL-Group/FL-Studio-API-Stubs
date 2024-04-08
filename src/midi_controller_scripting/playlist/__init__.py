"""
# Playlist

FL Studio built-in module.

Allows you to control and interact with the FL Studio Playlist.

## Note

* Playlist tracks are 1-indexed.

* For information on performance mode, see the
[performance mode tutorial](https://miguelguthridge.github.io/FL-Studio-API-Stubs/tutorials/performance_mode/).
"""

from .__tracks import (
    trackCount,
    getTrackName,
    setTrackName,
    getTrackColor,
    setTrackColor,
    isTrackMuted,
    muteTrack,
    isTrackMuteLock,
    muteTrackLock,
    isTrackSolo,
    soloTrack,
    isTrackSelected,
    selectTrack,
    selectAll,
    deselectAll,
    getTrackActivityLevel,
    getTrackActivityLevelVis,
)

from .__performance import (
    getDisplayZone,
    lockDisplayZone,
    liveDisplayZone,
    getLiveLoopMode,
    getLiveTriggerMode,
    getLivePosSnap,
    getLiveTrigSnap,
    getLiveStatus,
    getLiveBlockStatus,
    getLiveBlockColor,
    triggerLiveClip,
    refreshLiveClips,
    incLivePosSnap,
    incLiveTrigSnap,
    incLiveLoopMode,
    incLiveTrigMode,
    getVisTimeBar,
    getVisTimeTick,
    getVisTimeStep,
    getPerformanceModeState,
    getSongStartTickPos,
    liveBlockNumToTime,
    liveTimeToBlockNum,
    scrollTo,
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
