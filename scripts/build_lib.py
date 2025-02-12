"""
# Scripts / Build Lib

Transform docstrings as a pre-build step. This uses `transdoc` to rewrite
docstrings

Author: Maddy Guthridge
Date: 2024-04-07
"""

from pathlib import Path
import transdoc


INPUT = Path("src")
RULES = Path("data/transdoc_rules.py")
OUTPUT = Path("build_lib")


def main():
    try:
        transdoc.transform_tree(
            transdoc.get_all_handlers(),
            transdoc.TransdocTransformer.from_file(RULES),
            INPUT,
            OUTPUT,
            force=True,
        )
    except ExceptionGroup as e:
        transdoc.util.print_error(e)
        return 1
    return 0


if __name__ == "__main__":
    exit(main())
