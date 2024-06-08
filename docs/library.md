# Using the FL Studio Python API Stubs as a library

This documentation can be accessed from your development environment by
installing it as a Python package. Doing this will allow your IDE to provide
inline documentation for all of FL Studio's documentation, as well as allowing
your projects to be statically analyzed using type-checking tools such as
[mypy](https://mypy.readthedocs.io/en/stable/).

## Installing the library

### Windows

1. Install Python from [python.org](https://www.python.org/downloads/)

2. Install the FL Studio API Stubs by running `pip install fl-studio-api-stubs`

## MacOS

1. Ensure you have the Pip package manager installed by running
   `python3 -m ensurepip --upgrade`

2. Install the FL Studio API Stubs by running
   `pip3 install fl-studio-api-stubs`

### Project dependency management

If you work on other Python projects, it could be worthwhile using a project
dependency manager such as [Poetry](https://python-poetry.org/) or
[Hatch](https://hatch.pypa.io/latest/). This will ensure that your project's
dependencies don't conflict with your other work.

Using a [virtual environment](https://docs.python.org/3/library/venv.html) will
also work, but is comparatively simplistic, and may cause issues if used for
more complex projects.

## Getting inline suggestions with VS Code

1. Open your project folder in VS Code.
2. Select the Python environment (venv, Poetry environment, etc) in which you
   installed `fl-studio-api-stubs`. If you're unsure, skip this step.
3. Any imports from modules provided by the API stubs will have full
   documentation and type definitions.

## Type safety using mypy

[Mypy](https://mypy.readthedocs.io/en/stable/) is a static analysis tool that
can detect type safety issues such as incorrect function calls. The FL Studio
API Stubs support `mypy` out-of-the-box, but to get the highest level of type
safety, you may need to configure your project.

It is recommended to tell `mypy` to check untyped functions. This way, you it
can check for incorrect calls to API functions. To do this, create a `mypy.ini`
file within your project directory with these contents.

```ini
[mypy]
check_untyped_defs = True
```

After installing `mypy` (`pip install mypy` on Windows, `pip3 install mypy` on
MacOS), Mypy will be able to check your project. You can then type check your
project by running `mypy .` in your project directory.

### Type checking `.pyscript` files

By default, mypy won't perform type-checking on files with the `.pyscript`
files. To get type checking on these, you can add this line to your `mypy.ini`:

```ini
files = **/*.py, **/*.pyscript
```

This will make `mypy` check all files ending with `.py` and `.pyscript`. Note
that if there are files you don't want to include, you may need to modify the
[glob patterns](https://docs.python.org/3/library/glob.html) as required.
