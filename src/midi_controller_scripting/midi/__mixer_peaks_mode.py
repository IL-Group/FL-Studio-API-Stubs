"""
These flags can be passed to {{docs_url_fn[mixer.getTrackPeaks]}} to control
the kind of peaks returned.

```py
import mixer, midi

# Get left channel peaks for channel 5.
mixer.getTrackPeaks(5, midi.PEAK_L)
```
"""

PEAK_L = 0
"""
Return peaks for left channel.
"""

PEAK_R = 1
"""
Return peaks for right channel.
"""

PEAK_LR = 2
"""
Return maximum peak for both left and right channels.
"""

PEAK_LR_INV = 3
"""
Return inverted maximum peak for both left and right channels.

TODO: what is an inverted peak?
"""
