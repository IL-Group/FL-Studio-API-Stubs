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
[installation instructions](../library.md) to access this documentation
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

## Getting started

Check out the [getting started tutorial](./tutorials/getting_started.md).

## Basic information

* [Script locations and file names](./script_files.md)

* [Script metadata](./script_metadata.md)

* [Callbacks](./callbacks/)

* [Objects used within MIDI Controller Scripting](./fl_classes/)

## API modules

These are Python modules that are built into FL Studio.

* [`arrangement`][arrangement]

* [`channels`][channels]

* [`device`][device]

* [`general`][general]

* [`launchMapPages`][launchMapPages]

* [`mixer`][mixer]

* [`patterns`][patterns]

* [`playlist`][playlist]

* [`plugins`][plugins]

* [`screen`][screen]

* [`transport`][transport]

* [`ui`][ui]

## Extra modules

These are Python files stored within FL Studio's Python library directory.

* [`midi`][midi]

* [`utils`][utils]
