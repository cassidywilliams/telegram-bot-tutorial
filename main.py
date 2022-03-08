import os
import telegram
from flask import Response


BOT = telegram.Bot(token=os.environ["TELEGRAM_TOKEN"])


def bot(request):

    if request.method == "POST":
        request = telegram.Update.de_json(request.get_json(force=True), BOT)
        chat_id = request.message.chat.id

        # here you can add any functionality you want!

        # we will simply send a confirmation that the message was received for now
        BOT.sendMessage(chat_id=chat_id, text="Bot received your message")

    return Response("OK", 200)
