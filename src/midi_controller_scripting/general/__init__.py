"""
{{module_title[general]}}

The `general` module contains miscellaneous functions to handle general
interaction with FL Studio.

## Contents

* {{docs_url_page("FL State", "midi_controller_scripting/general/fl state")}}:
  access information about the general state of FL Studio.

* {{docs_url_page("Undo", "midi_controller_scripting/general/undo")}}:
  perform undo and redo actions.
"""
__all__ = [
    'saveUndo',
    'undo',
    'undoUp',
    'undoDown',
    'undoUpDown',
    'restoreUndo',
    'restoreUndoLevel',
    'getUndoLevelHint',
    'getUndoHistoryPos',
    'getUndoHistoryCount',
    'getUndoHistoryLast',
    'setUndoHistoryPos',
    'setUndoHistoryCount',
    'setUndoHistoryLast',
    'getRecPPB',
    'getRecPPQ',
    'getUseMetronome',
    'getPrecount',
    'getChangedFlag',
    'getVersion',
    'processRECEvent',
    'dumpScoreLog',
    'clearLog',
    'safeToEdit',
]


from .__fl_state import (
    clearLog,
    dumpScoreLog,
    getChangedFlag,
    getPrecount,
    getRecPPB,
    getRecPPQ,
    getUseMetronome,
    getVersion,
    processRECEvent,
    safeToEdit,
)
from .__undo import (
    getUndoHistoryCount,
    getUndoHistoryLast,
    getUndoHistoryPos,
    getUndoLevelHint,
    restoreUndo,
    restoreUndoLevel,
    saveUndo,
    setUndoHistoryCount,
    setUndoHistoryLast,
    setUndoHistoryPos,
    undo,
    undoDown,
    undoUp,
    undoUpDown,
)
