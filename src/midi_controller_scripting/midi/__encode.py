def EncodeRemoteControlID(PortNum: int, ChanNum: int, CCNum: int) -> int:
    """
    Generates a controlId given information about an event

    ## Args:
    * `PortNum` (`int`): the port that this event was sent to

    * `ChanNum` (`int`): the channel of this event

    * `CCNum` (`int`): the CC number of this event

    ## Returns:
    * `int`: controlId

    Included since API Version 1
    """
    return CCNum + (ChanNum << 16) + ((PortNum + 1) << 22)
