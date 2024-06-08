# Sharing your script

If you've made a MIDI Controller Script, it's a great idea to share it with
others so that everyone can benefit from your hard work! This tutorial runs
through the instructions for bundling MIDI Controller Scripts so that they can
be installed, used and enjoyed by others.

## Add a license to your work

When sharing work online, it is important to add a license so that other users
are aware of what they can (and can't) do with it. By default, anything you
create and share is "All rights reserved", meaning that your users can't
legally modify or create derivatives of your work. This probably isn't what you
want, and we encourage you to choose a license that benefits the community by
allowing derivative work, even if you don't maintain your script.

Although a license can be as simple as a text file where you explain what users
are allowed to do with your work, it is often better to apply an existing
license to your work. Here are some simple explanations of common software
licenses. (Disclaimer: this isn't legal advice).

| License | Meaning | More info |
|---------|---------|-----------|
| MIT     | Anyone is free to modify your work and redistribute it under their own terms, but they must leave credit for your code | [Here](https://choosealicense.com/licenses/mit/) |
| GPL v3  | Anyone who modifies or redistributes your work must keep it licensed as GPLv3, meaning all modifications will be free forever | [Here](https://choosealicense.com/licenses/gpl-3.0/) |
| Unlicense | Anyone can do anything with your work, with or without credit | [Here](https://choosealicense.com/licenses/unlicense/) |

Details on more licenses can be found at [choosealicense.com](https://choosealicense.com/licenses/).

You should ensure that you place your license within your script, either in a
separate `license.txt` file, or in a comment at the top of the source file.

## Include your device configuration

For some devices, the control mappings can be customized using companion
software (eg Novation Components for Novation controllers). If you have changed
your controller's mappings from their factory default, make sure to export the
settings from the companion software, and provide instructions for how users
can copy these settings to their own device.

## Document your work

Often, things that seem intuitive to you may not be obvious to others. As such,
it's crucial to document how to use your script if you want to share it with
others. You should include information on:

* How should users configure their MIDI settings, including MIDI ports and
  script assignments (if your script doesn't manage this
  [automatically](./automatic_script_setup.md)). It's a great idea to include a
  screenshot if your setup process is particularly complex.

* What each of the buttons do (if they aren't obvious such as a play button
  controlling playback).

* What parts of FL Studio it integrates with (eg the mixer, the step
  sequencer/channel rack, or performance mode), and how to control those
  integrations.

* What plugins/VSTs it automatically integrates with, and how to control these
  integrations.

* If your script changes its mappings dynamically, how it determines mappings
  (eg by tracking the active window inside FL Studio).

* If it controls hardware features such as LEDs, what all the options mean.

A great place to write this information is inside a `README.md` file (which you
can write in [Markdown format](https://www.markdownguide.org/)).

## Zip it up

Now, select all of your script's files and compress them into a `.zip` archive.
Make sure to include:

* Your Python script file(s) in their original file hierarchy.
* Any device-specific setup instructions (eg inside your `README.md` file).
* Your license file.

## Post it to the Image-Line forum

The [Image-Line forum](https://forum.image-line.com/) is the primary place
where FL Studio users discuss the DAW and its ecosystem. Posting your script
here will ensure that it can be found by other users. Create a new post in the
[MIDI Controller Scripting section](https://forum.image-line.com/viewforum.php?f=1994)
of the forum. Your post should include:

* A title that includes the make and model of the device(s) that your script
  supports.
* An image of the MIDI controller(s) that your script supports, so users can be
  certain that it matches their device.
* The `.zip` archive of your script's files.
* Information about your script's features (you can grab this from your
  `README.md` file). This is especially important if there are existing scripts
  for your device, since we try to add a short description for each script to
  the working scripts list so that users can choose an option that suits their
  needs.
* Any additional instructions for setting up your script.

Upon seeing your post, we will add it to our
[list of working scripts](https://forum.image-line.com/viewtopic.php?p=1494169#p1494169)
so that other users can find and enjoy it.

It could also be useful to share your work in other places, such as forums for
your MIDI controller.

## Set up version control (optional)

If your script has a lot of features, it can be useful to use version control
software to help you manage changes to your work. This is especially useful for
collaboration, since many version control websites can also help with:

* Issues with your project (so your users can report bugs and you can track
  your progress fixing them).
* Merge requests, where other users can integrate their own code contributions
  to your project.
* Continuous integration, so you can automatically validate that your project
  is working correctly.
* Releases, so you can share new versions of your script with users.

The most popular option for this is [GitHub](https://github.com). After
creating an account, you can install software such as
[GitHub Desktop](https://desktop.github.com/) to create a repository and commit
your work.

If you share your work on GitHub, it's a good idea to edit your forum post to
share the link to your project so that others can contribute to your work.
