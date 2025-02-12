"""
Rec events (recorded events) are events used to control any parameter within
FL Studio, and are the underlying architecture for controlling most parts of
FL Studio.

For more information, check out the {{docs_url_page(
    "tutorial on event mapping",
    "midi_controller_scripting/tutorials/event_mapping"
)}}.

## Table of contents

* [Process flags](./process flags)

* [Ranges](./ranges)

* [Global properties](./global properties)

* [Channel properties](./channel properties)

* [Mixer properties](./mixer properties)

* [Playlist properties](./playlist properties)

* [Special properties](./special)

* [TS404 (deprecated)](./ts404)
"""

from .channel_properties import (
    REC_Chan_AC_First,
    REC_Chan_AC_Last,
    REC_Chan_Arp_Chord,
    REC_Chan_Arp_First,
    REC_Chan_Arp_Gate,
    REC_Chan_Arp_Last,
    REC_Chan_Arp_Repeat,
    REC_Chan_Arp_Time,
    REC_Chan_Clip,
    REC_Chan_Crossfade,
    REC_Chan_Delay_First,
    REC_Chan_Delay_Last,
    REC_Chan_Delay_Time,
    REC_Chan_Env_First,
    REC_Chan_Env_Hole,
    REC_Chan_Env_Last,
    REC_Chan_Env_LFO_First,
    REC_Chan_Env_LFOA,
    REC_Chan_Env_MA,
    REC_Chan_Env_PLast,
    REC_Chan_FCut,
    REC_Chan_FRes,
    REC_Chan_FType,
    REC_Chan_FXTrack,
    REC_Chan_GateTime,
    REC_Chan_Misc,
    REC_Chan_Mute,
    REC_Chan_Note_First,
    REC_Chan_Note_Last,
    REC_Chan_Note_Num,
    REC_Chan_NoteMask,
    REC_Chan_NoteOff,
    REC_Chan_NoteOn,
    REC_Chan_NoteSlide,
    REC_Chan_NoteSlideMask,
    REC_Chan_NoteSlideOfs,
    REC_Chan_NoteSlideTo,
    REC_Chan_OfsFCut,
    REC_Chan_OfsFRes,
    REC_Chan_OfsPan,
    REC_Chan_OfsPitch,
    REC_Chan_OfsVol,
    REC_Chan_Pan,
    REC_Chan_PianoRoll,
    REC_Chan_Pitch,
    REC_Chan_Plugin_First,
    REC_Chan_Plugin_Last,
    REC_Chan_PortaTime,
    REC_Chan_SmpOfs,
    REC_Chan_StretchTime,
    REC_Chan_SwingMix,
    REC_Chan_TimeOfs,
    REC_Chan_Track_First,
    REC_Chan_Track_Last,
    REC_Chan_Track_PLast,
    REC_Chan_Vol,
)
from .global_properties import (
    REC_MainFCut,
    REC_MainFRes,
    REC_MainPitch,
    REC_MainShuffle,
    REC_MainVol,
    REC_Tempo,
)
from .mixer_properties import (
    REC_Mixer_EQ_First,
    REC_Mixer_EQ_Freq,
    REC_Mixer_EQ_Gain,
    REC_Mixer_EQ_Last,
    REC_Mixer_EQ_Q,
    REC_Mixer_EQ_Type,
    REC_Mixer_First,
    REC_Mixer_Last,
    REC_Mixer_Pan,
    REC_Mixer_Send_First,
    REC_Mixer_Send_Last,
    REC_Mixer_SS,
    REC_Mixer_Vol,
    REC_Plug_First,
    REC_Plug_General_First,
    REC_Plug_General_Last,
    REC_Plug_Last,
    REC_Plug_MixLevel,
    REC_Plug_Mute,
    REC_Plug_Plugin_First,
    REC_Plug_Plugin_Last,
)
from .playlist_properties import (
    REC_Pat_Block,
    REC_Pat_Clip,
    REC_Pat_First,
    REC_Pat_Last,
    REC_Playlist,
    REC_Playlist_First,
    REC_Playlist_Last,
    REC_Playlist_Old,
    REC_PLClip_First,
    REC_PLClip_Last,
    REC_PLTrack_First,
    REC_PLTrack_Last,
)
from .process_flags import (
    PME_RECFlagsT,
    REC_AnyInternalCtrl,
    REC_Control,
    REC_Controller,
    REC_FromInternalCtrl,
    REC_FromMIDI,
    REC_FromMixThread,
    REC_GetValue,
    REC_Init,
    REC_InitStore,
    REC_InternalCtrl,
    REC_InvalidID,
    REC_MIDIController,
    REC_NoLastTweaked,
    REC_NoLink,
    REC_None,
    REC_NoSaveUndo,
    REC_PlugCallback,
    REC_PlugReserved,
    REC_SetAll,
    REC_SetChanged,
    REC_SetTouched,
    REC_ShowHint,
    REC_Smoothed,
    REC_SomeGeneric,
    REC_Store,
    REC_UpdateControl,
    REC_UpdatePlugLabel,
    REC_UpdateValue,
    REC_Visual,
    REC_WrapperAfterTouch,
    REC_WrapperModWheel,
)
from .ranges import (
    REC_Chan_First,
    REC_Chan_Last,
    REC_EnvRange,
    REC_Global_First,
    REC_Global_Last,
    REC_GlobalChan,
    REC_GlobalPlug,
    REC_GlobalPlugTrack,
    REC_ItemMask,
    REC_ItemRange,
    REC_MaxChan,
    REC_MaxPat,
    REC_MixerMask,
    REC_PluginBase,
    REC_PluginRange,
    REC_TrackRange,
)
from .special import (
    REC_LastTweakedFirst,
    REC_LastTweakedLast,
    REC_Proj_First,
    REC_Reserved,
    REC_SongLength,
    REC_SongPosition,
    REC_Special,
    REC_StartStop,
)
from .ts404 import (
    REC_Chan_TS404_Env_First,
    REC_Chan_TS404_Env_Last,
    REC_Chan_TS404_FCut,
    REC_Chan_TS404_First,
    REC_Chan_TS404_FRes,
    REC_Chan_TS404_Last,
    REC_Chan_TS404_Valid_First,
    REC_Chan_TS404_Valid_Last,
    REC_TS404Delay_Feed,
    REC_TS404Delay_First,
    REC_TS404Delay_Pan,
    REC_TS404Delay_Time,
    REC_TS404Delay_Vol,
)

__all__ = [
    'REC_ItemRange',
    'REC_TrackRange',
    'REC_EnvRange',
    'REC_PluginBase',
    'REC_PluginRange',
    'REC_ItemMask',
    'REC_MaxChan',
    'REC_MaxPat',
    'REC_GlobalChan',
    'REC_GlobalPlugTrack',
    'REC_GlobalPlug',
    'REC_MixerMask',
    'REC_Chan_First',
    'REC_Chan_Last',
    'REC_Global_First',
    'REC_Global_Last',
    'REC_Chan_Vol',
    'REC_Chan_Pan',
    'REC_Chan_FCut',
    'REC_Chan_FRes',
    'REC_Chan_Pitch',
    'REC_Chan_FType',
    'REC_Chan_PortaTime',
    'REC_Chan_Mute',
    'REC_Chan_FXTrack',
    'REC_Chan_GateTime',
    'REC_Chan_Crossfade',
    'REC_Chan_TimeOfs',
    'REC_Chan_SwingMix',
    'REC_Chan_SmpOfs',
    'REC_Chan_StretchTime',
    'REC_Chan_OfsPan',
    'REC_Chan_OfsVol',
    'REC_Chan_OfsPitch',
    'REC_Chan_OfsFCut',
    'REC_Chan_OfsFRes',
    'REC_Chan_Delay_First',
    'REC_Chan_Delay_Last',
    'REC_Chan_Delay_Time',
    'REC_Chan_Arp_First',
    'REC_Chan_Arp_Last',
    'REC_Chan_Arp_Chord',
    'REC_Chan_Arp_Time',
    'REC_Chan_Arp_Gate',
    'REC_Chan_Arp_Repeat',
    'REC_Chan_Misc',
    'REC_Chan_Track_First',
    'REC_Chan_Track_PLast',
    'REC_Chan_Track_Last',
    'REC_Chan_AC_First',
    'REC_Chan_AC_Last',
    'REC_Chan_Env_First',
    'REC_Chan_Env_LFO_First',
    'REC_Chan_Env_MA',
    'REC_Chan_Env_LFOA',
    'REC_Chan_Env_Hole',
    'REC_Chan_Env_PLast',
    'REC_Chan_Env_Last',
    'REC_Chan_Note_First',
    'REC_Chan_Note_Num',
    'REC_Chan_Note_Last',
    'REC_Chan_NoteOn',
    'REC_Chan_NoteMask',
    'REC_Chan_NoteSlideMask',
    'REC_Chan_NoteSlide',
    'REC_Chan_NoteSlideTo',
    'REC_Chan_NoteSlideOfs',
    'REC_Chan_NoteOff',
    'REC_Chan_PianoRoll',
    'REC_Chan_Clip',
    'REC_Chan_Plugin_First',
    'REC_Chan_Plugin_Last',
    'REC_Chan_TS404_First',
    'REC_Chan_TS404_FCut',
    'REC_Chan_TS404_FRes',
    'REC_Chan_TS404_Env_First',
    'REC_Chan_TS404_Env_Last',
    'REC_Chan_TS404_Last',
    'REC_Chan_TS404_Valid_First',
    'REC_Chan_TS404_Valid_Last',
    'REC_TS404Delay_First',
    'REC_TS404Delay_Feed',
    'REC_TS404Delay_Pan',
    'REC_TS404Delay_Vol',
    'REC_TS404Delay_Time',
    'REC_Plug_First',
    'REC_Plug_Last',
    'REC_Plug_General_First',
    'REC_Plug_General_Last',
    'REC_Plug_Mute',
    'REC_Plug_MixLevel',
    'REC_Mixer_First',
    'REC_Mixer_Last',
    'REC_Mixer_Send_First',
    'REC_Mixer_Send_Last',
    'REC_Mixer_Vol',
    'REC_Mixer_Pan',
    'REC_Mixer_SS',
    'REC_Mixer_EQ_First',
    'REC_Mixer_EQ_Last',
    'REC_Mixer_EQ_Gain',
    'REC_Mixer_EQ_Freq',
    'REC_Mixer_EQ_Q',
    'REC_Mixer_EQ_Type',
    'REC_Plug_Plugin_First',
    'REC_Plug_Plugin_Last',
    'REC_MainVol',
    'REC_MainShuffle',
    'REC_MainPitch',
    'REC_MainFRes',
    'REC_MainFCut',
    'REC_Tempo',
    'REC_Playlist_First',
    'REC_Playlist_Last',
    'REC_Pat_First',
    'REC_Pat_Last',
    'REC_Pat_Clip',
    'REC_PLClip_First',
    'REC_PLClip_Last',
    'REC_Playlist_Old',
    'REC_Pat_Block',
    'REC_Playlist',
    'REC_PLTrack_First',
    'REC_PLTrack_Last',
    'REC_Reserved',
    'REC_Special',
    'REC_StartStop',
    'REC_SongPosition',
    'REC_SongLength',
    'REC_LastTweakedFirst',
    'REC_LastTweakedLast',
    'REC_Proj_First',
    'REC_UpdateValue',
    'REC_GetValue',
    'REC_ShowHint',
    'REC_UpdatePlugLabel',
    'REC_UpdateControl',
    'REC_FromMIDI',
    'REC_Store',
    'REC_SetChanged',
    'REC_SetTouched',
    'REC_Init',
    'REC_NoLink',
    'REC_InternalCtrl',
    'REC_PlugReserved',
    'REC_Smoothed',
    'REC_NoLastTweaked',
    'REC_NoSaveUndo',
    'REC_InitStore',
    'REC_Control',
    'REC_MIDIController',
    'REC_Controller',
    'REC_SetAll',
    'REC_Control',
    'REC_Visual',
    'REC_FromMixThread',
    'REC_PlugCallback',
    'REC_FromInternalCtrl',
    'REC_AnyInternalCtrl',
    'REC_InvalidID',
    'REC_None',
    'REC_SomeGeneric',
    'REC_WrapperModWheel',
    'REC_WrapperAfterTouch',
    'PME_RECFlagsT',
]
