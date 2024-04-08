"""
# Env editor / Script dialog

Code representing the Script dialog class.
"""


class ScriptDialog:
    """
    Used to create and read attributes from a script dialog
    """
    def __init__(self, title: str, description: str) -> None:
        """
        Used to define a script which can be used by Edison.

        This object can then be used to add inputs to the script.

        When the properties are generated, the script should begin by calling
        the `Execute()` method which returns whether the script should run or
        not.

        ## Args:
        * `title` (`str`): the title to use for the script
        * `description` (`str`): a description for what the script does
        """

    def AddInput(self, name: str, default_value: float) -> None:
        """
        Add an input to the dialog, which accepts a floating point value
        between `0.0` and `1.0`. The input will display as a text box and an
        associated knob.

        ## Args:
        * `name` (`str`): name of the input.

        * `default_value` (`float`): the starting value of the input (clamped
          between `0.0` and `1.0`)
        """

    def AddInputKnob(
        self,
        name: str,
        default_value: float,
        min_value: float,
        max_value: float,
    ) -> None:
        """
        Add an input to the dialog, which accepts a floating point value
        between `min_value` and `max_value`. The input will display as a text
        box and an associated knob.

        ## Args:
        * `name` (`str`): the name of the input

        * `default_value` (`float`): the default value for the knob

        * `min_value` (`float`): the minimum value for the knob

        * `max_value` (`float`): the maximum value for the knob
        """

    def AddInputCombo(
        self,
        name: str,
        values: str,
        default_value: int,
    ) -> None:
        """
        Add an input to the dialog, which accepts values from a selection of
        options from a drop-down menu.

        ## Args:
        * `name` (`str`): the name of the input

        * `values` (`str`): the collection of values that are allowed. This
          should be a single string, where each option is separated by a comma.

        * `default_value` (`int`): an integer representing the default value of
          the input.
        """

    def GetInputValue(self, name: str) -> float:
        """
        Get the result of an input that has been added.

        This should be called only after calling the `Execute()` method to
        ensure the value has been initialized.

        ## Args:
        * `name` (`str`): the name of the input to get the value from

        ## Returns:
        * `float`: the float value chosen for knob inputs

        * `float`: a poorly-rounded integer representing the index of the
          option that the user selected for combo boxes.
        """
        return 0.0

    def Execute(self) -> bool:
        """
        Shows the dialog and returns whether the script should execute.

        Note that it is possible to modify the audio even if this returns
        `False`. For the sake of your users not hating you, you SHOULD NOT DO
        THIS.

        ## Returns:
        * `bool`: whether the script should execute
        """
        return True
