"""
These flags are given as an argument to the
{{docs_url_callback[OnDirtyChannel]}} callback.
"""

CE_New = 0
"""
A channel was added.
"""

CE_Delete = 1
"""
A channel was removed.
"""

CE_Replace = 2
"""
A channel was replaced.
"""

CE_Rename = 3
"""
A channel was renamed.
"""

CE_Select = 4
"""
The channel selection was changed.
"""
