class PlugthonError(Exception):
    """
    This is a custom exception class for Plugthon errors.
    It inherits from the base Exception class.
    """
    def __init__(self, error_message):
        """
        The constructor for the PlugthonError class.

        Args:
            error_message: The error message to be displayed when the exception is raised.
        """
        super().__init__(error_message)