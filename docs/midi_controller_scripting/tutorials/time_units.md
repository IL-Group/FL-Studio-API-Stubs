# Time units used within FL Studio

FL Studio uses many different time formats, and it is important to understand
them all, so that your scripts can correctly interpret time-related data.

## Beats

A beat represents a musical beat, the central unit of time when playing live
music.

## Bars

A bar is a collection of beats, grouped based on the value of a time signature.

## Steps

A step is a subdivision of a beat. These are the same length as a unit in the
step sequencer. By default, there are 4 steps per beat.

## Ticks

A tick is the smallest subdivision of MIDI time. By default, there are 96 ticks
per quarter note, but this value can be adjusted by changing the
[timebase (PPQN)](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/songsettings_settings.htm)
of a project. The project timebase can be determined by calling
[`general.getRecPPQ()`][general.getRecPPQ].

Ticks can be used as in an absolute format (number of ticks since the start of
the arrangement), or in conjunction with other beat-based time unit (see
[B:S:T](#bst)).

## B:S:T

"B:S:T" is time counted as bars, steps and ticks. It is comprised of

* The bar number within the current arrangement.
* The number of steps since the start of the current bar.
* The number of ticks since the start of the current step.

## Seconds

The same as seconds in real life. If you want to know more,
[here's a link to the Wikipedia article](https://en.wikipedia.org/wiki/Second).

## Minutes

One minute is equal to 60 seconds.

## Centiseconds

One centisecond is equal to one hundredth of a second.

## M:S:CS

"M:S:CS" is time counted as minutes, seconds and centiseconds.

* The number of minutes since the start of the current arrangement.
* The number of seconds since the start of the current minute.
* The number of centiseconds since the start of the current second.
