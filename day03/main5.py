# 字串分析 - 切割(split)
# 正則表達式
import re
data = "國=100,英=90,數:75.4"
# 解法: scores = [100.0, 90.0, 75.4]
# 利用正則表達式找出所有的數字
scores = [float(score) for score in re.findall(r'[\d\.]+', data)]
print(scores)
total = sum(scores)
print(total)
avarage = total / len(scores)
print(avarage)


