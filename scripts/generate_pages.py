import os
from pathlib import Path
from shutil import copytree, rmtree

DOC_BUILD_DIR = Path("build_docs")
"""Directory where documentation is built"""
MD_DOCS_DIR = Path("docs")
"""Directory where markdown docs are located"""


# Documentation for these modules is written manually
SKIPPED_MODULES = [
    "enveditor",
    "flpianoroll"
]


def generate():
    # Remove the old build_docs directory
    rmtree(DOC_BUILD_DIR, ignore_errors=True)
    DOC_BUILD_DIR.mkdir()

    # We need to import this here, otherwise it kinda dies a little
    import mkdocs_gen_files  # type: ignore

    src = Path("src")
    modules = []

    # Get all modules in the src directory
    for path in src.rglob("*.py"):
        # Get the parent directory of the Python files, which returns the module itself rather than specific files
        module = Path(path.relative_to(src)).parent
        # Make sure no duplicate modules are added
        if module not in modules:
            modules.append(module)

    for module in modules:
        # For modules we're documenting manually
        if str(module) in SKIPPED_MODULES:
            continue
        # If there are any modules with submodules, make sure we generate an index page for that module instead of a separate page, then append the markdown file extension
        module_path = (Path(module, "index")
                       if any(m.parent == module for m in modules)
                       else module
                       ).with_suffix(".md")
        with mkdocs_gen_files.open(module_path, "w") as f:
            # Change module path to a dot-separated identifier for mkdocs-gen-files and generate that page
            identifier = ".".join(module.parts)
            print(f"::: {identifier}", file=f)

    def find_duplicates(src: Path, dest: Path) -> list[Path]:
        """
        Returns a list of files that would be overwritten when merging files
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

    duplicates = find_duplicates(MD_DOCS_DIR, DOC_BUILD_DIR)
    if len(duplicates):
        print("Unable to generate docs, files would be overwritten")
        for dup in duplicates:
            print(f"- {dup}")
        exit(1)

    # Now go and merge in the docs directory
    copytree(MD_DOCS_DIR, DOC_BUILD_DIR, dirs_exist_ok=True)


if __name__ == "__main__":
    generate()
