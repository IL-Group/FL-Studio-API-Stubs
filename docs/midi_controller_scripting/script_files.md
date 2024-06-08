# Script locations and file names

Script files are located within the [user data folder](https://www.image-line.com/fl-studio-learning/fl-studio-beta-online-manual/html/envsettings_files.htm#userdata)
under `.../Image-Line/FL Studio/Settings/Hardware/[script_name]`, where
`[script_name]` is a folder with a unique name. This folder should contain all
resources required to run the script, including:

* `device_[script_name].py` - this Python file is the entry-point for your
  script. It can have any content, but must begin with `device_` and end with
  `.py`.

* [Launchmap files][launchMapPages], stored as `Page[number].src`, where number
  is a positive integer.

* Additional Python files. Since each script has it's base directory added to
  its `PYTHONPATH`, any additional modules can be `import`ed from within your
  script with ease.

* Any additional resources, such as a `README.md` or a `LICENSE.txt`.
