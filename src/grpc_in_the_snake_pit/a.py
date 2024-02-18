"""Module a: Everything you need to know about the letters."""

__THE_VALUE = "a"

def get():
    """
    This function returns the string "a".

    Returns:
        str: The string "a".
    """
    return __THE_VALUE


def set_the_value(value: str):
    """
    This function sets the THE_VALUE of the string "a".

    Args:
        THE_VALUE (str): The THE_VALUE to set.
    """
    __THE_VALUE = value
