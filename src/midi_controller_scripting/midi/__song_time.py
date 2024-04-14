"""
Song time flags are used by functions such as {{docs_url_fn[transport.getSongPos]}}
to determine the units to use when referring to time within a song or pattern.

```py
import transport
import midi

total_time_ms = transport.getSongLength(midi.SONGLENGTH_MS)  # 63175
total_time_s = total_time_s // 1000

time_ms = total_time_ms % 1000
time_s = total_time_s % 60
time_mins = total_time_s // 60

print(f"Song position: {time_mins}:{time_s:02}.{time_ms:03}")
#       Song position: 1:02.175
```
"""

SONGLENGTH_MS = 0
"""
Use milliseconds (ms) as time unit.
"""

SONGLENGTH_S = 1
"""
Use seconds (s) as time unit.
"""

SONGLENGTH_ABSTICKS = 2
"""
Use absolute number of ticks as time unit.

This is the number of ticks since the start of the song (`0`), as opposed to
`SONGLENGTH_TICKS` which is the number of ticks since the last step.

A tick is the smallest time division supported by MIDI within FL Studio, and is
derived by the {{fl_manual_page("songsettings_settings.htm#project_timebase", "timebase (PPQ)")}}.
"""

SONGLENGTH_BARS = 3
"""
Use number of bars as time unit. Bars are 1-indexed.

This unit cannot be used in `transport.setSongPos`.
"""

SONGLENGTH_STEPS = 4
"""
Use number of steps since start of current bar as time unit.

A step is the subdivision of a bar used by the step sequencer, which is a 16th
note by default.

This unit cannot be used in `transport.setSongPos`.
"""

SONGLENGTH_TICKS = 5
"""
Use number of ticks since start of current step as time unit.

This unit cannot be used in `transport.setSongPos`.

A tick is the smallest time division supported by MIDI within FL Studio, and is
derived by the {{fl_manual_page("songsettings_settings.htm#project_timebase", "timebase (PPQ)")}}.
"""
