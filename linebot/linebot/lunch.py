# import os
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

linebot_api = LineBotApi("kmhdWuI33HGufZ4CenfTSXHUwWcKX9qIqKWju/spNTzClCNGaZ8ormJxrfB55n58h+ZdY7pr2EBPBWvsEZpTSaZMogIm5i5bX3982BZLI3vXzhdE1T3LNSGOpFO46ruyVUgHA/nD6VHxBb08EXFk7QdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("6d6da6c7f2d6c2d4a77b7ed752c41812")

@ app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@ handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # if event.message.text =='a':
    #     msg = (TextSendMessage(text='這是測試'))
    #     linebot_api.reply_message(event.reply_token, msg)

    # else:
    #     linebot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))


    mtext = event.message.text
    if mtext == '[午餐吃什麼]':
        try:    
            import random
            restaurant_ary = [
                '義大利麵',"丸龜","那個那個飯","吃你想吃的","泡麵","滷味","麻辣燙","美濃","莫尼","不要甲水餃"
            ]

            result = random.choice(restaurant_ary)
            msg_eat = TextSendMessage(text=result)
            linebot_api.reply_message(event.reply_token,msg_eat)

        except Exception as e:
            print(f"出現異常：{e}")


if __name__ == "__main__":
    app.run()