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


# 課表
@ handler.add(MessageEvent, message=TextMessage)
def handle_timetable(event):

    mtext = event.message.text

# 功能: 查課
    if mtext == '[查課]':
        try:
            msg = TextSendMessage(text="輸入星期幾(1~5)/第幾堂課(1~10) ex:2/3 ")
            linebot_api.reply_message(event.reply_token,msg)
        except Exception as e:
            print(f"出現異常：{e}")

    if len(mtext) == 3 and mtext[1] == '/' and mtext[0] in '12345' and mtext[2] in '123456789':
        try:
            day = int(mtext[0]) #星期幾
            No_class = int(mtext[2]) #第幾堂
            nullClass = "沒課開心睡覺局"
            # w11 = "生涯輔導"
            # w12 = "英文"
            class_array = [

                #w1
                [nullClass,nullClass,'生涯規劃','生涯規劃','英文','英文','英文',nullClass,nullClass],
                #w2
                [nullClass,"電子電路",'電子電路','進階程式設計','進階程式設計','進階程式設計',nullClass,nullClass],
                #w3
                [nullClass,'國文','國文','國文','資訊不專業證照輔導','資訊不專業證照輔導','資訊不專業證照輔導',nullClass,nullClass],
                #w4
                [nullClass,'計算機網路','計算機網路','計算機網路','網路應用程式設計','網路應用程式設計','班會','班會','網路應用程式設計'],
                #w5
                [nullClass,'微積分','微積分','微積分','體育','體育',nullClass,nullClass,nullClass]
                
            ]
            # print(class_array[day][No_class])
            class_info = class_array[day-1][No_class-1]
            msg1 = TextSendMessage(text=f"星期{day} 第{No_class}堂課 : {class_info}")
            linebot_api.reply_message(event.reply_token,msg1)
        except Exception as e:
            print(f"出現異常：{e}")


# 功能: 顯示現在時間&下一堂課
    if mtext == '[等下什麼課]':
        try:
            import datetime
            # 顯示現在時間&下一堂課

            current_time = datetime.datetime.now()
            week_of_day = current_time.weekday()+1 #不知道為甚麼星期漫一天
            hour = str(current_time)[11]+str(current_time)[12]

            class_dict = {
                "8" : 1,
                "9" : 2,
                "10" : 3,
                "11" : 4,
                "12" : "甲奔",
                "13" : 5,
                "14" : 6,
                "15" : 7,
                "16" : 8,
                "17" : 9
            }

            nullClass = "沒"
            class_array = [

                #w1
                [nullClass,nullClass,'生涯規劃','生涯規劃','英文','英文','英文',nullClass,nullClass],
                #w2
                [nullClass,"電子電路",'電子電路','進階程式設計','進階程式設計','進階程式設計',nullClass,nullClass],
                #w3
                [nullClass,'國文','國文','國文','資訊不專業證照輔導','資訊不專業證照輔導','資訊不專業證照輔導',nullClass,nullClass],
                #w4
                [nullClass,'計算機網路','計算機網路','計算機網路','網路應用程式設計','網路應用程式設計','班會','班會','網路應用程式設計'],
                #w5
                [nullClass,'微積分','微積分','微積分','體育','體育',nullClass,nullClass,nullClass]
                
            ]
            # 平日
            if week_of_day <= 5:
                week_of_day = week_of_day;
                
                if hour in class_dict:
                    msg_class = (f" 星期{week_of_day} 第{class_dict[hour]}節  {class_array[week_of_day-1][class_dict[hour]-1]}課")
                    msg_class2 = (f"下一節是{hour}點10分{class_array[week_of_day-1][class_dict[hour]]}課")
                if int(hour) < 8:
                    msg_class = ("還沒上課，不要猴急")
                elif int(hour) == 12:
                    msg_class = ("甲奔")
                elif int(hour) >= 18:
                    msg_class = ("下課勾home")
            # 假日
            else:
                msg_class = "今天放假!!"
            
            msg2 = TextSendMessage(text=msg_class)
            linebot_api.reply_message(event.reply_token,msg2)
            msg3 = TextSendMessage(text=msg_class2)
            linebot_api.reply_message(event.reply_token,msg3)

        except Exception as e:
            # 捕獲所有異常並打印相關訊息
            print(f"出現異常：{e}")

# 功能: 甲奔        
    if mtext == '[午餐吃什麼]':
        try:    
            choice = TextSendMessage(
                text="選",
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="breakfast",text="breakfast")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="lunch",text="lunch")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="dinner",text="dinner")
                        ),
                    ]
                )
            )
            linebot_api.reply_message(event.reply_token,choice)

        except Exception as e:
            print(f"出現異常：{e}")

    if mtext == "breakfast" or "lunch" or "dinner":
        try:
            import random
            #breakfast
            breakfast_ary = ['阿如','早安有喜','歐姆薯薯','橙家'] 
            #lunch or dinner
            restaurant_ary = [
                '義大利麵',"丸龜","那個那個飯","吃你想吃的","泡麵","滷味","麻辣燙","美濃","莫尼","不要甲水餃"
            ]
            if mtext == 'breakfast':
                result = random.choice(breakfast_ary)
                linebot_api.reply_message(event.reply_token,TextSendMessage(text=result))

            if mtext == 'lunch' or 'dinner':
                result = random.choice(restaurant_ary)
                linebot_api.reply_message(event.reply_token,TextSendMessage(text=result))
            
        except Exception as e:
            # 捕獲所有異常並打印相關訊息
            print(f"出現異常：{e}")


if __name__ == "__main__":
    app.run()