# Script metadata

Scripts can specify metadata, which is used to provide information to FL Studio
about the script.

This metadata is specified in a comment at the top of the script's entrypoint
(`device_*.py`) file.

## Example metadata

```py  linenums="1"
# name=Novation Launch Control XL
# url=https://forum.image-line.com/viewtopic.php?p=1494175
# receiveFrom=Forward Device
# supportedDevices=Launch Control XL,Launch Control XL mkII
# supportedHardwareIds=00 20 29 61 00 00 00 00 00 02 07
```

## `name`

The name property controls the name displayed to users in the script selection
menu. This should be descriptive, and should preferably contain your device's
make and model.

This property is required for all scripts. Scripts that do not specify the
property will not be shown in the list of available scripts.

```py
# name=Novation LaunchControl XL
```

## `url`

A help/support URL for your script. This URL must be a post on the
[Image-Line forum](https://forum.image-line.com/). Any URLs that don't start
with `https://forum.image-line.com/` will be redirected to the MIDI Controller
Scripting forum's main page.

```py
# url=https://forum.image-line.com/viewtopic.php?p=1494175
```

This property is optional.

## `receiveFrom`

A comma-separated list of device names from which this script can receive
MIDI messages.

```py
# receiveFrom=Forward Device
```

In the above example, the script named `Forward Device` will see this script in
its available dispatch targets, and will be able to send MIDI messages to this
script using [`device.dispatch()`][device.dispatch].

This property is optional.

## `supportedDevices`

A comma-separated list of device names to link to. FL Studio will automatically
link devices to your script if they have a matching name.

In this example, FL Studio will link the script to devices named
`Launch Control XL` and `Launch Control XL mkII`.

```py
# supportedDevices=Launch Control XL,Launch Control XL mkII
```

Note that device names change depending on your operating system, so it is
important to test these on both Windows and MacOS to ensure that automatic
linking works for both.

This property is optional.

## `supportedHardwareIds`

A comma-separated list of device hardware IDs to link to. FL Studio will
automatically link devices to your script if they provide a matching hardware
ID.

A hardware ID is sent by MIDI Controllers in response to a
[device ID request](https://music.stackexchange.com/a/93913/99162).

You can determine your device's hardware ID by calling
[`device.getDeviceID()`][device.getDeviceID] from that device's script output
console.

The hardware ID should be written as a series of space-separated hexadecimal
bytes.

```py
# supportedHardwareIds=00 20 29 61 00 00 00 00 00 02 07
```

FL Studio matches devices by using `bytes.startswith`, so bytes can be omitted
from the end of the hardware ID, allowing your script to disregard unimportant
aspects such as the firmware version.

This property is optional.
