"""
The `flpianoroll.score` object is used to represent the state of the piano
roll.
"""
from .__note import Note
from .__marker import Marker


class Score:
    """
    Access via the module attribute `flpianoroll.score`.

    Represents the current selection of the FL Studio score, or, if there is no
    selection, the full contents of the current instrument on the piano roll.
    """
    def __init__(self) -> None:
        pass

    @property
    def PPQ(self) -> int:
        """
        The PPQN (ticks per quarter note) of the score.

        Read-only.
        """
        return 96

    @property
    def tsnum(self) -> int:
        """
        The project's overall time signature numerator, as per the project
        settings. Note that this does not reflect time signature markers.

        Read-only.
        """
        return 0

    @property
    def tsden(self) -> int:
        """
        The project's overall time signature denominator, as per the project
        settings. Note that this does not reflect time signature markers.

        Read-only.
        """
        return 0

    def clear(self, all: bool = False) -> None:
        """
        Clear the selected notes and markers on the piano roll, or if there is
        no selection, clear everything.

        Markers are considered to be selected if all notes within them are
        selected.

        ## Args

        * `all` (`bool`, optional): whether to clear all content from the
          score, regardless of selection status. Defaults to `False`.
        """

    def clearNotes(self, all: bool = False) -> None:
        """
        Clear the selected notes on the piano roll, or if there is no
        selection, clear all notes.

        ## Args

        * `all` (`bool`, optional): whether to clear all notes from the
          score, regardless of selection status. Defaults to `False`.
        """

    def clearMarkers(self, all: bool = False) -> None:
        """
        Clear the selected markers on the piano roll, or if there is no
        selection, clear all markers.

        Markers are considered to be selected if all notes within them are
        selected.

        ## Args

        * `all` (`bool`, optional): whether to clear all markers from the
          score, regardless of selection status. Defaults to `False`.
        """

    @property
    def noteCount(self) -> int:
        """
        The number of notes currently in the score.
        """
        return 0

    def addNote(self, note: Note) -> None:
        """
        Add a note to the score.

        ## Args

        * `note` (`Note`): the note to add
        """

    def getNote(self, index: int) -> Note:
        """
        Return the note at position `index` from within the score.

        ## Args

        * `index` (`int`): index of note

        ## Returns

        * `Note`: the note
        """
        return Note()

    def deleteNote(self, index: int) -> None:
        """
        Remove the note at position `index` from within the score.

        ## Args

        * `index` (`int`): index of the note to remove
        """

    @property
    def markerCount(self) -> int:
        """
        The number of markers currently in the score.
        """
        return 0

    def addMarker(self, marker: Marker) -> None:
        """
        Add a marker to the score.

        ## Args

        * `marker` (`Marker`): the marker to add
        """

    def getMarker(self, index: int) -> Marker:
        """
        Return the marker at position `index` from within the score.

        ## Args

        * `index` (`int`): index of marker

        ## Returns

        * `Marker`: the marker
        """
        return Marker()

    def deleteMarker(self, index: int) -> None:
        """
        Remove the marker at position `index` from within the score.

        ## Args

        * `index` (`int`): index of the marker to remove
        """


score = Score()
"""
The singular instance of the `Score` class, used to access and manipulate data
in FL Studio's piano roll.
"""
