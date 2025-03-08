"""
The classes and functions documented here are used to manipulate and interact
with samples within the Edison editor.
"""
from typing import Literal


class Region:
    """
    Represents a region or marker within a sample

    A region is bound by a start and end point, and a marker only has a start
    point.
    """
    @property
    def SampleStart(self) -> int:
        """
        The starting point of this region in samples.
        """
        return 0

    @property
    def SampleEnd(self) -> int:
        """
        The ending point of this region in samples. If this is greater than the
        length of the sample, then this region is actually a marker.
        """
        return 0


class MEEditor:
    """
    An object representing the state of the Edison editor.

    For selections, if the start point is `0` and the end point is
    `EditorSample.Length - 1`, then the full clip is selected.
    """
    @property
    def SelectionStartS(self) -> int:
        """
        The starting point of the selection within the editor.
        """
        return 0

    @property
    def SelectionEndS(self) -> int:
        """
        The ending point of the selection within the editor.
        """
        return 0


class Sample:
    """
    Represents an audio clip which can be edited.

    Note that this is different from a sample point, which is a location within
    a sample's waveform at a single instance in time.
    """
    def __init__(self) -> None:
        """
        Create an audio sample
        """

    def GetSampleAt(self, position: int, channel: int) -> float:
        """
        Returns the magnitude of the waveform at position on the given audio
        channel

        ## Args:
        * `position` (`int`): position in the sample

        * `channel` (`int`): audio channel

        ## Returns:
        * `float`: the magnitude at this position
        """
        return 0.0

    def SetSampleAt(self, position: int, channel: int, value: float) -> None:
        """
        Sets the magnitude of the waveform at position on the given audio
        channel

        ## Args:
        * `position` (`int`): position in the sample

        * `channel` (`int`): audio channel

        * `value` (`float`): new magnitude
        """

    def NormalizeFromTo(
        self,
        start: int,
        end: int,
        volume: float,
        only_if_above: bool = False
    ) -> None:
        """
        Normalize the waveform between the `start` and `end` positions
        (inclusive)

        ## Args:
        * `start` (`int`): the starting position

        * `end` (`int`): the ending position

        * `volume` (`float`): ???

        * `only_if_above` (`bool`, optional): ???. Defaults to False
        """

    def AmpFromTo(
        self,
        start: int,
        end: int,
        volume: float,
    ) -> None:
        """
        Amplify the waveform between the `start` and `end` positions
        (inclusive)

        ## Args:
        * `start` (`int`): the starting position

        * `end` (`int`): the ending position

        * `volume` (`float`): the multiplication to apply to each value
        """

    def SilenceFromTo(
        self,
        start: int,
        end: int,
        volume: float,
    ) -> None:
        """
        Silence the waveform between the `start` and `end` positions
        (inclusive).

        This will set the value for each sample point to `0.0`.

        ## Args:
        * `start` (`int`): the starting position

        * `end` (`int`): the ending position
        """

    def DeleteFromTo(self, start: int, end: int) -> None:
        """
        Delete the waveform between the `start` and `end` positions (inclusive)

        ## Args:
        * `start` (`int`): the starting position

        * `end` (`int`): the ending position
        """

    def SineFromTo(
        self,
        start: int,
        end: int,
        frequency: float,
        phase: float,
        volume: float = 1,
    ) -> None:
        """
        Generate a sine wave between the `start` and `end` positions of the
        sample (inclusive).

        ## Args:
        * `start` (`int`): the starting point

        * `end` (`int`): the ending point

        * `frequency` (`float`): the frequency of the sine wave

        * `phase` (`float`): the phase of the sine wave

        * `volume` (`float`, optional): the amplitude of the sine wave.
          Defaults to `1`.
        """

    def LoadFromClipboard(self) -> None:
        """
        Load a sample from the clipboard into this sample object

        This will replace any existing sample
        """

    def PasteFromTo(
        self,
        old: 'Sample',
        start: int,
        end: int,
        mode: Literal[0, 1, 2],
    ) -> None:
        """
        Copy the contents of `old` into this sample.

        ## Args:
        * `old` (`Sample`): The sample to copy from

        * `start` (`int`): the starting point

        * `end` (`int`): the ending point

        * `mode` (`Literal[0, 1, 2]`):

              * `0`: Insert

              * `1`: Replace

              * `2`: Mix
        """

    def MsToSamples(self, time: float) -> int:
        """
        Returns a position within a sample given a time in ms

        ## Args:
        * `time` (`double`): time within the sample

        ## Returns:
        * `int`: position within the sample
        """
        return 0

    def NormalizeFormat(
        self,
        source: 'Sample',
        mode: int = 0b111
    ) -> None:
        """
        Normalize the format of this sample by copying properties from another
        sample to this one

        ## Args:
        * `source` (`Sample`): the source sample to copy from

        * `mode` (`int`, optional): the specific properties to copy. Must be
          some bitwise combination of:

              * `0b001`: number of channels

              * `0b010`: the sample format

              * `0b100`: the sample rate

            Defaults to `0b001 | 0b010 | 0b100`, to copy all properties.
        """

    def GetRegion(self, index: int) -> Region:
        """
        Returns the region within this sample clip at the given index.

        ## Args:
        * `index` (`int`): the index of the region

        ## Returns:
        * `Region`
        """
        return Region()

    @property
    def Length(self) -> int:
        """
        The length of this sample.

        For example, a 48 KHz sample that is 1 second long will have a length
        of `48_000`
        """
        return 0

    # @Length.setter
    # def Length(self, new_value: int) -> None:
    #     pass

    @property
    def NumChans(self) -> int:
        """
        The number of audio channels in this sample.

        For example, stereo audio has 2 channels.
        """
        return 2

    @NumChans.setter
    def NumChans(self, new_value: int) -> None:
        pass

    @property
    def SampleRate(self) -> int:
        """
        The sample rate of this sample.

        For most audio clips, this will be `44_100` for 44.1 KHz.
        """
        return 44_100

    @SampleRate.setter
    def SampleRate(self, new_value: int) -> None:
        pass

    @property
    def RegionCount(self) -> int:
        """
        The number of regions in this sample.

        Regions are specified using the yellow start and end markers in the
        Edison plugin's UI.
        """
        return 0


EditorSample = Sample()
"""
The sample which is currently loaded within the Edison editor.
"""

Editor = MEEditor()
"""
An object representing the state of the Edison editor.

For selections, if the start point is `0` and the end point is
`EditorSample.Length - 1`, then the full clip is selected.
"""
