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

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    try:
        mtext = event.message.text
        if mtext == '[常用連結]':
            # print("模板消息處理程序已觸發")
            result_link = TemplateSendMessage(
                alt_text='[常用連結]',
                template = ButtonsTemplate(
                    thumbnail_image_url="https://cdn-icons-png.flaticon.com/512/7471/7471685.png",
                    title="常用連結",
                    text="請選擇:",
                    actions=[
                        URITemplateAction(
                            label="eportal",
                            uri="https://sso.nutc.edu.tw/eportal/"
                        ),
                        URITemplateAction(
                            label="zuvio",
                            uri="https://irs.zuvio.com.tw/"
                        ),
                        URITemplateAction(
                            label="tronclass",
                            uri="https://tc.nutc.edu.tw/cas/login?service=https%3A//tc.nutc.edu.tw/login%3Fnext%3D/user/index&locale=zh_TW&ts=1676874443.898891"
                        ),
                    ]
                )
            )
            linebot_api.reply_message(event.reply_token, result_link)
    except Exception as e:
        print(f"出現異常：{e}")


if __name__ == "__main__":
    # port = int(os.environ.get('PORT', 5000))
    # app.run(host='0.0.0.0', port=port)
    app.run()


if __name__ == "__main__":
    # port = int(os.environ.get('PORT', 5000))
    # app.run(host='0.0.0.0', port=port)
    app.run()