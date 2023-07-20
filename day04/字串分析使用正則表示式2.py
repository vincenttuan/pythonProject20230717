# 字串分析使用正則表示式2
import re
data = "小明所得$65000, 所得$7200, 所得$18000, 今年公司發放6個月,試問小明年終"
# 將所有所得相加後 * 發放月數
# salaries = [65000, 7200]
salaries = [int(salary) for salary in re.findall(r'所得\$([0-9]+)', data)]
print(salaries)
total_salary = sum(salaries)
print(total_salary)


