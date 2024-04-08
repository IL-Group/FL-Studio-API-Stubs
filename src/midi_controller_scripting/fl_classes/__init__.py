"""
fl_classes

This module contains definitions for FL Studio's built-in types, which can be
used to assist with type hinting in your project.

NOTE: This module is not included in FL Studio's runtime.

```py
try:
    from fl_classes import FlMidiMsg
except ImportError:
    FlMidiMsg = 'FlMidiMsg'

def OnMidiIn(event: FlMidiMsg) -> None:
    ...
```
"""
from .__fl_midi_msg import FlMidiMsg

__all__ = ['FlMidiMsg']
