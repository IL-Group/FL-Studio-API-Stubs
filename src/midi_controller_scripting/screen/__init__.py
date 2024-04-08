"""
# Screen

FL Studio built-in module.

Helper functions for controlling the screen of the AKAI FL Studio Fire MIDI
controller.

These likely aren't useful for most scripts, but if you're writing a script for
the Fire they might be handy.

## HELP WANTED

These functions are undocumented. If you know how they work, I'd massively
appreciate a pull request with improvements to the type safety and
documentation.
"""
__all__ = [
    'init',
    'deInit',
    'setup',
    'update',
    'addMeter',
    'addTextLine',
    'animateText',
    'blank',
    'displayBar',
    'displayText',
    'displayTimedText',
    'drawRect',
    'drawText',
    'eraseRect',
    'fillRect',
    'findTextLine',
    'getScreenActiveCounter',
    'hideMenu',
    'isBlanked',
    'isUnBlank',
    'keepDisplayActive',
    'menuItemClick',
    'menuNext',
    'menuPrev',
    'menuShowing',
    'removeTextLine',
    'setScreenActiveCounter',
    'unBlank',
]


from .__screen import (
    init,
    deInit,
    setup,
    update,
    addMeter,
    addTextLine,
    animateText,
    blank,
    displayBar,
    displayText,
    displayTimedText,
    drawRect,
    drawText,
    eraseRect,
    fillRect,
    findTextLine,
    getScreenActiveCounter,
    hideMenu,
    isBlanked,
    isUnBlank,
    keepDisplayActive,
    menuItemClick,
    menuNext,
    menuPrev,
    menuShowing,
    removeTextLine,
    setScreenActiveCounter,
    unBlank,
)
