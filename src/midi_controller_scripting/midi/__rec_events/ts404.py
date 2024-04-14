"""
The TS404 REC events are undocumented. They are likely associated with the
[obsolete and unavailable](https://support.image-line.com/action/knowledgebase/?ans=352)
TS404 plugin.
"""
from .ranges import REC_Chan_First, REC_Global_First

REC_Chan_TS404_First = REC_Chan_First + 0x100  # same order as the 404 params
REC_Chan_TS404_FCut = REC_Chan_TS404_First + 18
REC_Chan_TS404_FRes = REC_Chan_TS404_First + 19
REC_Chan_TS404_Env_First = REC_Chan_TS404_First + 31
REC_Chan_TS404_Env_Last = REC_Chan_TS404_Env_First + 4
REC_Chan_TS404_Last = REC_Chan_TS404_First + 0x100 - 1
REC_Chan_TS404_Valid_First = 259
REC_Chan_TS404_Valid_Last = 293

REC_TS404Delay_First = REC_Global_First + 0x100  # obsolete
REC_TS404Delay_Feed = REC_TS404Delay_First
REC_TS404Delay_Pan = REC_TS404Delay_First + 1
REC_TS404Delay_Vol = REC_TS404Delay_First + 2
REC_TS404Delay_Time = REC_TS404Delay_First + 3
