"""
{{module_title[flpianoroll]}}

This module provides editing tools for interacting with notes and markers on
the FL Studio piano roll, using its piano roll scripting functionality.

Note that this module is not accessible in MIDI Controller Scripts, it can only
be used in scripts that run in FL Studio's piano roll.

## Table of contents

* {{docs_url_attr[flpianoroll.ScriptDialog]}}: create, show and get responses
  from dialog windows.
* {{docs_url_attr[flpianoroll.score]}}: access and manipulate the piano roll
  contents.
* {{docs_url_attr[flpianoroll.Note]}}: a class to represent notes in the piano
  roll.
* {{docs_url_attr[flpianoroll.Marker]}}: a class to represent markers in the
  piano roll.
* {{docs_url_attr[flpianoroll.Utils]}}: a collection of useful functions for
  interacting with the piano roll.
"""
from enveditor import Utils
from .__script_dialog import ScriptDialog
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
