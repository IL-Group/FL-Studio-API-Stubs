"""
patterns > performance

Contains functions for working with performance mode
"""


def getBlockSetStatus(left: int, top: int, right: int, bottom: int) -> int:
    """
    Returns the status of the live block.

    HELP WANTED: What does this do?

    ## Args

    * left (`int`): ?

    * top (`int`): ?

    * right (`int`): ?

    * bottom (`int`): ?

    ## Returns

    * `int`: live block status
          * `LB_Status_Filled` (`1`): Filled.

          * `LB_Status_Scheduled` (`2`): Scheduled.

          * `LB_Status_Playing` (`4`): Playing.

    Included since API version 1.
    """
    return 0


def ensureValidNoteRecord(index: int, playNow: int = 0, /) -> int:
    """
    Ensures valid note on the pattern at `index`.

    ## HELP WANTED

    * What does this do? I haven't managed to get it to return
      anything other than zero.

    ## Args

    * `index` (`int`): pattern index.

    * `playNow` (`int`, optional): ???. Defaults to 0.

    ## Returns

     * `int`: ???

    Included since API version 1.
    """
    return 0
