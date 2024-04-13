"""
# Mixer / EQ

Functions for interacting with the FL Studio mixer's built-in EQ.
"""


def getEqBandCount() -> int:
    """
    Returns the number of bands in the built-in EQ.

    Whilst this value will always be 3 for current FL Studio versions, it is
    recommended to use this function rather than hard-coding a value to allow
    for better future-proofing.

    ## Returns

    * `int`: number of mixer bands

    Included since API Version 35
    """
    return 0


def getEqGain(index: int, band: int, mode: int = 0) -> float:
    """
    Returns the gain of the given band on the given track for the built-in EQ.

    Setting `mode=1` will return the gain in decibels rather than as a
    normalized value from `0.0` to `1.0`.

    ## Args

    * `index` (`int`): mixer track index

    * `band` (`int`): EQ band

    * `mode` (`int`, optional): units to return value in. Defaults to `0`.

    ## Returns

    * `float`: EQ band gain

    Included since API Version 35
    """
    return 0.0


def setEqGain(index: int, band: int, value: float) -> None:
    """
    Sets the gain of the given band on the given track for the built-in EQ.

    ## Args

    * `index` (`int`): mixer track index

    * `band` (`int`): EQ band

    * `value` (`float`): new gain, as a normalized value between `0.0` and
      `1.0`.

    Included since API Version 35
    """


def getEqFrequency(index: int, band: int, mode: int = 0) -> float:
    """
    Returns the frequency of the given band on the given track for the built-in
    EQ.

    Setting `mode=1` will return the frequency in Hz rather than as a
    normalized value from `0.0` to `1.0`.

    ## Args

    * `index` (`int`): mixer track index

    * `band` (`int`): EQ band

    * `mode` (`int`, optional): units to return value in. Defaults to `0`.

    ## Returns

    * `float`: EQ band frequency

    Included since API Version 35
    """
    return 0.0


def setEqFrequency(index: int, band: int, value: float) -> None:
    """
    Sets the frequency of the given band on the given track for the built-in
    EQ.

    ## Args

    * `index` (`int`): mixer track index

    * `band` (`int`): EQ band

    * `value` (`float`): new frequency, as a normalized value between `0.0` and
      `1.0`.

    Included since API Version 35
    """


def getEqBandwidth(index: int, band: int) -> float:
    """
    Returns the bandwidth of the given band on the given track for the built-in
    EQ.

    ## Args

    * `index` (`int`): mixer track index

    * `band` (`int`): EQ band

    ## Returns

    * `float`: EQ bandwidth

    Included since API Version 35
    """
    return 0.0


def setEqBandwidth(index: int, band: int, value: float) -> None:
    """
    Sets the bandwidth of the given band on the given track for the built-in
    EQ.

    ## Args

    * `index` (`int`): mixer track index

    * `band` (`int`): EQ band

    * `value` (`float`): new bandwidth, as a normalized value between `0.0` and
      `1.0`.

    Included since API Version 35
    """
