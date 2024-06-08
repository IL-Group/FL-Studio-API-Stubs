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
"""
from .__properties import (
    patternNumber,
    patternCount,
    patternMax,
    getPatternName,
    setPatternName,
    getPatternColor,
    setPatternColor,
    getPatternLength,
    jumpToPattern,
    findFirstNextEmptyPat,
    isPatternSelected,
    selectPattern,
    selectAll,
    deselectAll,
    burnLoop,
    isPatternDefault,
    clonePattern,
    getChannelLoopStyle,
    setChannelLoop,
)
from .__performance import (
    getBlockSetStatus,
    ensureValidNoteRecord,
)
from .__groups import (
    getActivePatternGroup,
    getPatternGroupCount,
    getPatternGroupName,
    getPatternsInGroup,
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
