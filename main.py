from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError
from datetime import date
import os

LINE_CHANNEL_ACCESS_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]


if __name__ == "__main__":
    line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)

    try:
        line_bot_api.broadcast(TextSendMessage(text='Remind paying rate'))

    except LineBotApiError as e:
        print(e)
