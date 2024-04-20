"""
Process flags are used to specify how a Rec event should be processed.

You can either combine base flags using the bitwise or operator (`|`), or use
the preset combinations, which are also defined.
"""
from ..__miscellaneous import MaxInt

REC_UpdateValue = 1 << 0
"""
Update the value associated with the event ID.
"""

REC_GetValue = 1 << 1
"""
Return the value associated with the event ID.
"""

REC_ShowHint = 1 << 2
"""
Update the hint message to indicate the meaning of the event ID.
"""

REC_UpdatePlugLabel = 1 << 3
"""
Update the label for the parameter.
"""

REC_UpdateControl = 1 << 4
"""
Update the wheel/knob associated with the parameter. Without this, any changes
won't be shown in FL Studio's UI.
"""

REC_FromMIDI = 1 << 5
"""
The given value is in the range `0` to `midi.FromMIDI_Max`. If this flag is
specified, then FL Studio automatically converts the value into the required
range for the parameter.
"""

REC_Store = 1 << 6
"""
Store the value when recording automation.
"""

REC_SetChanged = 1 << 7
"""
Set the changed flag. If this is set, FL Studio will remind the user to save
changes before closing the project.
"""

REC_SetTouched = 1 << 8
"""
Set as touched event???
"""

REC_Init = 1 << 9
"""
Make sure to initialise the parameter with the previous value before storing
the updated value (meaning automation recording starts from the previous value,
not this one).
"""

REC_NoLink = 1 << 10
"""
Don't check if wheels are linked.
"""

REC_InternalCtrl = 1 << 11
"""
Event was sent by an internal controller.
"""

REC_PlugReserved = 1 << 12
"""
This flag is free to use by plugins.
"""

REC_Smoothed = 1 << 13
"""
Smoothed up controller, almost same as internal controller???
"""

REC_NoLastTweaked = 1 << 14
"""
Don't save this parameter as the last-tweaked parameter.
"""

REC_NoSaveUndo = 1 << 15
"""
Don't save an entry in the undo history.
"""

# Combination flags

REC_InitStore = REC_Init | REC_Store
"""
Used for control automation recording. Initialize control with the previous
value then store this value.
"""

REC_Control = REC_UpdateValue | REC_UpdateControl | REC_ShowHint | REC_InitStore | REC_SetChanged | REC_SetTouched
"""
Used for changing values from a MIDI controller, but where the value is already
in the right units.
"""

REC_MIDIController = REC_Control | REC_FromMIDI
"""
Used for changing values from a MIDI controller, but where the value has been
given within the range of `0` to `midi.FromMIDI_Max`. FL Studio will translate
the value into the correct units before storing it.
"""

REC_Controller = REC_Control
"""
Used for changing values from a MIDI controller, but where the value is already
in the right units.

For compatibility only, wrong name used.
"""

# called externally
REC_SetAll = REC_UpdateValue | REC_UpdateControl | REC_InitStore | REC_SetChanged | REC_SetTouched
# called by the param's control
REC_Control = REC_UpdateValue | REC_ShowHint | REC_InitStore | REC_SetChanged | REC_UpdatePlugLabel | REC_SetTouched
"""
Used for changing values from a MIDI controller, but where the value is already
in the right units. Note that this is missing `REC_UpdateControl`, so changes
using this flag won't be reflected in the UI.
"""

REC_Visual = REC_GetValue | REC_UpdateControl | REC_UpdatePlugLabel  # refresh visually
REC_FromMixThread = REC_UpdateValue  # change the value only
REC_PlugCallback = REC_InitStore | REC_SetChanged | REC_SetTouched
# let's not prevent automation & internal controllers at the same time
REC_FromInternalCtrl = REC_UpdateValue | REC_FromMIDI | REC_InternalCtrl
REC_AnyInternalCtrl = REC_InternalCtrl | REC_Smoothed

REC_InvalidID = MaxInt
"""
ProcessRECEvent returns this when the ID is invalid.
"""

REC_None = MaxInt
"""
used when filtering events that have no IDs.
"""

REC_SomeGeneric = REC_None - 1
"""
Remote_FindEventID returns this when a generic link could be found, but it's
not related to the focused window.
"""

REC_WrapperModWheel = 0x0FFF9001
"""
Default mod-wheel mapping for the wrapper (to support mod wheel in VSTs).
"""

REC_WrapperAfterTouch = 0x0FFF9080
"""
Default aftertouch mapping for the wrapper (to support mod aftertouch in VSTs).
"""


PME_RECFlagsT = [
    (REC_UpdateValue
        | REC_UpdateControl
        | REC_FromMIDI
        | REC_SetChanged
        | REC_SetTouched),
    REC_MIDIController,
]
"""
Recording flags for ProcessMIDIEvent.
"""
