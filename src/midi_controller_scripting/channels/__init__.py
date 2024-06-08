"""
{{module_title[channels]}}

Allows you to control and interact with the FL Studio Channel Rack, and with
instrument channels.

## Contents

* {{docs_url_page("Properties", "midi_controller_scripting/channels/properties")}}:
  functions for accessing properties of generator plugins and channels.

* {{docs_url_page("UI", "midi_controller_scripting/channels/ui")}}: functions
  for interacting with the UI of the channel rack, and with generator plugins.

* {{docs_url_page("Notes", "midi_controller_scripting/channels/notes")}}:
  control notes in channels.

* {{docs_url_page("Sequencers", "midi_controller_scripting/channels/sequencers")}}:
  functions for interacting with the step sequencer.

## Note

* Channels are zero-indexed.
"""
from .__properties import (
    channelNumber,
    channelCount,
    getChannelName,
    setChannelName,
    getChannelColor,
    setChannelColor,
    isChannelMuted,
    muteChannel,
    isChannelSolo,
    soloChannel,
    getChannelVolume,
    setChannelVolume,
    getChannelPan,
    setChannelPan,
    getChannelPitch,
    setChannelPitch,
    getChannelType,
    isChannelSelected,
    selectChannel,
    selectOneChannel,
    selectedChannel,
    selectAll,
    deselectAll,
    getChannelMidiInPort,
    getChannelIndex,
    getTargetFxTrack,
    setTargetFxTrack,
    processRECEvent,
    incEventValue,
    getRecEventId,
)
from .__sequencer import (
    getGridBit,
    getGridBitWithLoop,
    setGridBit,
    isGridBitAssigned,
    getStepParam,
    getCurrentStepParam,
    setStepParameterByIndex,
    updateGraphEditor,
    closeGraphEditor,
)
from .__ui import (
    isHighLighted,
    showGraphEditor,
    isGraphEditorVisible,
    showEditor,
    focusEditor,
    showCSForm,
    getActivityLevel,
)
from .__notes import (
    midiNoteOn,
    quickQuantize,
)


__all__ = (
    'channelNumber',
    'channelCount',
    'getChannelName',
    'setChannelName',
    'getChannelColor',
    'setChannelColor',
    'isChannelMuted',
    'muteChannel',
    'isChannelSolo',
    'soloChannel',
    'getChannelVolume',
    'setChannelVolume',
    'getChannelPan',
    'setChannelPan',
    'getChannelPitch',
    'setChannelPitch',
    'getChannelType',
    'isChannelSelected',
    'selectChannel',
    'selectOneChannel',
    'selectedChannel',
    'selectAll',
    'deselectAll',
    'getChannelMidiInPort',
    'getChannelIndex',
    'getTargetFxTrack',
    'setTargetFxTrack',
    'processRECEvent',
    'incEventValue',
    'getRecEventId',
    'getGridBit',
    'getGridBitWithLoop',
    'setGridBit',
    'isGridBitAssigned',
    'getStepParam',
    'getCurrentStepParam',
    'setStepParameterByIndex',
    'updateGraphEditor',
    'closeGraphEditor',
    'isHighLighted',
    'showGraphEditor',
    'isGraphEditorVisible',
    'showEditor',
    'focusEditor',
    'showCSForm',
    'getActivityLevel',
    'midiNoteOn',
    'quickQuantize',
)
