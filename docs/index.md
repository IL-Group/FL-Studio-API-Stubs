<h1>FL Studio API Documentation</h1>

This is user-written documentation for FL Studio's Python API. It contains information on how to use the API to interact with FL Studio. As well as this, it is also available as an [installable package](https://github.com/MiguelGuthridge/FL-Studio-API-Stubs#installation), which allows you to write code for FL Studio with the help of smart suggestions and inline documentation. Both the online documentation and the installable package use the same definitions, meaning that they share the same detailed and helpful information.

If you wish to help contribute to this documentation, you can do so by creating a pull request to [the repository](https://github.com/MiguelGuthridge/FL-Studio-API-Stubs). If you find any errors or omissions, please create an issue on the repository.

## List of modules

### MIDI controller scripting

* [`arrangement`][arrangement]: functions for interacting with individual arrangements,
  including markers and playlist selections.
* [`channels`][channels]: functions for interacting with the channel rack and its channels.
* [`device`][device]: functions for interacting with the device hardware, as well as
  tools for managing rec events.
* [`general`][general]: miscellaneous functions for interacting with FL Studio.
* [`launchMapPages`][launchMapPages]: functions for implementing page displays on some MIDI
  controllers.
* [`mixer`][mixer]: functions for interacting with the mixer and its tracks.
* [`patterns`][patterns]: functions for interacting with patterns.
* [`playlist`][playlist]: functions for interacting with the playlist.
* [`plugins`][plugins]: functions for interacting with plugins on the channel rack and
  mixer.
* [`screen`][screen]: functions for controlling the screen of the AKAI Fire MIDI
  controller.
* [`transport`][transport]: functions for interacting with FL Studio's playback and
  recording systems.
* [`ui`][ui]: functions for interacting with FL Studio's user interface.

### MIDI controller scripting (extra libraries)

* [`midi`][midi]: a module containing constants used by the rest of the API.
* [`utils`][utils]: utility functions and classes. Note that a lot of code in this
  module is buggy and should be avoided.

### MIDI controller scripting (stub code utilities)

* [`fl_classes`][fl_classes]: a non-built-in module that provides definitions for classes
  used by FL Studio. It cannot be imported during runtime.

### Edison scripting

* [`enveditor`](enveditor/index.md): a module for interacting with edison, only available through its
  scripting interface.

### Piano roll scripting

* [`flpianoroll`](flpianoroll/index.md): a module for interacting with the
  piano roll, only available through its scripting interface.
