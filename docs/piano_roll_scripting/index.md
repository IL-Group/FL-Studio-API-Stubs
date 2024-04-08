# FL Piano Roll

FL Studio built-in module.

This module provides editing tools for interacting with notes and markers on
the FL Studio piano roll, using its piano roll scripting functionality.

Main script files should use the .pyscript file extension, with additional
modules using standard .py files.

Note that this module is not accessible in MIDI Controller Scripts, it can only
be used in scripts that run in FL Studio's piano roll.

## Contents

* [`Score`](score.md): manipulation of the piano roll score.
* [`Note`](note.md): class representing a note on the piano roll score.
* [`Marker`](marker.md): class representing a marker on the piano roll score.
* [`ScriptDialog`](script_dialog.md): creation of interfaces for scripts.
* [`Utils`](utils.md): utility functions.
