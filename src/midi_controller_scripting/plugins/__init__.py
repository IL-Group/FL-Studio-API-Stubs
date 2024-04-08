"""
{{module_title[plugins]}}

FL Studio built-in module.

Handles the way that scripts communicate with and control FL Studio plugins,
including 3rd-party VST/AU plugins. The module allows scripts to get and set
parameter values for plugins on the mixer and the channel rack.

## Working with indexes

Almost all of the functions in this module accept an `index` and a `slotIndex`
parameter, which are used to determine which plugin to interact with.

* `index` either refers to the index of the plugin on the channel rack, or the
  index of the mixer track containing the plugin on the mixer. Note that the
  grouped index is used, rather than a global index on the channel rack.

* `slotIndex` refers the the mixer slot of the plugin if it is on the mixer.
  Leave this parameter unset, or set it to `-1` if the plugin is on the channel
  rack.

Tuple packing and unpacking can be used to simplify this process if your
script uses these variables a lot.

```py
# A plugin on channel 42
index1 = (42,)
# A plugin on mixer track 12, in slot 5
index2 = (12, 5)

# If you use the unary `*` operator, the tuple is unpacked to take up multiple
# arguments. Both of these function calls work correctly.
plugins.isValid(*index1)
plugins.isValid(*index2)
```

Note that this may be unreliable if you are also specifying `useGlobalIndex`.

## Interacting with VST plugins

VST plugins can behave somewhat unintuitively as a result of the system that FL
Studio uses for parameter mapping. In the VST specification, all VSTs have 4096
parameters available to use, but aren't required to use all of them. Unused
parameters are hidden in FL Studio's UI, but they are accessible through the
API - their returned names will be an empty string. However, there are actually
144 more parameters available. These are the 128 CC parameters from indexes
4096-4223 and the 16 channel after-touch parameters from indexes 4224-4239.

Module added in API version 8.
"""
from .__plugins import (
    isValid,
    getPluginName,
    getParamCount,
    getParamName,
    getParamValue,
    setParamValue,
    getParamValueString,
    getColor,
    getName,
    getPadInfo,
    getPresetCount,
    nextPreset,
    prevPreset,
)


__all__ = [
    "isValid",
    "getPluginName",
    "getParamCount",
    "getParamName",
    "getParamValue",
    "setParamValue",
    "getParamValueString",
    "getColor",
    "getName",
    "getPadInfo",
    "getPresetCount",
    "nextPreset",
    "prevPreset",
]
