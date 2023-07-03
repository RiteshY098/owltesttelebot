import telebot
from selenium.common.exceptions import TimeoutException
from ReelsAPI import is_reels_video, get_reels_video

bot = telebot.TeleBot("6043379854:AAGmG2eT_YMww5PBTCKZiwX72LyuqQqfxas", parse_mode=None)


# Define a function to handle any incoming message
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Check if the message text is a valid Instagram Reels URL
    if not is_reels_video(message.text):

        # If not, reply with an error message
        bot.reply_to(message, "The given url is not valid")

    else:

        # If yes, send a message indicating that the video is being processed
        bot.send_message(message.chat.id, "Please wait! Processing a video...")

        # Send a chat action to show that the video is being uploaded
        bot.send_chat_action(message.chat.id, action="upload_video")

        try:
            # Try to download and send the video
            bot.send_video(message.chat.id, get_reels_video(message.text))
        except TimeoutException:
            # If there is a timeout error, send a message indicating that the video could not be downloaded
            bot.send_message(message.chat.id, "Unable to download the video\n\nMake sure the given url is valid")


# Start polling for messages indefinitely
bot.infinity_polling()
