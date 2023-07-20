# 字串分析
data = "小明本薪$65000,今年公司發放6個月,試問小明年終"
print(data)
print(data.find('$') + 1)  # 5
print(data.find(','))  # 10
print(data[5:10])
print(data[data.find('$') + 1:data.find(',')])
print(data[data.find('發放') + 2:data.find('個月')])
# --------------------------------------------------
salary = int(data[data.find('$') + 1:data.find(',')])
bonus_months = int(data[data.find('發放') + 2:data.find('個月')])
# 計算年終
year_end_bonus = salary * bonus_months
print('小明的年終獎金是 :', year_end_bonus)
print('小明的年終獎金是 : %d' % year_end_bonus)
print('小明的年終獎金是 : {}'.format(year_end_bonus))
print(f'小明的年終獎金是 : {year_end_bonus}')


