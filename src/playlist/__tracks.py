"""
Playlist > Tracks

Code for managing the properties of playlist tracks
"""


def trackCount() -> int:
    """
    Returns the number of tracks on the playlist.

    Includes empty tracks.

    ## Returns

    * `int`: track count on playlist

    Included since API version 1
    """
    return 0


def getTrackName(index: int) -> str:
    """
    Returns the name of the track at `index`

    For unnamed tracks, returns "Track `n`" where `n` is `index` + 1

    {{note[playlist_indexes]}}

    ## Args

    * `index` (`int`): track index

    ## Returns

    * `str`: track name

    Included since API version 1
    """
    return ""


def setTrackName(index: int, name: str) -> None:
    """
    Sets the name of the track at `index`

    Setting the name to an empty string ("") will reset the name to "Track n"

    {{note[playlist_indexes]}}

    ## Args

    * `index` (`int`): track index

    Included since API version 1
    """


def getTrackColor(index: int) -> int:
    """
    Returns the color of the track at `index`

    Note that colors can be split into or built from components using the
    functions provided in the module [utils](https://miguelguthridge.github.io/FL-Studio-API-Stubs/utils/).

    * [ColorToRGB()](https://miguelguthridge.github.io/FL-Studio-API-Stubs/utils/#utils.ColorToRGB)

    * [RGBToColor()](https://miguelguthridge.github.io/FL-Studio-API-Stubs/utils/#utils.RGBToColor)

    {{note[playlist_indexes]}}

    ## Args

    * `index` (`int`): track index

    ## Returns

    * `int`: track color (`0x--BBGGRR`)

    Included since API version 1
    """
    return 0


def setTrackColor(index: int, color: int) -> None:
    """
    Sets the color of the track at `index`

    Note that colors can be split into or built from components using the
    functions provided in the module [utils](https://miguelguthridge.github.io/FL-Studio-API-Stubs/utils/).

    * [ColorToRGB()](https://miguelguthridge.github.io/FL-Studio-API-Stubs/utils/#utils.ColorToRGB)

    * [RGBToColor()](https://miguelguthridge.github.io/FL-Studio-API-Stubs/utils/#utils.RGBToColor)

    {{note[playlist_indexes]}}

    ## Args

    * `index` (`int`): track index

    * `color` (`int`): track color (`0x--BBGGRR`)

    Included since API version 1
    """


def isTrackMuted(index: int,) -> bool:
    """
    Returns whether the track at `index` is muted

    ## Args

    * `index` (`int`): track index

    ## Returns

    * `bool`: whether track is muted

    Included since API version 1
    """
    return False


def muteTrack(index: int, value: int = -1) -> None:
    """
    Toggle whether the track at `index` is muted. An unmuted track will become
    muted and a muted track will become unmuted.

    ## Args

    * `index` (`int`): track index

    * `value` (`int`, optional): new mute value (1 = mute, 0 = unmute)

    Included since API version 1

    ## API changes

    * `value` parameter added in API v30
    """


def isTrackMuteLock(index: int) -> bool:
    """
    Returns whether the mute status of the track at `index` is locked (meaning
    that solo/unsolo commands won't affect its mute status).

    ## Args

    * `index` (`int`): track index

    ## Returns

    * `bool`: whether track's mute status is locked

    Included since API version 2
    """
    return False


def muteTrackLock(index: int) -> None:
    """
    Toggle whether the track at `index`'s mute status is locked (meaning that
    solo/unsolo commands won't affect its mute status).

    ## Args

    * `index` (`int`): track index

    Included since API version 2
    """


def isTrackSolo(index: int) -> bool:
    """
    Returns whether the track at `index` is solo

    ## Args

    * `index` (`int`): track index

    ## Returns

    * `bool`: whether track is muted

    Included since API version 1
    """
    return False


def soloTrack(index: int, value: int = -1, inGroup: bool = False) -> None:
    """
    Toggle whether the track at `index` is solo. An unsolo track will become
    solo and a solo track will become unsolo. If `value` is provided, it will
    control what the new value will be (`1`: solo, `0`: unsolo).

    The `inGroup` parameter determines whether tracks in the same group are
    also soloed. For example, if tracks `2` and `3` are grouped under track
    `1`, soloing any of them with `inGroup=True` will solo all of them.

    ## Args

    * `index` (`int`): track index

    * `value` (`int`, optional): new solo value

    * `inGroup` (`bool`, optional): solo track within track group

    Included since API version 1

    ## API changes

    * `inGroup` parameter introduced in API version 30
    """


def isTrackSelected(index: int) -> bool:
    """
    Returns whether the track at `index` is selected

    ## Args

    * `index` (`int`): track index

    ## Returns

    * `bool`: whether track is selected

    Included since API version 12
    """
    return False


def selectTrack(index: int) -> None:
    """
    Toggle whether the track at `index` is selected. A deselected track will
    become selected and a selected track will become deselected.

    ## Args

    * `index` (`int`): track index

    Included since API version 12
    """


def selectAll() -> None:
    """
    Select all tracks on the playlist

    Included since API version 12
    """


def deselectAll() -> None:
    """
    Deselect all tracks on the playlist

    Included since API version 12
    """


def getTrackActivityLevel(index: int) -> float:
    """
    Returns the activity level of the track at `index`. This value is either
    `0.0` or `0.5`, representing whether an unmuted playlist clip is active at
    the playhead.

    Compare to `playlist.getTrackActivityLevelVis()`, which returns a "visual
    activity level" that takes the time since the most recent note-on event
    into account.

    ## Args

    * `index` (`int`): track index

    ## Returns

    * `float`: activity level
          * `0.0`: No clip is active

          * `0.5`: A clip is active at the play head

    ## Notes
    * This function will only return 0.0 or 0.5, and nothing in between. There
      is no documentation for whether this is by design.

    Included since API version 1
    """
    return 0.0


def getTrackActivityLevelVis(index: int) -> float:
    """
    Returns the visual activity level of the track at `index`. This value is a
    float in the range of 0.0 - 1.0 representing whether an unmuted playlist
    clip is active at the playhead and how recently a note-on event was played
    on this track.

    Compare to `playlist.getTrackActivityLevel()`, which just returns whether
    there is an active clip at that playhead.

    ## Args

    * `index` (`int`): track index

    ## Returns

    * float: activity level
          * `0.0`: No clip is active

          * `0.5 - 1.0`: A clip is active at the play head. Higher values represent more recent note-on events.

    Included since API version 1
    """
    return 0.0
