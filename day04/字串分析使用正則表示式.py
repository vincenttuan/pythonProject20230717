# 字串分析使用正則表示式
import re
data = "小明本薪$65000, 今年公司發放6個月,試問小明年終"

# 利用正則表示式來匹配找到薪水與月份
# group(0) 表示整個的捕獲的結果
print(re.search(r'本薪\$([0-9]+)', data).group(0))
# group(1) 表示第一個被捕獲的結果
salary = int(re.search(r'本薪\$([0-9]+)', data).group(1))
print(salary)
bonus_months = int(re.search(r'發放([0-9]+)個月', data).group(1))
print(bonus_months)
# 計算年終
year_end_bonus = salary * bonus_months
print(f'小明的年終獎金是 : {year_end_bonus}')


