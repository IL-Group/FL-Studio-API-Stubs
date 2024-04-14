"""
Many functions within the FL Studio API support a pickup option, meaning that
tweaks to the parameter will only take effect once the value moves past the
current value in the mixer (in both upwards and downwards directions).

By providing a pickup option, scripts can support pickup for these controls.
"""

PIM_None = 0
"""
Don't use pickup.
"""
PIM_AlwaysPickup = 1
"""
Always use pickup, regardless of user's preferences.
"""
PIM_FollowGlobal = 2
"""
Follow user's preference for pickup.
"""
