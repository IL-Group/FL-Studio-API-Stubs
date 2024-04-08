"""
{{module_title[device]}}

FL Studio built-in module.

Handles the way that devices connect to FL Studio's MIDI interface, and how
scripts communicate with each other.
"""

__all__ = [
    'isAssigned',
    'isMidiOutAssigned',
    'getPortNumber',
    'getName',
    'midiOutMsg',
    'midiOutNewMsg',
    'midiOutSysex',
    'sendMsgGeneric',
    'directFeedback',
    'repeatMidiEvent',
    'stopRepeatMidiEvent',
    'setMasterSync',
    'getMasterSync',
    'processMIDICC',
    'forwardMIDICC',
    'findEventID',
    'getLinkedValue',
    'getLinkedValueString',
    'getLinkedParamName',
    'getLinkedInfo',
    'dispatch',
    'dispatchReceiverCount',
    'dispatchGetReceiverPortNumber',
    'createRefreshThread',
    'destroyRefreshThread',
    'fullRefresh',
    'isDoubleClick',
    'getDeviceID',
    'getLinkedChannel',
    'linkToLastTweaked',
    'getIdleElapsed',
    'setHasMeters',
    'baseTrackSelect',
    'hardwareRefreshMixerTrack',
]

from .__device import (
    isAssigned,
    isMidiOutAssigned,
    getPortNumber,
    getName,
    midiOutMsg,
    midiOutNewMsg,
    midiOutSysex,
    sendMsgGeneric,
    directFeedback,
    repeatMidiEvent,
    stopRepeatMidiEvent,
    setMasterSync,
    getMasterSync,
    getDeviceID,
)
from .__fl import (
    processMIDICC,
    forwardMIDICC,
    findEventID,
    getLinkedValue,
    getLinkedValueString,
    getLinkedParamName,
    getLinkedInfo,
    getLinkedChannel,
    linkToLastTweaked,
    getIdleElapsed,
)
from .__dispatch import (
    dispatch,
    dispatchReceiverCount,
    dispatchGetReceiverPortNumber,
)
from .__util import (
    createRefreshThread,
    destroyRefreshThread,
    fullRefresh,
    isDoubleClick,
    setHasMeters,
    baseTrackSelect,
    hardwareRefreshMixerTrack,
)
