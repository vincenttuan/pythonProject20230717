# 字串分析 - 切割(split)
data = "100,90,80,70,60"  # 學生成績資料
scores = data.split(",")
print(len(scores))
print(scores[0], type(scores[0]))
print(scores[1], type(scores[1]))
print(scores[2], type(scores[2]))
print(scores[3], type(scores[3]))
print(scores[4], type(scores[4]))
# 計算總成績
total = scores[0] + scores[1] + scores[2] + scores[3] + scores[4]
print("總成績:", total)
# 改成每一個元素必須透過 int() 來轉型
total = int(scores[0]) + int(scores[1]) + int(scores[2]) + int(scores[3]) + int(scores[4])
print("總成績:", total)
# 計算平均
average = total / len(scores)  # total / 5
print("平均:", average)


