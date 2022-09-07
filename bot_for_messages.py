import os

import dotenv

from telegram.ext import (Updater,
                          Filters,
                          MessageHandler,
                          CommandHandler)


dotenv.load_dotenv()

token = os.getenv("TOKEN")
updater = Updater(token=token)
from_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
user_id = []
user_message = []


def make_file():
    file = open("details.txt", "w")
    file.write(user_id[0] + "\n")
    file.write(user_message[0])
    file.close()


def wake_up(update, context):
    chat = update.effective_chat
    if chat.last_name is None:
        context.bot.send_message(
           chat_id=chat.id,
           text = 'Привет,  {}'.format(chat.firtst_name)
        )
    else:
        context.bot.send_message(
            chat_id=chat.id,
            text="Привет,  {} {}".format(chat.first_name, chat.last_name)
        )
    context.bot.send_message(
        chat_id = chat.id,
        text = "Напишите id пользователя, которому надо отправить сообщение:"
    )


def get_id(update, context):
    message = update.message.text
    id = update.effective_chat.id
    if user_id == []:
        user_id.append(message)

        context.bot.send_message(
            id,
            text="Напишите мне сообщение, которое я должен отправить"
        )
    else:
        user_message.append(message)
        make_file()
        os.system("send_message.py")

        context.bot.send_message(
            id,
            text="Ваше сообщение отправлено"
        )
        os.remove("details.txt")


def main():
    updater.dispatcher.add_handler(CommandHandler("start", wake_up))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, get_id))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
