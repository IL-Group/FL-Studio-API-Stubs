"""
These values are provided to {{docs_url_fn[plugins.getName]}} to control the
information that it returns.
"""

FPN_Param = 0
"""
Name of plugin parameter.

* `paramIndex` should be the index of the parameter.

```py
>>> import plugins, midi
>>> plugins.getName(0, flag=midi.FPN_Param, paramIndex=0)
"Expression"
```
"""

FPN_ParamValue = 1
"""
Text value of plugin parameter.

* `paramIndex` should be the index of the parameter.

```py
>>> import plugins, midi
>>> plugins.getName(0, flag=midi.FPN_ParamValue, paramIndex=0)
"42%"
```
"""

FPN_Semitone = 2
"""
Name of note as defined by plugin.

* `paramIndex` should be the note number (eg `60` for middle C)
* If note names aren't defined by the plugin, an empty string is returned, even
  though FL Studio will display the generic note name.

```py
>>> import plugins, midi
>>> plugins.getName(1, flag=midi.FPN_Semitone, paramIndex=42)
"Closed Hat"
```
"""

FPN_Patch = 3
"""
Name of the patch defined by the plugin?
"""

FPN_VoiceLevel = 4
"""
Name of the per-voice parameter defined by the plugin?
"""

FPN_VoiceLevelHint = 5
"""
Hint for per-voice parameter defined by plugin?
"""

FPN_Preset = 6
"""
For plugins that support internal presets, the name of the preset.

* `paramIndex` should be the index of the preset.

```py
>>> import plugins, midi
>>> plugins.getName(1, flag=midi.FPN_Preset, paramIndex=0)
"Breakbeat"
```
"""

FPN_OutCtrl = 7
"""
For plugins that output controllers, the name of the output controller?
"""

FPN_VoiceColor = 8
"""
Name of per-voice color?
"""

FPN_OutVoice = 9
"""
For plugins that output voices, the name of output voice?
"""
