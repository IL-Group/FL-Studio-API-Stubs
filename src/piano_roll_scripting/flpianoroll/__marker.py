"""
flpianoroll > marker

Marker class definition
"""


class Marker:
    """
    Represents a marker in the FL Studio piano roll.
    """
    def __init__(self) -> None:
        pass

    @property
    def time(self) -> int:
        """
        Time at which the marker is placed (in ticks).
        """
        return 0

    @time.setter
    def time(self, new_value: int) -> None:
        pass

    @property
    def name(self) -> str:
        """
        Name of the marker.

        Note that for markers that have an associated action, this won't be
        displayed to the user.
        """
        return "Marker"

    @name.setter
    def name(self, new_value: str) -> None:
        pass

    @property
    def mode(self) -> int:
        """
        Action associated with the marker.

        ## Possible values

        * `0`: no action.

        * `6`: pattern length.

        * `8`: time signature (numerator and denominator can be accessed from
          properties `tsnum` and `tsden`, respectively).

        * `9`: start recording.

        * `10`: stop recording.

        * `12`: key/scale (key and scale helper can be accessed from properties
          `scale_root` and `scale_helper`, respectively).
        """
        return 0

    @mode.setter
    def mode(self, new_value: int) -> None:
        pass

    @property
    def tsnum(self) -> int:
        """
        Numerator of a time signature marker.
        """
        return 0

    @tsnum.setter
    def tsnum(self, new_value: int) -> None:
        pass

    @property
    def tsden(self) -> int:
        """
        Denominator of a time signature marker.
        """
        return 0

    @tsden.setter
    def tsden(self, new_value: int) -> None:
        pass

    @property
    def scale_root(self) -> int:
        """
        Root note of the scale of a key/scale marker, where C is note `0`.
        """
        return 0

    @scale_root.setter
    def scale_root(self, new_value: int) -> None:
        pass

    @property
    def scale_helper(self) -> str:
        """
        Notes that are highlighted in the piano roll, as a comma-separated list
        of boolean integers.

        For example, if C, D and Eb were highlighted, the elements would be:

        ```py
        >>> marker.scale_helper
        '1,0,1,1,0,0,0,0,0,0,0,0'
        ```

        To parse this into a more Pythonic form, you could use the following
        code:

        ```py
        >>> [n == '1' for n in marker.scale_helper.split(',')]
        [True, False, True, True, False, False, False, False, False, False, False, False]
        ```

        To assign this value in a more pythonic form, you could use the
        following code:

        ```py
        >>> scale = [True, False, True, True, False, False, False, False, False, False, False, False]
        >>> marker.scale_helper = ",".join(str(int(v)) for v in scale)
        ```
        """
        return ""

    @scale_helper.setter
    def scale_helper(self, new_value: str) -> None:
        pass
