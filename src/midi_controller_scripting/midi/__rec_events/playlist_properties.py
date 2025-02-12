"""
The following event IDs can be used to target properties of the playlist and
patterns.
"""
from .ranges import REC_Chan_First, REC_ItemRange

# playlist
REC_Playlist_First = 0x5000 * REC_ItemRange
REC_Playlist_Last = REC_Playlist_First + 0x2000 * REC_ItemRange - 1

# patterns (up to 4096)
REC_Pat_First = REC_Playlist_First
REC_Pat_Last = REC_Pat_First + 0x1000 * REC_ItemRange - 1
REC_Pat_Clip = REC_Pat_First + 0x5000  # clip item

# all clips
# this is not a typo, it includes channel and pattern clips
REC_PLClip_First = REC_Chan_First
REC_PLClip_Last = REC_Pat_Last

# pattern instances at the top of the playlist
REC_Playlist_Old = REC_Playlist_First  # obsolete
# pattern block, but shouldn't happen anymore?
REC_Pat_Block = REC_Playlist_First + 0x1000 * REC_ItemRange
REC_Playlist = REC_Playlist_Old

# playlist tracks (up to 4096)
REC_PLTrack_First = 0x6000 * REC_ItemRange
REC_PLTrack_Last = REC_PLTrack_First + 0x1000 * REC_ItemRange - 1
