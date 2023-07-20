# 字串分析
data = "小明本薪$65000,今年公司發放6個月,試問小明年終"
print(data)
print(data.find('$') + 1)  # 5
print(data.find(','))  # 10
print(data[5:10])
print(data[data.find('$') + 1:data.find(',')])



