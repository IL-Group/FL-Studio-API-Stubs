"""
On refresh flags are passed to the `OnRefresh` callback in order to indicate
what parts of the controller may need to be refreshed.

By checking these flags, controllers can avoid needlessly updating unchanged
parts of their UIs, thus improving performance.

```py
import midi

def OnRefresh(flags: int):
    if flags & midi.HW_Dirty_Mixer_Sel:
        update_mixer_selection_cache()
    if flags & midi.HW_Dirty_LEDs:
        update_led_cache()
    # etc
```
"""

# hardware dirty flags
HW_Dirty_Mixer_Sel = 1
"""
Selected tracks on the mixer have changed.
"""

HW_Dirty_Mixer_Display = 2
"""
Mixer display has changed.
"""

HW_Dirty_Mixer_Controls = 4
"""
Controls on the mixer have changed.
"""

HW_Dirty_RemoteLinks = 16
"""
Remote (linked) controls have been added, removed or modified. Note that
changes to values associated with a remote control will instead give a
`midi.HW_Dirty_RemoteLinkValues` event.
"""

HW_Dirty_FocusedWindow = 32
"""
Selected channel has changed.
"""

HW_Dirty_Performance = 64
"""
Performance mode layout (not playing state) has changed.
"""

HW_Dirty_LEDs = 256
"""
Indicates various possible changes in FL Studio which require update of
controller LEDs (play/stop/record/active window/.....).
"""

HW_Dirty_RemoteLinkValues = 512
"""
Value of remote (linked) control has changed. Note that
creation, deletion or modification of remote control mappings will instead give
a `midi.HW_Dirty_RemoteLinks` event.
"""

HW_Dirty_Patterns = 1024  # selected pattern is changed or pattern self is changed
"""
Changes to patterns or pattern selection.
"""

HW_Dirty_Tracks = 2048  # tracks changes
"""
Changes to mixer tracks?
"""

HW_Dirty_ControlValues = 4096
"""
Changes to plugin control values.
"""

HW_Dirty_Colors = 8192
"""
Changes to plugin colors.
"""

HW_Dirty_Names = 16384
"""
Plugin names have changed.
"""

HW_Dirty_ChannelRackGroup = 32768
"""
Channel rack groups have changed.
"""

HW_ChannelEvent = 65536
"""
Channel changes?
"""
