"""
{{module_title[enveditor]}}

FL Studio built-in module.

This module provides editing tools for interacting with audio clips in the
Edison editor, using its integrated scripts functionality.

Main script files should use the `.pyscript` file extension, with additional
modules using standard `.py` files.

Note that this module is not accessible in MIDI Controller Scripts, it can only
be used in scripts that run in Edison's editor.
"""
__all__ = [
    'ScriptDialog',
    'Region',
    'Sample',
    'EditorSample',
    'MEEditor',
    'Editor',
    'TUtils',
    'Utils',
]

from .__script_dialog import ScriptDialog
from .__sample import Region, Sample, EditorSample, MEEditor, Editor
from .__utils import TUtils, Utils
