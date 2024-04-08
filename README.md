# FL Studio Python API Stubs

This repository contains stub code for functions and classes used in FL
Studio's Python API. This includes modules used within:

* [MIDI Controller Scripting](https://www.image-line.com/fl-studio-learning/fl-studio-beta-online-manual/html/midi_scripting.htm)
* [Edison Audio Scripting](https://www.image-line.com/fl-studio-learning/fl-studio-beta-online-manual/html/pianoroll_scripting_api.htm)
* [Piano Roll Scripting](https://www.image-line.com/fl-studio-learning/fl-studio-beta-online-manual/html/plugins/editortool_run.htm)

## Usage

This documentation can be viewed online (TODO: link), or accessed by installing
the package from Python's package manager Pip.

### Installing the package

To avoid module conflicts with other Python projects, it is recommended that
you install this script in a virtual environment by following
[these instructions](https://docs.python.org/3/library/venv.html) in the
official Python documentation.

After activating the environment in your terminal, you can install the stub
modules by running the command `pip install fl-studio-api-stubs` on Windows or
`pip3 install fl-studio-api-stubs` on MacOS or Linux.

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
