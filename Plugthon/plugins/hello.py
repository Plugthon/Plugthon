# Import necessary libraries
from Plugthon import __version__ #Import Plugthon version
from telethon import version #Import Telethon version
from platform import python_version #Import Python version

# This class handles user greetings when the plugin is initialized
class Greetings:
    async def UserGreetings(self, event):
        """
        Handles the greeting message for the user.
        Args:
            event: The event object containing information about the message.
        Returns:
            str: The greeting message for the user.
        """

        # Delete the original message
        await event.delete()

        # Get the sender of the message
        get_user = await event.get_sender()

        # Extract the first name of the sender
        first_name = get_user.first_name

        # Construct the greeting message
        user_greetings = f"Greetings, {first_name}!\nCongratulations! Your \"Hello World\" plugin has been successfully initialized and is now operational within the Plugthon.\n\nPlugthon: {__version__}\nTelethon: {version.__version__}\nPython: {python_version()}\n\nThank you"

        return user_greetings