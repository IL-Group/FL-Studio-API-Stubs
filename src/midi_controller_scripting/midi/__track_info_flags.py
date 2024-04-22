"""
Track info flags are used with {{docs_url_fn[mixer.getTrackInfo]}} to control
which information is returned.

For example, to iterate over all insert tracks (excluding master and the
"current" track):

```py
import mixer, midi

for i in range(
    mixer.getTrackInfo(midi.TN_FirstIns),
    mixer.getTrackInfo(midi.TN_LastIns) + 1,
):
    ...
```
"""

TN_Master = 0
"""
Return index of master track.
"""

TN_FirstIns = 1
"""
Return index of first insert.
"""

TN_LastIns = 2
"""
Return index of last insert.
"""

TN_Sel = 3
"""
Return index of the "Current" track.

This is a special track that receives audio from whichever track is currently
selected.
"""
