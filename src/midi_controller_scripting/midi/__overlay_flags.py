"""
Overlay flags are used by functions such as {{docs_url_fn[ui.crDisplayRect]}}
to control options for displaying the overlay.

For example, to make FL Studio highlight channel names and mute buttons, and
scroll to the selected channels:

```py
import ui
import midi

ui.crDisplayRect(
    0, 1, 1, 3,
    2000,
    flags=midi.CR_HighlightChannelName
    | midi.CR_ScrollToView
    | midi.CR_HighlightChannelMute
)
```
"""

CR_HighlightChannels = 1
"""
When specified, {{docs_url_fn("ui.crDisplayRect", suffix="()")}} highlights
channel buttons.
"""

CR_ScrollToView = 1 << 1
"""
When specified, {{docs_url_fn("ui.crDisplayRect", suffix="()")}} scrolls so
that the given area is visible.
"""

CR_HighlightChannelMute = 1 << 2
"""
When specified, {{docs_url_fn("ui.crDisplayRect", suffix="()")}} highlights
channel mute buttons.
"""

CR_HighlightChannelPanVol = 1 << 3
"""
When specified, {{docs_url_fn("ui.crDisplayRect", suffix="()")}} highlights
channel pan and volume.
"""

CR_HighlightChannelTrack = 1 << 4
"""
When specified, {{docs_url_fn("ui.crDisplayRect", suffix="()")}} highlights
target mixer track controls.
"""

CR_HighlightChannelName = 1 << 5
"""
When specified, {{docs_url_fn("ui.crDisplayRect", suffix="()")}} highlights
channel names.
"""

CR_HighlightChannelSelect = 1 << 6
"""
When specified, {{docs_url_fn("ui.crDisplayRect", suffix="()")}} highlights
channel selection buttons.
"""

MI_ScrollToView = 1 << 1
"""
When specified, {{docs_url_fn("ui.miDisplayRect", suffix="()")}} scrolls so
that the given mixer tracks are visible.
"""
