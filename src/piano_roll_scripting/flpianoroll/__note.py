"""
flpianoroll > note

Note class definition
"""


class Note:
    """
    Represents a note in the FL Studio piano roll.
    """

    def __init__(self) -> None:
        """
        Create a new instance of a `Note` object

        This note won't be added to the piano roll unless it is passed to
        `score.addNote`.
        """
        pass

    @property
    def number(self) -> int:
        """
        Standard MIDI note number (60 is middle C).
        """
        return 0

    @number.setter
    def number(self, new_value: int) -> None:
        pass

    @property
    def time(self) -> int:
        """
        Time at which the note begins (in ticks).
        """
        return 0

    @time.setter
    def time(self, new_value: int) -> None:
        pass

    @property
    def length(self) -> int:
        """
        Length of the note (in ticks).
        """
        return 0

    @length.setter
    def length(self, new_value: int) -> None:
        pass

    @property
    def group(self) -> int:
        """
        Group number that this note belongs to. This can be used to link notes
        together such that if the user moves one, all others in the same group
        are also moved.

        To un-group notes, set the group number to `0`.
        """
        return 0

    @group.setter
    def group(self, new_value: int) -> None:
        pass

    @property
    def pan(self) -> float:
        """
        The panning value of the note, between `0` and `1`. `0.5` is centered.
        """
        return 0.5

    @pan.setter
    def pan(self, new_value: float) -> None:
        pass

    @property
    def velocity(self) -> float:
        """
        The velocity of the note, between `0` and `1`. `0.8` is the default.
        """
        return 0.8

    @velocity.setter
    def velocity(self, new_value: float) -> None:
        pass

    @property
    def release(self) -> float:
        """
        The release of the note, between `0` and `1`. `0.5` is the default.
        """
        return 0.5

    @release.setter
    def release(self, new_value: float) -> None:
        pass

    @property
    def color(self) -> int:
        """
        The color of the note, between `0` and `15`. `0` is the default note
        color.
        """
        return 0

    @color.setter
    def color(self, new_value: int) -> None:
        pass

    @property
    def fcut(self) -> float:
        """
        The note filter cutoff frequency, between `0` and `1`. `0.5` is the
        default.
        """
        return 0.5

    @fcut.setter
    def fcut(self, new_value: float) -> None:
        pass

    @property
    def fres(self) -> float:
        """
        The note filter resonance frequency, between `0` and `1`. `0.5` is the
        default.
        """
        return 0.5

    @fres.setter
    def fres(self, new_value: float) -> None:
        pass

    @property
    def pitchofs(self) -> int:
        """
        The pitch offset of the note, between `-120` (-1 octave) and `120` (+1
        octave).

        This is represented in units of 10 cents, so setting
        `note.pitchofs = 42` will set the pitch offset to +420 cents.
        """
        return 0

    @pitchofs.setter
    def pitchofs(self, new_value: int) -> None:
        pass

    @property
    def slide(self) -> bool:
        """
        Whether the note is a slide note.
        """
        return False

    @slide.setter
    def slide(self, new_value: bool) -> None:
        pass

    @property
    def porta(self) -> bool:
        """
        Whether the note is a portamento note.
        """
        return False

    @porta.setter
    def porta(self, new_value: bool) -> None:
        pass

    @property
    def muted(self) -> bool:
        """
        Whether the note is muted.
        """
        return False

    @muted.setter
    def muted(self, new_value: bool) -> None:
        pass

    @property
    def selected(self) -> bool:
        """
        Whether the note is selected within the piano roll.
        """
        return False

    @selected.setter
    def selected(self, new_value: bool) -> None:
        pass

    def clone(self) -> 'Note':
        """
        Return a new Note object with identical properties to this note.

        This note will not be added to the piano roll until `score.addNote` is
        called with it as an argument.
        """
        return self
