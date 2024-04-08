"""
# FL Piano Roll

FL Studio built-in module.

This module provides editing tools for interacting with notes and markers on
the FL Studio piano roll, using its piano roll scripting functionality.

Main script files should use the `.pyscript` file extension, with additional
modules using standard `.py` files.

Note that this module is not accessible in MIDI Controller Scripts, it can only
be used in scripts that run in FL Studio's piano roll.
"""
from enveditor import ScriptDialog, Utils
from .__note import Note
from .__marker import Marker
from .__score import score


__all__ = [
    'score',
    'Note',
    'Marker',
    'ScriptDialog',
    'Utils',
]
