"""
{{module_title[midi]}}

The `midi` modules contains helpful constants, which are often used as flags
when interacting with the FL Studio API.

## Table of contents

* {{docs_url_page("Miscellaneous", "midi_controller_scripting/midi/miscellaneous")}}:
  miscellaneous constants and functions.

* {{docs_url_page("REC events", "midi_controller_scripting/midi/__rec_events")}}:
  constants used for creating and processing REC events.

* {{docs_url_page("MIDI codes", "midi_controller_scripting/midi/midi codes")}}:
  constants useful for handling MIDI events.

* {{docs_url_page("`OnRefresh` flags", "midi_controller_scripting/midi/on refresh flags")}}:
  constants used by the `OnRefresh` callback.

* {{docs_url_page("PME flags", "midi_controller_scripting/midi/pme flags")}}:
  flags used when processing MIDI events to determine
  the availability of various features in FL Studio.

* {{docs_url_page("`triggerLiveClip` flags", "midi_controller_scripting/midi/tlc flags")}}:
  flags passed to the {{docs_url_fn[playlist.triggerLiveClip]}} function.

* {{docs_url_page("`globalTransport` commands", "midi_controller_scripting/midi/gt commands")}}:
  command flags passed to {{docs_url_fn[transport.globalTransport]}}.

* {{docs_url_page("`globalTransport` flags", "midi_controller_scripting/midi/gt flags")}}:
  response flags returned by {{docs_url_fn[transport.globalTransport]}}.

* {{docs_url_page("`mixer.setTrackNumber` flags", "midi_controller_scripting/midi/mixer setTrackNumber flags")}}:
  flags passed to {{docs_url_fn[mixer.setTrackNumber]}} to control selection
  behavior.

* {{docs_url_page("Linked event flags", "midi_controller_scripting/midi/linked event flags")}}:
  response flags returned by {{docs_url_fn[device.getLinkedInfo]}}.

* {{docs_url_page("`mixer.soloTrack` flags", "midi_controller_scripting/midi/mixer solo flags")}}:
  flags passed to {{docs_url_fn[mixer.soloTrack]}} to control solo behavior.

* {{docs_url_page("Overlay flags", "midi_controller_scripting/midi/overlay flags")}}:
  flags passed to UI overlay functions.

* {{docs_url_page("Pickup modes", "midi_controller_scripting/midi/pickup modes")}}:
  flags used to control pickup modes in various functions.

* {{docs_url_page("Play modes", "midi_controller_scripting/midi/play modes")}}:
  ??? undocumented

* {{docs_url_page("Song time flags", "midi_controller_scripting/midi/song time")}}:
  flags used to access particular units of time when getting/setting
  time-related properties.

* {{docs_url_page("Window indexes", "midi_controller_scripting/midi/window indexes")}}:
  index numbers used to refer to primary windows within FL Studio.
"""
# flake8: noqa

from .__miscellaneous import (
    EncodeRemoteControlID,
    MaxInt,
    GPN_GetCurrentPreset,
    TranzPort_OffOnT,
    TranzPort_OffBlinkT,
    TranzPort_OffOnBlinkT,
    FromMIDI_Max,
    FromMIDI_Half,
    EKRes,
    TrackNum_Master,
    SM_Pat,
    SM_Song,
    MiddleNote_Default,
    FineTune_Default,
    DotVol_Default,
    DotPan_Default,
    DotVol_Max,
    DotNote_Default,
)

from .__midi_codes import (
    MIDI_NOTEON,
    MIDI_NOTEOFF,
    MIDI_KEYAFTERTOUCH,
    MIDI_CONTROLCHANGE,
    MIDI_PROGRAMCHANGE,
    MIDI_CHANAFTERTOUCH,
    MIDI_PITCHBEND,
    MIDI_SYSTEMMESSAGE,
    MIDI_BEGINSYSEX,
    MIDI_MTCQUARTERFRAME,
    MIDI_SONGPOSPTR,
    MIDI_SONGSELECT,
    MIDI_ENDSYSEX,
    MIDI_TIMINGCLOCK,
    MIDI_START,
    MIDI_CONTINUE,
    MIDI_STOP,
    MIDI_ACTIVESENSING,
    MIDI_SYSTEMRESET,
    EventNameT,
)

from .__pme_flags import (
    PME_LiveInput,
    PME_System,
    PME_System_Safe,
    PME_PreviewNote,
    PME_FromHost,
    PME_FromMIDI,
    PME_FromScript,
)

from .__overlay_flags import (
    # crDisplayRect flags
    CR_HighlightChannels,
    CR_ScrollToView,
    CR_HighlightChannelMute,
    CR_HighlightChannelPanVol,
    CR_HighlightChannelTrack,
    CR_HighlightChannelName,
    CR_HighlightChannelSelect,
    # miDisplayRect flags
    MI_ScrollToView,
)


from .__tlc_flags import (
    TLC_MuteOthers,
    TLC_Fill,
    TLC_Queue,
    TLC_Release,
    TLC_NoPlayCheck,
    TLC_NoHardwareUpdate,
    TLC_SecondPass,
    TLC_ColumnMode,
    TLC_WeakColumnMode,
    TLC_TriggerCheckColumnMode,
    TLC_TrackSnap,
    TLC_GlobalSnap,
    TLC_NoSnap,
    TLC_SubNum_Normal,
    TLC_SubNum_ClipPos,
    TLC_SubNum_GroupNum,
    TLC_SubNum_Read,
    TLC_SubNum_Leave,
)

from .__play_modes import (
    PM_Stopped,
    PM_Playing,
    PM_Precount,
)

from .__on_refresh_flags import (
    HW_Dirty_Mixer_Sel,
    HW_Dirty_Mixer_Display,
    HW_Dirty_Mixer_Controls,
    HW_Dirty_RemoteLinks,
    HW_Dirty_FocusedWindow,
    HW_Dirty_Performance,
    HW_Dirty_LEDs,
    HW_Dirty_RemoteLinkValues,
    HW_Dirty_Patterns,
    HW_Dirty_Tracks,
    HW_Dirty_ControlValues,
    HW_Dirty_Colors,
    HW_Dirty_Names,
    HW_Dirty_ChannelRackGroup,
    HW_ChannelEvent,
)

from .__song_time import (
    SONGLENGTH_MS,
    SONGLENGTH_S,
    SONGLENGTH_ABSTICKS,
    SONGLENGTH_BARS,
    SONGLENGTH_STEPS,
    SONGLENGTH_TICKS,
)

from .__linked_event_flags import (
    Event_CantInterpolate,
    Event_Float,
    Event_Centered,
)

from .__rec_events import (
    REC_ItemRange,
    REC_TrackRange,
    REC_EnvRange,
    REC_PluginBase,
    REC_PluginRange,
    REC_ItemMask,
    REC_MaxChan,
    REC_MaxPat,
    REC_GlobalChan,
    REC_GlobalPlugTrack,
    REC_GlobalPlug,
    REC_MixerMask,
    REC_Chan_First,
    REC_Chan_Last,
    REC_Global_First,
    REC_Global_Last,
    REC_Chan_Vol,
    REC_Chan_Pan,
    REC_Chan_FCut,
    REC_Chan_FRes,
    REC_Chan_Pitch,
    REC_Chan_FType,
    REC_Chan_PortaTime,
    REC_Chan_Mute,
    REC_Chan_FXTrack,
    REC_Chan_GateTime,
    REC_Chan_Crossfade,
    REC_Chan_TimeOfs,
    REC_Chan_SwingMix,
    REC_Chan_SmpOfs,
    REC_Chan_StretchTime,
    REC_Chan_OfsPan,
    REC_Chan_OfsVol,
    REC_Chan_OfsPitch,
    REC_Chan_OfsFCut,
    REC_Chan_OfsFRes,
    REC_Chan_TS404_First,
    REC_Chan_TS404_FCut,
    REC_Chan_TS404_FRes,
    REC_Chan_TS404_Env_First,
    REC_Chan_TS404_Env_Last,
    REC_Chan_TS404_Last,
    REC_Chan_TS404_Valid_First,
    REC_Chan_TS404_Valid_Last,
    REC_TS404Delay_First,
    REC_TS404Delay_Feed,
    REC_TS404Delay_Pan,
    REC_TS404Delay_Vol,
    REC_TS404Delay_Time,
    REC_Chan_Delay_First,
    REC_Chan_Delay_Last,
    REC_Chan_Delay_Time,
    REC_Chan_Arp_First,
    REC_Chan_Arp_Last,
    REC_Chan_Arp_Chord,
    REC_Chan_Arp_Time,
    REC_Chan_Arp_Gate,
    REC_Chan_Arp_Repeat,
    REC_Chan_Misc,
    REC_Chan_Track_First,
    REC_Chan_Track_PLast,
    REC_Chan_Track_Last,
    REC_Chan_AC_First,
    REC_Chan_AC_Last,
    REC_Chan_Env_First,
    REC_Chan_Env_LFO_First,
    REC_Chan_Env_MA,
    REC_Chan_Env_LFOA,
    REC_Chan_Env_Hole,
    REC_Chan_Env_PLast,
    REC_Chan_Env_Last,
    REC_Chan_Note_First,
    REC_Chan_Note_Num,
    REC_Chan_Note_Last,
    REC_Chan_NoteOn,
    REC_Chan_NoteMask,
    REC_Chan_NoteSlideMask,
    REC_Chan_NoteSlide,
    REC_Chan_NoteSlideTo,
    REC_Chan_NoteSlideOfs,
    REC_Chan_NoteOff,
    REC_Chan_PianoRoll,
    REC_Chan_Clip,
    REC_Chan_Plugin_First,
    REC_Chan_Plugin_Last,
    REC_MainVol,
    REC_MainShuffle,
    REC_MainPitch,
    REC_MainFRes,
    REC_MainFCut,
    REC_Tempo,
    REC_Playlist_First,
    REC_Playlist_Last,
    REC_Pat_First,
    REC_Pat_Last,
    REC_Pat_Clip,
    REC_PLClip_First,
    REC_PLClip_Last,
    REC_Playlist_Old,
    REC_Pat_Block,
    REC_Playlist,
    REC_PLTrack_First,
    REC_PLTrack_Last,
    REC_Reserved,
    REC_Special,
    REC_StartStop,
    REC_SongPosition,
    REC_SongLength,
    REC_LastTweakedFirst,
    REC_LastTweakedLast,
    REC_Proj_First,
    REC_UpdateValue,
    REC_GetValue,
    REC_ShowHint,
    REC_UpdatePlugLabel,
    REC_UpdateControl,
    REC_FromMIDI,
    REC_Store,
    REC_SetChanged,
    REC_SetTouched,
    REC_Init,
    REC_NoLink,
    REC_InternalCtrl,
    REC_PlugReserved,
    REC_Smoothed,
    REC_NoLastTweaked,
    REC_NoSaveUndo,
    REC_InitStore,
    REC_Control,
    REC_MIDIController,
    REC_Controller,
    REC_SetAll,
    REC_Control,
    REC_Visual,
    REC_FromMixThread,
    REC_PlugCallback,
    REC_FromInternalCtrl,
    REC_AnyInternalCtrl,
    REC_InvalidID,
    REC_None,
    REC_SomeGeneric,
    REC_WrapperModWheel,
    REC_WrapperAfterTouch,
    PME_RECFlagsT,
)

# Global transport commnads
from .__gt_commands import (
    FPT_Jog,
    FPT_Jog2,
    FPT_Strip,
    FPT_StripJog,
    FPT_StripHold,
    FPT_Previous,
    FPT_Next,
    FPT_PreviousNext,
    FPT_MoveJog,
    FPT_Play,
    FPT_Stop,
    FPT_Record,
    FPT_Rewind,
    FPT_FastForward,
    FPT_Loop,
    FPT_Mute,
    FPT_Mode,
    FPT_Undo,
    FPT_UndoUp,
    FPT_UndoJog,
    FPT_Punch,
    FPT_PunchIn,
    FPT_PunchOut,
    FPT_AddMarker,
    FPT_AddAltMarker,
    FPT_MarkerJumpJog,
    FPT_MarkerSelJog,
    FPT_Up,
    FPT_Down,
    FPT_Left,
    FPT_Right,
    FPT_HZoomJog,
    FPT_VZoomJog,
    FPT_Snap,
    FPT_SnapMode,
    FPT_Cut,
    FPT_Copy,
    FPT_Paste,
    FPT_Insert,
    FPT_Delete,
    FPT_NextWindow,
    FPT_WindowJog,
    FPT_F1,
    FPT_F2,
    FPT_F3,
    FPT_F4,
    FPT_F5,
    FPT_F6,
    FPT_F7,
    FPT_F8,
    FPT_F9,
    FPT_F10,
    FPT_F11,
    FPT_F12,
    FPT_Enter,
    FPT_Escape,
    FPT_Yes,
    FPT_No,
    FPT_Menu,
    FPT_ItemMenu,
    FPT_Save,
    FPT_SaveNew,
    FPT_PatternJog,
    FPT_TrackJog,
    FPT_ChannelJog,
    FPT_TempoJog,
    FPT_TapTempo,
    FPT_NudgeMinus,
    FPT_NudgePlus,
    FPT_Metronome,
    FPT_WaitForInput,
    FPT_Overdub,
    FPT_LoopRecord,
    FPT_StepEdit,
    FPT_CountDown,
    FPT_NextMixerWindow,
    FPT_MixerWindowJog,
    FPT_ShuffleJog,
    FPT_ArrangementJog,
)
from .__gt_flags import (
    GT_Cannot,
    GT_None,
    GT_Plugin,
    GT_Form,
    GT_Menu,
    GT_Global,
    GT_All,
)

from .__pickup_modes import (
    PIM_None,
    PIM_AlwaysPickup,
    PIM_FollowGlobal,
)


# show ui
from .__window_indexes import (
    widMixer,
    widChannelRack,
    widPlaylist,
    widPianoRoll,
    widBrowser,
    widPluginEffect,
    widPluginGenerator,
)

from .__mixer_setTrackNumber_flags import (
    curfxScrollToMakeVisible,
    StartcurfxCancelSmoothing,
    curfxNoDeselectAll,
    curfxMinimalLatencyUpdate,
)

from .__mixer_solo_flags import (
    fxSoloModeWithSourceTracks,
    fxSoloModeWithDestTracks,
    fxSoloModeIgnorePrevious,
    fxSoloSetOff,
    fxSoloSetOn,
    fxSoloToggle,
    fxSoloGetValue,
)

from .__mixer_peaks_mode import (
    PEAK_L,
    PEAK_R,
    PEAK_LR,
    PEAK_LR_INV,
)

from .__mixer_link_channel_mode import (
    ROUTE_ToThis,
    ROUTE_StartingFromThis,
)

from .__scale_indexes import (
    HARMONICSCALE_MAJOR,
    HARMONICSCALE_HARMONICMINOR,
    HARMONICSCALE_MELODICMINOR,
    HARMONICSCALE_WHOLETONE,
    HARMONICSCALE_DIMINISHED,
    HARMONICSCALE_MAJORPENTATONIC,
    HARMONICSCALE_MINORPENTATONIC,
    HARMONICSCALE_JAPINSEN,
    HARMONICSCALE_MAJORBEBOP,
    HARMONICSCALE_DOMINANTBEBOP,
    HARMONICSCALE_BLUES,
    HARMONICSCALE_ARABIC,
    HARMONICSCALE_ENIGMATIC,
    HARMONICSCALE_NEAPOLITAN,
    HARMONICSCALE_NEAPOLITANMINOR,
    HARMONICSCALE_HUNGARIANMINOR,
    HARMONICSCALE_DORIAN,
    HARMONICSCALE_PHRYGIAN,
    HARMONICSCALE_LYDIAN,
    HARMONICSCALE_MIXOLYDIAN,
    HARMONICSCALE_AEOLIAN,
    HARMONICSCALE_LOCRIAN,
    HARMONICSCALE_CHROMATIC,
    HARMONICSCALE_LAST,
)

from .__ffnep_flags import (
    FFNEP_FindFirst,
    FFNEP_DontPromptName,
)

from .__step_params import (
    pPitch,
    pVelocity,
    pRelease,
    pFinePitch,
    pPan,
    pModX,
    pModY,
    pShift,
)

from .__channel_types import (
    CT_Sampler,
    CT_Hybrid,
    CT_TS404,
    CT_GenPlug,
    CT_Layer,
    CT_AudioClip,
    CT_AutoClip,
    CT_ColorT,
)

from .__event_editor_modes import (
    EE_EE,
    EE_PR,
    EE_PL,
)

from .__snap_modes import (
    Snap_Default,
    Snap_Line,
    Snap_Cell,
    Snap_None,
    Snap_SixthStep,
    Snap_FourthStep,
    Snap_ThirdStep,
    Snap_HalfStep,
    Snap_Step,
    Snap_SixthBeat,
    Snap_FourthBeat,
    Snap_ThirdBeat,
    Snap_HalfBeat,
    Snap_Beat,
    Snap_SixthBar,
    Snap_FourthBar,
    Snap_ThirdBar,
    Snap_HalfBar,
    Snap_Bar,
    Snap_Events,
    Snap_Markers,
    Snap_ForceCell,
    Snap_AltNone,
    Snap_FlagsMask,
)

from .__track_info_flags import (
    TN_Master,
    TN_FirstIns,
    TN_LastIns,
    TN_Sel,
)

from .__undo_flags import (
    UF_None,
    UF_EE,
    UF_PR,
    UF_PL,
    UF_EEPR,
    UF_Knob,
    UF_SS,
    UF_AudioRec,
    UF_AutoClip,
    UF_PRMarker,
    UF_PLMarker,
    UF_Plugin,
    UF_SSLooping,
)

from .__cc_flags import (
    CC_Normal,
    CC_Special,
    CC_PitchBend,
    CC_KeyAfterTouch,
    CC_ChanAfterTouch,
    CC_Note,
    CC_Free,
    CC_PLTrack,
)

from .__song_tick_modes import (
    ST_Int,
    ST_Beat,
    ST_PGB,
)

from .__live_block_status import (
    LB_Status_Default,
    LB_Status_Simple,
    LB_Status_Simplest,
)

# channel looping settings for a given pattern (see TChannelLoopInfo)
ssLoopOff = 0
ssLoopNextStep = -1
ssLoopNextBeat = -2
ssLoopNextBar = -3

# FPD_GetColor flags
GC_BackgroundColor = 0
GC_Semitone = 1

# GetVersion flags
VER_Major = 0
VER_Minor = 1
VER_Release = 2
VER_Build = 3
VER_VersionAndEdition = 4
VER_FullVersionAndEdition = 5
VER_ArchAndBuild = 6

# GetParamName flags
FPN_Param = 0
FPN_ParamValue = 1
FPN_Semitone = 2
FPN_Patch = 3
FPN_VoiceLevel = 4
FPN_VoiceLevelHint = 5
FPN_Preset = 6
FPN_OutCtrl = 7
FPN_VoiceColor = 8
FPN_OutVoice = 9

# OnProjectLoad status
PL_Start = 0
PL_LoadOk = 100
PL_LoadError = 101

# OnDirtyChannelFlag flags
CE_New = 0
CE_Delete = 1
CE_Replace = 2
CE_Rename = 3
CE_Select = 4


ChannelDefaultVolume = 1000 / 1280
TackDefaultVolume = 800 / 1000
