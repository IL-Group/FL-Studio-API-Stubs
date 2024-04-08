"""
# Transport

FL Studio built-in module.

Handles transport in FL Studio, including example playback and recording.
"""
from .__position import (
    start,
    stop,
    isPlaying,
    record,
    isRecording,
    getLoopMode,
    setLoopMode,
    globalTransport,
)
from .__state import (
    getSongPos,
    setSongPos,
    getSongLength,
    getSongPosHint,
    markerJumpJog,
    markerSelJog,
    getHWBeatLEDState,
    rewind,
    fastForward,
    continuousMove,
    continuousMovePos,
    setPlaybackSpeed,
)


__all__ = (
    'start',
    'stop',
    'isPlaying',
    'record',
    'isRecording',
    'getLoopMode',
    'setLoopMode',
    'globalTransport',
    'getSongPos',
    'setSongPos',
    'getSongLength',
    'getSongPosHint',
    'markerJumpJog',
    'markerSelJog',
    'getHWBeatLEDState',
    'rewind',
    'fastForward',
    'continuousMove',
    'continuousMovePos',
    'setPlaybackSpeed',
)
