"""
These constants are used with {{docs_url_fn[playlist.getLiveStatus]}} and
{{docs_url_fn[playlist.getLiveBlockStatus]}} to represent the status of a track
in {{docs_url_page("performance mode", "midi_controller_scripting/tutorials/performance_mode")}}.
"""

LB_Status_Default = 0
"""
The default status.

{{md_table([
    ["Return value", "Meaning"],
    ["1", "Filled"],
    ["2", "Scheduled"],
    ["4", "Playing"]
])}}
"""

LB_Status_Simple = 1
"""
Simpler status.

## For {{docs_url_fn[playlist.getLiveStatus]}}:

{{md_table([
    ["Return value", "Meaning"],
    ["0", "Empty"],
    ["1", "Filled"],
    ["2", "None playing (or scheduled)"],
    ["4", "None scheduled (and not playing)"]
])}}

## For {{docs_url_fn[playlist.getLiveBlockStatus]}}:

{{md_table([
    ["Return value", "Meaning"],
    ["0", "Empty"],
    ["1", "Filled"],
    ["2", "Playing (or scheduled)"],
    ["4", "Scheduled (and not playing)"]
])}}
"""

LB_Status_Simplest = 2
"""
Simplest status.

This flag can only be used with {{docs_url_fn[playlist.getLiveBlockStatus]}}.

{{md_table([
    ["Return value", "Meaning"],
    ["0", "Empty"],
    ["1", "Filled"],
    ["2", "Playing or scheduled"],
])}}
"""
