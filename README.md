# FL Studio Python API Stubs

This repository contains stub code for functions and classes used in FL
Studio's Python API. This includes modules used within:

* [MIDI Controller Scripting](https://www.image-line.com/fl-studio-learning/fl-studio-beta-online-manual/html/midi_scripting.htm)
* [Edison Audio Scripting](https://www.image-line.com/fl-studio-learning/fl-studio-beta-online-manual/html/pianoroll_scripting_api.htm)
* [Piano Roll Scripting](https://www.image-line.com/fl-studio-learning/fl-studio-beta-online-manual/html/plugins/editortool_run.htm)

## Usage

This documentation can be viewed online (TODO: link), or accessed by installing
the package from Python's package manager Pip.

For instructions, please visit the documentation website.

## Contributing

We'd love to have your help maintaining this project.

### Feature requests and bugs

If you'd like to report a bug in FL Studio, or get new features added to FL
Studio's Python API, please create a post on the Image-Line forum. The issues
tab for this repository should only be used for reporting issues with the
stub code.

### Issues with the API

If you've spotted an issue with the API documentation or stub code, please
open an issue and we'll get it fixed up as soon as we can. In particular,
we're on the look out for:

* Incorrect type definitions
* Missing functions or constants
* Confusing, missing or poorly-formatted documentation

### Setting up a development environment

Dependencies for this project are managed using
[Poetry](https://python-poetry.org/). You'll need to
[install Poetry](https://python-poetry.org/docs/#installation) to contribute to
the project.

To install dependencies for the project:

```sh
# Install dependencies for the project
poetry install --no-root
# Run the pre-build script
poetry run python -m scripts.build_lib
# Install the library
poetry install
```

Whenever you modify documentation, you will need to rerun the pre-build script
for your changes to be persisted.

### Developing the documentation site

You can trigger a build of the documentation site by running:

```sh
poetry run python -m scripts.build_docs
```

If you are using the [VS Code](https://code.visualstudio.com/) text editor,
we recommend using the [Live Server Extension](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)
to serve the documentation site, since it automatically refreshes the page
whenever you run the build command.

### Understanding the repository layout

In order to ensure that the documentation is of the highest quality, both
online and in library form, the layout is a little complex.

* `src/` contains the source code for all included modules, divided up based on
  whether they are a component of MIDI Controller Scripting, Edison Scripting,
  or Piano Roll Scripting. Each Python file contains function definitions, with
  [docstrings](https://peps.python.org/pep-0257/) showing their behaviour.

* `docs/` contains Markdown files and other assets used when building the
  online documentation. This is merged with the layout of `src/` when building
  documentation, so the resultant site ends up containing the documentation
  from both directories.

* `scripts/` contains Python scripts for performing common actions such as
  building the documentation or building the package.

* `data/` contains other assets used by the repository, such as
  [Transdoc](https://github.com/MiguelGuthridge/transdoc) rule definitions, and
  docstring templates.
