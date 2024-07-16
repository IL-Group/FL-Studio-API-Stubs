"""
Playlist > Performance

Functions for interacting with performance mode.
"""
import midi


def getDisplayZone() -> int:
    """
    Returns the current display zone in the playlist or zero if none.

    The display zone is the rectangular region for which a controller is active
    in performance mode, indicated by a red rectangle on the playlist.

    This value can be set using {{docs_url_fn[playlist.liveDisplayZone]}}.

    ## Returns

    * `int`: current display zone.

    Included since API version 1.
    """
    return 0


def lockDisplayZone(index: int, value: int) -> None:
    """
    Lock display zone at `index`.

    ## HELP WANTED

    * Explanation for parameters.

    ## Args

    * `index` (`int`): ???

    * `value` (`int`): ???

    Included since API version 1.
    """


def liveDisplayZone(
    left: int,
    top: int,
    right: int,
    bottom: int,
    duration: int = 0,
) -> None:
    """
    Set the display zone in the playlist to the specified co-ordinates. Use the
    optional `duration` parameter to make display zone temporary.

    ## Args

     * `left` (`int`): the zero-indexed position of the time marker from which
       to begin the display zone highlight.

     * `top` (`int`): the one-indexed track number from which to begin the
       display zone highlight.

     * `right` (`int`): the zero-indexed position of the time marker from which
       to end the display zone highlight. The highlight will go up to this
       marker, but will not include it.

     * `bottom` (`int`): the one-indexed track number from which to end the
        display zone highlight. The highlight will go up to, and will include
        this track.

     * `duration` (`int`, optional): duration for which to show the display
       zone highlight in ms. Defaults to `0`, for infinite duration.

    Included since API version 1.
    """


def getLiveLoopMode(index: int) -> int:
    """
    Get the loop mode of the given track.

    This value reflects the value in the "motion" section in the performance
    menu of the track.

    ## Args

    * `index` (`int`): track index.

    ## Returns

    * `int`: live loop mode:
          * `0` (`LiveLoop_Stay`): Stay.

          * `1` (`LiveLoop_OneShot`): One shot.

          * `2` (`LiveLoop_MarchWrap`): March and wrap.

          * `3` (`LiveLoop_MarchStay`): March and stay.

          * `4` (`LiveLoop_MarchStop`): March and stop.

          * `5` (`LiveLoop_Random`): Random.

          * `6` (`LiveLoop_ExRandom`): Exclusive random (play all clips on the track before playing anything again).

    Included since API version 1.
    """
    return 0


def getLiveTriggerMode(index: int) -> int:
    """
    Get the trigger mode of the given track.

    This value reflects the value in the "press" section in the performance
    menu of the track.

    ## Args

    * `index` (`int`): track index.

    ## Returns

    * `int`: live trigger mode:
          * `0` (`LiveTrig_Retrigger`): Retrigger.

          * `1` (`LiveTrig_Hold`): Hold and stop.

          * `2` (`LiveTrig_HMotion`): Hold and motion.

          * `3` (`LiveTrig_Latch`): Latch.

    Included since API version 1.
    """
    return 0


def getLivePosSnap(index: int) -> int:
    """
    Get the position sync mode of the given track.

    This value reflects the value in the "position sync" section in the
    performance menu of the track.

    ## Args

    * `index` (`int`): track index.

    ## Returns

    * `int`: live position snap:
          * `0` (`LiveSnap_Off`): No snap.

          * `1` (`LiveSnap_Fourth`): 1/4 beat.

          * `2` (`LiveSnap_Half`): 1/2 beat.

          * `3` (`LiveSnap_One`): 1 beat.

          * `4` (`LiveSnap_Two`): 2 beats.

          * `5` (`LiveSnap_Four`): 4 beats.

          * `6` (`LiveSnap_Auto`): Auto.

    Included since API version 1.
    """
    return 0


def getLiveTrigSnap(index: int) -> int:
    """
    Get the trigger sync mode of the given track.

    This value reflects the value in the "trigger sync" section in the
    performance menu of the track.

    ## Args

    * `index` (`int`): track index.

    ## Returns

    * `int`: live position snap:
          * `0` (`LiveSnap_Off`): No snap.

          * `1` (`LiveSnap_Fourth`): 1/4 beat.

          * `2` (`LiveSnap_Half`): 1/2 beat.

          * `3` (`LiveSnap_One`): 1 beat.

          * `4` (`LiveSnap_Two`): 2 beats.

          * `5` (`LiveSnap_Four`): 4 beats.

          * `6` (`LiveSnap_Auto`): Auto.

    Included since API version 1.
    """
    return 0


def getLiveStatus(index: int, mode: int = midi.LB_Status_Default) -> int:
    """
    Returns the live status for track at `index`.

    This can be used to determine if there are any blocks playing or scheduled.

    ## Args

     * `index` (`int`): track index.

     * `mode` (`int`, optional): live status mode. Defaults to 'LB_Status_Default'.

    ## Returns

     * `int`: live status of track: refer to {{fl_manual_anchor[getLiveStatusMode]}}.

    Included since API version 1.
    """
    return 0


def getLiveBlockStatus(
    index: int,
    blockNum: int,
    mode: int = midi.LB_Status_Default,
) -> int:
    """
    Returns the live block status for block `blockNum` within the track at
    `index`.

    This can be used to determine if this block is playing or scheduled.

    ## Args

    * `index` (`int`): track index.

    * `blockNum` (`int`): block number.

    * `mode` (`int`, optional): live status mode. Defaults to 'LB_Status_Default'.

    ## Returns

    * `int`: live status of track: refer to {{fl_manual_anchor[getLiveStatusMode]}}.

    Included since API version 1.
    """
    return 0


def getLiveBlockColor(index: int, blockNum: int) -> int:
    """
    Returns the color for block `blockNum` within the track at `index`.

    {{note[colors]}}

    ## Args

    * `index` (`int`): track index.

    * `blockNum` (`int`): block number.

    ## Returns

    * `int`: block color (`0x--BBGGRR`).

    Included since API version 1.
    """
    return 0


def triggerLiveClip(
    index: int,
    subNum: int,
    flags: int,
    velocity: int = -1,
) -> None:
    """
    Triggers live clip for track at `index` and for block `subNum`.

    ## Args

    * `index` (`int`): track index.

    * `subNum` (`int`): block number (usually `blockNum`), or `-1` to stop live
      clips on this track.

    * `flags` (`int`): live clip trigger flags. Refer to {{fl_manual_anchor[triggerLiveClipFlags]}}.

    * `velocity` (`int`, optional): velocity for triggering clip. Defaults to `-1`.

    Included since API version 1.
    """


def refreshLiveClips(*args) -> None:
    """
    Refresh live clips for track at `index`.

    ## HELP WANTED:
    * What does this do?

    This function appears to work, even when given no arguments.

    ## Args

    * `index` (`int`): track index.

    * `value` (`int`): ???

    Included since API version 1.
    """


def incLivePosSnap(index: int, value: int) -> None:
    """
    Increase live position snap for track at `index`.

    This is used to cycle through modes in the "position sync" section of the
    track's performance menu.

    ## Args

    * `index` (`int`): track index.

    * `value` (`int`): delta amount to change position snap mode by.

    Included since API version 1.
    """


def incLiveTrigSnap(index: int, value: int) -> None:
    """
    Increase live trigger snap for track at `index`.

    This is used to cycle through modes in the "trigger sync" section of the
    track's performance menu.

    ## Args

    * `index` (`int`): track index.

    * `value` (`int`): delta amount to change trigger snap mode by.

    Included since API version 1.
    """


def incLiveLoopMode(index: int, value: int) -> None:
    """
    Increase live loop mode for track at `index`.

    This is used to cycle through modes in the "motion" section of the
    track's performance menu.

    ## Args

    * `index` (`int`): track index.

    * `value` (`int`): delta amount to change loop mode by.

    Included since API version 1.
    """


def incLiveTrigMode(index: int, value: int) -> None:
    """
    Increase live trigger mode for track at `index`.

    This is used to cycle through modes in the "press" section of the
    track's performance menu.

    ## Args

    * `index` (`int`): track index.

    * `value` (`int`): delta amount to change trigger mode by.

    Included since API version 1.
    """


def getVisTimeBar() -> int:
    """
    Returns the current bar number, as shown in the song position panel. See
    {{docs_url_page("time format documentation", "midi_controller_scripting/tutorials/time_units")}}.

    ## Returns

    * `int`: time bar.

    Included since API version 1.
    """
    return 0


def getVisTimeStep() -> int:
    """
    Returns the step number within the song, as shown in the song position
    panel. See
    {{docs_url_page("time format documentation", "midi_controller_scripting/tutorials/time_units")}}.

    ## Returns

    * `int`: time step.

    Included since API version 1.
    """
    return 0


def getVisTimeTick() -> int:
    """
    Returns the tick number within the song, as shown in the song position
    panel. See
    {{docs_url_page("time format documentation", "midi_controller_scripting/tutorials/time_units")}}.

    ## Returns

    * `int`: time tick.

    Included since API version 1.
    """
    return 0


def getPerformanceModeState() -> bool:
    """
    Returns whether FL Studio's performance mode is enabled.

    ## Returns

    * `bool`: whether performance mode is enabled.

    Included since API Version 21.
    """
    return False


def getSongStartTickPos() -> int:
    """
    Returns the number of ticks before the "song start" marker (which marks the
    end of the performance mode section).

    ## WARNING

    * This function is undocumented.

    ## Returns

    * `int`: number of ticks before the "song start" marker.

    Included since API Version ???
    """
    return 0


def liveBlockNumToTime(index: int) -> int:
    """
    Returns the number of ticks before the live block marker at `index`.

    ## WARNING

    * This function is undocumented.

    ## Args

    * `index` (`int`): index of live block marker.

    ## Returns

    * `int`: number of ticks.

    Included since API Version ???
    """
    return 0


def liveTimeToBlockNum(time: int) -> int:
    """
    Returns the block number that a time (in ticks) is associated with in live
    performance mode.

    ## Note

    * The first tick of each block is counted as part of the previous block.
      For example, if block `1` starts at tick `384`, `liveTimeToBlockNum(384)`
      will return `0`, but `liveTimeToBlockNum(385)` will return `1`.

    * This is likely a bug.

    ## WARNING

    * This function is undocumented.

    ## Args

    * `time` (`int`): time in ticks.

    ## Returns

    * `int`: block number (0-indexed).

    Included since API Version ???
    """
    return 0


def scrollTo(a: int, b: int, c: int, d: int) -> None:
    """
    Scroll to the given location?

    ## WARNING

    * This function is undocumented.

    ## Args

    * `a` (`int`): ???

    * `b` (`int`): ???

    * `c` (`int`): ???

    * `d` (`int`): ???

    Included since API Version ???
    """
