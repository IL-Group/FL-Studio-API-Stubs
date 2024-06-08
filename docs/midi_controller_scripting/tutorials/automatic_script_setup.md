# Automatic script setup

MIDI Controller Scripts can be set up to work with compatible devices
automatically, if they provide the right metadata to FL Studio. This tutorial
documents the process for setting up a script.

## Script metadata

Script metadata is specified by adding header comments to a script. To set up
automatic linking, you should specify the `supportedDevices` and/or
`supportedHardwareIds` properties.

Information about these properties can be found in the
[script metadata documentation](../script_metadata.md).
