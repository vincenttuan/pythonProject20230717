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
