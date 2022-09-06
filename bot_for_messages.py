import os

import dotenv

from telegram import ReplyKeyboardMarkup
from telegram.ext import (Updater,
                          Filters,
                          MessageFilter,
                          CommandHandler)


dotenv.load_dotenv()

token = os.getenv("TOKEN")
updater = Updater(token=token)


def wake_up(update, context):
    pass


def get_id(update, context):
    pass


def main():
    updater.dispatcher.add_handler(CommandHandler("start", wake_up))
    updater.dispatcher.add_handler(Filters.text, get_id)


if __name__ == "__main__":
    main()
