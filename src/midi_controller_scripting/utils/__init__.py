"""
# Util

Module included in FL Studio Python lib folder.

Contains useful functions and classes for use when working with FL Studio's
Python API.

## Note

This code is taken from FL Studio's Python lib folder and included in this
package in the hope that it will be useful for script developers. It is not the
creation of the repository authors, and no credit is claimed for the code
content. However, the documentation for the provided code is created by the
authors of this repository.

## WARNING

Many of the provided functions in the FL Studio installation have bugs
that may result in unexpected behavior. These bugs have been left as-is in this
file for your inspection and warnings have been added to the docstrings. Use
any functions here with caution.
"""
__all__ = [
    'TRect',
    'TClipLauncherLastClip',
    'RectOverlapEqual',
    'RectOverlap',
    'Limited',
    'InterNoSwap',
    'DivModU',
    'SwapInt',
    'Zeros',
    'Zeros_Strict',
    'Sign',
    'SignBitPos_64',
    'SignBit_64',
    'SignBitPos_Nat',
    'SignOf',
    'KnobAccelToRes2',
    'OffsetRect',
    'RGBToHSV',
    'RGBToHSVColor',
    'HSVtoRGB',
    'NoteNameT',
    'GetNoteName',
    'ColorToRGB',
    'RGBToColor',
    'FadeColor',
    'LightenColor',
    'VolTodB',
]


from .__utils import (
    TRect,
    TClipLauncherLastClip,
    RectOverlapEqual,
    RectOverlap,
    Limited,
    InterNoSwap,
    DivModU,
    SwapInt,
    Zeros,
    Zeros_Strict,
    Sign,
    SignBitPos_64,
    SignBit_64,
    SignBitPos_Nat,
    SignOf,
    KnobAccelToRes2,
    OffsetRect,
    RGBToHSV,
    RGBToHSVColor,
    HSVtoRGB,
    NoteNameT,
    GetNoteName,
    ColorToRGB,
    RGBToColor,
    FadeColor,
    LightenColor,
    VolTodB,
)
