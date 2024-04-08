from .generate_pages import generate
from mkdocs.commands.build import build as mkdocs_build
from mkdocs.config import load_config
from pathlib import Path
from shutil import rmtree, move
from transdoc import main as transdoc_main
import os


INPUT = Path("src")
RULES = Path("data/transdoc_rules.py")
OUTPUT = Path("prebuild_docs")


def main():
    os.environ["DOCS_BUILD_ONLINE"] = "TRUE"
    transdoc_main(INPUT, RULES, OUTPUT, force=True)
    generate()
    config = load_config()
    mkdocs_build(config)
    temp_dir = Path('temp_site')
    assert temp_dir.is_dir()
    # FIXME: This sometimes causes a 404 when using the Live Server extension
    # -- we should overwrite the files one by one instead.
    rmtree('site', ignore_errors=True)
    move(temp_dir, 'site')


if __name__ == "__main__":
    main()
