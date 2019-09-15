# utility functions for using the API

# sends message
def send(update, context, message):
    context.bot.send_message(
        chat_id=update.message.chat_id,
        text=message
    )

# sends photo
def send_photo(update, context, photo, caption):
    context.bot.send_photo(
        chat_id=update.message.chat_id,
        photo=photo,
        caption=caption,
        parse_mode="Markdown"
    )
