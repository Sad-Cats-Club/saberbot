# utility functions for using the API

import logging

# sends message
def send(update, context, message):
    context.bot.send_message(
        chat_id=update.message.chat_id,
        text=message
    )
    logging.info("Sent message %s", message)

# sends photo
def send_photo(update, context, photo, caption):
    context.bot.send_photo(
        chat_id=update.message.chat_id,
        photo=photo,
        caption=caption,
        parse_mode="Markdown"
    )
    logging.info("Sent photo with caption %s", caption)
