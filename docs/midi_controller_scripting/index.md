# MIDI Controller Scripting

MIDI Controller Scripting allows native support for **any MIDI controller**.
Scripts are written in the
[Python programming language](https://www.python.org/about/gettingstarted/).
FL Studio executes these scripts, so that they can control FL Studio's
interaction with a MIDI device, meaning that the MIDI controller can access
features of FL Studio, and FL Studio can send back data to the controller to
trigger drum pad lights or show text on a display. The only limitations are
your controller's communication interface and your imagination.

There is no need to install anything to run scripts in FL Studio, as it has a
Python interpreter built-in. However, if you want to benefit from advanced code
editor features when writing your scripts, you may wish to follow the
[installation instructions](../installation.md) to access this documentation
as you write code.

* **Script hierarchy** - As FL Studio natively handles many MIDI functions and
  messages, this allows you to write simple scripts to handle specific cases or
  inputs and leave the rest to FL Studio's generic MIDI support. For example,
  you do not need to tell FL Studio what to do with MIDI notes. If the script
  doesn't specifically make changes to default behavior, FL Studio will handle
  them as normal.

* **Scripts are complex** - With power and flexibility comes complexity. MIDI
  Controller Scripting is intended for hardware manufacturers and advanced
  users to create custom support for MIDI controllers. If you are new to
  programming, MIDI scripting will be confronting and confusing at first. This
  is normal, but patience and persistence will be rewarded! There are some
  simple examples to get started on our user forum listed below.

## MIDI Controller Scripting support forum

FL Studio customers can access the
[MIDI Controller Scripting forum](https://support.image-line.com/redirect/midi_scripting_forum)
to discuss scripting, share scripts, make feature requests and report issues.

## Script locations and file names

FL Studio will check the following locations for MIDI Scripts and related
files:

* **Script files** - Script files are located within the
  [user data folder](https://www.image-line.com/fl-studio-learning/fl-studio-beta-online-manual/html/envsettings_files.htm#userdata)
  under `.../Image-Line/FL Studio/Settings/Hardware/[script_name]/device_[script_name].py`.

  * `[script_name]` - this folder can have any unique name. Normally, you would
    use the name of the MIDI controller you are scripting for.

  * `device_[script_name].py` - this Python file is the entry-point for your
    script. It can have any content, but must begin with `device_` and end with
    `.py`.

  * You can have additional files and directories within your script folder.
    Any additional code you place here can be `import`ed from within your
    script.

* **Launchmap pages** (optional) - Files are located in
  `Image-Line/FL Studio/Settings/Hardware/devicename/Page[number].scr`.

  * **Launchmap files** - Launchmaps are custom files that provide different
    behavior for a controller depending on what mode it is launched in.
    See the MIDI Controller reference post on
    [Custom controller layouts](https://forum.image-line.com/viewtopic.php?f=1914&t=92193)
    as well as the [`launchMapPages` module][launchMapPages].

* **Shared modules** - FL Studio locates custom modules within its installation
  files. It is not recommended to modify this data, as it will be reverted
  with each update to FL Studio.

  * **Windows** - `C:\Program Files\Image-Line\FL Studio [version]\Shared\Python\Lib`

  * **MacOS** - `/Library/Application support/Image-line/Shared/Python/Lib`

## Getting started

Check out the [getting started tutorial](./tutorials/getting_started.md).
