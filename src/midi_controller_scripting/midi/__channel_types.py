"""
The channel type constants are returned by the
{{docs_url_fn[channels.getChannelType]}} function, and describe the type of a
channel within the channel rack.

```py
import channels, midi

channel_type = channels.getChannelType(0)

if channel_type == midi.CT_Sampler:
    print("Channel is a sampler")
```
"""

CT_Sampler = 0
"""
Sampler channel.
"""

CT_Hybrid = 1
"""
Generator plugin feeding internal sampler.
"""

CT_TS404 = 1
"""
The [obsolete and unavailable](https://support.image-line.com/action/knowledgebase/?ans=352)
TS404 plugin.
"""

CT_GenPlug = 2
"""
Generator plugin.
"""

CT_Layer = 3
"""
Layer channel. For more information on layers, refer to the
{{fl_manual_page[chansettings_layer.htm]}}.
"""

CT_AudioClip = 4
"""
Audio clip channel.
"""

CT_AutoClip = 5
"""
Automation clip channel.
"""

CT_ColorT = (0x565148 + 0x141414, 0x868178,
             0x514F61, 0x474440, 0x787168, 0x787168)
"""
???

Perhaps default colors for various channel types?
"""
