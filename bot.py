import atexit
import json
import logging
import os
import time

import yaml

import telegram
from api_util import send
from telegram.ext import CommandHandler, Updater

# get api key from config file
def get_apikey():
    try:
        with open("apikey.yml") as f:
            return yaml.safe_load(f)["api-key"]
    except: # failed to open file, try environment variables
        return os.environ.get("api_key")

# process start command
start_response = "Hello! Welcome to Saber Bot."
def start(update, context):
    send(update, context, start_response)

def main():
    # create updater
    updater = Updater(token=get_apikey(), use_context=True)
    dispatcher = updater.dispatcher

    # set up logging
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO)

    # add handlers
    dispatcher.add_handler(CommandHandler("start", start))

    # start polling
    updater.start_polling()

if __name__ == "__main__":
    main()
