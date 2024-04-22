"""
# Data / Transdoc Rules

Rule definitions for transdoc
"""
import os


BUILDING_ONLINE_DOCS = os.getenv("DOCS_BUILD_SITE") is not None


BASE_URL = "https://il-group.github.io/FL-Studio-API-Stubs"

OLD_MANUAL_URL = "https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html"


def docs_url_mod(module: str) -> str:
    """
    Return a markdown URL for a module within the API documentation, given its
    name.
    """
    if BUILDING_ONLINE_DOCS:
        # Use mkdocs internal link
        return f"[`{module}`][{module}]"
    else:
        # FIXME: These won't link correctly due to new documentation structure
        return f"[{module}]({BASE_URL}/{module})"


def docs_url_fn(function: str, suffix: str = "()") -> str:
    """
    Return a markdown URL for a function within the API documentation, given
    its name.

    ## Args

    * `function` (`str`): function to link to

    * `suffix` (`str`, optional): suffix to use in the text representation.
    """
    if BUILDING_ONLINE_DOCS:
        module, fn = function.rsplit(".", 1)
        # Use mkdocs internal link
        return f"[`{module}.{fn}{suffix}`][{module}.{fn}]"
    else:
        # FIXME: These won't link correctly due to new documentation structure
        module, fn = function.rsplit(".", 1)
        return f"[{module}.{fn}{suffix}]({BASE_URL}/{module}/#{module}.{fn})"


def docs_url_attr(attribute: str, suffix: str = "") -> str:
    """
    Return a markdown URL for an attribute within the API documentation, given
    its name.

    ## Args

    * `attribute` (`str`): attribute to link to

    * `suffix` (`str`, optional): suffix to use in the text representation.
    """
    if BUILDING_ONLINE_DOCS:
        module, fn = attribute.rsplit(".", 1)
        # Use mkdocs internal link
        return f"[`{module}.{fn}{suffix}`][{module}.{fn}]"
    else:
        # FIXME: These won't link correctly due to new documentation structure
        module, fn = attribute.rsplit(".", 1)
        return f"[{module}.{fn}{suffix}]({BASE_URL}/{module}/#{module}.{fn})"


def docs_url_callback(callback: str) -> str:
    """
    Returns a markdown URL for a callback function within the API
    documentation, given its name.

    ## Args

    * `callback` (`str`): callback function to link to.
    """
    return f"`{callback}`"


NOTE_MAPPINGS = {
    # Commonly repeated info about colors
    "colors": f"""Note that colors can be split into or built from components using the
    functions provided in the [utils]({BASE_URL}/utils/) module.

    * {docs_url_fn("utils.ColorToRGB")}

    * {docs_url_fn("utils.RGBToColor")}""",

    # Note about playlist indexing
    "playlist_indexes": "Note that playlist track indexes start at 1.",
}


def module_title(text: str | list[str]) -> str:
    """
    Renders a nice-looking Markdown title for the given module, but only if
    we're not rendering online documentation (since mkdocs adds it for us).
    """
    if BUILDING_ONLINE_DOCS:
        return ""

    if isinstance(text, str):
        return f"# {text.capitalize()}"
    else:
        return "# " + " / ".join(text)


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


def md_table(table: list[list[str]]) -> str:
    """
    Generate a markdown table if rendering HTML documentation. Otherwise,
    generate bullet points, since VS Code doesn't render markdown tables
    nicely.
    """
    header = table.pop(0)

    # # Tables don't actually render nicely for the online docs either :(
    # if BUILDING_ONLINE_DOCS:
    #     output = f"|{'|'.join(header)}|\n|{'===|' * len(header)}\n"
    #
    #     for line in table:
    #         output += f"|{'|'.join(line)}|\n"
    #
    #     return output
    #
    # else:
    output = ""

    for line in table:
        output_line = ""
        for i, item in enumerate(line):
            output_line += f"{header[i]}: {item}, "

        output += f"* {output_line.removesuffix(', ')}\n"

    return output.strip()
