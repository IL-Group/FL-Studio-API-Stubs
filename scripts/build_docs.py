"""
# Scripts / Build Docs

Script for building the documentation site using mkdocs.

1. Transform docstrings from `src/` to `prebuild_docs/`.
2. Generate template files for `mkdocstrings` to fill in documentation from the
   Python library.
3. Copy in human-written documentation from `docs/` so it gets included in the
   site.
4. Run `mkdocs` to create the HTML page
5. Move the output file into the `site/` directory.

Author: Miguel Guthridge
Date: 2024-04-08
"""
import os
import sys
from pathlib import Path
from shutil import rmtree, copytree, move

from mkdocs.commands.build import build as mkdocs_build
from mkdocs.config import load_config
from transdoc import main as transdoc_main


TRANSDOC_INPUT = Path("src")
"""
Input dir for transdoc
"""

TRANSDOC_RULES = Path("data/transdoc_rules.py")
"""
Rule files for transdoc
"""
DOCS_PREBUILD_DIR = Path("prebuild_docs")
"""
Directory where project source was transformed in preparation for building
documentation.
"""

MD_DOCS_DIR = Path("docs")
"""
Directory where human-written markdown docs are located.
"""

DOCS_BUILD_DIR = Path("build_docs")
"""
Directory where documentation markdown is generated, built by merging
human-written content with the generated files.
"""

AUTO_DOCSTRINGS_SKIPPED = [
    "enveditor",
    "flpianoroll",
]
"""
Modules to skip when generating auto-docstrings

These modules have the documentation written for them manually.
"""

TEMP_SITE_OUTPUT = Path("temp_site")
"""
Location that mkdocs generates the site in
"""

FINAL_OUTPUT = Path("site")
"""
Final output location for the script
"""


FileTree = dict[str, 'FileTree']
"""
Tree of files.

Leaves (files) have value `None`, and directories are another `FileTree`.
"""


def py_path_to_md(path: Path) -> Path:
    """
    Transform a Python filename into a Markdown filename.

    ## Examples

    * `__example.py` -> `Example.md`
    * `__script_dialog.py` -> `Script Dialog.md`
    """
    return path \
        .with_name(path.name.replace('_', ' ').strip()) \
        .with_suffix(".md")


def generate_module_tree(
    tree: FileTree,
    mod_path: Path,
    input_base: Path,
    output_base: Path,
):
    """
    Generate Markdown template for a tree of modules.

    These will be used by mkdocstrings to get documentation for the functions
    from the source code transpiled to `prebuild_docs/`.
    """

    # We need to import this here, otherwise it kinda dies a little, likely
    # due to us nuking and recreating the old `build_docs` dir in
    # `generate_auto_docstrings`
    import mkdocs_gen_files  # type: ignore

    # If it's a file, write its output
    if (input_base / mod_path).is_file():
        output_file = py_path_to_md(output_base / mod_path)
        with mkdocs_gen_files.open(output_file, "w") as f:
            identifier = ".".join(mod_path.with_suffix("").parts)
            print(f"::: {identifier}", file=f)

    # Otherwise, it's a directory
    else:
        # Now write the `.pages` and `index.md` files, only if we're in a
        # module
        if mod_path != Path(""):
            # Create a `.pages` config to manage navigation in this directory
            with mkdocs_gen_files.open(
                output_base / mod_path / ".pages",
                "w",
            ) as f:
                print("nav:", file=f)
                # Put index.md at the top
                print(f"  - {mod_path.name.capitalize()}: index.md", file=f)
                print("  - ...", file=f)

            # index.md
            with mkdocs_gen_files.open(
                output_base / mod_path / "index.md",
                "w",
            ) as f:
                identifier = ".".join(mod_path.with_suffix("").parts)
                print(f"::: {identifier}", file=f)
                # If there are files here, we should exclude function
                # definitions from the main page, since they'll be in sub-pages
                if len(tree):
                    print("    options:", file=f)
                    print("      members: no", file=f)

        # Now write contents for all remaining contents in the directory
        for node, sub_tree in tree.items():
            generate_module_tree(
                sub_tree,
                mod_path / node,
                input_base,
                output_base,
            )


def add_path_to_tree(tree: FileTree, path: Path):
    """
    Add a path to the file tree.
    """
    if len(path.parts) == 1:
        if str(path) not in tree:
            tree[str(path)] = {}
    else:
        part = path.parts[0]
        if part not in tree:
            tree[part] = {}
        branch = tree[part]
        add_path_to_tree(branch, Path(*path.parts[1:]))


def generate_auto_docstrings():
    """
    Generate audo-docstring markdown files for all Python modules in the
    project.
    """
    # Remove the old build_docs directory
    rmtree(DOCS_BUILD_DIR, ignore_errors=True)
    DOCS_BUILD_DIR.mkdir()

    module_tree: FileTree = {}

    # Find all the modules in the library
    for path in DOCS_PREBUILD_DIR.rglob("*.py"):
        # So that files can be grouped, we find all Python files
        module = Path(path.relative_to(DOCS_PREBUILD_DIR))

        # only include it if it's not part of our modules to skip
        if not any(part in AUTO_DOCSTRINGS_SKIPPED for part in module.parts):
            # Skip over __init__.py, since it gets covered by parent directories
            if module.name == "__init__.py":
                add_path_to_tree(module_tree, module.parent)
            else:
                add_path_to_tree(module_tree, module)

    # Now generate each module
    # Place all contents in
    generate_module_tree(
        module_tree,
        Path(""),
        DOCS_PREBUILD_DIR,
        # FIXME: Don't hard-code this
        Path("MIDI Controller Scripting"),
    )


def find_duplicates(src: Path, dest: Path) -> list[Path]:
    """
    Returns a list of files that would be overwritten when merging files

    ## Args:

    * `src` (`Path`): directory containing files to merge
    * `dest` (`Path`): directory where files will be merged into
    """
    duplicates = []
    for root, dirs, files in os.walk(src):
        root_path = Path(root)
        dest_root = dest.joinpath(root_path.relative_to(src))
        # print(f"Root: {root} -> {dest_root}")
        for file in files:
            # print(f"{root.joinpath(file)} -> {dest_root.joinpath(file)}")
            file_path = dest_root.joinpath(file)
            if file_path.exists():
                duplicates.append(file_path)

    return duplicates


def merge_human_docs():
    """
    Merge the documentation written by humans into the final build directory.
    """
    duplicates = find_duplicates(MD_DOCS_DIR, DOCS_BUILD_DIR)
    if len(duplicates):
        print(
            "Unable to generate docs, files would be overwritten",
            file=sys.stderr,
        )
        for dup in duplicates:
            print(f"- {dup}", file=sys.stderr)
        exit(1)

    # If we reached this point, it is safe to merge
    copytree(MD_DOCS_DIR, DOCS_BUILD_DIR, dirs_exist_ok=True)


def main():
    """
    Main entrypoint of the build_docs script.
    """
    # Set the DOCS_BUILD_SITE environment variable, which is detected by our
    # rules in `data/transdoc_rules.py` in order to generate better links for
    # the site
    os.environ["DOCS_BUILD_SITE"] = "TRUE"
    # Run transdoc compilation
    transdoc_main(
        TRANSDOC_INPUT,
        TRANSDOC_RULES,
        DOCS_PREBUILD_DIR,
        force=True,
    )

    # Generate auto-docstrings
    generate_auto_docstrings()

    # Merge in hand-written documentation
    merge_human_docs()

    # Run mkdocs to generate our HTML site
    config = load_config()
    mkdocs_build(config)

    # If site output doesn't exist, mkdocs probably failed
    assert TEMP_SITE_OUTPUT.is_dir()
    # FIXME: This sometimes causes a 404 when using the Live Server extension
    # -- we should consider overwriting the files one by one instead.
    rmtree(FINAL_OUTPUT, ignore_errors=True)
    move(TEMP_SITE_OUTPUT, FINAL_OUTPUT)


if __name__ == "__main__":
    main()
