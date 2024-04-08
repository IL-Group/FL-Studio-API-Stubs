"""
# Data / Transdoc Rules

Rule definitions for transdoc
"""
import os


BUILDING_ONLINE_DOCS = os.getenv("DOCS_BUILD_SITE") is not None


BASE_URL = "https://il-group.github.io/FL-Studio-API-Stubs"

OLD_MANUAL_URL = "https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html"


def docs_url_fn(function: str) -> str:
    """
    Return a markdown URL for a function within the API documentation, given
    its name.
    """
    if BUILDING_ONLINE_DOCS:
        module, fn = function.rsplit(".", 1)
        # Use mkdocs internal link
        return f"[`{module}.{fn}()`][{module}.{fn}]"
    else:
        module, fn = function.rsplit(".", 1)
        return f"[{module}.{fn}()]({BASE_URL}/{module}/#{module}.{fn})"


NOTE_MAPPINGS = {
    # Commonly repeated info about colors
    "colors": f"""Note that colors can be split into or built from components using the
    functions provided in the [utils]({BASE_URL}/utils/) module.

    * {docs_url_fn("utils.ColorToRGB")}

    * {docs_url_fn("utils.RGBToColor")}""",

    # Note about playlist indexing
    "playlist_indexes": "Note that playlist track indexes start at 1.",
}


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
    return f"[{text}]({OLD_MANUAL_URL}/midi_scripting.htm#{anchor})"


def fl_manual_page(location: str, text: str = "FL Studio manual") -> str:
    """
    Return a markdown URL for a page within FL Studio's manual.
    """
    return f"[{text}]({OLD_MANUAL_URL}/{location})"


def note(name: str) -> str:
    """
    Insert a note into the documentation given its name.
    """
    return NOTE_MAPPINGS[name]
