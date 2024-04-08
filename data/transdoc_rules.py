"""
# Data / Transdoc Rules

Rule definitions for transdoc
"""

BASE_URL = "https://miguelguthridge.github.io/FL-Studio-API-Stubs"

FL_MANUAL_URL = "https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html"

NOTE_MAPPINGS = {
    "colors": """Note that colors can be split into or built from components using the
    functions provided in the [utils](https://miguelguthridge.github.io/FL-Studio-API-Stubs/utils/) module.

    * [ColorToRGB()](https://miguelguthridge.github.io/FL-Studio-API-Stubs/utils/#utils.ColorToRGB)

    * [RGBToColor()](https://miguelguthridge.github.io/FL-Studio-API-Stubs/utils/#utils.RGBToColor)""",

    "playlist_indexes": "Note that playlist track indexes start at 1.",
}


def docs_url_fn(function: str) -> str:
    """
    Return a markdown URL for a function within the API documentation, given
    its name.
    """
    module, fn = function.rsplit(".", 1)
    return f"[{module}.{fn}()]({BASE_URL}/{module}/#{module}.{fn})"

    # Or for the online site:
    # return f"[`{function}()`][{function}]"


def docs_url_page(text: str, location: str) -> str:
    """
    Return a markdown URL for a page in the API documentation.
    """
    return f"[{text}]({BASE_URL}/{location})"


def fl_manual_anchor(anchor: str, text: str = "FL Studio manual") -> str:
    """
    Return a markdown URL for a location anchored within the MIDI scripting
    page of FL Studio's manual.
    """
    return f"[{text}]({FL_MANUAL_URL}/midi_scripting.htm#{anchor})"


def fl_manual_page(location: str, text: str = "FL Studio manual") -> str:
    """
    Return a markdown URL for a page within FL Studio's manual.
    """
    return f"[{text}]({FL_MANUAL_URL}/{location})"


def note(name: str) -> str:
    """
    Insert a note given its name.
    """
    return NOTE_MAPPINGS[name]
