#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

import os
import logging
import time

from logging.handlers import RotatingFileHandler

from .translation import Translation

# Change Accordingly While Deploying To A VPS
APP_ID = int(os.environ.get("22506926"))

API_HASH = os.environ.get("34fe7b7d19572aae39c6db80e151d9f7")

BOT_TOKEN = os.environ.get("8004078816:AAFpANlxyG1emrSLYYuJXgEecNGJIvme78c")

DB_URI = os.environ.get("mongodb+srv://dilipdewasi7759:<NMzFkZqWZdi1GDG4>@ssdmovies.2nqad.mongodb.net/?retryWrites=true&w=majority&appName=ssdmovies")

USER_SESSION = os.environ.get("USER_SESSION")

VERIFY = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "autofilterbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
