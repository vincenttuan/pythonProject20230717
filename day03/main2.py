# 字串分析 - 切割(split)
data = "身高=170,體重=60"
print(data)
# 請計算出 BMI = ?
array1 = data.split(",")
print(array1)
print(array1[0])
height = array1[0].split("=")
print(height)
h = int(height[1])
print("h=", h)
w = int(array1[1].split("=")[1])
print("w=", w)
bmi = w / (h/100)**2
print(bmi)
