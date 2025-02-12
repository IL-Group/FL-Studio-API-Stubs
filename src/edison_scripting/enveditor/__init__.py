"""
{{module_title[enveditor]}}

This module provides editing tools for interacting with audio clips in the
Edison editor, using its integrated scripts functionality.

Main script files should use the `.pyscript` file extension, with additional
modules using standard `.py` files.

Note that this module is not accessible in MIDI Controller Scripts, it can only
be used in scripts that run in Edison's editor.

## Table of contents

* {{docs_url_attr[enveditor.ScriptDialog]}}: create, show and get responses
  from dialog windows.
* {{docs_url_attr[enveditor.Sample]}}: interact with audio samples.
* {{docs_url_attr[enveditor.EditorSample]}}: the sample loaded into Edison
* {{docs_url_attr[enveditor.Region]}}: a region of a sample.
* {{docs_url_attr[enveditor.Editor]}}: an object representing the state of
  the Edison editor.
* {{docs_url_attr[enveditor.Utils]}}: a collection of useful functions for
  interacting with audio.
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

from .__sample import Editor, EditorSample, MEEditor, Region, Sample
from .__script_dialog import ScriptDialog
from .__utils import TUtils, Utils
