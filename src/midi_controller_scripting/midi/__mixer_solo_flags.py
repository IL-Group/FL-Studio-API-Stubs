"""
These flags can be used alongside {{docs_url_fn[mixer.soloTrack]}} to control
the solo state of tracks.

These flags can be combined using bitwise operations.

```py
import mixer, midi

# Solo track one, keeping both source and destination tracks enabled.
mixer.soloTrack(1, midi.fxSoloModeWithSourceTracks | fxSoloModeWithDestTracks)
```
"""

fxSoloModeWithSourceTracks = 1
"""
Solo mixer track, including source tracks routed to it.
"""

fxSoloModeWithDestTracks = 1 << 1
"""
Solo mixer track, including send tracks that it is routed to.
"""

fxSoloModeIgnorePrevious = 1 << 2
"""
Solo only this track, muting all other tracks.
"""

# Undocumented
fxSoloSetOff = 0
fxSoloSetOn = 1
fxSoloToggle = 2
fxSoloGetValue = 3
