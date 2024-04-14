"""
The following events can be used to access properties of mixer tracks.
"""
from .ranges import REC_ItemRange, REC_PluginBase, REC_PluginRange

# *** effect plugins (up to 128 mixer tracks*64 plugins)
# designed not to overlap with REC_Chan events, so that they can be merged later
REC_Plug_First = 0x2000 * REC_ItemRange
REC_Plug_Last = REC_Plug_First + 0x2000 * REC_ItemRange - 1

# plugin common properties (up to 256)
REC_Plug_General_First = REC_Plug_First + 0x2000 - 0x100
REC_Plug_General_Last = REC_Plug_General_First + 0x40 - 1
REC_Plug_Mute = REC_Plug_General_First  # mute
"""Whether the FX plugin is muted"""
REC_Plug_MixLevel = REC_Plug_General_First + 1  # mix level
"""Mix level of the FX plugin"""

# mixer track properties
REC_Mixer_First = REC_Plug_General_First + 0x40
REC_Mixer_Last = REC_Mixer_First + 0x800 - 1
REC_Mixer_Send_First = REC_Mixer_First  # sends (up to 128)
REC_Mixer_Send_Last = REC_Mixer_Send_First + 0x80 - 1
REC_Mixer_Vol = REC_Mixer_Send_Last + 1  # volume
REC_Mixer_Pan = REC_Mixer_Vol + 1  # pan
REC_Mixer_SS = REC_Mixer_Vol + 2  # stereo separation

# EQ (up to 8 bands)
REC_Mixer_EQ_First = REC_Mixer_Vol + 0x10
REC_Mixer_EQ_Last = REC_Mixer_EQ_First + 8 * 3 - 1
REC_Mixer_EQ_Gain = REC_Mixer_EQ_First
REC_Mixer_EQ_Freq = REC_Mixer_EQ_First + 8
REC_Mixer_EQ_Q = REC_Mixer_EQ_First + 8 * 2
REC_Mixer_EQ_Type = REC_Mixer_EQ_First + 8 * 3

# linked plugin (>0x8000)
REC_Plug_Plugin_First = REC_Plug_First + REC_PluginBase
REC_Plug_Plugin_Last = REC_Plug_Plugin_First + REC_PluginRange - 1
