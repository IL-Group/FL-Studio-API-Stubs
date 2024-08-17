"""
# Data / Transdoc Rules

Rule definitions for transdoc.
"""
import sys
import os
from typing import Any, cast
import griffe
from griffe import Kind
from scripts.consts import MODULES, PATHS_TO_MODULES


# Add `src/*` to PATH so that building doesn't fail
sys.path.extend([
    'src/edison_scripting',
    'src/midi_controller_scripting',
    'src/piano_roll_scripting',
])


# Load griffe definitions for all modules
module_info: dict[str, dict[str, Any]] = {}
for mod in MODULES:
    loaded_mod = griffe.load(mod, resolve_aliases=True, resolve_external=True)
    module_info[mod] = loaded_mod.as_dict()


BUILDING_ONLINE_DOCS = os.getenv("DOCS_BUILD_SITE") is not None


BASE_URL = "https://il-group.github.io/FL-Studio-API-Stubs"

OLD_MANUAL_URL = "https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html"


def get_item_docs_url(module: str, name: str) -> Any:
    """
    Use Griffe to find the documentation URL for the given item.
    """
    mod_info = module_info[module]

    for item in mod_info["members"]:
        if item["name"] == name:
            if item["kind"] == Kind.ALIAS:
                path: list[str] = []
                for dir in cast(str, item["target_path"].split('.')[:-1]):
                    path.append(dir.removeprefix('__'))
                anchor = item["target_path"]
            else:
                # It's probably at the top of the module
                path = [module]
                anchor = f"{module}.{name}"
            return (
                f"{BASE_URL}/{PATHS_TO_MODULES[module]}"
                f"/{'/'.join(path)}"
                f"#{anchor}"
            )

    raise NameError(f"Griffe definition not found: '{module}.{name}'")


def docs_url_mod(module: str) -> str:
    """
    Return a markdown URL for a module within the API documentation, given its
    name.
    """
    if BUILDING_ONLINE_DOCS:
        # Use mkdocs internal link
        return f"[`{module}`][{module}]"
    else:
        return f"[{module}]({BASE_URL}/{PATHS_TO_MODULES[module]}/{module})"


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
        module, fn = function.rsplit(".", 1)
        return f"[{module}.{fn}{suffix}]({get_item_docs_url(module, fn)})"


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
        module, fn = attribute.rsplit(".", 1)
        return f"[{module}.{fn}{suffix}]({get_item_docs_url(module, fn)})"


NOTE_MAPPINGS = {
    # Commonly repeated info about colors
    "colors": f"""Note that colors can be split into or built from components using the
functions provided in the {docs_url_mod("utils")} module.

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
