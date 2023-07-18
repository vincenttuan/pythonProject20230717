# 變數與格式化印出
name1 = "Jack"
name2 = "Rose"
age = 18
bmi = 21.7612345
# 直接印出(不格式化)
print(name1, name2, age, bmi)
print("姓名", name1, "年齡", age, "BMI值", bmi)
# 印出(格式化, %s 放字串, %d 放整數, %f 放符點數)
print("姓名 %s 年齡 %d BMI值 %.2f" % (name1, age, bmi))
# 高級印出(格式化 {}, {0}, {name})
print("姓名 {} 年齡 {} BMI值 {}".format(name1, age, bmi))
print("姓名 {} 年齡 {} BMI值 {:.2f}".format(name1, age, bmi))
print("姓名 {0} 年齡 {1} 姓名 {2} 年齡 {1}".format(name1, age, name2))

web_name = "雅虎"
web_url = "https://tw.yahoo.com"
print("網站名 {name} 網址 {url}".format(name=web_name, url=web_url))

