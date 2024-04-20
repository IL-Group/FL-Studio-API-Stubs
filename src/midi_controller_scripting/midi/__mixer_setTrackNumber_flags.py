"""
These flags are used to control the mixer window's behavior when selecting a
track using {{docs_url_fn[mixer.setTrackNumber]}}.

```py
import mixer
import midi

# Select track 50 and scroll to make it visible
mixer.setTrackNumber(50, midi.curfxScrollToMakeVisible)
```

These constants can be combined using a bitwise or to specify multiple flags
simultaneously.

```py
# Select track 100, scrolling to make it visible, and not deselecting other
# tracks
mixer.setTrackNumber(
    50,
    midi.curfxScrollToMakeVisible | midi.curfxNoDeselectAll,
)
```
"""

curfxScrollToMakeVisible = 1
"""
Scroll within the mixer such that the newly selected track becomes visible.
"""

StartcurfxCancelSmoothing = 1 << 1
"""
Cancel smoothing.
"""

curfxNoDeselectAll = 1 << 2
"""
Don't deselect all tracks before selecting this track.

This doesn't appear to work correctly.
"""

curfxMinimalLatencyUpdate = 1 << 3
"""
TODO
"""
