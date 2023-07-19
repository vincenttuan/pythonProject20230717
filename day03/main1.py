# 字串分析 - 切割(split)
data = "100,90,80,70,60"  # 學生成績資料
scores = data.split(",")
print(len(scores))
print(scores[0])
print(scores[1])
print(scores[2])
print(scores[3])
print(scores[4])
# 計算總成績
sum = scores[0] + scores[1] + scores[2] + scores[3] + scores[4]
print(sum)


