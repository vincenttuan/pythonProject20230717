# 人機互動(使用者輸入並計算)
# 需求 : 能夠讓使用者可以輸入自己的身高與體重
#       系統會自動計算出 BMI 值
h = float(input('請輸入身高:'))
w = float(input('請輸入體重:'))
print(h, type(h))
print(w, type(w))
# h = int(h)
# print(h, type(h))
bmi = w / (h/100)**2
print("BMI %.2f" % bmi)
# 進行 BMI 診斷
if bmi > 23:
    print("過重")
elif bmi <= 18:
    print("過輕")
else:
    print("正常")
