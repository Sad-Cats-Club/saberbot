# Saber Bot

[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/chuahou/saberbot.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/chuahou/saberbot/context:python)

A simple Telegram bot that sends a random non-NSFW picture from [r/Saber](https://old.reddit.com/r/Saber).
Inspired by but not based on [doggobot](https://github.com/dzakyputra/doggobot).

This bot can be found at [t.me/ch_saberbot](https://t.me/ch_saberbot).

## Prerequisites

You need to have installed:

- Python 3 and pip

You also need these secrets (organisation memebers may use
[these](https://github.com/Sad-Cats-Club/saberbot/settings/secrets):

- Reddit API client ID + client secret
- Telegram bot API key

## Usage

First, create a virtual environment and source it:

	python3 -m venv venv
	. venv/bin/activate

Install dependencies using pip:

	pip3 install -r requirements.txt

Run the bot:

	python3 bot.py
