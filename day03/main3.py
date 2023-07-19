# 字串分析 - 切割(split)
data = "國=100,英=90,數=75.4"
# 請計算總分與平均
chinese = float(data.split(",")[0].split("=")[1])
print(chinese)
english = float(data.split(",")[1].split("=")[1])
print(english)
math = float(data.split(",")[2].split("=")[1])
print(math)
total = chinese + english + math
average = total / 3
print("總分 %.1f 平均 %.1f" % (total, average))
print("總分 {0:.1f} 平均 {1:.1f}".format(total, average))

