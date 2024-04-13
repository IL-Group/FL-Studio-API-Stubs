"""
The editor functions of the `ui` module can be used to launch editor windows,
such as Edison and the event editor.
"""


def launchAudioEditor(
    reuse: int,
    filename: str,
    index: int,
    preset: str,
    presetGUID: str,
) -> int:
    """
    Launches an audio editor for track at `index` and returns the state of
    the editor. Set `reuse` to true (`1`) to reuse an already loaded audio
    editor.

    ## HELP WANTED

    * How do I get this to work? I can only get it to open an empty window.

    ## Args

    * `reuse` (`int`): whether to reuse an already open audio editor.

    * `filename` (`str`): filename to open?

    * `index` (`int`): mixer track index to open on.

    * `preset` (`str`): ???

    * `presetGUID` (`str`): ???

    ## Returns

    * `int`: ???

    Included since API version 1.
    """
    return 0


def openEventEditor(
    eventId: int,
    mode: int,
    newWindow: int = 0,
) -> int:
    """
    Launches an event editor for `eventId`.

    See the {{docs_url_page("event mapping tutorial", "tutorials/event_mapping")}}
    for more information on REC events.

    ## Args

    * `eventId` (`int`): event ID.

    * `mode` (`int`): Refer to the {{fl_manual_anchor[openEventEditorMode]}}.

    * `newWindow` (`int`, optional): whether to open in a new window. Defaults
      to 0.

    ## Returns:
     * `int`: ???

    Included since API version 9.
    """
    return 0
