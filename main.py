from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError
import datetime
import os
from dotenv import load_dotenv


load_dotenv()
LINE_CHANNEL_ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
SUNDAY = 6


if __name__ == "__main__":
    today = datetime.date.today()
    if (today.weekday() == SUNDAY):
        line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)

        try:
            line_bot_api.broadcast(TextSendMessage(
                text='Reminder. paying rent!!!!'))

        except LineBotApiError as e:
            print(e)
