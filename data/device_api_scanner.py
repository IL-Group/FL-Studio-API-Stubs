# name=API Scanner
"""
# FL Studio API Scanner

A simple function script to allow for determining the difference between
functions available in FL Studio vs the stubs.

Eventually we should use Flapi to do this this, but it is not currently stable
enough and often crashes FL Studio.

## Usage

1. Create a virtual MIDI port
2. Put this script into your scripts folder
3. Make it attach to the virtual MIDI port in FL Studio
4. In the script output, run `generate()` which will produce a bunch of JSON
output.
5. Copy that into `data/fl_stubs.json`
6. Run `python -m scripts.check_stubs_against_fl_studio` which will show any
   missing functions.

## Authors

* Miguel Guthridge (hello@miguelguthridge.com)
"""
import arrangement
import channels
import device
import general
import launchMapPages
import mixer
import patterns
import playlist
import plugins
import screen
import transport
import ui
# import utils

import json


modules = [
    arrangement,
    channels,
    device,
    general,
    launchMapPages,
    mixer,
    patterns,
    playlist,
    plugins,
    screen,
    transport,
    ui,
    # utils,
]

ignored_types = [
    int,
    str,
    float,
]


def _do_generate_recurse(obj):
    """
    Recursively generate a dictionary showing the names of everything
    """
    ret = {}
    for ele in dir(obj):
        if ele.startswith("__"):
            continue
        e_obj = getattr(obj, ele)
        if type(e_obj) in ignored_types:
            ret[ele] = type(e_obj).__name__
        else:
            ret[ele] = _do_generate_recurse(e_obj)
    return ret


def _do_generate():
    values = {}
    for mod in modules:
        values[mod.__name__] = _do_generate_recurse(mod)
    return values


def generate():
    """
    Start generating the objects
    """
    values = _do_generate()
    print("\n\n")
    print(json.dumps(values))
    return ''


def OnMidiIn(event):
    pass


print("Available functions:")
print("generate()  - generate and print a list of available functions")
