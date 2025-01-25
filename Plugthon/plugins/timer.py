class SelfDestruct:
    def __init__(self):
        """
        Initializes the SelfDestruct class with an empty error message.
        """
        self.error_message = ""

    async def Media(self, event):
        """
        Downloads the media from the replied message in a private chat. 

        Args:
            event: The Telegram event object.

        Returns:
            A tuple containing the downloaded media path and a success flag (1 for success, 0 for failure).
            Returns None if an error occurs.
        """

        #Delete the original message
        await event.delete()

        try:
            #Check if the message is in a private chat
            if not event.is_private:
                raise ValueError("This feature only works for private messages.")
            
            #Check if the message is a reply
            elif not event.reply_to:
                raise ValueError("Please use the command in the media's reply.")
            else:
                #Get the replied message
                get_media = await event.get_reply_message()

                #Check if the replied message contains media
                if not get_media.media:
                    raise ValueError("This function is specifically designed for downloading media files. Since the content you're attempting to download does not fall under the media category, please restrict the use of this feature to media files only.")
                else:
                    #Download the media
                    downloaded_media = await get_media.download_media()

                    #Return the downloaded media path and success flag
                    return downloaded_media
        except ValueError as error:
            #Store the error message
            self.error_message = error