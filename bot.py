import logging
import os
import random
import yaml

import praw
from telegram.ext import CommandHandler, Updater

from api_util import send, send_photo

# configuration file path
APIKEY_YML_PATH = "apikey.yml"

# get api key from config file
def get_apikey():
    if os.path.exists(APIKEY_YML_PATH):
        with open(APIKEY_YML_PATH) as config_file:
            return yaml.safe_load(config_file)["api_key"]
    else: # no config file, try environment variables
        return os.environ.get("api_key")

# gets client ID and secret for praw
def get_praw_id_secret():
    if os.path.exists(APIKEY_YML_PATH):
        with open(APIKEY_YML_PATH) as config_file:
            yml = yaml.safe_load(config_file)
            return yml["client_id"], yml["client_secret"]
    else: # no config file, try environment variables
        return os.environ.get("client_id"), os.environ.get("client_secret")

# process start command
START_RESPONSE = "Hello! Welcome to Saber Bot."
def start(update, context):
    send(update, context, START_RESPONSE)

# process photo command
def photo(update, context):
    url, caption = get_pic()
    send_photo(update, context, url, caption)

# get picture from reddit
def get_pic():
    # get r/Saber
    sub = reddit.subreddit("saber")
    posts = list(sub.hot(limit=100))
    rng = posts[random.randint(0, 100)]
    while rng.over_18 or rng.is_self:
        rng = posts[random.randint(0, 100)]
    return rng.url, rng.title + \
            r" | \[ [Link](reddit.com" + rng.permalink + ") ]"

def main():
    global reddit

    # create updater
    updater = Updater(token=get_apikey(), use_context=True)
    dispatcher = updater.dispatcher

    # create praw instance
    client_id, client_secret = get_praw_id_secret()
    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent="ch_saberbot")

    # set up logging
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO)

    # add handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("photo", photo))

    # start polling
    updater.start_polling()

if __name__ == "__main__":
    main()
