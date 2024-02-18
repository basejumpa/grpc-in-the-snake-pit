"""All about the letter 'A'."""

class A:
    """
    A class representing an object with a value.
    """

    def __init__(self, value=0):
        self.value = value
        self.a = 5

    def get_value(self):
        """
        Get the current value of the object.

        Returns:
            The current value.
        """
        return self.value

    def set_value(self, new_value):
        """
        Set a new value for the object.

        Args:
            new_value: The new value to set.
        """
        if self.a == 5:
            self.value = new_value
        else:
            pass

    def __str__(self):
        """
        Return a string representation of the object.

        Returns:
            A string representation of the object.
        """
        return f"A(value={self.value})"
