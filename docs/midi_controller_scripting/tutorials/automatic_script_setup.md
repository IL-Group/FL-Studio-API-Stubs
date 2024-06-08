# Automatic script setup

MIDI Controller Scripts can be set up to work with compatible devices
automatically, if they provide the right metadata to FL Studio. This tutorial
documents the process for setting up a script.

## Script metadata

Script metadata is specified by adding header comments to a script. To set up
automatic linking, you should specify the
[`supportedDevices`](../script_metadata/#supporteddevices) and/or
[`supportedHardwareIds`](../script_metadata/#supportedhardwareids) properties.

```py
# name=My Script
# supportedDevices=Some Device Name
# supportedHardwareIds=01 02 03 04
```
