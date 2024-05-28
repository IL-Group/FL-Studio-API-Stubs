"""
# Scripts / consts.py

Constants used by build and CI scripts
"""
import os
from pathlib import Path


DOCS_SECTIONS = os.listdir(Path('src'))
"""
List of sections within the docs -- maps to the contents of the src/ directory.
"""

MODULES: list[str] = []
"""
List of all modules distributed by the library.
"""

PATHS_TO_MODULES: dict[str, str] = {}
"""
Mapping of modules names to their locations in the online documentation (also
their location within `src/`)
"""

# Add items
for section in DOCS_SECTIONS:
    mods = os.listdir(Path('src') / section)
    MODULES.extend(mods)
    for mod in mods:
        PATHS_TO_MODULES[mod] = section
