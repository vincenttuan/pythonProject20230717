import re
# 讀取: salary.txt 的內容
# 目的: 計算總薪資, 平均薪資, 最高薪資, 最低薪資
with open('salary.txt', 'r', encoding='UTF-8') as file:
    content = file.read()

pattern = re.compile(r'(\w+)\s(\d+)')
matches = pattern.findall(content)

# 計算總薪資, 平均薪資, 最高薪資, 最低薪資
total_salary = 0
total_person = 0
max_salary = 0
min_salary = float('inf')  # 無限大

for name, salary in matches:
    salary = int(salary)
    total_salary += salary
    total_person += 1
    max_salary = max(max_salary, salary)
    min_salary = min(min_salary, salary)

average_salary = total_salary / total_person

print('資料筆數:{}\n總薪資:{}\n平均薪資:{:.1f}\n最高薪資:{}\n最低薪資:{}'
      .format(total_person, total_salary, average_salary, max_salary, min_salary))




