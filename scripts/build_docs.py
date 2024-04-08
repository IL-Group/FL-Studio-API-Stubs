from .generate_pages import generate
from mkdocs.commands.build import build as mkdocs_build
from mkdocs.config import load_config
from pathlib import Path
from shutil import rmtree, move


def main():
    # transform_modules()
    generate()
    config = load_config()
    mkdocs_build(config)
    temp_dir = Path('temp_site')
    assert temp_dir.is_dir()
    rmtree('site', ignore_errors=True)
    move(temp_dir, 'site')


if __name__ == "__main__":
    main()
