"""
After giving a `FPT_` command to {{docs_url_fn[transport.globalTransport]}},
it returns a status flag to indicate the result of the command.

These flags begin with `GT_`.
"""

GT_Cannot = -1
"""
Command not handled.
"""
GT_None = 0
"""
None
"""
GT_Plugin = 1
"""
Command handled by focused plugin.
"""
GT_Form = 2
"""
Command handled by focused form.
"""
GT_Menu = 4
"""
Command handled by menu.
"""
GT_Global = 8
"""
Command handled globally by FL Studio.
"""
GT_All = GT_Plugin | GT_Form | GT_Menu | GT_Global
"""
Command handled by anything.
"""
