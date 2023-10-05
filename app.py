# import os
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

import datetime

from flask import Flask
from tzlocal import get_localzone



app = Flask(__name__)
app.config['TIMEZONE'] = get_localzone()

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


# current_time = datetime.datetime.now()
# 課表
@ handler.add(MessageEvent, message=TextMessage)

# def home(event):
#     # 在每个请求中获取当前时间戳并更新current_time

def handle_timetable(event):

    mtext = event.message.text
    global current_time,hour,week_of_day
    current_time = datetime.datetime.now()
    hour = (current_time.hour)
    week_of_day = current_time.weekday()+1 #不知道為甚麼星期漫一天

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
            print(f"查課出現異常：{e}")


# 功能: 顯示現在時間&下一堂課
    if mtext == '[等下什麼課]':
        try:
            print("haha")
            if (hour != ""):
                print(hour)
            else:
                print("hour為空")
            # import datetime
            # 顯示現在時間&下一堂課

            # current_time = datetime.datetime.now()
            # hour = (current_time.hour)
            # week_of_day = current_time.weekday()+1 #不知道為甚麼星期漫一天

            class_dict = {
                8 : 1,
                9 : 2,
                10 : 3,
                11 : 4,
                # "12" : "甲奔",
                13 : 5,
                14 : 6,
                15 : 7,
                16 : 8,
                17 : 9,
            }

            nullClass = "沒"
            class_array = [

                #w1
                [nullClass,nullClass,'生涯規劃','生涯規劃','英文','英文','英文',nullClass,nullClass],
                #w2
                [nullClass,"電子電路",'電子電路','電子電路','進階程式設計','進階程式設計','進階程式設計',nullClass,nullClass],
                #w3
                [nullClass,'國文','國文','國文','資訊不專業證照輔導','資訊不專業證照輔導','資訊不專業證照輔導',nullClass,nullClass],
                #w4
                [nullClass,'計算機網路','計算機網路','計算機網路','網路應用程式設計','網路應用程式設計','班會','班會','網路應用程式設計'],
                #w5
                [nullClass,'微積分','微積分','微積分','體育','體育',nullClass,nullClass,nullClass]
                
            ]
            result_class=[]
            # 平日
            
            # print(hour)
            # print(type(hour))
            # result_rest.append(TextSendMessage(text=hour))

# 補一個下一門課是什麼!!!!!!
            if week_of_day <= 5:
                week_of_day = week_of_day;
                if hour in class_dict:
                    result_class.append(TextSendMessage(text=f"now : 第{class_dict[hour]}節  {class_array[week_of_day-1][class_dict[hour]-1]}課"))
                    if class_array[week_of_day-1][class_dict[hour]-1] != "沒" and class_dict[hour] !=9:
                        result_class.append(TextSendMessage(text=f"next : {hour+1}點10分{class_array[week_of_day-1][class_dict[hour]]}課"))
                    else : 
                        result_class.append(TextSendMessage(text="等下回家局"))

                elif hour < 8:
                    result_class.append(TextSendMessage(text="還沒上課，不要猴急"))
                elif hour == 12:
                    result_class.append(TextSendMessage(text="甲奔"))
                elif hour >= 18:
                    result_class.append(TextSendMessage(text="下課勾home"))
            # 假日
            else:
                result_class.append(TextSendMessage(text="今天放假!!"))

            linebot_api.reply_message(event.reply_token,result_class)

        except Exception as e:
            # 捕獲所有異常並打印相關訊息
            print(f"等下什麼課出現異常：{e}")
            # print(hour)
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

    if mtext in ["breakfast","lunch","dinner"]:
        try:
            import random
            result_rest = [] #要輸出的總資料
            #breakfast *之後可以抓資料庫or爬蟲?
            breakfast_ary = ['阿如','早安有喜','歐姆薯薯','橙家'] 
            #lunch or dinner
            restaurant_ary = [
                "義大利麵","丸龜","那個那個飯","吃你想吃的","泡麵","滷味","麻辣燙","美濃","莫尼","不要甲水餃","麥當勞"
            ]
            if mtext in 'breakfast':
                result = random.choice(breakfast_ary)
                result_rest.append(TextSendMessage(text=result))

            if mtext in ['lunch','dinner']:
                result = random.choice(restaurant_ary)
                result_rest.append(TextSendMessage(text=result))

            stk_rpy = StickerSendMessage(
                type="sticker",
                package_id='8525',
                sticker_id='16581294'
            )
            result_rest.append(stk_rpy)
            linebot_api.reply_message(event.reply_token,result_rest)
            
        except Exception as e:
            # 捕獲所有異常並打印相關訊息
            print(f"午餐出現異常：{e}")
# 常用連結    
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

# if __name__ == "__main__":
#     app.run()
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)