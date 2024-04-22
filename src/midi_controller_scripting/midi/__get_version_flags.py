"""
These flags are given to {{docs_url_fn[ui.getVersion]}} to control the version
information returned.
"""

VER_Major = 0
"""
Return major version number as `int`.

```py
>>> import ui, midi
>>> ui.getVersion(midi.VER_Major)
20
```
"""

VER_Minor = 1
"""
Return minor version number as `int`.

```py
>>> import ui, midi
>>> ui.getVersion(midi.VER_Minor)
8
```
"""

VER_Release = 2
"""
Return release version number as `int`.

```py
>>> import ui, midi
>>> ui.getVersion(midi.VER_Release)
4
```
"""

VER_Build = 3
"""
Return build number as `int`.

```py
>>> import ui, midi
>>> ui.getVersion(midi.VER_Build)
2553
```
"""

VER_VersionAndEdition = 4
"""
Return program version and edition as `str`.

```py
>>> import ui, midi
>>> ui.getVersion(midi.VER_VersionAndEdition)
"Producer Edition v20.8.4 [build 2553]"
```
"""

VER_FullVersionAndEdition = 5
"""
Return program version and edition as `str`.

```py
>>> import ui, midi
>>> ui.getVersion(midi.VER_FullVersionAndEdition)
"Producer Edition v20.8.4 [build 2553] - Signature Bundle - 64Bit"
```
"""

VER_ArchAndBuild = 6
"""
Return operating system and system architecture as `str`.

```py
>>> import ui, midi
>>> ui.getVersion(midi.VER_ArchAndBuild)
"Windows - 64Bit [BETA]"
```
"""
