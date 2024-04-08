"""
# Env Editor / Utils

Contains utility functions used within Edison scripts
"""


class TUtils:
    """
    Utility class containing useful functions to allow audio processing scripts
    to interact with FL Studio.

    This is instantiated in the `Utils` object, and the fact that this class is
    public is probably unintentional. Just use `Utils` directly.
    """
    def ProgressMsg(self, message: str, position: int, total: int) -> None:
        """
        Report a progress message to FL Studio

        This will be displayed in the hint panel as the message alongside a
        progress bar.

        ## Args:
        * `message` (`str`): Message to display

        * `position` (`int`): Position within your audio processing

        * `total` (`int`): Total amount of processing to do
        """

    def ShowMessage(self, message: str) -> None:
        """
        Show a message to the user within a dialog box

        ## Args:
        * `message` (`str`): Message to show
        """


Utils = TUtils()
"""
A utility object containing useful functions to allow audio processing scripts
to interact with FL Studio

Included since API Version 21
"""
