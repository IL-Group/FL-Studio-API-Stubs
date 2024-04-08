"""
# Scripts / Build Lib

Transform docstrings as a pre-build step. This uses `transdoc` to rewrite
docstrings

Author: Miguel Guthridge
Date: 2024-04-07
"""
from pathlib import Path
from transdoc import main as transdoc_main


INPUT = Path("src")
RULES = Path("data/transdoc_rules.py")
OUTPUT = Path("build_lib")


def main():
    return transdoc_main(INPUT, RULES, OUTPUT, force=True)


if __name__ == '__main__':
    exit(main())
