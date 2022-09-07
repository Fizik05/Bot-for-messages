import os

from pyrogram import Client
import dotenv


dotenv.load_dotenv()

from_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

file = open("details.txt", "r")
user_id = int(file.readline())
user_message = file.readline()


def send_message():
    app = Client("left_acc", from_id, api_hash)
    app.start()
    app.send_message(user_id, user_message)
    app.stop()


def main():
    send_message()


if __name__ == "__main__":
    main()
