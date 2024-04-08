"""
# Launchmap Pages

FL Studio built-in module.

Handles custom controller layouts for certain controllers.

Refer to [reference](https://forum.image-line.com/viewtopic.php?f=1914&t=92193).

## HELP WANTED

* More detailed explanations would be good, since it's not very well
  explained by the manual.
"""
__all__ = [
    'init',
    'createOverlayMap',
    'length',
    'updateMap',
    'getMapItemColor',
    'getMapCount',
    'getMapItemChannel',
    'getMapItemAftertouch',
    'processMapItem',
    'releaseMapItem',
    'checkMapForHiddenItem',
    'setMapItemTarget',
]

from .__launchMapPages import (
    init,
    createOverlayMap,
    length,
    updateMap,
    getMapItemColor,
    getMapCount,
    getMapItemChannel,
    getMapItemAftertouch,
    processMapItem,
    releaseMapItem,
    checkMapForHiddenItem,
    setMapItemTarget,
)
