"""
{{module_title[ui]}}

The `ui` module provides many functions used for interacting with many parts
of FL Studio's user interface.

* {{docs_url_page("Navigation", "midi_controller_scripting/ui/navigation")}}:
  perform generic navigation commands. These functions can be used for binding
  arrow buttons, jog wheels and touch scripts in MIDI Controllers.

* {{docs_url_page("Windows", "midi_controller_scripting/ui/windows")}}:
  interact with and control FL Studio's window management, including switching
  between windows, and determining which windows are visible/active.

* {{docs_url_page("Browser", "midi_controller_scripting/ui/browser")}}:
  interact with and control FL Studio's content browser window. This allows you
  to navigate and select items from the browser tree, as well as navigate
  between browser tabs.

* {{docs_url_page("State", "midi_controller_scripting/ui/state")}}:
  query the general state of FL Studio and its UI, including the hint panel,
  time panel, and other properties.

* {{docs_url_page("Keyboard", "midi_controller_scripting/ui/keyboard")}}:
  interact with FL Studio using keyboard shortcuts. This can be used to perform
  actions such as copy/paste.

* {{docs_url_page("Overlays", "midi_controller_scripting/ui/overlays")}}:
  create UI overlays to indicate the state of your script. These functions can
  show selected regions on the playlist, channel rack and mixer.

* {{docs_url_page("Editors", "midi_controller_scripting/ui/editors")}}:
  launch editor windows, such as Edison or the event editor.
"""
from .__browser import (
    getFocusedNodeCaption,
    getFocusedNodeFileType,
    isBrowserAutoHide,
    navigateBrowser,
    navigateBrowserMenu,
    navigateBrowserTabs,
    previewBrowserMenuItem,
    selectBrowserMenuItem,
    setBrowserAutoHide,
    toggleBrowserNode,
)
from .__editors import (
    launchAudioEditor,
    openEventEditor,
)
from .__keyboard import (
    copy,
    cut,
    delete,
    down,
    enter,
    escape,
    insert,
    left,
    no,
    paste,
    right,
    up,
    yes,
)
from .__navigation import (
    closeActivePopupMenu,
    horZoom,
    isInPopupMenu,
    jog,
    jog2,
    moveJog,
    next,
    previous,
    strip,
    stripHold,
    stripJog,
    verZoom,
)
from .__overlays import (
    crDisplayRect,
    miDisplayDockRect,
    miDisplayRect,
)
from .__state import (
    getHintMsg,
    getHintValue,
    getProgTitle,
    getSnapMode,
    getStepEditMode,
    getTimeDispMin,
    getVersion,
    isClosing,
    isLoopRecEnabled,
    isMetronomeEnabled,
    isPrecountEnabled,
    isStartOnInputEnabled,
    setHintMsg,
    setSnapMode,
    setStepEditMode,
    setTimeDispMin,
    showNotification,
    snapMode,
    snapOnOff,
)
from .__windows import (
    closeAllMenu,
    getFocused,
    getFocusedFormCaption,
    getFocusedFormID,
    getFocusedPluginName,
    getVisible,
    hideWindow,
    nextWindow,
    scrollWindow,
    selectWindow,
    setFocused,
    showWindow,
)

__all__ = [
    'navigateBrowser',
    'navigateBrowserMenu',
    'navigateBrowserTabs',
    'toggleBrowserNode',
    'previewBrowserMenuItem',
    'selectBrowserMenuItem',
    'getFocusedNodeCaption',
    'getFocusedNodeFileType',
    'isBrowserAutoHide',
    'setBrowserAutoHide',
    'launchAudioEditor',
    'openEventEditor',
    'isClosing',
    'isMetronomeEnabled',
    'isStartOnInputEnabled',
    'isPrecountEnabled',
    'isLoopRecEnabled',
    'getSnapMode',
    'setSnapMode',
    'snapMode',
    'snapOnOff',
    'getTimeDispMin',
    'setTimeDispMin',
    'getHintMsg',
    'setHintMsg',
    'showNotification',
    'getHintValue',
    'getProgTitle',
    'getVersion',
    'getStepEditMode',
    'setStepEditMode',
    'cut',
    'copy',
    'paste',
    'insert',
    'delete',
    'enter',
    'escape',
    'yes',
    'no',
    'up',
    'down',
    'left',
    'right',
    'jog',
    'jog2',
    'strip',
    'stripJog',
    'stripHold',
    'previous',
    'next',
    'moveJog',
    'horZoom',
    'verZoom',
    'isInPopupMenu',
    'closeActivePopupMenu',
    'crDisplayRect',
    'miDisplayRect',
    'miDisplayDockRect',
    'getVisible',
    'showWindow',
    'hideWindow',
    'getFocused',
    'setFocused',
    'getFocusedFormCaption',
    'getFocusedFormID',
    'getFocusedPluginName',
    'scrollWindow',
    'nextWindow',
    'selectWindow',
    'closeAllMenu',
]
