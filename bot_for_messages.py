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
user_id = ""
user_message = ""


def wake_up(update, context):
    chat = update.effective_chat
    # button=ReplyKeyboardMarkup([['']])
    if chat.last_name is None:
        context.bot.send_message(
           chat_id=chat.id,
           text = 'Привет,  {}'.format(chat.firtst_name),
        #    reply_markup=button 
        )
    else:
        context.bot.send_message(
            chat_id=chat.id,
            text="Привет,  {} {}".format(chat.first_name, chat.last_name),
            # reply_markup=button
        )
    context.bot.send_message(
        chat_id = chat.id,
        text = "Напишите id пользователя, которому надо отправить сообщение:"
    )


def get_message(message, id, context):
    user_message = message

    context.bot.send_message(
        id,
        text="Ваше сообщение отправлено"
    )


def get_id(update, context):
    message = update.message.text
    id = update.effective_chat.id
    if user_id == "":
        user_id = message

        context.bot.send_message(
            id,
            text="Напишите мне сообщение, которое я должен отправить"
        )
    else:
        get_message(message, id, context)


def main():
    updater.dispatcher.add_handler(CommandHandler("start", wake_up))
    updater.dispatcher.add_handler(Filters.text, get_id)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()


