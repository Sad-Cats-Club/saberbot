# utility functions for using the API

import logging

# sends message
async def send(update, context, message):
    await context.bot.send_message(
        chat_id=update.message.chat_id,
        text=message
    )
    logging.info("Sent message %s", message)

# sends photo
async def send_photo(update, context, photo, caption):
    await context.bot.send_photo(
        chat_id=update.message.chat_id,
        photo=photo,
        caption=caption,
        parse_mode="Markdown"
    )
    logging.info("Sent photo with caption %s", caption)
