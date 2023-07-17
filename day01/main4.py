# 變數的應用
# 計算 BMI 值
# 公式 = 體重(kg) / (身高(公尺)**2)
w = 60   # 體重(kg)
h = 170  # 身高(cm)
h = h / 100  # 將身高(cm)轉公尺(m)
bmi = w / h**2  # 計算 bmi 的值
print("BMI值", bmi)
# 若只要印出小數點2位
# 透過資料格式化 %.2f
print("BMI值 %.2f" % bmi)
print("身高: %.1f 體重: %.1f bmi: %.2f" % (h, w, bmi))

