"""
# Scripts / transform docstrings

Transform docstrings to make them render more nicely inline, and online.
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
