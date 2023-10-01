import datetime
# 顯示現在時間&下一堂課

current_time = datetime.datetime.now()
week_of_day = current_time.weekday()+1
hour = str(current_time)[11]+str(current_time)[12]

print("現在時間",current_time)
print("星期",week_of_day)
# print(hour,"點")

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
if week_of_day <= 5:
    week_of_day = week_of_day;
    
    if hour in class_dict:
        print(f" 星期{week_of_day} 第{class_dict[hour]}節  {class_array[week_of_day-1][class_dict[hour]-1]}課")
        print(f"下一節是{hour}點10分{class_array[week_of_day-1][class_dict[hour]]}課")

    if int(hour) < 8:
        print("還沒上課，不要猴急")
    elif int(hour) == 12:
        print ("甲奔")
    elif int(hour) >= 18:
        print("勾home")

else:
    week_of_day = "今天放假!!";

