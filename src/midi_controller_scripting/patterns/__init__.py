"""
{{module_title[patterns]}}

Allows you to control and interact with FL Studio Patterns.

## Contents

* {{docs_url_page("Properties", "midi_controller_scripting/patterns/properties")}}:
  functions for accessing properties of patterns.

* {{docs_url_page("Groups", "midi_controller_scripting/patterns/groups")}}:
  functions for controlling pattern groups.

* {{docs_url_page("Performance", "midi_controller_scripting/patterns/performance")}}:
  functions for interacting with performance mode patterns.

## Note

* Patterns are 1-indexed, with a range from `1` - `999`, meaning that the
  1000th pattern cannot be created.

* Multiple patterns can be selected, but only one pattern is considered to be
  the active pattern (indicated by an arrow to the left of its entry in the
  pattern picker).
"""
from .__groups import (
    getActivePatternGroup,
    getPatternGroupCount,
    getPatternGroupName,
    getPatternsInGroup,
)
from .__performance import (
    ensureValidNoteRecord,
    getBlockSetStatus,
)
from .__properties import (
    burnLoop,
    clonePattern,
    deselectAll,
    findFirstNextEmptyPat,
    getChannelLoopStyle,
    getPatternColor,
    getPatternLength,
    getPatternName,
    isPatternDefault,
    isPatternSelected,
    jumpToPattern,
    patternCount,
    patternMax,
    patternNumber,
    selectAll,
    selectPattern,
    setChannelLoop,
    setPatternColor,
    setPatternName,
)

__all__ = (
    'patternNumber',
    'patternCount',
    'patternMax',
    'getPatternName',
    'setPatternName',
    'getPatternColor',
    'setPatternColor',
    'getPatternLength',
    'jumpToPattern',
    'findFirstNextEmptyPat',
    'isPatternSelected',
    'selectPattern',
    'selectAll',
    'deselectAll',
    'burnLoop',
    'isPatternDefault',
    'getBlockSetStatus',
    'ensureValidNoteRecord',
    'clonePattern',
    'getChannelLoopStyle',
    'setChannelLoop',
    'getActivePatternGroup',
    'getPatternGroupCount',
    'getPatternGroupName',
    'getPatternsInGroup',
)
