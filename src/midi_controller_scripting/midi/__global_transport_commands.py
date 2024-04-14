"""
Global transport commands are given as an argument to
{{docs_url_fn[transport.globalTransport]}}.

These commands begin with `FPT_`.
"""

FPT_Jog = 0
"""
Jog wheel, controlling selection.
"""
FPT_Jog2 = 1
"""
Alternate jog wheel, moving items.
"""

FPT_Strip = 2
"""
Touch-sensitive jog strip.

Value will be in range `-midi.FromMIDI_Max` to `midi.FromMIDI_Max` for leftmost
to rightmost.
"""
FPT_StripJog = 3
"""
Touch-sensitive jog string in jog mode.
"""
FPT_StripHold = 4
"""
Value will be `0` for release, `1,2` for 1,2 fingers centered mode, `-1,-2`
for 1,2 fingers jog mode (will then send `FPT_StripJog`).
"""

FPT_Previous = 5
"""
Previous button. Usually selects previous item.
"""
FPT_Next = 6
"""
Next button. Usually selects next item.
"""
FPT_PreviousNext = 7
"""
Jog, controlling track selection.
"""
FPT_MoveJog = 8
"""
Jog, moving items.
"""

FPT_Play = 10
"""
Play/pause button.
"""
FPT_Stop = 11
"""
Stop button.
"""
FPT_Record = 12
"""
Record button.
"""
FPT_Rewind = 13
"""
Rewind button.

Use {{docs_url_attr[midi.SS_Start]}} to begin rewind, and
{{docs_url_attr[midi.SS_Stop]}} to stop rewind.
"""
FPT_FastForward = 14
"""
Fast-forward button.

Use {{docs_url_attr[midi.SS_Start]}} to begin fast-forward, and
{{docs_url_attr[midi.SS_Stop]}} to stop fast-forward.
"""

FPT_Loop = 15
"""
Change loop mode.
"""

FPT_Mute = 16
"""
Mute button???
"""

FPT_Mode = 17
"""
Generic/record mode???
"""

FPT_Undo = 20
"""
Undo/redo button.
"""

FPT_UndoUp = 21
"""
Move up in undo history.
"""

FPT_UndoJog = 22
"""
Jog through undo history.
"""

FPT_Punch = 30
"""
(hold) live selection.
"""
FPT_PunchIn = 31
"""
Button.
"""
FPT_PunchOut = 32
"""
Button.
"""

FPT_AddMarker = 33
"""
Button.
"""
FPT_AddAltMarker = 34
"""
Button.
"""
FPT_MarkerJumpJog = 35
"""
Jump between markers.
"""
FPT_MarkerSelJog = 36
"""
Jump between markers, selecting their contents.
"""

FPT_Up = 40
"""
Navigate upwards (up arrow key).
"""
FPT_Down = 41
"""
Navigate downwards (down arrow key).
"""
FPT_Left = 42
"""
Navigate left (left arrow key).
"""
FPT_Right = 43
"""
Navigate right (right arrow key).
"""

FPT_HZoomJog = 44
"""
Change horizontal zoom level in active window, or modify font size in browser.
"""

FPT_VZoomJog = 45
"""
Change vertical zoom level in active window, or modify font size in browser.
"""

FPT_Snap = 48
"""
Enable/disable snapping.
"""

FPT_SnapMode = 49
"""
Control the snap mode.
"""

FPT_Cut = 50
"""
Cut selection (like Ctrl+X).
"""
FPT_Copy = 51
"""
Copy selection (like Ctrl+C).
"""
FPT_Paste = 52
"""
Paste selection (like Ctrl+V).
"""
FPT_Insert = 53
"""
Insert key.
"""
FPT_Delete = 54
"""
Delete key.
"""
FPT_NextWindow = 58
"""
Switch to next FL Studio window (like Tab key).
"""
FPT_WindowJog = 59
"""
Window selection.
"""

FPT_F1 = 60
"""
F1 key.
"""
FPT_F2 = 61
"""
F2 key.
"""
FPT_F3 = 62
"""
F3 key.
"""
FPT_F4 = 63
"""
F4 key.
"""
FPT_F5 = 64
"""
F5 key.
"""
FPT_F6 = 65
"""
F6 key.
"""
FPT_F7 = 66
"""
F7 key.
"""
FPT_F8 = 67
"""
F8 key.
"""
FPT_F9 = 68
"""
F9 key.
"""
FPT_F10 = 69
"""
F10 key.
"""
FPT_F11 = 70
"""
F11 key.
"""
FPT_F12 = 71
"""
F12 key.
"""

FPT_Enter = 80
"""
Enter key.
"""
FPT_Escape = 81
"""
Escape key.
"""
FPT_Yes = 82
"""
`'y'` key.
"""
FPT_No = 83
"""
`'n'` key.
"""

FPT_Menu = 90
"""
Open generic menu.
"""
FPT_ItemMenu = 91
"""
Open item edit/tool/context menu.
"""

FPT_Save = 92
"""
Save project.
"""
FPT_SaveNew = 93
"""
Save new version of project.
"""

FPT_PatternJog = 100
"""
Jog through pattern selection.
"""
FPT_TrackJog = 101
"""
Jog through track selection.
"""
FPT_ChannelJog = 102
"""
Jog through channel selection.
"""

FPT_TempoJog = 105
"""
Jog tempo control.
"""
FPT_TapTempo = 106
"""
Tap tempo button.
"""
FPT_NudgeMinus = 107
"""
Nudge tempo down.
"""
FPT_NudgePlus = 108
"""
Nudge tempo up.
"""

FPT_Metronome = 110
"""
Enable/disable metronome.
"""
FPT_WaitForInput = 111
"""
Wait for input to start playing.
"""
FPT_Overdub = 112
"""
Enable/disable overdub recording.
"""
FPT_LoopRecord = 113
"""
Enable/disable loop recording.
"""
FPT_StepEdit = 114
"""
Enable/disable step edit mode.
"""
FPT_CountDown = 115
"""
Enable/disable count-down before recording.
"""

FPT_NextMixerWindow = 120
"""
Tab between windows of FX plugins in the current mixer track.
"""
FPT_MixerWindowJog = 121
"""
Jog through windows of FX plugins in the current mixer track.
"""

FPT_ShuffleJog = 122
"""
Control main swing.
"""

FPT_ArrangementJog = 123
"""
Jog through arrangements?
"""

# Global transport return values.
