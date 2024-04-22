"""
Mixer > Tracks

Code for managing the properties of mixer tracks
"""
import midi


def getTrackName(index: int) -> str:
    """
    Returns the name of the track at `index`.

    ## Args

    * `index` (`int`): track index.

    ## Returns

    * `str`: name of track.

    Included since API version 1.
    """
    return ""


def setTrackName(index: int, name: str) -> None:
    """
    Sets the name of track at `index`

    Setting the name to an empty string will reset the name of the track to
    its default.

    ## Args

    * index (`int`): index of mixer track.

    * name (`str`): new name.

    Included since API version 1.
    """


def getTrackColor(index: int) -> int:
    """
    Returns the color of the track at `index`.

    {{note[colors]}}

    ## Args

    * `index` (`int`): track index.

    ## Returns

    * `int`: color of track (0x--BBGGRR).

    Included since API version 1.
    """
    return 0


def setTrackColor(index: int, color: int) -> None:
    """
    Sets the color of the track at `index`.

    {{note[colors]}}

    ## Args

    * `index` (`int`): track index.

    * `color` (`int`): color of track (0x--BBGGRR).

    Included since API version 1.
    """


def getSlotColor(index: int, slot: int) -> int:
    """
    Returns the color of a mixer track FX slot.

    {{note[colors]}}

    ## Args

    * `index` (`int`): mixer track index.

    * `slot` (`int`): mixer track FX slot index.

    ## Returns

    * `int`: color of mixer track FX slot.

    Included since API Version 32.
    """
    return 0


def setSlotColor(index: int, slot: int, color: int) -> None:
    """
    Sets the color of a mixer track FX slot.

    {{note[colors]}}

    ## Args

    * `index` (`int`): mixer track index.

    * `slot` (`int`): mixer track FX slot index.

    * color (`int`): color of mixer track FX slot.

    Included since API Version 32.
    """


def isTrackArmed(index: int) -> bool:
    """
    Returns whether the track at `index` is armed for recording.

    ## Args

    * `index` (`int`): track index.

    ## Returns

    * `bool`: whether track is armed.

    Included since API version 1.
    """
    return False


def armTrack(index: int) -> None:
    """
    Toggles whether the track at index is armed for recording.

    ## Args

    * `index` (`int`): track index.

    Included since API version 1.
    """


def isTrackSolo(index: int) -> bool:
    """
    Returns whether the track at `index` is solo.

    ## Args

    * `index` (`int`): track index.

    ## Returns

    * `bool`: whether track is solo.

    Included since API version 1.
    """
    return False


def soloTrack(index: int, value: int = -1, mode: int = -1) -> None:
    """
    Toggles whether the track at index is solo.

    ## Args

    * `index` (`int`): track index.

    * `value` (`int`, optional): the new value for the solo state (`1` for
      solo, `0` for unsolo). Defaults to `-1` (toggle).

    * `mode` (`int`, optional): solo mode to use. One of:

            * `1`: solo mixer track including source tracks.
            * `2`: solo mixer track including send tracks.
            * `3`: solo mixer track including source and sends.
            * `4`: solo only this mixer track.


    Included since API version 1.
    """


def isTrackEnabled(index: int) -> bool:
    """
    Returns whether the track at `index` is enabled

    ## Note

    * This seems to be functionally identical to `not isTrackMuted()`.

    ## Args

    * `index` (`int`): track index.

    ## Returns

    * `bool`: whether track is enabled.

    Included since API version 1.
    """
    return False


def isTrackAutomationEnabled(index: int, plugIndex: int) -> bool:
    """
    Returns whether the plugin at `plugIndex` on track at `index` has
    automation enabled.

    ## Args

    * `index` (`int`): track index.

    * `plugIndex` (`int`): index of plugin.

    ## Returns

    * `bool`: whether automation is enabled for the track.

    Included since API version 1.
    """
    return False


def enableTrack(index: int) -> None:
    """
    Toggles whether the track at `index` is enabled.

    ## Note

    * This seems to be functionally identical to `muteTrack()`.

    ## Args

    * index (`int`): track index.

    Included since API version 1.
    """


def isTrackMuted(index: int) -> bool:
    """
    Returns whether the track at `index` is muted.

    ## Args

    * `index` (`int`): track index.

    ## Returns

    * `bool`: whether track is solo.

    Included since API version 2.
    """
    return False


def muteTrack(index: int, value: int = -1) -> None:
    """
    Toggles whether the track at index is muted.

    ## Args

    * `index` (`int`): track index.

    * `value` (`int`, optional): the new value for the mute state (`1` for
      mute, `0` for unmute). Defaults to `-1` (toggle).

    Included since API version 2.
    """


def isTrackMuteLock(index: int) -> bool:
    """
    Returns whether the mute state of the track at `index` is locked.

    If this is true, the mute status of this track won't change when other
    tracks are solo or unsolo.

    ## Args

    * `index` (`int`): track index.

    ## Returns

    * `bool`: whether track is mute locked.

    Included since API version 13.
    """
    return False


def getTrackVolume(index: int, mode: int = 0) -> float:
    """
    Returns the volume of the track at `index`. Volume lies within the range
    `0.0` - `1.0`. Note that the default value is `0.8`. Use the `mode` flag to
    get the volume in decibels.

    ## Args

    * `index` (`int`): track index.

    * `mode` (`int`, optional): whether to return the volume as a value
      between `0` and `1`, or in decibels.

    ## Returns

    * `float`: volume of track.

    Included since API version 1.
    """
    return 0.0


def setTrackVolume(
    index: int,
    volume: float,
    pickupMode: int = midi.PIM_None,
) -> None:
    """
    Sets the volume of the track at `index`. Volume lies within the range
    `0.0` - `1.0`. Note that the default value is `0.8`. Use the pickup mode
    flag to set pickup options.

    ## Args

    * `index` (`int`): track index.

    * `volume` (`float`): volume of track.

    * `pickupMode` (`int`, optional): define the pickup behavior. Refer to
      the {{docs_url_page("pickup modes documentation", "midi_controller_scripting/midi/pickup modes")}}.

    Included since API version 1.
    """


def getTrackPan(index: int) -> float:
    """
    Returns the pan of the track at `index`. Pan lies within the range
    100% left (`-1.0`) - 100% right (`1.0`). Note that the default value is
    `0.0`.

    ## Args

    * `index` (`int`): track index.

    ## Returns

    * `float`: pan of track.

    Included since API version 1.
    """
    return 0.0


def setTrackPan(
    index: int,
    pan: float,
    pickupMode: int = midi.PIM_None,
) -> None:
    """
    Sets the pan of the track at `index`. Pan lies within the range
    100% left (`-1.0`) - 100% right (`1.0`). Note that the default value is
    `0.0`. Use the pickup mode flag to set pickup options.

    ## Args

    * `index` (`int`): track index.

    * `pan` (`float`): pan of track.

    * `pickupMode` (`int`, optional): define the pickup behavior. Refer to
      the {{docs_url_page("pickup modes documentation", "midi_controller_scripting/midi/pickup modes")}}.


    Included since API version 1.
    """


def getTrackStereoSep(index: int) -> float:
    """
    Returns the stereo separation of the track at `index`. Stereo separation
    lies within the range 100% centered (`-1.0`) - 100% separated (`1.0`). Note
    that the default value is `0.0`.

    ## Args

    * `index` (`int`): track index.

    ## Returns

    * `float`: stereo separation of track.

    Included since API version 12.
    """
    return 0.0


def setTrackStereoSep(
    index: int,
    pan: float,
    pickupMode: int = midi.PIM_None,
) -> None:
    """
    Sets the stereo separation of the track at `index`. Stereo separation
    lies within the range 100% centered (`-1.0`) - 100% separated (`1.0`). Note
    that the default value is `0.0`. Use the pickup mode flag to set pickup
    options.

    ## Args

    * `index` (`int`): track index.

    * `sep` (`float`): stereo separation of track.

    * `pickupMode` (`int`, optional): define the pickup behavior. Refer to
      the {{docs_url_page("pickup modes documentation", "midi_controller_scripting/midi/pickup modes")}}.

    Included since API version 12.
    """


def setRouteTo(index: int, destIndex: int, value: int) -> None:
    """
    Route the track at `index` to the track at `destIndex`.

    Ensure that after all routing changes are made, the `afterRoutingChanged()`
    function is called to allow the UI to update correctly.

    ## Args

    * `index` (`int`): source track index

    * `destIndex` (`int`): destination track index

    * `value` (`int`): whether to enable the route (`1`) or disable it (`0`)

    Included since API version 1
    """


def getRouteSendActive(index: int, destIndex: int) -> bool:
    """
    Return whether the track at `index` is routed to the track at `destIndex`

    ## Args

    * `index` (`int`): source track

    * `destIndex` (`int`): destination track

    ## Returns

    * `bool`: whether the tracks are routed

    Included since API version 1
    """
    return False


def afterRoutingChanged() -> None:
    """
    Notify FL Studio that channel routings have changed.

    Included since API version 1
    """


def getTrackPeaks(index: int, mode: int) -> float:
    """
    Returns the current audio peak value for the track at `index`.

    ## Args

    * `index` (`int`): track index

    * `mode` (`int`): track peaks mode
          * `0`: left channel

          * `1`: right channel

          * `2`: maximum from left and right channels

          * Values for inverted peaks are present, but appear to be
            incorrect.

    ## Returns

    * `float`: track peak values:

          * `0.0`: silence

          * `1.0`: 0 dB

          * `>1.0`: clipping

    Included since API version 1
    """
    return 0.0


def getTrackRecordingFileName(index: int) -> str:
    """
    Returns the file name for audio being recorded on the track at `index`.

    ## Note

    * Files can't be opened in FL Studio's Python interpreter due to disk
      access being disabled for security reasons.

    ## Args

    * `index` (`int`): track index

    ## Returns

    * `str`: filename

    Included since API version 1
    """
    return ""


def linkTrackToChannel(mode: int) -> None:
    """
    Link a mixer track to a channel.

    ## HELP WANTED
    * How does this function call work?

    ## Args

    * `mode` (`int`): link mode
          * `ROUTE_ToThis` (`0`)

          * `ROUTE_StartingFromThis` (`1`)

    Included since API version 1
    """


def getTrackDockSide(index: int) -> int:
    """
    Returns the dock side of the mixer for track at `index`.

    ## Args

    * `index` (`int`): track index.

    ## Returns

    * `int`: docking side:
          * `0`: Left.

          * `1`: Center (default).

          * `2`: Right.

    Included since API version 13.
    """
    return 0


def isTrackSlotsEnabled(index: int) -> bool:
    """
    Returns whether effects are enabled for a particular track, using the
    "enable effects slots" button.

    ## Args

    * `index` (`int`): track index.

    ## Returns

    * `bool`: whether effects are enabled on the track.

    Included since API Version 19.
    """
    return False


def enableTrackSlots(index: int, value: bool = False) -> None:
    """
    Toggle whether all effects are enabled on a track.

    ## KNOWN ISSUES

    * If a `value` isn't supplied, the value will be set to `False` rather than
      toggled.

    ## Note

    * Although there is no visual indication, this can be used to toggle
      effects for empty tracks, leading to effects users add in the future
      not doing anything.

    ## Args

    * `index` (`int`): Track index.

    * `value` (`bool`): Whether effects should be enabled or not.

    Included since API Version 19.
    """


def isTrackRevPolarity(index: int) -> bool:
    """
    Returns whether the polarity is reversed for the track at `index`.

    ## Args

    * `index` (`int`): track index.

    ## Returns

    * `bool`: whether polarity is inverted.

    Included since API Version 19.
    """
    return False


def revTrackPolarity(index: int, value: bool = False) -> None:
    """
    Inverts the polarity for a particular track.

    ## KNOWN ISSUES

    * If a `value` isn't supplied, the value will be set to `False` rather than
      toggled.

    ## Args

    * `index` (`int`): Index of track to reverse polarity for.
    * `value` (`bool`): Whether polarity should be swapped or not.

    Included since API Version 19.
    """


def isTrackSwapChannels(index: int) -> bool:
    """
    Returns whether left and right channels are inverted for a particular
    track.

    ## Args

    * `index` (`int`): track index.

    ## Returns

    * `bool`: whether left and right are inverted.

    Included since API Version 19.
    """
    return False


def swapTrackChannels(index: int, value: bool = False) -> None:
    """
    Toggle whether left and right channels are swapped for the mixer track at
    `index`.

    ## KNOWN ISSUES

    * If a `value` isn't supplied, the value will be set to `False` rather than
      toggled.

    ## Args

    * `index` (`int`): Index of track to swap channels for.
    * `value` (`bool`): Whether channels should be swapped or not.

    Included since API Version 19.
    """


def linkChannelToTrack(
    channel: int,
    track: int,
    select: bool = False,
) -> None:
    """
    Link the given channel to the given mixer track.

    ## Args

    * `channel` (`int`): channel index on channel rack (respecting groups).

    * `track` (`int`): mixer track index.

    * `select` (`bool`, optional): whether to select the mixer track. Defaults
      to `False`.

    Included since API Version 23.
    """
