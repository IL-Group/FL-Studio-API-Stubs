"""
The following events can be used to access global properties of the current FL
Studio project.

```py
import general
import midi

# Set tempo to 80.5 BPM
general.processRECEvent(
    # Target global tempo
    midi.REC_Tempo,
    # 80.5 BPM (* 1000)
    80500,
    # Set value and update the display in FL Studio
    midi.REC_Control | midi.REC_UpdateControl,
)
```
"""
from .ranges import REC_Global_First

REC_MainVol = REC_Global_First
"""FL Studio's main volume."""

REC_MainShuffle = REC_Global_First + 1
"""FL Studio's main swing, found in the channel rack."""

REC_MainPitch = REC_Global_First + 2
"""FL Studio's main pitch."""

REC_MainFRes = REC_Global_First + 3
"""Main filter -- obsolete."""
REC_MainFCut = REC_Global_First + 4
"""Main filter -- obsolete."""

REC_Tempo = REC_Global_First + 5
"""
Project tempo.

This is stored as `1000 * tempo`, meaning that to set a tempo of `85 BPM`, you
will need to set the value as `85 * 1000`.
"""
