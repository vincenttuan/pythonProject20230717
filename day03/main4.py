# 字串分析 - 切割(split)
data = "國=100,英=90,數=75.4"
# 請計算總分與平均
# 解法: scores = [100.0, 90.0, 75.4]
scores = [float(item.split("=")[1]) for item in data.split(",")]
print(scores)
total = sum(scores)
print(total)
avarage = total / len(scores)
print(avarage)
