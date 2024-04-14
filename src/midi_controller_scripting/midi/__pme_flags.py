"""
PME (process MIDI event) flags are used by FL Studio in order to represent
additional information about an event, and FL Studio's state while processing
the event.

```py
import midi

def OnMidiIn(msg: FlMidiMsg):
    if msg.pmeFlags & midi.PME_System:
        print("Safe to perform system operations")
```
"""

PME_LiveInput = 1
"""
TODO
"""

PME_System = 1 << 1
"""
Safe to perform common system operations, such as starting/stopping transport.
"""

PME_System_Safe = 1 << 2
"""
Safe to perform critical system operations, such as adding markers.

This flag is unset when a model window is shown.
"""

PME_PreviewNote = 1 << 3
"""
This event will trigger a preview note or control things.
"""

PME_FromHost = 1 << 4
"""
When FL Studio is hosted as a VST, this indicates that the event originates
from the host DAW.
"""

PME_FromMIDI = 1 << 5
"""
The event originates from an (external?) MIDI event.
"""

PME_FromScript = 1 << 6
"""
The event originates from another script? (ie via
{{docs_url_fn("device.dispatch", suffix="()")}}).
"""
