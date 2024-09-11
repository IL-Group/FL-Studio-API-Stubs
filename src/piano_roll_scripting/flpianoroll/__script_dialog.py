"""
The `ScriptDialog` class is used to create and control dialog windows when
running piano roll scripts.
"""
from typing import Union


class ScriptDialog():
    """
    Dialog that is shown when script is called
    """
    def __init__(self, title: str, description: str) -> None:
        """
        Initializes a new script dialog

        ## Args:
        * `title` (`str`): Title of Window
        * `description` (`str`): Description shown on windo
        """

    def AddInput(self, name: str, value: float, hint: str = '') -> None:
        """
        Adds a generic input control, rotary boolean

        ## Args:
        * `name` (`str`): Name of control
        * `value` (`float`): Initial value
        * `hint` (`str`, optional): Text to display in hint panel
        """

    def AddInputKnob(self, name: str, value: float, min: float, max: float, hint: str = '') -> None:
        """
        Adds a knob input control with float values

        ## Args:
        * `name` (`str`): Name of control
        * `value` (`float`): Initial value
        * `min` (`float`): Minimum value
        * `max` (`float`): Maximum value
        * `hint` (`str`, optional): Text to display in hint panel
        """

    def AddInputKnobInt(self, name: str, value: int, min: int, max: int, reserved: int, hint: str = '') -> None:
        """
        Adds a knob input control with int values

        ## Args:
        * `name` (`str`): Name of control
        * `value` (`int`): Initial value
        * `min` (`int`): Minimum value
        * `max` (`int`): Maximum value
        * `reserved` (`int`): Unused
        * `hint` (`str`, optional): Text to display in hint panel
        """

    def AddInputCombo(self, name: str, options: list, value: int, hint: str = '') -> None:
        """
        Adds a combo box input control with list of strings

        ## Args:
        * `name` (`str`): Name of control
        * `options` (`list`): Options for selection
        * `value` (`int`): Index of initial option
        * `hint` (`str`, optional): Text to display in hint panel
        """

    def AddInputText(self, name: str, value: str, hint: str = '') -> None:
        """
        Adds a text box input control with string value

        ## Args:
        * `name` (`str`): Name of control
        * `value` (`str`): text to display
        * `hint` (`str`, optional): Text to display in hint panel
        """

    def AddInputCheckbox(self, name: str, value: bool, hint: str = '') -> None:
        """
        Adds a checkbox input control with string value

        ## Args:
        * `name` (`str`): Name of control
        * `value` (`bool`): Initial value
        * `hint` (`str`, optional): Text to display in hint panel
        """

    def AddInputSurface(self, name: str) -> None:
        """
        Adds a control surface

        ## Args:
        * `name` (`str`): Name of the control surface's preset file (without the `.fst` extension)
        """

    def GetInputValue(self, name: str) -> Union[str, int, float]:
        """
        Retrieve the current value of the input with the specified name

        ## Args:
        * `name` (`str`): name of control

        ## Returns:
        * `Union[str, int, float]`: current value of control
        """
        return 0.0

    def Execute(self) -> bool:
        """
        Shows the dialog and returns how the dialog was closed.
        Returns TRUE if the user pressed OK, FALSE if the dialog was cancelled.

        ## Returns:
        * `bool`: state of dialog
        """
        return True