# Performance Mode

Performance mode in FL Studio is a powerful tool for sequencing patterns
on-the-fly, used to create live performances.

Most of the functions associated with live performance are found in the
[`playlist`][playlist] module.

To determine whether performance mode is enabled, use
[`playlist.getPerformanceModeState`][playlist.getPerformanceModeState].

## Display zone

The display zone is the region that a controller is currently mapping for live
performance. When set using [`playlist.liveDisplayZone`][playlist.liveDisplayZone],
FL Studio indicates this region using a red rectangle.

## Blocks

When performance mode is active, clips within the performance region are called
"blocks".

## Loop modes

In performance mode, each playlist track has a loop mode, which determines how
the blocks on this track advance when the track is being played.

## Trigger modes

Each playlist track also has a trigger mode which determines the action taken
when pressing on a block.

## Trigger snap

When triggering a block, the trigger snap value of its track determines how FL
Studio will adjust the timing of the clip so that it starts in time with other
clips. For example, if this is set to a beat, and you trigger a block half a
beat early, FL Studio will wait the remaining half-beat so that the block will
start on the next beat.

## Position snap

Contrastingly, the position snap value determines how far FL Studio can skip
into the clip so that it remains in time with other clips. For example, if this
is set to a beat, and you trigger a block half a beat late, FL Studio will skip
the first half-beat of that block so it remains in-time.
