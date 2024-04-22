"""
Song tick modes are passed to {{docs_url_fn[mixer.getSongTickPos]}} to
determine its behavior.
"""

ST_Int = 0
"""
Return the location within the song, measured in ticks.

This causes the return type to be `int`.
"""

ST_Beat = 1
"""
Return the fraction of a beat since the last beat. For example, if the playhead
is an 8th note past the previous beat, this will return `0.5`.
"""

ST_PGB = 2
"""
Return the fraction of a bar since the last bar. For example, if the playhead
is at 2 beats past the previous bar and the time signature is 4/4, this will
return `0.5`.
"""
