import atexit
import json
import logging
import os
import random
import time

import yaml

import praw
import telegram
from api_util import send, send_photo
from telegram.ext import CommandHandler, Updater

# get api key from config file
def get_apikey():
    try:
        with open("apikey.yml") as f:
            return yaml.safe_load(f)["api-key"]
    except: # failed to open file, try environment variables
        return os.environ.get("api_key")

# gets client ID and secret for praw
def get_praw_id_secret():
    try:
        with open("apikey.yml") as f:
            yml = yaml.safe_load(f)
            return yml["client_id"], yml["client_secret"]
    except: # failed to open file, try environment variables
        return os.environ.get("client_id"), os.environ.get("client_secret")

# process start command
start_response = "Hello! Welcome to Saber Bot."
def start(update, context):
    send(update, context, start_response)

# process photo command
def photo(update, context):
    send_photo(update, context, get_pic())

# get picture from reddit
def get_pic():
    # get r/Saber
    sub = reddit.subreddit("saber")
    posts = [post for post in sub.hot(limit=100)]
    rng = posts[random.randint(0, 100)]
    while rng.over_18 or rng.is_self:
        rng = posts[random.randint(0, 100)]
    return rng.url

def main():
    global reddit

    # create updater
    updater = Updater(token=get_apikey(), use_context=True)
    dispatcher = updater.dispatcher

    # create praw instance
    client_id, client_secret = get_praw_id_secret()
    reddit = praw.Reddit(client_id=client_id, client_secret=client_secret,
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
