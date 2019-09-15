# utility functions for using the API

# sends message
def send(update, context, message):
    context.bot.send_message(
        chat_id=update.message.chat_id,
        text=message
    )
